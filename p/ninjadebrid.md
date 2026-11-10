# NinjaDebrid

> ninjadebrid.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ninjadebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/ninjadebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NinjaDebrid

- `debrid/ninja-debrid` | dead | evidence documented | binding none | category multi-hoster (torrent debrid, direct links and streaming) - dead | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:35:36.095Z (live) | stale on 2026-12-04
- url https://ninjadebrid.net/
- free tier: Gone. Every path on ninjadebrid.net now redirects to monkeytorrent.com, a French torrent index. A 2026-10-11 Wayback capture of /en still shows the debrid site: 'Paste a magnet at the top of this page: 1 torrent every 24 hours, up to 10 GB, no account needed. Or create a free account and confirm your email: you get unlimited torrents free for 24 hours, with full speed on your first 100 GB.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The offer that existed until at least 2026-10-11 was the most generous free torrent debrid found among debrid providers: 100 GB at full speed on a free account, or 10 GB per torrent per 24 h anonymously. It is not available now.
- per-object cap: formerly 10 GB per torrent for anonymous use; the free-account allowance was 100 GB total | bytes: 10737418240 | source: [2] | note: Read from the search index and the 2026-10-11 capture, not from a live page.
- retention: not applicable: torrent debrid, no storage product | source: [1]
- egress: No live terms: the domain no longer serves the service. The last capture advertised full speed for the first 100 GB. | metered: yes | free allowance: formerly 100 GB once, 10 GB per 24 h anonymously | source: [1]
- identity: email | detail: Free account needed an email confirmation ('create a free account and confirm your email'). Anonymous path needed nothing.
- interface: unknown
- limits:
  - pull-count: 1 torrent per 24 hours anonymously, up to 10 GB [2]
  - volume-quota: 100 GB at full speed on the free account, then limited [2]
- binding note: A dead service binds nothing. The limit that ended it is not published; the redirect target is a torrent index, which is consistent with the operator moving to an index rather than maintaining the debrid backend.
- interface detail: Web magnet box. Nothing is served now.
- tooling: None: the domain redirects.
- composes with: Nothing to chain. It is preserved so that the subsequent audit does not spend a wave re-finding a free 100 GB offer that closed between 2026-10-11 and 2026-10-23.
- reliability: The service was replaced by a redirect to a torrent index within 12 days of the last capture; a client's bookmarked URL now lands on unrelated content.
- notes: Service ceased operations between 2026-10-11 and 2026-10-23, redirecting traffic to an advertising domain.
- evidence note: The redirect is measured twice (a HEAD and a GET, both finishing at monkeytorrent.com with network requests reporting redirects=followed(1)). The free-tier numbers come from the 2026-10-11 capture and a search index, so they describe what the service offered, not what it offers.
- extras:
  - redirect_target: https://monkeytorrent.com/
  - last_capture_live: 2026-10-11T07:48:59Z
  - former_free_offer: 100 GB at full speed on a free account; 10 GB per torrent per 24 h anonymously
- evidence:
  - [3] 2026-10-23: the archive API's metadata for https://ninjadebrid.net/en reports a 2026-10-11 capture at status 200 with a 65,100-byte record, so the debrid page was being served 12 days before this record. The replay body itself was not opened; only the metadata was read.
  - [2] 2026-10-23: search-engine snippet for the URL, not a page read: '1 torrent every 24 hours, up to 10 GB, no account needed ... unlimited torrents free for 24 hours, with full speed on your first 100 GB'. The live URL redirects, so this text survives only in the index.
  - [1] 2026-11-03: a fetch of https://ninjadebrid.net/ on 2026-11-03 answered HTTP 200 and reported the final URL https://monkeytorrent.com/ after one followed redirect | capture: sha256:b45c878137b1b7b3f125cd8d297e0ca26596a32eb7488f01cf429581135f7347 | quote: x-web-final-url: https://monkeytorrent.com/
- sources:
  - [1] https://ninjadebrid.net/
  - [2] https://ninjadebrid.net/en
  - [3] https://web.archive.org/web/20261011074859/https://ninjadebrid.net/en?provider=wayback
