# NLP Cloud

> nlpcloud.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nlpcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/nlpcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NLP Cloud

- `inference/nlp-cloud` | fails-identity | evidence documented | binding request-rate | category inference API, free plan and pay-as-you-go credit, registration closed to new users
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://nlpcloud.com/pricing.html
- free tier: a prepaid Free plan at $0 with 2 parallel requests and variable per-model request rates, and a pay-as-you-go plan that credits $15 automatically; the register page currently accepts no new users | unit: mixed | metered on: unstated | read on: 2026-11-04 | source: [1] | note: the Free plan has no volume figure: the pricing table gives 2 parallel requests and 'Variable' requests per minute; the $15 credit belongs to the pay-as-you-go plan, which the home page says needs a credit card
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: the register page refuses new users and offers an email waiting list that asks for the use case; the home page says the Free plan needs no credit card and the pay-as-you-go plan does
- interface: rest
- limits:
  - request-rate (binding): Free plan: 2 parallel requests and 'Variable' requests per minute on every listed model; pay-as-you-go: 10 parallel requests [1]
  - volume-quota: a $15 credit is granted automatically on the pay-as-you-go plan, which needs a credit card; per-request rates $0.003 on CPU and $0.005 on GPU [1]
- binding note: the Free plan's 2 parallel requests and unpublished per-model rate bind before any volume figure
- tooling: REST API with client libraries; asynchronous mode on pay-as-you-go
- composes with: none stated
- reliability: new registrations are closed: the register page says the service is at maximum capacity
- notes: the pricing page and the home page still advertise the Free plan and the $15 credit while the register page refuses new users, so the offer exists on paper only for accounts already registered
- evidence:
  - [2] 2026-11-04: the register page refuses new users and points to an email waiting list | capture: sha256:ab893c780f45855b1cadd45723fbbf55ee5daff09c81b83adc5045d6d5364b07 | quote: NLP Cloud is at maximum capacity and cannot accept new users for the moment
  - [1] 2026-11-04: the Free plan column allows 2 parallel requests | capture: sha256:b85b3dbe95aafba7ed44bcce7e4aacb3c164831539ab133fa92c80360cdfbfa6 | quote: | Parallel Requests | 2 | 10 | 20 | 40 | 10 | 20 | 40 | 50 |
  - [1] 2026-11-04: the Free plan column prints 'Variable' as the per-model request rate | capture: sha256:b85b3dbe95aafba7ed44bcce7e4aacb3c164831539ab133fa92c80360cdfbfa6 | quote: | Whisper on GPU (requests per minute) | Variable | | | | 1 | 3 | 10 | 50 |
  - [1] 2026-11-04: the pay-as-you-go plan credits $15 automatically | capture: sha256:b85b3dbe95aafba7ed44bcce7e4aacb3c164831539ab133fa92c80360cdfbfa6 | quote: - Automatically get a $15 FREE credit
  - [3] 2026-11-04: the home page FAQ says the Free plan needs no credit card and is throughput-limited | capture: sha256:5a00ea28801dbe043b04bf0eafda5242f7227835bbb66ab55fbbedcf45a981f2 | quote: Yes. All the I models can be tested for free thanks to the Free plan without a credit card, but the throughput on this plan is very limited.
  - [3] 2026-11-04: the pay-as-you-go plan needs a credit card and credits $15 | capture: sha256:5a00ea28801dbe043b04bf0eafda5242f7227835bbb66ab55fbbedcf45a981f2 | quote: A credit card is needed for this plan, but you automatically get an initial $15 credit for your tests.
- sources:
  - [1] https://nlpcloud.com/pricing.html
  - [2] https://nlpcloud.com/home/register
  - [3] https://nlpcloud.com/
