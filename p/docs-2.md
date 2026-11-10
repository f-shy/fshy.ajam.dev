# is-a.dev

> docs.is-a.dev | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docs-2/ | JSON https://fshy.ajam.dev/api/v1/entity/docs-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## is-a.dev

- `domains-dns/is-a-dev` | qualifies-with-caveat | evidence documented | binding write-gated | category free registrable subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:10.325Z (live) | stale on 2026-12-04
- url https://docs.is-a.dev/
- free tier: a free <name>.is-a.dev subdomain, registered by a pull request that adds one JSON file to the domains directory of the service's GitHub repository | unit: objects | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: no subdomain count per account is published on the pages read; only one single-letter subdomain per user is allowed
- retention: no expiry or renewal term is published; a subdomain lasts until the maintainers remove it or its JSON file is deleted by a pull request | source: [2]
- egress: no query cap published | metered: no | source: [3]
- identity: email | detail: a GitHub account of an individual; the only owner field the JSON file requires is the GitHub username, and a GitHub organisation account cannot register; no phone and no card are asked (https://docs.is-a.dev/domain-structure/)
- interface: git
- limits:
  - write-gated (binding): every registration and every later change is a pull request that a maintainer reviews; the service states it can deny any request for any reason, and review time is volunteer time with no published figure [2]
  - write-gated (binding): NS records are approved only in specific cases and are refused to an account without an is-a.dev subdomain held for at least 30 days; review takes usually 24 to 72 hours and up to 2 weeks [3]
  - write-gated (binding): a root subdomain must belong to a software-development-related project; the eligibility is part of the review [2]
- binding note: the operator reviews each request and states it can terminate a subdomain at any time for any reason, so the owner can withdraw the name; the zone is the operator's and the registrant holds records only, apart from approved NS cases
- interface detail: every create, change or delete is a pull request against the register repository with a JSON file per name; the supported record types are A, AAAA, CAA, CNAME, DS, MX, SRV, TLSA, TXT and a service-specific URL redirector, and NS only in approved cases
- tooling: git and a GitHub account; a pull request for each change, merged by a maintainer
- composes with: a CNAME to a free static host gives a named site; the zone is not yours (NS delegation is refused to an account that has held a subdomain for under 30 days and is otherwise decided case by case), so it cannot become a Cloudflare zone of its own by default
- reliability: the operator can remove a subdomain at any time for any reason, the service is run by volunteers and the TLS limit is per name because the suffix is on the Public Suffix List
- notes: Withdrawal binds first: a maintainer's pull-request review stands between the request and the name, and the operator can end the name at any time. The zone is not the registrant's, so there is no own zone, no Cloudflare zone and no wildcard certificate for the subdomain by default. The TLS limit does not bind, because the suffix is listed and each name counts alone against the Let's Encrypt limit.
- evidence note: the domain-structure, FAQ, quickstart and terms pages were read and quoted; the TLS statement is an inference from the Let's Encrypt registered-domain rule and the suffix's listing in the captured Public Suffix List
- evidence:
  - [1] 2026-11-03: registration is a pull request that adds a JSON file to the domains directory | capture: sha256:7893ea12c488accac0b0ba4d7feadeeac151cb479d541416be01e91c1363e7b6 | quote: To register a subdomain, submit a pull request with a new JSON file in the `domains` directory.
  - [1] 2026-11-03: the only required owner field is a GitHub username | capture: sha256:7893ea12c488accac0b0ba4d7feadeeac151cb479d541416be01e91c1363e7b6 | quote: `username`: Your GitHub username.
  - [2] 2026-11-03: the operator can terminate a subdomain at any time for any reason | capture: sha256:44a0a4517bed6442a132916cec318044e7dea12fbc746e6c2089f15920820306 | quote: We reserve the right to terminate your subdomain at any time, for any reason.
  - [2] 2026-11-03: the operator can deny any registration request for any reason | capture: sha256:44a0a4517bed6442a132916cec318044e7dea12fbc746e6c2089f15920820306 | quote: We reserve the right to deny any subdomain registration request for any reason.
  - [2] 2026-11-03: a subdomain must be registered to an individual GitHub account, not an organisation account | capture: sha256:44a0a4517bed6442a132916cec318044e7dea12fbc746e6c2089f15920820306 | quote: Subdomains must be registered to an individual GitHub account, and cannot be registered to a GitHub organisation account.
  - [2] 2026-11-03: root subdomains are for software-development-related projects | capture: sha256:44a0a4517bed6442a132916cec318044e7dea12fbc746e6c2089f15920820306 | quote: Subdomains are intended solely for individuals, software developer groups and non-commercial projects that are related to software development
  - [3] 2026-11-03: review is by volunteers and has no published time | capture: sha256:04da38c28de9de4605841d59128eaafa32a628ff2493a73aaf71145b89d5ef40 | quote: We're a team of volunteers, and is-a.dev is a side project for us, so review times can vary.
  - [3] 2026-11-03: NS delegation is refused to an account whose first is-a.dev subdomain is under 30 days old | capture: sha256:04da38c28de9de4605841d59128eaafa32a628ff2493a73aaf71145b89d5ef40 | quote: If you have not had an is-a.dev subdomain for at least 30 days, you will be denied due to security reasons.
  - [3] 2026-11-03: NS requests are decided at the operator's discretion | capture: sha256:04da38c28de9de4605841d59128eaafa32a628ff2493a73aaf71145b89d5ef40 | quote: We reserve the right to deny any NS request at our discretion for any reason.
  - [4] 2026-11-03: is-a.dev is an entry of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: hrsn.dev is-a.dev vps.hrsn.net
  - [5] 2026-11-03: Let's Encrypt counts 50 certificates per registered domain in 7 days and finds the registered domain with the Public Suffix List, so a listed suffix gives each name its own count | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: Up to 50 certificates can be issued per registered domain (or IPv4 address, or IPv6 /64 range) every 7 days.
- sources:
  - [1] https://docs.is-a.dev/domain-structure/
  - [2] https://github.com/is-a-dev/register/blob/main/TERMS_OF_SERVICE.md
  - [3] https://docs.is-a.dev/useful/faq.md
  - [4] https://publicsuffix.org/list/public_suffix_list.dat
  - [5] https://letsencrypt.org/docs/rate-limits/
