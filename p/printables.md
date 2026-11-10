# Printables

> printables.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/printables/ | JSON https://fshy.ajam.dev/api/v1/entity/printables.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Printables (Prusa Research)

- `storage/printables` | qualifies | evidence reported | binding per-object-cap | category 3D model repository / maker marketplace
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:08.098Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.printables.com
- free tier: No published account quota and no published upload cap. Verified live object: a single 1,036,822,737 B (1.037 GB) STL served from files.printables.com. Also verified a model holding 29 files totalling 404.3 MB, and one holding six ZIPs of 62.5/167.5/208.5/65.0/98.8/118.6 MB. 'Other files' accepts ZIP, so arbitrary payloads ride inside an archive; and a single model accepts 1335+ files (forum report of a user hitting UI limits, not a storage limit). | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 1.037 GB | bytes: 1036999999 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Backed by Google Cloud Storage (x-goog-* headers), fronted by files.printables.com with `Cache-Control: public, max-age=31536000` and `Access-Control-Allow-Origin: *`. No egress cap published, no paywall on download, no account needed to download. | metered: no
- identity: email | detail: email address and a password, or a Google, Apple or Facebook sign-in: the account article says to register or log in with Google, Apple or Facebook, or to choose Create an account at the bottom to use an email or password, then confirm the account from the sent email. No card and no phone number appear in that flow.
- interface: graphql
- limits:
  - write-gated: curator [1]
  - per-object-cap (binding): per-object-cap: 1.037 GB [1]
- limits note: Per-object-cap: 1.037 GB observed (no stated ceiling found. The '1 GB' in that model's own title is the author's description, not a platform limit). Write is normal account signup; no curator. Download is anonymous. RANGE VERIFIED: `Range: bytes=100-199` returned `HTTP/1.1 206 Partial Content`, `Content-Range: bytes 100-199/1036822737`, 100 bytes. So resumable/ranged GET works (this is NOT the RepOD case).
- interface detail: Undocumented but stable public GraphQL: POST https://api.printables.com/graphql/ with no auth. `print(id:N){ name stls{id name fileSize} otherFiles{id name fileSize} downloadPacks{...} }` to enumerate; then mutation `getDownloadLink(id, printId, source:"model_detail", fileType:"stl"|"other")` returns `{ok, output:{link}}`.
- tooling: Plain HTTP and JSON interface. Standard curl or Python requests interact directly with endpoints without special SDKs. Object path parameters use standard UUID identifiers.
- composes with: Returned links provide direct Google Cloud Storage object URLs where expiry headers are not enforced. Files remained accessible on 2026-10-21 despite past expiration timestamps. Objects are hotlinkable and enumerable per model identifier.
- reliability: The signup page answers a Cloudflare bot challenge to an unauthenticated fetch; the email signup is documented by Prusa's own account article.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: print(id:1216949){stls{fileSize}} returned 1036822737 for high_poly_benchy.stl, and downloadPacks 123718835; proves a real 1.037 GB object, not a claim
  - [2] 2026-10-21: getDownloadLink mutation — returned with no query-string signature
  - withheld 2026-10-21: curl -D - on that URL — 200, Content-Length: 1036822737, Content-Type: model/stl, x-goog-storage-class: STANDARD, Access-Control-Allow-Origin: *, Accept-Ranges: bytes
  - withheld 2026-10-21: curl -r 100-199 — HTTP/1.1 206 Partial Content, Content-Range: bytes 100-199/1036822737, exactly 100 bytes written
  - withheld 2026-10-21: full-object download of 24695 '0.25mm clip part 1.zip' — got exactly 62,510,662 B; md5sum 4df344d46a0452592f6a70bd88e63777 matched the server's x-goog-hash md5=TfNE1GoEUlkvanC9iOY3dw== (base64 -> same digest). SHA-256-class byte-exact roundtrip.
  - withheld 2026-10-21: print(id:868222) — 29 files, 404.3 MB in one model
  - withheld 2026-10-21: print(id:180017) — six ZIPs in 'Other files' up to 208,474,336 B; proves arbitrary archive types survive ingest
  - [3] 2026-10-21: section 2.1 lists accepted types incl. .gcode/.bgcode/.sl1/.stl/.3mf/.obj/.step/.scad/.amf plus images, 'and other information and files'; 2.9 disclaims storage durability
  - [4] 2026-11-01: Printables registration is a third-party sign-in or an email and password, confirmed by an email link | capture: sha256:c4a97fd8892abbe51e945c425d7b038755d7d247922c9f1fa0adeae9ba5503d2 | quote: you can choose to register or log in with your Google, Apple, or Facebook account. You can also choose "Create an account" at the bottom to use an email or password for registration
  - [3] 2026-11-01: the terms page states that the service is not data storage and does not guarantee that content survives | capture: sha256:c15f054d8688bc30df8071682bc575c0414fb5436ee688cd78a0d311b0ca0fc5 | quote: PRINTABLES does not serve as data storage and the Operator does not guarantee to the User that the User Content will not be damaged, modified or deleted.
  - [4] 2026-11-01: the account's registration path and its email confirmation are read on Prusa's own page | capture: sha256:c4a97fd8892abbe51e945c425d7b038755d7d247922c9f1fa0adeae9ba5503d2 | quote: you can choose to register or log in with your Google, Apple, or Facebook account. You can also choose "Create an account" at the bottom to use an email or password for registration
- sources:
  - [1] https://api.printables.com/graphql/
  - [2] https://files.printables.com/media/prints/1216949/stls/9131937_666a2768-.../high_poly_benchy.stl
  - [3] https://www.prusa3d.com/page/terms-of-service-of-printables-com_231249/
  - [4] https://help.prusa3d.com/article/prusa-account-creation_1939
