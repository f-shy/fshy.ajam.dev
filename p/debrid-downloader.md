# Debrid-Downloader

> debrid-downloader.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debrid-downloader/ | JSON https://fshy.ajam.dev/api/v1/entity/debrid-downloader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Debrid-Downloader

- `debrid/debrid-downloader` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category free premium-link generator with a 220-host landing list | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://www.debrid-downloader.com/
- price EUR 0 (cap unstated)
- free tier: 'Download from 220+ file hosting sites at maximum speed today' and 'Bypass slow downloads and paywalls'. No cap, no trial, no price is stated anywhere on the page. | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1] | note: An 'unlimited' claim with no stated counter; the only way to find the real cap is to generate links until it stops.
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: No bandwidth, quota or pricing language on the page at all; the only claim is 'maximum speed'. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: No login, no account and no email field appears on the generator page; the host picker is usable directly.
- interface: unknown
- limits note: No limit is published, which for a free service usually means an undocumented per-IP cap; nothing was measured.
- binding note: Inferred, not documented: a free generator that publishes no account quota is almost always shaped per IP, and the site states no counter of any other kind. The inference is recorded as an inference.
- interface detail: A host picker ('Select a filehost to leech from') leading to one page per host (/premium-generator/<host>); no API, CLI or plugin documented.
- tooling: Browser only.
- composes with: Its value is the per-host landing pages rather than the service: they are SEO pages that name a host, which makes the site a usable host index even if the generator does not work.
- reliability: The 220-host list is padded with hosts that no longer exist, so the effective coverage is well below the headline (see notes). No status page.
- notes: The 220-host figure is the weakest claim of this service: the list still carries Zippyshare (whose own front page announces its 2023 death), anonfiles.com, netload.in and rapidshare.io, so a reader who counts hosts is counting graves. The generator itself was not exercised, so the service may be fine; what is wrong is the coverage number, not the service.
- evidence note: The 220+ claim, the host list and the absence of any counter are read from the vendor page. The binding is inferred. A generated link would show whether the service works at all; the dead-host finding is measured separately.
- evidence:
  - [1] 2026-10-23: the '220+' host claim and the full host list, which includes zippyshare.com, anonfiles.com, netload.in, uploaded.net and rapidshare.io
  - [2] 2026-10-23: that one host on the list is dead, by the host's own memorial page: 'Here lies Zippyshare [2006 - 2023]' and 'Farewell.'
- sources:
  - [1] https://www.debrid-downloader.com/
  - [2] https://www.zippyshare.com/
