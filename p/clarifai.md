# Clarifai

> clarifai.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clarifai/ | JSON https://fshy.ajam.dev/api/v1/entity/clarifai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clarifai

- `inference/clarifai` | trial-only | evidence documented | binding retention-clamped | category inference endpoint, pay-as-you-go with an expiring welcome credit
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://docs.clarifai.com/control/account-billing
- free tier: a one-time USD 5 welcome credit after phone-number verification, expiring 30 days after claim; up to two bonuses (one personal, one organization); the underlying plan is pay-as-you-go prepaid credit | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: a phone number is verified by SMS to claim the free USD 5 credit; the same number may verify up to three accounts, but only one personal and one organization account get the bonus; a card is needed only to recharge after that
- interface: rest
- limits:
  - retention-clamped (binding): the one-time USD 5 welcome bonus expires 30 days after it is claimed [1]
  - request-rate: Up to 100 requests per second [1]
- binding note: the 30-day credit expiry ends the free allowance before any rate limit is reached
- endpoint: https://api.clarifai.com/v2/ext/openai/v1
- tooling: an OpenAI-compatible endpoint at api.clarifai.com/v2/ext/openai/v1 plus the Clarifai SDK and CLI
- composes with: pairs with an OpenAI-compatible agent only while the USD 5 credit lasts; the scarce link is the phone gate and the 30-day expiry
- reliability: no reliability event recorded
- notes: credits are expiring, not a standing tier.
- evidence note: the snapshot is dated 2026-07-20
- evidence:
  - [1] 2026-11-18: the free USD 5 credit requires phone verification and is one-time | capture: sha256:42b34a55798f888849f51fca2e29032b2bde5cc40ab41785bfe2ec7efa1c3482 | quote: After switching, click the notification bar and select Claim credits to verify your phone number and receive a one-time, free $5 credits, which can be used to try anything from serverless model access to dedicated deployments.
  - [1] 2026-11-18: the welcome bonus expires after 30 days | capture: sha256:42b34a55798f888849f51fca2e29032b2bde5cc40ab41785bfe2ec7efa1c3482 | quote: The $5 welcome bonus has a 30-day expiration period.
  - [1] 2026-11-18: the Pay-As-You-Go plan allows up to 100 requests per second | capture: sha256:42b34a55798f888849f51fca2e29032b2bde5cc40ab41785bfe2ec7efa1c3482 | quote: Up to 100 requests per second
- sources:
  - [1] https://docs.clarifai.com/control/account-billing
