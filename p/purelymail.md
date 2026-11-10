# Purelymail

> purelymail.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/purelymail/ | JSON https://fshy.ajam.dev/api/v1/entity/purelymail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Purelymail

- `email/purelymail` | paid-only | evidence documented | binding request-rate | category custom-domain email hosting | tier Simple pricing
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T05:33:22.972Z (live) | stale on 2026-12-05
- url https://purelymail.com/pricing
- free tier: no free plan: Simple pricing is $10 a year with no hard limits on users, custom domains or storage; a trial account starts with a limited credit balance and needs an SMS-capable phone | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: Advanced pricing bills resources instead: storage $0.56 per compressed GB per year, a $4.00 yearly account fee, $0.23 per 1000 external sends plus $0.18 per GB, $0.03 per 1000 received plus $0.04 per GB, and no charge for custom domains or users on owned domains. Significant overuse of Simple pricing may require a switch to Advanced pricing.
- per-object cap: unverified: no maximum message or attachment size is stated on the captured pages
- retention: no hard storage limit on Simple pricing; storage on Advanced pricing costs $0.56 per compressed GB per year | source: [2]
- egress: not applicable: a mailbox; external sending is rate limited to approximately 3000 messages per day, or 300 at once, per account | metered: yes | free allowance: approximately 3000 external messages per day | source: [3]
- identity: card | detail: the paid signup charges $10 through Stripe; the free trial needs an SMS-capable phone to activate. Signup asks for an administrator username on a shared domain and a password, with a recovery email or phone recommended.
- interface: unknown, webdav
- limits:
  - request-rate (binding): approximately 3000 external messages per day, or 300 at once, per account [3]
  - request-rate (binding): very low external sending limits on trial accounts [3]
- binding note: Simple pricing sets no hard limit on users, domains or storage, so the external sending rate is the first stated ceiling.
- interface detail: IMAP at imap.purelymail.com (993, SSL/TLS), SMTP at smtp.purelymail.com (465 SSL/TLS, or 587 with STARTTLS), POP3 at pop3.purelymail.com (995), ManageSieve at mailserver.purelymail.com (4190); WebDAV, CardDAV and CalDAV for basic file storage, contacts and calendars
- tooling: any IMAP, POP3 or SMTP client; IMAP IDLE; Sieve filters over ManageSieve or in webmail
- composes with: a flat $10 a year for unlimited mailboxes on unlimited owned domains, with external sending capped near 3000 messages per day; a fit for many addresses on domains already owned.
- reliability: an account broken into and used to send spam is locked
- notes: No free custom-domain mailbox; Simple pricing at $10 a year covers unlimited users on unlimited owned domains, with external sending near 3000 messages per day as the first stated ceiling.
- evidence note: prices and limits read from the vendor pages; imap.purelymail.com:993 accepted a TCP connection and smtp.purelymail.com:587 answered with an SMTP banner; no login or send was made
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-30: Simple pricing is $10 a year | capture: sha256:d4163763fc2c944a97500cab248ff3510d87a12c3861b21f5cb4d4bc2f532b6d | quote: It's called simple pricing, and it's very simple: it costs $10 a year.
  - [1] 2026-10-30: Simple pricing has no hard limit on users, custom domains or storage | capture: sha256:d4163763fc2c944a97500cab248ff3510d87a12c3861b21f5cb4d4bc2f532b6d | quote: There are no hard limits. Not on users, custom domains, storage, or anything else.
  - [1] 2026-10-30: heavy use may require Advanced pricing | capture: sha256:d4163763fc2c944a97500cab248ff3510d87a12c3861b21f5cb4d4bc2f532b6d | quote: If you use significantly more than $10 a year in resources, you may need to switch to advanced pricing.
  - [2] 2026-10-30: Advanced storage costs $0.56 per compressed GB per year | capture: sha256:73594c18bd6f34d3a4a5a0845b06659db810cc885d9afe77038044fd4966bd2e | quote: Storage: $0.56 per compressed GB per year
  - [2] 2026-10-30: the Advanced yearly account fee is $4.00 | capture: sha256:73594c18bd6f34d3a4a5a0845b06659db810cc885d9afe77038044fd4966bd2e | quote: Yearly account fee: $4.00 per year
  - [2] 2026-10-30: external sends cost $0.23 per 1000 plus $0.18 per GB on Advanced | capture: sha256:73594c18bd6f34d3a4a5a0845b06659db810cc885d9afe77038044fd4966bd2e | quote: Emails sent: $0.23 (if sent externally) or $0.03 (if sent within the same account) per 1000 plus $0.18 per GB
  - [2] 2026-10-30: received mail costs $0.03 per 1000 plus $0.04 per GB on Advanced | capture: sha256:73594c18bd6f34d3a4a5a0845b06659db810cc885d9afe77038044fd4966bd2e | quote: Email receipt: $0.03 per 1000 plus $0.04 per GB
  - [2] 2026-10-30: custom domains carry no charge | capture: sha256:73594c18bd6f34d3a4a5a0845b06659db810cc885d9afe77038044fd4966bd2e | quote: Custom domains: There is no additional charge for using a custom domain.
  - [3] 2026-10-30: external sending is limited to about 3000 per day or 300 at once | capture: sha256:73c3a07c783da773dab4189f7577c3166a93c9c4fe7b029640e47cf870d38e58 | quote: Sending email externally (i.e. to users not under your account). This is approximately 3000 messages per day, or 300 at once.
  - [3] 2026-10-30: trial accounts have very low external sending limits | capture: sha256:73c3a07c783da773dab4189f7577c3166a93c9c4fe7b029640e47cf870d38e58 | quote: Currently trial accounts have access to all the same features as regular accounts, however their rate limits for certain sensitive actions- like sending an email to an address not within the same account- are very low.
  - [4] 2026-10-30: users and custom domains are unlimited | capture: sha256:445ef4a764afce9b86efe14cb3c134a36e948b8252c3d5f24a58032a99515fb6 | quote: You may have as many users on as many custom domains as you like.
  - [4] 2026-10-30: IMAP IDLE is supported | capture: sha256:445ef4a764afce9b86efe14cb3c134a36e948b8252c3d5f24a58032a99515fb6 | quote: IMAP supports the IDLE command, for immediate, battery-efficient mail delivery for phones and other devices.
  - [5] 2026-10-30: SMTP also accepts STARTTLS on port 587 | capture: sha256:68dc685a9d938a7dae1371abd9d790e47506bf4cbf640ed0a15d8542f94e04e7 | quote: If your client only supports STARTTLS, use port 587 with STARTTLS enabled.
  - [5] 2026-10-30: POP3 is at pop3.purelymail.com:995 | capture: sha256:68dc685a9d938a7dae1371abd9d790e47506bf4cbf640ed0a15d8542f94e04e7 | quote: It can be found at: pop3.purelymail.com with port 995.
  - [4] 2026-10-30: IMAP and POP3 access are supported | capture: sha256:445ef4a764afce9b86efe14cb3c134a36e948b8252c3d5f24a58032a99515fb6 | quote: We support standard email access that works with most third party apps. This includes IMAP and POP3.
  - [4] 2026-10-30: WebDAV file storage, CardDAV and CalDAV are offered | capture: sha256:445ef4a764afce9b86efe14cb3c134a36e948b8252c3d5f24a58032a99515fb6 | quote: WebDAV/CardDAV/CalDAV: basic file storage, contact, and calendar synchronization
  - [5] 2026-10-30: IMAP is at imap.purelymail.com:993 over SSL/TLS | capture: sha256:68dc685a9d938a7dae1371abd9d790e47506bf4cbf640ed0a15d8542f94e04e7 | quote: Our imap servers can be found at imap.purelymail.com with port 993. Make sure your app connects with SSL/TLS.
  - [5] 2026-10-30: SMTP is at smtp.purelymail.com:465 over SSL/TLS | capture: sha256:68dc685a9d938a7dae1371abd9d790e47506bf4cbf640ed0a15d8542f94e04e7 | quote: SMTP takes care of delivering your messages. Use smtp.purelymail.com with port 465. This should be SSL/TLS.
  - [5] 2026-10-30: ManageSieve is at mailserver.purelymail.com:4190 | capture: sha256:68dc685a9d938a7dae1371abd9d790e47506bf4cbf640ed0a15d8542f94e04e7 | quote: a ManageSieve implementation is available at mailserver.purelymail.com with port 4190
  - [6] 2026-10-30: users on owned domains cost nothing extra | capture: sha256:192788102bda2f3ac8575326e75431d0507c256c2cc912746e8ce6d6fa215886 | quote: **Custom Domains: **There is no additional charge for users on domains you own.
  - [7] 2026-10-30: the trial needs an SMS-capable phone | capture: sha256:ea5c9b230400d08208dccd3c05bd86eba39e0f3f133628cc371c3fec78ddd32b | quote: A modern browser and SMS-capable phone are required to activate your trial account.
  - [7] 2026-10-30: signup creates an administrator user | capture: sha256:ea5c9b230400d08208dccd3c05bd86eba39e0f3f133628cc371c3fec78ddd32b | quote: This is your Purelymail account admin user, used to manage your domains, billing, and additional users.
  - [7] 2026-10-30: a recovery email or phone is recommended, not required | capture: sha256:6bb8cd560c7e0c21e282f49467a27e985fd43b010f9cb7f2268cbb759e8d9dd8 | quote: To protect your account, we strongly recommend adding a recovery email or phone number.
  - [7] 2026-10-30: the paid signup takes payment through Stripe | capture: sha256:ea5c9b230400d08208dccd3c05bd86eba39e0f3f133628cc371c3fec78ddd32b | quote: You’ll be redirected to Stripe to securely enter your details.
  - [7] 2026-10-30: a trial account starts with a limited credit balance | capture: sha256:ea5c9b230400d08208dccd3c05bd86eba39e0f3f133628cc371c3fec78ddd32b | quote: Your account starts with a limited credit balance that typically lasts a month with light usage.
  - [7] 2026-10-30: an account used to send spam is locked | capture: sha256:ea5c9b230400d08208dccd3c05bd86eba39e0f3f133628cc371c3fec78ddd32b | quote: And if they succeed and send spam through our system, your account will be locked.
  - probe:smtp.purelymail.com:587 2026-10-30: smtp.purelymail.com:587 answered with an SMTP banner | capture: sha256:0b22080304d3b313cdb36895ec1bbd85d05f3db5f934c48f8fedcea9d8cffe4e | quote: 220 smtp.purelymail.com
  - probe:imap.purelymail.com:993 2026-10-30: imap.purelymail.com:993 accepted a TCP connection | capture: sha256:0b22080304d3b313cdb36895ec1bbd85d05f3db5f934c48f8fedcea9d8cffe4e | quote: "host": "imap.purelymail.com", "port": 993, "ok": true
  - [1] 2026-11-04: Simple pricing is still $10 a year | capture: sha256:d4163763fc2c944a97500cab248ff3510d87a12c3861b21f5cb4d4bc2f532b6d | quote: It's called simple pricing, and it's very simple: it costs $10 a year.
  - [3] 2026-11-04: external sending is still about 3000 messages per day | capture: sha256:73c3a07c783da773dab4189f7577c3166a93c9c4fe7b029640e47cf870d38e58 | quote: This is approximately 3000 messages per day, or 300 at once.
  - probe:imap.purelymail.com:993 2026-11-04: imap.purelymail.com:993 accepted a TCP connection on 2026-11-04 | capture: sha256:0775cdc3ead7fefcd1d1311bb85b8bbefdcf9ff5773eb9d48aa4c18bf33dda1b | quote: "port": 993
- sources:
  - [1] https://purelymail.com/pricing
  - [2] https://purelymail.com/advancedpricing
  - [3] https://purelymail.com/docs/faq
  - [4] https://purelymail.com/docs/features
  - [5] https://purelymail.com/docs/setup/technical
  - [6] https://purelymail.com/docs/users
  - [7] https://purelymail.com/signup
