# TempsMail

> tempsmail.org | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tempsmail/ | JSON https://fshy.ajam.dev/api/v1/entity/tempsmail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TempsMail

- `email/tempsmail` | qualifies-with-caveat | evidence documented | binding request-rate | category disposable inbox API
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://tempsmail.org/page/api
- free tier: a disposable inbox and read API, free with an account key | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated on the API page
- retention: messages expire; the period is not stated on the API page | source: [1]
- egress: not applicable: receive-only | metered: no | source: [1]
- identity: email | detail: a free account with a verified address, to obtain the API key
- interface: rest
- limits:
  - request-rate (binding): 100 requests/minute per IP across the API [1]
  - request-rate (binding): 30 address creations/minute per IP [1]
- limits note: the inbox is bound to the IP and client that created it, which is a lock rather than a rate and none of the six kinds names it
- interface detail: POST /api/extension/emails/{apiKey} and the read endpoints
- tooling: curl, any HTTP client
- composes with: the same verification-code sink as mail.tm with one extra gate: an account key, and an inbox bound to the IP that created it.
- reliability: the inbox is bound to the creating IP, so it cannot be read from a second machine
- notes: The page requires an account and a personal key, and it binds the inbox to the IP and client that created it. Both facts change what a chain can do with the service, and neither is a no-key API.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: 'Free with an account', '100 requests / minute per IP', '30 address creations / minute per IP', and the IP binding of a created inbox
- sources:
  - [1] https://tempsmail.org/page/api
