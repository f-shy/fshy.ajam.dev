# DebridHub

> debridhub.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debridhub/ | JSON https://fshy.ajam.dev/api/v1/entity/debridhub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DebridHub

- `debrid/debridhub` | qualifies-with-caveat | evidence documented | binding pull-count | category premium-link generator (free, no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://debridhub.com/
- price USD 0
- free tier: Free and unlimited premium link generation; the FAQ says 'You can process up to 8 premium links daily'. | unit: objects | metered on: object-count | read on: 2026-10-23 | source: [1] | note: Eight generated links per day. No account, no balance, no paid tier on the page read.
- per-object cap: 'Unlimited file size processing - no restrictions, completely free access.' | source: [1] | note: Stated, not measured. The real ceiling is whatever the upstream host allows per file.
- retention: 'We automatically delete all processed links immediately after completion for maximum privacy.' | days: 0 | source: [1] | note: Links are consumed, not stored; nothing accumulates.
- egress: Downloads are served from DebridHub's own servers at '100% maximum speeds'. No byte allowance and no price appear on the page. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: No account or login on the generator; the page advertises free use with no registration. Nothing but the caller's IP is presented.
- interface: unknown
- limits:
  - pull-count (binding): 8 premium links per day [1]
  - per-ip-shaping: 'Advanced IP-locked access ensuring exclusive and protected link generation' [1]
- limits note: The site describes a generated link as bound to the IP that requested it ('locked and only accessible to the user that initiated the link generator' on the sibling site). A link is therefore not portable between machines.
- binding note: Eight links a day fails long before any byte total at 1 TiB of monthly transfer, if the host files are large at all. The byte ceiling is unstated, so pull-count is the only number a user can plan against.
- interface detail: A single web form: paste the host URL, press generate, receive a link. The FAQ claims '+100 cloud platforms'. No API, key or CLI is published.
- tooling: browser only. A wrapper would have to POST the form; the request shape was not read.
- composes with: A zero-identity leecher for the occasional file on a host not subscribed to. Eight links a day is enough for a handful of files and useless for a queue, so it sits beside a paid debrid rather than replacing it.
- reliability: IP-locked links mean a VPN change or a CGNAT egress breaks the generated link mid-download; the site states no refund or retry path because nothing was paid.
- notes: DebridHub and OkDebrid publish near-identical copy, feature lists and the same 8-links-a-day cap. They are either one operator running two fronts or one template sold twice; published records both because a user will meet both names.
- evidence note: The vendor's own FAQ states the daily cap. A completed download through a generated link would raise this to measured, and would also establish whether large files actually pass.
- extras:
  - hosts_claimed: 100+
  - sibling_site_identical_copy: okdebrid.com
- evidence:
  - [1] 2026-10-23: 'You can process up to 8 premium links daily', the +100-host claim, the immediate link deletion, and the IP-locked access claim
- sources:
  - [1] https://debridhub.com/
