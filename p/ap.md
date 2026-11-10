# Associated Press

> ap.org | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ap/ | JSON https://fshy.ajam.dev/api/v1/entity/ap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Associated Press (AP Media API)

- `data-apis/associated-press-media-api` | paid-only | evidence documented | binding write-gated | category licensed news content API | tier Contract plan
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T01:13:17.308Z (live) | stale on 2026-12-04
- url https://developer.ap.org/ap-media-api/
- free tier: a sandbox mode lets a key holder try the API before a contract with demo content, no main renditions and no billing. | unit: none | metered on: unstated | read on: 2026-11-02 | source: [1] | note: Content item prices come from the plan of the contract and are returned on request; a plan meters downloads in meter ticks or credits. The sandbox mode serves demo content only and the same API key opens every mode the account may use; how a key is obtained before a contract is unverified: behind a sales contact.
- per-object cap: not stated; search reaches 30 days of content and the feed up to the last 72 hours, depending on the contract | source: [2]
- retention: search covers 30 days of content plus the archive of pictures, video, audio and graphics the contract allows; the feed and the agent reach back 72 hours | days: 30 | source: [2]
- egress: not applicable to the API answers; a content item has a price or a count against the plan meter | metered: yes | source: [3]
- identity: institution | detail: Access follows a contract with AP sales or licensing for B2B use; the pages describe no self-serve sign-up, so the exact registration steps are unverified: behind a sales contact.
- interface: rest
- limits:
  - request-rate: unverified: quotas limit the calls per minute and per day of an API key and their size is read with an account call that needs a key [4]
  - write-gated (binding): an API key and the content rights come from a contract with AP sales or licensing [1]
- binding note: Nothing is served without a key that a contract provides, so the contract gate binds before any rate.
- interface detail: REST over HTTPS at api.ap.org/media (content feed, search, item, account plans and quotas) with an OpenAPI file and an API explorer; the key goes in the x-api-key header; an AP Media Agent downloads a continuous feed
- endpoint: https://api.ap.org/media/v/content/feed
- tooling: any HTTP client; the AP Media Agent
- composes with: Text, picture, graphic, video and audio items with AP metadata and curated links; the delivery is B2B into a content ingestion system or CMS.
- reliability: A keyless call answered HTTP 401 Supply a valid apikey; over the quota the API answers 429 and content can be delayed.
- notes: Storage: no general storage or caching figure is on the pages read; each item carries its own usage restrictions in its metadata. Bulk path: the feed and the AP Media Agent deliver a continuous stream of the last 72 hours, and search reaches 30 days, both within the contract. Free option: none found.
- evidence note: Key, quota and delivery facts are read from first-party help pages; the price, any trial and the quota sizes are behind a sales contact and unverified.
- evidence:
  - [1] 2026-11-02: the content available depends on the contract | capture: sha256:5cd6e77b462c55a1bc4b2e38210fe3a103c0a6638d9fdcd34bb1ef4f38892e8b | quote: AP Media API supports the same content as [AP Newsroom](https://newsroom.ap.org/), depending on your contract terms.
  - [1] 2026-11-02: content item pricing follows the contract | capture: sha256:5cd6e77b462c55a1bc4b2e38210fe3a103c0a6638d9fdcd34bb1ef4f38892e8b | quote: [Content item pricing](https://api.ap.org/media/v/docs/Pricing.htm) based on your contract is returned upon request.
  - [1] 2026-11-02: requests are subject to per-minute and per-day quotas | capture: sha256:5cd6e77b462c55a1bc4b2e38210fe3a103c0a6638d9fdcd34bb1ef4f38892e8b | quote: API requests are subject to quotas, which limit the number of calls per minute and/or per day.
  - [2] 2026-11-02: search covers 30 days of content plus the archive, depending on the contract | capture: sha256:05d497536bdd5833b1c772a875d11db8ffdaee1dbae864a00fb02a35dcf338a7 | quote: The AP Media API Search method provides programmatic access to 30 days of content, as well as the full library of current and archive picture, video, audio and graphics content; depending on your contract terms.
  - [2] 2026-11-02: the feed reaches back up to 72 hours | capture: sha256:05d497536bdd5833b1c772a875d11db8ffdaee1dbae864a00fb02a35dcf338a7 | quote: The AP Media API Feed method and the AP Media Agent allow downloading content up to the last 72 hours; depending on your contract terms.
  - [2] 2026-11-02: the API is designed for B2B integration with content ingestion systems | capture: sha256:05d497536bdd5833b1c772a875d11db8ffdaee1dbae864a00fb02a35dcf338a7 | quote: No, AP Media API is designed for B2B (Business-to-Business) integration with your content ingestion systems or CMSs.
  - [2] 2026-11-02: an API key is required for every call | capture: sha256:05d497536bdd5833b1c772a875d11db8ffdaee1dbae864a00fb02a35dcf338a7 | quote: An API key is required for making AP Media API calls.
  - [4] 2026-11-02: going over the quota answers HTTP 429 | capture: sha256:9d638cf5b7ba2d021bbdff061f4be5f578191c9a7688e70d5ae683a99daea542 | quote: If you exceed your quota limit, you will receive a [429 error code](https://api.ap.org/media/v/docs/API_Codes.htm#429_Status_Code).
  - [3] 2026-11-02: a content item can be included in the plan or priced at an extra charge | capture: sha256:eb66ba54427929408d5c411d9f83386d63749e73e28b5f2595fee92a6c92cfa6 | quote: | Not Included in Your Plan (Extra Charge) | 851 | All plans | Not included in your plan. Available for an extra charge. |
  - probe:https://api.ap.org/media/v/content/feed 2026-11-03: a keyless call answers HTTP 401 Supply a valid apikey | capture: sha256:bb60448d92d49f1f740e0cd383ef773744b5e2d7ba744833a6327dc3311ac718 | quote: "message":"Supply a valid apikey"
  - [5] 2026-11-03: a sandbox mode exists for trying the API before a contract is signed | capture: sha256:fa41f7a999d8e03b1429ac5b0271f8fd42629bb1727d474f68bfa511bd4509e4 | quote: Sandbox mode allows you to try out the API before you sign a contract with the AP.
  - [5] 2026-11-03: sandbox downloads are not billed | capture: sha256:fa41f7a999d8e03b1429ac5b0271f8fd42629bb1727d474f68bfa511bd4509e4 | quote: No billing. Downloads in the sandbox mode do not incur any charges.
  - [5] 2026-11-03: sandbox gives no main renditions, only demo content | capture: sha256:fa41f7a999d8e03b1429ac5b0271f8fd42629bb1727d474f68bfa511bd4509e4 | quote: Restricted downloads. The main renditions of a content item (for example, high-resolution images) are not available for download in the sandbox mode.
  - [5] 2026-11-03: one API key opens every mode the account is permitted | capture: sha256:fa41f7a999d8e03b1429ac5b0271f8fd42629bb1727d474f68bfa511bd4509e4 | quote: You can use the same API key to access all of the modes that you are allowed to use.
- sources:
  - [1] https://api.ap.org/media/v/docs/Getting_Started_API.htm
  - [2] https://api.ap.org/media/v/docs/FrequentlyAskedQuestions.htm
  - [3] https://api.ap.org/media/v/docs/Pricing_Information.htm
  - [4] https://api.ap.org/media/v/docs/Quota_Limits.htm
  - [5] https://api.ap.org/media/v/docs/Access_Modes.htm
