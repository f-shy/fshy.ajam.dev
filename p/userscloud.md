# UsersCloud

> userscloud.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/userscloud/ | JSON https://fshy.ajam.dev/api/v1/entity/userscloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsersCloud

- `debrid/userscloud` | dead | evidence documented | binding none | category former free file host, now a redirect to Send.now | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:37:40.772Z (live) | stale on 2026-11-23
- url https://userscloud.com/
- free tier: Not applicable: userscloud.com redirects to send.now and serves that site's homepage. The successor's terms live among debrid providers's send-now record. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Not applicable on this domain. | source: [1]
- retention: Not applicable on this domain. | source: [1]
- egress: None from this domain; requests are forwarded to send.now. | metered: no | source: [1]
- identity: anonymous | detail: Nothing is asked for by userscloud.com; the redirect target's free tier needs an email only for a free account.
- interface: webdav
- limits note: No constraint applies to the old domain; the successor's constraints are recorded under send-now.
- binding note: The old hostname transfers nothing itself.
- interface detail: Whatever send.now offers, now reachable under this hostname by redirect: WebDAV at webdav.send.now, FTP on port 992, and an HTTP API. userscloud.com itself serves no interface.
- tooling: None of its own. A client that had a UsersCloud integration now points at Send.now, which has a better tooling story (WebDAV and FTP).
- composes with: A rebrand with the old domain kept alive: old index links still resolve, land on the new product, and the new product is a transfer service rather than a PPD host. The chain step disappears but the link does not break.
- reliability: A redirect is the failure mode these records names explicitly: a link checker sees HTTP 200 and a live site, while the host behind the name is a different product with different rules. Any inventory counting UsersCloud separately from Send.now is counting one service twice.
- notes: Documented as dead-with-successor rather than merged, because the slug is what an old link or an old host list will contain. Successor record: send-now among debrid providers.
- evidence note: The redirect and landing site were read. The claim is narrow on purpose: the domain forwards, and it is not an independent service.
- extras:
  - successor_record: scratch (removed)
  - final_url: https://send.now/
- evidence:
  - [1] 2026-10-23: the final URL was https://send.now/ and the body is Send.now's transfer service ('Send large files securely', WebDAV and FTP sections), so UsersCloud no longer hosts anything under its own name
- sources:
  - [1] https://userscloud.com/
