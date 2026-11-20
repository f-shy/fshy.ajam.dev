# HubCloud

> hubcloud.ist | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hubcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/hubcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HubCloud

- `debrid/hubcloud` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category Google Drive link-to-direct-download generator, with API and folder packaging | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:34:15.635Z (live) | stale on 2026-11-23
- url https://hubcloud.ist/
- price USD 0
- free tier: Generating a link is free and needs no account: 'Paste your Google Drive link and generate a high-speed direct download link instantly. No account linking needed.' No price, byte allowance or account quota is printed anywhere on the page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: The product withholds its own numbers entirely; the quota it moves is Google Drive's.
- per-object cap: Not stated. Nothing on the page names a size for a wrapped file or for the ZIP a folder share produces. | source: [1] | note: The page's own figures (4.2 GB, 1.8 GB) are mocked-up dashboard filenames, not limits, and are not used here.
- retention: Not stated. The wrapper stores a Drive file id, so the link lives as long as the Drive object does. | source: [1]
- egress: Every download is proxied through HubCloud as a 'high-speed direct download link'; folder shares are 'Download folders as ZIP archives instantly'. Nothing is metered and no allowance is printed. | metered: no | source: [1]
- identity: anonymous | detail: Generating a link needs nothing: 'No account linking needed'. A dashboard exists at /drive/admin for managing files, but the public path does not require it.
- interface: rest, unknown
- limits:
  - per-ip-shaping (binding): unstated by HubCloud; the underlying Google Drive per-file download throttle is what a client hits [1]
  - request-rate: unstated [1]
- limits note: The absence is the finding: a service whose product is removing somebody else's limit publishes no limit of its own, so a client cannot budget against it. The Drive-side ceiling is documented one link further down the chain by DriveSeed, which lists '403: User Rate Limit Exceeded - Fixed to Great Extent' as a release note.
- binding note: At 1 TiB a month the throttle that reappears is Google's per-file and per-session shaping on the Drive object behind the wrapper. HubCloud adds no counter of its own, so nothing else on this record can bind.
- interface detail: REST upload endpoint `curl -X POST api.hubcloud.foo/upload`, announced as 'New: API v2.0 Released', with a dashboard at hubcloud.foo/drive/admin. The page also offers a 'Pack Manager' that combines several links into one package and a Drive integration that requires no account linking.
- endpoint: https://api.hubcloud.foo/upload
- tooling: No client library. The generation step is a form on the page; the API is a single documented POST. Third parties already automate it: hubcloud.cfd is a public 'HubCloud Bypass' page whose only feature is 'Extract direct download links from HubCloud video/drive pages instantly'.
- composes with: The middle layer of the Indian index chain: an index site posts a HubCloud link, HubCloud re-exposes the Google Drive file as a direct link that indexers and apps can hand to a downloader, and the same file is often re-wrapped one layer down by DriveSeed or GDFlix.
- reliability: The brand rotates hostnames faster than the index sites update: hubcloud.xyz could not be checked at all because network requests's DNS lookup timed out (503 destination-unchecked, retryable), which establishes nothing about the domain; hubcloud.ink answered an empty 204; and the live host was reached only through hubcloud.foo, which redirects to hubcloud.ist. A client that hard-codes a host breaks within weeks.
- notes: The record prices a link wrapper, not storage: nothing here can be mounted, and the bytes always belong to Google. hubcloud.xyz was the ledger's assumed host and is dead.
- evidence note: Feature list, API endpoint and dashboard path were read on the live page. The absence of any published quota is itself documented. What would raise the rung: one measured download through a generated link, with the byte count and the status of the first throttle.
- extras:
  - live_hosts: hubcloud.ist, reached via hubcloud.foo
  - empty_hosts: hubcloud.ink (origin answered 204 with an empty body)
  - third_party_fronts: hubcloud.cfd
- evidence:
  - [2] 2026-10-23: live service at hubcloud.ist: 'Paste your Google Drive link and generate a high-speed direct download link instantly. No account linking needed.', 'New: API v2.0 Released', folder-to-ZIP share, Pack Manager
  - [1] 2026-10-23: the same page served directly, confirming the redirect target is the app rather than a parking page
  - [3] 2026-10-23: third parties run a dedicated bypass front for the service ('Extract direct download links from HubCloud video/drive pages instantly'), which shows the wrapper is used at volume
- sources:
  - [1] https://hubcloud.ist/
  - [2] https://hubcloud.foo/
  - [3] https://hubcloud.cfd/
