# Meteostat

> meteostat.net | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/meteostat/ | JSON https://fshy.ajam.dev/api/v1/entity/meteostat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Meteostat

- `data-apis/meteostat` | qualifies | evidence measured | binding none | category weather data dumps | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:38:41.081Z (live) | stale on 2027-01-03
- url https://dev.meteostat.net/data
- free tier: Bulk Parquet files across all weather stations (hourly and daily as one file per year, monthly as a single file) and full per-station CSV time series, with no key and no sign-up; no quota is published. | unit: mixed | metered on: unstated | read on: 2026-10-31 | source: [1] | note: The 2024 hourly file for all stations declares 992,333,139 bytes; the 2024 hourly CSV for station 10637 downloaded at 133,686 bytes. Recent hourly data lands within 24 hours. The files are not versioned: columns can be added or reordered without notice.
- per-object cap: not applicable: read-only files; the 2024 hourly all-station Parquet file declares 992,333,139 bytes | source: [1]
- retention: not applicable: read-only files | source: [1]
- egress: no fee and no key on data.meteostat.net; a 2024 hourly station file downloaded and a 992,333,139-byte Parquet file answered HTTP 200 with no account | metered: no | source: [1]
- identity: anonymous | detail: No sign-up and no API key for the bulk and time-series files; a station file and a bulk file answered HTTP 200 with no credentials.
- interface: rest
- binding note: No quota is published for the files and no key is asked; the size of one year of hourly data (992,333,139 bytes) is the practical unit of a pull.
- interface detail: plain HTTPS downloads from data.meteostat.net: hourly/{year}.parquet and daily/{year}.parquet (one file per year) and monthly.parquet (one file) for all stations; hourly/{year}/{station}.csv.gz and daily/{year}/{station}.csv.gz and monthly/{station}.csv.gz per station; station metadata in JSON and SQL
- endpoint: https://data.meteostat.net/hourly/2024.parquet
- tooling: any HTTP client; the Meteostat Python library wraps the files
- composes with: A keyless bulk source of station history: one Parquet file per year for hourly and daily, and one Parquet file for monthly, covers every station, so a full year of hourly observations is one download.
- reliability: Meteostat may discontinue or block access at any time without prior notice; a year with no data answers HTTP 404.
- notes: Bulk path: data.meteostat.net Parquet and CSV files with no key. The JSON API is a separate keyed offer (data-apis/meteostat-json-api).
- evidence note: The 2024 hourly CSV for station 10637 downloaded in full (133,686 bytes) with no credentials, and the 2024 hourly all-station Parquet file answered HTTP 200 declaring 992,333,139 bytes (the first 1,048,576 bytes were read).
- evidence:
  - [1] 2026-10-31: the bulk interface covers all stations in Parquet | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: The Meteostat bulk data interface provides access to weather and climate data across all weather stations in Parquet format.
  - [1] 2026-10-31: the bulk files need no key | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: This interface does not require an API key.
  - [1] 2026-10-31: the bulk files need no sign-up | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: Users are not required to sign up for this service.
  - [1] 2026-10-31: a year of hourly data for all stations is one file | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: curl "https://data.meteostat.net/hourly/2024.parquet" --output "2024.parquet"
  - [1] 2026-10-31: recent hourly data lands within 24 hours | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: Recent hourly data should be available after a maximum of 24 hours.
  - [2] 2026-10-31: per-station time series are CSV files by year | capture: sha256:dcb6f3b1cfed1a1e54269751abc8a11ee0c39b1cf3890c45436ca4008f04cb9f | quote: curl "https://data.meteostat.net/hourly/2024/10637.csv.gz" --output "10637-2024.csv.gz"
  - [2] 2026-10-31: the Python library wraps the files | capture: sha256:dcb6f3b1cfed1a1e54269751abc8a11ee0c39b1cf3890c45436ca4008f04cb9f | quote: With our [Python library](https://dev.meteostat.net/python) we're providing a simple, yet powerful, wrapper for data dumps.
  - [1] 2026-10-31: the files come hourly, daily and monthly | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: Data is available in three different granularities:
  - [1] 2026-10-31: the files are not versioned | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: This dataset is not versioned.
  - [1] 2026-10-31: columns can be added without notice | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: New columns may be added to the datasets without prior notice.
  - [1] 2026-10-31: a year with no data answers 404 | capture: sha256:b668a44dcf70f3f75b9a964ccc7b6f4d71c58ee97df55fb6701550373ec01c9b | quote: Years without data will return an HTTP `404` status code.
  - [3] 2026-10-31: station metadata comes in JSON and SQL | capture: sha256:777ebcc7e170374148754f4c5cdc00fdd5871262ba1d14e8de38c19ad115dcd1 | quote: Weather station [meta data](https://dev.meteostat.net/data/weather-stations) is provided in JSON and SQL formats.
  - [4] 2026-10-31:  | capture: sha256:fabf2f17fd98447cb8ee975b862983681c15608dafd86b6807ad13e5196c4a8f | quote: You must give credit to Meteostat and its meteorological data providers.
  - [3] 2026-10-31: the datasets need no sign-up | capture: sha256:777ebcc7e170374148754f4c5cdc00fdd5871262ba1d14e8de38c19ad115dcd1 | quote: Users are not required to sign up for this service.
  - [4] 2026-10-31:  | capture: sha256:fabf2f17fd98447cb8ee975b862983681c15608dafd86b6807ad13e5196c4a8f
  - [4] 2026-10-31:  | capture: sha256:fabf2f17fd98447cb8ee975b862983681c15608dafd86b6807ad13e5196c4a8f
  - [5] 2026-10-31: the data costs nothing | capture: sha256:a158d021ac7a2dc67451f98160c35eb41c9f7fce329e51ddfbcaa063c4860a4e | quote: All weather and climate data provided by Meteostat can be accessed without any cost for the user.
  - [5] 2026-10-31: access can be blocked without notice | capture: sha256:a158d021ac7a2dc67451f98160c35eb41c9f7fce329e51ddfbcaa063c4860a4e | quote: Meteostat may discontinue or block access to the services at any time without prior notice.
  - probe:https://data.meteostat.net/hourly/2024/10637.csv.gz 2026-10-31: the 2024 hourly CSV for station 10637 downloaded at 133,686 bytes | capture: sha256:1ca43ea60dc6a23dfec6cfe838f04ffe1605d705527f9b3fc41c2f6c1a1988b8 | quote: "bytes": 133686
  - probe:https://data.meteostat.net/hourly/2024/10637.csv.gz 2026-10-31: the station file answered HTTP 200 with no credentials | capture: sha256:1ca43ea60dc6a23dfec6cfe838f04ffe1605d705527f9b3fc41c2f6c1a1988b8 | quote: "status": 200
  - probe:https://data.meteostat.net/hourly/2024.parquet 2026-10-31: the 2024 hourly all-station Parquet file answered HTTP 200 declaring 992,333,139 bytes | capture: sha256:48ef49c1edd2bb90271f4cb1d67f336d09646123f37ccfafe94bb93dc0ff5e38 | quote: "declared_bytes": 992333139
  - probe:https://data.meteostat.net/monthly.parquet 2026-11-03: monthly.parquet, a single file for all stations, answered HTTP 200 with 152,559,044 bytes and no credentials | capture: sha256:6170581ba4cb5ca9170dfac1db41c15cf9a57e5fb2949538ea32a8ed31046bc7 | quote: "status": 200
  - [6] 2026-11-03: monthly bulk data for all stations is a single Parquet file, not one per year | capture: sha256:6d4047959b8f6821a8bd976b842c8e66aa62a4229c49d28bfa6fd8c7a54d4a68 | quote: This endpoint provides a single Parquet file containing historical monthly data for all weather stations.
  - [6] 2026-11-03: the monthly bulk file is monthly.parquet | capture: sha256:6d4047959b8f6821a8bd976b842c8e66aa62a4229c49d28bfa6fd8c7a54d4a68 | quote: https://data.meteostat.net/monthly.parquet
  - [7] 2026-11-03: per-station monthly CSV has no year in its path | capture: sha256:e120d4e8a1f984661ec72d1a4b92d0cf6c9a9a0ad8b11f6383033bc0e80ecd71 | quote: https://data.meteostat.net/monthly/{station}.csv.gz
  - [8] 2026-11-03: daily bulk data is one Parquet file per year | capture: sha256:9c6c4df9dd6117d066e8b996889425dcd3c8d1ce445a95fc6ff7df61b6236064 | quote: This endpoint provides one Parquet file per year.
- sources:
  - [1] https://dev.meteostat.net/data/bulk
  - [2] https://dev.meteostat.net/data/timeseries
  - [3] https://dev.meteostat.net/data
  - [4] https://dev.meteostat.net/license
  - [5] https://dev.meteostat.net/terms.html
  - [6] https://dev.meteostat.net/data/bulk/monthly
  - [7] https://dev.meteostat.net/data/timeseries/monthly
  - [8] https://dev.meteostat.net/data/bulk/daily
