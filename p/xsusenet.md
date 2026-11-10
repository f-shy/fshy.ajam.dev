# XS Usenet

> xsusenet.com | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xsusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/xsusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## XS Usenet (premium)

- `debrid/xs-usenet` | qualifies | evidence documented | binding retention-clamped | category usenet provider (article spool, NNTP) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:22:02.000Z (live) | stale on 2026-11-23
- url https://my.xsusenet.com/index.php?/knowledgebase/article/22/common-usenet-error-messages/
- disagrees on identity_kind: `debrid/xs-usenet` says card, `debrid/xsusenet` says email
- disagrees on verdict: `debrid/xs-usenet` says qualifies, `debrid/xsusenet` says dead
- free tier: No free tier in use: 'All of our premium packages support posting, but some servers are read-only (free.xsusenet.com is no longer in use).' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: No price quoted; the pricing page was not read.
- per-object cap: Not published; the unit is the article. | source: [1]
- retention: 'Our retention is limited to 1100 days.' | days: 1100 | source: [1]
- egress: Plan-based; the only ceiling named on the page read is the connection count. | metered: no | free allowance: none | source: [1]
- identity: card | detail: Paid client-area account with email and card; usenet credentials are separate from the client-area login, which the KB calls out explicitly.
- interface: nntp
- limits:
  - retention-clamped (binding): 1100 days; older articles answer 423 or 430 [1]
  - request-rate: 'Too Many Connections' is a named refusal; the plan's connection count is the ceiling [1]
  - write-gated: posting is allowed on premium packages and refused with '440 Posting Not Allowed' where it is not [1]
- limits note: This is the only provider in the set whose documentation lists the connection-level refusals next to the article-level ones, which is what a client needs to tell 'wrong password' from 'article gone'.
- binding note: At 1100 days the spool is the shortest published retention here, so a client pulling older releases meets 430 far more often than a connection or byte limit.
- interface detail: NNTP reader, standard commands; the page lists the full refusal set a client meets at connect and at article fetch.
- tooling: SABnzbd, NZBGet, zurg's nzb provider
- composes with: A shorter-retention spool is the wrong primary for a 1 TiB/month archive and the right fill for recent content; 1100 days is the only day count among the providers in this set that publishes one.
- reliability: Nothing past 1100 days exists on this spool; the KB warns that client-area credentials are not usenet credentials, which is a common first-hour failure; a 503 is an overload rather than a credential problem.
- notes: Potential failure points: the connection cap, the 1100-day wall, or the credential split between client area and NNTP. The credential split is the one that breaks a first-hour setup; the 1100-day wall is the one that breaks an archive pull. Both are documented.
- evidence note: Every string and the retention figure are the vendor's own knowledge-base page. No probe was run.
- extras:
  - failure_angle: credential split and a published retention wall
  - strongest_signal: 482/502 at connect, 430 at fetch
  - account_states: 482 invalid credentials or expired account ('ensure your account is still active and hasn't expired'); 480 auth required; 503 service unavailable; 440 posting refused
  - cache_miss: not applicable
  - host_removal: not applicable
- evidence:
  - [1] 2026-10-23: The refusal set: '502 Authentication Error / 482 Invalid username or password'; '440 Posting Not Allowed'; '480 Authentication Required'; '423 Bad Article Number or 430 No Such Article Found' with 'Our retention is limited to 1100 days'; '503 Service Unavailable ... possibly due to maintenance or overload'; 'Too Many Connections'. Also 'Your email address and password for a user area are NOT your Usenet credentials.'
  - [2] 2026-10-23: Connection-count sizing: 'Set connections to what your plan actually allows ... Going over what the plan permits gets connections refused.'
- sources:
  - [1] https://my.xsusenet.com/index.php?/knowledgebase/article/22/common-usenet-error-messages/
  - [2] https://notes.debridmediamanager.com/providers/usenet/

## XS Usenet (debrid/xsusenet)

- `debrid/xsusenet` | dead | evidence documented | binding none | category usenet provider (Abavia reseller) - dead | tier none
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:29.000Z (live) | stale on 2026-11-23
- url https://xsusenet.com/
- price n/a
- disagrees on identity_kind: `debrid/xs-usenet` says card, `debrid/xsusenet` says email
- disagrees on verdict: `debrid/xs-usenet` says qualifies, `debrid/xsusenet` says dead
- free tier: The service is shut down. 'XS Usenet has shut down - but your Usenet service continues without interruption. All accounts have been moved to EasyUsenet.' The website and ordering system are closed. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: no per-object cap is published; no per-object cap is published; the unit of retrieval is a Usenet article, approximately 750 KB by convention, so 1 TiB of monthly transfer corresponds to roughly 1.4 million article… | source: [1]
- retention: Not applicable: no new accounts are sold. Existing accounts keep their expiry date on the EasyUsenet infrastructure. | source: [1]
- egress: Not applicable; the ordering system is closed | metered: no | source: [1]
- identity: email | detail: Registration is closed. Existing credentials were migrated unchanged to reader.easyusenet.com.
- interface: nntp
- limits note: No limits apply to a service that no longer signs up customers. The last published terms were a soft 5 TB/month ceiling on unlimited plans with speed cut to 40 Mbit above it, per the r/usenet map.
- binding note: Nothing binds because nothing is sold. A reader who needs this capacity must go to EasyUsenet, which inherited the accounts.
- interface detail: NNTP over TLS on port 563. No HTTP or object API exists for the download path, which is driven through SABnzbd, NZBGet or nzbdav.
- composes with: Nothing composes: the capacity moved to EasyUsenet, which is the Abavia brand a client should price instead.
- reliability: Shut down after 15 years, citing staff shortages; accounts moved to EasyUsenet with the same username and password and a new hostname. The VPN product was suspended and set to close on August 31, with refunds for unused time.
- notes: The interesting part is the epitaph: the first freemium Usenet provider in 2009 is gone in 2026, and its free-tier model went with it. That is the direction of travel for the debrid main question.
- evidence note: The shutdown notice is the vendor's own page, read. The fetch reported no upstream status, so the page content is the evidence rather than an HTTP code.
- extras:
  - backbone: Abavia
  - successor: EasyUsenet (reader.easyusenet.com)
  - lifetime: 2009-2026
- evidence:
  - [1] 2026-10-23: 'XS Usenet has shut down'; 'All accounts have been moved to EasyUsenet'; new server reader.easyusenet.com; 'Since starting in 2009 as the first freemium Usenet provider'
  - [2] 2026-10-23: Xsusenet listed as an Abavia reseller with 'soft limits (5tb per month) ... above 5TB speed will be capped to 40Mbit'
- sources:
  - [1] https://xsusenet.com/
  - [2] https://www.reddit.com/r/usenet/wiki/providers
