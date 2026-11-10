# FilePress

> filebee.xyz | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filebee/ | JSON https://fshy.ajam.dev/api/v1/entity/filebee.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FilePress (Filebee)

- `debrid/filepress` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category Google Drive link wrapper and file-index front end (Indian DDL ecosystem) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:35:38.850Z (live) | stale on 2026-11-23
- url https://filebee.xyz/
- price USD 0
- free tier: Publishing and downloading are free: 'Direct Download - Users can download File Directly Without Login'. No byte allowance, account quota or price appears on the page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The page sells a capability, not capacity. Whatever quota exists is Google Drive's, inherited through the file id the service wraps.
- per-object cap: No per-file size is stated for the wrapper itself. The two stated ceilings are feature limits: Telegram upload 'Support Upto 15GB' and watch-online 'Support Upto 20GB'. | source: [1] | note: 15 GB and 20 GB are the largest numbers the page prints, and each is attached to one output channel, not to storage.
- retention: Not stated. A link points at a Google Drive file id, so it lives as long as that Drive file does. | source: [1] | note: The service holds a pointer, not bytes.
- egress: The download is served as a 'Direct Download' without login. The page claims 'Anti Limit V5 - File will never get any Limit', which is the product's whole reason to exist: it interposes itself between the downloader and Google Drive's per-file limit. | metered: no | source: [1]
- identity: email | detail: Publishing needs an account (the homepage offers 'Open Login'); the signup form was not read, so whether the gate is an email address or Google OAuth is unverified. Downloading needs nothing: 'Users can download File Directly Without Login'.
- interface: rest, unknown
- limits:
  - per-object-cap: 15 GB per file via the Telegram upload channel; 20 GB per video via watch-online [1]
  - request-rate: unstated; whatever Google Drive enforces per file id is the real ceiling [1]
- limits note: The 'Anti Limit V5' badge is the vendor's claim that the wrapper defeats Drive's download limit. The sibling service DriveSeed lists '403: User Rate Limit Exceeded - Fixed to Great Extent' among its fixes, which is the same limit seen from the other side of the chain and confirms the limit is real and recurring.
- binding note: At 1 TiB a month the wall is Google's per-file and per-session throttling, not a FilePress quota: FilePress publishes none. The wrapper exists to move that throttle, so the constraint travels with it rather than disappearing.
- interface detail: REST: POST {Domain}/api/v1/file/add with a JSON body carrying a key, a Google Drive file id, quality, genre, tmdb_id, season and episode numbers, and an isAutoUploadToStream flag. Documentation is published at api.filebee.xyz, which titles itself 'FilePress API' and 'Documentation for the Kittn API'. Also 'Auto Upload To MirrorAce & MirroredTo - Just Add there api keys in your profile section'.
- endpoint: https://api.filebee.xyz/api/v1/file/add
- tooling: No client exists and none is needed: a POST with a JSON body and a key copied from the account does the publish. The published example carries a live-looking key value in the documentation itself; that is the vendor's sample, not a credential of ours.
- composes with: The publish step of the Indian index chain: an index site posts a FilePress link, FilePress wraps a Google Drive id into a page, and the downloader lands on a Drive file whose per-file limit the wrapper exists to dodge. It feeds HubCloud, DriveSeed and GDFlix, which all wrap the same Drive id again one layer down.
- reliability: The brand has moved domains repeatedly: filebee.xyz, filepress.cloud and filepress.wiki all resolve to the live app at new2.filepress.lat, filepress.xyz is parked for sale at USD 1,299, and filepress.info plus filepress.buzz could not be checked at all because network requests refused both (HTTP 530 at network requests, exit 4), so their state is unknown rather than dead. Any hard-coded hostname in a user breaks.
- notes: It is not storage: it is the publish step of the chain that turns a Google Drive file into a share page. The record exists so the subsequent audit prices the chain correctly and does not re-open filepress.info, which is dead.
- evidence note: The feature list, the API endpoint and the 15/20 GB ceilings were read on the vendor's own pages. What the record does not have is a measured download, so the 'Anti Limit' claim and the true throttle remain unverified.
- extras:
  - live_hosts: new2.filepress.lat (via filebee.xyz, filepress.cloud, filepress.wiki)
  - dead_hosts: filepress.xyz (GoDaddy parking, USD 1,299)
  - sibling_record: driveseed, hubcloud, gdflix, hubdrive
- evidence:
  - [1] 2026-10-23: the service is live under the FilePress brand at filebee.xyz; 'Anti Limit V5', 'Telegram Upload ... Upto 15GB', 'Watch Online ... Upto 20GB', 'Direct Download - Users can download File Directly Without Login'
  - [2] 2026-10-23: filepress.cloud redirects to new2.filepress.lat and adds 'API Support Available' with a link to api.filebee.xyz, plus auto-upload to MirrorAce and MirroredTo
  - [3] 2026-10-23: a real REST publish route exists: POST {Domain}/api/v1/file/add with key, Drive file id, quality, tmdb_id, season and episode; the page titles itself 'FilePress API'
  - [4] 2026-10-23: the .xyz domain is a GoDaddy parked listing, 'filepress.xyz is for sale ... $1,299', so that hostname is not the service
- sources:
  - [1] https://filebee.xyz/
  - [2] https://filepress.cloud/
  - [3] https://api.filebee.xyz/
  - [4] https://filepress.xyz/
