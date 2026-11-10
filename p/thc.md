# Segfault

> thc.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thc/ | JSON https://fshy.ajam.dev/api/v1/entity/thc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Segfault (THC)

- `compute/segfault-net` | qualifies | evidence documented | binding volume-quota | category sandbox | tier Free root server
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:00:12.000Z (live) | stale on 2026-11-24
- url https://www.thc.org/segfault/
- free tier: 'Segfault offers free unlimited Root Servers. A new server (inside a Virtual Machine) is created for every SSH connection.' Access is an ssh login as root on segfault.net with the password 'segfault'; no signup, no email, no account. The free server carries restrictions: 'The storage, memory, processing power and bandwidth is limited.' | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: one root server per SECRET; a new SECRET yields a new server with a new /sec filesystem. Not a cap on how many you may hold.
- retention: 'Data in your home directory and in /sec, /onion and /everyone are permanent. This data is cleared only if the server is not logged in for 30+ days.' Root filesystem and /tmp are wiped at logout: 'Data in (/usr, /tmp, ...) is only valid for the duration of the session'.
- egress: 'the outbound traffic is throttled' on the free service; the throttle rate is not published. Outbound is routed through Mullvad/CryptoStorm/NordVPN exit nodes. | metered: no | source: [2]
- identity: anonymous | detail: No account, email, card, phone, or identity document required. Access is via SSH as user root to segfault.net with password segfault. A per-server secret key is generated at session creation for instance identification.
- interface: ssh
- limits:
  - retention-clamped: auto-shutdown when no shell is running in tmux or screen and nobody has logged in for 1.5 days [2]
  - retention-clamped: permanent data in /sec cleared after 30+ days without a login [2]
  - volume-quota (binding): free servers are resource-restricted; the numeric memory, CPU and storage caps are not published on any page read [3]
  - per-ip-shaping: outbound traffic is throttled on the free tier; the rate is not published [2]
- binding note: The free tier's memory, CPU and disk caps are unpublished, so the first thing that fails is whatever the per-container limit is, and you cannot know it before logging in and running `cat /config/self/limits`.
- interface detail: SSH only, on port 22 or 443, plus a `.onion` and `.gsocket` route. Root inside the guest. No web console, no API. A reverse TCP/UDP port on a public IP is provided; `curl sf/port` prints the IP and port.
- tooling: any SSH client; OpenSSH must be new enough to support `-o SetEnv` (the FAQ names 'Bad configuration option: setenv' as the failure on old clients)
- composes with: An anonymous root shell with a public reverse port and no account of any kind: the cheapest possible way to hold a WireGuard endpoint or a cron-driven monitor without giving up an identity, at the cost of a 1.5-day idle reap.
- reliability: no reliability event observed. The operator states it may shut free servers down under resource contention and that it is 'no company' run in spare time, which is a capacity statement rather than an observed outage.
- notes: The only provider among documented hosts with a genuinely anonymous identity cost: no signup form exists to be filled in. Three things are unresolved and all three need a login this category must not perform. First, the numeric shape (vCPU, RAM, disk) is not on any first-party page; `cat /config/self/limits` prints it after login. A third-party writeup (nixsanctuary.com) states 128 MB personal storage, 16 GB shared and a read-only rootfs at 500 Mbit/s, which is reported-only and contradicts nothing but is unconfirmed. Second, the outbound throttle rate is unpublished. Third, 'unlimited Root Servers' is the operator's phrase; whether it means unbounded concurrent servers is unstated. The guest has no systemd, so a daemon has to be started from /sec/usr/etc/rc.local. A reverse port is explicitly provided, so an inbound listener works without a static IP of your own.
- evidence note: The machine's numeric shape is unverified: no first-party page publishes it, and the config file in the public repository has every limit commented out.
- extras:
  - shape.note: not published on any first-party page; the config file in the public repo has the limits commented out and the FAQ points at `cat /config/self/limits` inside the guest
  - billing_model: free
  - term: per session; persistent storage survives 30 days of non-use
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge at any point and no payment field exists, so there is no rate to multiply
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: one reverse TCP/UDP port on a public IP, assigned by the service; `curl sf/port` prints IP and port
  - network_out.static_ip: no
  - session_cap.idle_reap_s: 129600
  - session_cap.restart_required: yes
  - session_cap.note: no wall clock while a shell is attached; auto-shutdown after 1.5 days with no login and no shell in tmux or screen. Every login without the SECRET creates a fresh server.
  - signup_url: https://www.thc.org/segfault/
  - payment_methods: none; there is no billing system and no account to bill
- evidence:
  - [1] 2026-10-24: quoted: 'Segfault offers free unlimited Root Servers. A new server (inside a Virtual Machine) is created for every SSH connection.' and the login block 'ssh [address removed] # The password is segfault'
  - [1] 2026-10-24: quoted: 'Outgoing traffic is routed through NordVPN/CryptoStorm/Mullvad.', 'Reverse TCP/UDP port on a public IP.', 'Encrypted storage in /sec and /home'
  - [2] 2026-10-24: quoted: 'How long will the server run? Forever if you stay logged in (active session/connected). Auto-shutdown may occur if there is no shell running (in tmux or screen) and nobody has logged in for 1.5 days.'
  - [2] 2026-10-24: quoted: 'Data in your home directory and in /sec, /onion and /everyone are permanent. This data is clearedo only if the server is not logged in for 30+ days.'
  - [2] 2026-10-24: quoted: 'The FREE service is restricted and the outbound traffic is throttled.' and 'You can see your current restrictions by typing cat /config/self/limits.'
  - [2] 2026-10-24: quoted: 'The server comes with around 54GB of pre-installed tools.' and 'There is no systemd/systemctl.'
  - [3] 2026-10-24: quoted: 'The free servers have restrictions in place. The storage, memory, processing power and bandwidth is limited. When there is a squeeze for resources we may shut down free servers.'
  - [4] 2026-10-24: the public limit file ships every value commented out, e.g. '#SF_USER_MEMORY_LIMIT=256m', '#SF_USER_PIDS_LIMIT=128', '#SF_USER_CPU_SHARE=8', '#SF_CPUS= # automatic between 1..4 depending on host's cpu count' - these are examples, not the deployed defaults, so they cannot be read as the free shape
  - [5] 2026-10-24: quoted: 'Over 8GB of the finest hacking/coding tools pre-installed.' and 'Reverse Port Forwards (forget ngrok. This is free & better).'
  - [4] 2026-10-24: the public limit file ships every value commented out, e.g. '#SF_USER_MEMORY_LIMIT=256m', '#SF_USER_PIDS_LIMIT=128', '#SF_USER_CPU_SHARE=8', '#SF_CPUS= # automatic between 1..4 depending on host's cpu count' — these are examples, not the deployed defaults, so they cannot be read as the free shape
- sources:
  - [1] https://www.thc.org/segfault/
  - [2] https://www.thc.org/segfault/faq/
  - [3] https://www.thc.org/segfault/free/
  - [4] https://raw.githubusercontent.com/hackerschoice/segfault/main/config/etc/sf/sf.conf
  - [5] https://blog.thc.org/disposable-root-servers
