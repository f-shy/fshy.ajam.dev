# 中国科技云 数据胶囊

> cstcloud.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cstcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/cstcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 中国科技云 数据胶囊 (CSTCloud Data Capsule)

- `netdisk-pan/cstcloud-data-capsule` | fails-quota | evidence reported | binding write-gated | category academic object storage
- needs card no, phone no, ID yes, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.cstcloud.cn
- free tier: 1 GB on registration and 20 GB after identity verification: '注册赠送1G存储。需要20G和S3、WebDAV、MCP需要使用国家网络身份认证app进行认证' | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [1]
- retention: Not published. State-backed academic infrastructure, so durability is high and shutdown risk low | source: [1]
- egress: The headline property: '不限流量、不限读写次数', with zero egress charges and no request count metering. | metered: no | free allowance: unlimited | source: [1]
- identity: national-id | detail: the 国家网络身份认证 app, a national digital identity. Registration alone yields 1 GB with no identity document | country: cn
- interface: s3, webdav
- limits:
  - write-gated (binding): 20 GB and the S3, WebDAV and MCP interfaces all require the 国家网络身份认证 app [1]
  - per-object-cap: 20 GB is the account total and the per-object cap is unstated [1]
- binding note: Unlimited traffic and no request metering, and the gate is a national identity app. Only 1 GB is available without verification, so the identity decision is the only one that matters.
- tooling: first-party S3 credentials with an AccessKey from 客户端访问, plus WebDAV and MCP. A rclone S3 mounting walkthrough exists and sccache over CSTCloud is documented for Rust builds
- composes with: 20 GB per verified identity and each data space is a separate bucket, so the only multiplier is identities. The identity is 国家网络身份认证, a national digital ID app, which makes it non-multiplicable
- reliability: State-backed academic infrastructure providing high durability. Registration requires national identity verification, without which accounts remain restricted to 1 GB. Operated by CSTCloud, an institution affiliated with but administratively distinct from the Chinese Academy of Sciences.
- notes: Unlimited traffic with S3, WebDAV and MCP access, behind a national digital identity. storage/cstcloud holds the same provider for its object-storage role.
- extras:
  - access_mode: registration-gated
  - unlimited_traffic: yes
  - unlimited_request_count: yes
  - interfaces_beyond_s3: webdav; mcp
  - aliases: 中国科技云 数据胶囊 (CSTCloud Data Capsule); CSTCloud data capsule
  - cross_topic_record: storage/cstcloud
  - cross_topic_note: the storage topic carries the same provider for its object-storage role
- evidence:
  - [1] 2026-10-21: '中科院免费提供的20GB对象存储服务，不限流量、不限读写次数，支持多协议接入'
  - [2] 2026-10-21: '中科院 S3 配置, 注意现在不实名只有 1g 了, 实名才有 20g'
  - [3] 2026-10-21: an S3 and WebDAV mounting walkthrough with rclone
- sources:
  - [1] https://linux.do/t/topic/1614982
  - [2] https://linux.do/t/topic/1553784
  - [3] https://linux.do/t/topic/1793719
