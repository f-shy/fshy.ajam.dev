# IP 2 Country

> ip2country.info | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip2country/ | JSON https://fshy.ajam.dev/api/v1/entity/ip2country.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IP 2 Country (ip2country.info)

- `data-apis/ip2country-info` | dead | evidence measured | binding none | category IP to country API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://ip2country.info/
- free tier: none: every path tried on the documented API host api.ip2country.info answers HTTP 400 Invalid URL, and the home page sends visitors to ipapi.com for a free API key | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: the free key the home page points to is the ipapi.com Free plan, which has its own record.
- per-object cap: not applicable: the API does not answer | source: [1]
- retention: not applicable: the API does not answer | source: [1]
- egress: not applicable: the API does not answer | metered: no | source: [1]
- identity: email | detail: the home page now directs to an ipapi.com account for a free key; the former keyless form no longer answers
- interface: rest
- binding note: the documented API host does not answer, so no limit can be reached.
- interface detail: documented form GET https://api.ip2country.info/ip?{ip}; the host answers HTTP 400 Invalid URL (an error reference page) for that form, for /ip?ip={ip}, for /ip and for /
- endpoint: part of interface detail
- tooling: none that works; the home page names an npm package and a messenger bot
- composes with: No working route: the home page directs callers to a free ipapi.com key, which has its own record. Bulk path: none.
- reliability: api.ip2country.info answered HTTP 400 Invalid URL for every path tried on 2026-11-02, and ip2country.info/ip answered HTTP 404
- notes: Free requests: none; the API host does not answer. Rate limit: not applicable. Bulk path: none. The home page names the successor offer: a free key at ipapi.com.
- evidence note: Four paths of the API host were probed on 2026-11-02 and each answered HTTP 400; the home page was quoted. The former free quota and rate were never published on a page that could be read, so they are unverified.
- extras:
  - bulk_path: none
  - free_requests: none
- evidence:
  - [1] 2026-11-02: the home page directs callers to a free ipapi.com key | capture: sha256:4db0ddac4be77910093495e44a7befaf6bbbe3ec5613d32993a6296ffd270193 | quote: Get a FREE API key at [ipapi.com](https://ipapi.com/)
  - [1] 2026-11-02: the documented request form is GET https://api.ip2country.info/ip?{ip} | capture: sha256:4db0ddac4be77910093495e44a7befaf6bbbe3ec5613d32993a6296ffd270193 | quote: | GET HEAD | `https://api.ip2country.info/ip?5.6.7.8` |
  - probe:https://api.ip2country.info/ip?8.8.8.8 2026-11-02: the documented request form answered HTTP 400 | capture: sha256:25ffc9ad1a74970b0ead5cd98627c9ed43a472d7c56785916c19b8a0d98a4eab | quote: "status": 400
  - probe:https://api.ip2country.info/ip?8.8.8.8 2026-11-02: the answer is an Invalid URL error page | capture: sha256:a8c36b58618b5044193fcad8d9065dcb171f9155ceda782d0b75a2f5634fc23b | quote: <TITLE>Invalid URL</TITLE>
  - probe:https://api.ip2country.info/ip?ip=8.8.8.8 2026-11-02: the form with an ip parameter answered HTTP 400 | capture: sha256:46d77486df2b4a4b00d1606d04387b6f1a6cfe4e1bf7e073714318a983c362bb | quote: "status": 400
  - probe:https://api.ip2country.info/ 2026-11-02: the API host root answered HTTP 400 | capture: sha256:3b79514c63ab2177fe62744d1dbbf8fbaa422cfd4d02e454e885c9426dafaae3 | quote: "status": 400
  - probe:https://ip2country.info/ip?8.8.8.8 2026-11-02: the main host answers HTTP 404 for /ip | capture: sha256:a61751ff7bfd5a4fec3dcc1a1ae3badb2a591f9dac84797aa9aca53db3c92f76 | quote: "status": 404
- sources:
  - [1] https://ip2country.info/
