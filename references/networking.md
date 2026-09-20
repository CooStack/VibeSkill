# 计算机网络与互联网

按分层、寻址路由、传输、名字解析、边缘设施和质量指标检索。来源 S58、S59、S71、S74，见 [sources.md](sources.md)；HTTP/浏览器安全沿用 [web.md](web.md)。互联网、Web 和局域网不是同义。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| NW001 | Internet; Web; Intranet; 互联网/万维网 | 网站就是互联网吗、内网外网 | 互联网连接网络，Web 是其上的应用生态，内网描述访问范围 | 不是所有联网服务都使用 HTTP 或公开可达 |
| NW002 | Protocol; Layer; Encapsulation; OSI/TCP-IP | 网络分层、封装解封 | 用协议约定及分层职责组织通信 | 参考模型层次与具体实现边界不总一一对应 |
| NW003 | Packet switching; Frame; Packet; Segment | 帧包段、网络数据单元 | 按不同协议层组织待传输的数据 | 报文长度与应用消息边界依协议层确定 |
| NW004 | Ethernet; MAC address; Switch | 交换机、二层地址 | 在链路范围内转发帧并识别接口 | MAC 不是互联网端到端的身份认证 |
| NW005 | IP; IPv4/IPv6; Address; 网络地址 | IP 地址、双栈 | 提供网络层寻址和跨网络转发 | 地址可变化，共享地址不等于同一用户 |
| NW006 | CIDR; Subnet; Prefix; 子网掩码 | 网段划分、地址前缀 | 用前缀长度表达地址范围和路由匹配 | 不能把所有网络边界仅当成安全边界 |
| NW007 | Routing; Gateway; Routing table | 跨网段不通、默认网关 | 根据目标及策略选择下一跳 | 网络可达不保证目标端口和应用可用 |
| NW008 | AS; BGP; Peering; 自治系统 | 运营商互联、跨网路由 | 在管理域之间传播可达性和路由策略 | BGP 决策不只按最短地理距离 |
| NW009 | NAT; PAT; Port forwarding | 内网服务外网访问、端口映射 | 转换地址或端口以连接不同地址域 | NAT 不是身份鉴别或完整防火墙替代 |
| NW010 | ARP; NDP; Neighbor discovery | 同网段找网卡、邻居表 | 把网络层邻居需求连接到链路交付 | IPv4 ARP 与 IPv6 NDP 不能当相同协议 |
| NW011 | DHCP; SLAAC; Address configuration | 自动获得 IP、地址冲突 | 配置地址及相关网络参数 | 租约/自动配置不保证服务地址永久稳定 |
| NW012 | TCP; Byte stream; 字节流; 粘包/拆包 | TCP 收到半条或多条消息 | TCP 提供有序字节流，应用自行定义消息边界 | 一次 send 不保证对应一次 recv，更不保证业务恰好执行一次 |
| NW013 | UDP; Datagram; 数据报 | 实时消息、允许丢包 | 保留数据报边界且不内建 TCP 式可靠流语义 | 应用可以自行提供可靠性，UDP 不等于一定更快 |
| NW014 | Port; Socket; Endpoint; 五元组 | 端口占用、监听地址 | 描述传输端点及连接关联 | 绑定回环/所有接口的暴露范围不同 |
| NW015 | Handshake; TCP state; TIME_WAIT | 建连关闭、连接状态堆积 | 按协议状态建立、维护及结束连接 | 不应未经测量随意缩短状态保护时间 |
| NW016 | ACK; Sequence number; Retransmission | 重传、确认、重复数据 | 用序号和确认协调可靠传输 | 传输确认不表示应用已持久提交业务 |
| NW017 | Flow control; Congestion control | 发送太快、网络拥塞 | 分别保护接收端容量和网络路径承载 | 限制网络发送不能代替业务排队容量控制 |
| NW018 | RTT; Latency; Jitter; Loss | 延迟高、抖动、丢包 | 区分往返时间、变化程度和未到达数据比例 | 带宽大不代表延迟低，平均值可能掩盖尖峰 |
| NW019 | Bandwidth; Throughput; Goodput | 网速、有效业务吞吐 | 区分链路能力、实际传输量与有效负载量 | 单位、协议开销和测量窗口需一致 |
| NW020 | MTU; MSS; Fragmentation; PMTUD | 大包不通、小包正常 | 路径和协议限制影响分段或分片 | 禁用相关控制消息可能破坏路径 MTU 发现 |
| NW021 | DNS; Recursive resolver; Authoritative server | 域名解析错、递归权威 | 分工完成名字查询、权威回答和缓存 | 解析结果不是应用可用性检测；详见 WB002 |
| NW022 | DNS record; A/AAAA/CNAME/MX/TXT | 域名记录、别名、邮件路由 | 用记录类型表达不同服务信息 | CNAME 是名字别名，不是 HTTP 重定向 |
| NW023 | DNS TTL; Negative cache | 改解析后还访问旧地址 | 缓存寿命和否定回答缓存影响可见更新 | 修改配置不保证全网所有缓存瞬时刷新 |
| NW024 | TLS; Certificate chain; SNI; ALPN | 握手失败、证书链、协议协商 | 加密连接中认证端点并选择相关协议上下文 | 证书有效不证明网站业务可信，不能关闭验证当修复 |
| NW025 | QUIC; Connection ID; Multiplexed streams | HTTP/3、移动网络切换 | 基于 UDP 提供安全连接及独立流等传输能力 | 不是简单“UDP 版 HTTP”；应用协议另行定义 |
| NW026 | HTTP/1.1; HTTP/2; HTTP/3; HOL blocking | 多路复用、队头阻塞 | 不同 HTTP 版本及传输方式影响并发等待 | HTTP/2 仍可能受 TCP 连接级丢包等待影响 |
| NW027 | Forward/Reverse proxy; L4/L7 load balancer | 代理、网关、负载分流 | 按代理方向与协议层分担或中介流量 | 转发头可信范围、真实客户端地址和超时需明确 |
| NW028 | CDN; Anycast; Edge; 边缘节点 | 就近访问、全球分发 | 用节点布局和路由/缓存组织接近用户的服务 | 就近不一定是地理最近，缓存策略见 WB012 |
| NW029 | VPN; Tunnel; Overlay network | 虚拟内网、隧道封装 | 在底层连接之上提供逻辑链路或网络 | 使用隧道不自动可信或匿名，需授权和访问控制 |
| NW030 | Firewall; ACL; Security group | 连不上端口、网络访问规则 | 用策略限制网络流量 | 放行端口不等于应用授权，方向与状态规则需核对 |
| NW031 | Keepalive; Heartbeat; Idle timeout | 长连接断开、心跳检测 | 区分传输探测、业务健康探测和空闲回收 | 心跳正常不保证所有业务功能健康 |
| NW032 | NAT traversal; STUN; TURN; ICE | P2P 建连失败、实时通话中继 | 探测连接候选并在必要时使用中继 | 不能保证任意网络下都可直接点对点连接 |
| NW033 | Packet capture; Traceroute; Network diagnosis | 抓包、链路哪里不通 | 按授权观察协议交换与路径迹象 | 未响应探测不必代表实际应用流量失败；注意隐私 |
| NW034 | ISP; IXP; Registrar; Registry | 运营商、交换点、域名注册商 | 区分接入、互联及域名登记管理角色 | 域名注册、DNS 托管、网站托管可由不同主体提供 |
| NW035 | Email protocol; SMTP; IMAP; SPF/DKIM/DMARC | 发信、收信、邮件鉴别 | 分别处理投递、邮箱访问及域名邮件鉴别策略 | SPF 通过不等于邮件内容安全或必定入收件箱 |
| NW036 | URI; URL; IDN; Punycode | 国际化域名、地址编码 | 区分资源标识与域名国际化表示 | 相似字符域名不保证同一来源，URL 编码不是加密 |
