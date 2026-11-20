# Decypharr

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-sirrobot01/ | JSON https://fshy.ajam.dev/api/v1/entity/github-sirrobot01.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Decypharr

- `debrid/decypharr` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category client: qBittorrent/SABnzbd-compatible debrid gateway | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:51:00.000Z (live) | stale on 2026-11-23
- url https://github.com/sirrobot01/decypharr
- price USD 0 for the gateway
- free tier: MIT-licensed and self-hosted, no account of its own; the README calls it 'a Media Gateway for Debrid services and Usenet written in Go' that 'provides a unified interface for Sonarr, Radarr, and other *Arr applications'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable to the gateway; the provider's cap applies. | source: [1]
- retention: not applicable: it proxies the provider's library rather than storing it. | source: [1]
- egress: No meter of its own; egress is the provider's. | metered: no | free allowance: none of its own | source: [1]
- identity: anonymous | detail: No account; it takes the provider's key in config.json. | country: None
- interface: rest, nfs, smb
- limits:
  - request-rate: none of its own; it inherits whichever provider's limit, which ranges from 100/min on a free Deepbrid key to an unpublished one on Premiumize [1]
- limits note: Broadest provider list of any client read here: Real-Debrid, TorBox, Debrid-Link, AllDebrid, Premiumize. It supports no provider whose API is undocumented (LinkSnappy, Mega-Debrid).
- binding note: A pure client: the provider's per-object cap or add floor fails first at 1 TiB/month.
- interface detail: 'Mock Qbittorent and Sabnzbd API that supports the Arrs (Sonarr, Radarr, Lidarr etc)', plus 'Read-only NFSv4 and SMB servers for the same libraries, including custom virtual folders'. Runs on port 8282 in the documented compose file.
- endpoint: http://localhost:8282/
- tooling: Docker image cy01/blackhole:latest (documented) or a Go binary; integrates with Sonarr, Radarr, Lidarr and anything else that speaks the qBittorrent or SABnzbd API.
- composes with: This is what makes an *arr stack work without a disk: Sonarr asks Decypharr for a 'torrent', Decypharr adds the magnet to the provider, and the file is served from the provider's library over NFS or SMB.
- reliability: A mock API is a compatibility promise with two moving targets (the *arr client and the provider); a provider field rename surfaces as a failed grab, not as an error in Decypharr.
- notes: The *arr answer observed here: every integration read among debrid providers is a qBittorrent-shaped shim (this, rdt-client) or a Torznab indexer (Debrid Media Manager), and no *arr application was found with a debrid client of its own. This is the most capable shim read here.
- evidence note: README read. Not deployed here, so the NFS/SMB and mock-API behaviour is untested.
- self hosted: yes
- extras:
  - arr_integration: qBittorrent API for grabs, SABnzbd API for usenet grabs
  - providers: real-debrid, torbox, debrid-link, alldebrid, premiumize
  - missing_providers: linksnappy (undocumented API), mega-debrid (password-only auth and premium-only)
- evidence:
  - [1] 2026-10-23: 'Mock Qbittorent and Sabnzbd API that supports the Arrs', read-only NFSv4 and SMB servers, direct usenet streaming over NNTP, and the five supported providers (Real Debrid, Torbox, Debrid Link, All Debrid, Premiumize)
- sources:
  - [1] https://github.com/sirrobot01/decypharr
