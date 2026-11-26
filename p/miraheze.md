# miraheze

> miraheze.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/miraheze/ | JSON https://fshy.ajam.dev/api/v1/entity/miraheze.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## miraheze

- `storage/miraheze` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.012Z (live) | stale on 2026-12-04
- url https://meta.miraheze.org/w/api.php?action=query&meta=siteinfo
- free tier: None reachable: Quota was the best in the niche. FAQ (archived 2026-06-04) says 'There are no hard limits except "be reasonable"' on wiki storage. But the entire farm is OFFLINE today. meta.miraheze.org,. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not stated on https://meta.miraheze.org/wiki/FAQ | source: [1] | note: not applicable
- retention: not stated on https://meta.miraheze.org/wiki/FAQ | source: [1]
- egress: not stated on https://meta.miraheze.org/wiki/FAQ | metered: no
- identity: email
- interface: browser
- interface detail: MediaWiki wiki served over the web; a MediaWiki Action API answers with JSON.
- tooling: not documented
- composes with: Not stated on https://meta.miraheze.org/wiki/FAQ; wikis must not serve primarily as a file host.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Quota was the best in the niche — FAQ (archived 2026-06-04) says 'There are no hard limits except "be reasonable"' on wiki storage — but the entire farm is OFFLINE today. meta.miraheze.org,
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Quota was the best in the niche — FAQ (archived 2026-06-04) says 'There are no hard limits except "be reasonable"' on wiki storage — but the entire farm is OFFLINE today. meta.miraheze.org
  - withheld 2026-10-21: cited as the basis of the rejection: Quota was the best in the niche — FAQ (archived 2026-06-04) says 'There are no hard limits except "be reasonable"' on wiki storage — but the entire farm is OFFLINE today. meta.miraheze.org
  - [2] 2026-10-21: cited as the basis of the rejection: Quota was the best in the niche — FAQ (archived 2026-06-04) says 'There are no hard limits except "be reasonable"' on wiki storage — but the entire farm is OFFLINE today. meta.miraheze.org
  - [1] 2026-11-19: the first-party siteinfo API answers with a live 2026-11-19 timestamp, so the farm is online, not offline | capture: sha256:3d43c888897343f15b2251e5588369fced74c57c30eddd85c51a1b30dc6a6bea | quote: "time": "2026-11-19T15:25:37Z",
  - [3] 2026-11-19: the live FAQ rules out general file hosting, so the service is alive but unusable for this purpose rather than dead | capture: sha256:492da5d9be0ba2a7168a55e1da1215175e792f6b95c9039eff072dfacc7ae27c | quote: Wikis cannot be used primarily as a file host.
  - [3] 2026-11-19: the interface is a web wiki running MediaWiki | capture: sha256:492da5d9be0ba2a7168a55e1da1215175e792f6b95c9039eff072dfacc7ae27c | quote: Miraheze uses MediaWiki, the same software that powers Wikipedia
  - [1] 2026-11-19: a MediaWiki Action API answers with JSON | capture: sha256:af66343b65f42a46960d29badf00ea00350b232f2d06b87d1f1a6f3536144671 | quote: Specify the format parameter to change the output format. To see the non-HTML representation of the JSON format, set format=json.
  - [3] 2026-11-19: the FAQ gives a storage-use rule but states no numeric retention period, per-object cap or chaining terms | capture: sha256:492da5d9be0ba2a7168a55e1da1215175e792f6b95c9039eff072dfacc7ae27c | quote: There are no hard limits except "be reasonable".
- sources:
  - [1] https://meta.miraheze.org/w/api.php?action=query&meta=siteinfo
  - [2] https://web.archive.org/web/20260604152708/https://meta.miraheze.org/wiki/FAQ
  - [3] https://meta.miraheze.org/wiki/FAQ
