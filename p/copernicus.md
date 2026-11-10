# Copernicus

> copernicus.eu | Debrid, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/copernicus/ | JSON https://fshy.ajam.dev/api/v1/entity/copernicus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Copernicus Climate Data Store (CDS) API

- `debrid/copernicus-cds` | qualifies-with-caveat | evidence documented | binding none | category climate reanalysis and forecast archive (token-gated API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://cds.climate.copernicus.eu/how-to-api
- price USD 0
- free tier: Free data, account required: 'If you do not have an account yet, please register ... Once logged in, copy the code displayed below to the file $HOME/.cdsapirc' with url https://cds.climate.copernicus.eu/api and a personal access token. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No price, no byte allowance and no quota is published on the API setup page.
- per-object cap: not applicable: a retrieval request returns a packaged file (NetCDF, GRIB or ZIP) built from the requested variable, area and period | source: [1]
- retention: the archive is the product: ERA5 and the other datasets are reissued, not deleted, and a retrieval result is held for a limited period before it must be re-requested | source: [1] | note: The result-retention window is not stated on the page read; do not treat this row as a measured value.
- egress: Free. The token is identity, not payment. | metered: no | free allowance: no byte allowance published | source: [1]
- identity: email | detail: A CDS account (email registration) plus a personal access token copied into .cdsapirc, plus a licence acceptance per dataset. No card and no institution.
- interface: rest, cli
- limits:
  - request-rate: no numeric limit published on the setup page; retrievals are queued server-side and the queue position is the observable wait [1]
- limits note: The real gate is identity: registration plus a token plus, per dataset, a licence acceptance. The token is a credential and was not created here, so no retrieval was attempted.
- binding note: Nothing in the seven-kind vocabulary fails at 1 TiB/month that could be measured here; the gate that does fail is identity, which the vocabulary carries in identity_cost rather than in limits.
- interface detail: HTTPS API at https://cds.climate.copernicus.eu/api with the cdsapi python client; the token goes in $HOME/.cdsapirc. Process listing at /api/retrieve/v1/processes.
- endpoint: part of the free tier
- tooling: cdsapi (pip install 'cdsapi>=0.7.7') is the vendor's own client; curl can drive the same endpoints with the PRIVATE-TOKEN header.
- composes with: The only free ERA5-class reanalysis source among debrid providers; pair it with a compute sandbox because a full reanalysis pull is tens of GB and needs processing where it lands.
- reliability: Retrievals are queued and can take minutes to hours at peak; a client must poll a request id rather than expect a stream. No rate was measured because no token exists here.
- notes: Caveat is the account and the queue, not the price. This is the clearest example in the sector of a resource that is free but not anonymous: the bytes cost nothing and the token is mandatory.
- evidence note: The setup page was read and the process listing answered anonymously, which proves the service is live but not that a retrieval works. A retrieval with a real token would move this to measured.
- extras:
  - auth: personal access token in ~/.cdsapirc
  - client: cdsapi>=0.7.7
  - process_list_bytes: 25713
- evidence:
  - [1] 2026-10-23: account registration, personal access token in $HOME/.cdsapirc, cdsapi>=0.7.7, url https://cds.climate.copernicus.eu/api
  - probe:https://cds.climate.copernicus.eu/api/retrieve/v1/processes 2026-10-23: 200 with 25,713 bytes of JSON to an anonymous client - the process catalogue is public even though retrieval is not
- sources:
  - [1] https://cds.climate.copernicus.eu/how-to-api

## copernicus cds / ads

- `storage/copernicus-cds-ads` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cds.climate.copernicus.eu/how-to-api
- free tier: None reachable: Retrieval-only by design: a queue-based API (`cdsapi`) that materialises requested slices. There is no user deposit path, so it cannot store data. It is a data source, not stor. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Retrieval-only by design: a queue-based API (`cdsapi`) that materialises requested slices. There is no user deposit path, so it cannot store data — it is a data source, not stor
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Retrieval-only by design: a queue-based API (`cdsapi`) that materialises requested slices. There is no user deposit path, so it cannot store data — it is a data source, not stor
- sources:
  - [1] https://cds.climate.copernicus.eu/how-to-api

## Copernicus Data Space Ecosystem (CDSE / ESA DIAS) - 12 TB/month of free READ, zero writable storage

- `storage/copernicus-data-space-ecosystem-12-tb-month-of-free-read` | fails-quota | evidence reported | binding volume-quota | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:34:57.981Z (live) | stale on 2026-11-18
- url https://dataspace.copernicus.eu/
- free tier: 12 TB per rolling 30 days of download via S3/OData/STAC for a Copernicus General User, 20 MB/s per connection, 4 concurrent connections, 2,000 requests/min, empty-account registration. After the transfer limit is hit, bandwidth drops to 1 MB/s and 1 concurrent connection until the 30-day total falls back under the limit. Data Workspace adds 0.1 TB/month of deferred-access transfer and 25 processed products/month. JupyterLab gives 10 GB of persistent scratch, 30-day idle expiry. | unit: TB | metered on: downloaded-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: The whole quota IS egress - this is the largest free read allowance found anywhere in the programme, but there is no general-purpose bucket to write to. | metered: yes
- identity: email | detail: registration form (required fields not itemised on the page) with email verification
- interface: s3, cli
- limits:
  - volume-quota (binding): 12 TB of downloads per rolling 30 days [1]
  - per-ip-shaping: 20 MB/s [1]
  - per-ip-shaping: 4 concurrent connections [1]
  - per-ip-shaping: 1 MB/s and 1 concurrent connection after the 12 TB limit [1]
- limits note: Read-only EO products. No user-owned bucket: the S3 endpoint serves the mission archive. Registration is open to anyone with an email and is self-service.
- binding note: downloads are metered per account over a rolling 30 days; above 12 TB the rate drops to 1 MB/s and 1 connection, which is about 0.086 TB per day
- interface detail: s3
- tooling: S3 credentials self-service from the user panel against eodata.dataspace.copernicus.eu; openEO API (10,000 credits/month, temporary boost); Sentinel Hub APIs (10,000 requests/month); s3cmd/boto3 documented.
- composes with: Per account, and the 30-day rolling window means 12 TB/month sustained without cycling accounts. Creodias resells the same platform with paid extensions.
- reliability: CloudFerro-operated for ESA; the 1 MB/s throttle after the cap is a hard cliff, not a soft degrade.
- notes: the same as the free tier
- evidence note: the vendor pages of the 2026-11-03 evidence rows were read and captured (https://documentation.dataspace.copernicus.eu/Quotas.html, https://documentation.dataspace.copernicus.eu/Registration.html); a field that decides the verdict is not cited by those captures, so the rung stays reported
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 12 TB per rolling 30 days of download via S3/OData/STAC for a Copernicus General User, 20 MB/s per connection, 4 concurrent connections, 2,000 requests/min, empty-account registration. After the transfer limit is hit, bandwidth drops to 1 MB/s and 1 concurrent connection until the 30-day total falls back under the limit. Data Workspace adds 0.1 TB/month of deferred-access transfer and 25 processed products/month. JupyterLab gives 10 GB of persistent scratch, 30-day idle expiry.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Monthly transfer limit (TB) (IAD) 12'; 'After reaching this monthly transfer limit, the maximum bandwidth drops to 1MB/s and the number of concurrent connections drops to 1'
  - [1] 2026-10-21: 'Number of concurrent connections limit (IAD) 4'; 'Bandwidth limit per connection (MB/s) 20'; openEO 'Credits per month 10 000'
  - [2] 2026-10-21: 'Each JupyterLab instance includes 10GB of storage... preserved to 30 days from the last login'
  - [3] 2026-10-21: 6 TB -> 12 TB increase confirmed
  - [1] 2026-11-03: a Copernicus General User has a monthly transfer limit of 12 TB on S3, OData and STAC | capture: sha256:6b0f7ee93c56024d7b9b43bec0f6e13f6c7b318cddbf9877c841312b41a64944 | quote: | Monthly transfer limit (TB) (IAD¹)¹⁰ | 12 | - | - | - | - |
  - [1] 2026-11-03: the transfer limit is metered on downloaded volume over a rolling 30 days per account | capture: sha256:6b0f7ee93c56024d7b9b43bec0f6e13f6c7b318cddbf9877c841312b41a64944 | quote: The total volume of downloads from the Copernicus Data Space Ecosystem for each user account is summed up for the last 30 days.
  - [1] 2026-11-03: above the limit the rate drops to 1 MB/s and 1 connection | capture: sha256:6b0f7ee93c56024d7b9b43bec0f6e13f6c7b318cddbf9877c841312b41a64944 | quote: ¹⁰ After reaching this monthly transfer limit, the maximum bandwidth drops to 1MB/s and the number of concurrent connections drops to 1.
  - [4] 2026-11-03: registration is a form followed by an email verification | capture: sha256:2285f29441ab61fa6b1890f580ee1af278874e7ef934735dba515682639b17d9 | quote: Upon registration, you will be prompted to verify your email address by receiving a verification email.
  - [1] 2026-11-03: 20 MB/s per connection | capture: sha256:6b0f7ee93c56024d7b9b43bec0f6e13f6c7b318cddbf9877c841312b41a64944 | quote: | Bandwidth limit per connection (MB/s) (IAD¹) | 20 | - | - | - | - |
  - [1] 2026-11-03: 4 concurrent connections | capture: sha256:6b0f7ee93c56024d7b9b43bec0f6e13f6c7b318cddbf9877c841312b41a64944 | quote: | Number of concurrent connections limit (IAD¹) | 4 | - | - | - | - |
  - [1] 2026-11-03: above the monthly limit the bandwidth drops to 1 MB/s and 1 connection | capture: sha256:6b0f7ee93c56024d7b9b43bec0f6e13f6c7b318cddbf9877c841312b41a64944 | quote: ¹⁰ After reaching this monthly transfer limit, the maximum bandwidth drops to 1MB/s and the number of concurrent connections drops to 1.
  - [1] 2026-11-03: downloads are summed per user account over the last 30 days | capture: sha256:6b0f7ee93c56024d7b9b43bec0f6e13f6c7b318cddbf9877c841312b41a64944 | quote: The total volume of downloads from the Copernicus Data Space Ecosystem for each user account is summed up for the last 30 days.
- sources:
  - [1] https://documentation.dataspace.copernicus.eu/Quotas.html
  - [2] https://documentation.dataspace.copernicus.eu/Applications/JupyterHub.html
  - [3] https://forum.dataspace.copernicus.eu/t/update-increased-monthly-transfer-limit-from-6tb-to-12tb-for-cdse-users/752
  - [4] https://documentation.dataspace.copernicus.eu/Registration.html

## wekeo drive (copernicus dias file hosting)

- `storage/wekeo-drive` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:53.247Z (inherited) | stale on 2026-11-14
- url https://wekeo.copernicus.eu/wekeo-drive
- free tier: WEkEO Drive: up to 8 GB of free space for datasets and notebooks, free after sign-up; no period is stated. | unit: GB | metered on: stored-bytes | read on: 2026-10-30 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Free tier provides 8 GB of storage, operating as a workspace file-sharing system for hosted Jupyter notebooks rather than raw object storage.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [1] 2026-10-30: WEkEO Drive offers up to 8 GB of free space | capture: sha256:4482b8fec9b6e485cba28e6203f4bdff097af2b8624a0ed93b8f19cbd3f76e9e | quote: Up to 8GB of free space
  - [1] 2026-10-30: WEkEO Drive is free after sign-up | capture: sha256:4482b8fec9b6e485cba28e6203f4bdff097af2b8624a0ed93b8f19cbd3f76e9e | quote: WEkEO Drive it is free, you just need to sign up and go to the Drive from your “My WEkEO” dashboard.
- sources:
  - [1] https://wekeo.copernicus.eu/wekeo-drive
