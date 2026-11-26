# OpenGeocoding

> opengeocoding.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opengeocoding/ | JSON https://fshy.ajam.dev/api/v1/entity/opengeocoding.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenGeocoding

- `data-apis/opengeocoding` | qualifies-with-caveat | evidence documented | binding volume-quota | category geocoding, autocomplete and reverse geocoding API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-12-03
- url https://opengeocoding.com/pricing
- free tier: Free plan, USD 0: 50,000 requests a month at 2 requests a second, no credit card; monthly periods run from the signup date and unused free credits expire at the end of each period | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: each successful search, retrieve, reverse or resolve-region call costs one credit; autocomplete and region calls cost no credits but count against the rate limit; there is no daily cap and no automatically billed overage; the next plan, Starter, is USD 29 a month for 300,000 requests
- per-object cap: the bulk geocoding page runs a CSV as parallel single search requests at the plan's rate, 7,200 addresses an hour on Free, and names no batch endpoint; dedicated-capacity bulk jobs are an Enterprise item | source: [2]
- retention: source: [1]
- egress: not applicable: a query API metered in credits, not bytes | metered: no | source: [1]
- identity: email | detail: an account at opengeocoding.com with an email address and a password, or GitHub sign-in; free credits are granted after email verification
- interface: rest
- limits:
  - volume-quota (binding): 50,000 requests a month on the Free plan; free credits expire at the end of each period and there is no automatic overage [3]
  - request-rate: 2 requests a second on the Free plan, shared across all API keys; HTTP 429 with Retry-After beyond it [1]
- binding note: the bulk geocoding page puts the 50,000 allowance at about 7 hours at the full 2 requests a second, so the monthly allowance is met first
- interface detail: HTTPS JSON API at api.opengeocoding.com/v1/search (a POST with the key in an x-api-key header), a gRPC lane that shares the same credits and rate limit, and a remote MCP server with OAuth sign-in; a keyless call answered HTTP 401 unauthenticated
- endpoint: https://api.opengeocoding.com/v1/search
- tooling: any HTTP or gRPC client; a CSV geocoding script on the bulk geocoding page; a remote MCP server
- composes with: 50,000 permanently storable searches a month with no card, then USD 29 a month for 300,000; autocomplete and region calls cost no credits; bulk work is a CSV run through the search API at 2 requests a second
- reliability: when credits run out billable operations answer HTTP 429 until a new grant, while autocomplete and regions stay available at zero credits; there is no uptime guarantee outside an enterprise agreement
- notes: Free requests: 50,000 a month at 2 requests a second. Rate limit: 2 requests a second on Free. Bulk path: a CSV run through the search API at the plan's rate; dedicated bulk jobs on Enterprise. Last resort: the engine is source-available and a self-hosting licence is part of Enterprise.
- evidence note: the pricing page, the home page, the terms, the privacy statement and the bulk geocoding page were quoted on 2026-11-02; a keyless call answered HTTP 401. No account was opened, so the free monthly credits and the sign-up form were not exercised.
- extras:
  - free_requests: 50,000 requests a month, periods measured from the signup date
  - rate_limit: 2 requests a second on Free, shared across all API keys
  - bulk_path: CSV script over the search API at the plan's rate (7,200 addresses an hour on Free); dedicated bulk jobs on Enterprise
- evidence:
  - [1] 2026-11-02:  | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: ## Free Prototypes and side projects.
  - [4] 2026-11-02: the home page offers 50,000 free requests a month | capture: sha256:104ba2cb7cb9efd5386ffbd138e82928d1ba48c56b92b0a1e1e58344782fa839 | quote: Start with 50,000 free requests a month.
  - [4] 2026-11-02: no credit card and up to 2 requests a second on the free plan | capture: sha256:104ba2cb7cb9efd5386ffbd138e82928d1ba48c56b92b0a1e1e58344782fa839 | quote: No credit card. Up to 2 requests/second on the free plan.
  - [3] 2026-11-02: free credits are granted after email verification, run in monthly periods from the signup date and expire unused | capture: sha256:41d36aed55e9f0885ad79828a1f0cdedade076978e1ed6d6de8f57646cae8e7f | quote: The free tier grants credits after email verification, with monthly periods measured from your signup date, not calendar months. Unused free credits expire at the end of their period and do not carry over.
  - [1] 2026-11-02: one successful call costs one credit | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: Each successful search, retrieve, reverse or resolve-region call costs one credit (HTTP JSON 2xx or gRPC status 0).
  - [1] 2026-11-02: autocomplete and regions cost no credits but share the rate limit | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: Autocomplete and regions consume no credits, but remain authenticated and share your account rate limit.
  - [1] 2026-11-02: there are no daily limits, only the per-second rate limit | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: No. Use your monthly requests whenever you need them, subject to your account’s per-second rate limit.
  - [1] 2026-11-02: usage beyond the credits held is never billed | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: You are never billed for usage beyond what you bought.
  - [3] 2026-11-02: there is no automatically billed overage | capture: sha256:41d36aed55e9f0885ad79828a1f0cdedade076978e1ed6d6de8f57646cae8e7f | quote: There is no automatically billed overage.
  - [1] 2026-11-02: when credits run out billable operations answer 429 until new credits arrive | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: Billable operations answer 429 until new credits become available, normally at your next billing period.
  - [1] 2026-11-02: over the rate limit HTTP requests answer 429 with Retry-After | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: HTTP requests return 429 with Retry-After; gRPC returns RESOURCE_EXHAUSTED.
  - [1] 2026-11-02: results can be stored forever on every plan including the free one | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: Yes, forever, on every plan, including the free one.
  - [1] 2026-11-02:  | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc
  - [1] 2026-11-02: the Starter plan is USD 29 a month | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: $29 /month + tax
  - [1] 2026-11-02: the Starter plan includes 300,000 requests a month | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: 300,000 requests / month
  - [1] 2026-11-02: bulk jobs on dedicated capacity and a self-hosting licence are Enterprise items | capture: sha256:ffb9ed62fa7109f1ac2910142d6728e6e3ffcf4ab7c1d57339b933ca0c9ca0bc | quote: Bulk geocoding at the speed of light: dedicated capacity, SLA, self-hosting.
  - [2] 2026-11-02: a spreadsheet of addresses is run through the search API at the plan's speed | capture: sha256:5dc25e37306b7a9693662b86b7d40c80aad2850990dacfc11d3fb71bcbceb550 | quote: Run a spreadsheet of addresses through the search API at your plan's speed, or send millions of rows to a dedicated Enterprise cluster.
  - [2] 2026-11-02: the Free plan runs 2 requests a second, 7,200 addresses an hour, against 50,000 a month | capture: sha256:5dc25e37306b7a9693662b86b7d40c80aad2850990dacfc11d3fb71bcbceb550 | quote: | Free $0/month | 2 | 7,200 | 50,000 | ~7 h |
  - [2] 2026-11-02: the search endpoint is api.opengeocoding.com/v1/search | capture: sha256:5dc25e37306b7a9693662b86b7d40c80aad2850990dacfc11d3fb71bcbceb550 | quote: API_URL = os.environ.get('OPENGEOCODING_API_URL', 'https://api.opengeocoding.com') + '/v1/search'
  - [2] 2026-11-02: the key goes in an x-api-key header | capture: sha256:5dc25e37306b7a9693662b86b7d40c80aad2850990dacfc11d3fb71bcbceb550 | quote: headers={'x-api-key': API_KEY, 'Content-Type': 'application/json'},
  - [3] 2026-11-02: the request rate and credits are shared across API keys and protocols | capture: sha256:41d36aed55e9f0885ad79828a1f0cdedade076978e1ed6d6de8f57646cae8e7f | quote: Your account has a request rate and a balance of request credits, shared across its API keys and protocols.
  - [3] 2026-11-02: there is no uptime guarantee outside an enterprise agreement | capture: sha256:41d36aed55e9f0885ad79828a1f0cdedade076978e1ed6d6de8f57646cae8e7f | quote: We aim for high availability but, outside an enterprise agreement with an SLA, provide the Service without a guaranteed uptime.
  - [3] 2026-11-02: creating several free accounts to get around quotas is barred | capture: sha256:41d36aed55e9f0885ad79828a1f0cdedade076978e1ed6d6de8f57646cae8e7f | quote: try to get around rate limits or quotas, for example by creating several free accounts;
  - [3] 2026-11-02: an account is needed to get API keys | capture: sha256:41d36aed55e9f0885ad79828a1f0cdedade076978e1ed6d6de8f57646cae8e7f | quote: You need an account to get API keys.
  - [5] 2026-11-02: an account holds an email address, a name or a GitHub sign-in | capture: sha256:6da57ff3ee6c7ecd9681ed813fa3e5ebc4bb4058b83931c837ce440d74f1dc8e | quote: Email address, name, and your GitHub account ID, username, profile name and picture if you sign in with GitHub
  - [5] 2026-11-02: email and password sign-in exists | capture: sha256:6da57ff3ee6c7ecd9681ed813fa3e5ebc4bb4058b83931c837ce440d74f1dc8e | quote: Authenticating email/password sign-ins
  - [4] 2026-11-02: a remote MCP server with OAuth sign-in is offered | capture: sha256:104ba2cb7cb9efd5386ffbd138e82928d1ba48c56b92b0a1e1e58344782fa839 | quote: Remote MCP server · OAuth sign-in
  - [4] 2026-11-02: the engine is source-available under the PolyForm Shield licence | capture: sha256:104ba2cb7cb9efd5386ffbd138e82928d1ba48c56b92b0a1e1e58344782fa839 | quote: Our API runs on OpenGeocoding, the source-available geocoding engine we build and maintain under the PolyForm Shield licence.
  - probe:https://api.opengeocoding.com/v1/search 2026-11-02: a keyless call answers HTTP 401 | capture: sha256:e7802c9f91bd56b994b7b47268afa431f1b487fa51338a7e49760581c32f9c34 | quote: "status": 401
  - probe:https://api.opengeocoding.com/v1/search#body 2026-11-02: the keyless call is refused and names the x-api-key header | capture: sha256:c1f73064904cb24d41ea06d6297d2877f1adbeb87721bd18c2a51f8e58185f2c | quote: Pass your API key in the x-api-key header.
- sources:
  - [1] https://opengeocoding.com/pricing
  - [2] https://opengeocoding.com/bulk-geocoding
  - [3] https://opengeocoding.com/legal/terms
  - [4] https://opengeocoding.com/
  - [5] https://opengeocoding.com/legal/privacy
