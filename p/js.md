# JS.ORG

> js.org | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/js/ | JSON https://fshy.ajam.dev/api/v1/entity/js.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JS.ORG

- `domains-dns/js-org` | qualifies-with-caveat | evidence documented | binding write-gated | category free registrable subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:10.325Z (live) | stale on 2026-12-04
- url https://js.org/
- free tier: free <name>.js.org subdomains for JavaScript-ecosystem sites, added by a pull request to the js-org/js.org repository; the new URL goes live within 24 hours | unit: objects | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: no subdomain count per user is published on the pages read; the name must follow the GitHub Pages username or repository name
- retention: no expiry or renewal term is published; the user ends it by removing the entry in a pull request, and the operator may end a subdomain, or all of them, with at least 7 days of notice | source: [2]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: a GitHub account; the steps ask the user to log in to GitHub and open a pull request, and name no phone, card or ID
- interface: git
- limits:
  - write-gated (binding): a pull request is reviewed against the rule that a site must be directly related to the JavaScript ecosystem and carry substantive content; a naming conflict or a change request can hold it [1]
  - retention-clamped: the user acquires no ownership of the subdomain, and the operator may terminate a certain subdomain or all of them with at least 7 days of notice by an issue in the user's repository [2]
- binding note: the review gate is the first constraint and the operator can end any name on 7 days of notice; records are CNAME only and the zone is not the registrant's
- interface detail: a pull request adds the name to the subdomains list file cnames_active.js of the repository; every entry is a CNAME to a host, so no other record type is offered
- tooling: git and a GitHub account; a CNAME file in a GitHub Pages repository or a custom-domain setting at another host
- composes with: a CNAME to GitHub Pages or another host that accepts a custom domain by CNAME; the zone is the operator's and sits on Cloudflare's free plan, so it cannot be a zone of the registrant's
- reliability: the service states no right to constant availability and may end a subdomain on 7 days of notice; the suffix is on the Public Suffix List, so the TLS limit counts per name
- notes: The owner can withdraw the name on 7 days of notice and a review gates the start. The zone is not the registrant's and offers CNAME only, so no apex records, no mail and no own zone. The TLS limit does not bind, because the suffix is listed and each name counts alone.
- evidence note: the repository README, the terms page and the subdomain-determination wiki page were read and quoted; the TLS statement is an inference from the Let's Encrypt registered-domain rule and the suffix's listing in the captured Public Suffix List
- evidence:
  - [1] 2026-11-03: a pull request adds the name and goes live within 24 hours unless a conflict or change request holds it | capture: sha256:4ce3f8336ada918579e4f9482ba63c236c1e7d329593d5687a1a724daae185fd | quote: Your new URL should go live within 24 hours (keep an eye on your pull request in case of a naming conflict or if there are requested changes).
  - [1] 2026-11-03: content must be directly related to the JavaScript ecosystem | capture: sha256:4ce3f8336ada918579e4f9482ba63c236c1e7d329593d5687a1a724daae185fd | quote: Websites must be directly related to the JavaScript ecosystem/community
  - [1] 2026-11-03: the host must accept a custom domain through a CNAME record, so the registrant sets no other record type | capture: sha256:4ce3f8336ada918579e4f9482ba63c236c1e7d329593d5687a1a724daae185fd | quote: Note that to use JS.ORG, your hosting provider will need to support adding custom domains via a CNAME DNS record.
  - [1] 2026-11-03: registration needs a GitHub account | capture: sha256:4ce3f8336ada918579e4f9482ba63c236c1e7d329593d5687a1a724daae185fd | quote: If you haven't already, log in to your GitHub account and set up your GitHub Pages site following
  - [2] 2026-11-03: the user acquires no ownership of the registered subdomains | capture: sha256:8b4bc4a094a65451512c31a4f044c70f1153829294ca5faa018ba3787a829c93 | quote: The user acquires no ownership or other rights to single services, the registered subdomains and the whole service.
  - [2] 2026-11-03: the operator may terminate a subdomain or all subdomains with at least 7 days of notice | capture: sha256:8b4bc4a094a65451512c31a4f044c70f1153829294ca5faa018ba3787a829c93 | quote: JS.ORG may also terminate the provision of a certain or all subdomains. Concerned users will be notified at least 7 days in advance by an issue in their GitHub repository
  - [3] 2026-11-03: JS.ORG is an entry of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // JS.ORG : http://dns.js.org
  - [4] 2026-11-03: Let's Encrypt counts 50 certificates per registered domain in 7 days and finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
- sources:
  - [1] https://github.com/js-org/js.org
  - [2] https://js.org/terms.html
  - [3] https://publicsuffix.org/list/public_suffix_list.dat
  - [4] https://letsencrypt.org/docs/rate-limits/
