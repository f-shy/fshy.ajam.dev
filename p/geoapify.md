# Geoapify

> geoapify.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geoapify/ | JSON https://fshy.ajam.dev/api/v1/entity/geoapify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Geoapify

- `data-apis/geoapify` | qualifies | evidence documented | binding volume-quota | category geocoding and maps API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:11.228Z (live) | stale on 2026-12-04
- url https://www.geoapify.com/pricing/
- free tier: 3,000 credits a day (about 90,000 a month) at up to 5 requests a second, no credit card; a Geocoding, Reverse Geocoding or Autocomplete request costs 1 credit, a map tile 0.25 credit, and an address inside a batch job 0.5 credit | unit: credits | metered on: request-count | read on: 2026-10-30 | source: [1] | note: the daily quota is soft: steady overuse brings a request to upgrade, and the account can be blocked if that is ignored. The next plan, API 10, is USD 59 a month for 10,000 credits a day at 12 requests a second.
- per-object cap: a batch geocoding job takes up to 1000 addresses | source: [2]
- retention: source: [2]
- egress: not applicable: a query API metered in credits, not bytes | metered: no | source: [1]
- identity: email | detail: an account at myprojects.geoapify.com created with an email address, a password of at least 8 characters with its confirmation, an accepted-terms checkbox and a reCAPTCHA, or with Google or GitHub sign-in; a verification link is emailed after sign-up; no credit card for the Free plan
- interface: rest
- limits:
  - volume-quota (binding): 3,000 credits a day on the Free plan; a geocode is 1 credit and an address in a batch job 0.5 credit [1]
  - request-rate: up to 5 requests a second on the Free plan [1]
  - per-object-cap: up to 1000 addresses in one batch job [2]
- binding note: 5 requests a second allows far more than 3,000 credits in a day, so the daily credit quota is met first
- interface detail: HTTPS to api.geoapify.com/v1/geocode/search and /reverse with the key in the apiKey parameter, and an asynchronous batch endpoint at /v1/batch/geocode/search (POST a job, GET the result as JSON or CSV); a request without a key answers HTTP 401 Invalid apiKey
- endpoint: https://api.geoapify.com/v1/geocode/search
- tooling: any HTTP client; vendor NPM libraries, an API playground and a batch playground
- composes with: 3,000 storable credits a day with no card: 3,000 single geocodes, or more addresses through batch jobs of up to 1000 at 0.5 credit each, with results kept with no limit; the same key serves map tiles at 4 tiles a credit. Bulk path: the batch endpoint, plus free country-by-country downloads of OSM-derived localities and postcodes
- reliability: the daily quota is soft and the rate is not throttled at once, but steady overuse brings an upgrade request and the account can be blocked if it is ignored; spreading requests over several accounts or projects to stay on a lower plan can disable access
- notes: Bulk path: the asynchronous batch endpoint (up to 1000 addresses a job at 0.5 credit each) and free OSM-derived localities and postcodes downloads.
- evidence note: the pricing page, the pricing-details page, the batch geocoding docs, the terms, the homepage and the downloads pages were quoted on 2026-10-30; a keyless geocode answered HTTP 401, and the localities download directory answered HTTP 200 with a file listing. No account was opened, so no keyed geocode was made; one would move it to measured.
- extras:
  - bulk_path: batch geocoding jobs of up to 1000 addresses at 0.5 credit each; free localities and postcodes downloads
- evidence:
  - [1] 2026-10-30: the Free plan gives 3,000 credits a day | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: 3,000 credits / day
  - [1] 2026-10-30: the Free plan needs no credit card | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: No credit card required
  - [1] 2026-10-30: the Free plan rate is up to 5 requests a second | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: Up to 5 requests/second
  - [1] 2026-10-30: the next plan, API 10, is 10,000 credits a day | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: 10,000 credits / day
  - [1] 2026-10-30: API 10 is USD 59 billed monthly | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: $59
  - [1] 2026-10-30: API 10 allows up to 12 requests a second | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: Up to 12 requests/second
  - [1] 2026-10-30: a geocoding request costs 1 credit | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: In general, 1 API request costs 1 credit for simple requests like Geocoding API, Places API, Routing API.
  - [1] 2026-10-30: the daily quota is soft, with an upgrade request and a possible block on steady overuse | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: Our limits are "soft". If your usage constantly goes over the quota we contact you and ask for an upgrade. We reserve the right to block your account if you ignore our emails.
  - [1] 2026-10-30: going over the rate is not throttled at once, but persistent overuse can be restricted | capture: sha256:78c69d1c6e73c65a025a95d7952d4e4a1d48747870e50a7092e6340397ac10d9 | quote: In general, we do not throttle when you go over the limits.
  - [3] 2026-10-30: the Free plan is about 90,000 credits a month | capture: sha256:f075d05fdc86abfdf428d8fb119c3dceb7469713a2704601ac60d70b6dbf5d2a | quote: ~90,000 credits / month
  - [3] 2026-10-30: a map tile costs 0.25 credit | capture: sha256:f075d05fdc86abfdf428d8fb119c3dceb7469713a2704601ac60d70b6dbf5d2a | quote: 1 Geoapify Map Tile request costs 0.25 credits (4 map tiles = 1 credit)
  - [3] 2026-10-30: each call inside a batch job counts 0.5 credit | capture: sha256:f075d05fdc86abfdf428d8fb119c3dceb7469713a2704601ac60d70b6dbf5d2a | quote: Each API call included in the batch is counted with a coefficient of 0.5, which helps to offer more cost-effective pricing for batched requests.
  - [3] 2026-10-30: a batch of 1000 addresses costs 502 credits in all | capture: sha256:f075d05fdc86abfdf428d8fb119c3dceb7469713a2704601ac60d70b6dbf5d2a | quote: Therefore, the total cost for this asynchronous request would be 500 credits (API calls) + 1 credit (job creation) + 1 credit (result request) = 502 credits.
  - [2] 2026-10-30: a batch geocoding job takes up to 1000 addresses | capture: sha256:aea8811493abb74f145f2da227e0488a6d0d63788357d10c4ba2f6e69935ab0f | quote: The API accepts up to 1000 addresses in one batch.
  - [2] 2026-10-30:  | capture: sha256:aea8811493abb74f145f2da227e0488a6d0d63788357d10c4ba2f6e69935ab0f | quote: Cache/store results with no limits.
  - [2] 2026-10-30: the batch endpoint takes a POST job | capture: sha256:aea8811493abb74f145f2da227e0488a6d0d63788357d10c4ba2f6e69935ab0f | quote: `POST https://api.geoapify.com/v1/batch/geocode/search?&apiKey=YOUR_API_KEY&OPTIONAL_REQUEST_PARAMS`
  - [4] 2026-10-30:  | capture: sha256:8bb9871f0092466a8f2a703ae20450fb7132426506f196eba2fb719f1083f888
  - [5] 2026-10-30:  | capture: sha256:2ba58423076dc3b6d429481439495e836339326724fb8e16501a7f838fcaa608
  - [5] 2026-10-30: requests spread over several accounts or projects to stay on a lower plan can disable access | capture: sha256:2ba58423076dc3b6d429481439495e836339326724fb8e16501a7f838fcaa608
  - [6] 2026-10-30: a new account is created from the same page | capture: sha256:1d5b27995b3334ee06e0615902797109e7114962b9ff5bdfdf0e8e0ae231e42f | quote: Not registered yet? Create an Account
  - [7] 2026-10-30: a free country-by-country localities download compiled from OpenStreetMap exists | capture: sha256:c4811a8814f1b1dd8038e90779eb1db07486e4f32bd2778adf171f9ad5bfad1d | quote: Quick answer: Geoapify's World Cities Database is a free, country-based download of localities compiled from OpenStreetMap.
  - [8] 2026-10-30: a postcodes dataset is published as direct downloads | capture: sha256:db3b72f82e75d330aadbc3b18e75013f543c4354dc66f3322a7c393505203f31 | quote: ## Postcodes Dataset (Direct Downloads)
  - probe:https://www.geoapify.com/data-share/localities/#body 2026-10-30: the localities download directory answers anonymously with per-country ZIP files | capture: sha256:7a3bffbf7da002956f8f8e72fcffe1e6551897779d740402d1af668895ddc8a5 | quote: <head><title>Index of /data-share/localities/</title></head>
  - probe:https://api.geoapify.com/v1/geocode/search?text=Zurich#body 2026-10-30: the geocode endpoint answers and refuses a request with no key | capture: sha256:41a53158be87dc55c378c5c63933a7d2e79c41896d5582140d24191473469a2a | quote: "message":"Invalid apiKey"
  - [9] 2026-11-02: the account-creation form requires an email, a password, an accepted-terms checkbox and a reCAPTCHA, and has a password confirmation | capture: sha256:927cbe502417e0c606915e31fa72bb3a5a61088d13b0b0f52e97e2697311d3ad | quote: this.registerForm=this.fb.group({email:["",[N.required,N.email]],password:["",[N.required,i.strong]],passwordConfirm:[""],policyConcern:[!1,N.requiredTrue],recaptcha:[null,N.required]}
  - [9] 2026-11-02: the account form accepts a password of 8 or more characters | capture: sha256:927cbe502417e0c606915e31fa72bb3a5a61088d13b0b0f52e97e2697311d3ad | quote: static strong(e){return e.value&&e.value.length>=8?null:{strong:!0}}
  - [10] 2026-11-02: the rendered account-creation form asks for an email address | capture: sha256:3248963f8d1e68f6ceea95567865ed123e6433dc4123adfeec9d419d379ced04 | quote: Create a new account Enter your details to get started with Geoapify. Email address
  - [9] 2026-11-02: the account-creation form of the account app asks for a password and a password confirmation | capture: sha256:927cbe502417e0c606915e31fa72bb3a5a61088d13b0b0f52e97e2697311d3ad | quote: a(58,"label",22),c(59,"Password"),s(),P(60,"app-password-input",23),a(61,"label",24),c(62,"Confirm password")
  - [10] 2026-11-02:  | capture: sha256:4d3efecb7fc6da3e83baf75ada403e5b5aab33b89b86c42413d6336124d915df
  - [9] 2026-11-02: the account-creation form carries a reCAPTCHA component | capture: sha256:927cbe502417e0c606915e31fa72bb3a5a61088d13b0b0f52e97e2697311d3ad | quote: a(73,"div",29),P(74,"re-captcha",30),s()
  - [9] 2026-11-02: a verification email is sent right after the account is registered | capture: sha256:927cbe502417e0c606915e31fa72bb3a5a61088d13b0b0f52e97e2697311d3ad | quote: this.authService.doRegister(e).then(()=>{this.authService.doSendVerificationEmail()
  - [11] 2026-11-02: the sign-in page offers Google and GitHub next to email and password | capture: sha256:7b2f605619fdcf9229c8df0a3c0b4ad1d7b4b61de7826b2919439efb2a190fba | quote: Sign in with GoogleSign in with GitHub
  - [12] 2026-11-02: the account help names email and password, Google and GitHub as the sign-in methods | capture: sha256:69e1b54479028ab817b1010df71a3b32059445ce95c0e4b577580a928580232e | quote: | Google or GitHub | Manage your password and primary account security with the external provider. Password and authenticator settings are not available in MyProjects for these accounts. |
  - [1] 2026-11-02: the Free plan needs no credit card | capture: sha256:7589b9aa7c3a02a10d33430815a05177bbd995eed49f7e9bea1375b213b1a898 | quote: No credit card required
  - [1] 2026-11-02: the Free plan rate is up to 5 requests a second | capture: sha256:7589b9aa7c3a02a10d33430815a05177bbd995eed49f7e9bea1375b213b1a898 | quote: Up to 5 requests/second
- sources:
  - [1] https://www.geoapify.com/pricing/
  - [2] https://apidocs.geoapify.com/docs/geocoding/batch/
  - [3] https://www.geoapify.com/pricing-details/
  - [4] https://www.geoapify.com/
  - [5] https://www.geoapify.com/terms-and-conditions/
  - [6] https://myprojects.geoapify.com/
  - [7] https://www.geoapify.com/download-all-the-cities-towns-villages/
  - [8] https://www.geoapify.com/downloads/
  - [9] https://myprojects.geoapify.com/main-EYR24PFG.js
  - [10] https://myprojects.geoapify.com/register
  - [11] https://myprojects.geoapify.com/login
  - [12] https://myprojects.geoapify.com/help/account-security/
