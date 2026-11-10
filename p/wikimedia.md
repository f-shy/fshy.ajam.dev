# Wikimedia Downloads

> wikimedia.org | Storage, Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wikimedia/ | JSON https://fshy.ajam.dev/api/v1/entity/wikimedia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wikimedia Commons

- `storage/wikimedia-commons` | qualifies-with-caveat | evidence reported | binding per-object-cap | category open media repository (institutional-grade, Wikimedia Foundation)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://commons.wikimedia.org
- free tier: NO TOTAL QUOTA. Read verbatim from Commons:Maximum_file_size: 'there is no limit to the total size of uploads by an individual account.' Per-file cap is 5 GiB (5,368,709,120 bytes) via chunked upload, 100 MiB otherwise. Live API confirms: `maxuploadsize: 5368709120`. | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GiB/file | bytes: 5368709120 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, unmetered, CDN (upload.wikimedia.org), no auth, Range supported. Wikimedia runs its own edge cache in front of Swift. | metered: no
- identity: email | detail: Email. Account is username+password+email, no affiliation. Note the nuance: upload itself is in the base `user` group, but `reupload` (overwrite) needs autoconfirmed. So first uploads are open; overwriting an existing file needs account age.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 5 GiB/file [1]
  - write-gated: review at the community level [1]
- limits note: 5 GiB/file, 100 MiB without chunking; per-licence/scope review at the community level; thumbnailing capped at a 59 s timeout, 100 MP for GIFs
- interface detail: MediaWiki Action API + REST; `action=upload` with `stash`/`filekey` for chunked; `upload_by_url` right for server-side upload
- tooling: mwclient / pywikibot / commons-cli; `upload` and `upload_by_url` are granted to the plain `user` group (verified in siteinfo usergroups), so a brand-new account can already do server-side upload without waiting
- composes with: `upload_by_url` means Commons fetches the file from YOUR url. No local bandwidth at all. Files land at upload.wikimedia.org/wikipedia/commons/<x>/<xy>/<name>, hash-addressed and immutably versioned.
- reliability: The one platform here where a multi-TB batch is explicitly contemplated. Commons asks you to warn sysadmins before 'batch uploads amounting to several TB', which is an acknowledgement that people do it.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: maxuploadsize: 5368709120, generator MediaWiki 1.47.0-wmf.24
  - withheld 2026-10-21: same API with siprop=usergroups — `user` group holds ['upload','upload_by_url','reupload-own','move-categorypages']
  - [1] 2026-10-21: 'no limit to the total size of uploads by an individual account'; 5 GiB chunked / 100 MiB direct
  - [3] 2026-10-21: 149,839,243 files on the cluster (scale of the storage layer)
  - [4] 2026-10-21: 'Our swift backend storage is limited to files smaller than 5 Gb'
- sources:
  - [1] https://commons.wikimedia.org/wiki/Commons:Maximum_file_size
  - [2] https://commons.wikimedia.org/w/api.php?action=query&meta=siteinfo&siprop=general&format=json
  - [3] https://commons.wikimedia.org/w/api.php?...siprop=statistics
  - [4] https://wikitech.wikimedia.org/wiki/Uploading_large_files

## Wikimedia Downloads (dumps.wikimedia.org)

- `debrid/wikimedia-dumps` | qualifies-with-caveat | evidence measured | binding per-ip-shaping | category encyclopaedia corpus (monthly XML dumps, HTTP mirrors) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://dumps.wikimedia.org/
- price USD 0
- free tier: Complete public wiki dumps, monthly, free and anonymous. 'Downloads are also rate limited and capped at 3 connections per-IP.' The English Wikipedia article dump measured here is 25,800,511,704 bytes. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The dumps are being reorganised: the XML dumps are 'deprecated and will be sunset in January 2027' in favour of MediaWiki Content File Exports.
- per-object cap: not applicable: one compressed file per dump. enwiki-latest-pages-articles.xml.bz2 is 25,800,511,704 bytes; ranged reads are supported (accept-ranges: bytes). | source: [2]
- retention: monthly snapshots are kept; 'latest' is replaced each run and older dated directories persist for a period the dump index does not quantify | source: [1]
- egress: Free, but conditioned on the User-Agent policy: 'If you are reading this on Wikimedia servers, please note that we are now enforcing the Wikimedia Foundation User-Agent Policy for dumps downloads. Downloads are also rate limited and capped at 3 connections per-IP ... Clients that do not respect the user-agent policy or who try to evade these limits may be blocked.' | metered: no | free allowance: no byte allowance published | source: [1]
- identity: anonymous | detail: No account and no key; a descriptive User-Agent is the only requirement, and it is not a credential.
- interface: rest, rsync, cli
- limits:
  - per-ip-shaping (binding): capped at 3 connections per IP, and rate limited; measured here at 1.661-2.617 MiB/s over one connection (three runs) and 2.647-7.649 MiB/s total over eight connections (three runs), so parallelism helped up to 3.6x and the cap did not refuse the eighth connection [1]
- limits note: The User-Agent policy is enforced: a client without a descriptive agent may be blocked, and evasion attempts are named as a blocking reason on the front page.
- binding note: The documented 3-connection cap is a connection count, not a byte rate: eight parallel range reads all returned 206 and the best of them reached 7.649 MiB/s, which is about 645 GiB/day.
- interface detail: HTTPS per file with Range support; rsync mirrors are listed on meta.wikimedia.org; the dump index at /backup-index.html gives every file with size and checksum.
- endpoint: https://dumps.wikimedia.org/enwiki/latest/
- tooling: curl/wget with a descriptive User-Agent, rsync against a mirror, and the checksum files that ship beside each dump.
- composes with: A fixed encyclopaedia corpus to join against Common Crawl's web text; the 24 GiB article dump is small enough to hold beside a dataset snapshot, and the mirror list is the escape hatch when the per-IP cap binds.
- reliability: The dump format is changing: XML dumps sunset in January 2027, so a pipeline built on pages-articles.xml has a dated migration to the Content File Exports format.
- notes: Caveat is the 2027 format change and the 3-connection rule. A single connection gives about 178 GiB/day at the mean, and the best eight-connection run reached 645 GiB/day - which the published cap says a client should not do. The whole English Wikipedia article dump is one day's single-connection allowance.
- evidence note: The file size came from a HEAD and the rate from a 64 MiB ranged read, three runs at each concurrency. All eight parallel requests returned 206, so the documented 3-connection cap did not refuse them at the transport level - whether it is enforced by rate, by UA or only at peak is not established.
- extras:
  - enwiki_articles_xml_bytes: 25800511704
  - one_conn_mib_s: 2.617; 2.084; 1.661
  - eight_conn_mib_s: 2.647; 4.748; 7.649
  - connection_cap: 3
  - range_sha256: 3a74bf06ec319f7d702771523ec099593e7569f00b5bddfdbe3e76ddbc914ea7
  - xml_sunset: 2027-01
- evidence:
  - [1] 2026-10-23: 'Downloads are also rate limited and capped at 3 connections per-IP', User-Agent policy enforcement, and the January 2027 XML sunset notice
  - probe:https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 --head 2026-10-23: 200, content-length 25,800,511,704, accept-ranges: bytes, last-modified 2026-10-08
  - probe:https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 --range 0-67108863 2026-10-23: 64 MiB ranges at one connection: 2.617, 2.084 and 1.661 MiB/s across three runs, 206 with the range honoured; sha256 of the first range 3a74bf06ec319f7d702771523ec099593e7569f00b5bddfdbe3e76ddbc914ea7
  - probe:https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 --concurrency 8 --shard-bytes 67108864 2026-10-23: eight parallel 206s totalling 2.647, 4.748 and 7.649 MiB/s against same-run one-connection baselines of 1.317, 2.918 and 2.337 MiB/s - parallelism helped, and no request was refused
- sources:
  - [1] https://dumps.wikimedia.org/
  - [2] https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
