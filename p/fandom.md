# Fandom

> fandom.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fandom/ | JSON https://fshy.ajam.dev/api/v1/entity/fandom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fandom (wiki farm, MediaWiki)

- `storage/fandom` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.fandom.com
- free tier: 10 MB per file, no file-count cap: 'The maximum size of uploads is 10 MB. The maximum image resolution is 12.5 megapixels.' and 'There is no limit to the number of files you can upload' (with the caveat 'they shouldn't be used just as file stores'). | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB per file | bytes: 10000000 | source: [1] | note: not stated
- retention: request-rate: MediaWiki edit-rate limits per IP; anon upload needs a CSRF token (probe returned `badtoken`). Retention: permanent, but Fandom never deletes content even on community request. | source: [1] | note: not stated
- egress: Unmetered, Cloudflare-fronted static CDN. But see the read-path trap below. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 10 MB per file [1]
- limits note: per-object-cap: 10 MB (hard, confirmed live via siteinfo `maxuploadsize` = 10485760). request-rate: MediaWiki edit-rate limits per IP; anon upload needs a CSRF token (probe returned `badtoken`). Retention: permanent, but Fandom never deletes content even on community request.
- interface detail: rest
- tooling: MediaWiki Action API per wiki (`action=upload`), Pywikibot/mwclient. No rclone backend.
- composes with: 10 MB x unlimited files x unlimited free wikis (wiki creation is self-service). 10 MB is small enough that this only matters as a shard layer.
- reliability: Two read-path traps in one host. (1) `static.wikia.nocookie.net` returns `403 Cf-Mitigated: challenge` to any non-browser. A hard read gate. (2) When it does serve, it RE-ENCODES: a request for a .png returned `Content-Type: image/webp`, 6,326 bytes, sha1 ada19fa5.. NOT the 9,979-byte original whose sha1 ce3dee8b.. matches the API. You must append `&format=original` to get your bytes back. Textbook 'gives you storage but not your bytes'.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'The maximum size of uploads is 10 MB ... There is no limit to the number of files you can upload'
  - [2] 2026-10-21: probe: GET -> 200, maxuploadsize = 10485760
  - withheld 2026-10-21: probe: GET static.wikia.nocookie.net/.../Grass_Block.png/revision/latest (direct and via fetch proxy, browser UA) -> 403 with `Cf-Mitigated: challenge`; via proxy without UA -> 200 but image/webp 6,326 B, sha1 ada19fa5... != API sha1 ce3dee8b...
  - withheld 2026-10-21: probe: same URL with `&format=original` -> 200, image/png, 9,979 bytes, sha1 ce3dee8bd03c3a66eedef6e710491cf9f4f11e2b == API sha1. Original IS retrievable, but only on the explicit original path.
- sources:
  - [1] https://community.fandom.com/wiki/Help:Uploading_files
  - [2] https://minecraft.fandom.com/api.php?action=query&meta=siteinfo&siprop=general&format=json
