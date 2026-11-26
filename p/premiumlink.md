# PremiumLink.site

> premiumlink.site | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premiumlink/ | JSON https://fshy.ajam.dev/api/v1/entity/premiumlink.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PremiumLink.site

- `debrid/premiumlink-site` | qualifies-with-caveat | evidence documented | binding none | category premium link generator (free leech of host links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:32.906Z (live) | stale on 2026-12-04
- url https://premiumlink.site/
- free tier: 'Premiumlink - Free Premium Link Generator & File Hosting Leecher ... Get your free, direct download link instantly-no account required.' The page claims '1M+ Links Generated', '50K+ Active Users', '99.9% Uptime' and '100+ Hosts'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The counters are marketing figures with no methodology; no per-file, per-day or speed number is given.
- per-object cap: unstated: no per-file maximum published. | source: [1]
- retention: unverified: no retention statement. | source: [1]
- egress: No byte allowance or speed figure published. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: 'No registration required-just use, download, and enjoy.'
- interface: browser
- limits:
  - request-rate: unstated [1]
- limits note: The site's own numbers are popularity counters, not limits. There is no terms or FAQ page to check.
- binding note: No published constraint to bind; the unmeasured reality is the operator's host accounts and server capacity.
- interface detail: A single-page web form. No API, no documented endpoint.
- tooling: Nothing published.
- composes with: Interchangeable with any other free leech site among debrid providers; no cap means no planning value beyond a one-off fetch.
- reliability: unverified: no usable response from the origin on 2026-11-25; a direct probe returned status null with error tls_untrusted, and all read routes saw no content or a parked-domain redirect.
- notes: Included to document the shape of the class: an anonymous leech page that states no cap. It is not evidence that a free large-volume path exists, and it should not be counted as one. No programmatic path found: A single-page web form. No API, no documented endpoint.
- evidence note: The vendor page is captured and quoted: free, no account, 100+ hosts, popularity counters. No quota, per-file cap or retention is published; a direct probe from a residential ISP address ended in a connection reset, and no link generation was attempted, so nothing is measured.
- extras:
  - claimed_hosts: 100+
  - api: none found
- evidence:
  - [1] 2026-10-23: 'no account required', the 100+ host list (Rapidgator, Nitroflare, Uploaded, Keep2Share, Katfile...), and the 1M+/50K+/99.9% counters
  - probe:https://premiumlink.site/ 2026-10-23: no usable answer from this host at 01:56: connection reset ('Remote end closed connection without response'), status null, 0 bytes, no hash
  - [1] 2026-11-03: the vendor states free use with no account | capture: sha256:6805a0ca0b9f4fea2acc32e26779c694b94d7befdac6e85f5dcaaf8429eb4e9c | quote: Get your free, direct download link instantly—no account required.
  - [1] 2026-11-03: the page states no speed limit; it gives no per-file or per-day number | capture: sha256:6805a0ca0b9f4fea2acc32e26779c694b94d7befdac6e85f5dcaaf8429eb4e9c | quote: No more waiting, captchas, or download speed limits.
  - [1] 2026-11-03: no registration is required | capture: sha256:6805a0ca0b9f4fea2acc32e26779c694b94d7befdac6e85f5dcaaf8429eb4e9c | quote: No registration required—just use, download, and enjoy!
  - probe:https://premiumlink.site/ 2026-11-25: the direct probe got no HTTP status from the origin | capture: sha256:315dae00b89c1e2742ee9f1b704ec3d5aac0e1f67792219989b7dea35e689b7c | quote: "status": null
- sources:
  - [1] https://premiumlink.site/
