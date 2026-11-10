# RDT-Client

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-rogerfar/ | JSON https://fshy.ajam.dev/api/v1/entity/github-rogerfar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RDT-Client

- `debrid/rdt-client` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category client: debrid download manager with a qBittorrent shim | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:51:00.000Z (live) | stale on 2026-11-23
- url https://github.com/rogerfar/rdt-client
- price USD 0 for the caller
- free tier: Free software; the README specifies that the underlying service requires a paid account: 'You will need a Premium service at Real-Debrid, AllDebrid, Premiumize, Torbox or DebridLink, or a HIGHWAY account!' | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable to the caller; the provider's cap applies. | source: [1]
- retention: not applicable: it manages the provider's torrent and usenet lists and deletes completed items locally after download. | source: [1]
- egress: Downloads the files to the local machine ('Download all files from Real-Debrid, AllDebrid, Premiumize, TorBox or HIGHWAY to your local machine automatically'), so it converts unmetered provider egress into local disk use. | metered: no | free allowance: none of its own | source: [1]
- identity: anonymous | detail: No account with the project; it stores the provider's key. | country: None
- interface: rest
- limits:
  - request-rate: none of its own; its polling interval is the provider's problem, and its own issue tracker carries reports of it treating client-side retries as provider 429s [1]
- limits note: The project's issue #952 documents a client-side false 429: 'Evidence this isn't a real RD 429 ... Direct curl from inside the container with the same API key ... all return 200. 30 rapid-fire calls in a row to /torrents also return 200.' A retry layer can invent a throttle that the provider never sent.
- binding note: A pure client: the provider's per-object cap or add floor fails first.
- interface detail: Web UI plus 'a fake qBittorrent API so you can hook up other applications like Sonarr, Radarr or Couchpotato'. Built on .NET 10 and Angular 21; runs as a Windows or Linux service or in Docker.
- endpoint: unverified: the project's default web port was not read; the service is configured through appsettings.json
- tooling: Docker, Windows service, Linux service; Sonarr, Radarr and Couchpotato as downstream clients.
- composes with: The download-to-disk counterpart to Decypharr's stream-in-place: Sonarr grabs through it, it fetches from the provider, unpacks, and leaves a normal file where the *arr stack expects one.
- reliability: Its Polly retry pipeline has produced 429 warnings at ~10 ms execution time, which is too fast to be a network round trip; the log says throttled while the provider is healthy.
- notes: Named separately from Decypharr because the two make different tradeoffs: rdt-client downloads to disk, Decypharr serves in place over NFS/SMB. The client-side false-429 finding belongs to the user, not to Real-Debrid.
- evidence note: README read on 2026-10-23; the issue tracker entry is third-party observation of the user's behaviour, carried as such.
- self hosted: yes
- extras:
  - providers: real-debrid, alldebrid, premiumize, torbox, debrid-link, high-way
  - usenet: torbox, premiumize, high-way
  - arr_integration: qBittorrent API shim
- evidence:
  - [1] 2026-10-23: the six supported providers (Real-Debrid, AllDebrid, Premiumize, TorBox, DebridLink, HIGHWAY), usenet support limited to TorBox/Premiumize/HIGHWAY, automatic unpack, and 'Implements a fake qBittorrent API so you can hook up other applications like Sonarr, Radarr or Couchpotato'
  - [2] 2026-10-23: a reported case of the client logging 429s while direct calls to /user, /torrents, /torrents/activeCount and /hosts/status returned 200 in the same container
- sources:
  - [1] https://github.com/rogerfar/rdt-client
  - [2] https://github.com/rogerfar/rdt-client/issues/952
