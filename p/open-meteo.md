# Open-Meteo

> open-meteo.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/open-meteo/ | JSON https://fshy.ajam.dev/api/v1/entity/open-meteo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Open-Meteo

- `data-apis/open-meteo` | qualifies | evidence measured | binding request-rate | category weather API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T10:04:05.824Z (live) | stale on 2026-12-31
- url https://open-meteo.com/en/pricing
- free tier: Free API with no key: 600 calls a minute, 5,000 an hour, 10,000 a day and 300,000 a month, covering the forecast, air quality, elevation, flood, geocoding and marine APIs and the historical weather (ERA5 from 1940), historical forecast, climate, ensemble, seasonal and satellite radiation APIs. | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: A request over 10 weather variables or over 2 weeks of data for one location counts as more than one call, in fractions (15 variables over 2 weeks count as 1.5 calls). Bulk path: the AWS open-data bucket s3://openmeteo in us-west-2 holds the model archives as .om files and listed with no credentials.
- per-object cap: not applicable
- retention: not applicable: the unit is a request | source: [1]
- egress: not applicable: JSON answers counted as calls; the s3://openmeteo bucket listed with no credentials, and its transfer price was not read | metered: no | source: [2]
- identity: anonymous | detail: No API key, no sign-up and no credit card. GET requests with no credentials answered HTTP 200 from the forecast and archive endpoints, and the s3://openmeteo bucket listed with no credentials.
- interface: rest, s3
- limits:
  - request-rate (binding): 600 calls a minute [1]
  - request-rate (binding): 5,000 calls an hour [1]
  - request-rate (binding): 10,000 calls a day [1]
  - request-rate (binding): 300,000 calls a month [1]
  - per-ip-shaping: limits counted per IP address and application; callers on a shared egress can be limited earlier [3]
- binding note: 10,000 calls a day binds a steady poller: 600 a minute reaches the 5,000 hourly cap in under 9 minutes, 5,000 an hour reaches 10,000 in 2 hours, and 10,000 a day over 30 days equals the 300,000 monthly cap.
- interface detail: REST over HTTPS GET with query parameters, JSON answers and no key; the archive at archive-api.open-meteo.com; the bulk archive in the public AWS bucket s3://openmeteo (us-west-2) as .om files
- endpoint: https://api.open-meteo.com/v1/forecast
- tooling: any HTTP client; any S3 client reads the bucket anonymously, and .om files are read with the Open-Meteo OM-file readers for Python, Rust, Swift and TypeScript. Last resort: the user installs and runs the open-source AGPLv3 server on a rented or free machine.
- composes with: A keyless point-weather and reanalysis source: forecasts and ERA5 history per coordinate under a 10,000-call daily cap, with the full model archive in a public S3 bucket for bulk pulls.
- reliability: Applications and IP addresses can be blocked without prior notice; the free API carries no uptime target.
- notes: Bulk path: s3://openmeteo, read anonymously. Paid plans move the same API to customer-api.open-meteo.com with a key.
- evidence note: Limits and licence are read from first-party pages; the forecast and archive endpoints answered HTTP 200 with JSON to calls with no key, and an anonymous ListObjectsV2 on s3://openmeteo answered HTTP 200. The 10,000-a-day ceiling was not driven to its limit.
- evidence:
  - [1] 2026-10-31: the free tier allows 600 calls a minute | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: | Minutely Limit | ⚠️ 600 calls / min | ✅ Unlimited | ✅ Unlimited | ✅ Unlimited |
  - [1] 2026-10-31: the free tier allows 5,000 calls an hour | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: | Hourly Limit | ⚠️ 5.000 calls / hour | ✅ Unlimited | ✅ Unlimited | ✅ Unlimited |
  - [1] 2026-10-31: the free tier allows 10,000 calls a day | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: | Daily Limit | ⚠️ 10.000 calls / day | ✅ Unlimited | ✅ Unlimited | ✅ Unlimited |
  - [1] 2026-10-31: the free tier allows 300,000 calls a month | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: | Monthly Limit | ⚠️ 300.000 calls / month | ⚠️ 1M calls / month | ⚠️ 5M calls / month | ✅ >50M calls / month |
  - [1] 2026-10-31: the free tier includes the historical, climate, ensemble, seasonal and satellite radiation APIs | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: | Satellite Radiation API Climate API Seasonal Forecast API Ensemble Weather API Historical Weather API Historical Forecast API Previous Model Runs API Single Runs API | ✅ | ❌ | ✅ | ✅ |
  - [1] 2026-10-31: the free tier includes the forecast, air quality, elevation, flood, geocoding and marine APIs | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: | Weather Forecast APIs Air Quality API Elevation API Flood API Geocoding API Marine API | ✅ | ✅ | ✅ | ✅ |
  - [1] 2026-10-31: large requests count as more than one call | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: Requests for data covering more than 10 weather variables or extending over a period of more than 2 weeks for a single location are considered multiple API calls.
  - [1] 2026-10-31: the free API carries no uptime guarantee | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: The free API is rate-limited to 10,000 calls/day, and carries no uptime guarantee.
  - [1] 2026-10-31: paid plans use customer-api.open-meteo.com with a key | capture: sha256:6029e5824125c5f36caafbf8e9c48a01755eecf68a1cfd28396a9196bf145e45 | quote: The customer endpoint is customer-api.open-meteo.com; requests include &apikey=abc123.
  - [3] 2026-10-31: callers on a shared egress can be limited earlier | capture: sha256:5ab31b7b2b04aa75d440f81a36dfc0bb74f81662052e12830a4fef7df89bcfc7 | quote: If you are using providers like Vercel, Netlify, Render, or Google Sheets you might be rate-limited earlier then expected.
  - [4] 2026-10-31: displayed data carries a link to Open-Meteo | capture: sha256:201d70de1c1ffc91a548d79d687afaa14b817cb7ef6083e54e5374db3cb3273b | quote: You must include a link next to any location Open-Meteo data are displayed, for example:
  - [3] 2026-10-31: the limits are counted per IP address and application | capture: sha256:5ab31b7b2b04aa75d440f81a36dfc0bb74f81662052e12830a4fef7df89bcfc7 | quote: Rate limits are applied by IP addresses and application.
  - [3] 2026-10-31: applications and IP addresses can be blocked without notice | capture: sha256:5ab31b7b2b04aa75d440f81a36dfc0bb74f81662052e12830a4fef7df89bcfc7
  - [5] 2026-10-31: the free API needs no key, no account and no card | capture: sha256:94ac6220e7a96f239bcea9a63377975704a2b7311634fcb76861bc1c2d8daaa4 | quote: No API key, no sign-up, no credit card.
  - [5] 2026-10-31:  | capture: sha256:94ac6220e7a96f239bcea9a63377975704a2b7311634fcb76861bc1c2d8daaa4
  - [6] 2026-10-31: the historical weather API serves ERA5 hourly from 1940 with a 5-day delay | capture: sha256:d032e0fd4fd731dc23be87df16b76583b29994eb0a7f090928751d8375f91e79 | quote: | [ERA5](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | 🌍 Global | 0.25° (~25 km) | Hourly | 1940 to present | Daily with 5 days delay |
  - [2] 2026-10-31: the bulk archive is the AWS bucket s3://openmeteo in us-west-2 | capture: sha256:7737e07690ef0b315157cbc679cccca1c82c7ab8c804651feaa848634a2aece5 | quote: **AWS Bucket Name and Region: [s3://openmeteo](https://openmeteo.s3.amazonaws.com/index.html#data/); us-west-2; [AWS Registry](https://registry.opendata.aws/open-meteo/)**
  - [2] 2026-10-31: the .om files have readers for Python, Rust, Swift and TypeScript | capture: sha256:7737e07690ef0b315157cbc679cccca1c82c7ab8c804651feaa848634a2aece5 | quote: OM-Files can also be read from [Python](https://github.com/open-meteo/python-omfiles), [Rust](https://github.com/open-meteo/rust-omfiles), [Swift](https://github.com/open-meteo/om-file-format/tree/main/Swift), and [TypeScript WASM](https://github.com/open-meteo/typescript-omfiles).
  - [4] 2026-10-31: the server is open source under AGPLv3 | capture: sha256:201d70de1c1ffc91a548d79d687afaa14b817cb7ef6083e54e5374db3cb3273b | quote: Source code is available on [GitHub](https://github.com/open-meteo/open-meteo) under the GNU Affero General Public Licence Version 3 AGPLv3 or any later version.
  - probe:https://api.open-meteo.com/v1/forecast 2026-10-31: a forecast call with no key answered HTTP 200 with current conditions in JSON | capture: sha256:868d3285ead7dfa2e4cbe9fa06b48cdb6fbe534b89fb335d5c8a1e7f237138bd | quote: "current":{"time":"2026-10-31T06:30","interval":900,"temperature_2m":9.2}
  - probe:https://archive-api.open-meteo.com/v1/archive 2026-10-31: an archive call with no key answered HTTP 200 with hourly ERA5 values for 2024-01-01 and 2024-01-02 | capture: sha256:e303f1077c07e0dc15395ff7cee065971c4b8107ca34c34e1f2f918baf678cce | quote: "hourly":{"time":["2024-01-01T00:00","2024-01-01T01:00"
  - probe:https://openmeteo.s3.amazonaws.com/ 2026-10-31: an anonymous ListObjectsV2 on the bucket answered HTTP 200 with its model prefixes | capture: sha256:637e5e576076199dda8da9175c31ea80be1664c91f1816d66728f2e61b706177 | quote: <Name>openmeteo</Name><Prefix>data/</Prefix>
  - probe:https://openmeteo.s3.amazonaws.com/ 2026-10-31: the bucket holds the ERA5 archive under data/copernicus_era5/ | capture: sha256:637e5e576076199dda8da9175c31ea80be1664c91f1816d66728f2e61b706177 | quote: <CommonPrefixes><Prefix>data/copernicus_era5/</Prefix></CommonPrefixes>
  - [7] 2026-10-31: listed under Weather in the public-apis list with no auth | capture: sha256:7c0d65a75227ba9bd3f8576a39262f7af32373d3eca4190cd91e66329ca1d059 | quote: | [Open-Meteo](https://open-meteo.com/) | Global weather forecast API | No | Yes | Yes |
- sources:
  - [1] https://open-meteo.com/en/pricing
  - [2] https://github.com/open-meteo/open-data
  - [3] https://open-meteo.com/en/terms
  - [4] https://open-meteo.com/en/licence
  - [5] https://open-meteo.com/
  - [6] https://open-meteo.com/en/docs/historical-weather-api
  - [7] https://raw.githubusercontent.com/public-apis/public-apis/master/README.md
