# Currents API

> currentsapi.services | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/currentsapi/ | JSON https://fshy.ajam.dev/api/v1/entity/currentsapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Currents API

- `data-apis/currents-api` | qualifies-with-caveat | evidence documented | binding request-rate | category news search API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:28:46.350Z (live) | stale on 2026-12-04
- url https://currentsapi.services/en/product/price
- free tier: Free plan, USD 0: 250 requests a day (daily cap only), 20 results a request, 30 days of search history, at most 7 days per search; a 300-character text preview per article. | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: Quotas reset at 00:00 UTC; at the daily cap the API answers HTTP 429 with Retry-After, and there is no overage billing. The next plan up is Builder at USD 69 a month for 2,500 requests a day.
- per-object cap: 20 results a request on the Free plan; article text is a 300-character preview | note: Paging stops where (page_number - 1) * page_size passes 5000 rows; a larger offset answers HTTP 400.
- retention: search reaches 30 days back, at most 7 days per search, on the Free plan | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: The sign-up takes a username, an email and a password, or Microsoft, Google or GitHub sign-in; no card. Temporary or disposable email domains are refused where a permanent address is asked for. One account and one API key are held at a time per user, plus-addressed aliases included.
- interface: rest
- limits:
  - request-rate (binding): 250 requests a day per API key on the Free plan, reset at 00:00 UTC [1]
  - per-object-cap: 20 results a request on the Free plan [1]
  - request-rate (binding): unverified: behind a sign-up; no page states the burst window or its request count, and a burst 429 carries Retry-After as the seconds until the window clears [2]
- binding note: 250 requests a day per key is the published hard cap; a burst limit of unpublished window and request count also answers 429.
- interface detail: REST over HTTPS at api.currentsapi.services/v1 (latest-news and search); the key goes in the Authorization header (Bearer or the bare key) or the legacy apiKey parameter
- endpoint: https://api.currentsapi.services/v1/search
- tooling: any HTTP client
- composes with: Article metadata, 300-character previews and source links; the full article is fetched from the source URL by a crawler.
- reliability: At the daily cap or the burst limit the API answers HTTP 429 with Retry-After; a keyless call answered HTTP 401 Authentication required.
- notes: Bulk path: none; the search pages to an offset of 5000 rows.
- evidence note: Quota, result cap, history window and sign-up fields are read from first-party pages; a keyless call answered HTTP 401, so the free key was not exercised.
- evidence:
  - [1] 2026-10-31: Free: 250 requests a day, daily cap only, 20 results a request, 30 days of history, 7 days per search | capture: sha256:218008be611e14e10233e6f45397e661c127c2e160e8ee68eac208ab1a55fb02 | quote: | Free | $0 | 250 | daily cap only | 20 | 30 days | 7 days |
  - [1] 2026-10-31: quotas reset at 00:00 UTC, the cap answers 429 with Retry-After, and there is no overage billing | capture: sha256:218008be611e14e10233e6f45397e661c127c2e160e8ee68eac208ab1a55fb02 | quote: Quotas reset at 00:00 UTC. At the daily cap, the API returns HTTP 429 with a Retry-After header. There is no overage billing.
  - [1] 2026-10-31: the Free plan returns a 300-character text preview | capture: sha256:218008be611e14e10233e6f45397e661c127c2e160e8ee68eac208ab1a55fb02 | quote: Article text: Free returns a 300-character text preview.
  - [1] 2026-10-31:  | capture: sha256:218008be611e14e10233e6f45397e661c127c2e160e8ee68eac208ab1a55fb02
  - [1] 2026-10-31: Builder, the next plan up, is USD 69 a month for 2,500 requests a day | capture: sha256:218008be611e14e10233e6f45397e661c127c2e160e8ee68eac208ab1a55fb02 | quote: | Builder | $69/mo | 2,500 | 75,000 | 50 | 6 months | 31 days |
  - [3] 2026-10-31: the free tier needs no card | capture: sha256:8a02e53560807e362c8359cdecf7e0e4956bee166f9f753d2f8baa6fb608431b | quote: Start with our generous free tier. No credit card required.
  - [3] 2026-10-31: sign-up offers Microsoft, Google and GitHub sign-in, or a username, an email and a password | capture: sha256:8a02e53560807e362c8359cdecf7e0e4956bee166f9f753d2f8baa6fb608431b | quote: or create account with email/password
  - [4] 2026-10-31: temporary or disposable email domains are refused where a permanent address is asked for | capture: sha256:388bb3c6ba1c94f3fe1899f1f5b2a3ea97323593b9a199666a83b18e2356556b | quote: use temporary, disposable, or auto-generated email domains for registration when Currents API Service requests a permanent email address;
  - [5] 2026-10-31:  | capture: sha256:b06f37d996729ee95a2d011e1fef7d515c5ebc8c529fa2a6bded9cc413f10786
  - [4] 2026-10-31:  | capture: sha256:388bb3c6ba1c94f3fe1899f1f5b2a3ea97323593b9a199666a83b18e2356556b | quote: Create permanent copies of, scrape, build databases of such data
  - [2] 2026-10-31: a burst limit also answers 429; its window is not sized | capture: sha256:f7bf999095a38175afc028a109957cd24a0e402f3f10688dbb7717db79a890e7 | quote: Daily quota or burst limit exceeded.
  - [2] 2026-10-31: paging stops at an offset of 5000 rows | capture: sha256:f7bf999095a38175afc028a109957cd24a0e402f3f10688dbb7717db79a890e7 | quote: Offset guardrail: (page_number - 1) * page_size must not exceed 5000 rows; larger offsets are rejected with HTTP 400.
  - [2] 2026-10-31: the key goes in the Authorization header or the legacy apiKey parameter | capture: sha256:f7bf999095a38175afc028a109957cd24a0e402f3f10688dbb7717db79a890e7 | quote: Authentication accepts an API key via the `Authorization` request header (`Bearer <key>` or the bare key) or via the legacy `apiKey` query parameter.
  - probe:https://api.currentsapi.services/v1/latest-news 2026-10-31: a keyless call answers HTTP 401 Authentication required | capture: sha256:70c6bf2ee963e73c450e93baf5ff238cec3c32faa8b0e984fe17feaa5f3648ce | quote: {"status":"401","msg":"Authentication required"}
  - [6] 2026-11-02: the daily quota is a hard cap, and it is the key that exhausts its daily allowance | capture: sha256:dc3cb3ddd769a9b23530bb693941abe3ec071b59d42b0614fc062421d29b8eae | quote: Quota is enforced as a hard daily cap: when your key exhausts its daily allowance
  - [2] 2026-11-02: a burst limit answers 429 and Retry-After then holds the seconds until the burst window clears; no window length or request count is given | capture: sha256:bed213d2e0d489df4e03886abf99b13a1deb2d3ae2b2c1a20a1d5848221160ab | quote: Seconds until the quota resets (UTC midnight) or the burst window clears.
  - [4] 2026-11-02: an account and an API key are held one at a time per user, plus-addressed aliases and bulk sign-ups included | capture: sha256:388bb3c6ba1c94f3fe1899f1f5b2a3ea97323593b9a199666a83b18e2356556b | quote: 4. register or maintain more than one account or API key at any one time, whether directly, through aliases (including plus-addressing), or through automated or bulk account creation;
  - [1] 2026-11-02: Free: 250 requests a day, daily cap only, 20 results a request, 30 days of history, 7 days per search | capture: sha256:218008be611e14e10233e6f45397e661c127c2e160e8ee68eac208ab1a55fb02 | quote: | Free | $0 | 250 | daily cap only | 20 | 30 days | 7 days |
  - [6] 2026-11-02: the X-RateLimit-Limit header reports the daily limit of the key | capture: sha256:dc3cb3ddd769a9b23530bb693941abe3ec071b59d42b0614fc062421d29b8eae | quote: X-RateLimit-Limit: Displays the total daily limit of API calls for your key.
  - [2] 2026-11-02: X-RateLimit-Limit on a 429 is the daily request limit for the key | capture: sha256:bed213d2e0d489df4e03886abf99b13a1deb2d3ae2b2c1a20a1d5848221160ab | quote: Daily request limit for the key.
  - [7] 2026-11-02: HTTP 429 answers both the daily limit and a burst limit | capture: sha256:dfb28e09fda741f82cc993b64d6fc33fe45a4c58942a988481a99db4703e9ffc | quote: 429 Too Many Requests: Daily or burst limits exceeded.
  - [8] 2026-11-02: a free account starts with 250 requests a day | capture: sha256:12a7157fd34ff1fd3b538f8e7fc8b80b5ef080fd2f972341e42b0abbe2d9326d | quote: A free account starts with 250 requests per day.
  - [3] 2026-11-02: the free tier needs no card | capture: sha256:8e8a93ee7491d64cde6dce796d76b87934a005d5d4fcae73a89d0bf69806dd87 | quote: Start with our generous free tier. No credit card required.
  - [3] 2026-11-02: sign-up is open with an email and a password, besides the single sign-on options | capture: sha256:8e8a93ee7491d64cde6dce796d76b87934a005d5d4fcae73a89d0bf69806dd87 | quote: or create account with email/password
  - probe:https://api.currentsapi.services/v1/latest-news 2026-11-02: a keyless call answers HTTP 401 Authentication required | capture: sha256:70c6bf2ee963e73c450e93baf5ff238cec3c32faa8b0e984fe17feaa5f3648ce | quote: {"status":"401","msg":"Authentication required"}
  - [1] 2026-11-02: the Free plan returns a 300-character text preview | capture: sha256:218008be611e14e10233e6f45397e661c127c2e160e8ee68eac208ab1a55fb02 | quote: Article text: Free returns a 300-character text preview.
- sources:
  - [1] https://currentsapi.services/en/product/price
  - [2] https://currentsapi.services/json/swagger.json
  - [3] https://currentsapi.services/en/register
  - [4] https://currentsapi.services/terms
  - [5] https://currentsapi.services/en/faq
  - [6] https://currentsapi.services/en/docs/ratelimit
  - [7] https://currentsapi.services/en/docs/errors
  - [8] https://currentsapi.services/en/news-api-key
