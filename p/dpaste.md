# dpaste.org

> dpaste.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dpaste/ | JSON https://fshy.ajam.dev/api/v1/entity/dpaste.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dpaste.org

- `storage/dpaste-org` | fails-quota | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dpaste.org
- free tier: approx. 1 MiB per paste (measured: 1,040,000 chars accepted, 1,133,336 chars -> HTTP 413). No account, no quota, no count limit observed. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free direct GET, no metering, no redirect; pastes served as HTML with a raw path. | metered: no
- identity: institution
- interface: rest
- limits note: ~1 MiB per paste; expiry options 1 hour to never; no delete without the deletion key; a report about excess use routes to the operator.
- interface detail: rest
- tooling: curl -X POST -F 'format=url' -F 'content=<file' https://dpaste.org/api/ returns a plain URL. dpaste is the open-source Django app (github.com/bartTC/dpaste), so the same client works against any instance in the network.
- composes with: unlimited anonymous pastes x ~1 MiB. Cross-instance: dpaste.org, dpaste.com, dpaste.de and any self-hosted dpaste all share one API shape, so the same shard writer hits N independent operators. 1 TiB = ~1M pastes; only sane as a metadata/thumbnail tier.
- reliability: Stable across a dozen API calls with no throttling observed. The URL slug is only 4 characters by default (SLUG_LENGTH=4), so paste URLs are enumerable. Do not treat content as private without local encryption.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: approx. 1 MiB per paste (measured: 1,040,000 chars accepted, 1,133,336 chars -> HTTP 413). No account, no quota, no count limit observed.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'POST /api/ ... returns the full URL that snippet was created'; form parameters content, lexer
  - [2] 2026-10-21: probe: curl -X POST -F format=url -F 'content=<dd.txt' -> 1,040,000 chars = 200; 1,133,336 chars = 413 Request Entity Too Large
  - [3] 2026-10-21: probe: GET -> 200, bytes=3023518 (666,668-char payload stored and served in full)
- sources:
  - [1] https://docs.dpaste.org/api/
  - [2] https://dpaste.org/api/
  - [3] https://dpaste.org/GWLh0
