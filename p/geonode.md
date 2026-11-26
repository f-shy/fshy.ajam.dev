# Residential and mobile proxy free trials

> geonode.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geonode/ | JSON https://fshy.ajam.dev/api/v1/entity/geonode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Residential and mobile proxy free trials

- `egress/residential-proxy-trial` | fails-quota | evidence reported | binding volume-quota | category residential exit (dead end class)
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:23:44.599Z (live) | stale on 2026-12-10
- url https://www.geonode.com/pricing
- free tier: residential trial is paid: 3 days for USD 5; a 1 TB program gives 1 TB free for 7 days to teams using 500+ GB/month, by application, no credit card | unit: GB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: unverified: the pricing page states no per-object cap; the trial is a bandwidth allowance | source: [1]
- retention: the trial allowance expires in days | source: [1]
- egress: metered by the gigabyte; residential rates run from USD 0.792/GB (10 GB plan) to USD 0.270/GB at 100 TB | metered: yes | source: [1]
- identity: card | detail: the USD 5 residential trial is a paid purchase; the 1 TB program is by application with no credit card
- interface: rest
- limits:
  - volume-quota (binding): 1 TB free for 7 days (1TB Program, by application); the paid residential trial is 3 days for USD 5 [1]
- interface detail: an HTTP or SOCKS5 proxy with credentials
- tooling: none needed beyond curl
- composes with: a metered capacity lane, useful as an identity-rotation tool, at USD 0.270/GB to USD 0.792/GB for residential bandwidth.
- reliability: unverified: only the Geonode pricing page was re-read; other providers' trials were not
- notes: A workload of 1099.51 GB per day costs USD 870.8 per day at USD 0.792/GB and USD 296.9 per day at USD 0.270/GB (100 TB rate). Not a capacity source at any published price.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the proxy carries the request and the response through the residential peer
- evidence:
  - [1] 2026-10-22: per-GB residential pricing; the free trial is card-gated
  - [1] 2026-11-25: residential trials are a USD 5 3-day trial and a 1 TB 7-day program, not 100 MB to 2 GB | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: Trial: 3-day trial for $5. Teams using 500+ GB/month can apply for the 1TB Program — 1 TB free for 7 days, approval in under 24 hours, no credit card:
  - [1] 2026-11-25: published residential rates are 0.792 USD/GB at entry and 0.270 USD/GB at 100 TB | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: | Residential proxies | $0.792/GB (10 GB plan); $0.270/GB at 100 TB | per GB |
  - [1] 2026-11-25: the grant is a time-boxed bandwidth allowance (1 TB for 7 days), a volume quota; no per-object cap is stated | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: Trial: 3-day trial for $5. Teams using 500+ GB/month can apply for the 1TB Program — 1 TB free for 7 days, approval in under 24 hours, no credit card:
  - [1] 2026-11-25: the limit is a bandwidth allowance for a fixed time | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: Trial: 3-day trial for $5. Teams using 500+ GB/month can apply for the 1TB Program — 1 TB free for 7 days, approval in under 24 hours, no credit card:
  - [1] 2026-11-25: the allowance figures | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: Trial: 3-day trial for $5. Teams using 500+ GB/month can apply for the 1TB Program — 1 TB free for 7 days, approval in under 24 hours, no credit card:
  - [1] 2026-11-25: the grant is described as a bandwidth allowance | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: Trial: 3-day trial for $5. Teams using 500+ GB/month can apply for the 1TB Program — 1 TB free for 7 days, approval in under 24 hours, no credit card:
  - [1] 2026-11-25: the 3-day trial costs USD 5 and the 1 TB program needs no credit card | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: Trial: 3-day trial for $5. Teams using 500+ GB/month can apply for the 1TB Program — 1 TB free for 7 days, approval in under 24 hours, no credit card:
  - [1] 2026-11-25: the page read is the Geonode pricing page | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: | Residential proxies | $0.792/GB (10 GB plan); $0.270/GB at 100 TB | per GB |
  - [1] 2026-11-25: the residential rates | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: | Residential proxies | $0.792/GB (10 GB plan); $0.270/GB at 100 TB | per GB |
  - [1] 2026-11-25: the per-GB rates used | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: | Residential proxies | $0.792/GB (10 GB plan); $0.270/GB at 100 TB | per GB |
  - [1] 2026-11-25: residential bandwidth is billed per GB | capture: sha256:e8326c43b952fc80b9af624ea17aded7ee72e1a61539dab4d006752ac0dc9078 | quote: | Residential proxies | $0.792/GB (10 GB plan); $0.270/GB at 100 TB | per GB |
- sources:
  - [1] https://www.geonode.com/pricing
