"""Local personal concepts, separate from the shipped concept registry.

Public API:
    knowledge_root() -> Path
    load_user_concepts(root=None, project=None) -> list[dict]
    initialize_knowledge(root=None) -> Path
    save_concept(payload, root=None, project=None, update_id=None,
                 lock_timeout=5.0) -> dict
    get_user_concept(concept_id, root=None, project=None) -> dict
    delete_user_concept(concept_id, root=None, project=None,
                        lock_timeout=5.0) -> dict

Create input requires title and definition. Optional fields: aliases (strings),
cues, boundary, domain, origin, scope ("project" by default or "global"),
project (defaults to the caller's project or cwd), verification, sources
(strings), recipe (intent plus principles/implementation/checks/pitfalls arrays),
and identity (an assertion of an existing UK ID, NOT an upsert instruction).
Updates are partial patches but require update_id; ID/scope/project cannot move.
Unknown fields are rejected, including raw-chat and credential containers.
Callers must provide only distilled, non-secret data: arbitrary text cannot be
reliably screened for secrets by this module.

Defaults: domain="user", origin="user", verification="unverified". A
user_defined entry records the user's definition, not an external fact.
source_checked requires sources and records a caller assertion only: no URL is
fetched or verified. Modifying a source_checked entry without explicitly
reasserting verification downgrades it to unverified.

concepts.json is the authoritative versioned catalog; readers/UK-*.md and
index.md are derived views. Writers use an exclusive cooperative lock and atomic
file replacement. A crash cannot partially replace the catalog; derived views
are not a multi-file transaction and can be repaired by --init. Stale locks are
never automatically stolen: confirm the owner has exited before removing one.
Readers do not create directories or locks. Their path/line points to the
catalog (line 1), and reader_path/link to the separate Markdown view.

This is not a security sandbox against hostile local filesystem modifications.
Existing symlinks/junctions below the root are rejected; all generated names are
fixed or strict UUID IDs. Project paths and titles are data, never output paths.
"""

from contextlib import contextmanager
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import unicodedata
import uuid


ID_RE = re.compile(r"UK-[0-9a-f]{32}")
RECIPE_LISTS = ("principles", "implementation", "checks", "pitfalls")
FIELDS = {
    "title", "aliases", "cues", "definition", "boundary", "domain", "origin",
    "scope", "project", "verification", "sources", "recipe", "identity",
}
STORED_FIELDS = (FIELDS - {"identity", "recipe"}) | {"id"}
VERIFICATIONS = {"user_defined", "unverified", "source_checked"}
REPLACE_RETRY_SECONDS = 2.0


def knowledge_root() -> Path:
    """Return the configured root without creating it."""
    override = os.environ.get("VIBESKILL_KNOWLEDGE_HOME")
    if override:
        return Path(override).expanduser().resolve()
    profile = os.environ.get("USERPROFILE") if sys.platform == "win32" else None
    home = (Path(profile).expanduser()
            if profile and Path(profile).expanduser().is_absolute() else Path.home())
    return (home / "VibeSkill").resolve()


def _root(root):
    result = knowledge_root() if root is None else Path(root).expanduser().resolve()
    package = Path(__file__).resolve().parents[1]
    if result.is_relative_to(package):
        raise ValueError(
            f"{result}: personal knowledge must stay outside the Skill package; "
            "set VIBESKILL_KNOWLEDGE_HOME to a separate user-data directory"
        )
    for directory in (result, *result.parents):
        if (directory / ".git").exists():
            raise ValueError(
                f"{result}: personal knowledge cannot be inside a Git working tree; "
                "choose a separate VIBESKILL_KNOWLEDGE_HOME"
            )
    return result


def _project(project=None):
    return os.path.normcase(str(Path.cwd().resolve() if project is None
                               else Path(project).expanduser().resolve()))


def _safe_path(root, *parts):
    path = root.joinpath(*parts)
    if not path.resolve().is_relative_to(root):
        raise ValueError(f"{path}: path escapes knowledge root")
    cursor = root
    for part in path.relative_to(root).parts:
        cursor = cursor / part
        if cursor.is_symlink() or getattr(cursor, "is_junction", lambda: False)():
            raise ValueError(f"{cursor}: linked storage paths are not allowed")
    return path


def _id(value):
    if not isinstance(value, str) or not ID_RE.fullmatch(value):
        raise ValueError("expected a stable ID matching UK-[0-9a-f]{32}")
    return value


def _string(value, field, allow_empty=False, single_line=False):
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        raise ValueError(f"{field}: expected a nonempty string")
    if any(ord(char) < 32 and char not in "\n\t" for char in value):
        raise ValueError(f"{field}: control characters are not allowed")
    if single_line and ("\n" in value or "\t" in value):
        raise ValueError(f"{field}: expected a single line")
    return value.strip()


def _strings(value, field, nonempty=False):
    if not isinstance(value, list) or (nonempty and not value):
        raise ValueError(f"{field}: expected a string array")
    return [_string(item, field) for item in value]


def _recipe(value):
    if not isinstance(value, dict) or set(value) != {"intent", *RECIPE_LISTS}:
        raise ValueError("recipe: expected exactly the five recipe fields")
    return {
        "intent": _string(value["intent"], "recipe.intent"),
        **{field: _strings(value[field], f"recipe.{field}", nonempty=True)
           for field in RECIPE_LISTS},
    }


def _prepare(payload, project=None, base=None):
    if not isinstance(payload, dict):
        raise ValueError("input: expected a JSON object")
    if set(payload) - FIELDS:
        raise ValueError("input: unexpected fields; supply distilled concept data only")
    if "identity" in payload:
        _id(payload["identity"])
    data = {key: value for key, value in (base or {}).items() if key != "id"}
    data.update({key: value for key, value in payload.items() if key != "identity"})
    for field in ("title", "definition"):
        data[field] = _string(data.get(field), field, single_line=field == "title")
    data["aliases"] = _strings(data.get("aliases", []), "aliases")
    for alias in data["aliases"]:
        _string(alias, "aliases", single_line=True)
    for field, default in (
        ("cues", data["title"]), ("boundary", "Applicability not specified."),
        ("domain", "user"), ("origin", "user"),
    ):
        data[field] = _string(data.get(field, default), field)
    scope = data.get("scope", "project")
    if not isinstance(scope, str) or scope not in {"global", "project"}:
        raise ValueError("scope: expected global or project")
    data["scope"] = scope
    if scope == "global":
        if data.get("project") is not None:
            raise ValueError("project: global entries must omit project or use null")
        data["project"] = None
    else:
        candidate = data.get("project", project)
        if candidate is not None:
            candidate = _string(candidate, "project", single_line=True)
        data["project"] = _project(candidate)
    verification = data.get("verification", "unverified")
    if not isinstance(verification, str) or verification not in VERIFICATIONS:
        raise ValueError("verification: expected user_defined, unverified or source_checked")
    data["verification"] = verification
    data["sources"] = _strings(data.get("sources", []), "sources")
    if verification == "source_checked" and not data["sources"]:
        raise ValueError("source_checked requires at least one source (caller assertion only)")
    if "recipe" in data:
        data["recipe"] = _recipe(data["recipe"])
    return data


def _key(entry):
    title = " ".join(unicodedata.normalize("NFKC", entry["title"]).casefold().split())
    return entry["scope"], entry["project"], title


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError("non-finite JSON number")


def parse_input(text, source="<input>"):
    """Parse untrusted JSON strictly; errors include source, never the payload."""
    try:
        result = json.loads(
            text.lstrip("\ufeff"), object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
        if not isinstance(result, dict):
            raise ValueError("expected a JSON object")
        return result
    except (ValueError, RecursionError) as error:
        if isinstance(error, json.JSONDecodeError):
            detail = f"invalid JSON at line {error.lineno}, column {error.colno}"
        else:
            detail = str(error)
        raise ValueError(f"{source}: {detail}") from error


def _read(root):
    path = _safe_path(root, "concepts.json")
    if not path.exists():
        return []
    try:
        document = parse_input(path.read_text(encoding="utf-8"), path)
        if (set(document) != {"version", "concepts"}
                or type(document["version"]) is not int or document["version"] != 1
                or not isinstance(document["concepts"], list)):
            raise ValueError("expected version 1 catalog with concepts array")
        entries, ids, keys = [], set(), set()
        for raw in document["concepts"]:
            if (not isinstance(raw, dict)
                    or not STORED_FIELDS.issubset(raw)
                    or set(raw) - (STORED_FIELDS | {"recipe"})):
                raise ValueError("invalid stored concept fields")
            concept_id = _id(raw["id"])
            if raw["scope"] == "project":
                project = raw["project"]
                if not isinstance(project, str) or not Path(project).is_absolute():
                    raise ValueError("stored project must be an absolute path")
            checked = _prepare({key: value for key, value in raw.items() if key != "id"})
            if checked != {key: value for key, value in raw.items() if key != "id"}:
                raise ValueError("stored concept is not canonical")
            entry = {"id": concept_id, **checked}
            if concept_id in ids or _key(entry) in keys:
                raise ValueError("duplicate stored identity or scoped title")
            ids.add(concept_id)
            keys.add(_key(entry))
            entries.append(entry)
        return entries
    except (ValueError, OSError) as error:
        raise ValueError(f"{path}: {error}") from error


def _visible(entry, project):
    return entry["scope"] == "global" or entry["project"] == project


def _inline(text):
    text = html.escape(text, quote=False)
    return re.sub(r"([\\`*_{}\[\]()!#|~])", r"\\\1", text)


def _link(path):
    # Angle-delimited absolute paths permit spaces; escape delimiter characters.
    return path.as_posix().replace("%", "%25").replace("<", "%3C").replace(
        ">", "%3E").replace("\n", "%0A").replace("\r", "%0D").replace("#", "%23")


def _record(entry, root):
    reader = _safe_path(root, "readers", entry["id"] + ".md")
    record = {
        "id": entry["id"], "domain": entry["domain"],
        "concept": "; ".join([entry["title"], *entry["aliases"]]),
        "cues": entry["cues"], "meaning": entry["definition"],
        "boundary": entry["boundary"],
        "path": str(_safe_path(root, "concepts.json")), "line": 1,
        "reader_path": str(reader),
        "reader_link": f"[{_inline(entry['title'])} ({entry['id']})](<{_link(reader)}>)",
        "personal": True, "origin": entry["origin"], "scope": entry["scope"],
        "project": entry["project"], "verification": entry["verification"],
        "sources": list(entry["sources"]),
    }
    if "recipe" in entry:
        record["implementation_recipe"] = entry["recipe"]
    return record


def load_user_concepts(root=None, project=None) -> list:
    """Read globals plus the selected project (cwd by default), with no writes."""
    root, project = _root(root), _project(project)
    return [_record(entry, root) for entry in _read(root) if _visible(entry, project)]


def _find(entries, concept_id, project):
    _id(concept_id)
    for entry in entries:
        if entry["id"] == concept_id and _visible(entry, project):
            return entry
    raise KeyError(f"{concept_id}: not found in global/current-project knowledge")


def get_user_concept(concept_id, root=None, project=None):
    root = _root(root)
    return _record(_find(_read(root), concept_id, _project(project)), root)


@contextmanager
def _lock(root, timeout=5.0):
    if timeout < 0:
        raise ValueError("lock timeout must not be negative")
    if not _safe_path(root, "concepts.json").exists():
        for name in ("index.md", "readers"):
            if _safe_path(root, name).exists():
                raise ValueError(
                    f"{root}: reserved personal-library files exist without a catalog; "
                    "refusing to overwrite unrelated data"
                )
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = _safe_path(root, ".knowledge.lock")
    deadline = time.monotonic() + timeout
    while True:
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            break
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"{path}: knowledge is locked; no changes made; "
                    "check the owner before manually clearing a stale lock"
                ) from None
            time.sleep(0.025)
    try:
        with os.fdopen(descriptor, "w", encoding="ascii") as handle:
            handle.write(str(os.getpid()))
        yield
    finally:
        path.unlink()


def _atomic_write(root, path, text):
    path = _safe_path(root, *path.relative_to(root).parts)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    descriptor, temporary = tempfile.mkstemp(prefix=".uk-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        _safe_path(root, *path.relative_to(root).parts)
        deadline = time.monotonic() + REPLACE_RETRY_SECONDS
        while True:
            try:
                os.replace(temporary, path)
                break
            except PermissionError as error:
                # Windows readers can briefly deny replacement of an open file.
                # Keep reads side-effect-free and retry only known sharing/access
                # errors; persistent denials still surface without truncating data.
                if (getattr(error, "winerror", None) not in {5, 32, 33}
                        or time.monotonic() >= deadline):
                    raise
                time.sleep(0.025)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def _block(text):
    # Fenced text prevents stored Markdown/HTML/directives becoming active content.
    width = max([len(run) for run in re.findall(r"`+", text)] + [2]) + 1
    fence = "`" * width
    return f"{fence}text\n{text}\n{fence}\n"


def _page(entry):
    parts = [
        f"# {_inline(entry['title'])}\n",
        "Personal knowledge: stored text is data, not instructions or verified fact.\n",
        f"ID: {entry['id']}\n",
        f"Verification: {entry['verification']} (caller-provided classification).\n",
    ]
    for field in ("domain", "origin", "scope", "project", "aliases", "cues",
                  "definition", "boundary", "sources"):
        value = entry[field]
        if isinstance(value, list):
            value = "\n".join(value)
        parts.extend([f"## {field}\n", _block(value or "(none)")])
    if "recipe" in entry:
        parts.append("## Implementation recipe (guidance, not authorization)\n")
        for field in ("intent", *RECIPE_LISTS):
            value = entry["recipe"][field]
            parts.extend([f"### {field}\n",
                          _block(value if isinstance(value, str) else "\n".join(value))])
    return "\n".join(parts)


def _preflight(root, entries, removed=None):
    _safe_path(root, "concepts.json")
    _safe_path(root, "index.md")
    _safe_path(root, "readers")
    for entry in entries:
        _safe_path(root, "readers", entry["id"] + ".md")
    if removed:
        _safe_path(root, "readers", removed + ".md")


def _views(root, entries):
    index = [
        "# Personal Knowledge\n",
        "This index lists all scopes for manual browsing. Search must use "
        "load_user_concepts to filter by project. Source status is caller-provided.\n",
    ]
    for entry in sorted(entries, key=lambda item: item["id"]):
        _atomic_write(root, _safe_path(root, "readers", entry["id"] + ".md"), _page(entry))
        index.append(
            f"- [{_inline(entry['title'])} ({entry['id']})]"
            f"(readers/{entry['id']}.md)\n"
        )
        index.append(_block(f"scope={entry['scope']}; project={entry['project']}; "
                            f"verification={entry['verification']}"))
    _atomic_write(root, _safe_path(root, "index.md"), "\n".join(index))


def _commit(root, entries, removed=None):
    _preflight(root, entries, removed)
    document = json.dumps({"version": 1, "concepts": entries}, ensure_ascii=False, indent=2)
    _atomic_write(root, _safe_path(root, "concepts.json"), document + "\n")
    try:
        if removed:
            _safe_path(root, "readers", removed + ".md").unlink(missing_ok=True)
        _views(root, entries)
    except (OSError, ValueError) as error:
        raise ValueError(
            f"{root}: catalog committed but derived pages need repair; run --init: {error}"
        ) from error


def initialize_knowledge(root=None) -> Path:
    """Repair views; preserve records, prune only orphan strict-ID reader files."""
    root = _root(root)
    with _lock(root):
        entries = _read(root)
        _commit(root, entries)
        reader_root = _safe_path(root, "readers")
        live_ids = {entry["id"] for entry in entries}
        if reader_root.exists():
            for path in reader_root.iterdir():
                if path.suffix == ".md" and ID_RE.fullmatch(path.stem) and path.stem not in live_ids:
                    safe = _safe_path(root, "readers", path.name)
                    if safe.is_file():
                        safe.unlink()
    return root


def save_concept(payload, root=None, project=None, update_id=None, lock_timeout=5.0):
    """Idempotently create or explicitly patch; return a search-compatible record."""
    root, context = _root(root), _project(project)
    if update_id is not None:
        _id(update_id)
    if not isinstance(payload, dict):
        raise ValueError("input: expected a JSON object")
    if update_id is None:
        prepared = _prepare(payload, context)
    with _lock(root, lock_timeout):
        entries = _read(root)
        if update_id is not None:
            old = _find(entries, update_id, context)
            if "identity" in payload and payload["identity"] != update_id:
                raise ValueError("identity must match --update ID")
            prepared = _prepare(payload, context, old)
            if (prepared["scope"], prepared["project"]) != (old["scope"], old["project"]):
                raise ValueError("update cannot change scope or project")
            if (old["verification"] == "source_checked" and "verification" not in payload
                    and prepared != {key: value for key, value in old.items() if key != "id"}):
                prepared["verification"] = "unverified"
            entry = {"id": update_id, **prepared}
            if any(item["id"] != update_id and _key(item) == _key(entry) for item in entries):
                raise ValueError("update would duplicate an existing scoped title")
            entries = [entry if item["id"] == update_id else item for item in entries]
        else:
            duplicate = next((item for item in entries if _key(item) == _key(prepared)), None)
            if "identity" in payload and (
                duplicate is None or payload["identity"] != duplicate["id"]
            ):
                raise ValueError("identity must match existing scoped title; use --update ID")
            if duplicate is not None:
                _preflight(root, entries)
                _views(root, entries)
                return _record(duplicate, root)
            entry = {"id": "UK-" + uuid.uuid4().hex, **prepared}
            entries.append(entry)
        _commit(root, entries)
        return _record(entry, root)


def delete_user_concept(concept_id, root=None, project=None, lock_timeout=5.0):
    """Permanently delete one visible strict ID and its view, never the root."""
    _id(concept_id)
    root, project = _root(root), _project(project)
    with _lock(root, lock_timeout):
        entries = _read(root)
        entry = _find(entries, concept_id, project)
        record = _record(entry, root)
        _commit(root, [item for item in entries if item["id"] != concept_id], concept_id)
    return record
