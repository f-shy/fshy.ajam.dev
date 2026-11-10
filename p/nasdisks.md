# NASdisks Drive Data API

> nasdisks.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nasdisks/ | JSON https://fshy.ajam.dev/api/v1/entity/nasdisks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NASdisks Drive Data API

- `data-apis/nasdisks-drive-data-api` | qualifies | evidence documented | binding none | category open dataset API: NAS drive specifications and failure rates | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:45.809Z (live) | stale on 2026-12-03
- url https://www.nasdisks.com/data/
- free tier: No signup, no key, no rate limit: two read-only GET endpoints return the whole dataset of 298 drives, 21 with a measured failure rate, as JSON or CSV. | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: Both endpoints are cached for an hour. The failure-rate fields come from Backblaze Drive Stats.
- per-object cap: no cap stated; the whole dataset is one 168410-byte JSON or one 28364-byte CSV
- retention: the live endpoints serve the current catalogue, cached for an hour; dated snapshots of the dataset are kept in a GitHub repository and in a Zenodo deposit | source: [1]
- egress: not applicable: a dataset API, not metered in bytes; both endpoints are cached for an hour | metered: no | source: [1]
- identity: anonymous | detail: No signup and no key: the data page says so, and keyless GETs of both endpoints answered HTTP 200.
- interface: rest
- limits:
  - request-rate: none stated: the data page says no rate limit, and 40 parallel keyless GETs of drives.csv all answered HTTP 200 [1]
- binding note: No quota, key or rate limit is stated, and a 40-request parallel burst met no 429; the one-hour cache of both endpoints is the only limit on freshness.
- interface detail: HTTPS GET of https://www.nasdisks.com/data/drives.json (a top-level object with license, count and a drives array) and https://www.nasdisks.com/data/drives.csv (the same rows, flat), open to all origins; an OpenAPI 3.0.3 contract at https://www.nasdisks.com/openapi.yaml also covers a third endpoint, /embed/cheapest.json
- endpoint: part of interface detail
- tooling: any HTTP client, such as curl with jq; the data page gives a Zenodo DOI to cite the dataset
- composes with: Reference data on NAS and enterprise drives: specs, CMR/SMR recording technology and annualized failure rates derived from Backblaze Drive Stats, read as one JSON or CSV file. Bulk path: drives.json or drives.csv is the whole dataset in one GET, and dated snapshots of the dataset are in the GitHub repository deeddy/nas-drive-data and in a Zenodo deposit.
- reliability: Both endpoints are cached for an hour, so an answer can lag the catalogue; both answered HTTP 200 to keyless GETs on 2026-11-02.
- notes: Free requests: no quota, no key. Rate limit: none stated. Bulk path: drives.json or drives.csv, the whole dataset in one GET, with dated snapshots in a GitHub repository and a Zenodo deposit. The failure-rate fields come from Backblaze Drive Stats.
- evidence note: The data page states no signup, no key and no rate limit, and the repository README repeats no key and no rate limit; keyless GETs of drives.json and drives.csv answered 200 with the 298-drive count the page gives, and a 40-request parallel burst met no 429.
- evidence:
  - [1] 2026-11-02: the data page states no signup, no key and no rate limit | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: Refreshed as the catalogue and Backblaze data update. No signup, no key, no rate limit.
  - [1] 2026-11-02: the dataset holds 298 drives, 21 of them with a measured failure rate | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: 298 drives, 21 with a measured failure rate.
  - [1] 2026-11-02: both endpoints are read-only GETs, open to all origins and cached for an hour | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: Both endpoints are read-only `GET`s, allow cross-origin requests (`Access-Control-Allow-Origin: *`) and are cached for an hour, so you can call them straight from a browser, a notebook or a build step.
  - [1] 2026-11-02: drives.json is a JSON object with license, count and a drives array | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: - `https://www.nasdisks.com/data/drives.json` - JSON: a top-level object with `license`, `count` and a `drives` array.
  - [1] 2026-11-02: drives.csv carries the same rows as a flat CSV | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: - `https://www.nasdisks.com/data/drives.csv` - the same rows as a flat CSV.
  - [1] 2026-11-02: an OpenAPI 3.0 contract at openapi.yaml covers both endpoints and a price feed | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: Machine-readable contract: [`openapi.yaml`](https://www.nasdisks.com/openapi.yaml) (OpenAPI 3.0, covers both endpoints plus the embed price feed).
  - [1] 2026-11-02:  | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: The specs and CMR/SMR data are free to use with credit; the failure rates come from Backblaze Drive Stats.
  - [1] 2026-11-02: the data page shows a plain curl call piped to jq as the way to read the endpoint | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: curl -s https://www.nasdisks.com/data/drives.json | jq '.drives[0]'
  - [1] 2026-11-02: the data page names a Zenodo DOI to cite the dataset | capture: sha256:c37e2e5300278db4988573c69f2741bcf4aeb008be52712fa9e3eeb209fbd63e | quote: Cite this dataset: [NASdisks (2026), NAS Drive Dataset, Zenodo, doi:10.5281/zenodo.21225049](https://doi.org/10.5281/zenodo.21225049).
  - probe:https://www.nasdisks.com/data/drives.json 2026-11-02: a keyless GET of drives.json answered 200 with 168410 bytes | capture: sha256:988020122737d9a39f4791c45a77545327fb0b1dfa8dba06993691fad6bc4591 | quote: "status": 200, "bytes": 168410,
  - probe:https://www.nasdisks.com/data/drives.json 2026-11-02: the answer carries Cache-Control max-age=3600, public | capture: sha256:988020122737d9a39f4791c45a77545327fb0b1dfa8dba06993691fad6bc4591 | quote: "cache-control": "max-age=3600, public"
  - probe:https://www.nasdisks.com/data/drives.json 2026-11-02: the answer allows cross-origin reads from any origin | capture: sha256:988020122737d9a39f4791c45a77545327fb0b1dfa8dba06993691fad6bc4591 | quote: "access-control-allow-origin": "*"
  - probe:https://www.nasdisks.com/data/drives.json 2026-11-02: the body states a count of 298 drives and holds a drives array | capture: sha256:7213990808be25c641dfe9cddb05b3e16bcce1d8c89591bb4c3e06f2a18872d6 | quote: "count":298,"drives":[
  - probe:https://www.nasdisks.com/data/drives.csv 2026-11-02: a keyless GET of drives.csv answered 200 with 28364 bytes | capture: sha256:c4be341c7406a92805f36183e7f9045f8b3c785d652376bb3f2d0b6f1f0dcdba | quote: "status": 200, "bytes": 28364,
  - probe:https://www.nasdisks.com/data/drives.csv 2026-11-02: the CSV starts with a header row of the drive fields | capture: sha256:9f8f73ad6305cf0e06de633c24f0d02f28d16bb3188de5c9415c0d4c4489b2c7 | quote: model,brand,line,capacity_tb,rpm,cache_mb,interface,form_factor,recording_tech,erc_tler
  - probe:https://www.nasdisks.com/data/drives.csv 2026-11-02: the burst was 40 parallel GETs | capture: sha256:2e72d104147136c7fb3744ca5e8990f44bf35504fd1256b7a26e44e2e48a3ebe | quote: "concurrency": 40
  - probe:https://www.nasdisks.com/data/drives.csv 2026-11-02: the highest status of the 40 runs was 200, so none answered 429 | capture: sha256:2e72d104147136c7fb3744ca5e8990f44bf35504fd1256b7a26e44e2e48a3ebe | quote: "status": 200
  - [2] 2026-11-02: the contract is titled NASdisks Drive Data API | capture: sha256:6db4951c8a49193fcd1032ceea29b986d1cdb3802d1ed2b5d2ec77748528c187 | quote: title: NASdisks Drive Data API
  - [2] 2026-11-02: the contract is OpenAPI 3.0.3 | capture: sha256:6db4951c8a49193fcd1032ceea29b986d1cdb3802d1ed2b5d2ec77748528c187 | quote: openapi: 3.0.3
  - [2] 2026-11-02: the contract has a third path, /embed/cheapest.json | capture: sha256:6db4951c8a49193fcd1032ceea29b986d1cdb3802d1ed2b5d2ec77748528c187 | quote: /embed/cheapest.json:
  - [3] 2026-11-02: the repository README repeats that the live endpoints are cached, need no key and have no rate limit | capture: sha256:1d758b8ac3f5f75323a3099a18b5bdfc8ca3d8cf1eb61fe265a41adb1f09a543 | quote: If you'd rather hit a live endpoint (CORS-enabled, cached, no key, no rate limit):
  - [3] 2026-11-02: the repository keeps a dated JSON snapshot that mirrors the live API | capture: sha256:1d758b8ac3f5f75323a3099a18b5bdfc8ca3d8cf1eb61fe265a41adb1f09a543 | quote: | [`data/drives-2026-09-04.json`](https://github.com/deeddy/nas-drive-data/blob/main/data/drives-2026-09-04.json) | 273 | The same rows as JSON (mirror of the live API). |
  - [3] 2026-11-02: the repository files are dated snapshots, with the live dataset at nasdisks.com/data | capture: sha256:1d758b8ac3f5f75323a3099a18b5bdfc8ca3d8cf1eb61fe265a41adb1f09a543 | quote: These files are a dated snapshot and may be out of date.
  - [4] 2026-11-02: a Zenodo deposit holds a dated JSON snapshot of the dataset | capture: sha256:936f3a6b54c164079c700ac5208d7ba19cbc859a441f207f25ad4bf7661e8e64 | quote: | [drives-2026-09-04.json](https://zenodo.org/records/22552312/files/drives-2026-09-04.json?download=1) md5:a679dcd9c3ca426511ab6e5b12416c00 | 150.1 kB |
- sources:
  - [1] https://www.nasdisks.com/data/
  - [2] https://www.nasdisks.com/openapi.yaml
  - [3] https://github.com/deeddy/nas-drive-data
  - [4] https://zenodo.org/records/21225049
