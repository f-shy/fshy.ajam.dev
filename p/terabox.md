# TeraBox

> terabox.com | Storage, Netdisk and pan; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/terabox/ | JSON https://fshy.ajam.dev/api/v1/entity/terabox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TeraBox (Baidu / Flextech)

- `storage/terabox` | qualifies | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:24.769Z (live) | stale on 2026-12-10
- url https://www.terabox.com
- disagrees on identity_kind: `storage/terabox` says institution, `storage/terabox-2` says email
- disagrees on verdict: `storage/terabox` says qualifies, `storage/terabox-2` says fails-identity
- free tier: Free plan: 1024 GB (limited-time), up to 4GB per file, up to 20 files; Premium: 2048 GB; Premium+: 5TB of massive storage | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB/file | bytes: 4000000000 | source: [1] | note: 1024 GB (limited-time), up to 20 files, up to 4GB.
- retention: Share links can be set for 7 days, 30 days or permanent validity. | days: 7 | source: [1] | note: You can choose an expiry period: 7 days, 30 days or permanent validity.
- egress: Direct share links, no per-GB fee; free accounts throttled (~2-5 GB/day measured by third parties) and one download at a time | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 4 GB/file [1]
- limits note: Share links can be set for 7 days, 30 days or permanent validity.
- interface detail: rest
- tooling: Unofficial web API (app_id=250528, jsToken) + rclone fork bclone / gulp79/rclone-extra (upstream PR #8508 still open); official Open Platform OAuth is partner-gated
- composes with: 1 TB per account, and a second account carries a second allowance; email/SSO signup keeps identity cost low, but the 4 GB/file free cap forces splitting
- reliability: no official rclone backend; free-tier daily download cap makes it archive-shaped, and the web API breaks when the client changes
- notes: 1024 GB free ('Network disk capacity limited to 1024GB' on the free column; '1TB Free Cloud Storage for Basic & 2TB Storage for Pro'); Premium/Pro 2048 GB
- evidence:
  - [1] 2026-10-21: 'Network disk capacity limited to 1024GB' free column; title '1TB Free Cloud Storage for Basic & 2TB Storage for Pro'
  - [2] 2026-10-21: and /thai/ and /vietnamese/ and /indonesian/ — all show '1024 GB' free, 2048 GB paid; the '5GB ... gratuito' strings belong to the OneDrive/Google Drive comparison rows
  - [3] 2026-10-21: crawl render shows 'Sign in with Google', 'Phone or Email', 'Registered with phone No.?'; raw HTML carries thirdLoginSdk {apple, kakao, google, line, facebook} and a dial-code phone widget
  - [4] 2026-10-21: probe: GET -> {"errmsg":"user not login","errno":-6}
  - [1] 2026-11-19: the free tier still states 1024 GB of network disk capacity | capture: sha256:fdd9ada1c9ac231b3214ede769721216e34ee07830156a0e2fea5016f44b9641 | quote: Network disk capacity limited to 1024GB
  - [1] 2026-11-19: the free column now labels 1024 GB as limited-time and adds a 5TB Premium+ tier | capture: sha256:fdd9ada1c9ac231b3214ede769721216e34ee07830156a0e2fea5016f44b9641 | quote: 1024 GB (limited-time)
  - [1] 2026-11-19: the Premium+ paid tier is 5TB | capture: sha256:fdd9ada1c9ac231b3214ede769721216e34ee07830156a0e2fea5016f44b9641 | quote: 5TB of massive storage
  - [3] 2026-11-19: the login page offers phone or email alongside Google sign-in | capture: sha256:d79c1e7ce55bde2fabdde5b107e07fb9ce8e0522a25d40c82ef3a2be64788c6e | quote: Phone or Email
  - [1] 2026-11-25: the free plan column lists 1024 GB, up to 20 files and up to 4GB | capture: sha256:fdd9ada1c9ac231b3214ede769721216e34ee07830156a0e2fea5016f44b9641 | quote: 1024 GB (limited-time) up to 20 files up to 4GB
  - [5] 2026-11-25: the share-link expiry period is selectable as 7 days, 30 days or permanent validity | capture: sha256:fa7a6af322e399a3e53e05dd65cc507288e1997e602d03634512647af39c1a96 | quote: For example, if you want to make the link available for 7 days, you can easily choose that time period. Or you can even decide to keep it active for 30 days or set it up as a permanent validity link.
  - [5] 2026-11-25: the share-link expiry period is chosen by the user from 7 days, 30 days or permanent validity | capture: sha256:fa7a6af322e399a3e53e05dd65cc507288e1997e602d03634512647af39c1a96 | quote: For example, if you want to make the link available for 7 days, you can easily choose that time period. Or you can even decide to keep it active for 30 days or set it up as a permanent validity link.
- sources:
  - [1] https://www.terabox.com/cloud-storage-pricing-plans
  - [2] https://www.terabox.com/portuguese/cloud-storage-pricing-plans
  - [3] https://www.terabox.com/login
  - [4] https://dm.1024terabox.com/api/quota?...&app_id=250528
  - [5] https://blog.terabox.com/how-long-do-terabox-links-last/

## TeraBox (terabox.com)

- `netdisk-pan/terabox` | qualifies-with-caveat | evidence documented | binding per-object-cap | category consumer-pan
- needs card no, phone no, ID no, institution no | verified 2026-11-25T14:05:48.228Z (live) | stale on 2026-12-17
- url https://www.terabox.com/
- free tier: 1024 GB of free cloud storage on registration | unit: GB | metered on: stored-bytes | read on: 2026-11-09 | source: [1] | note: the free allowance is 1024 GB and the pricing page labels it limited-time
- per-object cap: 4 GB per single file on the web for non-Premium users; Premium users can upload single files up to 128 GB from the app | source: [2] | note: the vendor FAQ states 4 GB per file for non-Premium users and 128 GB for Premium; the login page's 'Upload and share 20GB files on PC' is a marketing figure not reconciled with the FAQ
- retention: inactive files on free accounts are removed after 60 days; Premium files are retained indefinitely | days: 60 | source: [2]
- egress: multi-file downloads from the web app are limited to 500 MB, while single-file downloads have no size limit | metered: no | source: [2]
- identity: email | detail: the email path submits an email address, a password, a user name, a date of birth and a verification code; the payload carries no phone number, card or identity-document field
- interface: rest
- limits:
  - per-object-cap (binding): 4 GB per file for non-Premium users; 128 GB for Premium from the app [2]
- binding note: The 1024 GB quota is not the constraint; the 4 GB per-file cap for non-Premium users and the undocumented programmatic interface are, because the quota must be filled through many objects and no supported API is documented.
- tooling: no official public API documented; the OpenList project ships a reverse-engineered TeraBox driver that authenticates with a browser session cookie and is not maintained, so a reverse-engineered client mounts it with…
- composes with: 1 TiB free is the largest single-tier free quota in the consumer set, but every route to it is either an app or an undocumented API
- reliability: The landing page served a verification interstitial; the quota was read from the login page and the web app bundle instead.
- notes: The free allowance is 1024 GB and the pricing page labels it limited-time.
- extras:
  - access_mode: registration-gated
  - official_api: not documented
  - third_party_drivers: Cloudreve; AList/OpenList
- evidence:
  - [1] 2026-10-22: the page title and meta description returned by the reader were 'TeraBox - Free Cloud Storage Up To 1 TB, Send Large Files Online', and the final URL was /simple-verify with the body 'Verification code was entered incorrectly', so the landing page itself was not served
  - [3] 2026-10-22: '1024GB of FREE Cloud Storage' on registration, and 'Upload, store, and share big files up to 128 GB seamlessly'
  - [1] 2026-11-03: the vendor landing page, read through a firecrawl pin, states 1024 GB of cloud storage | capture: sha256:476fe1d864de41c12f801bc37154d465d11bd243f430fe93c2ee476b0540e399 | quote: 1024GB Cloud Storage
  - [1] 2026-11-03: the 128 GB upload figure applies to Premium users, so it is not the free plan's cap | capture: sha256:476fe1d864de41c12f801bc37154d465d11bd243f430fe93c2ee476b0540e399 | quote: Premium users can upload files up to 128 GB at a time.
  - [4] 2026-11-03: the OpenList TeraBox driver is reverse-engineered and not actively maintained | capture: sha256:ce3286ea214026071ec8a91caf6aeb136ad5179c2d9722a71fbbc1ff19ff0b6f | quote: This interface is a reverse-engineered interface based on legacy products.
  - [2] 2026-11-09: the registration payload names email, password, user name, date of birth and verification code, with no phone, card or identity-document field | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: verifyParams:{email:"",pwd:"",uname:"",birthday:"",vcode:"",vcode_str:"",thrid_token:""}
  - [2] 2026-11-09: the sign-up screen offers 'Sign up with Email', so the identity kind is email | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: emailRegister:"Sign up with Email"
  - [5] 2026-11-09: the pricing page states a 1024 GB free allowance, labelled limited-time, which is above 500 GiB; the per-file cap and download conditions make the verdict qualifies-with-caveat | capture: sha256:6fccb1274246e7473e51617720a2ca7f04dbadddbce0ff8472805111f6aca272 | quote: 1024 GB (limited-time)
  - [6] 2026-11-09: the login page states 1024 GB free, so the quota was readable outside the landing page | capture: sha256:fce7086fe7f03be8c65f62a40d613a53bfab2b9b81e6853a1a4c8fd16d0600fc | quote: # The first cloud disk providing 1024GB for free
  - [2] 2026-11-09: the vendor FAQ states a 4 GB single-file upload limit for non-Premium users on the web and 128 GB for Premium from the app | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: Web: The maximum upload limit for a single file is 4GB. Premium can use the Mobile App and Desktop App to upload single files not exceeding 128GB.
  - [2] 2026-11-09: the vendor FAQ states that inactive files on free accounts are removed after 60 days and Premium files are retained indefinitely | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: p8:"Inactive files for individuals using the service at no cost will be removed after a 60-day period, while those with a premium subscription will have their files retained indefinitely."
  - [2] 2026-11-09: the sign-up screen offers email, Google, Facebook and Apple registration | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: titleRegister:"Sign up",facebookRegister:"Sign up with Facebook",googleRegister:"Sign up with Google",appleRegister:"Sign up with Apple",emailRegister:"Sign up with Email"
  - [2] 2026-11-09: mobile-number login is unavailable to unregistered users and is being discontinued | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: phoneNumberDiscontinuedDetailText:"Mobile number login is temporarily unavailable for unregistered users, and this option will be discontinued soon.
  - [2] 2026-11-09: a file over 100 MB must use PC Desktop for high-speed downloads on the web | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: over100M:"File exceeds 100MB. Please use PC Desktop for high-speed downloads"
  - [2] 2026-11-09: the web app's share download string caps multi-file downloads at 500 MB and states that a single file is not limited | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: shareDownloadExceed:"The download of multi-file has an upper limit of 500MB, while the download of a single file is not limited"
  - [7] 2026-11-09: a registered account gets 1 TB of free cloud space | capture: sha256:fc31a1dbe41d33006b83afe040bb8bb57d26c6af987ccbe521bea6bc3d90126e | quote: Once you have registered your account and log in, 1 TB of free cloud space will be completely yours!
  - [8] 2026-11-09: phone numbers are no longer supported for registering new accounts | capture: sha256:2845eaffdef6862fbc89f1c1439a7a6b84bec90c7f4f4f4e429bec4796a57d50 | quote: But now TeraBox no longer supports phone numbers to register new accounts.
  - [9] 2026-11-09: registration takes an email address and a password | capture: sha256:104eaa0388f1846e632c8929427e0d83a3a3efed3599b29be0651d34a869ff03 | quote: Enter your email address and password.
  - [2] 2026-11-09: the batch download check compares the size in MB against 500 for type batch, so the enforced multi-file cap is 500 MB; the over500M message text states 3 GB but is display text, not the compared threshold | capture: sha256:f41c9420fba9da96db1fefae6027c398dbeb2566ab634bc12a9eae252cd0f26e | quote: if(t=this.len/1048576,n=500,!(t>n&&"batch"===this.dlinkParams.type))
  - [5] 2026-11-25: the pricing page lists 1024 GB of free storage | capture: sha256:fdd9ada1c9ac231b3214ede769721216e34ee07830156a0e2fea5016f44b9641 | quote: 1024 GB (limited-time)
- sources:
  - [1] https://www.terabox.com/
  - [2] https://s5.teraboxcdn.com/fe-opera-static/node-static-v4/fe-webv4-main/js/main.ebd09b45.js
  - [3] https://play.google.com/store/apps/details?hl=en_US&id=com.dubox.drive
  - [4] https://doc.oplist.org/guide/drivers/terabox
  - [5] https://www.terabox.com/cloud-storage-pricing-plans
  - [6] https://www.terabox.com/login
  - [7] https://blog.terabox.com/how-do-i-get-a-free-terabox-account
  - [8] https://blog.terabox.com/how-to-change-my-password
  - [9] https://blog.terabox.com/how-do-i-register-on-terabox

## terabox (kr/id/jp localisation)

- `storage/terabox-2` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:24.518Z (live) | stale on 2026-12-04
- url https://www.terabox.com/indonesian
- disagrees on identity_kind: `storage/terabox` says institution, `storage/terabox-2` says email
- disagrees on verdict: `storage/terabox` says qualifies, `storage/terabox-2` says fails-identity
- free tier: 1024GB of free cloud storage is advertised on the localized page (Ruang penyimpanan cloud 1024GB); the /indonesian page now loads normally instead of the old verification stub | unit: GB | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub…
  - dead_end.retry_when: if the registration gate opens to a foreign individual
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub…
  - [2] 2026-10-21: cited as the basis of the rejection: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub, a
  - [3] 2026-10-21: cited as the basis of the rejection: Same 1 TB as everywhere else, and the localised pages are the interesting part: the /indonesian URL now redirects to /simple-verify with a 'Verification code was entered incorrectly' stub, a
  - [1] 2026-11-19: the localized page currently states a 1024GB free cloud-storage allowance | capture: sha256:ec9895a99fed0e75589101fd92f164839779793cdb5c03486b8cb1b701b8fe12 | quote: Ruang penyimpanan cloud 1024GB
  - [1] 2026-11-19: the headline is denominated in GB | capture: sha256:ec9895a99fed0e75589101fd92f164839779793cdb5c03486b8cb1b701b8fe12 | quote: Ruang penyimpanan cloud 1024GB
  - [1] 2026-11-19: the localized page still states the 1024GB allowance | capture: sha256:6197c6cdff2a88b8b6ff1f7754e347f8d0876d45865785f6ffbe38e3d640556f | quote: Ruang penyimpanan cloud 1024GB
  - [4] 2026-11-19: a verification-code gate still stands at /simple-verify, so the bytes are not anonymously reachable | capture: sha256:a6f12242d5519ee5c71e5a0a0a1252811e7a204ea7c64fcbaf81e6562e55432a | quote: Verification code was entered incorrectly
- sources:
  - [1] https://www.terabox.com/indonesian
  - [2] https://www.terabox.com/english
  - [3] https://bokgoon.com/free-cloud-storage-services/
  - [4] https://www.terabox.com/simple-verify
