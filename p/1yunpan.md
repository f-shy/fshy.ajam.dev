# 1yunpan

> 1yunpan.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/1yunpan/ | JSON https://fshy.ajam.dev/api/v1/entity/1yunpan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 1yunpan (易云盘)

- `netdisk-pan/1yunpan` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category Cloudreve-family drive with native S3 and WebDAV
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:59.760Z (inherited) | stale on 2026-11-19
- url https://www.1yunpan.com
- price Pro at CNY 29/month is 1 TB storage and 10 TB/month; the free tier is not purchasable and has no per-terabyte price | parsed USD 4.35/mo
- free tier: 100 GB on registration plus 400 GB earned by daily check-in, so 500 GB is reachable on a free account but only through a login streak. The free plan also carries 1 TB of monthly bandwidth | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1] | note: the pricing block reads '100GB Storage +400GB via check-in' and the check-in panel says 'up to 500GB free'
- per-object cap: 32212254720 bytes (30 GiB) per upload, as the site's published config.json sets limit.upload_allow_max_size | bytes: 32212254720 | source: [1]
- retention: Not published. The 400 GB is drip-fed by daily check-in, so an account that stops logging in cannot earn the rest | source: [1]
- egress: 1 TB per month on the free Starter tier, published, then paid. Direct links are served from per-user subdomains with Cache-Control: public, max-age=15552000 | metered: yes | free allowance: 1 TB per month | source: [1]
- identity: email | detail: an email address at one of a fixed list of domains (including gmail.com, qq.com, icloud.com, 163.com and yahoo.com) and an emailed six-digit code; the register form has username, password, confirm, email, email_code and an agreement checkbox with no phone or mobile input present
- interface: s3, webdav, rest
- limits:
  - per-ip-shaping (binding): 1 TB of bandwidth per month on the free tier [1]
  - write-gated: 400 of the 500 GB is granted 5 GB at a time by daily check-in [1]
- binding note: 1 TB a month corresponds to 33 GB a day, meaning the transfer allowance binds before the 500 GB storage ceiling does under sustained extraction.
- tooling: rclone s3 against s3.1yunpan.com, rclone webdav, s3cmd, any S3 SDK, and a raw GET on the per-user host. Registration is an email address and an emailed six-digit code with no phone field in the DOM; Google and GitHub OAuth are also offered
- composes with: The strongest chaining candidate in its group: a free bucket that answers both S3 and WebDAV drops into a chunk-and-replicate scheme as a first-class target with no AList shim. The 1 TB monthly bandwidth is the binding number, not the 500 GB of space
- reliability: Reads are real: a 1,326,142,372-byte MP4 came back byte-exact against Content-Length with Range honoured, and a ranged GET returned 206 with a correct Content-Range. The site notice states that files uploaded between 2026-10-05_22:00:00 and 2026-10-30_23:59:59 are temporarily not downloadable and that file upload is temporarily stopped, and config.json sets upload.temporarily_disabled to true. The 400 GB is streak-gated, so an account that stops logging in loses headroom
- notes: 500 GB reachable on an email address with no phone is unusual, and the S3 endpoint answering real S3 error semantics is what makes it useful: rclone, restic and Duplicati can each treat an account as a bucket. The check-in ladder is a daily quota rather than a wall-clock trial, so it is repeatable, but it also means the account is worth less the moment the streak stops.
- extras:
  - access_mode: registration-gated
  - free_tier_exists: yes
  - check_in_bytes: 429496729600
  - bandwidth_bytes_month: 1099511627776
  - oauth: email; google; github
  - s3_endpoint: https://s3.1yunpan.com
  - fronting: direct links carry Server: cloudflare and CF-Cache-Status: DYNAMIC
  - fx.pair: USD/CNY
  - fx.rate: 6.6702
  - fx.date: 2026-10-23
- evidence:
  - [1] 2026-10-21: rendered pricing 'Starter CNY 0/month, 1TB Monthly Bandwidth, 100GB Storage +400GB via check-in'
  - probe:https://id5mjj37zbn85c.1yunpan.com/Videos/test.mp4 2026-10-21: HTTP 200, Content-Length 1326142372, 1326142372 bytes downloaded, sha256 04b36ea0dc7a3bac5776b37432e16ad6d5a560a7da32b1ad7efbf00bfb5b6be7, so a 1.33 GB object came back byte-exact
  - probe:https://id5mjj37zbn85c.1yunpan.com/Videos/test.mp4#range 2026-10-21: Range bytes=1000000-1000255 returned HTTP 206 with Content-Range bytes 1000000-1000255/1326142372 and 256 bytes
  - probe:https://s3.1yunpan.com/ 2026-10-21: HTTP 400 with S3 XML InvalidArgument / Invalid path, and /testbucket returned 403 AccessDenied / Missing AWS authentication, so it is a real S3 implementation
  - probe:https://s3.1yunpan.com/testbucket 2026-10-21: 403 AccessDenied with real S3 error semantics rather than a stub
  - [2] 2026-10-21: the form DOM has username, password, confirm, email, email_code and 2FA support, and zero phone or mobile inputs
  - probe:https://www.1yunpan.com/config.json 2026-11-03: the site config sets the per-upload size limit to 32212254720 bytes | capture: sha256:6ce2e8085f6efcb6680948e05ef4cd11edc846997f85dc9948a0f5210d19570d | quote: "upload_allow_max_size": 32212254720
  - probe:https://www.1yunpan.com/config.json 2026-11-03: the config disables registration with any email domain and carries an email_whitelist of permitted domains | capture: sha256:6ce2e8085f6efcb6680948e05ef4cd11edc846997f85dc9948a0f5210d19570d | quote: "allow_all_email_to_register": 0,
  - [1] 2026-11-03: the front page carries a notice that files uploaded in a stated window are temporarily not downloadable, older files are unaffected, and file upload is temporarily stopped | capture: sha256:ba040c4c5957d054c511d27c79634b26062899734df270bc6760b45649a73604 | quote: 技术故障导致 2026-10-05_22:00:00 至 2026-10-30_23:59:59 期间上传的文件暂时无法下载，技术人员正在维护系统并从冷备份中恢复，我们会尽快恢复文件的正常下载。对于 2026-10-05:20:00:00 以前上传的文件均可正常下载未受影响。系统目前暂时停止文件上传功能。
  - probe:https://www.1yunpan.com/config.json 2026-11-03: the config the web app loads sets upload.temporarily_disabled to true | capture: sha256:6ce2e8085f6efcb6680948e05ef4cd11edc846997f85dc9948a0f5210d19570d | quote: "temporarily_disabled": true,
  - probe:https://id5mjj37zbn85c.1yunpan.com/Videos/test.mp4#head 2026-11-03: a HEAD on the demo MP4 answers HTTP 200 with Content-Length 1326142372 | capture: sha256:da84e4fbf59e71966245c47f355e5a175e03077211cf150a630a5f19f257c8cc | quote: "content-length": "1326142372"
  - probe:https://id5mjj37zbn85c.1yunpan.com/Videos/test.mp4#range 2026-11-03: a ranged GET returns the matching Content-Range, so Range is honoured on the direct host | capture: sha256:1da5e49ad74c30c1fe7d4115f6729ff103ae67da1c292d1ba45f6223db94ece7 | quote: "content_range": "bytes 1000000-1000255/1326142372"
  - probe:https://s3.1yunpan.com/ 2026-11-03: the S3 endpoint answers an S3-shaped XML error body to an unauthenticated GET of the root | capture: sha256:d8a819a2a379f435a64e66d22fc3da77424bdfec19ba321be0deb450c663c239 | quote: <Message>Invalid path</Message>
  - [1] 2026-11-03: the front-page Starter plan lists 1 TB of monthly bandwidth | capture: sha256:8db69290d523f57ce63a5017f1035788ad618ef51cce49c294e25acefa49caec | quote: 1TB Monthly Bandwidth
  - [1] 2026-11-03: the front-page Starter plan still lists 100 GB of storage plus 400 GB via check-in | capture: sha256:8db69290d523f57ce63a5017f1035788ad618ef51cce49c294e25acefa49caec | quote: 100GB Storage +400GB via check-in
- sources:
  - [1] https://www.1yunpan.com/
  - [2] https://www.1yunpan.com/register
