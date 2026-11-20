# Debrid Media

> debridmediamanager.com | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debridmediamanager/ | JSON https://fshy.ajam.dev/api/v1/entity/debridmediamanager.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Debrid Media Manager

- `debrid/debrid-media-manager` | qualifies | evidence documented | binding none | category hosted client: debrid library UI and Torznab/Newznab indexer | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:51:00.000Z (live) | stale on 2026-11-23
- url https://debridmediamanager.com/
- price USD 0 for the caller
- free tier: Free hosted web app, open source and self-hostable: 'This website is open source and you can also run this on your own machine ... no data or logs are stored on our servers'. The library, casting and transfer features need a debrid account; the indexer endpoint needs only a DMM API key. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: it manages the provider's library. | source: [1]
- retention: not applicable: state lives in the browser's local storage and in the debrid account. | source: [1]
- egress: No meter of its own; it serves the provider's links. | metered: no | free allowance: none of its own | source: [1]
- identity: anonymous | detail: No account with DMM; a debrid login for library features, or a DMM API key for the indexer endpoint alone. | country: None
- interface: rest
- limits:
  - request-rate: not published; it is a shared hosted instance and every search fans out to the provider's API under the user's own key [1]
- limits note: Because it calls the provider with the user's key, DMM's polling adds to the same per-key budget the user's other tools spend; the 250/min Real-Debrid ceiling is shared, not per application.
- binding note: A pure client: the provider's 250/min and 20-second add floor fail first, and they are shared with every other client on the same key.
- interface detail: A hosted web UI plus, in its own words, 'DMM also answers as a Torznab and Newznab indexer for Prowlarr, Sonarr and Radarr, and that only needs a DMM API key'. The login page offers Real-Debrid only.
- endpoint: https://debridmediamanager.com/
- tooling: Hosted, or self-hosted from source. Pairs with zurg for the filesystem route and with rclone for the mount. Neighbouring tools in the same ecosystem: Riven, CLI-Debrid, DUMB, CineSync.
- composes with: The only place in this layer where a *arr stack talks to a debrid ecosystem directly rather than through a qBittorrent shim: Prowlarr treats it as an indexer.
- reliability: Real-Debrid is the only login offered on the front page, so the tool's multi-provider reputation is ahead of what its own page shows; the login page is the thing to re-read before relying on another provider.
- notes: Included because it is the one *arr-visible endpoint in the debrid world and because its project notes are the best public measurements of Real-Debrid's real behaviour. Trigger condition: if the indexer endpoint starts requiring a debrid login, the 'only needs a DMM API key' line is stale.
- evidence note: The live front page was read; it states the indexer feature and the single-provider login. The Torznab endpoint itself was not called.
- extras:
  - arr_integration: Torznab and Newznab indexer for Prowlarr, Sonarr and Radarr
  - providers_offered: real-debrid on the login page
  - ecosystem: zurg (WebDAV), rclone (mount), Riven, CLI-Debrid, DUMB, CineSync
- evidence:
  - [1] 2026-10-23: 'DMM also answers as a Torznab and Newznab indexer for Prowlarr, Sonarr and Radarr, and that only needs a DMM API key'; 'No symlinks! Your whole debrid library in one folder'; open source and self-hostable; 'Login with Real Debrid' as the only offered provider
  - [2] 2026-10-23: the same project's measurement work on the Real-Debrid add floor and its provider-specific limit notes
- sources:
  - [1] https://debridmediamanager.com/
  - [2] https://notes.debridmediamanager.com/providers/realdebrid/

## TorBox Usenet (nntp.torbox.app)

- `debrid/torbox-news-server` | qualifies-with-caveat | evidence reported | binding retention-clamped | category usenet provider bundled with a debrid plan (NNTP) | tier pro
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:22:02.000Z (live) | stale on 2026-11-07
- url https://notes.debridmediamanager.com/providers/torbox-news-server/
- free tier: Bundled with TorBox Pro: 'A TorBox Pro subscription bundles a Usenet account ... The account costs nothing extra because it ships with Pro.' Not available on lower plans. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: Bandwidth is 'unlimited but counted in the TorBox dashboard usage figure', so article pulls spend the same fair-use allowance as torrent traffic.
- per-object cap: Not applicable; the unit is the article. | source: [1]
- retention: '3900+ days claimed by TorBox for this server' - a claim, not a measurement; the measured coverage falls well short of it for older posts. | days: 3900 | source: [1]
- egress: Unlimited on the wire but counted against the plan's fair-use bandwidth figure, so article traffic competes with streaming. | metered: yes | free allowance: shared with the plan's fair-use floor | source: [1]
- identity: email | detail: Tied to the TorBox account. News credentials come from torbox.app under tools, username is the account auth id, and the password is shown once.
- interface: nntp
- limits:
  - request-rate: 10 connections, a hard cap counted exactly, mid-handshake included; the refusal is '482 too many connections for your user' [1]
  - retention-clamped (binding): coverage measured at 531 article ids across 2011-2026: 0 of 9 for 2011, 16 of 21 for 2012, and no article that the Omicron account lacked [1]
- limits note: Credential resets are destructive: 'The password is shown once. Any reset invalidates the previous one so a reset breaks every client already configured.' Two clients on one account starve each other and the server refuses the older holder.
- binding note: Ten connections carry a 1 TiB/month pull comfortably; what fails is the article, because the spool is a strict subset of the Omicron feed and holds nothing the others lack.
- interface detail: nntp.torbox.app:563 over TLS 1.3, also 119; greeting '200 Welcome to TorBox'; capability list reports implementation 'nntpswitch2 (local-dev)' with READER, OVER, HDR, XZVER, XZHDR, POST.
- endpoint: part of interface detail
- tooling: any NNTP client; zurg's nzb provider with backup: true
- composes with: A free second opinion behind a paid primary: it is only asked after every other account has said no such article, so it costs nothing when it has nothing, and it held 9 articles one measured Frugal account lacked.
- reliability: A miss is real: 153 misses were re-asked on a fresh connection and none came back, roughly 1% noise; a password reset breaks every configured client; two clients on ten connections refuse each other.
- notes: Potential failure points: a 482 connection refusal, a password reset, or a 430 on older posts. The 430 is the one that matters for an archive pull and the coverage table quantifies it; the connection refusal is the one a careless pool meets in the first hour. The 3900-day retention claim and the measured coverage disagree, and the record keeps both rather than choosing.
- evidence note: This is one third party's measurement, dated 2026-09-02 and 2026-09-03, from two hosts on separate networks, including the connection cap and the coverage table. It is not the vendor's documentation and no probe was run here. The vendor's own retention claim (3900+ days) is quoted separately and is contradicted in practice by the measured coverage.
- extras:
  - failure_angle: subset spool
  - strongest_signal: 430 on posts the primary also lacks
  - account_states: 482 too many connections (transient); 482 invalid username or password (dead credential after a reset)
  - cache_miss: not applicable; the server answers from a local index, so a miss is absence rather than a slow upstream probe
  - host_removal: the software fingerprint (nntpswitch2) is shared with Cheapnews, XS News, Easyusenet, Hitnews and UseNeXT, so the spool behind the brand can change without the hostname changing
- evidence:
  - [1] 2026-10-23: 'Connections | 10, a hard cap counted exactly, mid handshake included'; '482 too many connections for your user' and '482 Invalid username or password'; '3900+ days claimed by TorBox'; the coverage table for 531 ids; 'All 153 misses were asked again on a fresh connection minutes later and none came back'; 'TorBox held nothing the others lacked. Not one article in 531.'
  - [2] 2026-10-23: The Pro plan at $10/mo is the tier that bundles usenet; the free and lower tiers list no usenet.
  - [3] 2026-10-23: 'backup: true keeps the ten connections for articles every other account has already refused ... Only a real no such article does.'
- sources:
  - [1] https://notes.debridmediamanager.com/providers/torbox-news-server/
  - [2] https://torbox.app/pricing
  - [3] https://notes.debridmediamanager.com/providers/usenet/
