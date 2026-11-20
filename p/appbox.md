# Appbox

> appbox.co | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/appbox/ | JSON https://fshy.ajam.dev/api/v1/entity/appbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Appbox

- `debrid/appbox-bg-2000` | paid-only | evidence documented | binding none | category app hosting and shared seedbox (one-click apps) | tier BG-2000
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.242Z (live) | stale on 2026-12-04
- url https://www.appbox.co/
- free tier: No free tier and no trial is published; the entry plan BG-2000 is EUR 8.74 per month, shown as EUR 6.12 per month for the first month with a 30% welcome discount. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: sold by total disk (2 TB HDD on BG-2000); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: BG-2000 lists 'Unmetered' traffic on a 10Gbps connection speed with 2 app slots. | metered: no | free allowance: unmetered stated | source: [1]
- identity: email | detail: Orders go through billing.appbox.co with an account. Payment methods, phone and document requirements were not read: unverified. | country: None
- interface: webdav
- limits:
  - per-ip-shaping: 10Gbps connection speed, unmetered traffic, 2 app slots [1]
- limits note: Larger plans: 3 TB EUR 10.99, 3.5 TB EUR 13.95, 4.5 TB EUR 18.51, 6 TB EUR 24.60, 8 TB EUR 31.90, 12 TB EUR 43.99 a month before the welcome discount. Streaming, Stacks, CMS, Operating System, Webserver, VPS and Windows app categories are excluded on BG-2000.
- binding note: No quota or object cap is published; the 2 app slots and the excluded categories shape what runs on the entry plan.
- interface detail: The app catalogue lists 'File Browser & Webdav' and a FileZilla Client app; the plan page itself does not name a transfer protocol, so SFTP or FTP access is unverified.
- tooling: Appbox dashboard with a 60+ app store (including File Browser with WebDAV, FileZilla Client and Rclone); streaming app categories are excluded on BG-2000; no API or CLI is documented
- composes with: A EUR 8.74 2 TB unmetered 10 Gbps app box; an Rclone app (Rclone Web plus an SSH login that runs rclone commands only) copies between cloud remotes; a torrent client app was not shown in the app text read: unverified
- reliability: Unmetered traffic with no fair-use numbers read; the app-slot count limits concurrent apps.
- notes: Not the same vendor as Bytesized Hosting's appbox range; the billing host is billing.appbox.co.
- evidence note: Plan, price and traffic are on the vendor home page read on 2026-11-03. A measured rung needs a slot and a timed transfer.
- extras:
  - port_gbps: 10
  - minimum_term: monthly; quarterly, semiannual and annual cycles are listed
  - trial_card_required: no trial exists
- evidence:
  - [1] 2026-11-03: BG-2000 is 2 TB HDD with unmetered traffic and 2 app slots | capture: sha256:f11e51d65a2170e44c7670f13b27337b29c6c9fe62bf89573ecb5c839446b50a | quote: BG-2000 2TB HDDStorage Unmetered Traffic 2 App Slots
  - [1] 2026-11-03: BG-2000 is EUR 8.74 a month, EUR 6.12 with the first-month discount | capture: sha256:f11e51d65a2170e44c7670f13b27337b29c6c9fe62bf89573ecb5c839446b50a | quote: €8.74 €6.12/mo
  - [1] 2026-11-03: the discount applies to the first month | capture: sha256:f11e51d65a2170e44c7670f13b27337b29c6c9fe62bf89573ecb5c839446b50a | quote: 💜 Save €2.62 on your first month
- sources:
  - [1] https://www.appbox.co/
