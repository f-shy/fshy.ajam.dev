# Panoramax federation

> panoramax.xyz | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/panoramax/ | JSON https://fshy.ajam.dev/api/v1/entity/panoramax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Panoramax federation — 25 instances with per-instance `registration_is_open` (ulm / osm-es / seespider / panoramax-ar / osm-hr / osm-be)

- `storage/panoramax-federation-25-instances-with-per-instance-regi` | qualifies | evidence reported | binding none | category federated instance pool
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://api.panoramax.xyz/api/instances
- free tier: No quota on any instance (same codebase, same absence of a quota mechanism). The federation catalog itself is the useful artifact: `GET /api/instances` returns all 25 instances WITH each one's live configuration, including `registration_is_open`. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: each instance serves its own originals, unmetered, no auth | metered: no
- identity: email | detail: email (OSM OAuth for most; Keycloak self-registration for seespider at auth.pycnogon.xyz; osm-es declares `user_profile.url = null`, i.e. its own local accounts)
- interface: cli
- limits note: Geo_coverage is enforced socially, not technically. IGN instance demands French territory; panorama.wales demands Wales; pano.locus.sbs demands US-NW. `panoramax-ulm.jjbaur.de` is the outlier: its config says verbatim 'Worldwide — The picture can be sent from anywhere in the world.'.
- interface detail: One shared STAC/OGC API shape across every instance. The same client works against all of them.
- tooling: panoramax_cli --api-url <instance>; `panoramax_cli transfer` moves a sequence between instances without re-uploading from disk
- composes with: Round-robin writes across the open instances; the federated meta-catalog at api.panoramax.xyz indexes all of them, so one search call sees every copy. Multiply capacity by instance count.
- reliability: Open=False on 11 of 25 instances (multimodall, bikespace, nl-test, osm-fulda, vee, multimob, serenedeluge, burakonder, mapcomplete, osm-tw). Two instances (mahdi, kasik-gis) have auth disabled entirely. Anonymous read, no upload path.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 25 instances enumerated, each with configuration.auth.registration_is_open
  - [2] 2026-10-21: registration_is_open: true, geo_coverage 'Worldwide\nThe picture can be sent from anywhere in the world.'
  - [3] 2026-10-21: registration_is_open true, own Keycloak realm, 'Photos must be located in France'
  - [4] 2026-10-21: registration_is_open true, user_profile.url = null (instance-local accounts)
- sources:
  - [1] https://api.panoramax.xyz/api/instances
  - [2] https://panoramax-ulm.jjbaur.de/api/configuration
  - [3] https://panoramax.ign.fr/api/configuration
  - [4] https://panoramax.openstreetmap.es/api/configuration
