# Freenom

> freenom.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freenom/ | JSON https://fshy.ajam.dev/api/v1/entity/freenom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Freenom (.tk, .cf, .ga, .gq, .ml)

- `domains-dns/freenom` | dead | evidence measured | binding write-gated | category free registrable domain
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:05:00.000Z (live) | stale on 2027-01-21
- url https://www.freenom.com/
- free tier: no free registration is obtainable. The site redirects to a domain checker that returns 500 on a lookup | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: no registration completes
- retention: not applicable | days: 0 | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: no usable registration path
- interface: rest
- limits:
  - write-gated (binding): the availability check returns HTTP 500, so no registration flow completes [2]
- interface detail: a web form only; the availability endpoint returned HTTP 500
- tooling: none that works
- composes with: no path: the free TLD product is gone
- reliability: the domain resolves and serves a page; the registration endpoint errors
- notes: A live domain in front of a broken product. A status check on the homepage reports a working site; the thing that would give you a name returns 500.
- evidence note: the site and the availability endpoint were fetched: 302 to my.freenom.com, then 200 on the checker page and 500 on a TLD lookup.
- evidence:
  - probe:https://www.freenom.com/ 2026-10-22: 302 to https://my.freenom.com/domains.php, which returns 200 and 30,683 bytes of a domain checker with no free-registration path
  - probe:https://my.freenom.com/domains.php?a=availability&domain=<redacted>&tld=.tk 2026-10-22: 500 with an 'Oops!' error page, 1,337 bytes, so the availability service is broken rather than closed
- sources:
  - [1] https://www.freenom.com/
  - [2] https://my.freenom.com/domains.php
