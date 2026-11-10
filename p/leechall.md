# Leechall

> leechall.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leechall/ | JSON https://fshy.ajam.dev/api/v1/entity/leechall.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leechall

- `debrid/leechall` | qualifies-with-caveat | evidence documented | binding volume-quota | category premium-link generator (free tier) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://leechall.com/
- price USD 0
- free tier: Free premium link generator with a per-host daily traffic allowance; the page's own counter reads 'Files Per Day: 0 / 5'. | unit: objects | metered on: object-count | read on: 2026-10-23 | source: [1] | note: Five files per day for an anonymous caller. The byte allowance is separate and per host, not per account.
- per-object cap: not stated on the page read; the listed limits are daily byte totals per host, not a single-file cap | source: [1] | note: A per-object cap would have to be read from a host-specific generator page; none was opened.
- retention: not applicable: the service generates a download link and does not offer storage | source: [1]
- egress: The link streams from Leechall's own servers, so the byte counter that binds is Leechall's, per host, per day. The page lists caps such as 'extmatrix.com 0 B / 6 GB /d', '1fichier.com 0 B / 8 GB /d', 'mega.nz 0 B / 1 GB /d', 'isra.cloud 0 B / 650 MB /d', 'emload.com 0 B / 250 MB /d'. | metered: yes | free allowance: per-host daily totals: extmatrix 6 GB/d, 1fichier 8 GB/d, mega.nz 1 GB/d, alfafile 1 GB/d, filestore.to 5 GB/d, tezfiles 800 MB/d, hitfile 650 MB/d, isra.cloud 650 MB/d, chomikuj.pl 350 MB/d, emload 250 MB/d | source: [1]
- identity: anonymous | detail: The generator ran with no account on the page read; the page prints a usage counter against the caller's network ('Your IP: ...', 'You Used: 0 B'), so the identity it bills is the egress address, not a login.
- interface: unknown
- limits:
  - pull-count: 5 files per day (page counter 'Files Per Day: 0 / 5') [1]
  - volume-quota (binding): per-host daily caps, 250 MB/day (emload) to 8 GB/day (1fichier) [1]
- limits note: Every listed host carries its own daily byte ceiling, so the binding number depends on which host is targeted. A host not on the list cannot be fetched at all.
- binding note: Five files a day is generous next to the bytes: at 250 MB/day for emload and 650 MB/day for isra.cloud, 1 TiB of monthly transfer would need roughly 1,500 days of emload quota. The daily byte ceiling on each host is what fails first.
- interface detail: A web form: paste a host URL, receive a generated link. The only other channel the page offers is a Telegram channel for status (t.me/leechallcom). No API, CLI or rclone backend was found.
- tooling: none today: browser form only. A wrapper would have to drive the form or reverse its request shape; that is a tooling gap, not a verdict.
- composes with: Covers the small set of hosts a debrid subscription does not: extmatrix, isra.cloud, emload, chomikuj.pl. At 250 MB/day on emload and 650 MB/day on isra it moves a few hundred megabytes a day, so it supplements a paid debrid rather than replacing one.
- reliability: When a host's daily allowance is exhausted the generator still answers and the link fails at download; the counter is against the caller's IP, so a shared or changing egress address changes the allowance.
- notes: The per-host caps are the useful artefact: they are a third-party statement of what each host lets a leecher pull per day, which is the number the filehost's own pages rarely publish.
- evidence note: Read on the live site. A generated link that completes a download would raise this to measured; that needs a target URL on a supported host.
- extras:
  - hosts_listed: 59
  - paid_sibling: leechall.io
- evidence:
  - [1] 2026-10-23: 'Files Per Day: 0 / 5', the per-host daily table (extmatrix 6 GB/d, 1fichier 8 GB/d, isra.cloud 650 MB/d, emload 250 MB/d), and the 59-host supported list
  - [2] 2026-10-23: the same operator sells a paid ad-free service from $2.99, which fixes leechall.com's free tier in the product line
- sources:
  - [1] https://leechall.com/
  - [2] https://leechall.io/
