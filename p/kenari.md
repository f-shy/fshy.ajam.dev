# Kenari

> kenari.id | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kenari/ | JSON https://fshy.ajam.dev/api/v1/entity/kenari.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kenari

- `inference/kenari` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway, free models plus paid credits
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://kenari.id/docs/free-models
- free tier: models whose ID ends in :free are billed Rp 0 and callable with a new account and zero balance; a new account gets 50 requests/day and 5 requests/minute, rising to 1,000/day and 10/minute after a qualifying top-up and unlimited daily with 25/minute on an active plan; a keyless GET /v1/models lists them | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: free registration at kenari.id/login?daftar=1&next=/keys; top-up via QRIS is optional and no credit card is needed for the free models
- interface: rest
- limits:
  - request-rate (binding): new account: 50 requests/day and 5 requests/minute on free models; qualifying top-up raises to 1,000/day and 10/minute; active plan gives unlimited daily and 25/minute [1]
  - request-rate (binding): free models run best-effort; exceeding a limit returns HTTP 429 [2]
- binding note: the 50-per-day and 5-per-minute limit on a new zero-balance account binds first
- endpoint: https://kenari.id/v1
- tooling: an OpenAI- or Anthropic-compatible key; a built-in kenari-free route picks a free model
- composes with: pairs with any OpenAI-compatible agent through the free :free models; the scarce link is the 50/day and 5/minute ceiling on a new account
- reliability: no reliability event recorded
- notes: free models are best-effort and the daily/minute ceilings rise with top-up or a plan; the free public catalog is keyless.
- evidence note: the Indonesian-language free-models page and apex publish the Rp 0 :free suffix and the tiered request limits; exact numbers for a new account come from the apex page
- evidence:
  - [2] 2026-11-18: models ending in :free are billed Rp 0 and callable with a new zero-balance account | capture: sha256:8bf0248c5dee175280c204561af11a3bd2071205bce310f17aad257fe96a403b | quote: Model yang id-nya berakhiran `:free` ditagih Rp 0. Kamu bisa memanggilnya dengan akun baru dan saldo nol, dalam batas per menit dan batas harian yang naik saat kamu top up atau berlangganan.
  - [1] 2026-11-18: free model limits: 50/day and 5/minute on a new account, rising with top-up or plan | capture: sha256:3db508edfae44e861cfbe862319b20496de7a91882c49b6af01295a49951d041 | quote: Tanpa top up: 50 request per hari, 5 request per menit. - Sudah top up Rp 10.000: 1.000 request per hari, 10 request per menit. - Langganan aktif: tanpa batas harian, 25 request per menit.
- sources:
  - [1] https://kenari.id
  - [2] https://kenari.id/docs/free-models
