# WebStreamr

> hayd.uk | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hayd/ | JSON https://fshy.ajam.dev/api/v1/entity/hayd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WebStreamr (public instances)

- `debrid/webstreamr-hosted` | dead | evidence documented | binding none | category hosted Stremio addon, HTTP streams scraped from streaming sites (no debrid required) | tier public instance
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://webstreamr.hayd.uk/
- price USD 0
- free tier: None any more. The addon was archived upstream and both public instances now serve a retirement page: the ElfHosted instance states 'The developer has archived Webstreamr, and in consultation, we've retired the hosted public instance donated to Hayd'; the Hayd instance serves the title 'Webstreamr is deprecated'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The retirement pages return HTTP 200 with no redirect, so any check that trusts status codes scores this as alive.
- per-object cap: not applicable: stream descriptors | source: [2]
- retention: not applicable | source: [2]
- egress: Never reached: the addon served no streams. Historically it returned HTTP URLs from streaming sites, which play without a debrid account at the source site's bitrate. | metered: no | free allowance: none | source: [2]
- identity: anonymous | detail: Nothing to register - there is nothing left to register for. | country: None
- interface: rest
- limits:
  - request-rate: not applicable: retired [1]
- limits note: The limit that killed it was not traffic but maintenance: the upstream developer archived the project and the sponsor withdrew the instance.
- binding note: No constraint applies: the service returns a retirement notice for every path, which is a total failure rather than a quota.
- interface detail: Stremio addon protocol. Both /manifest.json and /stream/movie/tt1254207.json returned the same 24,382-byte HTML retirement page.
- tooling: self-hosting the archived source remains possible, but that needs a machine - which is the one thing not available here.
- composes with: It was the only free hosted addon found that needed no debrid key at all, so its death removes the no-key HTTP branch of the free floor.
- reliability: HTTP 200 on every path with a deprecation page is the exact failure published records warns about.
- notes: This is the finding that decides the free floor: the no-debrid-key branch is gone, so every surviving free front end needs either a debrid key or a local streaming server.
- evidence note: Both the manifest and a stream call were fetched; each returned the retirement HTML. A dated search result also pointed at the ElfHosted retirement page. Documented without probe digest: no probe record with status, bytes and digest exists.
- extras:
  - retirement_pages: https://webstreamr-is-deprecated.elfhosted.com/; https://webstreamr.hayd.uk/
  - upstream: https://github.com/webstreamr/webstreamr (archived), https://gitlab.com/webstreamr
- evidence:
  - [3] 2026-10-23: HTTP 200, 24,382 bytes of HTML titled 'Webstreamr is deprecated' where a JSON manifest was expected
  - [4] 2026-10-23: the identical 24,382-byte retirement page for a stream request
  - [1] 2026-10-23: 'The developer has archived Webstreamr, and in consultation, we've retired the hosted public instance donated to Hayd'
  - [5] 2026-10-23: third-party/upstream confirmation in the project description: 'Stremio add-on which provides HTTP URLs from streaming websites. HTTP streams have limitations. For a better experience, I'd advise using a Debrid service'
- sources:
  - [1] https://webstreamr-is-deprecated.elfhosted.com/
  - [2] https://webstreamr.hayd.uk/
  - [3] https://webstreamr.hayd.uk/manifest.json
  - [4] https://webstreamr.hayd.uk/stream/movie/tt1254207.json
  - [5] https://gitlab.com/webstreamr
