# Disroot Cloud

> disroot.org | Storage, Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/disroot/ | JSON https://fshy.ajam.dev/api/v1/entity/disroot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## disroot

- `storage/disroot` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.059Z (live) | stale on 2026-12-04
- url https://disroot.org/services/nextcloud
- free tier: none reachable: free Nextcloud (so WebDAV works out of the box) but only 2 GB; extra space is granted by an application form, not by scaling accounts, and the instance is donation-funded and rate-conscious | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: write-gated
  - dead_end.why: free Nextcloud (so WebDAV works out of the box) but only 2 GB; extra space is granted by an application form, not by scaling accounts, and the instance is donation-funded and rate-conscious
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: free Nextcloud (so WebDAV works out of the box) but only 2 GB; extra space is granted by an application form, not by scaling accounts, and the instance is donation-funded and rate-conscious
  - [1] 2026-11-19: free cloud storage is 2GB; more requires an extension | capture: sha256:a01636f166602f9f778c27cf05572d1ffd87c638e60a58634df6200cfe633b54 | quote: If the free 2GB is not enough, you can extend your cloud storage.
  - [1] 2026-11-19: the service is Nextcloud-based | capture: sha256:a01636f166602f9f778c27cf05572d1ffd87c638e60a58634df6200cfe633b54 | quote: Disroot's Cloud service is powered by [Nextcloud](http://nextcloud.com/).
- sources:
  - [1] https://disroot.org/services/nextcloud

## Disroot Cloud (donation-funded Nextcloud)

- `netdisk-pan/disroot-cloud` | fails-quota | evidence reported | binding write-gated | category donation-funded Nextcloud, free tier only
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:23:48.016Z (inherited) | stale on 2026-12-10
- url https://disroot.org/en/services/nextcloud
- price EUR 110/year for 60 GB, which is EUR 152/TB/year and therefore irrelevant | parsed USD 14.27/TB-mo
- free tier: 1 GB for email, 2 GB for the cloud and 500 MB for CryptPad, free with an account | unit: GB | metered on: stored-bytes | read on: 2026-11-25 | source: [1]
- per-object cap: Not published | source: [2]
- retention: Until deleted. No retention clock published | source: [2]
- egress: No published cap. The instance is donation-funded and the guidance asks users not to overuse it; that is a fair-use sentence and not a number | metered: no | source: [3]
- identity: email | detail: a Disroot account. The extra-storage form is a separate human review that asks why the space is needed
- interface: webdav, rest, rclone
- limits:
  - write-gated (binding): extra capacity is granted by a human-reviewed application form, not by a self-serve checkout [3]
- binding note: The quota closes it at 60 GB, but the gate that matters more is that capacity above 2 GB is a human decision rather than a purchase, so no plan can be built on a number that arrives by review.
- tooling: rclone webdav and the Nextcloud clients, which is the one real advantage: it needs no wrapper
- composes with: Nothing to chain. The absolute ceiling is 60 GB at any price, so it cannot hold a share of a 10 TiB working set and cannot participate in a pool. Its role would be as a small always-available mount for a bridge's state
- reliability: The operator's status page states that the Nextcloud Files feature is disabled until a hardware failure on the storage server is solved, while calendars, contacts and chat work. Its 29.10.2026 update says the RAID array rebuild completed after a disk replacement, with one repeated unreadable sector left that complicates file system repair
- evidence note: Confidence is reported: documentation is dated to research on 2026-10-21. Raising confidence to documented or measured requires re-reading the storage expansion form and executing live WebDAV PROPFIND requests against an active account.
- extras:
  - access_mode: registration-gated
  - free_tier_exists: yes
  - maximum_purchasable_gb: 60
  - extra_storage_is_reviewed: yes
- evidence:
  - [2] 2026-10-21: 'If the free 2GB is not enough, you can extend your cloud storage', with WebDAV and the Nextcloud clients listed as access paths
  - [3] 2026-10-21: 'FREE storage: 1GB for your emails, 2GB for the cloud, 500MB for cryptpad'; tiers '5GB for 11 EUR annually' up to '60GB for 110 EUR annually'; 'European users have to add a VAT of 21%'
  - [4] 2026-11-03: the 2026-11-02 status update says unreadable disk regions may lead to unrecoverable data | capture: sha256:b74e3374025cc3095564123843ac7dc1443115f624ec16b7ffca11c2b5869abf | quote: some unreadable region does exist on the disk which may lead to unrecoverable data
  - probe:https://disroot.org/ 2026-11-03: the site root serves a maintenance page headed Major hardware failure on storage server | capture: sha256:6eba24a8ba7d3ba0f406e93a519d38b54ad07d67aab6cd4b7a6e90c705aedebe | quote: <h1>Major hardware failure on storage server!</h1>
  - probe:https://disroot.org/en/services/nextcloud 2026-11-03: the Nextcloud service page answers HTTP 404 while the site root serves the maintenance page | capture: sha256:62bf13eba8b6b167eb8dc6cb1b111568f95198399e65f8ca9726fffb1b162a8e | quote: "status": 404
  - [3] 2026-11-25: the form page states the three free allowances | capture: sha256:02ee9c1c18e4470472ef0f880fedb71930b0632678b4e52f4bb8f735829d5c1c | quote: With your Disroot account, you get FREE storage: 1GB for your emails, 2GB for the cloud, 500MB for cryptpad.
  - [3] 2026-11-25: the form lists the annual extra-storage steps from 5GB for 11 EUR to 60GB for 110 EUR | capture: sha256:02ee9c1c18e4470472ef0f880fedb71930b0632678b4e52f4bb8f735829d5c1c | quote: 5GB for 11€ annually10GB for 20€ annually15GB for 29€ annually30GB for 56€ annually45GB for 83€ annually60GB for 110€ annually
  - [3] 2026-11-25: European users add 21% VAT to the annual prices | capture: sha256:02ee9c1c18e4470472ef0f880fedb71930b0632678b4e52f4bb8f735829d5c1c | quote: However, European users have to add a VAT (Value Added Tax) which is 21% more.
  - [5] 2026-11-25: the project states it relies on donations | capture: sha256:8f81da045ae6953027603ef617ade982754b71acd19809f2d0ec9ddb32715d83 | quote: Disroot relies on donations and support from its community and users of services.
  - [4] 2026-11-25: the status page states the Nextcloud Files feature is disabled while calendars, contacts and chat work | capture: sha256:b01a16a01a6ebe5f54142078fbad10ebb94c32de34a4f585b85d7ba6b198c59d | quote: Nextcloud - Files feature has been disabled until the issue is solved, calendars, contacts, chat etc works as normal
  - [4] 2026-11-25: the 29.10.2026 update reports one repeated unreadable sector complicating file system repair | capture: sha256:b01a16a01a6ebe5f54142078fbad10ebb94c32de34a4f585b85d7ba6b198c59d | quote: However, we seem to have one confirmed repeated unreadable sector which makes the file system repair a bit tricky.
  - [1] 2026-11-25: the first-party storage form states the free allowances in GB | capture: sha256:3e4c699608388dc5adbd72e51e3eaf1d82d50484da1a452e29c0539bc8cd42e3 | quote: With your Disroot account, you get FREE storage: 1GB for your emails, 2GB for the cloud, 500MB for cryptpad.
- sources:
  - [1] https://disroot.org/forms/extra-storage-space
  - [2] https://disroot.org/en/services/nextcloud
  - [3] https://disroot.org/en/forms/extra-storage-space
  - [4] https://status.disroot.org/
  - [5] https://disroot.org/
