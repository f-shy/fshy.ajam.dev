# Mojeek

> mojeek.com | Crawling; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mojeek/ | JSON https://fshy.ajam.dev/api/v1/entity/mojeek.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mojeek

- `crawler-scraper/mojeek` | fails-identity | evidence documented | binding request-rate | category search API
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T01:01:54.326Z (live) | stale on 2026-12-03
- url https://www.mojeek.com/services/search/web-search-api/
- free tier: a free credit on the Startup plan, claimed after signup; a bank card is required to open the account; the credit's size and expiry are unverified: not published on any page read | unit: mixed | metered on: request-count | read on: 2026-10-30 | source: [1] | note: The unit is a one-time credit of unstated size against the Startup price of GBP 2 per 1,000 requests.
- per-object cap: not applicable: the unit is a request; up to 10 results a request on Startup | source: [1]
- retention: not published: no page read states an expiry for the free credit | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: card | detail: registration at the vendor's accounts site asks for an email address and a password; a bank card is required to open an account, even to claim the free credit; payments go through Stripe and none are taken automatically
- interface: rest
- limits:
  - request-rate (binding): Startup: GBP 2 per 1,000 requests, 5 queries a second, 100,000 queries a day, up to 10 results a request [1]
  - request-rate (binding): Business: GBP 3 per 1,000 requests, 10 queries a second, 400,000 queries a day, up to 40 results [1]
- limits note: pay-as-you-go with no automatic payments; prices exclude VAT
- binding note: identity fails first, since a bank card opens the account; once past it, the 5-a-second Startup cap is the first limit
- interface detail: GET https://api.mojeek.com/search with q and api_key parameters; JSON or XML output; country and language boosting parameters
- endpoint: part of interface detail
- tooling: plain HTTP GET with an api_key query parameter
- composes with: An independent crawler index rather than a resale of Google or Bing results, at GBP 2 per 1,000 requests once a card is on file
- reliability: a keyless call to the search endpoint answered 403 with an empty body
- notes: The card gate is the finding: the credit is real but no account opens without a bank card. The plan buttons link to a contact form rather than a self-serve checkout.
- evidence note: the card requirement, the Startup price and the rate caps are quoted from the first-party API page; the size of the free credit is behind a card-gated sign-up
- evidence:
  - [1] 2026-10-30: the free credit needs a bank card on the account | capture: sha256:495574e0b488e2756e499171344957d9a4fa3e54f6244e93be68b144c488222d | quote: Yes, sign up to our Startup Plan and claim a free credit. A bank card is required to open an account however no automatic payments are processed and you can cancel anytime.
  - [1] 2026-10-30: the Startup plan allows 5 queries a second | capture: sha256:495574e0b488e2756e499171344957d9a4fa3e54f6244e93be68b144c488222d | quote: * 5 Queries /sec
  - [1] 2026-10-30: the Startup plan allows 100,000 queries a day | capture: sha256:495574e0b488e2756e499171344957d9a4fa3e54f6244e93be68b144c488222d | quote: * 100,000 Queries /day
  - [1] 2026-10-30: the Startup plan costs GBP 2 per 1,000 requests | capture: sha256:495574e0b488e2756e499171344957d9a4fa3e54f6244e93be68b144c488222d | quote: Startup £2
  - [1] 2026-10-30: the API serves Mojeek's own index | capture: sha256:495574e0b488e2756e499171344957d9a4fa3e54f6244e93be68b144c488222d | quote: Global index with billions of fresh webpages.
  - [1] 2026-10-30: pay-as-you-go with no automatic payments | capture: sha256:4b01bcd5da48744da1f409e63266fd8f218530365459ed504f6d1b540b72b400 | quote: Our PAYG plans do not process automatic payments and you can set alerts on your account to control your budget.
  - [2] 2026-10-30: the search endpoint and its key parameter | capture: sha256:aa1535e1b0f29644732116299930d58d67c7eb311b9cea04d54d502a20d3e1ea | quote: curl "https://api.mojeek.com/search?q=mojeek&api_key=YOUR_API_KEY&lb=EN&lbb=100&rb=GB&rbb=10&fmt=json"
  - probe:api.mojeek.com/search 2026-10-30: a keyless call answered 403 | capture: sha256:4e70b72fa4225c9011565a2adcdf94e04bb09b7c50ba790b8d726c9a189f1618 | quote: "status": 403
  - [1] 2026-11-01: the FAQ offers a free credit after sign-up on the Startup plan and requires a bank card to open an account, and states neither a size nor an expiry for the credit | capture: sha256:495574e0b488e2756e499171344957d9a4fa3e54f6244e93be68b144c488222d | quote: Yes, sign up to our Startup Plan and claim a free credit. A bank card is required to open an account however no automatic payments are processed and you can cancel anytime.
  - [3] 2026-11-01: the account registration form asks for an email address and a password entered twice, and no other field | capture: sha256:d3caef81fe676f147dfd351682b2c4a4fa56bf7ecd402abbb929369775645a1b | quote: Email address * Password * Password Again *
  - [4] 2026-11-01: a reply from the vendor on its own forum (December 2025) says a signed-up account can claim some credits and try the API for free, and names no amount or expiry | capture: sha256:14c4304e0df7b104d14a6965cc8721d64ad418a2ade82b87385777a5d2864688 | quote: If you sign up for the Personal plan (initially) you can claim some credits, and then try out the API for free.
- sources:
  - [1] https://www.mojeek.com/services/search/web-search-api/
  - [2] https://www.mojeek.com/support/api/search/quickstart.html
  - [3] https://accounts.mojeek.com/register
  - [4] https://community.mojeek.com/t/web-search-api-trial-and-account-page-error/2655
