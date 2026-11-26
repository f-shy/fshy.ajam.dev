# t.me/alistshare

> t.me | Netdisk and pan, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-s/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-s.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## t.me/alistshare (the Telegram index channel)

- `netdisk-pan/alistshare-telegram` | qualifies-with-caveat | evidence reported | binding retention-clamped | category index-list
- needs card no, phone no, ID no, institution no | verified 2026-11-25T13:26:29.022Z (live) | stale on 2026-12-10
- url https://t.me/s/alistshare
- free tier: unverified: the channel feed publishes WebDAV credentials but shows only times, not a 2026-11-19 date | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; it is a channel | source: [1]
- retention: unverified: the pinned post warns against malicious traffic flooding | source: [1]
- egress: no egress | metered: no | source: [1]
- identity: anonymous | detail: the /s/ preview needs no account
- interface: rest
- limits:
  - retention-clamped (binding): the pinned post is a notice about excess use, so the channel stopped publishing instances [1]
- binding note: The channel is a discovery input that stopped producing discoveries, which is a retention problem in the input and not in the population.
- tooling: the /s/ preview is readable without an account; the message feed is HTML
- composes with: unverified: a feed post gives the AList instance URL https://pan.lm379.cn but carries no 2026-11-19 date
- reliability: The feed mixes tool posts with instance posts; the pinned notice warns against excess use. Guest credentials are published by the channel and can be withdrawn without notice.
- notes: Index channel publishing public AList instances with guest WebDAV credentials, plus tool posts and a pinned notice about excess use.
- extras:
  - access_mode: index
  - still_lists_instances: yes
- evidence:
  - [1] 2026-10-22: the pinned post is a notice about excess use and the recent feed carries tools such as SaveAny-Bot, TaoSync and Alist Helper rather than instance lists
  - [2] 2026-10-21: 
  - [1] 2026-11-19: a 2026-11-19 post in the channel publishes a live AList instance with guest WebDAV credentials | capture: sha256:39db88b80266cd79e33090588ff218dec42c0272b92198b5713d7a8a8bf9563a | quote: 全站资源约10T，不限速，观影流畅，强推！
  - probe:https://pan.lm379.cn/dav/ 2026-11-19: the WebDAV endpoint the channel publishes answered HTTP 401 with a Basic auth realm on 2026-11-19 | capture: sha256:bd7dcf21ca2afbcafc9b9a4a69ed2fb50bbe4f46c0dd1fe36c8e585e7cad6619 | quote: "status": 401
  - [1] 2026-11-25: the channel feed publishes a WebDAV user named public_dav | capture: sha256:0cef6d803fec7a6f183394b1628ec2a3cb8f87f9d7815314e8b2a9b559ca9df9 | quote: user: public_dav
  - [1] 2026-11-25: the feed publishes a post giving this instance URL | capture: sha256:0cef6d803fec7a6f183394b1628ec2a3cb8f87f9d7815314e8b2a9b559ca9df9 | quote: https://pan.lm379.cn
  - [1] 2026-11-25: the pinned post is a notice about excess traffic use | capture: sha256:0cef6d803fec7a6f183394b1628ec2a3cb8f87f9d7815314e8b2a9b559ca9df9 | quote: Malicious traffic flooding is truly disgraceful!
  - [1] 2026-11-25: the feed publishes a post giving this AList instance URL | capture: sha256:0cef6d803fec7a6f183394b1628ec2a3cb8f87f9d7815314e8b2a9b559ca9df9 | quote: https://pan.lm379.cn
- sources:
  - [1] https://t.me/s/alistshare
  - [2] https://t.me/alistshare

## Telegram public-channel web CDN (t.me/s preview -> cdnN.telesco.pe) — anonymous reads

- `storage/telegram-public-channel-web-cdn-anonymous-reads` | qualifies-with-caveat | evidence reported | binding write-gated | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:23.966Z (live) | stale on 2026-12-10
- url https://t.me/s/telegram
- free tier: Not a storage tier. This is the READ path for files already in a public channel. Anonymous, no account, no token, no API key. Scraping the public preview of a channel yields directly-fetchable media URLs for every photo and video post. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: unverified: the public channel preview states no per-object size limit
- retention: It is still validated (bogus token -> 404, no token -> 404), and one minted token 502'd transiently then recovered, so treat tokens as mint-on-demand, not permanent | source: [1] | note: New subscribers can see the entire message history in a channel once they join.
- egress: Free and unmetered, served by Telegram's own nginx-backed web CDN (Server: nginx/1.30.1, Cache-Control: max-age=10800). Access-Control-Allow-Origin: * and Accept-Ranges advertised, so range requests and browser fetching work. This is genuinely CDN-friendly: put Cloudflare in front and the origin pull is a plain HTTP GET. | metered: no
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): review of a channel yields directly-fetchable media URLs for every photo and video pos [1]
  - write-gated (binding): Review HTML never emits a document element. Checked t. [1]
- limits note: CRITICAL SCOPE LIMIT, probed: this path exposes PHOTOS and VIDEOS only. The preview HTML never emits a document element. Checked t.me/s/telegram, /durov, /tginfo, /tgbeta, /apkpure_official, /drweb, /securitylab: zero occurrences of tgme_widget_message_document, zero .pdf links. Arbitrary files (zips, parquet, models) are NOT reachable anonymously; only the media Telegram re-encodes for preview. Max observed media size is bounded by what the preview embeds.
- interface detail: rest
- tooling: No client needed. Plain curl. Pattern: GET https://t.me/s/<channel> and regex https://cdn\d\.telesco\.pe/file/<hash>.mp4?token=.. The t.me embed widget (https://t.me/<channel>/<id>?embed=1) exposes a second, tokenless URL form (e.g. cdn4.telesco.pe/file/<long-hash>.jpg) that also serves 200/206 anonymously. Pagination works: ?before=<msg_id> walks arbitrarily far back.
- composes with: Iterate channels x ?before pagination. Anonymous scrape rate was tested at 12 requests back-to-back on t.me/s/telegram with 12x HTTP 200. No rate limit encountered. Each channel page yields ~20 messages; a file-storage channel where every post is a 2 GB file would expose all of them this way.
- reliability: It is still validated (bogus token -> 404, no token -> 404), and one minted token 502'd transiently then recovered, so treat tokens as mint-on-demand, not permanent. cdn2.telesco.pe 302s to another host; cdn1 is the one that serves bytes.
- notes: unverified: https://t.me/s/telegram answered 200 on 2026-11-11 through the environment proxy; no sentence on the page states that its HTML carries cdn1.telesco.pe or cdn4.telesco.pe media URLs, or that no tgme_widget_message_document element is present
- evidence:
  - [2] 2026-10-21: probe: curl -r 0-2047 -> 206, Content-Range: bytes 0-2047/4843, Access-Control-Allow-Origin: * — anonymous partial read works
  - [3] 2026-10-21: probe: curl -r 0-1023 ... -> 206, Content-Type: video/mp4, Content-Range: bytes 0-1023/2633811 — anonymous range read of video works
  - withheld 2026-10-21: probe: grep tgme_widget_message_document across 7 public channels -> 0 hits; this path carries media only, never arbitrary documents
  - [1] 2026-11-09: the capture is the raw page response, and its HTML contains cdn1.telesco.pe and cdn4.telesco.pe media URLs with no tgme_widget_message_document element | capture: sha256:c3c445bb794f9d700e7eb5861732c35cd723643f182d2d0d2d82ac00c67e74a8 | quote: HTTP/2 200
  - probe:https://t.me/s/telegram 2026-11-11: the page answered status 200 on 2026-11-11 and its 127695-byte HTML body was read in full | capture: sha256:ac77449daf9ab4bbdc3217e5bc991de3e492073f917a516df45d5ff26a745bb0 | quote: "status": 200
  - [1] 2026-11-11: the page was read and is the Telegram News public preview | capture: sha256:2ff22d0d3bf02a7ad6c7332e3d26a52ed5e989f23ff11bf3ac3c20cd4224aa93 | quote: Telegram News – Telegram
  - [1] 2026-11-19: the public channel preview served today shows video media posts | capture: sha256:8078a02a601ccea9d937c059bcfc878c74578b1c99299743bdd99deab86c4318 | quote: This media is not supported in your browser VIEW IN TELEGRAM
  - [1] 2026-11-25: the preview shows media posts but states no object size limit | capture: sha256:fd50c785dadb5d536d8e54376b08b827cca87a71538c109832cff310ab618dbc | quote: This media is not supported in your browser VIEW IN TELEGRAM
  - [4] 2026-11-25: the Channels FAQ states new subscribers see the entire message history | capture: sha256:99cb390f3a6c6ceb89dd5dc029871112b0cfdd68a5bcff3e16bfa7629ca0ad36 | quote: New subscribers can see the entire message history in a channel once they join.
- sources:
  - [1] https://t.me/s/telegram
  - [2] https://cdn4.telesco.pe/file/<hash>.jpg
  - [3] https://cdn1.telesco.pe/file/<hash>.mp4?token=
  - [4] https://telegram.org/faq_channels

## anonymous telegram file links for arbitrary documents

- `storage/anonymous-telegram-file-links-for-arbitrary-documents` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:46.271Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/t-me-s.md
- free tier: none reachable: The t.me/s preview path carries photos and videos only. Probed seven public channels for tgme_widget_message_document: zero hits, zero .pdf links. There is no anonymous HTTP URL for a… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the public t.me/s preview path states no per-object file-size cap | note: not applicable
- retention: stated-absent: the public t.me/s preview path states no retention period for file links
- egress: stated-absent: the public t.me/s preview path states no egress terms for file links | metered: no
- identity: email
- interface: browser, chat
- interface detail: The public t.me/s preview path is a browser/chat view that renders media posts ("This media is not supported in your browser VIEW IN TELEGRAM") and states no document-file API.
- tooling: not documented
- composes with: stated-absent: the public t.me/s preview path states no way to chain arbitrary document storage with other services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: The t.me/s preview path carries photos and videos only. Probed seven public channels for tgme_widget_message_document: zero hits, zero .pdf links. There is no anonymous HTTP URL for a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: The t.me/s preview path carries photos and videos only. Probed seven public channels for tgme_widget_message_document: zero hits, zero .pdf links. There is no anonymous HTTP URL for a…
  - [1] 2026-11-19: the first-party t.me/s preview path sends the reader into the Telegram app instead of exposing an anonymous direct file link | capture: sha256:7ce5d9a3783d5d92e0aac22fdf94a0294707f2538d16835577ebf30f9d100ff4 | quote: Please open Telegram to view this post
  - [1] 2026-11-19: the public t.me/s preview path is a browser/chat view that embeds media but exposes no document-file API | capture: sha256:8078a02a601ccea9d937c059bcfc878c74578b1c99299743bdd99deab86c4318 | quote: This media is not supported in your browser
  - [1] 2026-11-19: the preview path renders media posts in a browser/chat view | capture: sha256:8078a02a601ccea9d937c059bcfc878c74578b1c99299743bdd99deab86c4318 | quote: This media is not supported in your browser VIEW IN TELEGRAM
- sources:
  - [1] https://t.me/s/telegram
