# Telegraph

> telegra.ph | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/telegra/ | JSON https://fshy.ajam.dev/api/v1/entity/telegra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Telegraph (telegra.ph)

- `storage/telegraph` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://telegra.ph
- free tier: Unlimited pages and unlimited uploaded images; no account-level byte quota. Each page is an independent object with a permanent URL. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Unlimited pages and unlimited uploaded images; no account-level byte quota. Each page is an independent object with a permanent URL | source: [1] | note: not stated
- egress: Free and unmetered, images served from telegra.ph CDN paths with no auth and no hotlink limit. Same infrastructure Telegram uses. | metered: no
- identity: institution
- interface: rest
- limits note: ~5 MB per image (JPEG/PNG/GIF/MP4). Uploads are multipart POST to https://telegra.ph/upload, NOT an api.telegra.ph method, and it is not part of the official API. The python-telegraph client's own wording for that is 'NOT PART OF OFFICIAL API, USE AT YOUR OWN RISK', which records that the endpoint is undocumented and unsupported.
- interface detail: rest
- tooling: Telegraph API (api.telegra.ph): createAccount, createPage, editPage, getPage, getPageList, getViews. Wrappers: github.com/TABmk/telegraph-wrapper, python-telegraph, many Telegram bots.
- composes with: createAccount calls carry no stated limit (probe returned a fresh access_token instantly, no email), pages carry no stated limit, and each image is ~5 MB. Pages are editable indefinitely, so content is mutable in place.
- reliability: Upload endpoint is undocumented and flaky from datacenter IPs: all four attempts (direct, via proxy, with browser UA/Origin/Referer) returned '"Unknown error"' or UNKNOWN_METHOD, while account creation and page API work perfectly. Assume upload needs a residential IP or a Telegram client.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: full method list (createAccount/createPage/editPage/getPage/getPageList/getViews); no upload method documented
  - withheld 2026-10-21: probe: GET api.telegra.ph/createAccount?short_name=t&author_name=t -> {"ok":true,..."access_token":"8705ef..."} — keyless instant accounts
  - withheld 2026-10-21: probe: POST telegra.ph/upload multipart (PNG and JPEG, with and without UA+Origin+Referer) -> '"Unknown error"'; POST api.telegra.ph/upload -> {"ok":false,"error":"UNKNOWN_METHOD"}
- sources:
  - [1] https://telegra.ph/api
