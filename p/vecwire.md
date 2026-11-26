# Vecwire

> vecwire.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vecwire/ | JSON https://fshy.ajam.dev/api/v1/entity/vecwire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vecwire

- `debrid/vecwire` | qualifies-with-caveat | evidence documented | binding request-rate | category multi-hoster (premium link generator, free tier on five hosts) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:53.853Z (live) | stale on 2026-12-26
- url https://get.vecwire.com/
- free tier: Up to 5 free links per day on 4 free hosts (1fichier, Fshare.vn, Syncs.online, YouTube); the counter resets at 00:00 UTC. Extmatrix is no longer listed as a free host. | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1]
- per-object cap: Per host on the free tier: 1fichier 4 GB, Fshare.vn 5 GB, Syncs.online 3 GB, YouTube 60 GB. Extmatrix is no longer listed as a free host. | source: [1]
- retention: unverified: not stated | source: [1]
- egress: Direct high-speed links; free access is limited by daily link count and host-specific maximum file size. | metered: yes | free allowance: 5 links per day | source: [1]
- identity: anonymous | detail: The free page shows a counter and no sign-up step. Unverified whether the counter is kept per address or per account.
- interface: browser
- limits:
  - request-rate (binding): 5 links per day, reset 00:00 UTC [1]
  - per-object-cap: free hosts: 1fichier 4 GB, Fshare.vn 5 GB, Syncs.online 3 GB, YouTube 60 GB [1]
- binding note: The 5-links-per-day counter is the first limit a free user meets; the per-host size caps follow.
- interface detail: Web generator: paste a URL, or a short batch, and receive a direct link. Premium accounts also get a personal Bearer API key with RD-compatible endpoints for automated workflows and third-party downloaders.
- tooling: Browser generator on the free path; premium accounts get a Bearer API key with RD-compatible endpoints, and generated HTTPS links work in IDM, NDM, FDM and JDownloader.
- composes with: Rapidgator, Nitroflare, K2S and Hot4share stay on the paid plan.
- reliability: No outage observed on the day read.
- notes: Cheapest paid tier: unverified, the plans page needs a login. No programmatic path found: Web generator: paste a URL, or a short batch, and receive a direct link.
- evidence note: First-party free page and home page; the paid plan page answered with a login wall, so its price is unverified.
- evidence:
  - [1] 2026-11-03: the free tier is 5 links per day on 5 hosts, reset at 00:00 UTC | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: 5 links/day 5 free hosts Resets at 00:00 UTC
  - [1] 2026-11-03: 1fichier is capped at 4 GB on the free tier | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: | 1fichier 1fichier | | 4 GB |
  - [1] 2026-11-03: YouTube is capped at 60 GB on the free tier | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: | youtube Youtube | | 60 GB |
  - [2] 2026-11-03: the generator on the home page requires a premium subscription | capture: sha256:548f791066bed2117ea0fa98ec67317ad3cc84b6192c334b2c39265f7be35b1a | quote: Premium subscription required to generate links.
  - [1] 2026-11-03: four hosts need the paid plan | capture: sha256:cb60ee1489997eb9c086a7b031380ffad16d10f3ba9de4b23fbb37a7be1fe5f5 | quote: Rapidgator, Nitroflare, K2S, and Hot4share require premium.
  - [1] 2026-11-25: the free page now states four free hosts and a 5-link daily cap | capture: sha256:122b8a1b884e7bce8323c0da456d727897f5f96bd8bdf00cde87e81e4d2bfac1 | quote: 5 links/day 4 free hosts
  - [1] 2026-11-25: the free-host table still lists 1fichier at 4 GB and no Extmatrix row | capture: sha256:122b8a1b884e7bce8323c0da456d727897f5f96bd8bdf00cde87e81e4d2bfac1 | quote: | 1fichier 1fichier | online | 4 GB |
  - [1] 2026-11-25: the free-host table now has four rows, with YouTube capped at 60 GB | capture: sha256:122b8a1b884e7bce8323c0da456d727897f5f96bd8bdf00cde87e81e4d2bfac1 | quote: | youtube Youtube | online | 60 GB |
  - [1] 2026-11-25: the free tier still offers 5 links per day across four hosts | capture: sha256:122b8a1b884e7bce8323c0da456d727897f5f96bd8bdf00cde87e81e4d2bfac1 | quote: 5 links/day 4 free hosts
  - [1] 2026-11-25: the free link counter still resets at 00:00 UTC | capture: sha256:122b8a1b884e7bce8323c0da456d727897f5f96bd8bdf00cde87e81e4d2bfac1 | quote: Resets at 00:00 UTC
  - [2] 2026-11-25: premium-only hosts are still sold from USD 3.49 on a one-time payment | capture: sha256:2033d351f548a43d920127fa7bd414947622639f473dc64a0f3d87843d624cf1 | quote: Rapidgator, Nitroflare, K2S, Hot4share and more from $3.49.
  - [2] 2026-11-25: a paid API is now documented; it uses the RD-compatible endpoint shape | capture: sha256:2033d351f548a43d920127fa7bd414947622639f473dc64a0f3d87843d624cf1 | quote: Premium members get a personal Bearer API key in Account Settings with RD-compatible endpoints for automated workflows and third-party downloaders.
  - [2] 2026-11-25: generated links work in four named download managers | capture: sha256:2033d351f548a43d920127fa7bd414947622639f473dc64a0f3d87843d624cf1 | quote: Every generated link works directly with IDM, Neat Download Manager (NDM), Free Download Manager (FDM), and JDownloader.
- sources:
  - [1] https://get.vecwire.com/free/
  - [2] https://get.vecwire.com/
