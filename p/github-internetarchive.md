# wayback cdx server as storage

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-internetarchive/ | JSON https://fshy.ajam.dev/api/v1/entity/github-internetarchive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## wayback cdx server as storage

- `storage/wayback-cdx-server-as-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:51.191Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/github-internetarchive.md
- free tier: none reachable: It is an index over captures, not a blob store. Useful only as a free listing/manifest source for items you already uploaded (1.7s-38s per query in probes). | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the Wayback CDX Server documentation states a maximum result rows per query but no per-object upload size cap | note: not applicable
- retention: stated-absent: the Wayback CDX Server documentation describes an index of captures returned per query and states no retention period for bytes deposited by a user
- egress: stated-absent: the Wayback CDX Server documentation describes query output formats (plain text or JSON) but states no egress price or transfer quota for deposited bytes | metered: no
- identity: email
- interface: rest
- interface detail: HTTP GET query API over web.archive.org/cdx/search/cdx returning CDX rows or JSON; a standalone servlet in the Internet Archive open-source wayback software
- tooling: not documented
- composes with: The CDX server is freely available open-source software and its queries return CDX data or a JSON array that can be consumed by other tools; it lists captures rather than holding deposited bytes.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: It is an index over captures, not a blob store. Useful only as a free listing/manifest source for items you already uploaded (1.7s-38s per query in probes).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: It is an index over captures, not a blob store. Useful only as a free listing/manifest source for items you already uploaded (1.7s-38s per query in probes).
  - probe:web.archive.org/cdx 2026-11-19: the CDX endpoint returns an index of captures (urlkey, timestamp, digest) over already-archived URLs, not a blob store | capture: sha256:f7dfda824c288219864c1d32c3f0a443881bb60b12f4d93f857b8e1822c609a7 | quote: "urlkey","timestamp","original","mimetype","statuscode","digest","length"
  - [1] 2026-11-19: the Wayback CDX Server is reached by HTTP GET queries returning CDX data or JSON | capture: sha256:aa8de6287af10520a7cf0e144d3a4a640d288867f1dfdf3f12419d819d6c8683 | quote: The server responds to GET queries and returns either the plain text CDX data, or optionally a JSON array of the CDX.
  - [1] 2026-11-19: the CDX server serves an index of captures over HTTP, not a blob store | capture: sha256:aa8de6287af10520a7cf0e144d3a4a640d288867f1dfdf3f12419d819d6c8683 | quote: The `wayback-cdx-server` is a standalone HTTP servlet that serves the index that the `wayback` machine uses to lookup captures.
  - [2] 2026-11-19: the CDX Server is described as a query API over capture data, with no user-byte retention term | capture: sha256:9da66609b8c1968ac5df9f3d37da3394f613379be691902ee04128f539a101f2 | quote: The CDX Server is another API which allows for complex querying, filtering and analysis of Wayback capture data.
  - [1] 2026-11-19: the only stated maximum is a query result limit, not a per-object storage cap | capture: sha256:aa8de6287af10520a7cf0e144d3a4a640d288867f1dfdf3f12419d819d6c8683 | quote: The CDX server config provides a setting for absolute maximum length returned from a single query (currently set to 150000 by default).
  - [1] 2026-11-19: the CDX server composes as open-source software and returns machine-readable index data, but stores no deposited bytes | capture: sha256:aa8de6287af10520a7cf0e144d3a4a640d288867f1dfdf3f12419d819d6c8683 | quote: However, the cdx server is freely available with the rest of the open-source wayback machine software in this repository.
- sources:
  - [1] https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md
  - [2] https://archive.org/help/wayback_api.php
