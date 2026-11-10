# HotDebrid

> hotdebrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hotdebrid/ | JSON https://fshy.ajam.dev/api/v1/entity/hotdebrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HotDebrid

- `debrid/hotdebrid` | qualifies-with-caveat | evidence documented | binding pull-count | category multi-hoster (free premium link generator, ad-funded) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:32.905Z (live) | stale on 2026-12-04
- url https://www.hotdebrid.com/
- price USD 0 (claimed)
- free tier: HotDebrid premium link generator is free and unlimited (feature list); the FAQ states 'each single user is able to leech up to 8 premium links per day'. HotDebrid premium leech is compatible with over +100 cloud file hosts. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The feature list says 'free and unlimited'; the FAQ gives a per-user limit of 8 premium links per day ('At the moment'), so 'unlimited' describes bandwidth and file size, not the number of links. No host list, status page or terms page is published.
- per-object cap: There is no absurd file size limits. (vendor) | source: [1]
- retention: We will remove your file links after the premium download has finished. | source: [1]
- egress: We don't limit your download bandwidth in any way. (vendor) No allowance, no counter and no measured throughput is published. | metered: no | free allowance: unlimited (claimed) | source: [1]
- identity: anonymous | detail: No account and no email is requested on the page; the generator takes a link only.
- interface: unknown
- limits:
  - per-ip-shaping: the generated premium link is 'locked to a single user IP'; no numeric limit published [1]
  - pull-count (binding): up to 8 premium links per day per user ('At the moment') [1]
- limits note: Two sibling sites, okdebrid.com and anydebrid.com, publish the same feature list, the same FAQ shape and the same 'free and unlimited' claim with different sentences, so they are not copies. None of the three publishes a host list or a status page; only HotDebrid's FAQ was re-read and it gives a per-user quota of 8 premium links per day.
- binding note: The FAQ states up to 8 premium links per day per user, the only numeric limit published; file size and bandwidth are stated as unlimited, and no throughput was measured.
- interface detail: One web form: paste a link, click Generate Premium Link, receive a download link. No API, no plugin, no documented endpoint.
- tooling: Browser only; no extension, plugin, API or CLI is published.
- composes with: A published ceiling of 8 premium links per day per user can be planned against, but no host list is published, so a client cannot know whether a needed host is covered.
- reliability: Ad-funded with no status page and no published host list, so a dead host and a banned client look the same from outside; links are IP-locked.
- notes: Documented as the representative of a class rather than as a measured option. okdebrid.com and anydebrid.com are separate services with the same claims and the same missing evidence; they are not counted as separate capacity. This class is why the debrid answer cannot be 'free is unlimited': the claim is free to make and unverifiable from outside.
- evidence note: The vendor's own page is captured and quoted for each field. The 8 links per day figure is a stated limit; 'unlimited' elsewhere on the page is a claim, and no unlock or throughput was measured. No host list is published.
- extras:
  - siblings: okdebrid.com, anydebrid.com
  - similarity_note: pairwise text similarity 0.13-0.17, so related by template and claim, not by copied text
  - host_list: not published
  - status_page: none
- evidence:
  - [1] 2026-10-23: 'free and unlimited', 'compatible with over +100 cloud file hosts', 'We don't limit your download bandwidth in any way', 'The provided premium link is locked to a single user IP', and the absence of any host list or numeric limit on the page
  - [1] 2026-11-03: the FAQ states a per-user limit of 8 premium links per day | capture: sha256:d70426b70db3f6942b029a7c087614b0daff643e0f48c46b429cc65dce4b2421 | quote: At the moment, each single user is able to leech up to 8 premium links per day.
  - [1] 2026-11-03: the page states no per-file size cap | capture: sha256:d70426b70db3f6942b029a7c087614b0daff643e0f48c46b429cc65dce4b2421 | quote: Our premium downloader is not capped by file size limitations.
  - [1] 2026-11-03: links are removed after the leech ends | capture: sha256:d70426b70db3f6942b029a7c087614b0daff643e0f48c46b429cc65dce4b2421 | quote: Your premium links are automatically removed once you end leeching the file.
  - [1] 2026-11-03: the vendor states no bandwidth limit | capture: sha256:d70426b70db3f6942b029a7c087614b0daff643e0f48c46b429cc65dce4b2421 | quote: Max download speed, 100% guaranteed! We don't limit your download bandwidth in any way.
  - [1] 2026-11-03: the first step of the flow takes a link and no account | capture: sha256:d70426b70db3f6942b029a7c087614b0daff643e0f48c46b429cc65dce4b2421 | quote: Input your link in the field above.
  - [1] 2026-11-03: the generated link is locked to one user IP | capture: sha256:d70426b70db3f6942b029a7c087614b0daff643e0f48c46b429cc65dce4b2421 | quote: The provided premium link is locked to a single user IP, only you may have access to it.
- sources:
  - [1] https://www.hotdebrid.com/
