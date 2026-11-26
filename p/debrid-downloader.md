# Debrid-Downloader

> debrid-downloader.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debrid-downloader/ | JSON https://fshy.ajam.dev/api/v1/entity/debrid-downloader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Debrid-Downloader

- `debrid/debrid-downloader` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category free premium-link generator with a 220-host landing list | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:44.526Z (live) | stale on 2026-12-26
- url https://www.debrid-downloader.com/
- price EUR 0 (cap unstated)
- free tier: 'Download from 220+ file hosting sites at maximum speed today!'; 'Over 220+ supported hosts'; the FAQ says the service is 'completely free and requires no registration or premium accounts'. No cap, trial or price is stated on the page. | unit: unlimited | metered on: unstated | read on: 2026-10-23 | source: [1] | note: An 'unlimited' claim with no stated counter; the only way to find the real cap is to generate links until it stops.
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: No bandwidth, quota or pricing language on the page at all; the only claim is 'maximum speed'. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: No login, no account and no email field appears on the generator page; the host picker is usable directly.
- interface: browser
- limits note: No limit is published, which for a free service usually means an undocumented per-IP cap; nothing was measured.
- binding note: Inferred, not documented: a free generator that publishes no account quota is almost always shaped per IP, and the site states no counter of any other kind. The inference is recorded as an inference.
- interface detail: A host picker ('Select a filehost to leech from') leading to one page per host (/premium-generator/<host>); no API, CLI or plugin documented.
- tooling: Browser only.
- composes with: Its value is the per-host landing pages rather than the service: they are SEO pages that name a host, which makes the site a usable host index even if the generator does not work.
- reliability: The 220-host list is padded with hosts that no longer exist, so the effective coverage is well below the headline (see notes). No status page.
- notes: The 220-host figure is the weakest claim of this service: the list still carries Zippyshare (whose own front page announces its 2023 death), anonfiles.com, netload.in and rapidshare.io, so a reader who counts hosts is counting graves. The generator itself was not exercised, so the service may be fine; what is wrong is the coverage number, not the service. No programmatic path found: A host picker ('Select a filehost to leech from') leading to one page per host (/premium-generator/<host>); no API, CLI or plugin documented.
- evidence note: The 220+ claim, the host list and the absence of any counter are read from the vendor page. The binding is inferred. A generated link would show whether the service works at all; the dead-host finding is measured separately.
- evidence:
  - [1] 2026-10-23: the '220+' host claim and the full host list, which includes zippyshare.com, anonfiles.com, netload.in, uploaded.net and rapidshare.io
  - [2] 2026-10-23: that one host on the list is dead, by the host's own memorial page: 'Here lies Zippyshare [2006 - 2023]' and 'Farewell.'
  - [1] 2026-11-25: the generator requires no registration, email, phone or card | capture: sha256:69380f885ddf24b97c776fa4af510ca5053c85e7535ff12b440c2ab25c2b36a3 | quote: Yes, our service is completely free and requires no registration or premium accounts.
  - [1] 2026-11-25: the current page still states over 220 supported hosts | capture: sha256:69380f885ddf24b97c776fa4af510ca5053c85e7535ff12b440c2ab25c2b36a3 | quote: Over 220+ supported hosts
  - [2] 2026-11-25: Zippyshare, still on the generator's host list, is dead by its own memorial page | capture: sha256:c643388588a6169cf89d6bed1578a58d804e9238ae9b8d376f53734f313594c5 | quote: Here lies Zippyshare [2006 - 2023], once upon a time a fairly big file hosting site blessed with a loyal and loving community.
  - [2] 2026-11-25: the dead-host example in the coverage note still holds | capture: sha256:c643388588a6169cf89d6bed1578a58d804e9238ae9b8d376f53734f313594c5 | quote: Here lies Zippyshare [2006 - 2023], once upon a time a fairly big file hosting site blessed with a loyal and loving community.
- sources:
  - [1] https://www.debrid-downloader.com/
  - [2] https://www.zippyshare.com/
