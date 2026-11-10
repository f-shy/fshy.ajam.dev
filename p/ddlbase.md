# DDLBase

> ddlbase.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ddlbase/ | JSON https://fshy.ajam.dev/api/v1/entity/ddlbase.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DDLBase

- `debrid/ddlbase` | qualifies-with-caveat | evidence documented | binding request-rate | category DDL release index (Blu-ray and REMUX releases, host mirrors per post) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-30T13:11:55.961Z (live) | stale on 2026-11-30
- url https://ddlbase.com/
- price USD 0
- free tier: No account to read the index or the feed: /rss returned 300 items. A post page shows two mirror slots anonymously and prints '(login for more mirrors)'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: an index, not storage | source: [2]
- retention: Posts persist. The feed carries the 300 most recent items. | source: [1]
- egress: No byte allowance: HTML and XML only. Each post's mirrors point at external hosts; the href behind 'Link 1' did not appear in the extracted page, so the host behind it is unverified. | metered: no | free allowance: none published | source: [2]
- identity: email | detail: A login is what unlocks mirrors beyond the first two. The registration form was not opened, so whether it asks for email alone or email plus captcha was not established.
- interface: rest
- limits:
  - request-rate (binding): no published limit; 10 sequential /rss requests about 1.2 s apart and 8 concurrent requests all returned 200, and robots.txt is Allow: / for every agent probe:ddlbase.com/rss
- limits note: Anonymous posts show 'Mirror 1: Link 1' and 'Mirror 2: Link 2' then '(login for more mirrors)'. The wider mirror set sits behind an account.
- binding note: As with any index, the only thing that can throttle a caller is page rate; the wider mirror set is an identity gate recorded in identity_cost rather than one of the seven constraints.
- interface detail: RSS 2.0 at /rss (content-type application/rss+xml, 300 items, self-link /rss.php), sitemap at /sitemap.xml. /feed/ returns 404. No JSON API found.
- endpoint: https://ddlbase.com/rss
- tooling: RSS reader. The item title carries release name and size ('Gebo.And.The.Shadow... - 23.7 GB'), so size filtering needs no post fetch.
- composes with: Poll /rss, filter on size from the item title, then open the post for the two anonymous mirrors or log in for the rest.
- reliability: Cloudflare plus LiteSpeed. /feed/ 404s while /rss works, so a client that guesses the conventional WordPress path gets nothing.
- notes: The deepest free feed measured among debrid providers at 300 items, and the only one that puts the size in the item title. The caveat is the mirror cap: two anonymous links per post. ddlbase.net answers as a separate XenForo forum and is not the same index.
- evidence note: Feed, post, robots.txt and both mirror slots were read on 2026-10-23. Registering and capturing the full mirror set would raise it to measured.
- extras:
  - feed_items: 300
  - feed_protocol: rss2
  - account_for_links: yes
  - anonymous_mirrors: 2
- evidence:
  - [1] 2026-10-23: content-type application/rss+xml, 300 items, titles that carry the size, self-link https://ddlbase.com/rss.php
  - [3] 2026-10-23: 'Mirror 1: Link 1', 'Mirror 2: Link 2', '(login for more mirrors)', MediaInfo block and 23.67 GiB filesize
  - [4] 2026-10-23: 
  - [4] 2026-10-30: robots.txt allows every crawler on every path ('Allow: /') and names the sitemap https://ddlbase.com/sitemap.xml | capture: sha256:aa35174fcfab6e690884252a9d1e703fc8e50e48ef6a7e57c2a63ca53148d672 | quote: Allow: /
  - probe:https://ddlbase.com/robots.txt 2026-10-30: a GET of https://ddlbase.com/robots.txt answered HTTP 200 with 128 bytes of text/plain on 2026-10-30 | capture: sha256:f9c08cd6cb942d66931a6a82c9ee968e3b4e8975129a8c0c446e0562c3160afb | quote: "bytes": 128
- sources:
  - [1] https://ddlbase.com/rss
  - [2] https://ddlbase.com/
  - [3] https://ddlbase.com/post/45631/gebo-and-the-shadow-2012-bluray-1080p-dts-hd-ma-5-1-avc-remux-framestor
  - [4] https://ddlbase.com/robots.txt
