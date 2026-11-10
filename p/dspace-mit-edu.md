# DSpace 7+ platform class

> dspace.mit.edu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dspace-mit-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/dspace-mit-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DSpace 7+ platform class (MIT, UCT, demo.dspace.org and ~3,485 registered sites)

- `storage/dspace-7-platform-class` | fails-identity | evidence reported | binding none | category academic repository / DSpace 7.x–10.2
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dspace.mit.edu
- free tier: NO QUOTA CONCEPT AT ALL. The string 'quota' does not appear once in DSpace's 2,125-line dspace.cfg; the only two hits repo-wide are a Solr query-parser class and a discovery.cfg comment. There is no per-user, per-collection or per-installation storage limit in the software. The only byte constraint is a per-request multipart limit. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 512 MB/file | bytes: 512000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: institution | detail: institution
- interface: rest, cli
- limits:
  - per-object-cap: 512 MB/file [1]
- limits note: per-object-cap 512 MB/file in DSpace 7+ (spring.servlet.multipart.max-file-size = 512MB, max-request-size = 512MB). DSpace 6 and below used upload.max, which accepts -1 for 'no limit'.
- interface detail: REST (/server/api), OAI-PMH, SWORD
- tooling: curl / dspace CLI / OAI-PMH harvesters
- composes with: Unbounded by construction. But every instance's write path is affiliation-gated in practice, and the registry is dominated by pre-7 installs with no REST API at all.
- reliability: 60 of 60 sampled registry sites returned no /server/api/info, i.e. they are DSpace 6 or earlier and expose no modern REST API. The registry is a lagging indicator of what is programmatically usable.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: NO QUOTA CONCEPT AT ALL. The string 'quota' does not appear once in DSpace's 2,125-line dspace.cfg; the only two hits repo-wide are a Solr query-parser class and a discovery.cfg comment. There is no per-user, per-collection or per-installation storage limit in the software. The only byte constraint is a per-request multipart limit.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'spring.servlet.multipart.max-file-size = 512MB' and 'max-request-size = 512MB'
  - [3] 2026-10-21: 2,125 lines, zero occurrences of 'quota'
  - [4] 2026-10-21: total_count 2, both unrelated (dspace-api/.../core/Utils.java, dspace/config/modules/discovery.cfg)
  - [5] 2026-10-21: 'DSpace 10.2-SNAPSHOT', REST root present
  - [6] 2026-10-21: POST — 403 'Invalid CSRF token.' (endpoint exists and is CSRF-guarded, so self-registration is a deployment toggle)
  - [7] 2026-10-21: 'Displaying 1 - 100 of 3,485', 35 pages
- sources:
  - [1] https://github.com/DSpace/DSpace/blob/main/dspace-server-webapp/src/main/resources/application.properties
  - [2] https://raw.githubusercontent.com/DSpace/DSpace/main/dspace-server-webapp/src/main/resources/application.properties
  - [3] https://raw.githubusercontent.com/DSpace/DSpace/main/dspace/config/dspace.cfg
  - [4] https://api.github.com/search/code?q=quota+repo:DSpace/DSpace
  - [5] https://demo.dspace.org/server/api
  - [6] https://demo.dspace.org/server/api/eperson/registrations
  - [7] https://dspace.org/registry/
