# freevpshostings.com

> freevpshostings.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freevpshostings/ | JSON https://fshy.ajam.dev/api/v1/entity/freevpshostings.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freevpshostings.com

- `egress/freevpshostings-com` | trial-only | evidence documented | binding volume-quota | category origin VM (claimed free plan) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:10:53.451Z (live) | stale on 2026-12-20
- url https://freevpshostings.com/
- price USD 0 for 7 days
- free tier: Learner ... $0 for 7 days, not for production ... No Root Access ... 1-Core CPU ... 10 GB Bandwidth ... WordPress Only | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10 GB Bandwidth; ingress: none | metered: yes | free allowance: 10 GB Bandwidth | source: [1]
- identity: email | detail: the plan page is reached through a registration form and the FAQ advertises 'no credit card requirements for the free tier'; no identity document was stated on the page | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 10 GB Bandwidth on the Learner plan (USD 0 for 7 days, not for production) [1]
  - write-gated: no root access, WordPress only, so the software on the host is fixed [1]
- binding note: The vendor plan table states 10 GB Bandwidth on the Learner plan, which is USD 0 for 7 days and not for production; no period is stated for the 10 GB.
- interface detail: the plan advertises no root access, so the only interface is a hosting panel
- tooling: nothing: no root, no package installs
- composes with: does not compose into any path
- reliability: no root access and a fixed WordPress image, so the server cannot host a tunnel at all
- notes: Surfaced by the search for a free VPS that lasts. The headline says free forever and the plan table says 7 days; the plan table is specific and the FAQ is the marketing line, so the record takes the 7 days. Either way the write gate settles it: a WordPress slice with no root cannot run WireGuard.
- evidence note: the plan table and the FAQ answer are on the page read; the two contradict each other and the plan table is the specific statement
- extras:
  - wg_path: none
  - wg_detail: no root access and 'WordPress Only', so nothing can be installed and wg-quick cannot run; the plan is a managed WordPress slice, not a server
  - ingress: none
  - volume_tib_month: 0.0091
  - volume_stated: 10 GB Bandwidth
  - bytes_transit: yes
  - transit_note: bytes would leave through the host's shared address, but nothing can be installed to generate them
- evidence:
  - [1] 2026-10-23: the Learner plan reads '$0 for 7 days, not for production' with 'No Root Access', '500 MB SSD', '10 GB Bandwidth', 'WordPress Only'
  - [1] 2026-10-23: the FAQ answer reads 'Yes, our Learner plan is completely free with no time limits or hidden charges', which contradicts the 7-day term in the plan table on the same page
  - [1] 2026-11-19: the first-party plan table states a 10 GB bandwidth allowance with a number and unit | capture: sha256:9e449312ccaeee008011042201646d0a4b243709fb2e984b833839d593af969d | quote: 10 GB Bandwidth
  - [1] 2026-11-19: the Learner plan is a 7-day non-production offer; the 10 GB figure appears in the same plan table | capture: sha256:9e449312ccaeee008011042201646d0a4b243709fb2e984b833839d593af969d | quote: for 7 days, not for production
  - [1] 2026-11-19: the binding is the first-party 10 GB bandwidth volume quota | capture: sha256:9e449312ccaeee008011042201646d0a4b243709fb2e984b833839d593af969d | quote: 10 GB Bandwidth
- sources:
  - [1] https://freevpshostings.com/
