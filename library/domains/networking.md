# 计算机网络与互联网

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [NW001 · Internet; Web; Intranet; 互联网/万维网](../concepts/NW001.md) | 网站就是互联网吗、内网外网 |
| [NW002 · Protocol; Layer; Encapsulation; OSI/TCP-IP](../concepts/NW002.md) | 网络分层、封装解封 |
| [NW003 · Packet switching; Frame; Packet; Segment](../concepts/NW003.md) | 帧包段、网络数据单元 |
| [NW004 · Ethernet; MAC address; Switch](../concepts/NW004.md) | 交换机、二层地址 |
| [NW005 · IP; IPv4/IPv6; Address; 网络地址](../concepts/NW005.md) | IP 地址、双栈 |
| [NW006 · CIDR; Subnet; Prefix; 子网掩码](../concepts/NW006.md) | 网段划分、地址前缀 |
| [NW007 · Routing; Gateway; Routing table](../concepts/NW007.md) | 跨网段不通、默认网关 |
| [NW008 · AS; BGP; Peering; 自治系统](../concepts/NW008.md) | 运营商互联、跨网路由 |
| [NW009 · NAT; PAT; Port forwarding](../concepts/NW009.md) | 内网服务外网访问、端口映射 |
| [NW010 · ARP; NDP; Neighbor discovery](../concepts/NW010.md) | 同网段找网卡、邻居表 |
| [NW011 · DHCP; SLAAC; Address configuration](../concepts/NW011.md) | 自动获得 IP、地址冲突 |
| [NW012 · TCP; Byte stream; 字节流; 粘包/拆包](../concepts/NW012.md) | TCP 收到半条或多条消息 |
| [NW013 · UDP; Datagram; 数据报](../concepts/NW013.md) | 实时消息、允许丢包 |
| [NW014 · Port; Socket; Endpoint; 五元组](../concepts/NW014.md) | 端口占用、监听地址 |
| [NW015 · Handshake; TCP state; TIME_WAIT](../concepts/NW015.md) | 建连关闭、连接状态堆积 |
| [NW016 · ACK; Sequence number; Retransmission](../concepts/NW016.md) | 重传、确认、重复数据 |
| [NW017 · Flow control; Congestion control](../concepts/NW017.md) | 发送太快、网络拥塞 |
| [NW018 · RTT; Latency; Jitter; Loss](../concepts/NW018.md) | 延迟高、抖动、丢包 |
| [NW019 · Bandwidth; Throughput; Goodput](../concepts/NW019.md) | 网速、有效业务吞吐 |
| [NW020 · MTU; MSS; Fragmentation; PMTUD](../concepts/NW020.md) | 大包不通、小包正常 |
| [NW021 · DNS; Recursive resolver; Authoritative server](../concepts/NW021.md) | 域名解析错、递归权威 |
| [NW022 · DNS record; A/AAAA/CNAME/MX/TXT](../concepts/NW022.md) | 域名记录、别名、邮件路由 |
| [NW023 · DNS TTL; Negative cache](../concepts/NW023.md) | 改解析后还访问旧地址 |
| [NW024 · TLS; Certificate chain; SNI; ALPN](../concepts/NW024.md) | 握手失败、证书链、协议协商 |
| [NW025 · QUIC; Connection ID; Multiplexed streams](../concepts/NW025.md) | HTTP/3、移动网络切换 |
| [NW026 · HTTP/1.1; HTTP/2; HTTP/3; HOL blocking](../concepts/NW026.md) | 多路复用、队头阻塞 |
| [NW027 · Forward/Reverse proxy; L4/L7 load balancer](../concepts/NW027.md) | 代理、网关、负载分流 |
| [NW028 · CDN; Anycast; Edge; 边缘节点](../concepts/NW028.md) | 就近访问、全球分发 |
| [NW029 · VPN; Tunnel; Overlay network](../concepts/NW029.md) | 虚拟内网、隧道封装 |
| [NW030 · Firewall; ACL; Security group](../concepts/NW030.md) | 连不上端口、网络访问规则 |
| [NW031 · Keepalive; Heartbeat; Idle timeout](../concepts/NW031.md) | 长连接断开、心跳检测 |
| [NW032 · NAT traversal; STUN; TURN; ICE](../concepts/NW032.md) | P2P 建连失败、实时通话中继 |
| [NW033 · Packet capture; Traceroute; Network diagnosis](../concepts/NW033.md) | 抓包、链路哪里不通 |
| [NW034 · ISP; IXP; Registrar; Registry](../concepts/NW034.md) | 运营商、交换点、域名注册商 |
| [NW035 · Email protocol; SMTP; IMAP; SPF/DKIM/DMARC](../concepts/NW035.md) | 发信、收信、邮件鉴别 |
| [NW036 · URI; URL; IDN; Punycode](../concepts/NW036.md) | 国际化域名、地址编码 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为网络领域基线，将协议与连接概念落实为分层故障定位、消息边界和端到端行为。

### 关键特征

- 区分名称解析、建连、传输、协议处理与业务响应，不用单一超时描述所有阶段。
- 连接成功、字节送达和业务完成是不同证据。
- 重试、超时与连接复用服从实际协议和副作用语义，不默认追加代理或更换协议。

### 如何落实

- 列出通信双方、地址来源、实际路径及相关协议，明确本次失败或延迟所在阶段。
- 定义消息编码、边界、长度和错误处理，区分部分输入、完整消息及连接关闭。
- 根据调用契约安排超时、取消和重试范围，若可能重发有副作用的请求则明确重复处理方式。
- 用现有日志或受控流量观测关联两端事件，采集必要信息时避免记录凭据与无关内容。

### 如何验收

- 分别模拟解析失败、建连失败和响应延迟，确认诊断与用户可见错误能够区分阶段。
- 在传输方式允许的情况下拆分或合并输入片段，验证消息解析不依赖单次读取边界。
- 中断连接并恢复，核对未完成请求、重试副作用和连接资源的最终状态。

### 常见误用

- 把本机连通或一次探测成功当作完整应用协议可用。
- 对所有网络错误无限重试，忽略重复副作用和故障期间的负载放大。
