# openml

> openml.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openml/ | JSON https://fshy.ajam.dev/api/v1/entity/openml.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## openml

- `storage/openml` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.276Z (live) | stale on 2026-12-04
- url https://www.openml.org/api/v1/json/data/list/limit/1
- free tier: Reachable: the OpenML dataset-list API returned JSON dataset records; it is a dataset catalogue, not a general file store. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: OpenML dataset-list API returned JSON dataset records on recheck; it is a dataset catalogue, not a general file store.
- notes: Unreachable for the entire session from this network. Openml.org, www.openml.org, api.openml.org and docs.openml.org all timed out at TCP connect (21 s, 4 attempts incl. IPv4-forced, over ~.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Unreachable for the entire session from this network — openml.org, www.openml.org, api.openml.org and docs.openml.org all timed out at TCP connect (21 s, 4 attempts incl. IPv4-forced, over…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Unreachable for the entire session from this network — openml.org, www.openml.org, api.openml.org and docs.openml.org all timed out at TCP connect 21 s, 4 attempts incl. IPv4-forced, over ~
  - [2] 2026-10-21: cited as the basis of the rejection: Unreachable for the entire session from this network — openml.org, www.openml.org, api.openml.org and docs.openml.org all timed out at TCP connect 21 s, 4 attempts incl. IPv4-forced, over ~
  - [1] 2026-11-19: the OpenML dataset-list API returned JSON dataset records on 2026-11-19 | capture: sha256:5091cb54b63d5e7a4b8b907ee32cd489cee2a74c71c34da99c1f9ab6d68ba6ae | quote: {"data":{"dataset":[
  - [1] 2026-11-19: the OpenML API is reachable on 2026-11-19 and serves dataset metadata, re-dating the record | capture: sha256:5091cb54b63d5e7a4b8b907ee32cd489cee2a74c71c34da99c1f9ab6d68ba6ae | quote: {"data":{"dataset":[
  - [1] 2026-11-19: the API answered with dataset JSON on 2026-11-19 | capture: sha256:5091cb54b63d5e7a4b8b907ee32cd489cee2a74c71c34da99c1f9ab6d68ba6ae | quote: {"data":{"dataset":[
- sources:
  - [1] https://www.openml.org/api/v1/json/data/list/limit/1
  - [2] https://api.openml.org/

## openml (200 gb per dataset)

- `storage/openml-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.276Z (live) | stale on 2026-12-04
- url https://www.openml.org/api/v1/json/data/list/limit/2
- free tier: Reachable: the OpenML dataset-list API returned two JSON dataset records; it is a dataset catalogue, not a general file store. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: OpenML dataset-list API returned dataset JSON on recheck; it is a dataset catalogue, not a general file store.
- notes: Endpoint was unreachable on 2026-10-21. Every attempt failed at the network layer. The API timed out on port 443 with curl error 28.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Every attempt failed at the network layer: the API timed out curl 28, port 443
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Every attempt failed at the network layer: the API timed out curl 28, port 443
  - [2] 2026-10-21: Every attempt failed at the network layer: the API timed out curl 28, port 443
  - [3] 2026-10-21: Every attempt failed at the network layer: the API timed out curl 28, port 443
  - [1] 2026-11-19: the OpenML dataset-list API returned dataset records on 2026-11-19 | capture: sha256:95a44caac5c956bea50c2d09d367c46cbe9a3888bc839e6022eb80e35b59b205 | quote: "name":"kr-vs-kp"
  - [1] 2026-11-19: the OpenML API is reachable on 2026-11-19 and serves dataset metadata, re-dating the record | capture: sha256:95a44caac5c956bea50c2d09d367c46cbe9a3888bc839e6022eb80e35b59b205 | quote: "name":"kr-vs-kp"
  - [1] 2026-11-19: the API answered with dataset records on 2026-11-19 | capture: sha256:95a44caac5c956bea50c2d09d367c46cbe9a3888bc839e6022eb80e35b59b205 | quote: "name":"kr-vs-kp"
- sources:
  - [1] https://www.openml.org/api/v1/json/data/list/limit/2
  - [2] https://docs.openml.org/concepts/authentication/
  - [3] https://neurips.cc/Conferences/2026/EvaluationsDatasetsHosting
