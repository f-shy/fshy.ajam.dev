# Payhip

> payhip.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/payhip/ | JSON https://fshy.ajam.dev/api/v1/entity/payhip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Payhip

- `storage/payhip` | qualifies | evidence reported | binding per-object-cap | category Digital-product fulfilment (sell any file)
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:08.102Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://payhip.com
- free tier: Explicit, from their own page: 'No, we have no storage or bandwidth limits. We only have a 5GB per file limit.' Help centre repeats: 'Payhip supports a maximum file size of 5GB per digital product.' | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5GB per file | bytes: 5000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No bandwidth limit stated (their words: 'no storage or bandwidth limits'). Free plan is 'Free Forever' with a 5% transaction fee. No monthly fee, so an unpriced/cheap product costs ~nothing. | metered: no
- identity: email | detail: a first name, last name, email address and password on the free-account form. No card is asked for: the help centre adds card details only to upgrade a paid plan. No phone field is on the form.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 5GB per file [1]
- limits note: Per-object-cap 5 GB. The only limit they publish. Extension blocklist is a hard gate on ingress: EXE, ISO, DMG, VBS, SCR refused unless inside a ZIP. No aggregate quota.
- interface detail: Web upload. REST API + webhooks on paid plans; the digital-product upload itself is form-based.
- tooling: curl/browser; no first-class CLI.
- composes with: 5 GB/file x unlimited files per product x unlimited products = unbounded account. Every listing is a shard with its own 5 GB ceiling. The cleanest 'shard into 5 GB pieces' target found.
- reliability: Serving path is fine; the operational risk is that a 'digital product' must be a listed product, and free products still sit behind a checkout page. Buyer link is emailed, not a stable public URL. So it is an archive/delivery tier, not a hot-link CDN.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 5GB per digital product; EXE/ISO/DMG/VBS/SCR blocked unless zipped
  - [3] 2026-10-21: 'Free Forever' + 5% transaction fee, no monthly fee
  - [4] 2026-11-01: the free-account form asks for a first name, last name, email address and password only | capture: sha256:59140e5be20faa292153c27bdd6f75b527fc1cc63290f090479b762a8294dd56 | quote: Setup a free Payhip account to create a store. ... First Name ... Last Name ... Email Address ... Password
  - [1] 2026-11-01: the no-storage-limit statement and the 5 GB per-file ceiling are unchanged | capture: sha256:d3470891a7f805a500ff4c378581961db517462f8d3b7a90cf399e270ea5a0d1 | quote: No, we have no storage or bandwidth limits. We only have a 5GB per file limit.
- sources:
  - [1] https://payhip.com/features/sell-digital-downloads
  - [2] https://help.payhip.com/article/375-cannot-upload-file-or-image
  - [3] https://payhip.com/pricing
  - [4] https://payhip.com/auth/register
