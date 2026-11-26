# dediseedbox

> dediseedbox.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dediseedbox/ | JSON https://fshy.ajam.dev/api/v1/entity/dediseedbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dediseedbox

- `storage/dediseedbox` | paid-only | evidence documented | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:45:00.000Z (inherited) | stale on 2026-11-23
- url https://www.dediseedbox.com/
- free tier: No free tier published. The home page sells seedbox and VPS hosting in the Netherlands with "10Gbps Unlimited traffic" and "50+ apps One-click install". | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the price is not on the home page
- per-object cap: not applicable: a rented seedbox, so the plan disk is the only object store and no per-file cap is published | source: [1]
- retention: not applicable: the volume is rented for the plan term | source: [1]
- egress: Unlimited traffic, stated on the home page as "10Gbps Unlimited traffic". No byte allowance is published. | metered: no | free allowance: unlimited traffic, stated | source: [1]
- identity: email | detail: a client area is required to deploy; the signup fields were not read
- interface: unknown
- limits note: no named constraint was read: the home page publishes throughput and no byte cap
- binding note: nothing in the vocabulary was found to fail at this scale; the offer is a paid plan and its disk size is the only stated limit
- interface detail: the home page names one-click applications, not retrieval protocols
- tooling: vendor lists 50+ one-click apps including Plex, Jellyfin, Emby, Sonarr, Radarr and SABnzbd
- composes with: a rented seedbox gives a retrieval endpoint with no client hardware; it composes with a debrid key or a public index, and the client retrieves over whatever protocol the plan exposes
- reliability: site answered 200 on 2026-10-23 after the record had called it dead on the evidence of a JS configurator and two 404 paths
- notes: Corrected from verdict dead to paid-only on 2026-10-23: the pricing paths 404 but the service sells hosting and answers. The earlier rejection was a read failure, not a dead provider.
- evidence note: the vendor page was read; the price, the cap and the retrieval protocol were not
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Pricing is behind a JS configurator; /seedbox-plans/ and /seedbox-hosting/ both 404, homepage returns a heading with no plan table. Third-party figures ($25/3TB = $8.33/TB) are…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-23: HTTP 200; "10Gbps Unlimited traffic", "50+ apps One-click install", "NL hosted Netherlands datacenter", and the application list
- sources:
  - [1] https://www.dediseedbox.com/
