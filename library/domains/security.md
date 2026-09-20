# 安全与密码学

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [SE001 · Threat modeling; 威胁建模](../concepts/SE001.md) | 不知道保护什么、信任边界 |
| [SE002 · CIA triad; 机密性完整性可用性](../concepts/SE002.md) | 防泄露、防篡改、不能停机 |
| [SE003 · Authentication vs Authorization; 认证与授权](../concepts/SE003.md) | 登录了却能看别人数据 |
| [SE004 · Least privilege; 最小权限](../concepts/SE004.md) | 服务权限太大、临时凭证 |
| [SE005 · Trust boundary; Attack surface; 信任边界](../concepts/SE005.md) | 外部输入进入内部系统 |
| [SE006 · Hash; Digest; Cryptographic hash](../concepts/SE006.md) | 文件指纹、完整性校验 |
| [SE007 · Password hashing; Salt; KDF](../concepts/SE007.md) | 密码数据库泄露、密码存储 |
| [SE008 · Symmetric encryption; 对称加密](../concepts/SE008.md) | 大量数据保密 |
| [SE009 · Public-key cryptography; 非对称密码](../concepts/SE009.md) | 公钥私钥、密钥协商 |
| [SE010 · AEAD; Authenticated encryption](../concepts/SE010.md) | 密文也要防改、认证标签 |
| [SE011 · MAC; HMAC; 消息认证码](../concepts/SE011.md) | 消息防篡改、共享密钥校验 |
| [SE012 · Digital signature; 数字签名](../concepts/SE012.md) | 发布包验签、证明来源 |
| [SE013 · PKI; Certificate chain; 公钥基础设施](../concepts/SE013.md) | 证书不受信、证书链 |
| [SE014 · CSPRNG; Secure randomness](../concepts/SE014.md) | token 被猜到、随机密钥 |
| [SE015 · Injection; Parameterization; 注入与参数化](../concepts/SE015.md) | SQL 拼接、命令注入 |
| [SE016 · XSS; Contextual escaping; 跨站脚本](../concepts/SE016.md) | 评论里脚本执行、HTML 拼接 |
| [SE017 · CSRF; 跨站请求伪造](../concepts/SE017.md) | 登录态被跨站利用 |
| [SE018 · SSRF; 服务端请求伪造](../concepts/SE018.md) | 用户 URL 让服务器访问内网 |
| [SE019 · IDOR; BOLA; 对象级越权](../concepts/SE019.md) | 改订单 ID 看到别人订单 |
| [SE020 · TOCTOU; Check-use race](../concepts/SE020.md) | 检查文件后被替换 |
| [SE021 · Supply-chain security; SBOM](../concepts/SE021.md) | 依赖投毒、软件成分清单 |
| [SE022 · Secret management; 密钥管理](../concepts/SE022.md) | token 写进仓库、凭证轮换 |
| [SE023 · Sandbox; Defense in depth](../concepts/SE023.md) | 运行不可信插件、隔离执行 |
| [SE024 · Side channel; Timing attack; 侧信道](../concepts/SE024.md) | 耗时泄露秘密、缓存侧信道 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为安全领域基线，将防护概念落实为具体资产、信任边界和允许或拒绝的行为；不凭检查清单声称系统已安全。

### 关键特征

- 从本次资产、入口和攻击者能力确定威胁范围，不泛化为全面改造。
- 身份确认、操作授权和数据校验分别承担责任，客户端声明不能替代服务端信任判断。
- 沿用经过项目认可的安全设施，具体算法、参数与标准要求另行核对，不自创协议。

### 如何落实

- 列出涉及的敏感数据、可执行动作和跨越的信任边界，标明输入由谁控制。
- 在实际执行动作的边界校验身份、资源归属和输入约束，明确拒绝时不得发生的副作用。
- 沿既有机制处理密钥、会话和敏感配置，限制日志内容及任务涉及资源的访问范围。
- 构造与当前威胁对应的滥用案例，在授权的隔离环境验证，并记录未覆盖的边界。

### 如何验收

- 用不同身份与资源组合验证允许和拒绝矩阵，确认拒绝不能通过替换标识绕过。
- 输入畸形、超长或带特殊语义的数据，核对解析及执行边界没有将其当作指令。
- 检查错误、日志与产物中是否暴露敏感内容，确认凭据失效或权限撤回路径符合既定要求。

### 常见误用

- 只验证正常用户路径，或把隐藏按钮当作操作授权。
- 以加密、扫描通过或脱敏标签替代具体威胁验证，并作全面安全承诺。
