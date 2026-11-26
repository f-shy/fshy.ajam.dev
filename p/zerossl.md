# ZeroSSL

> zerossl.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zerossl/ | JSON https://fshy.ajam.dev/api/v1/entity/zerossl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZeroSSL

- `domains-dns/zerossl` | qualifies-with-caveat | evidence documented | binding none | category certificate authority | tier ACME (all plans)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:09.557Z (live) | stale on 2026-12-04
- url https://zerossl.com/documentation/acme/
- free tier: unlimited 90-day certificates over ACME at no charge, with multi-domain and wildcard certificates; the Free plan's own dashboard allowance is 3 90-day certificates | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: a certificate name may have at most six labels below the public suffix, the wildcard asterisk included; a deeper name needs the ZeroSSL REST API instead of ACME | source: [1]
- retention: ACME certificates are valid 90 days (the directory is named DV90) and must be renewed | days: 90 | source: [1]
- egress: no charge | metered: no | source: [1]
- identity: email | detail: an account made with an email address and a password; no card is needed for the Free plan; the ACME client then needs EAB credentials from that account (https://app.zerossl.com/signup/free, https://zerossl.com/pricing/)
- interface: rest
- limits:
  - request-rate: no ACME rate limit is published: the ACME feature page says 'No Rate Limits' while the documentation says abusive use can be limited or blocked; no number is given [2]
  - request-rate: EAB credential creation is limited to a maximum per user per day (the number is unpublished); the credentials are reusable, so one set normally suffices [1]
  - per-object-cap: at most 6 labels below the public suffix per name, counting a wildcard asterisk [1]
- binding note: no published number binds ACME issuance; the unpublished per-user daily cap on EAB credential creation does not bind a normal client because the credentials are reusable
- interface detail: ACME v2 at https://acme.zerossl.com/v2/DV90 with external account binding required (EAB key id and HMAC key made in the dashboard or by GET api.zerossl.com/acme/eab-credentials?access_key=...); a separate ZeroSSL REST API with an access key also exists
- tooling: acme.sh (owned by ZeroSSL), Caddy and CertMagic, dehydrated, win-acme, getssl, acme-companion, any ACME client that supports EAB
- composes with: a second free ACME CA beside Let's Encrypt: the same 90-day certificates with wildcard names and no published per-domain weekly cap, signed by a different CA, so an ACME client can fail over between the two
- reliability: unverified: no outage history or abuse-block rate was read
- notes: ZeroSSL sells paid plans with more annual certificates, which the ACME allowance does not need. The free dashboard allowance of 3 certificates and the unlimited ACME allowance are different channels, both stated by ZeroSSL.
- evidence note: the ACME documentation, the ACME feature page, the pricing FAQ, the sign-up page and the EAB error table were captured and quoted; the live ACME directory answered 200 with externalAccountRequired true. Whether a wildcard name needs the DNS-01 challenge is unverified: the ZeroSSL pages read do not say.
- evidence:
  - [1] 2026-11-03: ACME certificates are free, unlimited in count, valid 90 days, multi-domain and wildcard | capture: sha256:54ff0a15b540f0871d99b5d107a07c48d59e8c51b375a92b203ea5cf1281f739 | quote: By using ZeroSSL's ACME feature, you will be able to generate an unlimited amount of 90-day SSL certificates at no charge, also supporting multi-domain certificates and wildcards.
  - [1] 2026-11-03: no number is published; abusive use can be limited or blocked | capture: sha256:54ff0a15b540f0871d99b5d107a07c48d59e8c51b375a92b203ea5cf1281f739 | quote: malicious users can be limited or even blocked.
  - [1] 2026-11-03: a name may have at most six labels below the public suffix over ACME | capture: sha256:54ff0a15b540f0871d99b5d107a07c48d59e8c51b375a92b203ea5cf1281f739 | quote: the maximum number of labels in subdomains is six, excluding the public suffix
  - [1] 2026-11-03: EAB credential creation has an unpublished per-user daily cap | capture: sha256:54ff0a15b540f0871d99b5d107a07c48d59e8c51b375a92b203ea5cf1281f739 | quote: EAB credentials are limited to a maximum per user/per day.
  - [2] 2026-11-03: the ACME feature page states no rate limits | capture: sha256:1e097abdefa97a875b27bc92be51d6e4cdca6eacff1db26a216528600fad2f25 | quote: No Rate Limits
  - [2] 2026-11-03: ACME automation needs no card | capture: sha256:1e097abdefa97a875b27bc92be51d6e4cdca6eacff1db26a216528600fad2f25 | quote: It's free. No credit card required.
  - [3] 2026-11-03: the Free plan needs no card | capture: sha256:b2116692e1750d976b5b97e994073ec4e005310f455a16a9a7b00b3a97306fa9 | quote: To get started using the Free Plan, a credit card will not be required.
  - [3] 2026-11-03: ACME 90-day certificates are free on all plans | capture: sha256:b2116692e1750d976b5b97e994073ec4e005310f455a16a9a7b00b3a97306fa9 | quote: you can use our free 90-day ACME certificates
  - [3] 2026-11-03: the Free plan row lists 3 90-day certificates for the dashboard, apart from the ACME allowance | capture: sha256:b2116692e1750d976b5b97e994073ec4e005310f455a16a9a7b00b3a97306fa9 | quote: 3 90-Day Certificates
  - [4] 2026-11-03: Free plan sign-up asks for an email address and a password | capture: sha256:ffad40246208ce60c3c21fec9941a0ce581aa3a6ca5771e017c0a8a1873efcc9 | quote: Enter an email address and password to proceed.
  - [5] 2026-11-03: a per-day EAB credential cap is enforced with error 2904 | capture: sha256:85234c1e0affb51c8b4166e37451cee507dc3b603819872d3fa3443608326772 | quote: You have created too many EAB credentials today.
  - probe:https://acme.zerossl.com/v2/DV90 2026-11-03: the ACME directory is live (HTTP 200, 712 bytes) and requires external account binding | capture: sha256:4603550b5c519a2ae25d18a6bf060e80207e1ea538553509ae7c7071e46e70cf | quote: "externalAccountRequired": true
- sources:
  - [1] https://zerossl.com/documentation/acme/
  - [2] https://zerossl.com/features/acme/
  - [3] https://zerossl.com/pricing/
  - [4] https://app.zerossl.com/signup/free
  - [5] https://zerossl.com/documentation/acme/error-codes/
