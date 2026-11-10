# Neocities

> neocities.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neocities/ | JSON https://fshy.ajam.dev/api/v1/entity/neocities.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Neocities

- `storage/neocities` | qualifies-with-caveat | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://neocities.org
- free tier: Free: 1 GB storage, 200 GB/month bandwidth, WebDAV and API on Free (WebDAV is listed on the Supporter table as a Free-tier feature). | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free plan includes a 200 GB per month soft bandwidth cap (~6.6 GB per day). Terms state: 'Don't worry—these are soft limits. Temporary surges are fine, we won't take your site down automatically'. | metered: no | free allowance: 200 GB per month
- identity: institution
- interface: rest, webdav, rclone, cli
- limits note: 1 GB per site on Free (50 GB Supporter); 200 GB/month bandwidth on Free; file-type restrictions on Free (no arbitrary binary types. 'No File Upload Type Restrictions' is a Supporter-only row); API requires a key per site.
- interface detail: rest
- tooling: Documented REST API: POST /api/upload (multipart, Bearer API key), plus WebDAV and an official CLI; rclone has no neocities backend but the WebDAV mount covers it.
- composes with: 1 GB per site x unlimited sites per account ('Multiple Site Creation' is listed as a free feature) x unlimited free accounts. 20 TiB = 20,480 sites. Operationally absurd, so this only works as a shard for a small hot set, not the archive.
- reliability: Bandwidth is internally enforced and will throttle, not delete; static file serving goes through Cloudflare with a 300s edge cache.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: plan table: 'Storage 1 GB / 50 GB', 'Bandwidth 200 GB / 3000 GB', WebDAV listed under Supporter-only features
  - [2] 2026-10-21: 'curl -H "Authorization: Bearer YOUR_API_KEY" -F "hello.html=@local.html" https://neocities.org/api/upload' (documented programmatic upload)
  - [3] 2026-10-21: probe: curl -D - -> 200, Content-Type: image/svg+xml, Cache-Control: max-age=300, Server: cloudflare
  - [4] 2026-10-21: probe: curl -> {"result":"error","error_type":"invalid_auth"} (API is live and key-gated, not open)
- sources:
  - [1] https://neocities.org/supporter
  - [2] https://neocities.org/api
  - [3] https://neocities.org/img/neocities-logo.svg
  - [4] https://neocities.org/api/info?site=neocities

## neocities as the archive tier

- `storage/neocities-as-the-archive-tier` | fails-egress | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:31.182Z (live) | stale on 2026-11-19
- url https://neocities.org/supporter
- free tier: none reachable: 1 GB per site and 200 GB/month bandwidth per site means 20 TiB would need 20,480 sites and would still be bandwidth-starved; Free also restricts uploadable file types ('No File Upload Type… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Free: 200 GB bandwidth; Supporter (USD 5/mo): 3000 GB; the page states no overage price and no billing period for the figures. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the Free (1 GB storage, 200 GB bandwidth) and Supporter (50 GB storage, 3000 GB bandwidth) columns were read on 2026-11-03 at https://neocities.org/supporter. The page does not state the period of the bandwidth allowance or whether it is per site: unverified, so the per-site monthly reading that decides the verdict is not documented.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: 1 GB per site and 200 GB/month bandwidth per site means 20 TiB would need 20,480 sites and would still be bandwidth-starved; Free also restricts uploadable file types ('No File Upload Type…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 1 GB per site and 200 GB/month bandwidth per site means 20 TiB would need 20,480 sites and would still be bandwidth-starved; Free also restricts uploadable file types 'No File Upload Type R
  - [1] 2026-11-03: Free allows 200 GB and Supporter 3000 GB of bandwidth | capture: sha256:40141a59234b845a5bcc52fb5464a47e3fb5493e0b7c24ea052e854805a88158 | quote: | Bandwidth | 200 GB | 3000 GB |
  - [1] 2026-11-04: the Free plan has 200 GB and Supporter 3000 GB of bandwidth | capture: sha256:40141a59234b845a5bcc52fb5464a47e3fb5493e0b7c24ea052e854805a88158 | quote: | Bandwidth | 200 GB | 3000 GB |
- sources:
  - [1] https://neocities.org/supporter
