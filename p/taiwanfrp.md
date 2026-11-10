# TaiwanFRP

> taiwanfrp.me | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/taiwanfrp/ | JSON https://fshy.ajam.dev/api/v1/entity/taiwanfrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TaiwanFRP

- `egress/taiwanfrp` | qualifies-with-caveat | evidence documented | binding retention-clamped | category udp port forward (hosted, Taiwan) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T06:52:59.172Z (live) | stale on 2026-12-05
- url https://taiwanfrp.me/
- price USD 0
- free tier: [translated] 'A free service, designed for users who do not have a public IP.' 'It supports both TCP and UDP traffic forwarding at the same time, ensuring stable server operation.' | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: [translated] No byte allowance, rate or session length is published on the front page, the how-to page, the terms page or the client download page. The only limit visible is an account expiry, which the status panel reports.; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: [translated] Registration takes a username, a password and a verification code obtained from the vendor's Discord: 'one Discord user may register only one account'. The third field reads 'Taiwan mobile phone (not required) - Taiwan mobile numbers only, landlines cannot be used; some features require a phone number, which you can also add later in the account settings'. | country: None
- interface: cli
- limits:
  - retention-clamped (binding): [translated] 'The account has already expired, the proxy cannot be started! Please contact TaiwanFRP.' [1]
- binding note: No byte allowance is published anywhere, so no volume quota can be shown to fail first. What the site itself displays as a failure is an expired account: the status panel reports the expiry and refuses to start the proxy.
- interface detail: the downloads page lists per-architecture binaries and a separate FRPC file.
- tooling: the vendor's client builds for Windows 386/amd64/arm64, Linux on 11 architectures, macOS two builds, version 1.1.1; a custom FRPC file is also offered
- composes with: A Taiwanese UDP port forward is the missing third leg of an Asia set that already covers Japan and Korea, and it needs no phone number.
- reliability: Nodes provided by other users are described by the vendor as sometimes unstable; the account expiry stops the proxy; Discord membership is checked at start-up.
- notes: The only Taiwanese free service found that forwards UDP on a public port without a public IP, and the cheapest identity cost: a Discord account, with the Taiwanese mobile number explicitly optional and needed only for some features. Two gaps. Every page is silent on volume. And the account appears to carry an expiry that must be renewed, which the status panel reports as a hard stop. Country: Taiwan; the operator writes in Traditional Chinese, and the terms invoke the law of the Republic of China. A user is frp-based: a 'custom client FRPC file' is offered for download.
- evidence note: Port forwarding support for TCP and UDP, client binaries and Discord registration are documented on official pages.
- extras:
  - wg_path: inside-udp
  - wg_detail: [translated] 'Register an account and create a proxy, and you can host a Minecraft or other TCP/UDP server.' A UDP proxy on a public port would carry a WireGuard datagram; the vendor issues no .conf and a user is their own build.
  - ingress: tcp+udp
  - volume_stated: [translated] No byte allowance, rate or session length is published on the front page, the how-to page, the terms page or the client download page. The only limit visible is an account expiry, which the status panel reports.
  - bytes_transit: yes
  - transit_note: The vendor's Taiwanese public node relays to the local machine.
- evidence:
  - [1] 2026-10-23: [translated] 'It supports both TCP and UDP traffic forwarding at the same time', 'A free service, designed for users who do not have a public IP.'
  - [2] 2026-10-23: [translated] 'Taiwan mobile phone (not required)'; 'Go to Discord to get the verification code'; 'one Discord user may register only one account'.
  - [1] 2026-10-23: [translated] The status panel text, confirmed in the served HTML of the page on 2026-10-23: 'The account has already expired, the proxy cannot be started! Please contact TaiwanFRP', and 'Detected that you have not joined Discord; please join promptly, otherwise the proxy cannot be started.'
  - [3] 2026-10-23: The terms, last updated 2026-02-19, describe FRP forwarding, multi-node choice and flexible scaling, and publish no quota table.
  - [2] 2026-11-03: [translated] registration needs a verification code obtained from the vendor's Discord, and one Discord user may register one account | capture: sha256:a185601c942d56886a49f0b59b2dadcb29ca41c1ba56c29289d73a31580857d9 | quote: 請進入 Discord 獲取驗證碼。進入之後到頻道▘註冊使用者帳號▗點擊點擊按鈕獲取。一位discord使用者只能註冊一個帳號。
  - [1] 2026-11-03: [translated] the front page states that TCP and UDP traffic forwarding are both supported | capture: sha256:ef4247fe56937b87b64c2df30f7b4e05966ec49c885758d52d7d79a663e8a7af | quote: 同時支援 TCP 與 UDP 流量轉發，確保伺服器穩定運行。
  - [1] 2026-11-03: [translated] the served front page carries the status text that an expired account cannot start the proxy | capture: sha256:ef4247fe56937b87b64c2df30f7b4e05966ec49c885758d52d7d79a663e8a7af | quote: 帳號已經到期，無法啟動代理！請聯絡TaiwanFRP
  - [2] 2026-11-03: [translated] the Taiwanese mobile number is optional and can be added later in the account settings | capture: sha256:9de9a3955524f402d185f6580bcc0c4bc8e91f89a59f5adfdbf9e3fd54438489 | quote: （僅限台灣行動電話，市內電話不可使用；部分功能要求電話號碼，你也可以稍後再帳號設定中添加）
  - [3] 2026-11-03: [translated] some nodes are provided by other users and are sometimes unstable | capture: sha256:8782aefc7abc023daaf742c41d0fe5dca131c32cdd6706c4db6d673357f1fd94 | quote: 部分節點由其他使用者提供，有時可能不穩定，請見諒。
  - [1] 2026-11-04: the front page states simultaneous TCP and UDP forwarding | capture: sha256:533ca64190205a8229f6ad2fdbc0c81200be6c4db1d4fb35cbc34706aa8fa2a0 | quote: 同時支援 TCP 與 UDP 流量轉發，確保伺服器穩定運行。
  - [2] 2026-11-04: registration takes a verification code from the vendor's Discord, one account per Discord user | capture: sha256:a185601c942d56886a49f0b59b2dadcb29ca41c1ba56c29289d73a31580857d9 | quote: 請進入 Discord 獲取驗證碼。進入之後到頻道▘註冊使用者帳號▗點擊點擊按鈕獲取。一位discord使用者只能註冊一個帳號。
- sources:
  - [1] https://taiwanfrp.me/
  - [2] https://taiwanfrp.me/reg.html
  - [3] https://taiwanfrp.me/terms.html
