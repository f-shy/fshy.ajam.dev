# MapTiler

> maptiler.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/maptiler/ | JSON https://fshy.ajam.dev/api/v1/entity/maptiler.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MapTiler

- `data-apis/maptiler` | qualifies-with-caveat | evidence documented | binding volume-quota | category geocoding and maps API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:27:11.225Z (live) | stale on 2026-12-04
- url https://www.maptiler.com/cloud/pricing/
- free tier: 100,000 API requests a month (each geocoding call, and each query inside a batch call, counts as one request; map tiles count from the same pool), 1,000 search sessions and 5,000 map sessions a month through the SDK, 5 GB of storage in one file; no credit card | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: at either monthly limit the Free plan's maps are suspended for the rest of the month; the Free plan has no paid extra usage. The next plan, Flex, is USD 30 a month for 500,000 API requests and 3,000 search sessions, then USD 0.15 per 1,000 requests.
- per-object cap: a batch geocoding call takes at most 50 semicolon-separated queries, each counted as one request | source: [2]
- retention: source: [3]
- egress: not applicable: a query API metered in requests and sessions, not bytes | metered: no | source: [1]
- identity: email | detail: a MapTiler Cloud account created with an email address, a first and last name and a chosen password, or with Google sign-in; sign-in completes only after the emailed verification link is opened; no credit card for the Free plan
- interface: rest
- limits:
  - volume-quota (binding): 100,000 API requests a month on the Free plan, geocoding and map tiles together; at the limit maps are suspended for the rest of the month [1]
  - volume-quota (binding): 1,000 search sessions a month on the Free plan for the SDK search control [1]
  - per-object-cap: at most 50 queries in one batch geocoding call, each counted as one request [2]
- limits note: unverified: no per-second request rate was found on the pricing page, the Cloud terms (which defer the Free plan limits to the pricing page), the API reference, the Geocoding API reference, the geocoding guide or the sessions guide
- binding note: the 100,000 monthly requests are shared between geocoding and map tiles, and reaching them suspends the Free plan for the rest of the month
- interface detail: HTTPS GET to api.maptiler.com/geocoding/{query}.json (forward, reverse by longitude,latitude, by feature id, and batch with semicolon-separated queries) with the key in the key parameter; an EU-based endpoint is offered; a request without a key answers HTTP 403 Missing key
- endpoint: https://api.maptiler.com/geocoding/{query}.json
- tooling: any HTTP client; the MapTiler Client JS library (geocoding.batch) and the MapTiler SDK JS geocoding control, which is metered in sessions rather than requests
- composes with: 100,000 storable geocodes a month with no card, shared with map tile requests, so a stored table of up to that many addresses a month can be built through batch calls of 50; past the limit the Free plan stops for the rest of the month, and more is Flex at USD 30 a month or the Geoapify free plan (data-apis/geoapify). Bulk path: the batch endpoint only; no hosted geocoding data download. The last resort is self-hosted: the On-prem Free tile download (OpenStreetMap vectors of 2020) that the user installs and runs with MapTiler Server, tiles only, with no geocoder
- reliability: usage beyond the Free plan limits can bring a temporary suspension of the account, and at either monthly limit the Free plan's maps are suspended for the rest of the month
- notes: Bulk path: batch geocoding calls of up to 50 queries, each one request; no hosted data download for geocoding.
- evidence note: the Cloud pricing page, the Cloud terms, the Geocoding API reference, the batch guide, the sessions guide, the search product page and the sign-in page were quoted on 2026-10-30 and 2026-10-31; a keyless geocode answered HTTP 403 Missing key. No account was opened, so no keyed geocode was made; one would move it to measured.
- extras:
  - bulk_path: batch geocoding calls of up to 50 queries, each counted as one request; no geocoding data download
- evidence:
  - [1] 2026-10-30: the Free plan gives 100,000 API requests a month (Flex 500,000) | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: | API requests | 100k/month | 500k/month | Custom |
  - [1] 2026-10-30: the Free plan gives 1,000 search sessions a month (Flex 3,000) | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: | Search sessions | 1k/month | 3k/month | Custom |
  - [1] 2026-10-30: the Free plan gives 5,000 map sessions a month | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: | Sessions | 5k/month | 25k/month | Custom |
  - [1] 2026-10-30: the Free plan has 5 GB of storage in one file | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: 5 GB storage (1 file limit)
  - [1] 2026-10-30: the Free plan needs no credit card | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: No credit card needed
  - [1] 2026-10-30: the Flex plan is USD 30 a month | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: $30/month (USD)
  - [1] 2026-10-30: extra API requests are not available on Free and cost USD 0.15 per 1,000 on Flex | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: | API requests | N/A | $0.15/1k requests | Custom |
  - [4] 2026-10-31: at either monthly limit a Free plan's maps are suspended for the rest of the month | capture: sha256:b8707fa71f5882885dcdd4373089ef392ff75895f3cdf35fb095edef2f4477c3 | quote: When you hit either of these two limits, you get charged extra (on a paid plan) or your maps get suspended for the rest of the month (on a free plan).
  - [4] 2026-10-31: each query inside a batch call counts as one request | capture: sha256:b8707fa71f5882885dcdd4373089ef392ff75895f3cdf35fb095edef2f4477c3 | quote: For example, a batch of 20 queries counts as 20 requests, even though it’s technically one API call.
  - [4] 2026-10-31: a geocoding session covers all search-box interactions in one sitting | capture: sha256:b8707fa71f5882885dcdd4373089ef392ff75895f3cdf35fb095edef2f4477c3 | quote: Similarly, in case of [geocoding](https://docs.maptiler.com/guides/developer/location-services/geocoding-search/), a session includes all interactions with a search field in one sitting.
  - [2] 2026-10-30: a batch call takes at most 50 queries | capture: sha256:61fbf5c45fb8f5e3fe1ca639af8cf037c244c57f799576dc9c902f4fa83894f5 | quote: Each query may be forward, reverse or by feature ID. Maximum of 50 queries are supported.
  - [2] 2026-10-30: every geocoding call needs a MapTiler API key | capture: sha256:61fbf5c45fb8f5e3fe1ca639af8cf037c244c57f799576dc9c902f4fa83894f5 | quote: You need a MapTiler API key to use this service.
  - [5] 2026-10-30: batch geocoding uses the standard endpoint with semicolon-separated queries | capture: sha256:1ba112d8ae155d3324125ebd52aa1b3c4a419f1fbb9dc787574232c7096fc313 | quote: Just make sure you use semicolons `;` to separate individual requests when sending multiple requests at once.
  - [3] 2026-10-30:  | capture: sha256:aed811301dc0076b68c61006d2daa125f8efbb2ee553d6a0875d08efd0f0c323
  - [3] 2026-10-30: each HTTPS geocoding call counts as one request against the plan | capture: sha256:aed811301dc0076b68c61006d2daa125f8efbb2ee553d6a0875d08efd0f0c323 | quote: The geocoding API is part of Cloud. You need to have a [free or paid plan](https://www.maptiler.com/cloud/pricing/); each HTTPS API call is counted as an individual request.
  - [6] 2026-10-30:  | capture: sha256:58eff6a6fa0cdde5d3b37e206f836b62b308db174ef08a4eef4525356354dcba
  - [6] 2026-10-30:  | capture: sha256:58eff6a6fa0cdde5d3b37e206f836b62b308db174ef08a4eef4525356354dcba
  - [6] 2026-10-30:  | capture: sha256:58eff6a6fa0cdde5d3b37e206f836b62b308db174ef08a4eef4525356354dcba
  - [6] 2026-10-30: usage beyond the Free plan limits can suspend the account temporarily | capture: sha256:58eff6a6fa0cdde5d3b37e206f836b62b308db174ef08a4eef4525356354dcba | quote: Usage of the Service beyond these limits may result in temporary suspension of the Service for your account.
  - [7] 2026-10-31: the sign-up widget offers email and password, or Google | capture: sha256:aaae0a72014e8f54b3d0970c5d8ff4b843bfef7f28395336b7e9d358ba8979b7 | quote: "signInOptions": [{"provider": "password"}, {"provider": "google.com"}]
  - [8] 2026-10-30: the On-prem Free plan for self-hosted maps is limited to 100 monthly active users | capture: sha256:56ba21ac42c79dab2b5ff93b0848ff2a2577c2b990fdbc387868601ddf4ed483 | quote: - maximum 100 MAU
  - [8] 2026-10-30: the On-prem Free maps are the 2020 OpenStreetMap vectors and low-resolution satellite | capture: sha256:56ba21ac42c79dab2b5ff93b0848ff2a2577c2b990fdbc387868601ddf4ed483 | quote: OpenStreetMap Vectors (2020)
  - probe:https://api.maptiler.com/geocoding/Zurich.json#body 2026-10-30: the geocoding endpoint answers and refuses a request with no key | capture: sha256:9a206e23b36aee1b80d6b8e4cd1056a849cffba58713dfe1ef9160dbfb3a775f | quote: Missing key - Get your FREE key at https://cloud.maptiler.com/account/keys/
  - [9] 2026-11-02: the account-creation form of the sign-in script has a first and last name field | capture: sha256:b4dd6cacd88bba8011f6ffc0a3c70c356fa3ddd56eba94a478f2b5c2d2a34e30 | quote: <label class="mdl-textfield__label firebaseui-label" for="ui-sign-in-name-input">First &amp; last name</label><input type="text" name="name" id="ui-sign-in-name-input" autocomplete="name"
  - [9] 2026-11-02: the name field is required unless the page's email option sets requireDisplayName to false, which its options do not | capture: sha256:b4dd6cacd88bba8011f6ffc0a3c70c356fa3ddd56eba94a478f2b5c2d2a34e30 | quote: function qa(e){return!(e=Ra(e,t.Z.auth.EmailAuthProvider.PROVIDER_ID))||void 0===e.requireDisplayName||!!e.requireDisplayName}
  - [9] 2026-11-02: the account form reads email, name and password, and stops at an empty name | capture: sha256:b4dd6cacd88bba8011f6ffc0a3c70c356fa3ddd56eba94a478f2b5c2d2a34e30 | quote: var i=qa(jf(e)),r=n.j(),o=null;i&&(o=n.M());var a=n.P();if(r){if(i){if(!o)return void n.u().focus();
  - [9] 2026-11-02: the account-creation form has a Choose password field | capture: sha256:b4dd6cacd88bba8011f6ffc0a3c70c356fa3ddd56eba94a478f2b5c2d2a34e30 | quote: e+"Choose password",hn(e+'</label><input type="password" name="newPassword" id="ui-sign-in-new-password-input" autocomplete="new-password"
  - [9] 2026-11-02: sign-in proceeds only for a verified email; an unverified one is sent a verification message instead | capture: sha256:b4dd6cacd88bba8011f6ffc0a3c70c356fa3ddd56eba94a478f2b5c2d2a34e30 | quote: return n.emailVerified?this.signIn(n,e):this.sendEmailVerification(n)
  - [9] 2026-11-02: the widget tells an unverified email to open the emailed verification link | capture: sha256:b4dd6cacd88bba8011f6ffc0a3c70c356fa3ddd56eba94a478f2b5c2d2a34e30 | quote: Your email address has not been verified yet.
  - [7] 2026-11-02: the sign-up widget offers email and password, or Google, and sets no requireDisplayName option | capture: sha256:b6a2e4b2cf1bdc9236b8db58b0ed0aae5ad80cfbf7354b2ff276396af676319a | quote: "signInOptions": [{"provider": "password"}, {"provider": "google.com"}]
  - [2] 2026-11-02: a batch geocoding call takes at most 50 queries | capture: sha256:61fbf5c45fb8f5e3fe1ca639af8cf037c244c57f799576dc9c902f4fa83894f5 | quote: Each query may be forward, reverse or by feature ID. Maximum of 50 queries are supported.
  - [6] 2026-11-02: the Cloud terms defer the Free plan limits to the pricing page, which lists monthly quotas only | capture: sha256:58eff6a6fa0cdde5d3b37e206f836b62b308db174ef08a4eef4525356354dcba | quote: Details on the limitations to the Free Plan are specified at https://www.maptiler.com/cloud/pricing/.
  - [5] 2026-11-02: a batch geocoding call separates its queries with semicolons | capture: sha256:1ba112d8ae155d3324125ebd52aa1b3c4a419f1fbb9dc787574232c7096fc313 | quote: Just make sure you use semicolons `;` to separate individual requests when sending multiple requests at once.
  - [10] 2026-11-02: each query inside a batch call counts as one request | capture: sha256:b8707fa71f5882885dcdd4373089ef392ff75895f3cdf35fb095edef2f4477c3 | quote: For example, a batch of 20 queries counts as 20 requests, even though it’s technically one API call.
  - [1] 2026-11-02: the Free plan needs no credit card | capture: sha256:f83ae2598712f8cdc6b50ac88c4688c670a100a5936dbffd7e34717c414c3398 | quote: No credit card needed
- sources:
  - [1] https://www.maptiler.com/cloud/pricing/
  - [2] https://docs.maptiler.com/cloud/api/geocoding/
  - [3] https://www.maptiler.com/search/
  - [4] https://docs.maptiler.com/guides/maps-apis/maps-platform/tile-requests-and-map-sessions-compared/
  - [5] https://docs.maptiler.com/guides/geocoding/batch-geocoding-api/
  - [6] https://www.maptiler.com/terms/cloud/
  - [7] https://cloud.maptiler.com/auth/widget?mode=signup
  - [8] https://www.maptiler.com/data/pricing/
  - [9] https://cloud.maptiler.com/static/js/auth.js?t=1793082545
  - [10] https://docs.maptiler.com/guides/account/sessions-vs-requests/
