# Stamen map tiles

> stamen.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stamen/ | JSON https://fshy.ajam.dev/api/v1/entity/stamen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Stamen map tiles (maps.stamen.com)

- `data-apis/stamen-map-tiles` | qualifies-with-caveat | evidence documented | binding volume-quota | category map tiles (Stamen styles hosted by Stadia Maps) | tier Stamen styles on Stadia Maps
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:41.926Z (live) | stale on 2026-12-03
- url https://maps.stamen.com/stadia-partnership/
- free tier: Creating the Stadia Maps account needs no credit card | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: the 200,000-tile figure is from the Stamen page's text of 2023 and the allowance is the Stadia Maps Free plan's, whose current credit terms sit on the Stadia Maps pricing page; the keyless maps.stamen.com tile service ended when its redirects stopped on October 31, 2023
- per-object cap: in the legacy archive each tile is one object at s3://{bucket}{prefix}/{z}/{x}/{y}.{extension}; the archive is an outdated snapshot that does not cover the whole globe at every zoom level | source: [1]
- retention: source: [1]
- egress: the legacy S3 buckets are requester-pays: AWS charges the downloader for requests and bandwidth and does not charge Stamen | metered: yes | source: [1]
- identity: email | detail: a Stadia Maps account, which the migration guide says needs no credit card to create; the legacy S3 archive needs an AWS account that pays the request and bandwidth charges
- interface: rest, s3
- limits:
  - volume-quota (binding): under 200,000 tiles a month free; plans from $20/month above that or [1]
  - request-rate: unverified: the Stamen pages state no rate limit; the Stadia Maps plan governs it [1]
- binding note: no rate limit is stated on the Stamen pages, so the 200,000-tile monthly figure is the first limit met
- interface detail: HTTPS XYZ tile URLs at tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.png (stamen_terrain and stamen_watercolor too, the latter a .jpg) with domain authentication or an api_key parameter; the original tiles are in requester-pays S3 buckets tile.stamen.com and long-term.cache.maps.stamen.com
- endpoint: https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.png
- tooling: Leaflet, MapLibre, OpenLayers and any XYZ tile client; the AWS CLI or an SDK with requester-pays enabled for the legacy buckets
- composes with: the Stamen styles spend the same Stadia Maps account and free tile allowance as any other Stadia Maps tile; the original keyless maps.stamen.com service ended on October 31, 2023, so a new project signs up with Stadia Maps or reads the legacy archive from requester-pays S3 buckets
- reliability: the keyless maps.stamen.com tile service ended on October 31, 2023 and its redirects no longer work; the legacy archive is outdated and incomplete, provided to be accessed and used at the user's own risk
- notes: Free requests: under 200,000 tiles a month, through a Stadia Maps account. Rate limit: not stated on the Stamen pages. Bulk path: the legacy tile archive in requester-pays S3 buckets, billed to the downloader by AWS.
- evidence note: the Stamen home page and its Stadia Maps partnership page, the Stadia Maps Stamen page and the migration guide were quoted on 2026-11-02; the 200,000-tile figure is dated 2023 and may differ from the current Stadia Maps credit terms. No account was opened and no legacy tile was downloaded.
- extras:
  - rate_limit: unverified: not stated on the Stamen pages
  - bulk_path: legacy tile archive in requester-pays S3 buckets tile.stamen.com and long-term.cache.maps.stamen.com
- evidence:
  - [2] 2026-11-02: Stamen map tiles have been served by Stadia Maps since July 31, 2023 | capture: sha256:d55333aed9b3c8d945958ee007713d6711745d7b487016c2e7a2773eae239c5b | quote: As of July 31, 2023, Stamen Map Tiles are served by Stadia Maps.
  - [1] 2026-11-02: Stadia Maps hosts the Stamen map tiles | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: We are pleased to announce that we are partnering with Stadia Maps to provide tile hosting for Stamen map tiles.
  - [1] 2026-11-02: the redirects from the old tile service stopped on October 31, 2023 | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: redirects stopped working on October 31, 2023.
  - [1] 2026-11-02: usage under 200,000 tiles a month is free | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: If your current usage is less than 200,000 tiles / month—FREE
  - [1] 2026-11-02:  | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: If your usage goes above 200,000 tiles / month or you are a commercial user—plans start at $20/month.
  - [3] 2026-11-02: the Stamen maps are on all Stadia Maps plans and free for non-commercial projects | capture: sha256:3a2bdd3baa3289dd43a0610f4fb4051a5c62734d199f871a0f1c6414c4cf2d77 | quote: The Stamen maps are available with all of our plans and priced as normal vector or raster map tiles. Get started for as little as $20/month, or free if your project is non-commercial.
  - [3] 2026-11-02: the Stadia Maps tiles are drop-in compatible with Leaflet, MapLibre and OpenLayers | capture: sha256:3a2bdd3baa3289dd43a0610f4fb4051a5c62734d199f871a0f1c6414c4cf2d77 | quote: drop-in compatible with Leaflet, MapLibre, OpenLayers, and more
  - [4] 2026-11-02: creating a Stadia Maps account needs no credit card | capture: sha256:1cbaf6d4b66a5611a7a015b16a8dda8b7a25e7a0d6ea96c3ef207836e5ea5aca | quote: No credit card is required to create an account, and we offer a free tier for non-commercial users.
  - [4] 2026-11-02: the Stamen Toner tile URL on Stadia Maps | capture: sha256:1cbaf6d4b66a5611a7a015b16a8dda8b7a25e7a0d6ea96c3ef207836e5ea5aca | quote: | `toner` | `https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.png` | |
  - [4] 2026-11-02: the Stamen Watercolor tile URL on Stadia Maps is a JPEG path | capture: sha256:1cbaf6d4b66a5611a7a015b16a8dda8b7a25e7a0d6ea96c3ef207836e5ea5aca | quote: https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg
  - [4] 2026-11-02: an API key can replace domain authentication | capture: sha256:1cbaf6d4b66a5611a7a015b16a8dda8b7a25e7a0d6ea96c3ef207836e5ea5aca | quote: If you'd like to use an API key instead of domain auth, simply append `?api_key=YOUR-API-KEY` to the URLs above.
  - [4] 2026-11-02: onboarding sets up domain authentication or an API key | capture: sha256:1cbaf6d4b66a5611a7a015b16a8dda8b7a25e7a0d6ea96c3ef207836e5ea5aca | quote: the onboarding flow will walk you through setting up domain authentication or an API key
  - [1] 2026-11-02:  | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: If you have the resources to cache and host our existing tiles, you are welcome to host, share, modify, and use the original tiles we have been serving up for over ten years.
  - [1] 2026-11-02: the legacy tiles | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18
  - [1] 2026-11-02:  | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: Otherwise, you can use these maps anywhere, we just ask that you attribute the work appropriately.
  - [1] 2026-11-02: the legacy tiles are in requester-pays AWS S3 buckets | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: we are providing the tiles in AWS S3 buckets that are set to requester pays.
  - [1] 2026-11-02: AWS charges the downloader and not Stamen | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: AWS will charge you for accessing and downloading a copy of the tiles and will not charge Stamen.
  - [1] 2026-11-02: downloading the legacy tiles needs an AWS account | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: You will need an AWS account and will want to follow the directions in the
  - [1] 2026-11-02: the legacy archive is old and does not cover the whole globe at every zoom level | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: It has been nearly a decade since the data behind the tiles was updated and the archived tiles do not cover the entire globe at all zoom levels.
  - [1] 2026-11-02: the legacy archive is provided to be used at the user's own risk | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: They are provided to be accessed and used at your own risk.
  - [1] 2026-11-02: the Toner tiles are in the long-term.cache.maps.stamen.com bucket | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: | Toner | long-term.cache.maps.stamen.com | /toner | png |
  - [1] 2026-11-02: the Terrain tiles are in the tile.stamen.com bucket | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: | Terrain | tile.stamen.com | /terrain | png |
  - [1] 2026-11-02: a legacy tile is addressed by bucket, prefix, z, x and y | capture: sha256:9c7a0bf4395bd9ded52e2ede2cd7ef5a3db71894943fa93f44e59361fa7fbf18 | quote: s3://{bucket}{prefix}/{z}/{x}/{y}.{extension}
- sources:
  - [1] https://maps.stamen.com/stadia-partnership/
  - [2] https://maps.stamen.com/
  - [3] https://stadiamaps.com/stamen/
  - [4] https://docs.stadiamaps.com/guides/migrating-from-stamen-map-tiles/
