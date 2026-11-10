# DanubeData Storage Share

> danubedata.ro | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/danubedata/ | JSON https://fshy.ajam.dev/api/v1/entity/danubedata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DanubeData Storage Share (managed Nextcloud)

- `netdisk-pan/danubedata-storage-share` | qualifies | evidence documented | binding request-rate | category managed Nextcloud, paid only
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T04:06:37.166Z (live) | stale on 2026-11-13
- url https://docs.danubedata.ro/storage-share
- price EUR 4.99/TB/month at 1 TB falling to EUR 3.00/TB/month at 10 TB, read 2026-10-22 | parsed USD 3.38/TB-mo
- free tier: No free tier. Three resource profiles: DD1 Sulina 1 TB at EUR 4.99/month, DD5 Sf. Gheorghe 5 TB at EUR 14.99, DD10 Chilia 10 TB at EUR 29.99 | unit: TiB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: Not published as a per-file cap. The published per-profile numbers are subdomains and concurrent connections: 3 and 50, 7 and 100, 10 and 200 | source: [1] | note: The docs say 'S3-backed storage, up to 10 TB of object storage per instance', which is the instance total and not a per-object ceiling
- retention: Until deleted. The instance lifecycle is Pending, Provisioning, Running, Error, Destroying, with redeploy from Error. No retention clock is documented | source: [1]
- egress: No egress price and no traffic quota are published anywhere in the vendor documentation, so this field is false by the schema's own definition (false when traffic out has neither a price nor a quota) and not because the vendor granted anything. The instance is S3-backed and DanubeData sells object storage separately, so a traffic line may exist behind the Nextcloud facade and the docs do not say | metered: no | source: [1]
- identity: card | detail: a DanubeData account and a payment method. The docs do not describe the signup gate
- interface: webdav, rest, s3
- limits:
  - request-rate (binding): 50, 100 or 200 concurrent connections depending on the profile [1]
- binding note: The only published numbers that can bind are the concurrent-connection caps, because the traffic terms are unstated and the per-file cap is unstated. 50 connections on the 1 TB profile is ample for a copy job and thin for a serving path.
- tooling: a WebDAV endpoint on every profile, the Nextcloud clients, and one-scan QR setup for iOS and Android. S3-backed means the same bytes are in an object store, so an S3 tool may reach them without a second copy, but the docs do not publish the bucket
- composes with: S3-backed Nextcloud is the cleanest architecture of the four: the bytes live in an object store behind a Nextcloud facade, so either access path should reach the same copy. Ten subdomains per instance is an unusual sharding affordance and it is the only reseller here that offers it
- reliability: Falkenstein, Germany, the same data centre as Hetzner, so the failure domain is shared with the Hetzner option. Dedicated CPU and memory per instance, automatic TLS renewal. The product is young and the documentation is thin: the WebDAV page returned 404 when requested
- notes: The cheapest 10 TB managed Nextcloud of the five at EUR 3.00/TB/month, and the only one whose storage is documented as an object store behind the Nextcloud facade. Two things are unverified that a buyer needs: the traffic terms, and whether the S3 backend is reachable with credentials the customer holds. The docs describe the second as a property of the product and publish no endpoint.
- evidence note: Prices and profile numbers are from the vendor's own table read. `documented` at best: the traffic terms and the per-file cap are published nowhere, so the egress field carries a null `metered` rather than a guess.
- extras:
  - access_mode: paid
  - free_tier_exists: no
  - region: Falkenstein, Germany
  - tier_prices_eur_month.DD1_1TB: 4.99
  - tier_prices_eur_month.DD5_5TB: 14.99
  - tier_prices_eur_month.DD10_10TB: 29.99
  - connections_per_profile.DD1: 50
  - connections_per_profile.DD5: 100
  - connections_per_profile.DD10: 200
  - subdomains_per_instance.DD1: 3
  - subdomains_per_instance.DD5: 7
  - subdomains_per_instance.DD10: 10
  - vat_position: the price table does not state whether VAT is included
  - nextcloud_version: 32
- evidence:
  - [1] 2026-10-22: the profile table reads 'DD1 Sulina 1 TB 3 50 EUR 4.99', 'DD5 Sf. Gheorghe 5 TB 7 100 EUR 14.99', 'DD10 Chilia 10 TB 10 200 EUR 29.99'
  - [1] 2026-10-22: 'Managed Nextcloud 32', 'S3-backed storage, up to 10 TB of object storage per instance', 'All profiles include ... WebDAV endpoint', 'EU data residency, all data stored in Falkenstein, Germany'
  - [1] 2026-10-22: the instance lifecycle is documented as Pending, Provisioning, Running, Error, Destroying, with redeploy from Error, and status is pushed over WebSocket
  - [2] 2026-10-22: this path returned 404 'The documentation page you're looking for doesn't exist yet', so the WebDAV endpoint is claimed in the profile table and not documented separately
- sources:
  - [1] https://docs.danubedata.ro/storage-share
  - [2] https://docs.danubedata.ro/storage-share/webdav
