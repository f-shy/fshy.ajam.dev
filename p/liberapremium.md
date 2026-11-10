# Libera Premium

> liberapremium.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/liberapremium/ | JSON https://fshy.ajam.dev/api/v1/entity/liberapremium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Libera Premium

- `debrid/liberapremium` | dead | evidence documented | binding none | category premium link generator / multi-host (Brazil, BRL) - closed | tier closed
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:15:00.000Z (live) | stale on 2026-11-23
- url https://liberapremium.com/
- free tier: None. The live site is a closure notice: 'liberapremium chegou ao fim' (liberapremium has come to an end), 'Desde 2015', 'liberapremium • 2015 - 2026'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: no service. The last indexed host table showed 1fichier and Mega as 'ilimitado' with a 1,000 KB/s ceiling on Mega, and Mediafire, Uploaded, Zippyshare and Uptobox marked 'OFF'. | source: [1] | note: Host statuses are from the search index's copy of the page, not from a live read; the live page no longer serves them.
- retention: not applicable: no storage, and the operation has ended. | source: [1]
- egress: No terms remain. The last indexed price table sold access by period: '1 Dia R$ 3,99', '30 Dias R$ 16,90', '60 Dias R$ 28,99', '90 Dias R$ 50,70', '180 Dias R$ 101,40'. | metered: no | source: [1]
- identity: email | detail: Not applicable now. The indexed copy implies a registration, as every Brazilian generator among debrid providers requires one.
- interface: unknown
- limits:
  - volume-quota: historical: 'ilimitado' on 1fichier, 1,000 KB/s on Mega, and four of the ten listed hosts already dead when the page was indexed [1]
  - volume-quota: none: service closed [1]
- limits note: The indexed page shows the structural problem without any enforcement data: half the host table was 'OFF'. A generator that resells host access loses a host whenever the host changes its API or blocks the reseller's IP range.
- binding note: Historical. The binding constraint was never reached because the service ended first, which is itself the finding.
- interface detail: The service is gone, so the interface is historical: a web generator. No API appears in the indexed copy.
- tooling: None. Any client still pointed at it fails.
- composes with: Nothing to chain. Its value now is as the failure mode of the Brazilian generator market: a 2015-vintage generator with ten years of operation closed in 2026, so a prepaid 180-day term bought in late 2025 bought less than half of what it promised.
- reliability: Closed in 2026 after eleven years. The farewell page gives no reason and offers no migration path or refund channel: 'Obrigado a todos que participaram durante esse tempo todo'.
- notes: Method note for the subsequent audit: a search snippet for this domain still returns a working price list and a host table, while the origin serves a farewell page. Any lane that prices Brazilian generators from snippets alone will quote a service that no longer exists. The live read is what settled it. Found by searching in Portuguese ('gerador de links premium gratis'), which is the only way it surfaced; an English query never returns it. It is the second Brazilian multi-hoster to close found among debrid providers's search results.
- evidence note: The closure was read live on the vendor's own domain, which is the strongest possible evidence for a dead verdict. Prices are reported only: they survive in the search index's copy of the page, and the live page does not serve them.
- extras:
  - closed_in: 2026
  - operated_since: 2015
  - last_indexed_prices_brl.1d: 3.99
  - last_indexed_prices_brl.30d: 16.90
  - last_indexed_prices_brl.60d: 28.99
  - last_indexed_prices_brl.90d: 50.70
  - last_indexed_prices_brl.180d: 101.40
  - last_indexed_dead_hosts: Dropbox; Mediafire; Uploaded; Zippyshare; Uptobox
  - lifetime: 2015-2026
  - market: Brazil
- evidence:
  - [1] 2026-10-23: the live closure notice: title 'liberapremium chegou ao fim', 'Desde 2015', 'Foram anos de historias, momentos, amizades e muita dedicacao', 'liberapremium • 2015 - 2026'
  - [1] 2026-10-23: the search index's copy of the same URL, still showing the price table (1 Dia R$ 3,99 through 180 Dias R$ 101,40) and a host table with Dropbox, Mediafire, Uploaded, Zippyshare and Uptobox marked 'OFF' - proof that an indexed snippet can outlive the page it describes
  - [1] 2026-10-23: 'liberapremium chegou ao fim ... Desde 2015 ... Foram anos de histórias ... liberapremium • 2015 - 2026'
- sources:
  - [1] https://liberapremium.com/
