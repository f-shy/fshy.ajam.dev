# Theta EdgeCloud

> thetaedgecloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thetaedgecloud/ | JSON https://fshy.ajam.dev/api/v1/entity/thetaedgecloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Theta EdgeCloud

- `compute/theta-edgecloud` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:36:22.537Z (live) | stale on 2026-12-04
- url https://www.thetaedgecloud.com/
- free tier: On-demand GPU rental, from USD 0.05 per hour on the vendor page. Vendor rates per GPU-hour: A100 80 GB USD 1.99, H100 80 GB USD 2.29, RTX 4090 USD 0.26, H200 USD 2.29. The index lists the H200 at USD 3.69, the V100 at USD 0.99 and the Tesla T4 at USD 0.20. The L40S is named as an option with no price, and no L4 is listed. A Claim Free Compute link exists; its allowance is unverified: behind a sign-up. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the machine shape
- retention: not applicable | source: [1]
- egress: not published on the pages read | metered: no | source: [1]
- identity: email | detail: The sign-up page shows 'Sign Up' with 'Continue with Google' or an email route and no card, phone or ID field on the page read. Whether a card or crypto balance is needed to launch a GPU, and the size of the Claim Free Compute allowance, are unverified: behind a sign-up.
- interface: rest, cli, ssh
- limits note: No quota is stated: prices are dynamic marketplace rates set by node operators, and live availability needs sign-in.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: REST API, Python, Node.js, Go, Rust and Java SDKs and a CLI; Docker-based jobs with Jupyter and SSH access per the index.
- composes with: A marketplace of community edge nodes and cloud partners with dynamic prices set by node operators; the vendor's own rates for the A100 and the 4090 are among the lowest listed, but availability and live prices need a signed-in dashboard.
- reliability: The index notes community node reliability can vary compared with dedicated data centres and that payments and rewards run on the TFUEL token. No outage was observed.
- notes: Found via computeprices. The index and the vendor page disagree on the H200 (USD 3.69 against USD 2.29): the index row is dated 2026-11-03 and the vendor row is a marketing rate card. The vendor page names the H200, A100, RTX 4090, L40S, V100, A40, RTX A6000 and T4 as options.
- evidence:
  - [1] 2026-11-03: first-party on-demand rate for the A100 80 GB: USD 1.99 per GPU-hour | capture: sha256:f334cca4dac6c3d7b32ded7211042a2050f27b977e321374b52c411d06335ec3 | quote: | NVIDIA A100 80GB | $1.99/hr | $4.10/hr | $3.67/hr | $3.67/hr |
  - [1] 2026-11-03: first-party on-demand rate for the H100 80 GB: USD 2.29 per GPU-hour | capture: sha256:f334cca4dac6c3d7b32ded7211042a2050f27b977e321374b52c411d06335ec3 | quote: | NVIDIA H100 80GB | $2.29/hr | $3.10/hr | $3.60/hr | $4.02/hr |
  - [1] 2026-11-03: first-party rate for the RTX 4090: USD 0.26 per GPU-hour | capture: sha256:f334cca4dac6c3d7b32ded7211042a2050f27b977e321374b52c411d06335ec3 | quote: ### RTX 4090 Production AI workloads $0.26 per GPU hour
  - [1] 2026-11-03: the vendor lists the L40S among its GPU options but shows no L40S price and no L4 on the page read | capture: sha256:f334cca4dac6c3d7b32ded7211042a2050f27b977e321374b52c411d06335ec3 | quote: H200A100RTX 4090L40SV100 A40RTX A6000T4
  - [2] 2026-11-03: the index lists the Tesla T4 (not an L4) at USD 0.20 per GPU-hour and lists no H100, A100, L40S, RTX 4090 or L4 for this provider | capture: sha256:5bbaad89204f17be07a01ff73ee4ac7cffba59529f4ed718c53005b2e6e5679b | quote: | [Tesla T4](https://computeprices.com/providers/theta-edgecloud/gpus/t4)1× | $0.20/hr |
  - [2] 2026-11-03: the index notes that availability and pricing require sign-in to view | capture: sha256:5bbaad89204f17be07a01ff73ee4ac7cffba59529f4ed718c53005b2e6e5679b | quote: - GPU availability and pricing require authentication to view
  - [3] 2026-11-03: the sign-up page offers Google sign-in beside an email route; no card, phone or ID field is shown | capture: sha256:e37bdd3699daf9a4cf37df9e5deb68f833cdac93a557ca22939a654cd26c4759 | quote: Continue with Google
  - [1] 2026-11-03: the home page links a Claim Free Compute call to the sign-up page; the allowance is not stated | capture: sha256:f334cca4dac6c3d7b32ded7211042a2050f27b977e321374b52c411d06335ec3 | quote: [Claim Free Compute](https://www.thetaedgecloud.com/sign-up)
- sources:
  - [1] https://www.thetaedgecloud.com/
  - [2] https://computeprices.com/providers/theta-edgecloud
  - [3] https://www.thetaedgecloud.com/sign-up
