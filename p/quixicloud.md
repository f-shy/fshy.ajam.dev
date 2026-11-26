# QuixiCloud

> quixicloud.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quixicloud/ | JSON https://fshy.ajam.dev/api/v1/entity/quixicloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## QuixiCloud

- `netdisk-pan/quixicloud` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cheap managed cloud, ZFS-backed, Cloudreve-family front end
- needs card no, phone no, ID no, institution no | verified 2026-11-25T14:05:44.507Z (inherited) | stale on 2026-12-10
- url https://quixicloud.com
- price USD 1.42/TB/month on the 2 TB plan at USD 33.99/yr, and USD 1.56/TB/month on 6 TB at USD 112.49/yr | parsed USD 1.42/TB-mo
- free tier: 10 GB free forever with no payment required. Paid annually: 100 GB at USD 6.79, 500 GB at USD 13.49, 2 TB at USD 33.99, 6 TB at USD 112.49, one user and no per-seat fee | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB on the 100 GB tier, 10 GB on 500 GB, 15 GB on 2 TB and 20 GB on 6 TB, so the cap rises with the tier and never clears 20 GB | bytes: 20000000000 | source: [1]
- retention: At Day 60, primary storage data is permanently deleted. | source: [1]
- egress: Not metered in the published plan table; unlimited devices, WebDAV mounting and rclone are bundled into every paid tier | metered: no | source: [1]
- identity: email | detail: an email address. The free 10 GB plan needs no payment method
- interface: webdav, s3, rest, rclone
- limits:
  - per-object-cap (binding): 20GB (6TB plan) [1]
  - write-gated: the front end is a Cloudreve fork and its /api/v3 endpoints return 404, so stock Cloudreve tooling does not apply [2]
- tooling: rclone webdav and rclone s3. The drive host answers OPTIONS with DAV: 1, 2 and Allow: OPTIONS, LOCK, PUT, MKCOL, so the WebDAV server is real. A REST sync API and Windows, macOS and Android apps exist
- composes with: Priced at USD 1.42 per TB per month on the 2 TB tier. WebDAV and S3 API support without egress bandwidth fees provides cost-effective secondary storage under fronting caches.
- reliability: Indian-operated with INR billing and Mumbai, Bengaluru and Delhi regions. The app., my. and cloud. subdomains do not resolve, so only drive.quixicloud.com is live and the marketing site is ahead of the DNS. The front end is Cloudreve-derived and its /api/v3 endpoints 404, so it is a fork and not stock Cloudreve
- notes: The best price per terabyte found anywhere in this topic, from an operator with a marketing site ahead of its DNS and a forked front end. Two things are unproven: that the no-egress-line claim survives contact, and that a 6 TB plan is provisioned as advertised. A 10 GB free tier needs no card, so both can be tested before paying.
- extras:
  - access_mode: registration-gated
  - free_tier_exists: yes
  - free_tier_bytes: 10
  - front_end: a Cloudreve fork, /api/v3 returns 404
  - dns_defect: app., my. and cloud. subdomains do not resolve; only drive.quixicloud.com answers
  - per_file_caps_bytes_derived.100GB_tier: 5000000000
  - per_file_caps_bytes_derived.500GB_tier: 10000000000
  - per_file_caps_bytes_derived.2TB_tier: 15000000000
  - per_file_caps_bytes_derived.6TB_tier: 20000000000
- evidence:
  - [1] 2026-10-21: the full annual plan table: '2TB Cloud Storage, USD 34/year', 'Start Free, 10 GB, USD 0 forever. No payment required', and the per-tier single-file limits
  - probe:https://drive.quixicloud.com/dav/ 2026-10-21: OPTIONS returned HTTP 200 with Allow: OPTIONS, LOCK, PUT, MKCOL and dav: 1, 2, so the WebDAV write surface is live; a GET returned 401 with 0 bytes
  - probe:https://drive.quixicloud.com/session 2026-10-21: HTTP 200, a real login and registration app offering 'zero-knowledge, end-to-end encrypted cloud storage'
  - [3] 2026-10-21: the same product with India pricing, 2 TB from INR 3,249/yr, and Mumbai, Bengaluru and Delhi regions
  - [1] 2026-11-03: the 100 GB annual plan is listed at $6.79 a year | capture: sha256:b9b3843e5014aa3d776b93c963f47e09c06beb916764a922b69862ca4cb11722 | quote: $6.79 / year
  - [1] 2026-11-03: the 500 GB annual plan is listed at $13.49 a year | capture: sha256:b9b3843e5014aa3d776b93c963f47e09c06beb916764a922b69862ca4cb11722 | quote: $13.49 / year
  - [1] 2026-11-03: the 6 TB annual plan is listed at $112.49 a year | capture: sha256:b9b3843e5014aa3d776b93c963f47e09c06beb916764a922b69862ca4cb11722 | quote: $112.49 / year
  - [1] 2026-11-25: the annual per-file limits are unchanged up to 20 GB on the 6 TB plan | capture: sha256:993b8f2437d0a14ddaf14a333580e6eaad01e343323a835c6d51d40b336ba260 | quote: Single-file upload limits range from 2GB on monthly plans to 5GB (100GB plan), 10GB (500GB plan), 15GB (2TB plan), and 20GB (6TB plan) on annual tiers.
  - [1] 2026-11-25: the 2 TB annual price is still USD 33.99 | capture: sha256:993b8f2437d0a14ddaf14a333580e6eaad01e343323a835c6d51d40b336ba260 | quote: $33.99 / year
  - [1] 2026-11-25: the free 10 GB tier still needs no payment | capture: sha256:993b8f2437d0a14ddaf14a333580e6eaad01e343323a835c6d51d40b336ba260 | quote: $0 forever. No payment required.
  - [3] 2026-11-25: the Indian signup still offers 10 GB with no card | capture: sha256:9d6a2be68e0eb768b23375498b93731479d7cf84b71ec1773da419dfaf450e9b | quote: Sign up and get 10GB instantly — no credit card required.
  - probe:https://drive.quixicloud.com/dav/ 2026-11-25: the DAV endpoint is still live and auth-gated behind a cloudreve realm | capture: sha256:1ad5c0e8d3bcd6dc660f4ac92f5d7579d7a0fa897b96bb3d177845360b9ced89 | quote: "status": 401
  - [3] 2026-11-25: primary storage data is permanently deleted at Day 60 after plan expiry, so a retention clock is published | capture: sha256:9d6a2be68e0eb768b23375498b93731479d7cf84b71ec1773da419dfaf450e9b | quote: At Day 60, primary storage data is permanently deleted.
- sources:
  - [1] https://quixicloud.com/
  - [2] https://drive.quixicloud.com/dav/
  - [3] https://quixicloud.in/
