# Open Disease API

> disease.sh | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/disease/ | JSON https://fshy.ajam.dev/api/v1/entity/disease.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Open Disease API (disease.sh)

- `data-apis/disease-sh` | qualifies-with-caveat | evidence documented | binding none | category open disease statistics API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:45.809Z (live) | stale on 2026-12-03
- url https://disease.sh/
- free tier: Free to use, with no key and no request limit stated on the home page, the docs or the README: COVID-19 and influenza statistics as JSON. | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: A burst of 120 parallel keyless GETs all answered HTTP 200. The Worldometers totals update every 10 minutes.
- per-object cap: no cap stated; one GET of /v3/covid-19/historical?lastdays=all returned the whole JHU time series of every country and province in 13953048 bytes
- retention: the JHU time series runs from 1/22/20 to 3/9/23; the Worldometers totals are live, updated every 10 minutes | source: [2]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: No account and no key: the home page states that no signup is required, and keyless GETs answered HTTP 200.
- interface: rest
- limits:
  - request-rate: no limit stated; 120 parallel keyless GETs in one burst all answered HTTP 200, with no 429 probe:https://disease.sh/v3/covid-19/all
- binding note: No quota, key or rate limit is stated, and a 120-request parallel burst met no 429; what a reader meets instead is a feed that has stopped updating or fails.
- interface detail: HTTPS GET at disease.sh/v3/ with JSON answers, open to all origins (Access-Control-Allow-Origin: *); the OpenAPI 3.0.0 document is at disease.sh/apidocs/swagger_v3.json and the live reference at disease.sh/docs/
- endpoint: https://disease.sh/v3/covid-19/all
- tooling: any HTTP client. The last resort is self-hosted: the open-source API server, which the user installs and runs with Redis on a rented or free machine, started with docker-compose or npm.
- composes with: Free keyless epidemiology numbers for dashboards: live Worldometers totals by country and continent, with the JHU time series for history up to 3/9/23. Bulk path: GET /v3/covid-19/historical?lastdays=all returns the whole time series of every country and province in one JSON of 13953048 bytes; the JHU CSSE and NYT repositories that the README lists as sources are the public bulk data behind it. The last resort is self-hosted: the open-source server that the user installs and runs with Redis on a rented or free machine.
- reliability: On 2026-11-02 /v3/covid-19/jhucsse/counties answered HTTP 502 with Retry-After 60, and the JHU time series ends on 3/9/23; the live Worldometers totals answered 200 with JSON that carries an updated timestamp.
- notes: Caveat: the JHU time series ends 3/9/23 and /v3/covid-19/jhucsse/counties failed with HTTP 502 on 2026-11-02; the Worldometers totals are live. Free requests: no key, no stated limit. Bulk path: /v3/covid-19/historical?lastdays=all, one GET.
- evidence note: Free use and no sign-up are stated on the home page and in the site source; keyless GETs answered 200, one request returned the whole JHU series, and 120 parallel GETs met no 429. No rate limit is published, so the absence of one is read from that burst and not from a statement.
- self hosted: no
- evidence:
  - [1] 2026-11-02: the services are free to use | capture: sha256:9698e14dd289abb8cb07fc08ecbf174c888b1c1bc11111ab2a1fec8b36dcd6d8 | quote: Our services are free to use, and have a 100/100 page insight performance score.
  - [1] 2026-11-02: the API covers current global outbreaks, COVID-19 and influenza | capture: sha256:9698e14dd289abb8cb07fc08ecbf174c888b1c1bc11111ab2a1fec8b36dcd6d8 | quote: We provide data on current global outbreaks, including COVID-19 and Influenza.
  - [1] 2026-11-02: the served home page's own metadata says no signup is required | capture: sha256:8ee298a5fe3eceeed6aa761fe7f64e623be66e5031008372266fa33b51831a0f | quote: An open API for disease-related statistics. No signup required.
  - [3] 2026-11-02: the site source's page metadata says no signup is required | capture: sha256:5728d939bcc8c1658f1ead897f59f2daa802d6da917ba0b367766bd700b5e9ed | quote: An open API for disease-related statistics. No signup required.
  - probe:https://disease.sh/v3/covid-19/all 2026-11-02: a keyless GET of the global totals answered HTTP 200 | capture: sha256:0510d3339e2426cb9a718901e8246a1490a6b7d302dce15cd881e5b588041175 | quote: "status": 200
  - probe:https://disease.sh/v3/covid-19/all 2026-11-02: the answer allows cross-origin reads from any origin | capture: sha256:0510d3339e2426cb9a718901e8246a1490a6b7d302dce15cd881e5b588041175 | quote: "access-control-allow-origin": "*"
  - probe:https://disease.sh/v3/covid-19/all 2026-11-02: the body is JSON with an updated timestamp and the global totals | capture: sha256:2692cc5bc804be870a21384bf30353865d9127928bde5e45f767be950a3e2029 | quote: {"updated":1793615351436,"cases":704753890,
  - probe:https://disease.sh/v3/covid-19/all 2026-11-02: the burst was 120 parallel GETs | capture: sha256:b3f4b4b56828e3c64f94e9d8893a191f42b117bace74cea14dc0b540c123181c | quote: "concurrency": 120
  - probe:https://disease.sh/v3/covid-19/all 2026-11-02: the highest status of the 120 runs was 200, so none answered 429 | capture: sha256:b3f4b4b56828e3c64f94e9d8893a191f42b117bace74cea14dc0b540c123181c | quote: "status": 200
  - [2] 2026-11-02: the Worldometers COVID-19 totals update every 10 minutes | capture: sha256:bf9e9278948ad2a740d8204a32b5046d2e2e074fae0ed89261e355cfd0762f38 | quote: (COVID-19 data sourced from Worldometers, updated every 10 minutes)
  - [2] 2026-11-02: the JHUCSSE group, which holds the historical endpoints, is sourced from Johns Hopkins University | capture: sha256:bf9e9278948ad2a740d8204a32b5046d2e2e074fae0ed89261e355cfd0762f38 | quote: (COVID-19 data sourced from Johns Hopkins University, updated every 10 minutes)
  - [2] 2026-11-02: the /v3/covid-19/historical endpoint returns the time series of all countries and their provinces | capture: sha256:bf9e9278948ad2a740d8204a32b5046d2e2e074fae0ed89261e355cfd0762f38 | quote: Get COVID-19 time series data for all countries and their provinces
  - [4] 2026-11-02: the lastdays parameter takes all for the full data set | capture: sha256:65d0e7dfe742ebfe60304810a1dcf784919d262bbcacbc924959febab44c2c51 | quote: Number of days to return. Use 'all' for the full data set (e.g. 15, all, 24)
  - [4] 2026-11-02: the contract is an OpenAPI 3.0.0 document | capture: sha256:65d0e7dfe742ebfe60304810a1dcf784919d262bbcacbc924959febab44c2c51 | quote: "openapi": "3.0.0",
  - probe:https://disease.sh/v3/covid-19/historical?lastdays=all 2026-11-02: one GET with lastdays=all answered 200 with 13953048 bytes | capture: sha256:8c0badb7d1d7a145248cd78116e04dc6cefcbe422aa93b2b1f0947014dcb8aa0 | quote: "status": 200, "bytes": 13953048,
  - probe:https://disease.sh/v3/covid-19/historical/all?lastdays=all 2026-11-02: the global series starts on 1/22/20 | capture: sha256:449abb17ee9118c6f17a369abaa09b95eb14f3b99fc7291d2573158c1996b50a | quote: {"cases":{"1/22/20":557,"1/23/20":657
  - probe:https://disease.sh/v3/covid-19/historical/all?lastdays=all 2026-11-02: the global series ends on 3/9/23 | capture: sha256:449abb17ee9118c6f17a369abaa09b95eb14f3b99fc7291d2573158c1996b50a | quote: "3/9/23":676570149},"deaths":{"1/22/20":17
  - probe:https://disease.sh/v3/covid-19/jhucsse/counties 2026-11-02: the JHU counties endpoint answered HTTP 502 | capture: sha256:cdaff5c95a3158728756661254605643926750fdd380f949c9f9116e0976f573 | quote: "status": 502
  - probe:https://disease.sh/v3/covid-19/jhucsse/counties 2026-11-02: that answer carried Retry-After 60 | capture: sha256:cdaff5c95a3158728756661254605643926750fdd380f949c9f9116e0976f573 | quote: "retry-after": "60"
  - [5] 2026-11-02: the open-source server needs a Redis server started with redis-server | capture: sha256:c04f694aa4f122a0681d8fee347a6d9a30524c4b9719e9c6c42ab24ed4927496 | quote: 2. Start redis server using `redis-server`
  - [5] 2026-11-02: the README has a docker-compose install path for the open-source server | capture: sha256:c04f694aa4f122a0681d8fee347a6d9a30524c4b9719e9c6c42ab24ed4927496 | quote: ## With docker-compose
  - [5] 2026-11-02: the open-source server also runs with docker-compose | capture: sha256:c04f694aa4f122a0681d8fee347a6d9a30524c4b9719e9c6c42ab24ed4927496 | quote: 5. Run `npm run docker-start` to run the published version of the API with Docker
  - [5] 2026-11-02: the README lists the JHU CSSE time series repository as a source | capture: sha256:c04f694aa4f122a0681d8fee347a6d9a30524c4b9719e9c6c42ab24ed4927496 | quote: > https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
  - [5] 2026-11-02: the README lists the NYT COVID-19 data repository as a source | capture: sha256:c04f694aa4f122a0681d8fee347a6d9a30524c4b9719e9c6c42ab24ed4927496 | quote: > https://github.com/nytimes/covid-19-data
  - [6] 2026-11-02: the server source sets CORS open to every origin | capture: sha256:48dd9efd20d6daa194f76b1f6915b36d929a7fcc546f35f778c8e207f5b694a6 | quote: app.use(require('cors')({ origin: '*' }));
- sources:
  - [1] https://disease.sh/
  - [2] https://disease.sh/docs/
  - [3] https://github.com/disease-sh/API/blob/master/public/index.ejs
  - [4] https://disease.sh/apidocs/swagger_v3.json
  - [5] https://raw.githubusercontent.com/disease-sh/API/master/README.md
  - [6] https://raw.githubusercontent.com/disease-sh/API/master/server.js
