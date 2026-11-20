# JustHosting

> just.hosting | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/just/ | JSON https://fshy.ajam.dev/api/v1/entity/just.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JustHosting

- `compute/justhosting` | paid-only | evidence reported | binding none | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:35.516Z (live) | stale on 2026-11-22
- url https://just.hosting/services/vps/tariffs/jh-1c-1g-20gb-nvme
- free tier: Sirius (jh-1c-1g-20gb-nvme) at USD 8.09/month, or USD 6.47/month when paid for 12 months (vendor tariff page 2026-11-07): 1 Intel core shared, 1,024 MB RAM, 20 GB NVMe, unmetered 300 Mbps port (fair-share, which the card equates to 93+ TB a month), IPv4 + IPv6, Tirana Albania. Billing terms run monthly to 36 months: the configurator's price table discounts 3 months 5%, 6 months 10%, 12 months 20% and 36 months 40% off the USD 8.09025 base, so the 12-month term totals USD 77.64. The configurator rendered its order form with no out-of-stock notice, so the plan is in stock; the order form posts to the site's own API behind a login/register step, and no guest cart page prices the plan. No renewal price is published. The IPv6-only Sirius variant is USD 6.02/month, or USD 4.81/month on 12 months; the tracker's USD 4.82/month row matches that variant's 12-month rate, not this plan's IPv4+IPv6 price. The vendor's plan page sells "Free unmetered traffic. You only pay for disk space. Every plan includes unlimited traffic." and prices the IPv4 separately at USD 3.31/month, with the free IPv6 address described as the budget path. The page title advertises "VPS from $1.99", which is the VPS Promo plan's first-month price; its terms read 'The "VPS Promo" plan is billed at a promotional price for the first month, then automatically switches to a suitable regular plan.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the plan page claims unlimited traffic and no metering, and sells bandwidth as a port upgrade (USD 2.50 a month for 10 Mbps more, USD 333.33 a month for a dedicated 1 Gbps); the tracker's 51,200 GB a month is not on the vendor page and is not recorded as the vendor's allowance | metered: no | source: [1]
- identity: email | detail: not stated
- interface: ssh
- limits note: the plan page states no byte allowance at all ("Free unmetered traffic ... unlimited traffic") while the tracker lists 51,200 GB a month and a 0.29 Gbps port for the same plan; with an allowance stated only by a third party, the record says none and flags the conflict here rather than choosing the tracker's number as the vendor's.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with root, SSH access, instant location switching across 80 locations and IP changes from the client area, sold through a configurator; the company is Baxet Group Inc. of Hong Kong and the site states 379,589 customers and 53,131 active VPS.
- composes with: 20 GB of NVMe with claimed unlimited traffic and instant location switching is a crawler front end that can be moved when a region is rate-limited; 1 GB of RAM keeps it a relay, and the IPv4 at USD 3.31 a month raises the real cost by 69 percent over the advertised figure, so the IPv6-only build is the budget path and the one comparative records would use.
- reliability: no reliability event recorded
- notes: The tracker and the vendor disagree on the meter: the tracker publishes 51,200 GB a month and a 0.29 Gbps port, the vendor page says unlimited traffic and sells port upgrades. The price is also tracker-only, since the plan page carries "VPS from $1.99" in its title and no plan price in its body; the two are not the same figure and the title is not used as the price. verification criteria: a render of the configurator for the per-plan price, and the fair-use clause that sits behind "unlimited traffic", which is the term that would replace none with a real binding.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
- evidence:
  - [2] 2026-10-22: the cheapest row quoted: "JustHosting - $4.82 / month" / "cpu 1 Intel Cores (shared)" / "ram 1,024 MB RAM" / "disk 20 GB NVMe" / "bandwidth 51,200 GB/month bandwidth" / "rj45 0.29 Gbps port speed" / "inet IPv4 + IPv6" / "city Tirana Albania", product slug Sirius_IPv6
  - [1] 2026-10-22: the traffic term quoted: "Free IPv6 address for VPS" / "Perfect for a budget virtual server: no need to buy an IPv4 address" and "Free unmetered traffic - You only pay for disk space. Every plan includes unlimited traffic."
  - [1] 2026-10-22: the add-on table quoted: "Sysadmin services | $9.16/hour", "IPv4 address | $3.31/month", "+10 Mbps bandwidth | $2.50/month", "Dedicated 1 Gbps bandwidth | $333.33/month"
  - [1] 2026-11-07: the vendor's tariff page prices the Sirius plan at $8.09 per month, or $6.47 per month when paid for 12 months; the tariff cards carry Choose plan buttons and the configurator rendered, so the plan is in stock; no renewal price is published | capture: sha256:1bd29aa738ec6a387114cbd41272baa9ad433309fe3e9e04cb6f4a8b7ba70044 | quote: data-plan_uid="sirius" ... $8.09 ... $6.47 ... when you pay for 12 months
  - [1] 2026-11-07: the vendor's tariff page prices Sirius at USD 8.09 per month and USD 6.47 per month on the 12-month term | capture: sha256:1bd29aa738ec6a387114cbd41272baa9ad433309fe3e9e04cb6f4a8b7ba70044 | quote: data-plan_uid="sirius" ... $8.09 ... $6.47 ... when you pay for 12 months
  - [1] 2026-11-07: the tariff card prices the 12-month term from $6.47 per month | capture: sha256:85b6cb7602588d6e251a0eaebfa0770337da4d13a280f37c9d46bb2bb85a799c | quote: $6.47</span> <span class="plan-price__info"> when you pay for 12 months
  - [1] 2026-11-07: the tariff card prints the monthly term at $8.09, struck through with a -20% mark | capture: sha256:85b6cb7602588d6e251a0eaebfa0770337da4d13a280f37c9d46bb2bb85a799c | quote: $8.09</span></del> <span class="plan-discount__percent">-20%</span>
  - [1] 2026-11-07: the card's port line reads Unmetered port: 300 Mbps (fair-share) * (equivalent to: 93+ TB/mo) | capture: sha256:85b6cb7602588d6e251a0eaebfa0770337da4d13a280f37c9d46bb2bb85a799c | quote: Unmetered port: <strong>300 Mbps</strong> (fair-share) <br /> * (equivalent to: <b>93+ TB/mo</b>)
  - [3] 2026-11-07: the configurator's price table carries the Sirius base price USD 8.09025 | capture: sha256:30c214e3cc84a9457b9ad4d8653dd0a3f03b78f5c17756b57b67c9e94fa4d972 | quote: "USD":"8.09025"
  - [3] 2026-11-07: the configurator's discount table: 5% from 3 months, 20% at 12 months, 40% at 36 months | capture: sha256:30c214e3cc84a9457b9ad4d8653dd0a3f03b78f5c17756b57b67c9e94fa4d972 | quote: "3":5 ... "12":20 ... "36":40
  - [4] 2026-11-07: the order flow carries a login/register step (No account? / Sign up / Log in), so checkout continues behind an account | capture: sha256:2028f25b6e4fdd4b43ba17cfce2dccee53e14f05ef410799f3ad302f3c763bc0 | quote: "noAccount":"No account?","alreadyHaveAccount":"Already have an account?","register":"Sign up"
  - [1] 2026-11-07: the tariff card still prices the 12-month term from $6.47 per month | capture: sha256:85b6cb7602588d6e251a0eaebfa0770337da4d13a280f37c9d46bb2bb85a799c | quote: $6.47</span> <span class="plan-price__info"> when you pay for 12 months
- sources:
  - [1] https://just.hosting/services/vps/tariffs/jh-1c-1g-20gb-nvme
  - [2] https://vpspricetracker.com/provider/JustHosting/vps
  - [3] https://just.hosting/api/v1/cloud-vps/manifest
  - [4] https://just.hosting/services/vps/tariffs/sirius
