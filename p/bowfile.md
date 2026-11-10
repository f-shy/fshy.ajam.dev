# Bowfile

> bowfile.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bowfile/ | JSON https://fshy.ajam.dev/api/v1/entity/bowfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bowfile

- `debrid/bowfile` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (freemium, free uploads without an account) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://bowfile.com/upgrade
- price USD 1.49 (Pro) and USD 2.99 (Vip); billing period and volume not stated
- free tier: Free User: Unlimited Storage, download speed limited, advert supported, files kept for 20 days, maximum file upload size 20.00 GB. | unit: unlimited | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The FAQ states uploading and downloading is free for all users; no byte allowance for downloads is printed.
- per-object cap: Each file you upload must be less than 20 GB in size for free/non accounts or less than 20 GB in size for premium accounts. | bytes: 21474836480 | source: [2] | note: bytes = 20 x 1024^3; the cap is the same on the free and the premium plans.
- retention: Free/non accounts files are kept for 20 days. Premium accounts files are kept for 100 days. | days: 20 | source: [2] | note: The Vip plan keeps files 100 days; the Pro plan 30 days.
- egress: Free downloads run at a limited speed; premium members get no waiting time and direct downloads. No byte allowance is printed for either plan. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The FAQ prices 'free/non accounts' files at 20 days, so upload works without registering; the homepage offers both Upload and Register.
- interface: unknown
- limits:
  - per-object-cap: 20 GB per file on every plan [2]
  - retention-clamped (binding): 20 days for free and non-account files; 30 days Pro; 100 days Vip [1]
  - per-ip-shaping: download speed limited on the free plan; premium has maximum download speed [1]
- binding note: Files vanish after 20 days free; the 20 GB cap is the same on the paid plans, so the paid plans buy retention and speed, not size.
- interface detail: Web upload with a register_non_user upload route. No API page was read.
- tooling: Browser only as read. No rclone backend found.
- composes with: 20 GB per file with no account is large for a free host, but 20-day retention and a speed-limited free download make it a hand-off point, not an archive.
- reliability: The Pro plan keeps files 30 days and the Vip plan 100 days, so the cheaper paid plan keeps files for less time than the dearer one.
- notes: Cheapest paid plan is Pro at USD 1.49, which adds maximum download speed and removes adverts.
- evidence note: Plan list, FAQ and homepage read on the vendor pages on 2026-11-03. The billing period of the $1.49 and $2.99 prices is not printed.
- extras:
  - plans: Free; Pro $1.49; Vip $2.99
- evidence:
  - [1] 2026-11-03: the free plan keeps files 20 days | capture: sha256:0b2f4143600493b5a9e5f8e67277e4397a213455ad6e7108a72b0ba1406bad7c | quote: Files kept for 20 Days
  - [1] 2026-11-03: every plan lists a 20.00 GB maximum upload | capture: sha256:0b2f4143600493b5a9e5f8e67277e4397a213455ad6e7108a72b0ba1406bad7c | quote: Maximum File Upload Size 20.00 GB
  - [2] 2026-11-03: non-account uploads exist and retention is 20 days against 100 days | capture: sha256:172cf06be6a3e569a4c36b4ef987fc3070bb0c7808b80f7b8b5b29a7e1e156bb | quote: Free/non accounts files are kept for 20 days. Premium accounts files are kept for 100 days.
- sources:
  - [1] https://bowfile.com/upgrade
  - [2] https://bowfile.com/faq
