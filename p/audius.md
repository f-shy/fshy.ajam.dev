# Audius

> audius.co | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/audius/ | JSON https://fshy.ajam.dev/api/v1/entity/audius.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Audius (Open Audio Protocol) — original file is served byte-for-byte

- `storage/audius-original-file-is-served-byte-for-byte` | qualifies | evidence documented | binding per-object-cap | category p2p
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:09.750Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://audius.co
- free tier: There is no limit to the number of tracks you can upload to your Audius profile, so you can freely share your music with your listeners without any limitations! | unit: unlimited | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: Please note that while there is no limit on the duration of your tracks, there is a file size limit for each upload, which is currently set at 2GB. | bytes: 2000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Content is served by creator nodes / the open-audio validator network; no egress meter, no account-level bandwidth cap, no paid tier to upgrade to. | metered: no
- identity: anonymous | detail: unverified: the captured FAQ states the upload limits, not what creating an Audius profile requires
- interface: rest
- limits:
  - per-object-cap (binding): file size cap is 2 GB [1]
- limits note: Upload limit is 2 GB per track. The is_downloadable flag must be true for the /download path. Direct endpoint /content/{cid} on creator nodes returns HTTP 401 to anonymous callers, requiring signed URLs from the discovery endpoint.
- interface detail: rest
- tooling: Public discovery-provider REST API (discoveryprovider.audius.co/v1). Keyless with app_name. Track objects expose orig_file_cid, orig_filename, is_original_available, is_downloadable. /v1/tracks/{id}/stream returns a 302 to a creator-node cidstream; /v1/tracks/{id}/download returns a 302 to the ORIGINAL file. JS SDK (@audius/sdk), docs.audius.co/api.
- composes with: Unlimited tracks per account across multiple accounts, with each track capped at 2 GB. The /download endpoint serves orig_file_cid directly rather than transcoded audio, preserving uploaded bytes intact.
- reliability: No transcoding on the download path. Verified live: GET /v1/tracks/7AVQpPA/download -> 302 to val007.open-audio-validator.com/tracks/cidstream/<orig_file_cid>?filename=....wav -> 206, Content-Type audio/wave, Content-Disposition attachment; filename='...wav', Content-Range bytes 0-1023/54711220, body starts 'RIFF....WAVEJUNK'. The stream path, by contrast, is a 128 kbps mp3 re-encode. Retrieval depends on the discovery provider being up; the network is decentralised so a single node going down is survivable.
- notes: 'There is no limit to the number of tracks you can upload to your Audius profile' and 'no limit on the duration of your tracks'; per-upload file size cap is 2 GB. Unlimited tracks x 2 GB = unbounded, free, no paid tier exists.
- evidence note: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'no limit to the number of tracks'; 'file size limit for each upload ... currently set at 2GB'; page footer 'Updated April 30, 2026'
  - withheld 2026-10-21: probe: GET discoveryprovider.audius.co/v1/tracks/7AVQpPA?app_name=test -> 200, orig_filename 'Cartel De Santa - Tomala Cochino (Shavezz Remix).wav', duration 310, is_downloadable true, is_original_available true, orig_file_cid baeaaaiqsebqzfbbf2id64h6rtnfuhedc3h2qyrxhch4axr7tonaeq77novlzo
  - withheld 2026-10-21: probe: GET /v1/tracks/7AVQpPA/download -L -> 206, Content-Type audio/wave, Content-Range 0-1023/54711220, magic bytes RIFF/WAVE
  - withheld 2026-10-21: probe: GET /v1/tracks/a5aXGmz/stream -> 302 to creator-node .../tracks/cidstream/<track_cid> (the transcode, not the original)
  - [1] 2026-11-09: the FAQ states there is no limit on uploads, so the unit is unlimited | capture: sha256:457fbf4b1e43b788a9c27fe3c5056543d39eef60b0941dad1b589bfad2b6651d | quote: There is no limit to the number of tracks you can upload to your Audius profile, so you can freely share your music with your listeners without any limitations!
  - [1] 2026-11-09: the FAQ states a 2 GB per-upload file size limit | capture: sha256:457fbf4b1e43b788a9c27fe3c5056543d39eef60b0941dad1b589bfad2b6651d | quote: Please note that while there is no limit on the duration of your tracks, there is a file size limit for each upload, which is currently set at 2GB.
- sources:
  - [1] https://help.audius.co/faq/is-there-a-limit-to-how-much-i-can-upload-to-my-audius-profile
