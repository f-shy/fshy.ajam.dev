# PlayHT

> play.ht | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/play/ | JSON https://fshy.ajam.dev/api/v1/entity/play.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PlayHT / PlayAI

- `compute/playht-playai` | dead | evidence measured | binding none | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-12-07
- url https://play.ht/pricing/
- free tier: No offer: the service is gone. Meta acquired the PlayAI team in July 2025 and the platform was switched off at the end of 2025. Measured on 2026-10-22: the resolver returns the name play.ht with no address record, and api.play.ht returns 'Non-existent domain'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none-withdrawn
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: anonymous
- interface: rest
- limits note: nothing binds because nothing answers: no credential can be issued and no endpoint resolves, so any tutorial that still recommends PlayHT for a free TTS tier sends its reader to a dead domain.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: nothing composes with a dead provider. The replacement in documented records is Cartesia or ElevenLabs for dialogue-capable TTS, both recorded separately among documented hosts.
- reliability: no reliability event recorded
- notes: PlayHT API and platform services have been discontinued following corporate acquisition, and domain endpoints return NXDOMAIN.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: none-withdrawn
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: nslookup returned 'Name: play.ht' with no address record, and nslookup api.play.ht returned 'Non-existent domain' [receipt: dns:play.ht]
  - [1] 2026-10-22: 
  - [1] 2026-10-22: the nearest Wayback capture returned timestamp 20260210213038 with status 522 and record_length 686, an error page rather than a pricing table
  - [2] 2026-10-22: 'Dec 31, 2025 PlayAI platform and services officially shut down completely' and 'July 26, 2025 Public API services began winding down following the Meta acquisition', reported
  - [3] 2026-10-22: Meta confirmed the acquisition of the team on 13 July 2025 and the voice API was deprecated within weeks; 'as of 22 September 2026 the play.ht domain still returns no DNS record at all', reported and corroborated by the DNS check
- sources:
  - [1] https://play.ht/pricing/
  - [2] https://www.everydev.ai/developers/play-ai
  - [3] https://getcartsignal.com/tools/playht
