# MTempMail

> mtempmail.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mtempmail/ | JSON https://fshy.ajam.dev/api/v1/entity/mtempmail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MTempMail

- `email/mtempmail` | qualifies-with-caveat | evidence documented | binding retention-clamped | category disposable inbox and read API
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:37:19.395Z (live) | stale on 2026-12-20
- url https://mtempmail.com/
- free tier: a free disposable inbox created anonymously with no signup; the homepage states unlimited creation of new addresses and a 24-hour lifespan per address | unit: unlimited | metered on: none | read on: 2026-11-19 | source: [1] | note: 10 active domains including EDU-style .edu.pl domains, stated on the homepage. A private API key with dedicated rate limits is available in an account, but no account is needed for the public key.
- per-object cap: unverified: no first-party page states an inbox size or a per-message size cap | note: Attachment reception is stated on the help page without a size figure; no byte cap was found on the homepage, the API page or the help page.
- retention: Every MTempMail address and its messages are deleted automatically 24 hours after the address is created. | source: [1] | note: The help page repeats the 24-hour purge and states that messages deleted by it cannot be restored.
- egress: inbound receive-only; sending and replying are deliberately not allowed | metered: no | source: [2]
- identity: anonymous | detail: No email, name, password, or credit card needed. The API page states the offer needs no registration or credit card and publishes a public key.
- interface: rest
- limits:
  - retention-clamped (binding): 24 hours before an address and its messages are deleted [1]
  - request-rate: about 120 requests per minute per IP for the free public key [3]
  - request-rate: 60 requests per minute per IP for the standard free tier [2]
- binding note: the 24-hour purge deletes the message a caller is polling for, so it ends a workflow before either published per-IP request rate is reached
- interface detail: REST API at mtempmail.com/api for creating addresses, listing domains and reading messages with a published public key; a web inbox, a Telegram bot and mobile apps are also offered.
- endpoint: https://mtempmail.com/api
- tooling: curl, Python requests, Node.js fetch or PHP against the REST API; the public key is printed on the API page
- composes with: the verification-code sink: create an address with the public key, let a service deliver to it, then read the message back over REST; the 24-hour purge and the per-IP limit on the shared key decide how long and how often a test can poll
- reliability: the free public key is shared and rate-limited per IP; the help page states 60 requests per minute per IP while the API page states about 120. An inbox is not password-protected, so anyone who knows the exact address can open it.
- notes: Inbox size and per-message size cap are unverified: no first-party page publishes a number. The 10-domain figure and the 24-hour lifespan are stated on the homepage. The free public key is shared, and the two first-party rate figures conflict.
- evidence note: Anonymous creation, retention, domain count, receive-only behaviour, identity and API access are stated on first-party pages. Inbox size and the per-message size cap are unverified because no first-party page publishes a number.
- evidence:
  - [1] 2026-11-19: each address and its messages expire 24 hours after creation | capture: sha256:e590e6066e962c1803114ed456d120f329de7d5f889717128ee8c30f27fecd9d | quote: Every MTempMail address and its messages are deleted automatically 24 hours after the address is created.
  - [1] 2026-11-19: 10 active domains including EDU-style ones, and a 24-hour address lifespan | capture: sha256:e590e6066e962c1803114ed456d120f329de7d5f889717128ee8c30f27fecd9d | quote: MTempMail keeps each address for 24 hours, generates non-guessable addresses, lets you choose your own name across 10 domains including EDU-style ones, and delivers attachments to keep their main inboxes clean.
  - [1] 2026-11-19: no identity document, contact detail or card is asked for | capture: sha256:e590e6066e962c1803114ed456d120f329de7d5f889717128ee8c30f27fecd9d | quote: No email, name, password, or credit card needed.
  - [3] 2026-11-19: the API page sets a per-IP request rate of about 120 per minute for the public key | capture: sha256:38b7ff93e18e4ab1ac5bd8b7f7cb052c37232c6ccff14596ee6b6527b4dc6658 | quote: The free public key is rate-limited to about 120 requests per minute per IP.
  - [3] 2026-11-19: the API is open without an account or a card | capture: sha256:38b7ff93e18e4ab1ac5bd8b7f7cb052c37232c6ccff14596ee6b6527b4dc6658 | quote: It is free, needs no registration or credit card, and works from any programming language, script, or AI agent.
  - [2] 2026-11-19: the help page sets a per-IP request rate of 60 per minute on the free tier | capture: sha256:eb7597232a0e99d5003409f2a53e8322e2144e8edb8f9c023497d9693f654710 | quote: Standard free tier requests are rate-limited to 60 requests per minute per IP, which is plenty for automated QA test suites.
  - [2] 2026-11-19: the service receives mail only and does not allow sending | capture: sha256:eb7597232a0e99d5003409f2a53e8322e2144e8edb8f9c023497d9693f654710 | quote: Free Edu & .COM Temporary Mails is strictly an inbound receive-only service. We deliberately do not allow sending or replying, to prevent spammers from abusing our mail servers.
  - [2] 2026-11-19: no identity detail or card is required, and messages are purged after 24 hours | capture: sha256:eb7597232a0e99d5003409f2a53e8322e2144e8edb8f9c023497d9693f654710 | quote: We do not require your real name, physical location, or credit card for free disposable email generation, and all incoming emails are deleted automatically after 24 hours.
  - [2] 2026-11-19: the help page confirms the 24-hour message purge | capture: sha256:eb7597232a0e99d5003409f2a53e8322e2144e8edb8f9c023497d9693f654710 | quote: Incoming messages are automatically deleted after 24 hours to safeguard your privacy and maintain optimal server performance.
- sources:
  - [1] https://mtempmail.com/
  - [2] https://www.mtempmail.com/help
  - [3] https://mtempmail.com/page/api
