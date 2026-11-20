# ameriflux

> ameriflux.lbl.gov | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ameriflux-lbl-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/ameriflux-lbl-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ameriflux

- `storage/ameriflux` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:54.754Z (live) | stale on 2026-12-04
- url https://ameriflux.lbl.gov/data/how-to-upload-data/
- free tier: none reachable: Deposit is gated on registering a physical tower site and having a Site PI choose a data policy; content is restricted to half-hourly flux/BADM formats. No blob storage, no general quota. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on the AmeriFlux upload-data page | source: [1] | note: not applicable
- retention: Uploaded data is archived and shared under the AmeriFlux Data Policy the Site PI selected for the site; no fixed retention period is stated. | source: [1]
- egress: not stated on the AmeriFlux upload-data page | metered: no
- identity: email
- interface: browser
- interface detail: Flux and BADM data files are submitted through the AmeriFlux website after signing in.
- tooling: not documented
- composes with: Feeds an AmeriFlux data archive under the site's data policy; not stated on the upload page as chaining to other storage services.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Deposit is gated on registering a physical tower site and having a Site PI choose a data policy; content is restricted to half-hourly flux/BADM formats. No blob storage, no general quota.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Deposit is gated on registering a physical tower site and having a Site PI choose a data policy; content is restricted to half-hourly flux/BADM formats. No blob storage, no general quota.
  - [1] 2026-11-19: AmeriFlux deposit requires an account and a registered tower site with a Site PI-selected data policy; it is a domain repository, not blob storage | capture: sha256:c5af162e8dece9c7c681dae125fabe996024bcead767623a9d1ebbdd6882dd9a | quote: When you upload your data, you agree that your data will be archived and shared according to the AmeriFlux Data Policy that the Site PI selected for your site.
  - [1] 2026-11-19: data is submitted as files through the AmeriFlux website after signing in | capture: sha256:f20a5830a662d5ab9ea8d89177b5ce326cd496ae8fb12f37c08f660bbac81577 | quote: Prepare the data, then go to Upload Data to submit your files and your comments describing the data files (sign in required).
  - [1] 2026-11-19: the upload page describes flux-data submission to AmeriFlux and states no per-object cap, egress price or cross-service chaining | capture: sha256:f20a5830a662d5ab9ea8d89177b5ce326cd496ae8fb12f37c08f660bbac81577 | quote: AmeriFlux.lbl.gov is now the place to submit all AmeriFlux data.
  - [1] 2026-11-19: uploads are archived and shared under the site's chosen AmeriFlux data policy | capture: sha256:f20a5830a662d5ab9ea8d89177b5ce326cd496ae8fb12f37c08f660bbac81577 | quote: When you upload your data, you agree that your data will be archived and shared according to the AmeriFlux Data Policy that the Site PI selected for your site.
- sources:
  - [1] https://ameriflux.lbl.gov/data/how-to-upload-data/
