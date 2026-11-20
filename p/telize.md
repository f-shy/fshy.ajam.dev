# Telize

> telize.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/telize/ | JSON https://fshy.ajam.dev/api/v1/entity/telize.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Telize

- `data-apis/telize` | paid-only | evidence documented | binding volume-quota | category IP geolocation API | tier Basic
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://www.telize.com/
- free tier: none: the public API was permanently shut down on November 15, 2015; the hosted API is sold on RapidAPI from the Basic plan at USD 7.00 a month for 1,000 requests a day | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: Pro is USD 22.00 a month for 5,000 requests a day, Ultra USD 50.00 for 20,000 and Mega USD 100.00 for 100,000; each plan adds a per-request price past its daily count and a bandwidth fee past 10240 MB a month.
- per-object cap: one IP address per request (Location with specific IP) | source: [2]
- retention: not applicable: a lookup API | source: [1]
- egress: RapidAPI plans include a bandwidth allowance of 10240 MB a month, then USD 0.001 per 1 MB | metered: yes | free allowance: 10240 MB a month on every paid plan | source: [3]
- identity: card | detail: a RapidAPI account and a paid subscription; the payment form of RapidAPI was not read
- interface: rest
- limits:
  - volume-quota (binding): Basic: 1,000 requests a day, then USD 0.0005 a request; Pro 5,000, Ultra 20,000, Mega 100,000 a day [3]
- binding note: there is no free allowance; the lowest paid plan counts 1,000 requests a day.
- interface detail: RapidAPI endpoints Legacy - GeoIP, JSON IP, IP, Location and Location with specific IP; the project site documents /ip, /jsonip and /geoip/{ip} with JSON and JSONP answers
- endpoint: https://rapidapi.com/fcambus/api/telize
- tooling: any HTTP client through a RapidAPI subscription; the open-source Go server over MaxMind GeoLite2 databases is the last resort, which the user installs and runs on a rented or free machine
- composes with: No free hosted route exists. Hosted first: the paid RapidAPI plans from USD 7.00 a month, or any free keyless or free-key API of this topic. Last resort: the open-source server. Bulk path: none.
- reliability: the public API has been shut down since 2015-11-15; the project site still serves its documentation, and the hosted API is reached only through paid RapidAPI plans
- notes: Free requests: none; Basic is USD 7.00 a month for 1,000 requests a day on RapidAPI. Rate limit: the plan's daily count. Bulk path: none. Self-hosted last resort: the open-source Go server over MaxMind GeoLite2 data.
- evidence note: The project site, the RapidAPI listing and pricing page and the repository README were quoted on 2026-11-02; no paid subscription was made and the RapidAPI payment step was not read.
- self hosted: no
- extras:
  - bulk_path: none
  - free_requests: none
- evidence:
  - [1] 2026-11-02: the public API was shut down on 2015-11-15 | capture: sha256:0d171273ec828c72d4c604e9820302624def876faa6df6459292db6be5f41ef9 | quote: The public API was permanently shut down on November 15, 2015.
  - [1] 2026-11-02: continued use needs an own instance or a paid plan | capture: sha256:0d171273ec828c72d4c604e9820302624def876faa6df6459292db6be5f41ef9 | quote: To continue using Telize after this date, please spin up your own instance or subscribe to a [paid plan](https://rapidapi.com/fcambus/api/telize).
  - [3] 2026-11-02: the Basic plan costs USD 7.00 a month | capture: sha256:02c05aa093a81ffe67e6d55fc0c1bf219e8a3c0ba960b06f456408f004fc0378 | quote: $7.00 /mo
  - [3] 2026-11-02: Basic allows 1,000 requests a day, then USD 0.0005 a request | capture: sha256:02c05aa093a81ffe67e6d55fc0c1bf219e8a3c0ba960b06f456408f004fc0378 | quote: 1,000 / Day + $0.0005
  - [3] 2026-11-02: Pro allows 5,000 requests a day | capture: sha256:02c05aa093a81ffe67e6d55fc0c1bf219e8a3c0ba960b06f456408f004fc0378 | quote: 5,000 / Day + $0.0002
  - [3] 2026-11-02: Ultra allows 20,000 requests a day | capture: sha256:02c05aa093a81ffe67e6d55fc0c1bf219e8a3c0ba960b06f456408f004fc0378 | quote: 20,000 / Day + $0.0001
  - [3] 2026-11-02: Mega allows 100,000 requests a day | capture: sha256:02c05aa093a81ffe67e6d55fc0c1bf219e8a3c0ba960b06f456408f004fc0378 | quote: 100,000 / Day + $0.00005
  - [3] 2026-11-02: a bandwidth allowance of 10240 MB a month, then USD 0.001 per 1 MB | capture: sha256:02c05aa093a81ffe67e6d55fc0c1bf219e8a3c0ba960b06f456408f004fc0378 | quote: 10240MB / Month + $0.001 per 1MB
  - [2] 2026-11-02: the RapidAPI listing offers sign in and sign up for subscribing | capture: sha256:3945efc4b522e54812e16a598bc98ce8923115713f377a57635df485ab6c8c2e | quote: Sign InSign Up
  - [2] 2026-11-02: Pro costs USD 22.00 a month | capture: sha256:3945efc4b522e54812e16a598bc98ce8923115713f377a57635df485ab6c8c2e | quote: $22.00 / mo
  - [2] 2026-11-02: Ultra costs USD 50.00 a month | capture: sha256:3945efc4b522e54812e16a598bc98ce8923115713f377a57635df485ab6c8c2e | quote: $50.00 / mo
  - [2] 2026-11-02: Mega costs USD 100.00 a month | capture: sha256:3945efc4b522e54812e16a598bc98ce8923115713f377a57635df485ab6c8c2e | quote: $100.00 / mo
  - [4] 2026-11-02: the open-source server is a Go REST API | capture: sha256:afcbe53f6147175b78c760a507ecfc83f13d35d9b8479612670af39d579348b9 | quote: Telize is a REST API built in Go allowing to get a visitor IP address and to query location information from any IP address.
  - [4] 2026-11-02: the server needs the free MaxMind GeoLite2 databases | capture: sha256:afcbe53f6147175b78c760a507ecfc83f13d35d9b8479612670af39d579348b9 | quote: Telize requires the free [GeoLite2 databases](https://dev.maxmind.com/geoip/geoip2/geolite2/) from MaxMind.
- sources:
  - [1] https://www.telize.com/
  - [2] https://rapidapi.com/fcambus/api/telize
  - [3] https://rapidapi.com/fcambus/api/telize/pricing
  - [4] https://github.com/fcambus/telize
