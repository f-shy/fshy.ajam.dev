# FS.TO

> rbc.ua | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rbc/ | JSON https://fshy.ajam.dev/api/v1/entity/rbc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FS.TO

- `debrid/fs-to` | dead | evidence documented | binding write-gated | category Ukrainian file host / online cinema (servers seized 2016) | tier closed
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:58:40.528Z (live) | stale on 2026-12-27
- url https://daily.rbc.ua/rus/show/fayloobmenniki-berut-abordazh-pochemu-zakryvayutsya-1479386850.html
- free tier: Closed. 'Департамент киберполиции Национальной полиции Украины 15 ноября [2016] изъял сервера одного из крупнейших в Украине онлайн-кинотеатров fs.to. Ресурс прекратил работу по основному адресу.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the service is closed | source: [1] | note: unstated
- retention: not applicable: the servers were seized | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: not applicable: no account can be created | country: Ukraine
- interface: unknown
- limits:
  - write-gated (binding): servers seized 2016-11-15; service stopped at the main address [1]
- limits note: The article names a claimed relocation ('Киберполиция изъяла сервера только на территории Украины') posted on a VK page; the claim is unverified and no live successor was found.
- binding note: Nothing is served; the closure is the fact.
- interface detail: None at the main address. A VK page claiming to be official announced a move to a new domain, according to the same report; no working replacement was verified.
- tooling: None verified.
- composes with: Nothing to chain. Like EX.UA it explains why the Ukrainian market has no domestic large host and why the debrid Ukrainian record is a seedbox (seedbox-org-ua) rather than a host.
- reliability: | [fs.to](https://fs.to) | FS stands for File Sharing. | [.to](https://www.iana.org/domains/root/db/to.html) | Cloudflare | Cloudflare | [View](https://dnssec-analyzer.verisignlabs.com/fs.to) | ✓ |
- notes: Recorded with FS.TO's sibling EX.UA so the pair is closed together. No live successor was found, and the VK relocation claim is not treated as one.
- evidence note: The seizure date, the actor and the stopped service are quoted from RBC-Ukraine's report of 2016-11-17, read. The relocation claim is a quote of an unverified VK post and is labelled as such. Evidence dates normalised to the read date on 2026-10-23; a source that carries its own date keeps it in the proved field.
- evidence:
  - [1] 2026-10-23: the 2016-11-15 seizure of FS.TO's servers by Ukraine's cyberpolice, the service stopping at its main address, and the unverified VK relocation claim
  - probe:https://fs.to/ 2026-11-26: a GET to fs.to on 2026-11-26 redirected to a different host | capture: sha256:f881ce49d889da6ba39abb2e649a55a8fb25e7a12f3af024b763fa1774dae529 | quote: "location":"https://s.ee/docs/official-domains/"
  - [1] 2026-11-26: the 2016 report says Ukraine's cyberpolice seized fs.to servers on 15 November | capture: sha256:9c2c011bde6a77b663f40a1d7c4469bbfd99bf00eaa21d3bd8d4675dbb5b6423 | quote: Департамент киберполиции Национальной полиции Украины 15 ноября изъял сервера одного из крупнейших в Украине онлайн-кинотеатров fs.to.
  - [2] 2026-11-26: the first-party page names fs.to as an official S.EE file-sharing domain | capture: sha256:f9a5f1b9aa6480c88619a7dd8460b5442d0a52e87a80a70f1db3b4e728fde0be | quote: | [fs.to](https://fs.to) | FS stands for File Sharing. | [.to](https://www.iana.org/domains/root/db/to.html) | Cloudflare | Cloudflare | [View](https://dnssec-analyzer.verisignlabs.com/fs.to) | ✓ |
  - [1] 2026-11-26: the report states the cyberpolice seizure of fs.to servers on 15 November | capture: sha256:9c2c011bde6a77b663f40a1d7c4469bbfd99bf00eaa21d3bd8d4675dbb5b6423 | quote: Департамент киберполиции Национальной полиции Украины 15 ноября изъял сервера одного из крупнейших в Украине онлайн-кинотеатров fs.to.
- sources:
  - [1] https://daily.rbc.ua/rus/show/fayloobmenniki-berut-abordazh-pochemu-zakryvayutsya-1479386850.html
  - [2] https://s.ee/docs/official-domains/
