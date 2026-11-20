# KrakenFiles

> krakenfiles.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/krakenfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/krakenfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KrakenFiles

- `storage/krakenfiles` | fails-quota | evidence documented | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:15.277Z (live) | stale on 2026-12-04
- url https://krakenfiles.com
- free tier: The homepage advertises 'Unlimited Disk Space'; the premium page lists a registered (free) account at a 5 GB maximum file size and a 3 months non-downloaded file lifetime, with the safety storage figure left blank. No numeric free total quota is published. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 500 MB per file | bytes: 500000000 | source: [1] | note: not stated
- retention: Non-downloaded files lifetime: 1 month (non-registered), 3 months (registered), up to 4 months (premium), applied to files above the safety storage. | days: 30 | source: [1] | note: not stated
- egress: Free downloads speed-limited ('We need to limit download speed for keep our servers online 24/7'); no GB cap published. | metered: no
- identity: email
- interface: rest
- limits:
  - per-ip-shaping: Speed-limited downloads [1]
  - per-object-cap (binding): 500 MB per file [1]
  - retention-clamped: Retention: 1 month [1]
- limits note: 500 MB per file for anonymous/private; larger downloads require a registered account. Retention: 1 month inactive for unregistered, 3 months registered, 5 months premium. TTL grows with downloads/plays.
- interface detail: rest
- tooling: Documented API: GET /api/server/available returns {url, serverAccessToken}; POST {url} multipart with serverAccessToken (+ optional X-AUTH-TOKEN for account uploads).
- composes with: Paid plans in USD for 1 year: Basic 500 GB safety storage $119.99, Pro 2 TB $215.99, MAX 6 TB $239.99; billed per term. Anonymous uploads allowed without X-AUTH-TOKEN, so unlimited identities x the per-file cap. The per-file cap is the binding constraint; you would shard.
- reliability: GET /api/server/available returned a JSON answer naming the upload node hs11.krakencloud.net on 2026-11-03, and a TCP connect to hs11.krakencloud.net:443 was refused, so uploads through the API are unconfirmed. Free downloads are speed-limited.
- notes: Marketed as 'unlimit drive'; free registered users get unlimited file count with a 500 MB per-file ceiling for private files. No numeric total quota published.
- evidence note: documented: the plan prices and storage tiers, the registered-account column (5 GB file size, 3 months lifetime, no safety storage figure) and the premium lifetime are quoted from https://krakenfiles.com/premium; the 1/3/5 month lifetimes and the sign-up email message from https://krakenfiles.com/faq; the private-file ceiling from https://krakenfiles.com/terms; the unlimited disk space claim from https://krakenfiles.com/ (all read 2026-11-03). The vendor pages disagree on the per-file size (terms against premium page) and on the premium lifetime (FAQ against premium page); the upload-node findings come from an API probe and a TCP probe, not from vendor pages
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Marketed as 'unlimit drive'; free registered users get unlimited file count with a 500 MB per-file ceiling for private files. No numeric total quota published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'maximum size of the user's private files cannot exceed 500MB'; anonymous users 'may not ... download files exceeding 500MB'
  - [3] 2026-10-21: 'not been downloaded for at least 1 month for non-register user, 3 months register users and 5 month for premium'
  - [4] 2026-10-21: probe: GET -> 200 {"status":200,"data":{"url":"https://hs7.krakencloud.net/api/file","serverAccessToken":"..."}} but POST to hs6.krakencloud.net:443 -> connect timeout after 21s
  - [5] 2026-11-03: the registered-account column states a 5 GB file size and 3 months lifetime and no safety storage figure | capture: sha256:6fbcf3dd4b22881a9a01c52b9df69be0c282853b6d96605002412ac8d935b651 | quote: Register user - Max file size 5 GB - Safety storage - Non downloaded files lifetime 3 months
  - [5] 2026-11-03: the premium column states up to 4 months | capture: sha256:6fbcf3dd4b22881a9a01c52b9df69be0c282853b6d96605002412ac8d935b651 | quote: up to 4 months
  - [3] 2026-11-03: the FAQ states 5 months for premium, which differs from the premium page | capture: sha256:6cc2a6048c993fff837153aef1c9a3ef0af65bafb32291228f4e45f0ad643f02 | quote: The file has not been downloaded for at least 1 month for non-register user, 3 months register users and 5 month for premium account.
  - [2] 2026-11-03: the terms state a 500MB ceiling for private files, which differs from the 5 GB on the premium page | capture: sha256:fcb0b9a6e09335de76994245ebb0a087ad0b6e6f9a08390c9c0c168e4bfafe86 | quote: provided that the maximum size of the user's private files cannot exceed 500MB
  - [1] 2026-11-03: the homepage advertises unlimited disk space | capture: sha256:d8d3d95cefcabf9a7f11160085a98df8367272bb6c038695de42f712ea7445c9 | quote: Unlimited Disk Space
  - [5] 2026-11-03: the MAX plan (6 TB safety storage) costs $239.99 for 1 year | capture: sha256:2576f3d28f277f77f4c67791438ce03f14066a2e36eff8006eeaa5c7d3e96319 | quote: <option value="1_year">1 year - $239.99 ($19.99/mo)</option>
  - [5] 2026-11-03: the Basic plan (500 GB safety storage) costs $119.99 for 1 year | capture: sha256:2576f3d28f277f77f4c67791438ce03f14066a2e36eff8006eeaa5c7d3e96319 | quote: <option value="1_year" data-select2-id="14">1 year - $119.99 ($9.99/mo)</option>
  - [5] 2026-11-03: the Pro plan (2 TB safety storage) costs $215.99 for 1 year | capture: sha256:2576f3d28f277f77f4c67791438ce03f14066a2e36eff8006eeaa5c7d3e96319 | quote: <option value="1_year">1 year - $215.99 ($17.99/mo)</option>
  - [3] 2026-11-03: registration is a form confirmed by an email message | capture: sha256:6cc2a6048c993fff837153aef1c9a3ef0af65bafb32291228f4e45f0ad643f02 | quote: If you complete register form and email message doesn't receive please check SPAM folder in your mailbox.
  - probe:hs11.krakencloud.net:443 2026-11-03: the TCP connect to hs11.krakencloud.net:443 failed (connection refused) | capture: sha256:8261a2bb38ffa9ec552f642f5441842373e8be056e5d7df2cc3ff07120041e51 | quote: "ok": false
  - probe:krakenfiles.com-api-server-available 2026-11-03: the API names hs11.krakencloud.net as the upload node | capture: sha256:c620282ba7fc107d7dcd9de1f45ff94808330f7472c53fab6cae93df967d469e | quote: hs11.krakencloud.net
  - [5] 2026-11-03: the largest paid plan has up to 6 TB of safety storage, below the 10 TiB need, and the free columns carry no storage figure | capture: sha256:6fbcf3dd4b22881a9a01c52b9df69be0c282853b6d96605002412ac8d935b651 | quote: up to 6 TB
  - [5] 2026-11-03: the vendor page was read and quoted on 2026-11-03: the registered-account column states a 5 GB file size and 3 months lifetime and no safety storage figure | capture: sha256:6fbcf3dd4b22881a9a01c52b9df69be0c282853b6d96605002412ac8d935b651 | quote: Register user - Max file size 5 GB - Safety storage - Non downloaded files lifetime 3 months
- sources:
  - [1] https://krakenfiles.com/
  - [2] https://krakenfiles.com/terms
  - [3] https://krakenfiles.com/faq
  - [4] https://krakenfiles.com/api/server/available
  - [5] https://krakenfiles.com/premium
