# Pobierz.biz

> pobierz.biz | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pobierz/ | JSON https://fshy.ajam.dev/api/v1/entity/pobierz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pobierz.biz

- `debrid/pobierz-biz` | qualifies-with-caveat | evidence documented | binding volume-quota | category Polish multi-hoster debrid, prepaid traffic packages | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:06:35.000Z (live) | stale on 2026-11-23
- url https://www.pobierz.biz/pricing
- price PLN 276 per TB (EUR 63.2 at the ECB reference rate 4.3695 of 2026-10-22)
- free tier: None. The site sells traffic packages only, from 10 GB at 6,99 zł; no trial, credit or free plan is offered on the home page or the price page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not stated: the product is a traffic balance, capped by total gigabytes rather than by file size | source: [1]
- retention: Purchased transfer does not expire: 'Transfer nie wygasa' on every package. | source: [1]
- egress: Prepaid gigabytes, no expiry, no speed cap: 'Bez limitu prędkości', 'Transfer nie wygasa'. | metered: yes | price per TB: PLN 31.99 per 100 GB (PLN 0.32/GB); PLN 109.99 per 400 GB (PLN 0.27/GB) | source: [1]
- identity: email | detail: An account is needed to hold the prepaid balance; the signup form was not opened, and login is protected by a Cloudflare Turnstile widget.
- interface: unknown
- limits:
  - volume-quota (binding): prepaid balance: 10 GB for 6,99 zł; 30 GB 15,99; 50 GB 19,99; 100 GB 31,99; 200 GB 59,99; 400 GB 109,99 [1]
- limits note: 64 supported hostings. No concurrency figure, no per-host daily cap and no fair-use paragraph is published.
- binding note: Every gigabyte is bought before it is downloaded, so 1 TiB of monthly transfer costs PLN 0.27 x 1024 = about PLN 276 (EUR 63 at the ECB rate of 4.3695); the balance runs out mid-transfer rather than the speed or the request rate.
- interface detail: Web form: paste a link, the service fetches it, the download comes from its servers. No API, CLI or protocol endpoint is documented.
- tooling: Browser only as far as the site documents; no API and no download-manager plugin is named.
- composes with: At PLN 0.27-0.70 per GB it is the cheapest option for a few tens of gigabytes once, and the worst option for a sustained daily load; it belongs in the overflow slot, not the base of the stack.
- reliability: Prepaid credit with no expiry is the safe shape for a service that might close: the risk is losing an unused balance, not a subscription charge. The brand's own HTML is a clone of a second brand (see notes).
- notes: White-label twin of RapidTraffic.pl: two domains, one codebase, one Google Ads conversion id, one price list. Treat the two as one provider and do not count them as two services. At this volume the pay-per-GB model is 20 times the monthly cost of AllDebrid, so this is a small-burst tool, not a base.
- evidence note: The full price ladder, the host count and the no-expiry term are vendor-stated and read. What would raise it: buying 100 GB and pulling 100 GB, which would also show whether the 64 hosts all resolve.
- evidence:
  - [1] 2026-10-23: the six package prices from 10 GB / 6,99 zł to 400 GB / 109,99 zł, 'Pobieranie z 64 hostingów', 'Transfer nie wygasa'
  - [2] 2026-10-23: the three-step flow, 'Jedno konto - kilkadziesiąt hostingów' and the supported-host list headed by Filefactory, Turbobit and Youtube
  - probe:html-diff https://www.pobierz.biz/ vs https://www.rapidtraffic.pl/ 2026-10-23: the two home pages are the same build: after normalising the brand string the raw HTML differs only in the GA property, the logo asset, the Trustpilot business-unit id and the Turnstile site key, and both carry the same Google Ads conversion id AW-17061610643
- sources:
  - [1] https://www.pobierz.biz/pricing
  - [2] https://www.pobierz.biz/
