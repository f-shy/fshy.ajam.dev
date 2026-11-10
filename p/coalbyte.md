# CoalByte Cloud

> coalbyte.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coalbyte/ | JSON https://fshy.ajam.dev/api/v1/entity/coalbyte.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoalByte Cloud

- `compute/coalbyte-free` | qualifies-with-caveat | evidence documented | binding write-gated | category game-server | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-24T04:12:03.000Z (live) | stale on 2026-11-24
- url https://coalbyte.com/de
- free tier: 'Starte deinen garantierten kostenlosen Server mit 3 GB RAM, 1 vCPU und 8 GB Speicher in unter 60 Sekunden'; '100% Dauerhaft kostenlos'; 'Keine Kreditkarte nötig'. The Discord-bot page states a different free allocation: '1024 MB RAM · 1 vCPU Dedicated' with '1.1 GB / 5 GB NVMe'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: 'Jeder Benutzer erhält bei der Registrierung garantiert 1 komplett kostenlosen Server-Slot' (one free server slot per account)
- retention: not published for the game servers; the Minecraft page states '100% kostenloses 24/7 Minecraft Server Hosting' without a sleep rule. A separate free host in the same German search results (mcfreehost) states a 15-minute sleep, but that is a different provider and is not evidence about this one.
- egress: not published: no traffic allowance appears on the German home page, the Minecraft page or the Discord-bot page read | metered: no | source: [2]
- identity: email | detail: no card: quoted 'Keine Kreditkarte nötig' and 'No credit card required'.
- interface: ftp, rest
- limits:
  - volume-quota: 3 GB RAM, 1 vCPU, 8 GB storage on the game-server tier; 1024 MB RAM, 5 GB NVMe on the bot tier [1]
  - write-gated (binding): one free server slot per account [1]
- binding note: The free slot is guaranteed per account and there is one of them, so the second project is the wall rather than any resource inside the first.
- interface detail: a panel with FTP access, a live console and 1-click installers for Spigot, Paper, Forge, Discord.js, Discord.py, Java JDA and Go
- tooling: FTP and the vendor panel; no SSH and no root stated
- composes with: A game server or a Discord bot, which is what the offer is for. It is a narrow host: nothing on the pages read suggests a general-purpose machine.
- reliability: no reliability event observed. The imprint states the entity is not yet a registered company, which is a fact about the seller and not about uptime.
- notes: The allocation is the largest of any no-card row among evaluated providers, and the imprint is unusually honest about the seller: it states in its own words that the company is a 'planned' S.R.L. that will be registered 'when the platform reaches operational viability'. That is precisely the pattern comparative records was burned by once, so it is classified as a caveat in the same sentence as the offer rather than as a disqualification. Two further defects: the two product pages give different free allocations (3 GB with 8 GB of storage on the game tier, 1024 MB with 5 GB NVMe on the bot tier), and no page states a traffic allowance or a sleep rule. It is also a game and bot host, not a general machine.
- evidence note: The free allocation, the no-card statement and the one-slot rule are quoted from the vendor's own pages read. Egress and retention are unpublished. The entity disclosure is quoted from the imprint and is the reason the verdict is a caveat rather than a rejection.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 3
  - shape.disk_gib: 8
  - billing_model: free
  - term: not published; described as 'dauerhaft kostenlos'
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: EUR 0.00 for the free slot; no published rate to multiply
  - free_tier_kind: free-forever-with-quota
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a game or bot port on the provider's address; not enumerated
  - session_cap.restart_required: no
  - session_cap.note: no sleep rule published for the game tier; the bot tier advertises a 24/7 auto-restart watchdog
- evidence:
  - [1] 2026-10-24: quoted: '3 GB Dedizierter RAM', '1 vCPU & 8 GB', '100% Dauerhaft kostenlos', 'Keine Kreditkarte nötig', 'Jeder Benutzer erhält bei der Registrierung garantiert 1 komplett kostenlosen Server-Slot'
  - [2] 2026-10-24: quoted: '0€ / Forever Free', 'NO CREDIT CARD', '1024 MB RAM· 1 vCPU Dedicated', '1.1 GB / 5 GB NVMe', 'Auto-Restart Watchdog'
  - [3] 2026-10-24: quoted: 'Bezeichnung: Robert - CoalByte Cloud'; 'Geplante Rechtsform: S.C. CoalByte Cloud S.R.L.'; 'Unabhängiges Technologieprojekt in der Entwicklungs- und Machbarkeitsvalidierungsphase. Die formelle Eintragung als Handelsgesellschaft erfolgt mit Erreichen der operativen Tragfähigkeit der Plattform.'; 'Stadt: Bacău', 'Land: Rumänien'
  - [4] 2026-10-24: quoted: '100% kostenloses 24/7 Minecraft Server Hosting ohne Kreditkarte'; '3 GB dedizierter RAM, 1 vCPU Ryzen 4.5+ GHz, 20.0 TPS'
- sources:
  - [1] https://coalbyte.com/de
  - [2] https://coalbyte.com/de/discord-bot-hosting
  - [3] https://coalbyte.com/de/imprint
  - [4] https://coalbyte.com/de/free-minecraft-hosting
