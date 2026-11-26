# Payhip

> payhip.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/payhip/ | JSON https://fshy.ajam.dev/api/v1/entity/payhip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Payhip

- `storage/payhip` | qualifies | evidence reported | binding per-object-cap | category Digital-product fulfilment (sell any file)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:14.040Z (live) | stale on 2026-12-10
- url https://payhip.com
- free tier: Explicit, from their own page: 'No, we have no storage or bandwidth limits. We only have a 5GB per file limit.' Help centre repeats: 'Payhip supports a maximum file size of 5GB per digital product.' | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: maximum file size of 5GB per digital product | bytes: 5000000000 | source: [1] | note: Each uploaded file can be up to 5GB in size; larger files can be split into multiple smaller files uploaded to the same product listing.
- retention: source: [1] | note: not stated
- egress: No, we have no storage or bandwidth limits. We only have a 5GB per file limit. | metered: no
- identity: email | detail: a first name, last name, email address and password on the free-account form. No card is asked for: the help centre adds card details only to upgrade a paid plan. No phone field is on the form.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 5GB per file [1]
- limits note: Per-object-cap 5 GB. The only limit they publish. Extension blocklist is a hard gate on ingress: EXE, ISO, DMG, VBS, SCR refused unless inside a ZIP. No aggregate quota.
- interface detail: Web upload. REST API + webhooks on paid plans; the digital-product upload itself is form-based.
- tooling: curl/browser; no first-class CLI.
- composes with: Each uploaded file can be up to 5GB; larger files can be split into multiple smaller files and uploaded separately to the same product listing.
- reliability: Serving path is fine; the operational risk is that a 'digital product' must be a listed product, and free products still sit behind a checkout page. Buyer link is emailed, not a stable public URL. So it is an archive/delivery tier, not a hot-link CDN.
- notes: The features page was read on 2026-11-19 and states no storage or bandwidth limit with a 5GB per-file ceiling.
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 5GB per digital product; EXE/ISO/DMG/VBS/SCR blocked unless zipped
  - [3] 2026-10-21: 'Free Forever' + 5% transaction fee, no monthly fee
  - [4] 2026-11-01: the free-account form asks for a first name, last name, email address and password only | capture: sha256:59140e5be20faa292153c27bdd6f75b527fc1cc63290f090479b762a8294dd56 | quote: Setup a free Payhip account to create a store. ... First Name ... Last Name ... Email Address ... Password
  - [1] 2026-11-01: the no-storage-limit statement and the 5 GB per-file ceiling are unchanged | capture: sha256:d3470891a7f805a500ff4c378581961db517462f8d3b7a90cf399e270ea5a0d1 | quote: No, we have no storage or bandwidth limits. We only have a 5GB per file limit.
  - probe:https://payhip.com/features/sell-digital-downloads 2026-11-11: the cited features page answered HTTP 403 with a Cloudflare challenge and no usable content | capture: sha256:f9290dcf3ece7627c907c645bb36f11d0a3b066eba32d59899bcdea262d47694 | quote: "status": 403 ... "error": "http-403" ... "cloudflare-challenge:title:just a moment..." ... "usable": false
  - [2] 2026-11-11: the help centre states a 5GB maximum file size per digital product | capture: sha256:932a792d8197acce2e0ca71dc1dc725f35c8d4aaff09478428140b487530a7e9 | quote: Payhip supports a maximum file size of 5GB per digital product.
  - [1] 2026-11-19: Payhip states no storage or bandwidth limit and a 5GB per-file ceiling | capture: sha256:fff6c848f54abc7e0023b692c923815208a3b3f57be15fa5dfa4fa2fb621c5c5 | quote: No, we have no storage or bandwidth limits. We only have a 5GB per file limit.
  - [1] 2026-11-19: the features page is readable on 2026-11-19 and states the no-limit offer and 5GB per-file ceiling | capture: sha256:fff6c848f54abc7e0023b692c923815208a3b3f57be15fa5dfa4fa2fb621c5c5 | quote: No, we have no storage or bandwidth limits. We only have a 5GB per file limit.
  - [5] 2026-11-25: the help centre states the 5GB per-file ceiling and splitting files within one product listing | capture: sha256:224760bc18b896ee11226c7bc712973df19c1b9d838e22c59871f8aa4b374eec | quote: Yes, each uploaded file can be up to 5GB in size. If your file exceeds this limit, you can split it into multiple smaller files and upload them separately to the same product listing.
  - [5] 2026-11-25: the help centre confirms the 5GB per-file ceiling | capture: sha256:224760bc18b896ee11226c7bc712973df19c1b9d838e22c59871f8aa4b374eec | quote: Yes, each uploaded file can be up to 5GB in size. If your file exceeds this limit, you can split it into multiple smaller files and upload them separately to the same product listing.
  - [5] 2026-11-25: the help centre documents splitting larger files across uploads in one product listing | capture: sha256:224760bc18b896ee11226c7bc712973df19c1b9d838e22c59871f8aa4b374eec | quote: Yes, each uploaded file can be up to 5GB in size. If your file exceeds this limit, you can split it into multiple smaller files and upload them separately to the same product listing.
  - [5] 2026-11-25: the help centre confirms the same-listing split path | capture: sha256:224760bc18b896ee11226c7bc712973df19c1b9d838e22c59871f8aa4b374eec | quote: Yes, each uploaded file can be up to 5GB in size. If your file exceeds this limit, you can split it into multiple smaller files and upload them separately to the same product listing.
  - [1] 2026-11-25: the features page states there is no bandwidth limit | capture: sha256:fff6c848f54abc7e0023b692c923815208a3b3f57be15fa5dfa4fa2fb621c5c5 | quote: No, we have no storage or bandwidth limits. We only have a 5GB per file limit.
  - [1] 2026-11-25: the features page confirms no bandwidth limit | capture: sha256:fff6c848f54abc7e0023b692c923815208a3b3f57be15fa5dfa4fa2fb621c5c5 | quote: No, we have no storage or bandwidth limits. We only have a 5GB per file limit.
  - [4] 2026-11-25: the free-account form asks for a name, email address and password | capture: sha256:affc6ea12fd4a8939f6df812b295485fc410a2854fb3f5176e6a2f8cf20d241c | quote: Setup a free Payhip account to create a store. ... First Name ... Last Name ... Email Address ... Password
- sources:
  - [1] https://payhip.com/features/sell-digital-downloads
  - [2] https://help.payhip.com/article/375-cannot-upload-file-or-image
  - [3] https://payhip.com/pricing
  - [4] https://payhip.com/auth/register
  - [5] https://help.payhip.com/article/59-adding-a-digital-product
