# GrosFichiers

> grosfichiers.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/grosfichiers/ | JSON https://fshy.ajam.dev/api/v1/entity/grosfichiers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GrosFichiers

- `debrid/grosfichiers` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file transfer service (free with ads, paid packs) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://www.grosfichiers.com/questions-frequentes?faqID=faq1
- price unverified: the pack price page was not read
- free tier: Free transfers up to 10 Go per transfer, no account, 30 recipients, files available 14 days. | unit: GB | metered on: uploaded-bytes | read on: 2026-11-03 | source: [1] | note: The page is in French; Go is gigabyte.
- per-object cap: Sans pack, GrosFichiers permet d'envoyer gratuitement jusqu'à 10 Go par transfert. Avec un pack, la taille maximale passe à 50 Go par transfert. | bytes: 10737418240 | source: [1] | note: bytes = 10 x 1024^3; the cap is per transfer, not per file.
- retention: Ceux-ci restent disponibles pendant 14 jours, avec possibilité de prolonger gratuitement leur disponibilité. | days: 14 | source: [1] | note: Availability can be extended for free.
- egress: The recipient downloads from an emailed link; no download byte cap is printed. | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: 'Il suffit de disposer d'une adresse email valide pour envoyer vos fichiers.' No account is created.
- interface: unknown
- limits:
  - per-object-cap (binding): 10 Go per transfer free, 50 Go with a pack [1]
  - retention-clamped: 14 days, extendable for free [1]
- binding note: 10 Go per transfer is the published free ceiling.
- interface detail: Web upload; links are delivered by email to up to 30 recipients.
- tooling: Browser only as read.
- composes with: A transfer needs a valid email address and mails a link to each recipient, so it suits one-off hand-off.
- reliability: The free service is funded by advertising; the Standard and Pro pack prices are on a separate page that was not read.
- evidence note: FAQ read on 2026-11-03. Pack prices unverified.
- evidence:
  - [1] 2026-11-03: the free cap is 10 Go per transfer and 50 Go with a pack | capture: sha256:cf7e5d4f962a11ce0c2d5d0844917484f9f1fd96b12d663aa646ffb358fb4e63 | quote: Sans pack, GrosFichiers permet d'envoyer gratuitement jusqu'à 10 Go par transfert. Avec un pack, la taille maximale passe à 50 Go par transfert.
  - [1] 2026-11-03: files stay available 14 days | capture: sha256:cf7e5d4f962a11ce0c2d5d0844917484f9f1fd96b12d663aa646ffb358fb4e63 | quote: Ceux-ci restent disponibles pendant 14 jours, avec possibilité de prolonger gratuitement leur disponibilité.
  - [1] 2026-11-03: a valid email address is the only requirement | capture: sha256:cf7e5d4f962a11ce0c2d5d0844917484f9f1fd96b12d663aa646ffb358fb4e63 | quote: Il suffit de disposer d'une adresse email valide pour envoyer vos fichiers.
- sources:
  - [1] https://www.grosfichiers.com/questions-frequentes?faqID=faq1
