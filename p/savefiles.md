# SaveFiles

> savefiles.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/savefiles/ | JSON https://fshy.ajam.dev/api/v1/entity/savefiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SaveFiles

- `debrid/savefiles` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file and video host (free account, premium) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://savefiles.com/
- free tier: Free account: 10480 MB maximum upload, 2000 GB of storage, unlimited download volume, 1500 Kbytes/sec download speed, files expire after 12 days without downloads. | unit: GB | metered on: stored-bytes | read on: 2026-11-03 | source: [1]
- per-object cap: 10480 MB per file on Free; 20480 MB on Premium | source: [1]
- retention: 12 days with no downloads on Free; 28 days on Premium | days: 12 | source: [1]
- egress: Download volume is Unlimited on both tiers; download speed is 1500 Kbytes/sec on Free and 2000 Kbytes/sec on Premium. | metered: no | free allowance: not published | source: [1]
- identity: email | detail: The registration form asks for a username, an e-mail, a password and a reCAPTCHA check. Premium is paid by Bitcoin, Litecoin, PayPal or Stripe.
- interface: rest
- limits:
  - per-object-cap: 10480 MB per file on Free, 20480 MB on Premium [1]
  - per-ip-shaping: download speed 1500 Kbytes/sec on Free, 2000 Kbytes/sec on Premium [1]
  - retention-clamped (binding): files expire after 12 days with no downloads on Free, 28 days on Premium [1]
  - volume-quota: 2000 GB of storage on Free, 10000 GB on Premium [1]
- binding note: A 12-day no-download expiry binds before the 2000 GB storage or the per-file cap does.
- interface detail: Web upload; the site links an API Docs page that was not read. Remote URL upload is 15 threads on Free and 200 on Premium.
- tooling: Browser upload, remote URL upload and an API Docs page (unread).
- composes with: Premium is $29.99 for 30 days, $69.99 for 90 days, $149.99 for 180 days, $299 for 365 days; it raises the storage to 10000 GB and the per-file cap to 20480 MB.
- reliability: Files expire 12 days after the last download on the free tier; the registration form sits behind a reCAPTCHA.
- notes: Cheapest paid tier is the 30-day Premium at 29.99 USD.
- evidence note: Limits and prices read on the vendor premium and registration pages. Whether a file can be fetched without a browser challenge was not probed.
- evidence:
  - [1] 2026-11-03: per-file cap is 10480 MB on Free and 20480 MB on Premium | capture: sha256:0be609b06f7cad0194316607b0f4f0b8cb504fea0962b4674622c38f45b99908 | quote: Max upload file size 10480 MB 20480 MB
  - [1] 2026-11-03: storage is 2000 GB on Free and 10000 GB on Premium | capture: sha256:0be609b06f7cad0194316607b0f4f0b8cb504fea0962b4674622c38f45b99908 | quote: Storage space 2000 GB 10000 GB
  - [1] 2026-11-03: download speed is 1500 Kbytes/sec on Free | capture: sha256:0be609b06f7cad0194316607b0f4f0b8cb504fea0962b4674622c38f45b99908 | quote: Download speed 1500 Kbytes/sec 2000 Kbytes/sec
  - [1] 2026-11-03: free files expire after 12 days with no downloads | capture: sha256:0be609b06f7cad0194316607b0f4f0b8cb504fea0962b4674622c38f45b99908 | quote: File expiration period 12 days no downloads 28 days no downloads
  - [1] 2026-11-03: the cheapest premium period is 30 days at 29.99 USD | capture: sha256:0be609b06f7cad0194316607b0f4f0b8cb504fea0962b4674622c38f45b99908 | quote: 30 days 29.99 USD
  - [2] 2026-11-03: registration asks for a username, e-mail and password with a reCAPTCHA | capture: sha256:ad689a4206a6c2661275660645f47a470634dc66487c8a2666801267daac301c | quote: Username E-mail Password Retype Password Recaptcha requires verification.
- sources:
  - [1] https://savefiles.com/premium
  - [2] https://savefiles.com/?op=registration
