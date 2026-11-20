# CloudDrive2

> clouddrive2.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clouddrive2/ | JSON https://fshy.ajam.dev/api/v1/entity/clouddrive2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudDrive2

- `debrid/clouddrive2` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category cloud-drive mount + cross-cloud transfer licence | tier 核心会员
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:56:12.307Z (live) | stale on 2026-11-23
- url http://www.clouddrive2.com/pricing.html
- price CNY 4.99/month; CNY 49.99/year; CNY 499 lifetime | parsed USD 0.7481/mo
- free tier: 基础会员 free: 最多 2 个云盘, 最多 1 个本地挂载, 2 devices, no core Pro features. '传输不限速' is listed as available even on the free tier. | unit: mixed | metered on: object-count | read on: 2026-10-23 | source: [1] | note: The free tier is counted in connected drives and mounts, not bytes.
- per-object cap: Encrypted upload is capped at 200 MB per file on every tier except 核心终身版; the cloud drive's own per-file cap still applies beneath it. | source: [1]
- retention: Not applicable: it is a mount and a transfer layer, not a store. | source: [1]
- egress: '传输不限速' on every tier including free. Traffic is the cloud drive's traffic, so the pan's own quota binds, not CloudDrive2's. | metered: no | source: [1]
- identity: email | detail: A CloudDrive account, purchased in-app through App Store or Google Play or directly. No phone gate is published.
- interface: webdav, cli
- limits:
  - write-gated: free tier: 2 drives, 1 mount; Pro unlock at ¥4.99/month [1]
  - per-object-cap: encrypted upload 200 MB/file below 核心终身版 [1]
- binding note: A ¥4.99/month licence has no byte counter of its own; the pan's quota is what fails first. Naming a CloudDrive2 quota would misattribute another provider's limit.
- interface detail: The server runs on the local machine and exposes WebDAV; '独立 WebDAV 用户管理' is a Pro feature. Supported sources include 阿里云盘, 百度网盘, 115网盘, 天翼云盘, 123云盘, 迅雷云盘, OneDrive, Google Drive and WebDAV.
- tooling: Windows/macOS/Linux/Docker server plus apps for phone, TV and headset. WebDAV means rclone, Infuse, VidHub and any player can mount it.
- composes with: One licence turns five Chinese pans into one WebDAV endpoint, which is the piece AList does not sell: paid support, encrypted folders and cross-cloud copy in one binary.
- reliability: The mount is a client-side process: 115's API suspension in 2026 broke third-party mounts for a period, which is the failure mode of every layer that sits on a pan's private endpoints.
- notes: Runs on a free VM or a local machine - it is software on somebody else's hardware either way. The 视障用户 lifetime tier at ¥299 is a real discount route documented on the page.
- evidence note: The whole price ladder and the tier comparison table were read off the vendor's pricing page. No mount was run.
- self hosted: yes
- extras:
  - supports: 阿里云盘; 百度网盘; 115; 天翼; 123; 迅雷云盘; OneDrive; Google Drive; WebDAV
- evidence:
  - [1] 2026-10-23: 基础会员 free (2 drives, 1 mount); 核心会员 ¥4.99/月, ¥49.99/年; 轻享终身 ¥199; 核心终身版 ¥499; '传输不限速'; encrypted upload 200 MB cap named in the 终身 column
  - [2] 2026-10-23: '云盘本地挂载' with full random read/write; supported pan list including 阿里云盘/百度网盘/115网盘/天翼云盘/123云盘/迅雷云盘
- sources:
  - [1] http://www.clouddrive2.com/pricing.html
  - [2] https://www.clouddrive2.com/features.html
