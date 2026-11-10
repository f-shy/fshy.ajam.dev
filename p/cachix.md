# Cachix

> cachix.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cachix/ | JSON https://fshy.ajam.dev/api/v1/entity/cachix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cachix

- `storage/cachix-2` | fails-quota | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:39.698Z (live) | stale on 2026-12-04
- url https://www.cachix.org/pricing
- free tier: none reachable: 5 GB free for open source. Cloudflare egress is genuinely unlimited, but 5 GB is the cap. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Unlimited bandwidth on the Starter, Standard and Pro plans, served through the CloudFlare CDN; egress is not capped or priced. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the verdict rests on the vendor pricing page, read on 2026-11-03: it quotes the free 5 GB limit for open source projects and the unlimited bandwidth line of the paid plans
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 5 GB free for open source. Cloudflare egress is genuinely unlimited, but 5 GB is the cap.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB free for open source. Cloudflare egress is genuinely unlimited, but 5 GB is the cap.
  - [1] 2026-11-03: every paid plan (Starter, Standard, Pro) lists unlimited bandwidth | capture: sha256:349e7f1fac99ef3afe21f124aefab09f8ad8e9bde5f268f43996c1664b521c5a | quote: - Unlimited bandwidth
  - [1] 2026-11-03: the free allowance is 5 GB for open source projects | capture: sha256:349e7f1fac99ef3afe21f124aefab09f8ad8e9bde5f268f43996c1664b521c5a | quote: Users have a free 5 GB limit for open source projects and 20 Cachix Deploy agents.
- sources:
  - [1] https://www.cachix.org/pricing

## Cachix (Nix binary cache hosting)

- `storage/cachix` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.cachix.org
- free tier: 5 GB free for open-source projects: 'Users have a free 5 GB limit for open source projects and 20 Cachix Deploy agents.' Paid tiers start at 50 GiB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unlimited bandwidth even on the paid Starter tier ('Unlimited bandwidth', 'CloudFlare CDN caching'); free tier inherits the CF-backed delivery. Free egress is genuinely not the constraint here. | metered: no
- identity: email
- interface: rest, rclone, cli
- limits note: per-account quota: 5 GB hard on free (open-source only). retention: garbage collection removes unreferenced paths after a retention window (docs have a dedicated GC page). request-rate: not documented; served via Cloudflare.
- interface detail: rest
- tooling: `cachix` CLI (push/use), Nix `--substituters`, and the standard Nix binary-cache HTTP protocol (narinfo/nar). No rclone backend but the nar protocol is scriptable.
- composes with: one cache per account, 5 GB free; unlimited free accounts x 5 GB. Because a Nix cache is content-addressed and deduplicated, identical NARs are only stored once per cache - so multiplication is by account, not by file.
- reliability: Clean, documented, Cloudflare-fronted, unlimited bandwidth - the 5 GB is the only issue, and it is 100x short of the workload. Any Nix-cache-based plan is account-farming at 5 GB/account.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB free for open-source projects: 'Users have a free 5 GB limit for open source projects and 20 Cachix Deploy agents.' Paid tiers start at 50 GiB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Users have a free 5 GB limit for open source projects and 20 Cachix Deploy agents'; '50 GiB of storage / Unlimited bandwidth / CloudFlare CDN caching' on Starter
  - [2] 2026-10-21: probe: GET -> 200, 241 bytes (cache endpoint live, anonymous)
- sources:
  - [1] https://www.cachix.org/pricing
  - [2] https://cachix.org/api/v1/cache/nixpkgs
