# UniHost

> unihost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unihost/ | JSON https://fshy.ajam.dev/api/v1/entity/unihost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UniHost

- `compute/unihost` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID yes, institution no | verified 2026-11-24T13:21:06.619Z (live) | stale on 2026-12-25
- url https://unihost.com/vps/germany/
- free tier: LVP-G1 is EUR 6.90 per month excluding VAT for 4 shared AMD EPYC vCores, 6 GB RAM, 100 GB SSD and a 10 Gbps port with 30 TB a month of traffic, in Germany or the Netherlands. The rate read on 2026-11-24 shows a different dollar and pound figure in the comparison row, so those currency values are not repeated. The asterisk on 30 TB is not explained on the page. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The LVP-G1 page lists 30 TB a month of traffic on a 10 Gbps port and states "We offer affordable rates for VPS and do not set limits for clients." No per-GB rate or overage price is published. | metered: yes | free allowance: 30 TB a month, printed as '30 TB*' | source: [1]
- identity: national-id | detail: Payment by bank card requires full account verification with a passport; the VPS itself can be rented without documents when paid by another method.
- interface: browser
- limits:
  - volume-quota (binding): 30 TB a month, printed as "30 TB*", on a 10 Gbps port; the provider states it sets no client limits and the asterisk is not explained on the page read. [1]
- limits note: 30 TB a month, printed as '30 TB*', on a 10 Gbps port. The asterisk is not explained on the page read, so the allowance may carry a fair-use term that was not read.
- binding note: the same as limits note
- interface detail: A web control panel with Cpanel, Linux Plesk, VestaCP or Virtualmin is listed; no REST or SSH interface is documented on the page read.
- tooling: not stated on the page read; the vendor documents a dashboard cart and no client or API in the material read
- composes with: 4 vCores and 6 GB for EUR 6.90 with a 30 TB allowance is the cheapest per-core shape among documented hosts; it suits a scheduler or a scraper front end that bursts, with bulk bytes pushed to an unmetered host
- reliability: no reliability event recorded
- notes: The tracker's row and the vendor's row agree on price and shape, so this is one of the few lane entries where a third-party table and the first-party page can be checked against each other and both hold. The vendor row is 'ex.VAT' and the buyer's VAT position was not read. Unverified: whether the '30 TB*' asterisk hides a fair-use throttle, and whether the Germany and Netherlands rows are the same product.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 6
  - facets.shape.disk_gib: 100
- evidence:
  - [1] 2026-10-22: LVP-G1 row: '4 vCore / AMD EPYC / Shared', '6 GB RAM', '100 GB SSD', '10 Gbps 30 TB*', with data-prices_for_filter="{USD:7.74, EUR:6.90, GBP:5.80}" and the EUR column headed 'Price, EUR / mo.ex.VAT'
  - [1] 2026-10-22: 'LVP-G2 / DE NL / 6 vCore AMD EPYC / Shared / 16 GB RAM / 200 GB SSD / 10 Gbps 30 TB*' at EUR 12 a month in the same table
  - [2] 2026-10-22: tracker agrees: 'These are the cheapest VPSs currently offered by UniHost, starting at EUR 6.90 per month' with 4 Epyc cores (shared), 6,144 MB RAM, 100 GB SSD, 30,720 GB/month, 10 Gbps, Germany
  - [1] 2026-11-24: the LVP-G1 plan is EUR 6.90 per month excluding VAT with 4 vCores, 6 GB RAM, 100 GB SSD and 30 TB traffic in Germany or the Netherlands | capture: sha256:81cf13713190426af88631c9e561ad90e959064862d7d925d299cdcce307aff0 | quote: - LVP-G1 DE NL [4 vCoreAMD EPYC](https://dashboard.unihost.com/cart.php?a=add&pid=2267&cur=1&language=english) Shared 6 GB RAM 100 GB SSD 10 Gbps30 TB\* 7.58 Install: $0 6.90 Install: €0 5.78 Install: £0 - LVP-G2 DE NL [6 vCoreAMD EPYC](https://dashboard.uniho
  - [1] 2026-11-24: the provider states it sets no client limits on VPS use | capture: sha256:67724bcebbc99f8c2292a44d62cb8d1c2d441d82655bf3aa0d33b37241725900 | quote: We offer affordable rates for VPS and do not set limits for clients.
  - [1] 2026-11-24: the LVP-G1 row lists 30 TB of traffic on a 10 Gbps port | capture: sha256:67724bcebbc99f8c2292a44d62cb8d1c2d441d82655bf3aa0d33b37241725900 | quote: 10 Gbps 30 TB\*
  - [1] 2026-11-24: bank-card payment requires full account verification with a passport | capture: sha256:67724bcebbc99f8c2292a44d62cb8d1c2d441d82655bf3aa0d33b37241725900 | quote: VPS server rental can be issued without documents. But please note that when paying with a bank card, you will have to go through a full account verification, which will require a passport.
  - [3] 2026-11-24: the terms allow a request for passport or other identity documents | capture: sha256:9beaa0c8a3f308f70a649b239ce533040d9b12335c1322d20362fa264ecfe627 | quote: Request additional personal data and legitimation (copies of the passport or other documents confirming the identity or status of the Customer) from the Customer
  - [1] 2026-11-24: the VPS ships with a web control panel | capture: sha256:67724bcebbc99f8c2292a44d62cb8d1c2d441d82655bf3aa0d33b37241725900 | quote: ### Control Panel - Cpanel - Linux Plesk - VestaCP - Virtualmin
- sources:
  - [1] https://unihost.com/vps/germany/
  - [2] https://vpspricetracker.com/provider/UniHost/vps
  - [3] https://unihost.com/terms/
