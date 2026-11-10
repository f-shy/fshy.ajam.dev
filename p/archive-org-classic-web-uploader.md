# archive.org classic web uploader

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archive-org-classic-web-uploader/ | JSON https://fshy.ajam.dev/api/v1/entity/archive-org-classic-web-uploader.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## archive.org classic web uploader (browser drag-and-drop)

- `storage/archive-org-classic-web-uploader` | qualifies-with-caveat | evidence documented | binding per-object-cap | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:31:28.058Z (live) | stale on 2026-12-05
- url https://help.archive.org/help/uploading-troubleshooting/
- free tier: No upload fee is stated and no total storage quota is stated; a free account is required. A single file should not exceed ~500 to ~700 GB (500 GB recommended) and an item should hold fewer than 10,000 files. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: A single file in an item should not be larger than ~500 to ~700 GB; 500 GB is the recommended lower limit. | bytes: 500000000000 | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: a free archive.org account is required before uploading; sign-in uses the account email address and a password
- interface: unknown
- limits:
  - per-object-cap (binding): ~500 to ~700 GB per file (500 GB recommended) [1]
- limits note: Items should hold fewer than 10,000 files with no file above 1TB; the page states the API allows up to 250,000 files, and a browser upload that fails on a network interruption shows a Resume button.
- binding note: the per-file size (500 GB recommended) sets the shard size; no total storage quota is stated
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: A browser upload that fails on a network interruption shows a Resume button; a failed upload can instead show a 503-slowdown-spam message, for which the page gives no cause.
- notes: Manual browser upload path is subject to Resume button retries, HTTP 503 slowdown responses, and ASCII-only filenames. The IAS3 API or ia CLI provide programmatic access.
- evidence note: The 2026-11-03 evidence rows read https://help.archive.org/help/uploading-troubleshooting/ (per-file size, 10,000-file item guidance, Resume button, 503-slowdown-spam), https://help.archive.org/help/archive-org-information/ (no upload fees) and https://help.archive.org/help/uploading-a-basic-guide/ (free account required). Every field that decides the verdict cites those captures.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Also the weakest path (Resume-button retries, 503-slowdown-spam, ASCII-only filenames). Only the IAS3 API or ia CLI are viable at 20TB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: also the weakest path (Resume-button retries, 503-slowdown-spam, ASCII-only filenames). Only the IAS3 API or ia CLI are viable at 20TB.
  - [1] 2026-11-03: the per-file size guidance is 500 GB recommended, ~500 to ~700 GB maximum | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
  - [2] 2026-11-03: the Help Center states there is no fee for uploading and preserving materials | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: At this time we have no fees for uploading and preserving materials.
  - [2] 2026-11-03: uploads are free; the limits on the pages are per file and per item, not a total in one unit | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: At this time we have no fees for uploading and preserving materials.
  - [2] 2026-11-03: the page states no metering basis for uploads | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: At this time we have no fees for uploading and preserving materials.
  - [1] 2026-11-03: the recommended per-file limit is 500 GB | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
  - [1] 2026-11-03: the per-file limit | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
  - [1] 2026-11-03: the per-item file-count and file-size recommendation | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: We recommend creating items that have less than 10,000 files, and where the files do not exceed 1TB.
  - [1] 2026-11-03: the only stated numeric limit is the per-file size | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
  - [1] 2026-11-03: the per-file size is the stated limit | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
  - [3] 2026-11-03: a free account is required before upload | capture: sha256:2af054d55dffcd44c8d0693ae3231334ab0a26da635bddc2219a2aa78c8b5d20 | quote: You will need a to register for a free account on archive.org before you can upload.
  - [1] 2026-11-03: the page documents the 503-slowdown-spam failure of the browser uploader | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: You may receive a 503-slowdown-spam message.
  - [2] 2026-11-03: uploads are free and no total storage quota is stated, so the allowance is not the limit | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: At this time we have no fees for uploading and preserving materials.
  - [1] 2026-11-03: the per-file limit is as stated | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
  - [1] 2026-11-03: the page lists a 503-slowdown-spam message as a second upload failure notice and gives no cause for it | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: You may receive a 503-slowdown-spam message. When this occurs, please click the Details link and send the error message to [info@archive.org](mailto:info@archive.org).
  - [1] 2026-11-03: a Resume button is shown when the upload failed due to a network interruption | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: You will see a Resume button as shown below. This is when the upload failed due to some network interruption.
  - [1] 2026-11-04: the per-file size guidance is 500 GB recommended, ~500 to ~700 GB maximum | capture: sha256:696664a1c6dded7af69f2771c2f51bf956239376771cea7e8889806aed3dfcdb | quote: A single file in an item should not be larger than ~500 to ~700 GB (capacity depends on activity levels and other circumstances, so we recommend using the lower limit of 500GB).
- sources:
  - [1] https://help.archive.org/help/uploading-troubleshooting/
  - [2] https://help.archive.org/help/archive-org-information/
  - [3] https://help.archive.org/help/uploading-a-basic-guide/
