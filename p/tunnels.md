# tunnels.io

> tunnels.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnels/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnels.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunnels.io

- `egress/tunnels-io` | fails-egress | evidence documented | binding volume-quota | category tunnel (hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://tunnels.io/pricing
- price USD 0
- free tier: Basic (Free): 4 GB / month bandwidth. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 4 GB per month on the free Basic tier; 128 GB, 256 GB and 512 GB on the paid tiers.; ingress: http-only | metered: yes | free allowance: 4 GB per month on the free Basic tier; 128 GB, 256 GB and 512 GB on the paid tiers. | source: [1]
- identity: email | detail: An account through the signup link on the pricing page; the form was not opened. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 4 GB per month [1]
  - request-rate: 1024 requests per second [1]
- binding note: For a byte-only workload the 4 GB monthly allowance binds, about 275 times below 1 TiB. Here the HTTP-only free tier refuses a UDP workload before a byte is counted, and the constraint vocabulary has no kind that names an ingress protocol.
- interface detail: 'Every plan includes HTTPS, the CLI, the desktop GUI, and request inspection.'
- tooling: CLI, desktop GUI and request inspection; HTTPS on every plan.
- composes with: Nothing here reaches 1 TiB and the free tier cannot carry UDP, so it does not compose with the workload.
- reliability: Not established: no terms page was read and no tunnel was run.
- notes: Tunneling service providing HTTP and TCP ingress. Free tier includes 4 GB of monthly bandwidth and 1 tunnel; paid tiers provide 128 GB, 256 GB and 512 GB.
- evidence note: The free block sits in a collapsed comparison table that the page's own body extraction drops; the figure comes from the raw HTML of the same page, which carries 'Basic (Free)' and '4 GB / month bandwidth'. A rendered read would confirm the association.
- extras:
  - wg_path: none
  - wg_detail: The free tier is HTTP only, TCP appears from the Professional tier up, and no UDP tunnel is offered on any plan on the pricing page.
  - ingress: http-only
  - volume_tib_month: 0.0036
  - volume_stated: 4 GB per month on the free Basic tier; 128 GB, 256 GB and 512 GB on the paid tiers.
  - bytes_transit: yes
  - transit_note: tunnels.io's own relay carries the bytes.
- evidence:
  - [1] 2026-10-23: Raw HTML: 'Basic (Free)' followed by '4 GB / month bandwidth' and 'Student (Free)' with 8 GB; the paid cards list 128, 256 and 512 GB and 'HTTP / TCP'
- sources:
  - [1] https://tunnels.io/pricing
