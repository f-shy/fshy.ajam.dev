# Residential and mobile proxy free trials

> geonode.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geonode/ | JSON https://fshy.ajam.dev/api/v1/entity/geonode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Residential and mobile proxy free trials

- `egress/residential-proxy-trial` | fails-quota | evidence reported | binding per-object-cap | category residential exit (dead end class)
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-06
- url https://www.geonode.com/pricing
- free tier: 100 MB to 2 GB for 3 to 14 days, gated on a card, KYC or a minimum top-up | unit: GB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: the trial allowance is 100 MB to 2 GB in total | source: [1]
- retention: the trial allowance expires in days | source: [1]
- egress: metered by the gigabyte once the trial ends; USD 0.80/GB is the cheapest rate seen | metered: yes | source: [1]
- identity: card | detail: every trial surveyed is bounded by a card, KYC or a minimum top-up
- interface: rest
- limits:
  - per-object-cap (binding): the trial allowance is 100 MB to 2 GB in total [1]
- interface detail: an HTTP or SOCKS5 proxy with credentials
- tooling: none needed beyond curl
- composes with: a dead capacity lane that stays live only as an identity-rotation tool, at USD 0.80/GB and up.
- reliability: every trial surveyed is bounded by a card, KYC or a minimum top-up
- notes: At USD 0.80/GB one day of the workload is USD 879.61 and a month is USD 26,388. Not a capacity source at any price available, and the search results for 'free proxy trial' are confidently wrong.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the proxy carries the request and the response through the residential peer
- evidence:
  - [1] 2026-10-22: per-GB residential pricing; the free trial is card-gated
- sources:
  - [1] https://www.geonode.com/pricing
