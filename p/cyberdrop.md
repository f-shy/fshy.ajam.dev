# CyberDrop

> cyberdrop.cr | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cyberdrop/ | JSON https://fshy.ajam.dev/api/v1/entity/cyberdrop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CyberDrop

- `storage/cyberdrop` | qualifies-with-caveat | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cyberdrop.cr
- free tier: Not stated numerically. 'Will you keep my files forever? Yes'. No published storage ceiling found; account creation is unverified and email-less. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: | Retention claims 'forever' and has been stable for years, but the extension allowlist and account-wide purge on a single CSAM hash match are real technical failure modes | source: [1] | note: not stated
- egress: No stated cap; files served directly. | metered: no
- identity: anonymous
- interface: rest
- limits note: Strict extension allowlist: only video/audio/image/archive/doc extensions (.mp4 .mkv .mp3 .flac .png .pdf .zip .7z .tar .iso .torrent .kdbx ..). No .bin/.parquet/.npy. This kills it as a raw dataset store. CSAM scanning via Cloudflare tooling purges the entire account on any hit.
- interface detail: rest
- tooling: No public API documented. Community downloader cyberdrop-dl exists. Upload is web-only per published documentation.
- composes with: Unlimited email-less accounts x no stated quota x permanent retention. The classic anonfiles shape.
- reliability: Retention claims 'forever' and has been stable for years, but the extension allowlist and account-wide purge on a single CSAM hash match are real technical failure modes. Domain has rotated (.me -> .cr) more than once.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Will you keep my files forever? Yes, we also offer a temporary uploads feature'; allowed-extension list quoted in full
  - [2] 2026-10-21: probe: GET -> 200 (cyberdrop.me is dead: DNS NXDOMAIN / CF 1016)
- sources:
  - [1] https://cyberdrop.cr/faq
  - [2] https://cyberdrop.cr/
