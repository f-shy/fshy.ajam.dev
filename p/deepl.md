# DeepL API

> deepl.com | Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deepl/ | JSON https://fshy.ajam.dev/api/v1/entity/deepl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DeepL API (Developer plan)

- `inference/deepl-api-developer` | trial-only | evidence documented | binding volume-quota | category machine translation API, one-time free character credit | tier Developer
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:34:02.146Z (live) | stale on 2026-12-04
- url https://www.deepl.com/en/pro-api
- disagrees on identity_kind: `inference/deepl-api-developer` says email, `inference/deepl-api-free` says card
- disagrees on verdict: `inference/deepl-api-developer` says trial-only, `inference/deepl-api-free` says dead
- free tier: a one-time credit of 1 million characters for text and document translation on the Developer plan: a total translation limit of 1,000,000 characters that does not reset; further use needs the paid Growth plan | unit: mixed | metered on: unstated | read on: 2026-11-03 | source: [1] | note: the true unit is source characters (Unicode code points sent for translation); the schema vocabulary has no character unit, so mixed is the nearest term. The Developer plan does not include speech to text and does not include access to the web translator. The earlier DeepL API Free plan (500,000 characters per month) is a separate record
- per-object cap: 128 KiB total request size and 16 KiB header size for every API plan; the document limit column for free plans is 10 MB and 500,000 characters for a Word file (whether the Developer plan uses that column is unverified) | source: [2]
- retention: not applicable: a translation endpoint stores nothing for the caller
- egress: metered: no
- identity: email | detail: the sign-up form is step 1 of 3 ('Sign up', 'Plan details', 'Get API key') and asks for an email, a password and a confirmation of being over 14; whether step 2 'Plan details' asks for a card or an address is unverified: behind a sign-up. The paid Growth plan is bought by credit card only
- interface: rest
- limits:
  - volume-quota (binding): 1,000,000 characters in total, one time, does not reset [1]
  - per-object-cap: 128 KiB total request size; 16 KiB header size [2]
  - request-rate: unverified: no request-rate figure is published; the API answers HTTP 429 for too many requests in a short period and HTTP 456 when a usage limit is reached [3]
- binding note: the 1,000,000 character lifetime total is the limit that decides; it does not reset
- tooling: HTTP REST API with the header 'Authorization: DeepL-Auth-Key <key>' and DeepL's own client libraries; JSON or form-encoded bodies. Free API keys are identified by the suffix ':fx' and use the host api-free.deepl.com; whether a Developer key carries that suffix and host is unverified: behind a sign-up
- composes with: a lifetime credit of 1,000,000 characters, then the Growth plan at a card-only checkout; the credit does not recur, so it does not replace a recurring free translation route
- reliability: the allowance is a lifetime total: once it is used up the plan has to be upgraded, and the API answers HTTP 456 when a character quota is used up
- notes: Supported languages: the API language page lists 126 entries (for example Acehnese, Afrikaans, Albanian, Arabic through Zulu), retrievable from the /v3/languages endpoint; features such as glossaries cover only some of them. Character limit per request: 128 KiB total request size; the API counts source characters, and document formats bill a minimum of 50,000 characters per document. Not keyless: every request needs an API key.
- evidence note: the 1,000,000 character one-time limit and its non-reset are quoted from the vendor's help centre and pricing page; the sign-up form fields are read from the sign-up page; step 2 of the sign-up and the host of a Developer key are behind a sign-up and unverified.
- evidence:
  - [1] 2026-11-03: the Developer plan is free with a total translation limit of 1,000,000 characters | capture: sha256:0951163069adfd52dd6d46bab3ad9975b1b033ac6f542a1d275885a8fced11db | quote: The DeepL API Developer plan allows developers to try out DeepL’s API for free, with a total translation limit of 1,000,000 characters.
  - [1] 2026-11-03: the Developer allowance does not reset, so it is a one-time credit | capture: sha256:0951163069adfd52dd6d46bab3ad9975b1b033ac6f542a1d275885a8fced11db | quote: Once this limit has been reached, **it will not reset **and you will need to upgrade to the DeepL API Growth plan.
  - [4] 2026-11-03: the pricing page lists the Developer plan as a one-time credit of 1 million characters | capture: sha256:549d47f8ba7d898a59658e75f3eaa505f8606ca42ed42c698a69d1e04c3c1e30 | quote: One-time credit of 1 million characters
  - [4] 2026-11-03: the plan comparison gives the Developer character usage limit as 1 million | capture: sha256:549d47f8ba7d898a59658e75f3eaa505f8606ca42ed42c698a69d1e04c3c1e30 | quote: | Character usage limit | 1 million | 50 million per month | Unlimited 1 |
  - [4] 2026-11-03: API plans are paid for by credit card only, which is what upgrading from Developer to Growth takes | capture: sha256:549d47f8ba7d898a59658e75f3eaa505f8606ca42ed42c698a69d1e04c3c1e30 | quote: For API plans, we accept payment by credit card only.
  - [5] 2026-11-03: the Developer sign-up page offers 1 million characters for free | capture: sha256:d98205a2b9a7f5d0b41953ea710fe7a1d3cff92ce5b12446f9c6bf0f643a8b44 | quote: Translate 1 million characters for free.
  - [5] 2026-11-03: the sign-up form has a password field, next to an email field | capture: sha256:d98205a2b9a7f5d0b41953ea710fe7a1d3cff92ce5b12446f9c6bf0f643a8b44 | quote: Use at least 8 characters for your password
  - [5] 2026-11-03: the sign-up form asks for an age confirmation and is step 1 of a 3 step flow | capture: sha256:ae2dab06ab73274dc03a8adb6637c8a7df79c630ee8608035df4d0626fdb7386 | quote: I confirm that I am over the age of 14.
  - [2] 2026-11-03: the total request size limit is 128 KiB | capture: sha256:d52d38681e4a88c2cd7f814184c2f4527872904e91293390f18a566b76175cae | quote: | Total request size | 128 KiB (128\*1024 bytes) |
  - [6] 2026-11-03: the API language list has 126 entries | capture: sha256:f30fc56801f424f6e8357287e68fccc2beee11a3ece2c2d9381ded6542885539 | quote: Showing 126 of 126 languages
  - [3] 2026-11-03: HTTP 456 is the answer when a usage limit is reached | capture: sha256:6813ac536005d40f1e2776437cb8ca980f2c04fb56f03a76adb466f1d567b3e3 | quote: * HTTP 456: quota exceeded. The request would take the account or API key past one of its usage limits.
  - probe:api-free.deepl.com/v2/usage 2026-11-03: the DeepL API host answers an unauthenticated request with HTTP 403 and names the key header, so there is no keyless route | capture: sha256:a84af4df923fa1b1452d8954948eb1343518a6e7e56a947c792ad92231f6f164 | quote: Missing Authorization header, expected 'Authorization: DeepL-Auth-Key <API key>'.
- sources:
  - [1] https://support.deepl.com/hc/en-us/articles/360021200939-DeepL-API-plans
  - [2] https://developers.deepl.com/docs/resources/usage-limits
  - [3] https://developers.deepl.com/docs/best-practices/error-handling.md
  - [4] https://www.deepl.com/en/pro-api
  - [5] https://www.deepl.com/en/signup?cta=checkout&is_api=true&productId=api-developer
  - [6] https://developers.deepl.com/docs/getting-started/supported-languages

## DeepL API (Free plan)

- `inference/deepl-api-free` | dead | evidence documented | binding volume-quota | category machine translation API, legacy recurring free plan closed to new sign-ups | tier API Free
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:22:57.424Z (live) | stale on 2026-12-05
- url https://support.deepl.com/hc/en-us/articles/360021200939-DeepL-API-plans
- disagrees on identity_kind: `inference/deepl-api-developer` says email, `inference/deepl-api-free` says card
- disagrees on verdict: `inference/deepl-api-developer` says trial-only, `inference/deepl-api-free` says dead
- free tier: 500,000 characters per month for free on the DeepL API Free plan; the plan can no longer be purchased and has been replaced by the one-time 1,000,000 character Developer plan | unit: mixed | metered on: unstated | read on: 2026-11-03 | source: [1] | note: the true unit is source characters per month; the schema vocabulary has no character unit, so mixed is the nearest term. The plan does not include DeepL Write or speech to text translation. Whether keys issued earlier still answer is unverified: it needs an existing account
- per-object cap: 128 KiB total request size and 16 KiB header size; document limit column for free plans is 10 MB and 500,000 characters for a Word file | source: [2]
- retention: not applicable: a translation endpoint stores nothing for the caller
- egress: metered: no
- identity: card | detail: unverified: the plan can no longer be purchased, so its sign-up cannot be read and no first-party page read states the requirement; the kind is a placeholder for the plan as it was sold
- interface: rest
- limits:
  - volume-quota (binding): 500,000 characters per month [3]
  - per-object-cap: 128 KiB total request size; 16 KiB header size [2]
- binding note: the plan is closed to new sign-ups; for the keys that exist, the 500,000 characters per month quota decides
- endpoint: https://api-free.deepl.com/v2/translate
- tooling: HTTP REST API at https://api-free.deepl.com with the header 'Authorization: DeepL-Auth-Key <key>'; keys of this plan end in ':fx'; up to 2 keys per Free API subscription
- composes with: none for a new account: the plan is closed; the Developer plan (one-time 1,000,000 characters) is the current free entry
- reliability: the plan is closed to new sign-ups; the API answers HTTP 456 when the monthly quota is used up
- notes: Supported languages: see the Developer plan record for the API language list. Character limit per request: 128 KiB total request size. Not keyless: every request needs an API key.
- evidence note: the closure and the 500,000 characters per month figure are quoted from the vendor's help centre; the sign-up requirement of the closed plan is unverified.
- evidence:
  - [1] 2026-11-03: the Free plan can no longer be purchased | capture: sha256:0951163069adfd52dd6d46bab3ad9975b1b033ac6f542a1d275885a8fced11db | quote: The DeepL API Free plan can no longer be purchased.
  - [1] 2026-11-03: the Free plan allowed 500,000 characters per month | capture: sha256:0951163069adfd52dd6d46bab3ad9975b1b033ac6f542a1d275885a8fced11db | quote: DeepL API Free allows developers to translate up to 500,000 characters per month for free.
  - [3] 2026-11-03: the billing article still states the 500,000 characters per month allowance | capture: sha256:44d5a3c9f73369097cf55d2476f0cb1b51f3126be0fde628f44772b05defd006 | quote: With DeepL API Free, you can translate up to 500,000 characters per month for free.
  - [4] 2026-11-03: Free plan keys carry the suffix :fx | capture: sha256:a0c1ea529d3c160fe6998552ac8649ee65b49f7166476bce0844f3ee2acb1441 | quote: DeepL API Free authentication keys can be identified easily by the suffix ":fx"
  - [4] 2026-11-03: the Free API host is api-free.deepl.com | capture: sha256:a0c1ea529d3c160fe6998552ac8649ee65b49f7166476bce0844f3ee2acb1441 | quote: Free API -> `https://api-free.deepl.com`
  - [5] 2026-11-03: a Free API plan can hold up to 2 active keys | capture: sha256:88ad7c7991f5c0869566ce6d16726bdb4b83aa1d22a6477af4f58727d0ced7fc | quote: up to 25 on Pro API plans and up to 2 on Free API plans
  - [2] 2026-11-03: the total request size limit is 128 KiB | capture: sha256:d52d38681e4a88c2cd7f814184c2f4527872904e91293390f18a566b76175cae | quote: | Total request size | 128 KiB (128\*1024 bytes) |
  - probe:api-free.deepl.com/v2/usage 2026-11-03: the Free API host answers an unauthenticated request with HTTP 403 and names the key header, so there is no keyless route | capture: sha256:a84af4df923fa1b1452d8954948eb1343518a6e7e56a947c792ad92231f6f164 | quote: Missing Authorization header, expected 'Authorization: DeepL-Auth-Key <API key>'.
  - [3] 2026-11-04: the page states 500,000 characters per month and says nothing about rollover | capture: sha256:44d5a3c9f73369097cf55d2476f0cb1b51f3126be0fde628f44772b05defd006 | quote: With DeepL API Free, you can translate up to 500,000 characters per month for free.
- sources:
  - [1] https://support.deepl.com/hc/en-us/articles/360021200939-DeepL-API-plans
  - [2] https://developers.deepl.com/docs/resources/usage-limits
  - [3] https://support.deepl.com/hc/en-us/articles/360020685720-Usage-count-and-billing-in-DeepL-API
  - [4] https://developers.deepl.com/docs/getting-started/auth
  - [5] https://developers.deepl.com/docs/admin/managing-api-keys.md
