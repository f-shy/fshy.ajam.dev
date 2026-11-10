# NASA POWER

> power.larc.nasa.gov | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/power-larc-nasa-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/power-larc-nasa-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NASA POWER

- `data-apis/nasa-power` | qualifies | evidence measured | binding per-object-cap | category weather and solar data API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:48.564Z (live) | stale on 2027-01-02
- url https://power.larc.nasa.gov/docs/services/
- free tier: Free, keyless REST API for global solar and meteorological data (hourly, daily, monthly and climatology levels; daily series from 1981); no numeric request quota is published, the vendor says there is no set rate limit and usage is monitored. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: A single point takes up to 20 parameters on the daily API and 15 on the hourly API; regional requests take one parameter. Bulk path: the complete datastore is in public S3 buckets (s3://nasa-power as Zarr, s3://power-datastore as NetCDF, us-west-2), read with no AWS account, which bypasses the API's rate, transfer and timeout limits. Recent meteorological values are replaced by climate-quality values within 2 to 3 months.
- per-object cap: 20 parameters per single-point request on the daily API, 15 on the hourly API, 1 per regional request | source: [2]
- retention: not applicable: the unit is a request | source: [1]
- egress: JSON, CSV, NetCDF and ASCII answers; the S3 buckets are free of charge to everyone | metered: no | source: [1]
- identity: anonymous | detail: No sign-up and no key: keyless API calls and anonymous bucket listings answered HTTP 200; the AWS registry page says no AWS account is required.
- interface: rest, s3
- limits:
  - request-rate: unverified: no numeric limit is published; the vendor says there is no set rate limit and usage is limited to support equitable access [3]
  - per-object-cap (binding): 20 parameters per single-point request on the daily API, 15 on the hourly API, 1 per regional request [2]
- binding note: No request rate is published, so the parameter cap per request is the number that shapes a large pull; the S3 buckets have no such cap.
- interface detail: REST over HTTPS GET at power.larc.nasa.gov/api/temporal/{daily,hourly,monthly,climatology}/{point,regional}, with OpenAPI pages; Zarr and NetCDF files in anonymous S3 buckets
- endpoint: https://power.larc.nasa.gov/api/temporal/daily/point
- tooling: any HTTP client; any S3 client reads the buckets with no signing; Python tutorials for Zarr access are published by the project
- composes with: A keyless solar and reanalysis-based weather source for coordinates worldwide; use the S3 Zarr store for bulk pulls instead of looping the API.
- reliability: Repeating the same location or flooding with synchronous requests can get an application blocked; overload answers HTTP 429.
- notes: Bulk path: s3://nasa-power (Zarr analysis-ready store) and s3://power-datastore (NetCDF).
- evidence note: A keyless daily point call and an anonymous bucket listing were made and kept; the rate limit is not published and was not driven.
- evidence:
  - [2] 2026-11-02: daily API caps parameters per request | capture: sha256:fb93f9121ae86328de6ce803fb8160c9ca5f6fdcfb0f2ad802badc8ceceeaa5e | quote: A maximum of 20 parameters can currently be requested in one submission for a single point. Regional requests are limited to one parameter.
  - [4] 2026-11-02: hourly API caps parameters per request | capture: sha256:f6389097b6aac2c6b5b0bd9b41cc611d6f62de94607ea8e7c3f9d7089d62c13f | quote: A maximum of 15 parameters can currently be requested in one submission.
  - [2] 2026-11-02: repeating a location can get an application blocked | capture: sha256:fb93f9121ae86328de6ce803fb8160c9ca5f6fdcfb0f2ad802badc8ceceeaa5e | quote: If your application persists in requesting the same relative location, it will potentially be blocked.
  - [5] 2026-11-02: too many synchronous requests can be blocked | capture: sha256:a89f073b0e913664f1acf2b5bbebe9cde1d844e723d41662cb4ea04886b9b8cb | quote: If the server determines that you are negatively impacting performance, it may block your access.
  - [6] 2026-11-02: the API answers 429 when overloaded | capture: sha256:e3c65a4f8670b8969860e241c724948e809d2741461bcef5acc0d978299e7778 | quote: | 429 | Too Many Requests | Too Many Requests. |
  - [3] 2026-11-02: no set rate limit; usage is monitored and limited for equitable access (answer of 2023-05-22) | capture: sha256:272181478c1047e24e4ae765f50029b45e166525920e31410869772895a72918 | quote: The Subject Matter Expert from the NASA POWER Team responded and said there is no set rate limit. However, the NASA POWER Team monitors the usage and will limit usage to support equitable access.
  - [7] 2026-11-02: a 2021 reply of the POWER team, relayed by a third party, gave 30 requests a minute on the climatology endpoint | capture: sha256:2eaf2d2ecfde90e600f32de1821cc85f86561991e68a7c35fb0a708b099fd40b | quote: The POWER API has a limit of 30 request per minute on the climatology endpoint.
  - [1] 2026-11-02: the API has rate, transfer and timeout limits | capture: sha256:fda6e3ba91aa537945a47de2f11227920fab9a7c667440097fa72a90e2b4daff | quote: However, this service has rate, data transfer, and timeout limits due to a balance of user-experience optimization and cost-saving measures.
  - [1] 2026-11-02: the S3 buckets bypass the API limits | capture: sha256:fda6e3ba91aa537945a47de2f11227920fab9a7c667440097fa72a90e2b4daff | quote: By connecting directly to data in AWS, users can bypass service limitations.
  - [1] 2026-11-02: the AWS datastore is free to everyone | capture: sha256:fda6e3ba91aa537945a47de2f11227920fab9a7c667440097fa72a90e2b4daff | quote: is accessible free of charge to everyone.
  - [8] 2026-11-02: the buckets are read with no AWS account | capture: sha256:4d6a30f5764e9a6b965299ed461a07adefe1fae9f1ba39c8d4cb6f34bc228bd9 | quote: Access (No AWS account required)
  - [8] 2026-11-02: anonymous listing of the Zarr bucket | capture: sha256:4d6a30f5764e9a6b965299ed461a07adefe1fae9f1ba39c8d4cb6f34bc228bd9 | quote: aws s3 ls --no-sign-request s3://nasa-power/
  - [8] 2026-11-02: no restriction on access or download | capture: sha256:4d6a30f5764e9a6b965299ed461a07adefe1fae9f1ba39c8d4cb6f34bc228bd9 | quote: There are no restrictions on the use, access, and/or download of data from the NASA POWER Project.
  - [8] 2026-11-02: daily history from 1981 | capture: sha256:4d6a30f5764e9a6b965299ed461a07adefe1fae9f1ba39c8d4cb6f34bc228bd9 | quote: The daily time series for meteorology is available from 1981, while solar-based parameters start in 1984.
  - [8] 2026-11-02: near-real-time lag | capture: sha256:4d6a30f5764e9a6b965299ed461a07adefe1fae9f1ba39c8d4cb6f34bc228bd9 | quote: The data is updated nightly to maintain near real time availability (2-3 days for meteorological parameters and 5-7 days for solar).
  - probe:https://power.larc.nasa.gov/api/temporal/daily/point 2026-11-02: a daily point call with no key and no sign-up answered daily T2M values | capture: sha256:b626c523262b04330c8b546d411925e7b5aa581e48a0ff0bcaddb93fb685b1e8 | quote: "parameter":{"T2M":{"20240101":10.67,"20240102":11.08,"20240103":9.93}}
  - probe:https://power.larc.nasa.gov/api/temporal/daily/point 2026-11-02: the call answered HTTP 200 | capture: sha256:62842280fa3f6872009a3cc0cd499e1a45363bf4a942813abecd8f645d733b4c | quote: "status": 200
  - probe:https://nasa-power.s3.us-west-2.amazonaws.com/ 2026-11-02: an anonymous ListObjectsV2 on s3://nasa-power listed the MERRA-2 prefix | capture: sha256:1d1ebc4bd22be124d45ac0d1c6809d095409c5a3b6191143b961e0b7e546b659 | quote: <CommonPrefixes><Prefix>merra2/</Prefix></CommonPrefixes>
  - probe:https://nasa-power.s3.us-west-2.amazonaws.com/ 2026-11-02: the anonymous bucket listing answered HTTP 200 | capture: sha256:1c23e459d75e1a5b60ef4c0cdcd7315512d6f205404f6182de910eed78f58590 | quote: "status": 200
  - [9] 2026-11-02: listed under Weather in public-apis with no auth | capture: sha256:1ce4b056b48404fe8a332497495ca5d12ca2b9f5aa4e985e8fd5fb14f90fe164 | quote: | [NASA POWER](https://power.larc.nasa.gov/docs/) | Global solar and weather data for energy and agriculture | No | Yes | Yes |
- sources:
  - [1] https://power.larc.nasa.gov/docs/services/aws/
  - [2] https://power.larc.nasa.gov/docs/services/api/temporal/daily/
  - [3] https://forum.earthdata.nasa.gov/viewtopic.php?t=4273
  - [4] https://power.larc.nasa.gov/docs/services/api/temporal/hourly/
  - [5] https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/
  - [6] https://power.larc.nasa.gov/docs/services/api/
  - [7] https://github.com/ropensci/nasapower/issues/57
  - [8] https://registry.opendata.aws/nasa-power/
  - [9] https://raw.githubusercontent.com/public-apis/public-apis/master/README.md
