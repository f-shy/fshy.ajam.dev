# Shadow Drive

> shadow.tech | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shadow/ | JSON https://fshy.ajam.dev/api/v1/entity/shadow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shadow Drive (Blade, France)

- `netdisk-pan/shadow-drive` | fails-quota | evidence reported | binding per-object-cap | category hosted Nextcloud, freemium
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T00:20:59.761Z (inherited) | stale on 2026-11-19
- url https://shadow.tech/eu/drive/offers/
- free tier: 20 GB free; Basic 200 GB at EUR 2.99/month; Premium 2 TB at EUR 6.99/month. Every tier carries the same 'Upload up to 20 GB' line | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 GB per upload on every plan, including the 2 TB one | bytes: 20000000000 | source: [1] | note: the vendor writes 20 GB; the decimal figure is used as stated
- retention: Until deleted. No retention clock published | source: [1]
- egress: Not metered in the offer table | metered: no | source: [1]
- identity: card | detail: a card, and a billing address in one of twelve countries: France, the United Kingdom, Belgium, Switzerland, Luxembourg, Germany, the Netherlands, Austria, Italy, Sweden, Denmark and Spain | country: FR, GB, BE, CH, LU, DE, NL, AT, IT, SE, DK, ES
- interface: webdav, rest, rclone
- limits:
  - per-object-cap (binding): 20 GB per upload on every tier including 2 TB [1]
- binding note: The free 20 GB is an order of magnitude under a 500 GB threshold, and the paid tiers carry a 20 GB per-file cap that does not move with the plan. Either number alone stops it; the cap is the one that would still bind at 2 TB.
- tooling: rclone webdav against /remote.php/webdav/, which answers 401 with a Basic realm of 'Shadow Drive'. Standard Nextcloud clients
- composes with: The cheapest Enterprise-build Nextcloud in Europe at EUR 2.99 for 200 GB, so it is a candidate small shard. The 20 GB per-file cap is uniform across tiers and does not scale, which stops it being an archive target
- reliability: Signup is geo-fenced to twelve countries. Encryption at rest is still listed as not implemented. The price rose from EUR 4.99 to EUR 6.99 for 2 TB since the 2024 announcement while press coverage still quotes the old figure
- notes: The free 20 GB is real and it is the same Enterprise build as the paid tiers, so it works as a cheap test endpoint. It fails as capacity on size, and it fails on a per-file cap that never improves.
- evidence note: Confidence is reported: pricing and status endpoints were documented from research records. Verification requires live re-reading of current pricing pages and Nextcloud WebDAV endpoints.
- extras:
  - access_mode: registration-gated
  - free_tier_exists: yes
  - geo_fenced_countries: 12
  - per_file_cap_bytes_derived: 20000000000
  - nextcloud_version: 27.1.11 Enterprise
- evidence:
  - [1] 2026-10-21: 'Free 20 GB ... Upload up to 20 GB', 'Basic 200 GB ... 2.99 EUR/month', 'Premium 2 TB ... 6.99 EUR/month', all three with the same 20 GB upload line, and 'Shadow Drive is already available in 12 countries: France, UK, Belgium, Switzerland, Luxemburg, Germany, Netherlands, Austria, Italy, Sweden, Denmark and Spain'
  - [2] 2026-10-21: HTTP 200, version 27.1.11.4, versionstring '27.1.11 Enterprise', productname Nextcloud
  - [3] 2026-10-21: OPTIONS returned HTTP 401 with WWW-Authenticate: Basic realm="Shadow Drive"
  - [1] 2026-11-03: the Basic plan is a 200 GB offer | capture: sha256:ca530d4fabc396c1f36fc76cccb340a9ae0763e619b54fa5f93d031ce7f041bb | quote: <strong><span>200 GB</span></strong>
  - [1] 2026-11-03: the Premium plan is a 2 TB offer | capture: sha256:ca530d4fabc396c1f36fc76cccb340a9ae0763e619b54fa5f93d031ce7f041bb | quote: <strong><span>2 TB</span></strong>
  - [1] 2026-11-03: the Basic plan button reads Subscribe at 2.99 per month | capture: sha256:ca530d4fabc396c1f36fc76cccb340a9ae0763e619b54fa5f93d031ce7f041bb | quote: Subscribe at 2.99
  - [1] 2026-11-03: the Premium plan button reads Subscribe at 6.99 per month | capture: sha256:ca530d4fabc396c1f36fc76cccb340a9ae0763e619b54fa5f93d031ce7f041bb | quote: Subscribe at 6.99
  - [4] 2026-11-03: the product page offers 20 GB free for life | capture: sha256:4edf5ad86b62a3cb7ffcf4a6b1371b94ed99340361dee229313e84d78cb21cbe | quote: Enjoy 20 GB free (for life!)
  - [1] 2026-11-03: the FAQ lists the twelve countries where Shadow Drive can be subscribed | capture: sha256:7af5fc4777b4b6d25d917556400c1b7a5ed078d75356a884096d4cb0aa4b975f | quote: Shadow Drive is already available in 12 countries: France, UK, Belgium, Switzerland, Luxemburg, Germany, Netherlands, Austria, Italy, Sweden, Denmark and Spain.
  - [1] 2026-11-03: the FAQ still says encryption at rest is being worked on | capture: sha256:7af5fc4777b4b6d25d917556400c1b7a5ed078d75356a884096d4cb0aa4b975f | quote: At rest: Shadow Drive Teams are currently working on encryption at rest to strengthen the overall security of our solution.
  - probe:https://drive.shadow.tech/status.php 2026-11-03: the drive host answers the Nextcloud 27.1.11.4 status JSON, installed and not in maintenance | capture: sha256:263ef38322034768118919a7c300d79ba2da5e2dc9b9b1b26ece124593fb3ad4 | quote: "version":"27.1.11.4"
  - probe:https://drive.shadow.tech/remote.php/dav/ 2026-11-03: the WebDAV endpoint answers a SabreDAV NotAuthenticated error, a live auth-gated WebDAV server | capture: sha256:4ad43d022695535b35e042e186b21a160f37829e8d7404d74c8ff0085d7a4c3b | quote: Sabre\DAV\Exception\NotAuthenticated
  - [1] 2026-11-03: every plan on the offers page carries the Upload up to 20 GB line | capture: sha256:ca530d4fabc396c1f36fc76cccb340a9ae0763e619b54fa5f93d031ce7f041bb | quote: Upload up to 20 GB
- sources:
  - [1] https://shadow.tech/eu/drive/offers/
  - [2] https://drive.shadow.tech/status.php
  - [3] https://drive.shadow.tech/remote.php/dav/
  - [4] https://shadow.tech/eu/drive/
