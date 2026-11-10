# Vecwire

> vecwire.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vecwire/ | JSON https://fshy.ajam.dev/api/v1/entity/vecwire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vecwire

- `debrid/vecwire` | qualifies-with-caveat | evidence documented | binding request-rate | category multi-hoster (premium link generator, free tier on five hosts) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://get.vecwire.com/
- free tier: Up to 5 free links per day on 5 free hosts (1fichier, Extmatrix, Fshare.vn, Syncs.online, YouTube); the counter resets at 00:00 UTC. | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1]
- per-object cap: Per host on the free tier: 1fichier 4 GB, Extmatrix 2 GB, Fshare.vn 5 GB, Syncs.online 3 GB, YouTube 60 GB. | source: [1]
- retention: unverified: not stated | source: [1]
- egress: Direct high-speed links; free access is limited by daily link count and host-specific maximum file size. | metered: yes | free allowance: 5 links per day | source: [1]
- identity: anonymous | detail: The free page shows a counter and no sign-up step. Unverified whether the counter is kept per address or per account.
- interface: unknown
- limits:
  - request-rate (binding): 5 links per day, reset 00:00 UTC [1]
  - per-object-cap: free hosts: 1fichier 4 GB, Extmatrix 2 GB, Fshare.vn 5 GB, Syncs.online 3 GB, YouTube 60 GB [1]
- binding note: The 5-links-per-day counter is the first limit a free user meets; the per-host size caps follow.
- interface detail: Web generator: paste a URL, or a short batch, and receive a direct link.
- tooling: Browser only on the pages read.
- composes with: Rapidgator, Nitroflare, K2S and Hot4share stay on the paid plan.
- reliability: No outage observed on the day read.
- notes: Cheapest paid tier: unverified, the plans page needs a login.
- evidence note: First-party free page and home page; the paid plan page answered with a login wall, so its price is unverified.
- evidence:
  - [1] 2026-11-03: the free tier is 5 links per day on 5 hosts, reset at 00:00 UTC | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: 5 links/day 5 free hosts Resets at 00:00 UTC
  - [1] 2026-11-03: 1fichier is capped at 4 GB on the free tier | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: | 1fichier 1fichier | | 4 GB |
  - [1] 2026-11-03: YouTube is capped at 60 GB on the free tier | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: | youtube Youtube | | 60 GB |
  - [2] 2026-11-03: the generator on the home page requires a premium subscription | capture: sha256:548f791066bed2117ea0fa98ec67317ad3cc84b6192c334b2c39265f7be35b1a | quote: Premium subscription required to generate links.
  - [1] 2026-11-03: four hosts need the paid plan | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: Rapidgator, Nitroflare, K2S, and Hot4share require premium.
- sources:
  - [1] https://get.vecwire.com/free/
  - [2] https://get.vecwire.com/
