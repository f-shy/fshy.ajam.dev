# Hirak IP to Country

> hirak.site | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hirak/ | JSON https://fshy.ajam.dev/api/v1/entity/hirak.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hirak IP to Country

- `data-apis/hirak-ip-to-country` | dead | evidence measured | binding none | category IP geolocation API | tier Trial
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://iplocation.hirak.site/
- free tier: none: iplocation.hirak.site now redirects (HTTP 302) to the parking host ww547.hirak.site, which answers HTTP 401; the archived page of 2022-06-11 listed a Trial plan of 50 requests a month and calls without a token stopped at 10 requests | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: the archived page also listed paid plans: Basic 225K requests a month for 1 USD, Mega 500K for 2 USD and Yota 1M for 5 USD.
- per-object cap: not applicable: the API is gone | source: [1]
- retention: not applicable: the API is gone | source: [1]
- egress: not applicable: the API is gone | metered: no | source: [1]
- identity: anonymous | detail: the archived page says no sign up was required to choose a plan; calls carry a token parameter
- interface: rest
- binding note: the host no longer serves the API.
- interface detail: former form GET https://iplocation.hirak.site/?ip={ip}&token={token} (archived 2022-06-11); the host now redirects to a parking host
- endpoint: part of interface detail
- tooling: none that works
- composes with: No working route: any free or paid IP geolocation API of this topic replaces it. Bulk path: none.
- reliability: iplocation.hirak.site answered an HTTP 302 redirect to the parking host ww547.hirak.site, which answered HTTP 401, on 2026-11-02
- notes: Free requests: none; the former Trial of 50 requests a month is gone with the host. Rate limit: not applicable. Bulk path: none.
- evidence note: The redirect of the host was probed on 2026-11-02 and the archived page of 2022-06-11 was read; the plan figures are from the archived page.
- extras:
  - bulk_path: none
  - free_requests: none
- evidence:
  - [1] 2026-11-02: the archived request form is a GET with an ip and a token parameter | capture: sha256:baa6b582eb5bde3c8edbcf3243af5497bda2103f51fe978d157e1e4c6065a4c6 | quote: Perform simple GET request to https://iplocation.hirak.site/?ip=THE-IP-ADDRESS&token=YOUR-TOKEN, you recieve result as shown on the top.
  - [1] 2026-11-02: calls without a token stopped at 10 requests | capture: sha256:baa6b582eb5bde3c8edbcf3243af5497bda2103f51fe978d157e1e4c6065a4c6 | quote: please note requests without token stop on 10 requests
  - [1] 2026-11-02: the archived page said no sign up was required to choose a plan | capture: sha256:baa6b582eb5bde3c8edbcf3243af5497bda2103f51fe978d157e1e4c6065a4c6 | quote: We've awesome various plans with instant access, no sign up required, choose the sweetable plan that satisfy your needs, moneyback garanteed
  - [1] 2026-11-02: the archived Trial plan was 50 requests a month and free | capture: sha256:baa6b582eb5bde3c8edbcf3243af5497bda2103f51fe978d157e1e4c6065a4c6 | quote: #### Trial 50 req/month FREE
  - [1] 2026-11-02: the archived Basic plan was 225K requests a month for 1 USD | capture: sha256:baa6b582eb5bde3c8edbcf3243af5497bda2103f51fe978d157e1e4c6065a4c6 | quote: #### Basic 225K req/month 1$
  - probe:https://iplocation.hirak.site/ 2026-11-02: the host answered an HTTP 302 redirect | capture: sha256:8c73f39c207e52bc529fa982180185fb5897e970f1a13675d42e14824543740b | quote: "status": 302,
  - probe:https://iplocation.hirak.site/ 2026-11-02: the redirect target is a parking host | capture: sha256:8c73f39c207e52bc529fa982180185fb5897e970f1a13675d42e14824543740b | quote: "location": "http://ww547.hirak.site/?tkn=19vnMT3S",
  - probe:https://iplocation.hirak.site/ 2026-11-02: the parking host answered HTTP 401 | capture: sha256:8c73f39c207e52bc529fa982180185fb5897e970f1a13675d42e14824543740b | quote: "status": 401,
- sources:
  - [1] https://web.archive.org/web/20220611011308/https://iplocation.hirak.site/
