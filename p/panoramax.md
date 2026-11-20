# Panoramax federation

> panoramax.xyz | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/panoramax/ | JSON https://fshy.ajam.dev/api/v1/entity/panoramax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Panoramax federation — 25 instances with per-instance `registration_is_open` (ulm / osm-es / seespider / panoramax-ar / osm-hr / osm-be)

- `storage/panoramax-federation-25-instances-with-per-instance-regi` | qualifies | evidence reported | binding none | category federated instance pool
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:14:36.639Z (live) | stale on 2026-12-04
- url https://api.panoramax.xyz/api/instances
- free tier: unverified: the /api/instances page returns a JSON array of instance objects carrying configuration.auth.registration_is_open; it states no storage quota. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: each instance serves its own originals, unmetered, no auth | metered: no
- identity: email | detail: email (OSM OAuth for most; Keycloak self-registration for seespider at auth.pycnogon.xyz; osm-es declares `user_profile.url = null`, i.e. its own local accounts)
- interface: cli
- limits note: Geo_coverage is enforced socially, not technically. IGN instance demands French territory; panorama.wales demands Wales; pano.locus.sbs demands US-NW. `panoramax-ulm.jjbaur.de` is the outlier: its config says verbatim 'Worldwide — The picture can be sent from anywhere in the world.'.
- interface detail: One shared STAC/OGC API shape across every instance. The same client works against all of them.
- tooling: panoramax_cli --api-url <instance>; `panoramax_cli transfer` moves a sequence between instances without re-uploading from disk
- composes with: Round-robin writes across the open instances; the federated meta-catalog at api.panoramax.xyz indexes all of them, so one search call sees every copy. Multiply capacity by instance count.
- reliability: unverified: the /api/instances page lists a different set of open and closed instances than the record's counts; it states no storage quota.
- notes: unverified: the /api/instances page returns a JSON array of instance objects carrying configuration.auth.registration_is_open; its membership differs from the instances the record names and it states no storage quota.
- evidence:
  - [1] 2026-10-21: 25 instances enumerated, each with configuration.auth.registration_is_open
  - [2] 2026-10-21: registration_is_open: true, geo_coverage 'Worldwide\nThe picture can be sent from anywhere in the world.'
  - [3] 2026-10-21: registration_is_open true, own Keycloak realm, 'Photos must be located in France'
  - [4] 2026-10-21: registration_is_open true, user_profile.url = null (instance-local accounts)
  - [1] 2026-11-11: the page is a JSON catalogue whose instances array contains instance objects | capture: sha256:c9e9d167122ffb0557a235458181319b0a773ac69f4b7d91d3ed26b8909338a5 | quote: "instances":[{"id":"4adfe644-eefc-4f83-97a5-a65828280757","name":"multimodall","url":"https://panoramax.multimodall.com"
  - [1] 2026-11-19: the /api/instances page is a JSON catalogue whose membership now lists a us-ne instance, differing from the instances the record names | capture: sha256:109b4eaefc8574e17b765cd308e64cebc71ebfa2d6c5f615eb39d36413a7ca17 | quote: "name":"us-ne","url":"https://panoramax.horatio.us"
- sources:
  - [1] https://api.panoramax.xyz/api/instances
  - [2] https://panoramax-ulm.jjbaur.de/api/configuration
  - [3] https://panoramax.ign.fr/api/configuration
  - [4] https://panoramax.openstreetmap.es/api/configuration
