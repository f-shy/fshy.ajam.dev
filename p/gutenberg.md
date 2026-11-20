# Project Gutenberg

> gutenberg.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gutenberg/ | JSON https://fshy.ajam.dev/api/v1/entity/gutenberg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Project Gutenberg

- `debrid/project-gutenberg` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category public-domain ebook library (bulk mirrorable) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://www.gutenberg.org/
- price USD 0
- free tier: 79,657 free eBooks, 'No fees, no registration, completely free'. The published collection metadata gives the real size: main collection 3,443,023 files / 1,064,736,252,276 bytes, generated collection (EPUB, MOBI, HTML) 2,681,516 files / 1,375,569,708,792 bytes, i.e. 6,124,539 files and 2,440,305,961,068 bytes (2.44 TB), metadata updated 2026-10-19. | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The 79,657 counts titles; metadata.json counts files. Both were read on the same day and they describe different things, so neither is the other's check.
- per-object cap: not applicable: one file per book per format. No per-file cap is published; the largest objects in the tree are audio ZIPs, and the file list is the only inventory. | source: [1] | note: A text file measured here was 772,386 bytes (Pride and Prejudice, plain text).
- retention: permanent: the mirroring guide describes a fixed collection that 'changes daily, as new items are added or updated', with no expiry clock. | source: [2]
- egress: Free and unmetered from the main site and from every mirror. The main site is not a bulk endpoint: 'This website is intended for human users only. Any perceived use of automated tools to access this website will result in a temporary or permanent block of your IP address.' Bulk is approved through rsync mirrors, which the mirroring guide documents. | metered: no | free allowance: no byte allowance published | source: [3]
- identity: anonymous | detail: The home page states 'No fees, no registration, completely free'. No account exists to create; a mirror operator is a volunteer arrangement, not a registration that is needed.
- interface: rest, rsync, cli
- limits:
  - per-ip-shaping (binding): automated access from the main site is blocked by IP; 'Such blocks automatically expire after a few days' [3]
  - request-rate: the vendor's own harvest example uses wget -w 2 (two seconds between requests); mirrors are the approved bulk path [3]
- binding note: At 1 TiB/month the main site blocks the caller long before any byte cap; the mirror network is the only path that carries that volume, and the mirror list is what makes the quota effectively unlimited.
- interface detail: plain HTTPS per file (https://www.gutenberg.org/cache/epub/<id>/pg<id>.txt), an OPDS feed at /ebooks/search.opds/, a JSON OPDS2 feed 'currently available for testing', GUTINDEX.ALL and metadata.json for inventory, and rsync mirrors listed in MIRRORS.ALL.
- endpoint: part of interface detail
- tooling: wget/curl, rsync against any mirror, the OPDS feed for readers. The robot policy's own example is 'wget -w 2 -m -H "https://www.gutenberg.org/robot/harvest?filetypes[]=html"' - two seconds between requests, from the main site, for a bounded harvest.
- composes with: The canonical public-domain text corpus to pair with LibriVox audio and Internet Archive scans of the same titles; a 2.44 TB rsync mirror can be filtered to the zip files only, which drops the audio weight.
- reliability: Main-site IP blocks are automatic and last days; the generated collection is rebuilt in batches, so a mirror refresh sees traffic spikes rather than a steady delta.
- notes: Caveat is the main site, not the catalogue. The catalogue is 2.44 TB and mirrorable, which is more than the stated archive of 20 TiB needs from this one source, but the main site will block a bulk puller within a day. The abandoned route is 'scrape gutenberg.org with parallel connections': the robot policy names it as a blockable offence and the mirror path costs nothing.
- evidence note: The collection size is the vendor's own metadata.json, fetched here; one complete file was downloaded and hashed. What would raise it to measured for the bulk path is an rsync of a filtered subset from a mirror with a byte count, which was not run.
- extras:
  - total_bytes: 2440305961068
  - total_files: 6124539
  - titles: 79657
  - metadata_updated: 2026-10-19T02:49:46+00:00
  - mirror_list: https://www.gutenberg.org/MIRRORS.ALL
  - measured_file_sha256: 3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75
- evidence:
  - [4] 2026-10-23: 'Project Gutenberg is a library of 79,657 free eBooks' and '100% Free - No fees, no registration'
  - [1] 2026-10-23: collection size: main 3,443,023 files / 1,064,736,252,276 bytes, generated 2,681,516 files / 1,375,569,708,792 bytes, metadata_updated 2026-10-19T02:49:46+00:00
  - [3] 2026-10-23: 'intended for human users only', automatic IP blocks that 'expire after a few days', and the sanctioned wget -w 2 harvest recipe
  - [2] 2026-10-23: rsync mirroring is offered; 'around 6 million files, over 60 languages'; main collection changes daily
  - probe:https://www.gutenberg.org/cache/epub/1342/pg1342.txt 2026-10-23: 200, 772,386 bytes, sha256 3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75, text/plain, 2,239.5 ms - the file downloaded here is the book
- sources:
  - [1] https://www.gutenberg.org/dirs/metadata.json
  - [2] https://www.gutenberg.org/help/mirroring.html
  - [3] https://www.gutenberg.org/policy/robot_access.html
  - [4] https://www.gutenberg.org/
