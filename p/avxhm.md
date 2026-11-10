# AvaxHome

> avxhm.se | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/avxhm/ | JSON https://fshy.ajam.dev/api/v1/entity/avxhm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AvaxHome

- `debrid/avaxhome` | qualifies | evidence documented | binding none | category DDL blog index (books, courses, software) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://avxhm.se/
- price USD 0
- free tier: Free to read and free to take the links. No account, subscription or quota appears on the page. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: pages carry links to file hosts, not files | source: [1]
- retention: not applicable: each post's links live on the host they point to | source: [1]
- egress: Nothing is served by AvaxHome; every download is fetched from the host a post links to. | metered: no | free allowance: none | source: [1]
- identity: anonymous | detail: No registration to read. Whether a download from a linked host requires an account depends on that host.
- interface: unknown
- limits:
  - request-rate: unstated [1]
- limits note: No rate limit is published. Posts are dated to the minute, which makes the site a usable freshness signal for what a host index is missing.
- binding note: AvaxHome transfers nothing, so no byte constraint binds. The constraint lives on whichever host a post links to.
- interface detail: A blog front page with dated posts and category facets (/ebooks/facet/<topic>/). No API, RSS or search endpoint was read.
- tooling: Browser only as read. The dated, faceted structure is easy to crawl; published records own crawler is the tool.
- composes with: A source of links rather than capacity: it is where a book, course or piece of software is announced, and the file itself arrives from whichever host the poster chose. That makes it the front end of the debrid chain for text and software, where the torrent indexers carry video.
- reliability: Posts are made by named contributors ('Posted By: roxul', 'IrGens', 'AvaxHomeAI') and the front page carries an AvaxHomeAI-written editorial post at the top, so the site mixes automated editorial with human uploads. A post's links rot at the host's pace, not the site's.
- notes: It is an index, not a provider: nothing here can be scheduled, mounted or measured for capacity.
- evidence note: The live front page was read with posts timestamped 23 Oct 2026 02:12, which is what establishes it as alive. No download was attempted.
- extras:
  - domain_note: avaxhome.ws and avaxhome.is are older domains; avxhm.se is the live one today
  - contributors_seen: AvaxHomeAI, roxul, IrGens
- evidence:
  - [1] 2026-10-23: the site is live with posts dated '23 Oct 2026 02:14', the ebook/course/software facets, and the named contributors
- sources:
  - [1] https://avxhm.se/
