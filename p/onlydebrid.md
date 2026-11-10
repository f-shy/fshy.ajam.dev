# OnlyDebrid

> onlydebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onlydebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/onlydebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OnlyDebrid

- `debrid/onlydebrid` | paid-only | evidence documented | binding none | category multi-hoster (premium link generator) | tier Premium (yearly)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://onlydebrid.com/
- free tier: unverified: the registration page says 'Free account · Premium upgrades available from your account' and states no free allowance | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: Per host transfer limit is listed as Unlimited for the hosts on the supported-hosts table. | source: [2]
- retention: unverified: not stated | source: [3]
- egress: Premium connections to supported hosts; the supported-hosts table lists a transfer limit column, Unlimited for the rows read. | metered: no | free allowance: none stated | source: [2]
- identity: email | detail: Registration asks for an email address, a password of 8+ characters and a confirmation.
- interface: unknown
- limits:
  - per-ip-shaping: unverified: no concurrency or address rule stated [3]
- binding note: The supported-hosts table lists Unlimited transfer for the hosts read, so no cap is published to name.
- interface detail: Web generator: paste a URL, generate a premium link, download.
- tooling: Browser only on the pages read.
- composes with: $6.99 per year is the headline price; the supported-hosts table shows per-host status (Working, Not live).
- reliability: The host table marks some hosts Not live, so coverage changes between reads.
- notes: The page says $6.99 per year without naming the plan; the billing term is read from that line.
- evidence note: First-party home page, registration page and supported-hosts table.
- evidence:
  - [3] 2026-11-03: the headline price is $6.99 per year | capture: sha256:d883978e2fdb0dedeeaffa60deb7948466219aba8aa655bdde78ae2adc39a260 | quote: $ 6.99/ year
  - [3] 2026-11-03: premium link generator with 50+ filehosts | capture: sha256:d883978e2fdb0dedeeaffa60deb7948466219aba8aa655bdde78ae2adc39a260 | quote: ✓ Premium link generator✓ 50+ supported filehosts✓ One easy workflow
  - [2] 2026-11-03: the host table has a transfer limit column | capture: sha256:62a7ecf03b45016aed6c51b46efb0c70848c127afccdbed355774c57d4672ead | quote: | FILEHOST | TRANSFER LIMIT | STATUS |
  - [2] 2026-11-03: 1fichier is listed with an Unlimited transfer limit | capture: sha256:62a7ecf03b45016aed6c51b46efb0c70848c127afccdbed355774c57d4672ead | quote: | [1fichier.com](https://www.onlydebrid.com/1fichier) | Unlimited | Working |
  - [1] 2026-11-03: registration asks for email and password | capture: sha256:019aaee2aa7b710c3b382e3fb608c9006aebdc285701b501ecd74c9347ca17ef | quote: EMAIL ADDRESS PASSWORD8+ CHARACTERS CONFIRM PASSWORD
  - [1] 2026-11-03: a free account exists and premium is an upgrade | capture: sha256:019aaee2aa7b710c3b382e3fb608c9006aebdc285701b501ecd74c9347ca17ef | quote: Free account · Premium upgrades available from your account
- sources:
  - [1] https://www.onlydebrid.com/register
  - [2] https://www.onlydebrid.com/supported-hosts
  - [3] https://onlydebrid.com/
