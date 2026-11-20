# Play with Docker

> play-with-docker.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/play-with-docker/ | JSON https://fshy.ajam.dev/api/v1/entity/play-with-docker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Play with Docker

- `compute/play-with-docker` | dead | evidence documented | binding retention-clamped | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://labs.play-with-docker.com/
- free tier: no longer available: Play with Docker is unavailable starting 2026-03-01 | unit: none | metered on: wall-clock | read on: 2026-10-06 | source: [1] | note: this was the canonical anonymous free VM in every list older than 2026-03
- per-object cap: not applicable
- retention: the service is withdrawn | days: 0 | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: was anonymous; the service is withdrawn
- interface: ssh
- limits:
  - retention-clamped (binding): unavailable from 2026-03-01 [1]
- limits note: a 4-hour session was the historical limit
- binding note: the service is unavailable from 2026-03-01, so the withdrawal is the end of it
- interface detail: was a browser terminal with Docker-in-Docker
- tooling: was docker and docker compose in a browser tab
- composes with: none: withdrawn
- reliability: no reliability event recorded
- notes: The deprecation notice is on the playground host, not on docs.docker.com, and the Markdown rendering of the playground page drops it: the page still returns 200 with the playground description. Reading the status code or the rendered text finds a live product. The raw HTML carries the notice.
- extras:
  - billing_model: flat-pool
  - free_tier_kind: none
- evidence:
  - [2] 2026-10-22: 'Deprecation notice: Play with Docker will be unavailable starting March 1, 2026', read from the raw HTML. The Markdown extraction of the same page drops the notice and returns only the playground description
  - [1] 2026-10-22: no match for 'Play with Docker' or 'unavailable'
- sources:
  - [1] https://docs.docker.com/
  - [2] https://labs.play-with-docker.com/
