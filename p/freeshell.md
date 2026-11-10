# freeshell.de

> freeshell.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freeshell/ | JSON https://fshy.ajam.dev/api/v1/entity/freeshell.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freeshell.de

- `compute/freeshell-de` | qualifies-with-caveat | evidence documented | binding write-gated | category shell | tier Free shell account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:15:00.000Z (live) | stale on 2026-11-24
- url https://freeshell.de/services/
- free tier: 'SSH to Ubuntu 24.04 LTS server with many tools and apps.' and 'Quota: 42 GB', 'Network: IPv4 + IPv6', 'Private TCP/UDP port: yes — on request'. The shell account is free and non-profit, online since 2002. | unit: GiB | metered on: stored-bytes | read on: 2026-10-24 | source: [1]
- per-object cap: ulimit values per account: 'nofile=unlimited', 'nproc=150', 'fsize=unlimited', 'mem=4 GB'
- retention: Not stated on the pages read: no inactivity deletion rule is published. Backups run daily with 30 days retention, which is the only retention number on the page.
- egress: not published: no traffic allowance or port speed is stated. 'Liberal fair-use limits' is the only qualifier. | metered: no | source: [1]
- identity: email | detail: no card, no phone, no document, no national ID. The signup form asks for a desired login and an existing email address only; a token arrives by email and is then written on a postcard and mailed to a German address before the account is enabled. The identity cost is a postal address, not a payment instrument.
- interface: ssh, sftp, webdav
- limits:
  - volume-quota: 42 GB of shell quota, shared with mail and web space [1]
  - volume-quota: nproc=150 and mem=4 GB per account [1]
  - write-gated (binding): activation requires a physical postcard mailed to a German address [2]
- binding note: The postcard is the gate: nothing is provisioned until a piece of physical mail reaches Germany, which is a delay of days and a cost of one stamp, and no digital route exists.
- interface detail: SSH to Ubuntu 24.04 LTS, a ShellInABox browser terminal, rsync/scp, WebDAV through ownCloud, MySQL over the CLI and phpMyAdmin, and a private TCP/UDP port on request. Podman is available for containers.
- tooling: any SSH client; Podman for containers; rsync/scp for transfer
- composes with: A shared shell with 4 GB of memory, 42 GB of disk, a real IPv4 and a private port on request, for no money and no card: the closest thing among evaluated providers to a free always-on host, at the cost of a physical postcard and a shared kernel.
- reliability: no reliability event observed. It is a non-profit club, not a company, so continuity rests on volunteers; the page states it has been online since 2002.
- notes: The best free always-on shape found among evaluated providers that takes no card: 4 GB of memory, 42 GB of disk and an inbound port. Three caveats. First, activation is by physical postcard to Germany, which is days of latency and a stamp, and it is the only route. Second, it is a shared host, not a VM: no root, a shared kernel, and Podman rather than Docker daemon access. Third, no vCPU count and no egress allowance are published, so the compute and bandwidth sides of the shape are unverified. Not previously in earlier readings. A third-party aggregator states 20 GB and 1 Gbps for this service; both disagree with the vendor's own 42 GB, and the vendor page is the one recorded.
- evidence note: Quota, memory, nproc, the IPv4+IPv6 pair, the private port and the postcard activation are all quoted from freeshell.de's own services and get-started pages read. Egress allowance, vCPU count and the inactivity rule are not published on any page read.
- extras:
  - shape.ram_gib: 4
  - shape.disk_gib: 42
  - shape.note: mem=4 GB is a ulimit, not an allocation; vCPU is not published, only nproc=150
  - billing_model: free
  - term: indefinite while the account is active; no term is published
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge, no card, no billing relationship; the cost is one postcard
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a private TCP/UDP port on request; IPv4 and IPv6 both assigned
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none published; background processes, screen/tmux and personal crontab are all permitted
  - signup_url: https://freeshell.de/get-started/
  - payment_methods: none; donations accepted, no billing system
- evidence:
  - [1] 2026-10-24: quoted: 'SSH to Ubuntu 24.04 LTS server with many tools and apps.', 'Quota: 42 GB', 'Network: IPv4 + IPv6', 'Private TCP/UDP port: yes - on request'
  - [1] 2026-10-24: quoted: 'Default limits (ulimit): nofile=unlimited nproc=150 fsize=unlimited mem=4 GB'; 'Background processes: yes · screen/tmux: yes · personal crontab: yes'; 'Backups: daily, 30 days retention'
  - [1] 2026-10-24: quoted: 'Podman (Docker-compatible). Find, run, build, share and deploy apps in your own environment here.' and 'Storage: images/volumes live under ~/.local/share/containers/ (counts to your quota)'
  - [2] 2026-10-24: quoted: 'Free Linux shell account. Activated by postcard.' and 'Grab a postcard: write your token on it, then mail it (physically) to the address in the email.' and 'once the postcard arrives, we enable your account'
  - [3] 2026-10-24: quoted: 'Your non-profit free shell provider since 2002' and 'Generous resources, rich environment, friendly by design'
  - [1] 2026-10-24: quoted: 'Quota: additional 42 GB (separate from shell quota)' for ownCloud, and 'MySQL 8.0 databases ... Quota: technically none - fair-use'
  - [1] 2026-10-24: quoted: 'SSH to Ubuntu 24.04 LTS server with many tools and apps.', 'Quota: 42 GB', 'Network: IPv4 + IPv6', 'Private TCP/UDP port: yes — on request'
  - [1] 2026-10-24: quoted: 'Quota: additional 42 GB (separate from shell quota)' for ownCloud, and 'MySQL 8.0 databases ... Quota: technically none – fair-use'
- sources:
  - [1] https://freeshell.de/services/
  - [2] https://freeshell.de/get-started/
  - [3] https://freeshell.de/
