# PrimeLeech

> primeleech.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/primeleech/ | JSON https://fshy.ajam.dev/api/v1/entity/primeleech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PrimeLeech

- `debrid/primeleech` | qualifies-with-caveat | evidence documented | binding pull-count | category premium-link generator (free, no account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://www.primeleech.com/
- price USD 0
- free tier: Free premium link generation: 'our advanced script will download it to our server, for free, without needing a premium account' and the files are 'sent to you at maximum speed without any annoying ads or hourly limits'. | unit: objects | metered on: object-count | read on: 2026-10-23 | source: [1] | note: No number is given for files per day; the promise is the absence of an hourly limit.
- per-object cap: not stated | source: [1]
- retention: 'The downloaded files are stored on our secure server' - how long is unstated | source: [1]
- egress: 'maximum speed without any annoying ads or hourly limits'. No byte allowance published. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: No account or login on the generator page.
- interface: unknown
- limits:
  - pull-count (binding): no number stated; 'without any annoying ads or hourly limits' [1]
- limits note: The page promises an absence of an hourly limit without publishing a daily one. A cap that is real but unpublished is worse than a published cap, because it cannot be planned around.
- binding note: Named as pull-count by elimination: nothing on the page prices bytes or shapes the IP, and the only quantity the service discusses is how many links a user generates.
- interface detail: Web form plus one static page per supported host under /generator/<host>.html. No API.
- tooling: browser only. The per-host pages make a scripted loop easy in principle; the request shape was not read.
- composes with: The widest host list of the free generators read, at roughly 90 hosts including isra.cloud, filestore.me, emload and extmatrix. Useful for the long tail a debrid subscription leaves out.
- reliability: No stated cap and no account means the only throttle available to the operator is a silent refusal, which is the failure a client will meet at volume.
- notes: Host list is the asset here: it names hosts the paid debrids do not carry, which is the gap hit on a specific release.
- evidence note: The absence of a cap is read from the vendor's own sentence. The host list is read directly from the page. A download would raise the egress claim to measured.
- extras:
  - hosts_listed: 90
  - hosts_distinct_from_debrid: isra.cloud, extmatrix.com, filestore.me, chomikuj.pl, brupload.net
- evidence:
  - [1] 2026-10-23: 'without any annoying ads or hourly limits', the free-script sentence, and the per-host generator list including isra.cloud, extmatrix.com, filestore.me and emload
- sources:
  - [1] https://www.primeleech.com/
