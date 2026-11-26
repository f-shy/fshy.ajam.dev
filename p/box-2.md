# Box for Nonprofits

> box.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/box-2/ | JSON https://fshy.ajam.dev/api/v1/entity/box-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Box for Nonprofits — donated Starter (10 perpetual licences)

- `storage/box-for-nonprofits-donated-starter` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:06.016Z (live) | stale on 2026-12-04
- url https://www.box.org/use-box/nonprofit
- free tier: Box Starter, free for nonprofits via TechSoup validation: 'Secure file collaboration, storage and native e-signatures for up to 10 users | 100 GB of storage | 2 GB file upload'. The first-party nonprofit page states 'donated Plan' for Starter and 'up to 10 perpetual licenses for Box Starter edition'. 100 GB shared per org. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 2 GB per upload | bytes: 2000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress meter on Box downloads documented on the nonprofit page. | metered: no
- identity: institution
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 2 GB per upload [1]
- limits note: Per-object-cap 2 GB per upload. request-rate: Box API per-app throttling. retention: 'perpetual licenses'. No expiry, which is unusual and worth noting.
- interface detail: rest
- tooling: rclone backend 'box' (Tier 1, server-side copy); Box Content API.
- composes with: 100 GB x one nonprofit org, with 10 perpetual seats sharing that 100 GB. Not 100 GB per seat. Paid Business/Enterprise are 50% off, which is a discount not a grant, so this does not reach 500 GB free.
- reliability: Perpetual license model provides 100 GB aggregate storage without expiration.
- notes: Box Starter, free for nonprofits via TechSoup validation: 'Secure file collaboration, storage and native e-signatures for up to 10 users | 100 GB of storage | 2 GB file upload'. TechSoup confirms 'donations of up to 10 perpetual licenses for Box Starter Edition'. 100 GB shared per org.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Box Starter, free for nonprofits via TechSoup validation: 'Secure file collaboration, storage and native e-signatures for up to 10 users | 100 GB of storage | 2 GB file upload'. TechSoup confirms 'donations of up to 10 perpetual licenses for Box Starter Edition'. 100 GB shared per org.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Starter ... up to 10 users | 100 GB of storage | 2 GB file upload ... Free'
  - [2] 2026-10-21: 'donations of up to 10 perpetual licenses for Box Starter Edition or ... 50 percent discount'
  - withheld 2026-10-21: probe: GET www.box.org/use-box/nonprofit -> 403 on first attempt but full plan table extracted; GET www.techsoup.org/box -> 200
  - [1] 2026-11-19: the first-party nonprofit page still lists Starter at 100 GB storage and 2 GB file upload | capture: sha256:7c76139b1dada0a63dd75e9dae6fd9c7e7e1daf2f7a47fdd44a3b9fcecc9b3ae | quote: Secure file collaboration, storage and native e-signatures for up to 10 users 100 GB of storage 2 GB file upload
  - [1] 2026-11-19: the first-party nonprofit page confirms up to 10 perpetual Box Starter licenses are donated | capture: sha256:7c76139b1dada0a63dd75e9dae6fd9c7e7e1daf2f7a47fdd44a3b9fcecc9b3ae | quote: We donate up to 10 perpetual licenses for Box Starter edition or offer 50% discount on monthly or annual subscriptions to any Box Enterprise plan.
  - [1] 2026-11-19: the first-party page states the institution eligibility requirement for the donated Starter plan | capture: sha256:7c76139b1dada0a63dd75e9dae6fd9c7e7e1daf2f7a47fdd44a3b9fcecc9b3ae
- sources:
  - [1] https://www.box.org/use-box/nonprofit
  - [2] https://www.techsoup.org/box
