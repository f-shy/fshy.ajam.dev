# UsenetServer

> usenetserver.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetserver/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetServer

- `debrid/usenetserver` | paid-only | evidence documented | binding none | category usenet provider (article spool, NNTP) | tier unlimited
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:47:09.830Z (live) | stale on 2026-12-26
- url https://support.usenetserver.com/kb/article/193-i-received-a-423-no-such-article-or-a-430-no-such-article-error-when-downloading-what-is-the-problem/
- free tier: No free tier; a paid usenet account. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: No price is quoted because the pricing page was not read.
- per-object cap: Not published; the unit is the article. | source: [1]
- retention: 'UsenetServer offers one of the highest article retention times available'; no day count on the page read. | source: [1]
- egress: Unmetered on an unlimited plan; article availability binds before bytes. | metered: no | free allowance: none | source: [1]
- identity: card | detail: Paid account with email and card. No identity document described.
- interface: nntp
- limits:
  - retention-clamped: articles past retention answer 423 or 430 per article id [1]
  - request-rate: plan connection count is the ceiling; excess connections are refused at connect time [2]
  - request-rate: 50 SSL connections on the 12-month plan, 20 on the 1-month [3]
  - retention-clamped: over 6675 days of stored posts [3]
- limits note: The vendor points at indexers as the amplifier: 'Many Indexers maintain references to articles long after they've been removed from Usenet servers', so the NZB can be valid and the articles still gone.
- binding note: Unlimited bytes; the first failure is a per-article 430/423 whose frequency is set by the indexer's freshness and the spool's retention.
- interface detail: NNTP reader, TLS; standard article commands.
- tooling: SABnzbd, NZBGet, zurg's nzb provider
- composes with: The clearest documented split between the two article codes: 423 means the group is there and the article is not, 430 means the article is unavailable while the group remains readable, which is what a script can branch on.
- reliability: An indexer can point at articles the spool no longer holds; each such article is a per-file failure and only PAR2 or a second provider recovers it.
- notes: Potential failure points: retention, indexer staleness, or a connection ceiling. The vendor gives a number for none of them; the useful part of this page is the 423/430 split, which lets a user distinguish a missing group from a missing article. A vendor KB article says article access is unrestricted and uncapped; that is the only statement about volume on the site.
- evidence note: The 423/430 distinction and the indexer behaviour are the vendor's own. No removal-by-notice cause is named on this page, which differs from Newshosting's page in the same group.
- extras:
  - failure_angle: missing article
  - strongest_signal: 430 (article absent) vs 423 (article number absent in a known group)
  - account_states: article-level states only on the page read
  - cache_miss: not applicable
  - host_removal: not applicable
  - backbone: Omicron (Highwinds Media), AS33438
  - conflict: support KB 176 vs /pricing/ on price and connections
- evidence:
  - [1] 2026-10-23: '423 No Such Article: The server acknowledges the group exists, but the article requested is not present. 430 No Such Article: The article is not available on the server, even though the newsgroup is accessible.' And 'Many Indexers maintain references to articles long after they've been removed from Usenet servers.'
  - [2] 2026-10-23: Second server behaviour: a backup account is only asked after every primary has answered no such article; a second server turns a whole-release PAR2 read into one article fetch.
  - [3] 2026-10-23: $14.95 1 month 20 connections; $8.95 3 months; $7.95 12 months billed $95.40 with 50 connections and US+EU; 6642 days
  - [4] 2026-10-23: The same vendor's KB quotes $16.95 1 month, $8.95 exclusive and $7.95 12-month, and 'up to 20 SSL-encrypted connections' - a stale page
  - [5] 2026-10-23: 'UsenetServer does not impose restrictions on the number of articles accessed by users.'
  - [3] 2026-11-25: the pricing page now states over 6675 days of stored posts, replacing 6642 | capture: sha256:7c31ca61fb2d926836ba957892ec4616d3e14fc0a8cb8c40e471297b13a4a4d1 | quote: With over 6675 days of stored posts to explore, you’ll always find what you’re looking for with the most complete searches every time.
  - [3] 2026-11-25: the pricing page states over 6675 days of stored posts | capture: sha256:7c31ca61fb2d926836ba957892ec4616d3e14fc0a8cb8c40e471297b13a4a4d1 | quote: With over 6675 days of stored posts to explore, you’ll always find what you’re looking for with the most complete searches every time.
  - [1] 2026-11-25: the vendor still documents the 423 per-article failure that bounds retrieval | capture: sha256:7038446b05495a03ae216912f90223af86921ae7a8657daac115f8bf9dbf5c7b | quote: - 423 No Such Article: The server acknowledges the group exists, but the article requested is not present.
  - [3] 2026-11-25: signup takes a card through PayPal or major card networks; no identity document or phone number is named | capture: sha256:7c31ca61fb2d926836ba957892ec4616d3e14fc0a8cb8c40e471297b13a4a4d1 | quote: When signing up for UsenetServer, we offer payment through PayPal and all major credit cards, including Visa, Mastercard, Discover, American Express, JCB, and Visa Electron.
  - [3] 2026-11-25: signup uses a card or PayPal, with no identity document or phone number named | capture: sha256:7c31ca61fb2d926836ba957892ec4616d3e14fc0a8cb8c40e471297b13a4a4d1 | quote: When signing up for UsenetServer, we offer payment through PayPal and all major credit cards, including Visa, Mastercard, Discover, American Express, JCB, and Visa Electron.
  - [5] 2026-11-25: article volume remains unrestricted, consistent with a paid unlimited plan and no free tier | capture: sha256:fb2c72535ab772deef022b82ab9510a349dd26a96f558171ea9d8d623a67e7fc | quote: UsenetServer does not impose restrictions on the number of articles accessed by users.
- sources:
  - [1] https://support.usenetserver.com/kb/article/193-i-received-a-423-no-such-article-or-a-430-no-such-article-error-when-downloading-what-is-the-problem/
  - [2] https://notes.debridmediamanager.com/providers/usenet/
  - [3] https://www.usenetserver.com/pricing/
  - [4] https://support.usenetserver.com/kb/article/176-how-much-does-the-service-cost/
  - [5] https://support.usenetserver.com/kb/article/183-are-there-any-limits-on-the-number-of-downloads/
