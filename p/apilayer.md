# ipstack

> apilayer.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apilayer/ | JSON https://fshy.ajam.dev/api/v1/entity/apilayer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipstack (APILayer)

- `data-apis/ipstack` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://app.apilayer.com/signup/ipstack/free
- free tier: Free plan: 100 requests a month | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: Starter is USD 12.99 a month for 50,000 requests
- per-object cap: not stated
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an APILayer account with email and password, or GitHub or Google sign-in
- interface: rest
- limits:
  - volume-quota (binding): 100 requests a month [1]
- tooling: any HTTP client
- composes with: 100 lookups a month is a test allowance only; a paid plan from USD 12.99 a month is the working route. Bulk path: none free
- reliability: usage notices are sent at 75, 90 and 100 percent of the monthly allowance
- notes: Free requests: 100 a month. Rate limit: not stated. Bulk path: none on the free plan.
- evidence note: the APILayer signup page for the ipstack free plan and the ipstack pricing page were quoted on 2026-10-30 and 2026-10-31; no keyed lookup was made.
- extras:
  - bulk_path: none free
  - free_requests: 100 a month
- evidence:
  - [1] 2026-10-31: the free plan is 100 requests a month | capture: sha256:9afc03f61e17562aa27fb326c097f89235091c89c12ece90565e05f2eca70c8f | quote: 100 Requests / month
  - [1] 2026-10-31: Starter is USD 12.99 a month | capture: sha256:9afc03f61e17562aa27fb326c097f89235091c89c12ece90565e05f2eca70c8f | quote: $12.99/month
  - [1] 2026-10-31: Starter is 50,000 requests a month | capture: sha256:9afc03f61e17562aa27fb326c097f89235091c89c12ece90565e05f2eca70c8f | quote: 50,000 Requests / month
  - [1] 2026-10-31: GitHub and Google sign-in are offered | capture: sha256:9afc03f61e17562aa27fb326c097f89235091c89c12ece90565e05f2eca70c8f | quote: Sign up with GitHubSign up with Google
  - [1] 2026-10-31: the signup form is an APILayer account | capture: sha256:9afc03f61e17562aa27fb326c097f89235091c89c12ece90565e05f2eca70c8f
  - [2] 2026-10-30: ipstack has a free tier with a limited monthly count | capture: sha256:95cc22e805accc1bd5762e271b5dbb4dc06e3de39c1592d15b47d49b61e3afab | quote: Yes, IPstack offers a free IP API tier with a limited number of monthly requests, ideal for personal projects, testing, and small applications.
  - [2] 2026-10-30: usage notices at 75, 90 and 100 percent | capture: sha256:95cc22e805accc1bd5762e271b5dbb4dc06e3de39c1592d15b47d49b61e3afab | quote: Users will be automatically notified via e-mail and on their Account Dashboard once at least 75%, 90%, and 100% of their monthly API Request allowance has been reached.
- sources:
  - [1] https://app.apilayer.com/signup/ipstack/free
  - [2] https://ipstack.com/pricing
