# StreamRuby

> streamruby.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/streamruby/ | JSON https://fshy.ajam.dev/api/v1/entity/streamruby.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StreamRuby

- `storage/streamruby` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://streamruby.com
- free tier: 250 GB free storage, grows +250 GB per 1,500 monthly views; 'no upper limit'; unlimited bandwidth; no credit card | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free, explicitly unmetered. 'Unlimited Bandwidth / Never worry about traffic spikes or overage fees'; HLS delivery from their CDN. | metered: no
- identity: card
- interface: rest
- limits note: 20,000 MB (20 GB) per file per the official plan table; video-only (HLS transcode); 60-day deletion when unviewed for free tier
- interface detail: rest
- tooling: XFileSharing-style api.html + PolyUploader (github.com/spel987/PolyUploader) lists StreamRuby; XFS '?op=api' key pattern applies
- composes with: The quota scales with views rather than accounts, i.e. 250 GB + 250 GB per 1.5k monthly views. A view-inflation loop (or simply many free accounts) turns this into an unbounded pool; each account independently starts at 250 GB.
- reliability: video-only: everything is transcoded to HLS, so it is not byte-exact storage; free-tier storage allowance is recomputed monthly from views, so it can shrink (existing videos are not deleted)
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views'; 'Unlimited Bandwidth'; 'A lower allowance won't delete your existing videos'
  - [2] 2026-10-21: 20,000 MB max upload for free tier, 60-day no-download expiry (per awesome-file-hosts citations of this page)
  - [3] 2026-10-21: StreamRuby listed as a supported host
- sources:
  - [1] https://streamruby.com/
  - [2] https://streamruby.com/premium
  - [3] https://github.com/spel987/PolyUploader
