# GNews API

> gnews.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gnews/ | JSON https://fshy.ajam.dev/api/v1/entity/gnews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GNews API

- `data-apis/gnews` | qualifies-with-caveat | evidence documented | binding request-rate | category news search API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:28:40.847Z (live) | stale on 2026-12-04
- url https://gnews.io/pricing
- free tier: Free plan, EUR 0: 100 requests a day, up to 10 articles a request, articles 12 hours late, 30 days of history. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The counter resets at 00:00 UTC and unused requests do not carry over. Article content is truncated to a short excerpt on the Free plan, and pagination stops at 1,000 articles a query. CORS allows only localhost. The next plan up is Essential at EUR 49.99 a month for 1,000 requests a day. A free education plan built on Essential (1,000 requests a day, 25 articles a request, history back to 2020, full content) is granted after a manual review to students, researchers and teaching staff at a recognised institution.
- per-object cap: 10 articles a request on the Free plan; content truncated to a short excerpt | note: unverified: behind a sign-up. The first-party pages say only 'a short excerpt' for the Free plan content and give no length. Sample responses show an excerpt of 250 characters followed by '... [N chars]' (the documentation's JSON sample and a third-party sample of ten articles), and a third-party benchmark on a Free key reported a median visible content length of 265 characters over 80 values.
- retention: search reaches the last 30 days, and articles appear after a 12-hour delay | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for an email and a password, or Google sign-in, and the email is verified; the Free plan never asks for payment details. A trial of a paid plan asks for a payment method.
- interface: rest
- limits:
  - request-rate (binding): 100 requests a day on the Free plan, reset at 00:00 UTC; over it the API answers 403 [1]
  - request-rate (binding): 1 request a second on the Free plan; over it the API answers 429 [2]
  - per-object-cap: 10 articles a request on the Free plan; pagination stops at 1,000 articles a query [2]
- binding note: 100 requests a day is the first ceiling; at 10 articles a request that is at most 1,000 articles a day.
- interface detail: REST over HTTPS: GET /api/v4/search and /api/v4/top-headlines, with the key in the apikey parameter
- endpoint: https://gnews.io/api/v4/search
- tooling: any HTTP client; official Python, JavaScript and PHP packages
- composes with: Headline and article-metadata search with the article URL in each result; the full page is fetched separately by a crawler.
- reliability: Over the daily quota the API answers 403 until 00:00 UTC, and over 1 request a second it answers 429; the 99.95% uptime commitment covers only the Business and Enterprise plans.
- notes: Bulk path: none; the API pages up to 1,000 articles a query.
- evidence note: unverified: behind a sign-up. The 101st request of a day answering 403, a second request inside one second answering 429 and the Free plan content excerpt length need a free key and were not measured: the 403 and the 429 are documented, and no first-party page states the excerpt length. Quota, delay, history window, rate and sign-up fields are read from first-party pages (pricing, FAQ, error handling); a call with no key answered HTTP 400 'You did not provide an API key.', which the error handling page documents for a missing key. A call with a free key would move this to measured.
- evidence:
  - [1] 2026-10-31: the Free plan allows 100 requests a day | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: 100 requests per day
  - [1] 2026-10-31: the Free plan returns up to 10 articles a request | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: Up to 10 articles returned per request
  - [1] 2026-10-31: Free plan articles are delayed 12 hours and history reaches 30 days | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: Free gives 100 requests/day and 10 articles per request, with a 12-hour delay and 30 days of history.
  - [1] 2026-10-31:  | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4
  - [1] 2026-10-31: the Free plan asks for no payment details | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: The Free plan is available as soon as your account is activated and never asks for payment details.
  - [1] 2026-10-31: a paid-plan trial asks for a payment method | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: A card is only needed when you start a paid plan or a free trial of one.
  - [1] 2026-10-31: over the daily quota the API answers 403 until the 00:00 UTC reset | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: returns no more data until the counter resets, which happens every day at 00:00 UTC
  - [1] 2026-10-31: unused requests do not carry over | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: Unused requests do not carry over to the next day.
  - [1] 2026-10-31: Free plan content is truncated to a short excerpt | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: On the Free plan the content is truncated to a short excerpt.
  - [1] 2026-10-31: Essential, the next plan up, gives 1,000 requests a day and 25 articles a request | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: Essential gives 1,000 requests/day and 25 articles, Business 5,000 requests/day and 50 articles, Enterprise 25,000 requests/day and 100 articles.
  - [2] 2026-10-31: paid plans start at EUR 49.99 a month | capture: sha256:4d99964c1c6f77614b5561e97cb44fcb33c68f7f48a0fe0cf35d01fd9ab378f8 | quote: Paid plans start at €49.99 per month
  - [2] 2026-10-31: the Free plan allows 1 request a second, and over it the API answers 429 | capture: sha256:4d99964c1c6f77614b5561e97cb44fcb33c68f7f48a0fe0cf35d01fd9ab378f8 | quote: Yes: 1 request per second on the Free plan and 10 requests per second on every paid plan.
  - [2] 2026-10-31: pagination stops at 1,000 articles a query | capture: sha256:4d99964c1c6f77614b5561e97cb44fcb33c68f7f48a0fe0cf35d01fd9ab378f8 | quote: Pagination stops at 1,000 articles per query, so narrow the query with filters or a date range to go deeper.
  - [2] 2026-10-31: CORS on the Free plan allows only localhost | capture: sha256:4d99964c1c6f77614b5561e97cb44fcb33c68f7f48a0fe0cf35d01fd9ab378f8 | quote: On the Free plan, CORS only allows `localhost`, so browser requests from a deployed site are blocked.
  - [2] 2026-10-31: the education plan is built on Essential: 1,000 requests a day, 25 articles, history back to 2020, full content | capture: sha256:4d99964c1c6f77614b5561e97cb44fcb33c68f7f48a0fe0cf35d01fd9ab378f8 | quote: Free access to a plan built on our Essential tier: 1,000 requests per day, up to 25 articles per request, real-time article availability, historical data back to 2020, full article content
  - [2] 2026-10-31: the education plan is for students, researchers and teaching staff at a recognised institution, reviewed one by one | capture: sha256:4d99964c1c6f77614b5561e97cb44fcb33c68f7f48a0fe0cf35d01fd9ab378f8 | quote: Students, researchers and teaching staff working on an academic project, a thesis or coursework at a recognised institution. Requests are reviewed individually
  - [3] 2026-10-31: sign-up verifies the email before the dashboard gives the key | capture: sha256:5ee47832dac43293203ccfe5eb959a30502de27611d0f115e9148e50a146abc8 | quote: Verify your email
  - [3] 2026-10-31: the request pattern is GET /api/v4/{endpoint} with the key in the apikey parameter | capture: sha256:5ee47832dac43293203ccfe5eb959a30502de27611d0f115e9148e50a146abc8 | quote: GEThttps://gnews.io/api/v4/{endpoint}?{parameters}&apikey=YOUR_API_KEY
  - [4] 2026-10-31: the sign-up form takes an email and a password, or Google sign-in | capture: sha256:793164a145aab37864011988b1f2b018f486cfd0f3c3912c6237a927e85fc970 | quote: Sign up with Google
  - [5] 2026-10-31:  | capture: sha256:d642e2f0a6f86f716d563bc449d139403c9b2ef4942fe1b328c1589745a5bacc
  - [5] 2026-10-31:  | capture: sha256:d642e2f0a6f86f716d563bc449d139403c9b2ef4942fe1b328c1589745a5bacc
  - [5] 2026-10-31: the 99.95% monthly uptime commitment covers only the Business and Enterprise plans | capture: sha256:d642e2f0a6f86f716d563bc449d139403c9b2ef4942fe1b328c1589745a5bacc | quote: If you are on a paid Business or Enterprise plan, we commit to a monthly uptime of at least 99.95% for the API.
  - probe:https://gnews.io/api/v4/search?q=test&lang=en&max=1 2026-10-31: a search call with no key answers HTTP 400 | capture: sha256:3c23f2953427a7e81194ac6025927e9f4e41dfd7853bfcb0588a0c9d0d876160 | quote: "status": 400
  - probe:https://gnews.io/api/v4/search 2026-10-31: the keyless answer names the missing key | capture: sha256:63c071ea422c63298508e4cd75844983ba9641ab97e397799b1d2d37da5cc68e | quote: You did not provide an API key.
  - [6] 2026-11-02: the error-handling page maps HTTP 403 to the daily quota being used up, with the reset at 00:00 UTC | capture: sha256:8ac223e4f91921143e01896e9f846023cd7eaf440d05df591932303ad0d3896f
  - [6] 2026-11-02: the error-handling page maps HTTP 429 to more than 1 request a second on the Free plan, and 10 a second on paid plans | capture: sha256:8ac223e4f91921143e01896e9f846023cd7eaf440d05df591932303ad0d3896f | quote: 429Too Many RequestsToo many requests were sent in a short time period The Free plan is limited to 1 request per second Paid plans are limited to 10 requests per second
  - probe:https://gnews.io/api/v4/search?q=test&lang=en&max=1 2026-11-02: a search call with no key answered HTTP 400 | capture: sha256:3147cdf54d946435b590728021a257362a984bdc6649c7efe93dff25d0aa4021 | quote: "status": 400
  - probe:https://gnews.io/api/v4/search?q=test&lang=en&max=1 2026-11-02: the keyless answer names the missing key | capture: sha256:63c071ea422c63298508e4cd75844983ba9641ab97e397799b1d2d37da5cc68e | quote: You did not provide an API key.
  - [7] 2026-11-02: the documentation's response sample shows a truncated content of 250 characters (counted) followed by '... [1862 chars]' | capture: sha256:477bb27a523e2f5732073f18ed0c7a0ba185344313e6a3da13dc85ba4e3542c3 | quote: Today, Apple’s as-yet-unannounced M5 iPad Pro was seemingly leaked by the same YouTuber who last year leaked the M4 MacBook Pro. Thanks to the surprise reveal, we now have benchmarks for Apple’s forthcoming M5 chip, and they point to big gains coming... [1862 chars]
  - [8] 2026-11-02: a third-party sample response shows content cut to 250 characters (counted) before '... [305 chars]', the same cut on all ten articles of the page | capture: sha256:ee996d55ec2ffa581e49175d7b74aa5ec0efcfa79b6f4cdca59c40f3aecd1616 | quote: Le secteur de la gare de Chêne-Bourg va continuer à se développer. Ce mercredi, le Conseil d'Etat a adopté un plan localisé de quartier visant à bâtir, juste à côté de la halte du Léman Express, un nouvel immeuble abritant 115 logements. Les rez-de-c... [305 chars]
  - [5] 2026-11-02: the 99.95% monthly uptime commitment covers only the Business and Enterprise plans | capture: sha256:d642e2f0a6f86f716d563bc449d139403c9b2ef4942fe1b328c1589745a5bacc | quote: If you are on a paid Business or Enterprise plan, we commit to a monthly uptime of at least 99.95% for the API.
  - [6] 2026-11-02: a request with no apikey parameter answers 400 with the message 'You did not provide an API key.' rather than 401 | capture: sha256:8ac223e4f91921143e01896e9f846023cd7eaf440d05df591932303ad0d3896f | quote: Note that a request sent without an `apikey` parameter, or with a malformed one, returns a 400 - Bad Request with the message `You did not provide an API key.` rather than a 401.
  - [9] 2026-11-02: a third-party benchmark that used a Free key reported a median visible content length of 265 characters over 80 truncated values | capture: sha256:69abc62cb11199702dd481ab3e9df2f9f94b51e77ec399d65c9893519c6317ab | quote: The median visible GNews content value was 265 characters, and all 80 tested GNews content values were truncated because the supplied credential was on the free plan.
  - [1] 2026-11-02: the Free plan gives 100 requests a day, 10 articles a request, a 12-hour delay and 30 days of history | capture: sha256:71a8bb44351f01065f79767b9c0bf6897dffb5602cd70e6d928e2fd166d7a9d4 | quote: Free gives 100 requests/day and 10 articles per request, with a 12-hour delay and 30 days of history.
  - [2] 2026-11-02: the Free plan allows 1 request a second, and over it the API answers 429 | capture: sha256:4d99964c1c6f77614b5561e97cb44fcb33c68f7f48a0fe0cf35d01fd9ab378f8 | quote: Yes: 1 request per second on the Free plan and 10 requests per second on every paid plan. Going over that returns `429 Too Many Requests`, so spread out bursts or retry with exponential backoff.
- sources:
  - [1] https://gnews.io/pricing
  - [2] https://gnews.io/faq
  - [3] https://docs.gnews.io/
  - [4] https://gnews.io/register
  - [5] https://gnews.io/legal/terms-of-service
  - [6] https://docs.gnews.io/error-handling
  - [7] https://docs.gnews.io/json-response
  - [8] https://www.cnblogs.com/flyingsir/p/19061708
  - [9] https://webz.io/blog/news-api-benchmarks/webz-io-vs-gnews-api-news-api-comparison/
