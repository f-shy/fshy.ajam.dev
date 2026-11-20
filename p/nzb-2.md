# NZB.su

> nzb.su | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nzb-2/ | JSON https://fshy.ajam.dev/api/v1/entity/nzb-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NZB.su

- `debrid/nzb-su` | dead | evidence measured | binding write-gated | category Usenet indexer (retired API endpoint) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:11:54.066Z (live) | stale on 2026-11-23
- url https://nzb.su/
- free tier: None: the API endpoint answers <error code="101" description="This API endpoint has been retired. Update your indexer URL from nzb.su to nzb.life."/> The name still resolves, the indexer behind it has moved. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable under this name; the successor publishes its own caps | source: [1]
- egress: none: the endpoint returns a 157-byte error document | metered: no | source: [1]
- identity: email | detail: Accounts and registration were carried to nzb.life; the old host no longer offers a path.
- interface: rest
- limits:
  - write-gated (binding): the indexer URL is retired; every API call returns error 101 probe:https://nzb.su/api?t=caps
- binding note: The name is the constraint: no query reaches an index. The successor record carries the live limits.
- interface detail: The /api path is alive and answers XML, but only with error 101. This is the cleanest death signal in the sector: a machine-readable redirect to the successor, not a timeout.
- endpoint: https://nzb.su/api (retired)
- tooling: A Prowlarr or NZBHydra2 entry pointed at nzb.su keeps the URL and receives error 101 on every search; the fix is to change the host to nzb.life, not to re-add the indexer.
- composes with: Retired in favour of nzb.life, which carries the live limits.
- reliability: A retired API with a live DNS record: a stale client gets a well-formed XML error, which most clients log as an empty result set rather than as a configuration problem.
- notes: Do not delete: the old host is still in circulating lists and in old client configs, and the error message is the only thing that tells a reader where the index went.
- evidence note: The error document was fetched with its exact wording, so the retirement is measured. The successor's limits are on the nzb-life record.
- extras:
  - price: retired
  - successor: nzb-life
  - error_code: 101
- evidence:
  - probe:https://nzb.su/api?t=caps&x=1 2026-10-23: returned 157 bytes: <error code="101" description="This API endpoint has been retired. Update your indexer URL from nzb.su to nzb.life."/> (sha256 867011a3...)
  - [2] 2026-10-23: the successor states the mapping in its own meta description: 'NZB.su and nzbsu users should use NZB.life.'
- sources:
  - [1] https://nzb.su/api?t=caps
  - [2] https://www.nzb.life/
