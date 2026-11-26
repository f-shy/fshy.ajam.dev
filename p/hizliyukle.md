# HızlıYükle

> hizliyukle.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hizliyukle/ | JSON https://fshy.ajam.dev/api/v1/entity/hizliyukle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HızlıYükle

- `debrid/hizliyukle-com` | qualifies-with-caveat | evidence documented | binding per-object-cap | category anonymous large-file upload page, Turkish market | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-26T01:59:17.123Z (live) | stale on 2026-12-27
- url https://hizliyukle.com/
- price USD 0
- free tier: Dosya yükle işlemini HızlıYükle ile kayıt olmadan yapın - Dosya başına 10GB'a kadar (upload without registering, up to 10 GB per file) | unit: GB | metered on: none | read on: 2026-10-23 | source: [1] | note: Found through a Turkish-language query; an English-language pass would not have surfaced it.
- per-object cap: Dosya başına 10GB'a kadar (up to 10 GB per file) | bytes: 10000000000 | source: [1]
- retention: unverified: the page publishes no expiry period | source: [1]
- egress: No byte allowance stated; the page advertises unlimited free upload with an optional password per file. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'Hesap oluşturmanıza gerek yok' (no need to create an account), with an optional per-file password.
- interface: browser
- limits:
  - per-object-cap (binding): 10 GB per file [1]
- limits note: The 307 redirects on every path tried, including the API paths, which is either a canonical-host rule or a regional edge.
- binding note: 10 GB per file is the published ceiling and the only number available; retention is unstated so nothing else can be named.
- interface detail: Browser drop zone with typed upload pages (image, video, PDF, large file). /api/upload and /upload answer 307 to another host, so the real endpoint is a redirect target that was not followed.
- tooling: Browser interface only; upload requests redirect via HTTP 307 to the active storage host.
- composes with: A Turkish-market 10 GB drop is the kind of regional option that survives when a Western service rate-limits a whole region; it needs its own measurement before it can be trusted.
- reliability: Oluşan yüklü sunucu masrafları yüzünden sistemimizi kapatmak zorunda kaldığımız için üzgünüz.
- notes: Included because the regional pass is the point: the same 10 GB offer is invisible to an English query. No programmatic path found: Browser drop zone with typed upload pages (image, video, PDF, large file). /api/upload and /upload answer 307 to another host, so the real endpoint is a redirect target that was not followed.
- evidence note: The cap and the no-account sentence are quoted from the vendor page in Turkish; no upload was attempted.
- extras:
  - language: tr
  - api_shapes_tried: /api/upload; /upload; /api/files; /v1/upload; /api/v1/upload
- evidence:
  - [1] 2026-10-23: 'Dosya başına 10GB'a kadar' and 'Hesap oluşturmanıza gerek yok' on the Turkish upload page
  - probe:https://hizliyukle.com/api/upload 2026-10-23: HTTP 307 on /api/upload, /upload, /api/files, /v1/upload and /api/v1/upload
  - [1] 2026-11-26: the first-party page announces a shutdown and names the reason without a date | capture: sha256:fcfdecdd7a27377667433237d978daae4738df26610e5d79a3380b937b6a51d9 | quote: Oluşan yüklü sunucu masrafları yüzünden sistemimizi kapatmak zorunda kaldığımız için üzgünüz.
  - [2] 2026-11-26: the archived first-party page states uploads up to 10GB without registration | capture: sha256:40aac166212b0e608b486d3ca5ef60aecb878ce9e1a0c2c3b2d34eeea5dff287 | quote: Kayıt yok, ücret yok. Dosya başına 10GB’a kadar ücretsiz paylaşım.
- sources:
  - [1] https://hizliyukle.com/
  - [2] https://web.archive.org/web/20260808164501/https://www.hizliyukle.com/?provider=wayback
