# xeno-canto

> xeno-canto.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xeno-canto/ | JSON https://fshy.ajam.dev/api/v1/entity/xeno-canto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xeno-canto (bird sound archive)

- `storage/xeno-canto` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:33.472Z (inherited) | stale on 2026-12-04
- url https://xeno-canto.org/api/3/recordings?query=cnt:%22Common%20Blackbird%22
- free tier: none reachable: the API docs at /explore/api are readable and state that API v3 requires an API key held by registered XC members with a verified email address; /api/3/recordings without a key returns HTTP 401 | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: signup gate: API key requires a registered XC member with a verified email address; no account created
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Both the API and every documentation page sit behind an Anubis proof-of-work wall. `/api/3/recordings` without a key returns 401 asking for a `key` parameter, and /explore/api +…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Both the API and every documentation page sit behind an Anubis proof-of-work wall. `/api/3/recordings` without a key returns 401 asking for a `key` parameter, and /explore/api +…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both the API and every documentation page sit behind an Anubis proof-of-work wall. `/api/3/recordings` without a key returns 401 asking for a `key` parameter, and /explore/api +…
  - [2] 2026-10-21: cited as the basis of the rejection: Both the API and every documentation page sit behind an Anubis proof-of-work wall. `/api/3/recordings` without a key returns 401 asking for a `key` parameter, and /explore/api + /about/uploa
  - probe:https://xeno-canto.org/explore/api 2026-11-19: the docs are readable and the gate is a registered-member API key, not a proof-of-work wall | capture: sha256:f4b6f7a0460277367bb4c2a21399d569b604bb94d0af7866127de21c97d38e90 | quote: The API now requires an API key. Every XC member with a verified email address already has one.
  - probe:https://xeno-canto.org/explore/api 2026-11-19: using the API requires registering an account with a verified email address | capture: sha256:f4b6f7a0460277367bb4c2a21399d569b604bb94d0af7866127de21c97d38e90 | quote: you will need to register first to use API v3
  - probe:https://xeno-canto.org/explore/api 2026-11-19: every API call requires the registered-member key; the docs page itself is readable | capture: sha256:f4b6f7a0460277367bb4c2a21399d569b604bb94d0af7866127de21c97d38e90 | quote: you will need to append your key to every API call
  - probe:https://xeno-canto.org/api/3/recordings 2026-11-19: the recordings API endpoint answers HTTP 401 without a key | capture: sha256:2af7d485e655f8b702babb1d13c060f79bd14308ed64740de75b611892b620b6 | quote: "status": 401
- sources:
  - [1] https://xeno-canto.org/api/3/recordings?query=cnt:%22Common%20Blackbird%22
  - [2] https://xeno-canto.org/explore/api
