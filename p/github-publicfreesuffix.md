# Public Free Suffix

> github.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-publicfreesuffix/ | JSON https://fshy.ajam.dev/api/v1/entity/github-publicfreesuffix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Public Free Suffix

- `domains-dns/public-free-suffix` | qualifies-with-caveat | evidence documented | binding write-gated | category free registrable subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:41.766Z (live) | stale on 2026-12-20
- url https://github.com/PublicFreeSuffix/PublicFreeSuffix
- free tier: one free label under any of six live suffixes (bg5.net, is-a.si, nastu.net, tun.re, us.mw, pfsdns.org), resolved on the operator's DNS with A, AAAA, MX, NS, CAA, TXT, CNAME, ALIAS and HTTPS records; no annual fees | unit: objects | metered on: object-count | read on: 2026-11-03 | source: [1]
- per-object cap: one label under a suffix, never a nested name: myname.is-a.si works and my.name.is-a.si does not; the number of labels per account is not stated on the page read
- retention: a domain left empty for 30 consecutive days is reclaimed; no renewal term is stated | days: 30 | source: [1]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: an account on the operator's console with a verified GitHub account at least 2 years old; no phone and no card are named on the README
- interface: browser
- limits:
  - write-gated (binding): a GitHub account at least 2 years old is required, and the account is verified in the console [1]
  - retention-clamped: a domain with no content for 30 consecutive days is reclaimed [1]
- binding note: the GitHub-account-age check is the gate and the 30-day empty-name reclaim is the clock; the operator can reclaim a name, so the owner of the suffix can withdraw it; the zone is on the operator's DNS unless the registrant sets NS records
- interface detail: a web console at s.eus/domains for search, registration and every DNS record; the earlier git pull-request registration flow is retired; no dyndns update URL was found; a REST API and MCP are named only for the BYOS suffix-operator program, with no documented endpoint or open to ordinary registrants
- tooling: the SEUS domain console, then any host that takes a DNS record
- composes with: a label with NS records offered in the same console, so delegation to an external DNS service is a record the registrant can set; the suffixes were not found in the captured Public Suffix List, so each name shares one Let's Encrypt count with every user of the suffix
- reliability: an empty name is reclaimed after 30 consecutive days, the operator can end a name, the flow changed from pull requests to a console within 2025 to 2026, and the suffixes are not on the Public Suffix List, which is an inference from absence
- notes: Two binds: the account-age gate, and an operator clock that reclaims an empty name after 30 days, so the owner of the suffix can withdraw it. The zone starts on the operator's DNS, and NS records let the registrant delegate. The TLS limit is a risk here: the suffixes have no entry in the captured Public Suffix List, so each suffix is one registered domain for Let's Encrypt, which is an inference from absence.
- evidence note: the repository README was read and quoted; the console and the agreements were not read; the Public Suffix List statement is an inference from the absence of an entry and cannot be quoted
- evidence:
  - [1] 2026-11-03: six live suffixes and one label under any of them | capture: sha256:b4bd7a3031d462d47f114f1dfd85c05b85579926e02ad5d1a42f826b38c58029 | quote: Six live zones. One label under any suffix, while names last.
  - [1] 2026-11-03: a verified GitHub account at least 2 years old is required | capture: sha256:b4bd7a3031d462d47f114f1dfd85c05b85579926e02ad5d1a42f826b38c58029 | quote: Your GitHub account must be at least 2 years old; verification keeps the zone safe for everyone.
  - [1] 2026-11-03: an empty name is reclaimed after 30 consecutive days | capture: sha256:b4bd7a3031d462d47f114f1dfd85c05b85579926e02ad5d1a42f826b38c58029 | quote: Domains left empty for 30 consecutive days are reclaimed, so names go to people who actually use them.
  - [1] 2026-11-03: the console hosts the zone and offers A, AAAA, MX, NS, CAA, TXT, CNAME, ALIAS and HTTPS records | capture: sha256:b4bd7a3031d462d47f114f1dfd85c05b85579926e02ad5d1a42f826b38c58029 | quote: A, AAAA, MX, NS, CAA, TXT, CNAME, ALIAS, HTTPS, and more, all managed in the same console.
  - [1] 2026-11-03: a name is a single label under the suffix | capture: sha256:b4bd7a3031d462d47f114f1dfd85c05b85579926e02ad5d1a42f826b38c58029 | quote: A domain is a single label under the suffix: `myname.is-a.si` works, `my.name.is-a.si` does not.
  - [1] 2026-11-03: there are no annual fees | capture: sha256:b4bd7a3031d462d47f114f1dfd85c05b85579926e02ad5d1a42f826b38c58029 | quote: No annual fees, ever.
  - [1] 2026-11-03: the pull-request registration flow has been retired in favour of the console | capture: sha256:b4bd7a3031d462d47f114f1dfd85c05b85579926e02ad5d1a42f826b38c58029 | quote: That flow has been retired;
  - [2] 2026-11-03: Let's Encrypt counts 50 certificates per registered domain in 7 days, and finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: Up to 50 certificates can be issued per registered domain (or IPv4 address, or IPv6 /64 range) every 7 days.
  - [1] 2026-11-19: registration, search and DNS record management all run through the web domain console; no programmatic interface is named | capture: sha256:2cdadbf5a9e31b384c6000562dfc88f2e43a63669201e0a35ad911ba8f743d6a | quote: Everything runs through the [domain console](https://s.eus/domains): no pull requests, and no waiting on email verification. From search to a resolving name takes minutes.
  - [3] 2026-11-19: the API and MCP are described only for the BYOS private-mode suffix operator, not for ordinary free-label registrants | capture: sha256:ed95ad54edf102b9cabed8cdf11beb4098379d659ff5f36eb8d091d1be034506 | quote: Private mode is where the API shines. Registration and DNS management are fully callable, and MCP support comes included, so you can put your own registration site, your own dashboard, or your own user community on top of a suffix you control end to end.
  - [4] 2026-11-19: DNS records are created and updated in the same web console | capture: sha256:2636875b27ffe08fe0d87fbcc45526d6a8ba3060ba86399253f8ca0e2f2e2b9b | quote: You add records in the same console where you registered, and the name resolves.
- sources:
  - [1] https://github.com/PublicFreeSuffix/PublicFreeSuffix
  - [2] https://letsencrypt.org/docs/rate-limits/
  - [3] https://publicfreesuffix.org/blog/introducing-seus-byos/
  - [4] https://publicfreesuffix.org/blog/introducing-seus-dns
