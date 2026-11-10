# Nexus Mods

> nexusmods.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nexusmods/ | JSON https://fshy.ajam.dev/api/v1/entity/nexusmods.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nexus Mods

- `storage/nexus-mods` | qualifies-with-caveat | evidence reported | binding per-object-cap | category Game-mod repository — unlimited hosting, GB-scale files
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.nexusmods.com
- free tier: Vendor help page states it outright: 'Unlimited storage and distribution for mods and images that you create. Unlimited file hosting for mods and images that you've created and uploaded.' Their own wiki table: Maximum Storage 'Unrestricted', Upload Limitations 'Unlimited (20GB limit through the browser, contact us for larger uploads)'. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 20 GB | bytes: 20000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, no egress quota. But per-IP shaped (see reliability_note). No Cloudflare in front of the file CDN; downloads come from their own edge. | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - per-ip-shaping: 1 MB/s [1]
  - per-ip-shaping: 1.5 MB/s [1]
  - per-object-cap (binding): per-object-cap 20 GB [1]
- limits note: per-object-cap 20 GB via browser, larger by request. per-ip-shaping is the binding number: ~1 MB/s regular, ~1.5 MB/s with an adblocker, 3 MB/s Supporters; uncapped only for Premium (paid). Resumable downloads are free only on files >500 MB.
- interface detail: Web upload + REST API v1 (api.nexusmods.com, `users/validate.json` returned 401 unauthenticated = live and auth-gated, not dead). Free API key issued per account.
- tooling: REST + a maintained community uploader (Digitalroot.ModUploader, supports `nexusmods` commands).
- composes with: Offers 20 GB per object with no aggregate storage quota. Downloads require session authentication or API keys, operating as an archive store rather than a direct origin.
- reliability: The 1–1.5 MB/s un-premium cap is the real constraint. ~3.5–5 GB/hour per stream, so per-IP-shaping governs, not storage. Files are virus-scanned and quarantined on false positives (WinRAR .rar especially).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Unlimited storage and distribution' and 'Unlimited file hosting' as free Basic benefits
  - [2] 2026-10-21: Nexus Mods row: Maximum Storage Unrestricted, Upload Limitations 20GB via browser
  - [3] 2026-10-21: speed cap table: ~1.5MB/s adblock, 3MB/s Supporter, uncapped Premium
  - [4] 2026-10-21: resumable downloads free only on files over 500MB, still in beta
  - [5] 2026-10-21: 401 (endpoint alive, auth required); www.nexusmods.com itself 403s plain curl (Cloudflare)
- sources:
  - [1] https://help.nexusmods.com/article/42-what-are-the-benefits-of-creating-a-nexus-mods-account
  - [2] https://wiki.nexusmods.com/index.php/List_of_online_hosting_sites
  - [3] https://help.nexusmods.com/article/96-download-speed-caps-adblockers-and-different-types-of-membership
  - [4] https://help.nexusmods.com/article/170-resumable-downloads
  - [5] https://api.nexusmods.com/v1/users/validate.json
