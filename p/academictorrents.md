# Academic Torrents

> academictorrents.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/academictorrents/ | JSON https://fshy.ajam.dev/api/v1/entity/academictorrents.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Academic Torrents (tracker + index, with optional donor mirroring)

- `storage/academic-torrents` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-01T18:05:15.756Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://academictorrents.com
- free tier: NO BYTE QUOTA ON THE INDEX, because the index is all they host: 'It's important to note that we don't directly host your data. However, we manage a network of donated servers. When you upload a torrent file to our site, hosting nodes (seeds) register with the tracker to provide download locations for the data.' The catalogue is 419.44 TB across the network but that is other people's disk. The only hard number is on the torrent file itself: a 10 MB per-torrent limit, stated by the maintainer ('each of them is beneath the 10MB size limit') and defended against a request to raise it. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 10 MB | bytes: 10000000 | source: [1] | note: not stated
- retention: per-object-cap: 10 MB for the .torrent file only; no cap on the dataset it describes. retention: entries are permanent in practice; the PDF describes a network designed for durability across node failure | source: [1] | note: not stated
- egress: Free, and structurally so - it is BitTorrent, so egress is other peers' bandwidth. Also offers an HTTP fallback: 'Backup URLs (also called WebSeeds)' are injected into the .torrent so the swarm can be skipped entirely. Their own docs note most free hosts (Google Drive, Dropbox) do NOT work as webseeds because they lack RANGE support, while archive.org and Zenodo (single-file only) do. | metered: no
- identity: email | detail: sign-up asks a desired username, an email address and a password twice and sends a confirmation email; it asks no phone number and no card, and an educational institution address enables more features but is not required
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap: 10 MB [1]
- limits note: per-object-cap: 10 MB for the .torrent file only; no cap on the dataset it describes. retention: entries are permanent in practice; the PDF describes a network designed for durability across node failure. request-rate: not documented on the API page. There is no seed guarantee - 'as long as at least one person can become a seed for that data' - so durability is a function of who else mirrors it.
- interface detail: rest
- tooling: REST v2 at https://academictorrents.com/apiv2/ - POST /apiv2/entry with `file` as a base64-encoded .torrent and `urllist` as the webseed URLs; API key required. Also POST /apiv2/collection. A first-party uploader exists (github.com/academictorrents/academictorrents_uploader) and a `mirroring.md` doc for running a Smart Node that seeds selected collections from an RSS feed. Standard BitTorrent clients (transmission-daemon recommended) do the actual transfer.
- composes with: This is a discovery and swarm-coordination layer, not storage. What it multiplies is availability: one .torrent entry (10 MB) makes an arbitrarily large dataset reachable through unlimited peers, and the webseed lists let you point at storage you already have elsewhere (archive.org items, Zenodo records, your own HTTP server). Chain shape: bytes live on IA/Zenodo/your server -> webseed URL -> AT entry -> swarm plus HTTP fallback. Verified that the mechanism is real: a fetched .torrent carries `url-list` with https://files.inria.fr/ and the AT announce URL.
- reliability: The fatal caveat: without a donor node or a webseed, an entry is a pointer to nothing. Their model is explicitly 'the burden of hosting data' distributed to volunteers, so AT gives zero storage guarantee. It is also not a place to put bytes - upload.php returned 409 and there is no bulk endpoint. Treat it as a distribution amplifier for data that already has a home, never as a home.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'we don't directly host your data. However, we manage a network of donated servers... Alternatively, you can use a Backup URL... where the data will be mirrored.'; WebSeeds section; RANGE queries section
  - [2] 2026-10-21: 'Making over 419.44TB of research data available!'
  - [3] 2026-10-21: maintainer ieee8023: 'I'm against raising the per file limit because that's a lot of space to take up for just a torrent file'; reporter confirms 'each of them is beneath the 10MB size limit'
  - [4] 2026-10-21: probe: GET -> 200, application/x-bittorrent, 100,785 bytes; bencoded body contains 'url-list' with https://files.inria.fr/ and announce https://academictorrents.com/announce.php
  - [5] 2026-10-21: POST /apiv2/entry with base64 torrent + urllist, API key required
  - [6] 2026-10-21: probe: GET -> 409 (no anonymous bulk write path)
  - [7] 2026-11-01: the sign-up form asks an email address | capture: sha256:48c95204e4f4da254fd936bec9ab7a9db59b5f553913f5003ae14a50add6fdb4 | quote: <td align="right" class="heading">Email address:</td>
  - [7] 2026-11-01: an institution address adds features but is not the requirement | capture: sha256:48c95204e4f4da254fd936bec9ab7a9db59b5f553913f5003ae14a50add6fdb4 | quote: Use an educational institution address to enable more features.
  - [7] 2026-11-01: the sign-up form's only required fields are a username, an email and a password | capture: sha256:48c95204e4f4da254fd936bec9ab7a9db59b5f553913f5003ae14a50add6fdb4 | quote: <input class="form-control" type="text" size="40" name="wantusername" required="">
  - [7] 2026-11-01: the account needs a working email address to be confirmed | capture: sha256:48c95204e4f4da254fd936bec9ab7a9db59b5f553913f5003ae14a50add6fdb4 | quote: You will receive a confirmation email which you need to respond to.
- sources:
  - [1] https://academictorrents.com/docs/uploading.html
  - [2] https://academictorrents.com/
  - [3] https://github.com/academictorrents/academictorrents-docs/issues/46
  - [4] https://academictorrents.com/download/cf445f6073540af0803ee345f46294f088e7bba5.torrent
  - [5] https://academictorrents.com/docs/api.html
  - [6] https://academictorrents.com/upload.php
  - [7] https://academictorrents.com/signup.php
