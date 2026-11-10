# NASA Earthdata

> earthdata.nasa.gov | Debrid, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/earthdata-nasa-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/earthdata-nasa-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NASA Earthdata (Earthdata Login + CMR Search)

- `debrid/nasa-earthdata` | qualifies-with-caveat | evidence documented | binding request-rate | category Earth science data archive (login-gated DAAC downloads, open search API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://www.earthdata.nasa.gov/data/earthdata-login
- price USD 0
- free tier: Data are free but gated: 'You will need to use Earthdata Login anytime you want to download Earth science data from any of the DAACs. Access to DAAC and other EOSDIS web information (e.g. about data, missions, instruments) does not require a login.' The CMR search API answers anonymously. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: Registration is at urs.earthdata.nasa.gov; no fee is mentioned.
- per-object cap: not applicable: a granule is the object and its size is collection-specific. The search response measured here was 4,238 bytes. | source: [2]
- retention: per collection; DAACs publish their own retention, and CMR itself is a catalogue that reflects current holdings | source: [1]
- egress: Free. The login is identity and metrics, not payment: the registration page describes it as a user registration and profile system. | metered: no | free allowance: no byte allowance published | source: [1]
- identity: email | detail: Earthdata Login registration (free, at urs.earthdata.nasa.gov) is mandatory for any DAAC download; the catalogue search needs nothing.
- interface: rest, cli
- limits:
  - request-rate (binding): CMR deploys throttling rules that return 429 with a retry-after header; a hard 180-second limit applies to any request, and paging stops at the 1,000,000th item [3]
- limits note: The CMR page names the throttle mechanism and the 180 s ceiling but publishes no numeric rate. The download path itself was not exercised because no EDL account exists here.
- binding note: For a caller holding an account, CMR's throttling and the 180-second request ceiling bound a catalogue walk. For a caller without one, the EDL gate fails first - recorded in identity_cost, because the seven-kind vocabulary has no identity kind.
- interface detail: CMR search at https://cmr.earthdata.nasa.gov/search/ (JSON), granule download from the DAAC with an EDL bearer token or a .netrc entry; earthaccess and the EDL client wrap the token flow.
- endpoint: part of interface detail
- tooling: earthaccess (python) handles login and download; curl needs the Authorization: Bearer header; the CMR API also takes a token query parameter but marks it for deprecation.
- composes with: The climate and remote-sensing counterpart to Copernicus: two login-gated archives that between them cover reanalysis and satellite products, both needing the same kind of free account.
- reliability: CMR paging cannot pass the millionth item and granule queries without a collection stop at 10,000; a whole-archive crawl has to be sliced by collection or by time.
- notes: Caveat is identity: the bytes are free and the account is mandatory. This is the pattern the sector is meant to separate from the anonymous sources - NASA is not a no-account source, even though nothing is charged.
- evidence note: The search API was exercised anonymously and the login requirement is the vendor's own sentence; no granule was downloaded, so the download path is documented and not measured.
- extras:
  - login_required_for: any DAAC download
  - cmr_anonymous: yes
  - cmr_hard_timeout_s: 180
  - cmr_paging_ceiling: 1000000
- evidence:
  - [1] 2026-10-23: Earthdata Login is the registration system for DAAC data; 'registration is quick and easy' at urs.earthdata.nasa.gov
  - [3] 2026-10-23: 429 with retry-after throttling rules, the 180-second hard request limit, and the 1,000,000-item paging ceiling
  - probe:https://cmr.earthdata.nasa.gov/search/collections.json?page_size=1 2026-10-23: 200, 4,238 bytes of JSON to an anonymous client - the catalogue is open even though the granules are not
- sources:
  - [1] https://www.earthdata.nasa.gov/data/earthdata-login
  - [2] https://cmr.earthdata.nasa.gov/search/collections.json
  - [3] https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html

## NASA Earthdata AWS allocation (2 PB pool via Space Act Agreement)

- `storage/nasa-earthdata-aws-allocation` | fails-identity | evidence reported | binding none | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.earthdata.nasa.gov/engage/partnerships/aws-storage-cloud-compute-request
- free tier: A 2 PB storage allocation held by NASA's Earth Science Division inside the AWS Open Data Program, subdivided by request. Individual allocations are not published; requests are reviewed monthly (1st) with responses by the 7th. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: | Requirements are explicitly internal: data must be 'write once, read many', a large meaningful NASA science collection, listed on the Registry of Open Data, and 'not stored for long-term operational use' | source: [1] | note: not stated
- egress: Free public read through the AWS Open Data registry entry. | metered: no
- identity: institution | detail: institution
- interface: s3
- limits:
  - write-gated: reviewed monthly (1st) with responses by the 7th [1]
  - write-gated: review is NASA's ESD [1]
- limits note: Requirements are explicitly internal: data must be 'write once, read many', a large meaningful NASA science collection, listed on the Registry of Open Data, and 'not stored for long-term operational use'. A Google Form is the entry point, but the review is NASA's ESD.
- interface detail: s3
- tooling: S3 bucket handed over by the platform point of contact after approval; Registry YAML PR required to publish.
- composes with: Not multiplicable by an outsider: this is an internal reallocation of NASA's own 2 PB, gated on being NASA-affiliated NASA science.
- reliability: Same S3 reliability as AWS ODS. Not reachable without a NASA affiliation.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: A 2 PB storage allocation held by NASA's Earth Science Division inside the AWS Open Data Program, subdivided by request. Individual allocations are not published; requests are reviewed monthly (1st) with responses by the 7th.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'NASA's Earth Science Division (ESD) has been given an allocation of 2 PB within the AWS Open Data Program'
  - withheld 2026-10-21: same - 'Data should be considered write once, read many'; 'Requests will be reviewed on the 1st of each month and responses provided by the 7th'
- sources:
  - [1] https://www.earthdata.nasa.gov/engage/partnerships/aws-storage-cloud-compute-request
