# nsupdate.info

> nsupdate.info | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nsupdate/ | JSON https://fshy.ajam.dev/api/v1/entity/nsupdate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## nsupdate.info

- `domains-dns/nsupdate-info` | fails-identity | evidence documented | binding none | category free dynamic subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-04T01:33:33.616Z (live) | stale on 2026-12-05
- url https://www.nsupdate.info/
- free tier: a free dynamic DNS service on the nsupdate.info suffix, several hosts per user, with no ads or spam | unit: objects | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the pages read say multiple hosts per user and publish no number
- retention: unverified: no expiry, inactivity or confirmation rule is stated on the pages read | source: [2]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: new account registration is closed on the public service; the sign-up page states that registration of new accounts is currently not possible, and the software's feature list names local or remote account login
- interface: rest
- binding note: no count, expiry or review is published on the pages read, so no limit binds there; the zone is the operator's
- interface detail: dynamic updates by the dyndns2 protocol that many routers and clients speak, with a separate secret for each host; a browser-based updater and a manual web update also exist
- tooling: any dyndns2 client or router, curl, or the web interface
- composes with: a free name for a changing address; the zone is the operator's, so it cannot be a Cloudflare zone; the project is open-source software that can also be run by the user on a machine of their own, which ranks after every hosted offer
- reliability: an operator-run public service whose count and expiry rules were not found; the suffix is on the Public Suffix List, so the TLS limit counts per name
- notes: This record is the hosted public service. The count and the withdrawal rule are unverified. The zone is the operator's. The TLS limit does not bind, because the suffix is listed.
- evidence note: the home page and the documentation introduction were read and quoted; no count, expiry or sign-up form was read; the TLS statement is an inference from the Let's Encrypt registered-domain rule and the Public Suffix List entry
- evidence:
  - [1] 2026-11-03: the public service is free | capture: sha256:79e8f61103f26e22f05f9e80aea55cee188253c942ea63d886b044177b642a5c | quote: www.nsupdate.info is a free service.
  - [2] 2026-11-03: a user can have several hosts, each with its own secret | capture: sha256:19a78def4cc74cc04f1d7a7e91f0b71359a77b147f41e120badfbf9046e2c17e | quote: Multiple Hosts per user (using separate secrets for security)
  - [2] 2026-11-03: login is by a local account or a remote account such as Google or GitHub | capture: sha256:19a78def4cc74cc04f1d7a7e91f0b71359a77b147f41e120badfbf9046e2c17e | quote: Login with local or remote accounts (Google, GitHub, Bitbucket, … accounts - everything supported by the python-social-auth package)
  - [2] 2026-11-03: the software is open source and can be hosted by the user, which is the self-run lane | capture: sha256:19a78def4cc74cc04f1d7a7e91f0b71359a77b147f41e120badfbf9046e2c17e | quote: nsupdate.info is also the name of the software used to implement it. If you like, you can use it to host the service on your own server.
  - [3] 2026-11-03: nsupdate.info is an entry of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // nsupdate.info : https://www.nsupdate.info/
  - [4] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
  - [5] 2026-11-04: the sign-up page states that new accounts cannot be registered | capture: sha256:961628dfdffe2b3f94c805f76ad2ff55f3a1f85d50fc60613ffcbdef2b7a5616 | quote: Registration of new accounts is currently not possible.
- sources:
  - [1] https://www.nsupdate.info/
  - [2] https://nsupdateinfo.readthedocs.io/en/latest/intro.html
  - [3] https://publicsuffix.org/list/public_suffix_list.dat
  - [4] https://letsencrypt.org/docs/rate-limits/
  - [5] https://www.nsupdate.info/account/register/
