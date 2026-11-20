# Standard Ebooks

> standardebooks.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/standardebooks/ | JSON https://fshy.ajam.dev/api/v1/entity/standardebooks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Standard Ebooks

- `debrid/standard-ebooks` | qualifies-with-caveat | evidence documented | binding none | category public-domain ebook library (curated) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://standardebooks.org/
- price USD 0
- free tier: Free, public-domain, carefully produced ebooks. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No byte or title count is published on the site; 1,541 is the GitHub repository count, which includes non-book tooling repos.
- per-object cap: not applicable: one EPUB/AZW3/KEPUB per book; the measured EPUB is 831,959 bytes | source: [2]
- retention: permanent: a curated public-domain catalogue, each book also held as a public git repository | source: [1]
- egress: Per-book downloads are free and unmetered. Bulk ZIPs of whole collections are not: 'Access to our bulk downloads is a benefit of Patrons circle membership', a paid donation tier. The Atom feed at /feeds/atom/all answered 401 to an anonymous client on 2026-10-23. | metered: no | free allowance: no byte allowance published; bulk ZIPs are paywalled, per-book files are not | source: [3]
- identity: anonymous | detail: No account for per-book downloads or for git clone. A Patrons Circle membership (paid) is the only registration-like gate, and it buys the bulk ZIPs only.
- interface: rest, git, cli
- limits:
  - request-rate: bulk ZIPs are restricted to Patrons Circle members; no anonymous bulk endpoint exists [3]
- limits note: The paywall on bulk ZIPs is a membership gate, not one of the seven vocabulary kinds: it is a purchase, not a rate, a quota or an identity check. The Atom feed also refused an anonymous client with 401, so feed-based crawling is closed.
- binding note: Nothing in the vocabulary fails at 1 TiB/month because the catalogue is far smaller than that: roughly 1,500 books at about 1 MB each is under 2 GB. The ceiling is corpus size, not service policy.
- interface detail: HTTPS per book, and a two-hop download: /ebooks/<author>/<title>/downloads/<file>.epub returns an HTML 'Your Download Has Started!' page carrying a meta refresh to the same path with ?source=download, which is the actual file. Each title is also a public git repository under github.com/standardebooks.
- endpoint: https://standardebooks.org/ebooks/<author>/<title>/downloads/<author>_<title>.epub?source=download
- tooling: git clone of the per-book repository is the only bulk path that needs no donation; wget/curl with the two-hop pattern works per book.
- composes with: Small, high-quality text corpus to pair with Gutenberg's 2.44 TB when typography matters; the git repos give clean XHTML source that a diff pipeline can track.
- reliability: The direct .epub URL silently returns 200 with an HTML redirect page instead of the file; a client that trusts the status code saves a 8,777-byte web page as a book. The ?source=download hop is required.
- notes: The caveat is bulk only: the free path is one book at a time or one git clone at a time. The abandoned route was 'download the Atom feed and walk it' - the feed answered 401.
- evidence note: The per-book EPUB was downloaded and hashed here; the paywall and the 401 on the feed were observed. Catalogue size is the one soft number - the 1,541 repository count is a proxy, not a title count.
- extras:
  - epub_sha256: 85814417c1a74d2ca7f3b077b47454d0cfc728392d40d846d1c97d44f24c5279
  - epub_bytes: 831959
  - github_repos: 1541
  - atom_feed_status: 401
- evidence:
  - [1] 2026-10-23: 
  - [3] 2026-10-23: 'Access to our bulk downloads is a benefit of Patrons circle membership' - ZIP bulk is a paid tier
  - [4] 2026-10-23: Link header page=1541: 1,541 public repositories, the per-book git path
  - probe:https://standardebooks.org/ebooks/jane-austen/pride-and-prejudice/downloads/jane-austen_pride-and-prejudice.epub 2026-10-23: 200 with 8,777 bytes of application/xhtml+xml - an HTML 'Your Download Has Started!' page, not an EPUB; false-200 shape
  - probe:https://standardebooks.org/ebooks/jane-austen/pride-and-prejudice/downloads/jane-austen_pride-and-prejudice.epub?source=download 2026-10-23: 200, 831,959 bytes, application/epub+zip, sha256 85814417c1a74d2ca7f3b077b47454d0cfc728392d40d846d1c97d44f24c5279
  - probe:https://standardebooks.org/feeds/atom/all 2026-10-23: 401 to an anonymous client - the catalogue feed is not public
- sources:
  - [1] https://standardebooks.org/about
  - [2] https://standardebooks.org/ebooks
  - [3] https://standardebooks.org/bulk-downloads
  - [4] https://api.github.com/orgs/standardebooks/repos?per_page=1&type=public
