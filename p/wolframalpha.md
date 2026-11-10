# Wolfram

> wolframalpha.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wolframalpha/ | JSON https://fshy.ajam.dev/api/v1/entity/wolframalpha.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wolfram|Alpha API

- `data-apis/wolfram-alpha-api` | qualifies-with-caveat | evidence documented | binding request-rate | category computational knowledge API | tier Get Started for Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:45.809Z (live) | stale on 2026-12-03
- url https://products.wolframalpha.com/api
- free tier: Free access for up to 2,000 non-commercial API calls per month, from a Wolfram ID and an AppID. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The terms count the results received within a 30-day period, set the quota in the API Plan Summary issued at registration, and let Wolfram change it. The FAQ describes the free access as non-commercial experimental use with a low monthly cap on queries.
- per-object cap: the LLM API returns at most 6800 characters by default, set with the maxchars parameter
- retention: not applicable: every answer is computed on the fly for the query, and the FAQ answers no to a data download | source: [1]
- egress: not applicable: a query API answered per call, not metered in bytes | metered: no | source: [1]
- identity: email | detail: A Wolfram ID is required. Its sign-up form asks for an email (which becomes the Wolfram ID), a first name, a last name and a password, with no card or phone field. The first AppID follows a one-time survey about intended usage and takes an application name and a simple description.
- interface: rest
- limits:
  - request-rate (binding): 2,000 non-commercial API calls per month [1]
  - request-rate (binding): unverified: no per-second, per-minute or per-day limit is published; the quota in force for an AppID is in the API Plan Summary received at registration in the Developer Portal, behind a sign-up [2]
- limits note: A third-party integration guide reports a limit of 100 calls/day and 2000/month for regular users; no Wolfram page states a daily cap.
- binding note: The 2,000 calls a month is the one ceiling that a Wolfram page states; a daily or per-second limit, if any, is in the plan summary behind the sign-up.
- interface detail: REST over HTTP GET with the AppID in the appid parameter: the Full Results API at api.wolframalpha.com/v2/query (XML or JSON), the Short Answers API at api.wolframalpha.com/v1/result (plain text), the Simple API at api.wolframalpha.com/v1/simple (an image) and the LLM API at www.wolframalpha.com/api/v1/llm-api
- endpoint: https://api.wolframalpha.com/v2/query
- tooling: any HTTP client, or one of the language bindings that the vendor's libraries page lists
- composes with: Computed knowledge answers, one call at a time, at 2,000 calls a month. Bulk path: none; the FAQ answers no to a raw-data export and no to a data download. For a table-shaped read of open data, see data-apis/wikidata.
- reliability: A call to the Full Results endpoint with no AppID answers HTTP 400 with the message Appid Missing.
- notes: Bulk path: none; the FAQ answers no to both a raw-data export and a data download. Paid plans: the overview page shows no price and its Pricing Information link opens a contact form.
- evidence note: The quota, the sign-up fields and the FAQ answers are read from first-party pages; a keyless call answered 400 Appid Missing. The free key was not exercised, so the AppID creation dialog, the API Plan Summary and any per-day or per-second limit are unread; they sit behind a Wolfram ID sign-in.
- evidence:
  - [1] 2026-11-02: the free access is up to 2,000 non-commercial API calls per month | capture: sha256:4f08829e81b64b8a5dae1019b22e31a7660699b35b149beeecb5da4f20591247 | quote: Immediate free access for up to 2,000 non-commercial API calls per month
  - [3] 2026-11-02: the text bundle of the API FAQ page states the allowance as up to 2,000 free API calls per month | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517 | quote: You can make up to 2,000 free API calls per month.
  - [3] 2026-11-02: the FAQ describes the free access as non-commercial experimental use with a low monthly cap on queries | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517 | quote: Yes and no. Wolfram|Alpha APIs are available for free for non-commercial experimental use with a low monthly cap on queries.
  - [2] 2026-11-02: the limits include the number of results received within a 30-day period and the number of allowed AppIDs | capture: sha256:b9958dbce5f55fc0cc98f11f765a5d043f0a33234c0e6bf16701e3f338a43fc9 | quote: the number of Results that may be received by Your API Client within a 30-day period and the number of allowed AppIDs associated with your API Client
  - [2] 2026-11-02: the quotas are expressed in an API Plan Summary received at registration in the Developer Portal | capture: sha256:b9958dbce5f55fc0cc98f11f765a5d043f0a33234c0e6bf16701e3f338a43fc9 | quote: will be expressed in the API Plan Summary you will receive when you register for the Wolfram|Alpha API through the
  - [2] 2026-11-02: the limits and quotas can be changed by Wolfram | capture: sha256:b9958dbce5f55fc0cc98f11f765a5d043f0a33234c0e6bf16701e3f338a43fc9 | quote: Wolfram|Alpha may adjust these limits and usage quotas at its discretion.
  - [3] 2026-11-02: access needs a Wolfram ID and an AppID (API key) | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517 | quote: To access any Wolfram|Alpha API, you need two things: a current Wolfram ID and an AppID (API key).
  - [2] 2026-11-02: a Wolfram ID is required to access the API | capture: sha256:b9958dbce5f55fc0cc98f11f765a5d043f0a33234c0e6bf16701e3f338a43fc9 | quote: A Wolfram Login Service Account (Wolfram ID) will be required in order to access the Wolfram|Alpha API.
  - [4] 2026-11-02: the Wolfram ID sign-up form asks for an email, a first name, a last name and a password, and has no card or phone field | capture: sha256:ff9bfa5f9cb5bd7d2502e026d977ee04eca21128900843975c445afca0965110 | quote: Email(this will be your Wolfram ID) First name Last name Password(at least 8 characters) Confirm password
  - [5] 2026-11-02: the first AppID follows a one-time survey about intended usage and takes an application name and a simple description | capture: sha256:2d4243b800fee664aacf686cdeac6907ef2f1b544649d692d32bc48c257c7a45 | quote: After a one-time survey about intended usage, the AppID creation dialog will appear. Give your application a name and a simple description to register an AppID.
  - [3] 2026-11-02:  | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517 | quote: Yes, upon entering into a commercial licensing agreement.
  - [1] 2026-11-02: the Pricing Information link of the overview goes to a purchase contact page | capture: sha256:4f08829e81b64b8a5dae1019b22e31a7660699b35b149beeecb5da4f20591247 | quote: [Pricing Information](https://products.wolframalpha.com/contact-us/purchase)
  - [6] 2026-11-02: that page is a contact form for purchasing a product, with no price on it | capture: sha256:84ad4dc9eb2381a1f27d5ea58fe4de63a5452cd360ce7e648c90318ee1ad21f5 | quote: Main Purpose for Contacting Us Purchasing product
  - [3] 2026-11-02: the FAQ answers no to a raw-data export: the APIs give processed answers | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517 | quote: No. The purpose of Wolfram|Alpha is to provide specific answers to questions, using both data and algorithms. The Wolfram|Alpha APIs are intended to provide fully processed answers, rather than raw data.
  - [3] 2026-11-02: the FAQ answers no to a data download: results are computed on the fly | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517 | quote: No. Almost every data result that Wolfram|Alpha gives is computed on the fly, so it would be impossible to download all of Wolfram|Alpha\'s data.
  - [3] 2026-11-02:  | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517
  - [7] 2026-11-02: a third-party integration guide reports 100 calls/day and 2000/month for regular users; the figure is not on a Wolfram page | capture: sha256:dc377755d60859df01861ba7e4db28206184d7901caf3f7b77da028fc23d5b34 | quote: Note: Wolfram API calls are limited to 100 calls/day and 2000/month for regular users.
  - [8] 2026-11-02: the Full Results API is a REST API over HTTP GET that returns XML or JSON | capture: sha256:4d976f1c0a8674d3d006acfe131d8b8157f64d6c21a18e09ca7b86449c6e8289 | quote: It is implemented in a standard REST protocol using HTTP GET requests. Each result is returned as a descriptive XML or JSON structure wrapping the requested content format.
  - [8] 2026-11-02: the Full Results API base URL is api.wolframalpha.com/v2/query | capture: sha256:4d976f1c0a8674d3d006acfe131d8b8157f64d6c21a18e09ca7b86449c6e8289 | quote: http://api.wolframalpha.com/v2/query
  - [9] 2026-11-02: the Short Answers API is at api.wolframalpha.com/v1/result with the appid parameter | capture: sha256:c22b49b263cc531a08e3fd2db4be846626478316d4610343aa33118e430ea012 | quote: http://api.wolframalpha.com/v1/result?appid=DEMO
  - [10] 2026-11-02: the Simple API is at api.wolframalpha.com/v1/simple with the appid parameter | capture: sha256:554e0aae9b6b7d6c1603e78ddf51f928f7416baaa4ebbd45874970aa11482158 | quote: http://api.wolframalpha.com/v1/simple?appid=DEMO
  - [5] 2026-11-02: the LLM API is at www.wolframalpha.com/api/v1/llm-api with the appid parameter | capture: sha256:ca421e2e5be378eb43aa7a89048950ff7295218c78070e9b6a6fdc037af33332 | quote: https://www.wolframalpha.com/api/v1/llm-api?appid=DEMO
  - [5] 2026-11-02: the LLM API returns at most 6800 characters by default and the maxchars parameter changes it | capture: sha256:ca421e2e5be378eb43aa7a89048950ff7295218c78070e9b6a6fdc037af33332 | quote: By default, this will return at most 6800 characters. To update the response length, change maxchars to another value
  - [9] 2026-11-02: the Short Answers API returns a single plain text result | capture: sha256:c22b49b263cc531a08e3fd2db4be846626478316d4610343aa33118e430ea012 | quote: The Short Answers API returns a single plain text result directly from Wolfram|Alpha.
  - [10] 2026-11-02: the Simple API returns an image | capture: sha256:554e0aae9b6b7d6c1603e78ddf51f928f7416baaa4ebbd45874970aa11482158 | quote: When executed with a valid AppID, this URL will return an image with informational elements relating to the input:
  - [3] 2026-11-02: the service computes answers from its own knowledgebase and algorithms rather than returning web pages | capture: sha256:bcb70c5ad953a7817552fcdd8decc8b879b9b0b374364c17fba18f640ecd7517 | quote: Wolfram|Alpha computes answers to specific questions using its built-in knowledgebase and algorithms.
  - [11] 2026-11-02: any language with web requests and XML/JSON can call the API, and vendor-listed language bindings exist | capture: sha256:dc06594943c23ca571ba769963134d6a21b7b4e4a25cab53031f58ce11ea1ea5 | quote: The Wolfram|Alpha Full Results API can be accessed from any language that supports web requests and XML/JSON.
  - probe:https://api.wolframalpha.com/v2/query?input=population+of+france&output=json 2026-11-02: a Full Results call with no AppID answered HTTP 400 | capture: sha256:a15a0f1648fe30484e85bed62087069f66bf8e25e65f93de0cc5a5335a64ebbb | quote: "status": 400
  - probe:https://api.wolframalpha.com/v2/query?input=population+of+france&output=json 2026-11-02: the body of that keyless call names the missing AppID | capture: sha256:a7bff8339dc1d3c094bf40f770a05a2a63a423c39d0f6a581ee65f455bf9ef1a | quote: {"status":400,"message":"Appid Missing"}
- sources:
  - [1] https://products.wolframalpha.com/api
  - [2] https://products.wolframalpha.com/api/termsofuse
  - [3] https://products.wolframalpha.com/_next/static/chunks/pages/%5Bapi%5D/faqs-69e8c40159193624.js
  - [4] https://account.wolfram.com/auth/create
  - [5] https://products.wolframalpha.com/llm-api/documentation
  - [6] https://products.wolframalpha.com/contact-us/purchase
  - [7] https://www.librechat.ai/docs/configuration/tools/wolfram
  - [8] https://products.wolframalpha.com/api/documentation
  - [9] https://products.wolframalpha.com/short-answers-api/documentation
  - [10] https://products.wolframalpha.com/simple-api/documentation
  - [11] https://products.wolframalpha.com/api/libraries
