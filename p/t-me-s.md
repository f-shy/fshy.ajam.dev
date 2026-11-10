# Telegram public-channel

> t.me | Storage, Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-s/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-s.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Telegram public-channel web CDN (t.me/s preview -> cdnN.telesco.pe) — anonymous reads

- `storage/telegram-public-channel-web-cdn-anonymous-reads` | qualifies-with-caveat | evidence reported | binding write-gated | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://t.me/s/telegram
- free tier: Not a storage tier. This is the READ path for files already in a public channel. Anonymous, no account, no token, no API key. Scraping the public preview of a channel yields directly-fetchable media URLs for every photo and video post. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: It is still validated (bogus token -> 404, no token -> 404), and one minted token 502'd transiently then recovered, so treat tokens as mint-on-demand, not permanent | source: [1] | note: not stated
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
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: probe: curl -r 0-2047 -> 206, Content-Range: bytes 0-2047/4843, Access-Control-Allow-Origin: * — anonymous partial read works
  - [3] 2026-10-21: probe: curl -r 0-1023 ... -> 206, Content-Type: video/mp4, Content-Range: bytes 0-1023/2633811 — anonymous range read of video works
  - withheld 2026-10-21: probe: grep tgme_widget_message_document across 7 public channels -> 0 hits; this path carries media only, never arbitrary documents
- sources:
  - [1] https://t.me/s/telegram
  - [2] https://cdn4.telesco.pe/file/<hash>.jpg
  - [3] https://cdn1.telesco.pe/file/<hash>.mp4?token=

## t.me/alistshare (the Telegram index channel)

- `netdisk-pan/alistshare-telegram` | dead | evidence reported | binding retention-clamped | category index-list
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:37:00.574Z (live) | stale on 2026-11-06
- url https://t.me/s/alistshare
- free tier: a Telegram channel that used to publish public AList instances and their guest WebDAV credentials | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable; it is a channel | source: [1]
- retention: the channel's recent feed carries tools rather than instances, and its pinned post is a notice about excess use from 2025-01 | source: [1]
- egress: no egress | metered: no | source: [1]
- identity: anonymous | detail: the /s/ preview needs no account
- interface: rest
- limits:
  - retention-clamped (binding): the pinned post is a notice about excess use, so the channel stopped publishing instances [1]
- binding note: The channel is a discovery input that stopped producing discoveries, which is a retention problem in the input and not in the population.
- tooling: the /s/ preview is readable without an account; the message feed is HTML
- composes with: Inactive discovery channel. It previously provided instance hosts but no longer publishes new endpoints.
- reliability: The channel shifted from publishing instance lists to publishing tools (SaveAny-Bot, TaoSync, Alist Helper) and pinned a notice about excess use, so a discovery loop that polls it will return no new hosts.
- notes: Documented to record channel status. Historical instance listings originated from this Telegram channel, which has ceased publishing new instance hostnames.
- extras:
  - access_mode: index
  - still_lists_instances: no
- evidence:
  - [1] 2026-10-22: the pinned post is a notice about excess use and the recent feed carries tools such as SaveAny-Bot, TaoSync and Alist Helper rather than instance lists
  - [2] 2026-10-21: 
- sources:
  - [1] https://t.me/s/alistshare
  - [2] https://t.me/alistshare
