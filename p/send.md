# Send.now

> send.now | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/send/ | JSON https://fshy.ajam.dev/api/v1/entity/send.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Send.now

- `debrid/send-now` | qualifies-with-caveat | evidence documented | binding volume-quota | category file transfer and drive hybrid: WebDAV, FTP and HTTP API on one host | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:41:32.718Z (live) | stale on 2026-11-23
- url https://send.now/
- price EUR 1.50 per TB-month of storage at Premium (EUR 14.99 for 10 TB); EUR 3 per TB of direct-link egress | parsed USD 1.68/TB-mo
- free tier: "Free to use, no account needed" for upload, share and download. A guest 'can send a few an hour'; an account is free. Retention is by download activity rather than by a byte count: 'files stay while they are downloaded at least once every 30 days' with an account, and 'As a guest user, your files might be lost after 15 days of inactivity'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The free tier is not priced in bytes at all. It is priced in activity and in how many transfers a guest may start per hour.
- per-object cap: "Any type and size" for uploads; the paid tier repeats 'No limits on file size'. Chunked upload with a selectable part size (10 to 100 MB) and auto-retry. | source: [1] | note: No hard per-file number is printed anywhere on the site, free or paid.
- retention: Guests: 'might be lost after 15 days of inactivity'. Accounts: 'Create a free account to push this to 30 days', and files stay 'while they are downloaded at least once every 30 days'. The sender can also set an explicit expiry from 1 hour to 15 days, or burn after download. | days: 15 | source: [1] | note: Two clocks: the activity clock (15 days guest, 30 days account) and the sender-set expiry, whichever comes first. Paid accounts get 'Files never expire'.
- egress: Downloads are unmetered on the free path; the meters are on direct links. Premium includes '1000 GB direct link traffic' and 'Unlimited bandwidth' for ordinary downloads, with 'Direct Link Traffic' sold as an add-on at EUR 3 per 1000 GB. | metered: yes | free allowance: Free direct links are limited to 10 MB files | price per TB: EUR 3 per TB of direct-link traffic (1 TB minimum block) | source: [2]
- identity: email | detail: Free account needs an email; the registration page sets only two constraints: 'Password must be at least 14 characters long' and no special characters or spaces in the username. No card, no phone, no verification was mentioned.
- interface: webdav, ftp, rest, unknown
- limits:
  - volume-quota (binding): 1000 GB of direct-link traffic included per month on Premium; further blocks at EUR 3 per 1000 GB [2]
  - request-rate: guests 'can send a few an hour'; the API returns 429 after 5 wrong-key requests in 5 minutes [1]
  - retention-clamped: files are removed after 15 days of inactivity as a guest, 30 days with a free account, unless a paid plan is held [1]
- limits note: The word 'unlimited' in the paid tier applies to download-page traffic, not to direct links: the same pricing table lists '1000 GB direct link traffic' in the Premium column and sells extra blocks. A client that hotlinks files is on the meter; a client that sends a page link is not.
- binding note: At 1 TiB per month of direct-link traffic the 1000 GB direct-link allowance is spent inside the first month and every TB after it costs EUR 3; ordinary page downloads stay unmetered but cannot be embedded or fetched by a script that expects a stable URL.
- interface detail: Three programme paths, all documented on the homepage: WebDAV at `https://webdav.send.now` (needs a free account and an app password); FTP at `ftp.send.now` (Europe) or `ftp-us.send.now` (USA) on port 992 with implicit FTP over TLS, one transfer at a time; and an HTTP API whose upload path is two calls - `GET https://send.now/api/upload/server` for an upload address, then `POST -F "file_0=@video.mp4"` to it.
- endpoint: part of interface detail
- tooling: The best-served host among debrid providers: WebDAV means a native macOS/Finder or Windows mount with no wrapper, FTP with TLS means FileZilla or lftp, and the API means a script. rclone can talk to it through WebDAV without a dedicated backend.
- composes with: A drop box for handoffs and a WebDAV drive for the rare file that must live somewhere mountable: it takes a 5 GB render out of a paid object store, serves it to a collaborator, and expires it by itself. The WebDAV endpoint is what makes it a candidate for a mounting layer rather than a download queue.
- reliability: Two operational facts a client must know before putting anything there: FTP allows 'One transfer at a time', and files disappear by inactivity rather than by quota, so an archive left untouched for a month is gone whether or not there was room for it. The API also answers HTTP 200 on every call and puts the real status in the JSON body.
- notes: File hosting service providing native WebDAV and FTP access alongside REST API endpoints without requiring custom wrappers.
- evidence note: Retention rules, both metering rules, all three access paths and the full price table were read on the vendor's pages. Nothing was uploaded, so throughput and the real per-file ceiling are unmeasured.
- extras:
  - webdav: https://webdav.send.now
  - ftp: ftp.send.now (EU) / ftp-us.send.now (US), port 992, implicit FTP over TLS, one transfer at a time
  - successor_note: userscloud.com now redirects here; the older brand is recorded separately as dead
- evidence:
  - [1] 2026-10-23: the three access paths (WebDAV `webdav.send.now`, FTP `ftp.send.now` port 992 implicit TLS, API), the guest and account retention rules, and 'Any type and size' uploads
  - [2] 2026-10-23: Premium at EUR 14.99 with 10 TB storage, EUR 2 per extra TB, 'Unlimited bandwidth', '1000 GB direct link traffic', 5 simultaneous downloads, files never expire; Yearly EUR 60 with 6000 GB direct link traffic; the EUR 3 per 1000 GB direct-link add-on
  - [3] 2026-10-23: 
  - [4] 2026-10-23: signup needs only a username and a 14-character password; no card or phone is asked for on the form
- sources:
  - [1] https://send.now/
  - [2] https://send.now/pricing
  - [3] https://send.now/docs/api/
  - [4] https://send.now/register
