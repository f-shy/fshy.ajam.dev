# mail.lesin.org

> lesin.org | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lesin/ | JSON https://fshy.ajam.dev/api/v1/entity/lesin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mail.lesin.org (TempMail)

- `email/mail-lesin-org` | qualifies-with-caveat | evidence documented | binding retention-clamped | category disposable inbox with a separate paid developer API | tier free disposable inbox
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:49:45.930Z (live) | stale on 2026-12-20
- url https://mail.lesin.org/
- free tier: Free disposable inbox, no registration and no personal details; the developer email API is a separate paid offer at USD 5/month; no numeric storage quota is published | unit: mixed | metered on: unstated | read on: 2026-11-19 | source: [1] | note: mixed is used because the free disposable inbox carries no published numeric quota. The live host mail.lesin.org has no current A or AAAA record, so the first-party pages were read from Wayback snapshots captured 2026-03-27.
- per-object cap: unverified: no per-message size cap is published on the first-party pages | source: [1] | note: No message size figure appears on the main page, about, terms, privacy or blog pages.
- retention: All temporary emails and addresses are automatically deleted after 24 hours; the inbox offers manual auto-delete timers of 10 minutes, 30 minutes, 1 hour, 6 hours and 24 hours | days: 24 | source: [2] | note: The 24-hour figure is stated on both the terms and the privacy page.
- egress: not applicable: a receive-only disposable inbox; mail is delivered in via SMTP and read back over the web UI or the retrieval API | metered: no | source: [1]
- identity: anonymous | detail: TempMail is a free temporary email service that allows you to receive emails without registration. No registration, no personal information required. The paid API asks for an account and payment, but the free disposable inbox needs no key, email or card.
- interface: rest
- limits:
  - retention-clamped (binding): all temporary emails and addresses are deleted after 24 hours [2]
  - per-object-cap: unverified: no per-message size cap is published on first-party pages [1]
- binding note: the 24-hour automatic deletion caps how long a verification code can be read; no message size cap or published rate limit binds earlier
- interface detail: The free disposable inbox is a web UI with an outbound webhook that POSTs JSON on arrival. A separate paid private REST API exposes inbox, HTML view and code-retrieval endpoints for scripts.
- tooling: any HTTP client for the paid private REST API; a web browser for the free disposable inbox
- composes with: verification-code sink: create an inbox with no key, let a service deliver a code to it, then read the message back over the paid retrieval API; the scarce links are the 24-hour deletion and the unpublished message cap
- reliability: messages and addresses are deleted after 24 hours, so a code must be read inside that window; the operator states that emails may be delayed or lost; the live host has no current DNS record, so availability is unverified
- notes: Inbox size and per-message size cap are unverified: no first-party page publishes figures. The seven domains on the captured page are iopia.org, karsus.org, kvarra.org, aatrox.org, ambes.org, angues.org and ayuta.org. The live host mail.lesin.org has no current A or AAAA record; the first-party pages were read from Wayback snapshots captured 2026-03-27. The free disposable inbox is hosted; the developer API is a separate paid offer, not software the reader installs.
- evidence note: all figures come from first-party pages captured from Wayback snapshots of 2026-03-27; the live host did not resolve, and no probe was run, so the rung stays documented
- evidence:
  - [3] 2026-11-19: the service is free and an inbox is created without registration | capture: sha256:dfbdc31eca092f5b2bb2fce8c7c8b2cb1e74381ee63bb942ebaad80182a122f8 | quote: TempMail is a free temporary email service that allows you to receive emails without registration.
  - [3] 2026-11-19: inbox creation is anonymous: no registration and no personal details | capture: sha256:dfbdc31eca092f5b2bb2fce8c7c8b2cb1e74381ee63bb942ebaad80182a122f8 | quote: No registration, no personal information required.
  - [1] 2026-11-19: the developer email API is a separate paid offer at USD 5 per month | capture: sha256:1923132044cd5606da10cdcf5784cc8996e025b3efe91a70abf1638ab36f253b | quote: Get your own dedicated domain · Receive unlimited emails · Extract codes instantly via API · IP protected · $5/month
  - [1] 2026-11-19: an inbox supports up to five aliases feeding the same mailbox | capture: sha256:1923132044cd5606da10cdcf5784cc8996e025b3efe91a70abf1638ab36f253b | quote: Create up to 5 aliases. All emails go to your main inbox.
  - [1] 2026-11-19: a webhook delivers a JSON POST to a caller URL when mail arrives | capture: sha256:1923132044cd5606da10cdcf5784cc8996e025b3efe91a70abf1638ab36f253b | quote: We'll POST JSON data to this URL when emails arrive
  - [1] 2026-11-19: the inbox offers a user-set automatic deletion timer | capture: sha256:1923132044cd5606da10cdcf5784cc8996e025b3efe91a70abf1638ab36f253b | quote: Automatically delete this inbox after a set time.
  - [1] 2026-11-19: the custom-email selector lists seven domains: iopia.org, karsus.org, kvarra.org, aatrox.org, ambes.org, angues.org, ayuta.org | capture: sha256:1923132044cd5606da10cdcf5784cc8996e025b3efe91a70abf1638ab36f253b | quote: DomainRandomiopia.orgkarsus.orgkvarra.orgaatrox.orgambes.organgues.orgayuta.org
  - [2] 2026-11-19: messages are deleted after 24 hours | capture: sha256:a039cde79b24227158c7db9ed36056ac0c0275a88c9f68741bb730fada338153 | quote: All temporary emails are automatically deleted after 24 hours
  - [4] 2026-11-19: both addresses and messages have a 24-hour deletion window | capture: sha256:bb2f3b4c4d736507f7a2d39d73605d36ae5f01ac5d8774fea1c802ee9de48bad | quote: All emails and temporary addresses are automatically deleted after 24 hours. We do not store personal information or email content permanently.
- sources:
  - [1] https://mail.lesin.org/
  - [2] https://mail.lesin.org/terms
  - [3] https://mail.lesin.org/about
  - [4] https://mail.lesin.org/privacy
