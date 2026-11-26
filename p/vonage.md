# Vonage

> vonage.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vonage/ | JSON https://fshy.ajam.dev/api/v1/entity/vonage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Vonage

- `dev-services/vonage` | trial-only | evidence documented | binding write-gated | category hosted SMS and voice API provider with a free trial credit and a DEMO mode; paid plans are usage based | tier Free Trial (DEMO mode)
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T00:19:24.331Z (live) | stale on 2026-12-20
- url https://www.vonage.com/communications-apis/pricing/
- free tier: EUR 2 free test credit on signup, with the account in DEMO mode; trial SMS is limited to the registered number and four verified test numbers and carries a [FREE SMS DEMO, TEST MESSAGE] notice; no credit card required | unit: credits | metered on: unstated | read on: 2026-11-19 | source: [1] | note: The test credit is denominated in euros. One first-party guide states up to 10 destination numbers in DEMO mode while two support articles state the registered number plus four verified test numbers; both figures are quoted in evidence. No credit card is required at signup.
- per-object cap: unverified: the API reference pages read state no hard numeric limit on SMS message length; an over-long message returns error code 12 'Message Too Long' | source: [2]
- retention: not applicable to stored bytes: messages are delivered and can be looked up, but no explicit message-log retention period is stated on the pages read; SMS delivery is attempted by default for 72 hours, typically 24 to 48 hours | source: [2]
- egress: Outbound SMS and voice calls are the metered service itself; the pricing page lists USD 0.00860 per US LVN SMS message and USD 0.01538 per voice minute, with carrier fees added. SMS delivery attempts run for up to 72 hours by default. | metered: yes | free allowance: EUR 2 free test credit in DEMO mode | source: [3]
- identity: any-phone | detail: The sign-up page lists Email, First name, Last name, Password and Phone number and the steps Verify email and Verify number. A verified phone number is required and no card is asked for; for very few countries Vonage cannot create an account automatically.
- interface: rest, cli
- limits:
  - volume-quota: EUR 2 free test credit on signup in DEMO mode [1]
  - write-gated (binding): trial SMS only to the registered number and four verified test numbers; voice calls only to the registered number [4]
  - write-gated (binding): trial credit cannot be used to buy virtual phone numbers [4]
  - write-gated (binding): DEMO mode requires target numbers to be added to a whitelisted destination list [2]
  - request-rate: Pricing API rate limited to one request per second [5]
  - retention-clamped: SMS delivery attempted for up to 72 hours by default, typically 24 to 48 hours [2]
- limits note: First-party pages disagree on the trial destination count: two support articles say the registered number plus four verified test numbers (or up to 5 test numbers), while the account getting-started guide says up to 10 destination numbers. Both figures are quoted in evidence.
- binding note: The DEMO mode destination whitelist and the ban on buying virtual numbers with trial credit restrict what the account can send to before the EUR 2 credit is used up.
- interface detail: A REST SMS API at rest.nexmo.com with an OpenAPI specification, plus Messages, Voice and Pricing APIs, authenticated with an API key and secret; a Vonage CLI, language SDKs and inbound and outbound webhooks are documented. SMPP is also listed as an option. The Pricing API is rate limited to one request per second.
- endpoint: https://rest.nexmo.com
- tooling: Vonage CLI, language SDKs, the REST API with an OpenAPI description, the Account Dashboard and inbound webhook endpoints
- composes with: Transactional SMS and voice for alerts and two-factor authentication; the Verify API adds OTP delivery with voice fallback, and webhooks feed delivery and inbound events into a larger stack.
- reliability: The SMS API answers error 1 when sending faster than the account limit, error 9 when credit is insufficient and error 29 for non-whitelisted destinations in demo mode; inbound webhooks are retried for 24 hours without a 2xx answer.
- notes: Vonage was formerly Nexmo. The free offer is a DEMO mode trial with a [FREE SMS DEMO, TEST MESSAGE] notice on SMS. A verified phone number is required at signup and no card is required. For very few countries Vonage cannot create an account automatically. The trial destination count differs between first-party pages (5 versus 10); both figures are quoted and the conflict is left open rather than resolved.
- evidence note: Values are quoted from first-party signup, documentation and support pages. No account was opened, so any value visible only after signup is unverified.
- evidence:
  - [6] 2026-11-19: the signup page states no credit card is required | capture: sha256:f99ee0c674881b454d5248fb392502f157157f7770f53e648c090f43fd39516c | quote: No credit card required.
  - [6] 2026-11-19: a verified phone number is required at signup | capture: sha256:f99ee0c674881b454d5248fb392502f157157f7770f53e648c090f43fd39516c
  - [6] 2026-11-19: signup requires email verification | capture: sha256:f99ee0c674881b454d5248fb392502f157157f7770f53e648c090f43fd39516c | quote: 2. Verify email
  - [6] 2026-11-19: the signup form asks for a phone number | capture: sha256:f99ee0c674881b454d5248fb392502f157157f7770f53e648c090f43fd39516c | quote: Phone number
  - [1] 2026-11-19: signup gives EUR 2 free test credit and puts the account in DEMO mode | capture: sha256:87b26634b0920b437117351cade4a136a2ed1a26a1a4a5c78d23ffbb38076beb | quote: When you create your Vonage account you are given €2 free test credit and your account is set in DEMO mode.
  - [1] 2026-11-19: DEMO mode allows messages to up to 10 destination numbers and appends a demo notice to SMS | capture: sha256:87b26634b0920b437117351cade4a136a2ed1a26a1a4a5c78d23ffbb38076beb | quote: You can use our products to send messages to up to 10 destination numbers, a message stating that the account is in demo mode is added to all the SMS you send.
  - [1] 2026-11-19: phone verification uses a PIN sent by text message or call, with a 5 minute timeout | capture: sha256:87b26634b0920b437117351cade4a136a2ed1a26a1a4a5c78d23ffbb38076beb | quote: Vonage sends a PIN to your phone as a text message or automated phone call. The timeout for each verification attempt is 5 minutes.
  - [1] 2026-11-19: some countries cannot create an account automatically because of payment or trading restrictions | capture: sha256:87b26634b0920b437117351cade4a136a2ed1a26a1a4a5c78d23ffbb38076beb | quote: For very few countries Vonage cannot create an account for you automatically.
  - [4] 2026-11-19: trial SMS is limited to the registered number and four verified test numbers, voice to the registered number | capture: sha256:3759fb6de1013e12dee6c62c00a3fc4aa1267944065afb80bffe665f9dd2282e | quote: You can send SMS to your registered number and four verified test numbers, while Voice calls can only be made to your registered number.
  - [4] 2026-11-19: trial credit cannot buy virtual phone numbers | capture: sha256:3759fb6de1013e12dee6c62c00a3fc4aa1267944065afb80bffe665f9dd2282e | quote: You cannot use trial credit to buy virtual phone numbers.
  - [4] 2026-11-19: trial SMS carries a demo notice in the message body | capture: sha256:3759fb6de1013e12dee6c62c00a3fc4aa1267944065afb80bffe665f9dd2282e | quote: Your SMS messages will have the text [FREE SMS DEMO, TEST MESSAGE] appended to the body of the message.
  - [7] 2026-11-19: trial mode allows messages and calls to up to 5 verified test numbers | capture: sha256:42742fac6cdabee1ebad3edb37a7d74e6703008908461a8816b45b0ae188cf3b | quote: While in trial mode, you can only send messages and make calls to up to 5 test numbers that you've verified.
  - [3] 2026-11-19: Vonage offers free credit with no credit card | capture: sha256:3805fa4642d542dcbbe5a80da0a817450598c7fc8b55d02dbd38867fe8eb1223 | quote: Start developing now with free credit. No credit card required.
  - [3] 2026-11-19: API pricing is usage based | capture: sha256:3805fa4642d542dcbbe5a80da0a817450598c7fc8b55d02dbd38867fe8eb1223 | quote: All API pricing is by usage, with big value and no surprises a key part of our philosophy.
  - [3] 2026-11-19: the lowest listed US LVN SMS price is USD 0.00860 per message | capture: sha256:3805fa4642d542dcbbe5a80da0a817450598c7fc8b55d02dbd38867fe8eb1223 | quote: €0.00735/$0.00860
  - [2] 2026-11-19: demo mode requires a whitelisted destination list | capture: sha256:331349aa8af233509e9f329463c584496c1f821826a5711502270829dd538e9f | quote: Non-Whitelisted Destination. Your Vonage account is still in demo mode. While in demo mode you must add target numbers to your whitelisted destination list.
  - [2] 2026-11-19: sending faster than the account limit returns a throttled error | capture: sha256:331349aa8af233509e9f329463c584496c1f821826a5711502270829dd538e9f | quote: Throttled. You are sending SMS faster than the account limit.
  - [2] 2026-11-19: SMS delivery is attempted for up to 72 hours by default, typically 24 to 48 hours | capture: sha256:331349aa8af233509e9f329463c584496c1f821826a5711502270829dd538e9f | quote: By default Vonage attempts delivery for 72 hours, however the maximum effective value depends on the operator and is typically 24 - 48 hours.
  - [2] 2026-11-19: inbound webhooks are retried for 24 hours without a 2xx answer | capture: sha256:331349aa8af233509e9f329463c584496c1f821826a5711502270829dd538e9f | quote: If you do not send a 2xx response Vonage will resend the inbound message for the next 24 hours.
  - [5] 2026-11-19: the Pricing API is limited to one request per second | capture: sha256:42a0cdbef98e4603563ff2c8ae20f0de0c16638dbdb5689146fd1963a385a1f0 | quote: Please note the Pricing API is rate limited to one request per second.
- sources:
  - [1] https://developer.vonage.com/en/account/guides/dashboard-management
  - [2] https://developer.vonage.com/en/api/sms
  - [3] https://www.vonage.com/communications-apis/pricing/
  - [4] https://api.support.vonage.com/hc/en-us/articles/212554438-What-are-the-limitations-of-a-trial-account
  - [5] https://developer.vonage.com/en/api/pricing
  - [6] https://developer.vonage.com/sign-up
  - [7] https://api.support.vonage.com/hc/en-us/articles/212107987-How-can-I-get-full-account-features-enabled
