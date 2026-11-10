# rdpserverss.com Free IPv6 VPS

> rdpserverss.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rdpserverss/ | JSON https://fshy.ajam.dev/api/v1/entity/rdpserverss.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## rdpserverss.com Free IPv6 VPS

- `egress/rdpserverss-free-ipv6` | trial-only | evidence documented | binding volume-quota | category origin VM (credit trial) | tier trial
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://rdpserverss.com/free-ipv6-vps/
- price USD 0 for the first month, then list price
- free tier: Premium ... $0 first month ... Full Root Access ... 8-Core CPU ... 16 GB RAM ... 1 TB SSD ... 1 TB Transfer | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 1 TB Transfer on the plan that carries root access; ingress: udp | metered: yes | free allowance: 1 TB Transfer on the plan that carries root access | source: [1]
- identity: email | detail: the page title and description both advertise 'No Credit Card' and the registration form is the only gate read; the $100 credit that funds the first month is granted at registration | country: None
- interface: ssh
- limits:
  - volume-quota (binding): 1 TB of transfer on the root-access plan [1]
  - write-gated: the standing $0 plan has no root access and is WordPress only [1]
- binding note: 1 TB is 0.909 TiB, 9% on the decimal reading, so the quota is the first wall and it fails narrowly; the 30-day credit is the second wall, and it is the one that cannot be fixed by buying more traffic
- interface detail: full root over SSH on the Premium plan
- tooling: wg-quick, for the length of the credit
- composes with: a 30-day 1 TB endpoint is a way to measure the path, not a way to keep it
- reliability: the root-access offer is a first-month credit; the standing $0 plan has no root and no custom software
- notes: Same template and same plan names as freevpshostings.com, which suggests one operator behind several free-VPS storefronts; that is an observation about the pages, not a finding about the companies. The root-access plan is genuinely $0 for a first month at 1 TB, which would meet for 30 days, and the standing free plan cannot run anything.
- evidence note: the plan table and the credit framing are on the page read; whether the transfer is per month or per term is not stated, which is why the volume is recorded with the caveat rather than as a monthly rate
- extras:
  - wg_path: native-conf
  - wg_detail: full root access on a KVM-style VPS, so wg-quick is native; the offer is a first-month credit, so the path exists for about 30 days
  - ingress: udp
  - volume_tib_month: 0.909
  - volume_stated: 1 TB Transfer on the plan that carries root access
  - bytes_transit: yes
  - transit_note: bytes leave over one of 24 data centres' uplinks
- evidence:
  - [1] 2026-10-23: the Premium plan reads '$0 first month', 'Full Root Access', '8-Core CPU', '16 GB RAM', '1 TB SSD', '1 TB Transfer'
  - [1] 2026-10-23: the page title reads '#1 Free IPv6 VPS Hosting [$100 30 Day] No Credit Card 2026', so the offer is a 30-day credit
  - [1] 2026-10-23: the standing $0 Learner plan reads 'No Root Access', '500 MB SSD', '10 GB Bandwidth', 'WordPress Only'
- sources:
  - [1] https://rdpserverss.com/free-ipv6-vps/
