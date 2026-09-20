"""CLI for the local, project-filtered personal knowledge library."""

import argparse
import json
from pathlib import Path
import sys

from user_knowledge import (
    delete_user_concept, get_user_concept, initialize_knowledge,
    load_user_concepts, parse_input, save_concept,
)


def parser():
    result = argparse.ArgumentParser(
        description="Personal concept CRUD. No network, execution of input, or source verification.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Create: --file concept.json OR --stdin
Update: --update UK-<32 lowercase hex digits> with --file/--stdin (partial patch)
Read:   --list OR --get ID; includes globals and selected project only
Delete: --delete ID; permanent single-record deletion, no trash
Init:   --init; preserve catalog, repair views, prune orphan strict-ID reader files

JSON schema:
  Required on create: title: str, definition: str
  Optional: aliases: [str], cues: str, boundary: str, domain: str (default user),
    origin: str (default user), scope: project|global (default project),
    project: str (default --project/cwd; global must omit or null),
    verification: user_defined|unverified|source_checked (default unverified),
    sources: [str], identity: existing UK ID (assertion, not implicit update),
    recipe: {intent: str, principles: [str], implementation: [str],
             checks: [str], pitfalls: [str]} (exact fields, nonempty arrays).
  Updates preserve omitted fields and cannot move scope/project or change ID.
  source_checked needs sources; it is your assertion, not script verification.
  Editing a checked entry without reasserting verification downgrades it.
  Duplicate normalized title + scope + project returns the existing entry.
  Unknown fields rejected. Supply distilled knowledge, never chats or secrets.

Root: VIBESKILL_KNOWLEDGE_HOME overrides home/VibeSkill
      (Windows uses USERPROFILE when set). No extra knowledge subdirectory.
Module APIs: knowledge_root, load_user_concepts, initialize_knowledge,
            save_concept, get_user_concept, delete_user_concept.
""",
    )
    actions = result.add_mutually_exclusive_group()
    actions.add_argument("--init", action="store_true", help="initialize or repair local library")
    actions.add_argument("--list", action="store_true", help="list visible records as JSON")
    actions.add_argument("--get", metavar="ID", help="read one visible record")
    actions.add_argument("--delete", metavar="ID", help="permanently delete one visible record")
    actions.add_argument("--update", metavar="ID", help="explicitly patch one visible record")
    inputs = result.add_mutually_exclusive_group()
    inputs.add_argument("--file", type=Path, help="read concept JSON from this file")
    inputs.add_argument("--stdin", action="store_true", help="read concept JSON from stdin")
    result.add_argument("--project", help="project path for scope/filter; defaults to cwd")
    return result


def main(argv=None):
    arguments = parser()
    args = arguments.parse_args(argv)
    has_input = args.file is not None or args.stdin
    readonly_or_init = args.init or args.list or args.get is not None or args.delete is not None
    if readonly_or_init and has_input:
        arguments.error("--init/--list/--get/--delete cannot be combined with input")
    if args.update is not None and not has_input:
        arguments.error("--update requires --file or --stdin")
    if not readonly_or_init and args.update is None and not has_input:
        arguments.error("choose --init, --list, --get, --delete or JSON input")
    source = str(args.file.resolve()) if args.file is not None else "<stdin>"
    try:
        if args.init:
            output = {"root": str(initialize_knowledge()), "operation": "initialized"}
        elif args.list:
            output = load_user_concepts(project=args.project)
        elif args.get is not None:
            output = get_user_concept(args.get, project=args.project)
        elif args.delete is not None:
            record = delete_user_concept(args.delete, project=args.project)
            output = {"deleted": record["id"], "permanent": True, "trash": False}
        else:
            text = args.file.read_text(encoding="utf-8") if args.file is not None else sys.stdin.read()
            payload = parse_input(text, source)
            try:
                output = save_concept(payload, project=args.project, update_id=args.update)
            except ValueError as error:
                raise ValueError(f"{source}: {error}") from error
        print(json.dumps(output, ensure_ascii=True, indent=2))
    except (ValueError, KeyError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    raise SystemExit(main())
