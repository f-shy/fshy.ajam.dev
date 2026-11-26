# Linveo

> linveo.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linveo/ | JSON https://fshy.ajam.dev/api/v1/entity/linveo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Linveo (Intel KVM VPS 16GB - Windows - Ohio)

- `compute/linveo-windows` | qualifies-with-caveat | evidence documented | binding volume-quota | category Windows VPS | tier Intel KVM VPS 16GB - Windows - Ohio
- needs card yes, phone no, ID no, institution no | verified 2026-10-26T13:30:00.000Z (live) | stale on 2026-11-26
- url https://billing.linveo.com/order/main/packages/windows-kvm-vps
- price parsed USD 16/mo
- disagrees on identity_kind: `compute/linveo` says email, `compute/linveo-windows` says card
- disagrees on verdict: `compute/linveo` says paid-only, `compute/linveo-windows` says qualifies-with-caveat
- free tier: no free tier; the 16 GB Windows plan is USD 16.00 a month for 6 CPU cores, 16 GB of RAM and 100 GB of NVMe | unit: none | metered on: none | read on: 2026-10-26 | source: [1]
- per-object cap: not applicable
- retention: the disk persists while the plan is paid; the page states no deletion clock
- egress: 8000 GB a month on a 10 Gigabit port, stated on the plan line | metered: yes | free allowance: 8000 GB per month | source: [1]
- identity: card | detail: an account and a payment method at order; the checkout was not completed
- interface: rest, cli
- limits:
  - volume-quota (binding): 8000 GB a month [1]
  - per-ip-shaping: 10 Gigabit port [1]
- limits note: the page prints the byte allowance and the port. It prints no licence sentence, so the operating-system cost is unknown.
- binding note: 8 TB is the published ceiling; the licence is the open cost, not a quota.
- interface detail: Windows is a selectable image at order; the admin path is RDP on the issued IPv4
- tooling: any RDP client
- composes with: a second USD 16 row beside DataWagon, with more transfer and less disk. It replaces neither the Rabisu row nor the Layer7 row on price.
- reliability: no reliability event observed; the 16 GB plan was orderable on the page read, while an earlier USD 11 listing was out of stock.
- notes: The page sells the Windows plan by name and prints no licence price. The vendor sells the same machine twice: the Linux twin at the identical 6 core, 16 GB, 100 GB shape is USD 11.00 a month, so the Windows layer is USD 5.00 by implication. That 5.00 is arithmetic on two printed vendor prices, not a printed licence line, and it is the cheapest Windows layer found anywhere in the sweep: it sits beside Virtarix at USD 16.00 and Kimsufi at USD 34.00. The 4 GB plan is USD 4.00 and the 8 GB plan is USD 8.00, so the ladder is USD 1 per GB of RAM and the Windows product line is priced on top of it. A buyer who needs a licence in writing should ask before ordering, because the 5.00 is a price difference and not a statement of what it buys.
- evidence note: the shape, the single billing cycle and the USD 16.00 price are printed on the order page, and the Linux twin at the same shape is printed at USD 11.00 for one month, so the USD 5.00 Windows layer is arithmetic on two vendor prices and is inferred rather than stated. The licence treatment is absent rather than stated, which is the field that keeps this at documented: no licence wording appears on the package page or the config page.
- extras:
  - shape.vcpu: 6
  - shape.ram_gib: 16
  - shape.disk_gib: 100
  - billing_model: monthly
  - term: none
  - monthly_usd: 16.0
  - setup_fee_usd: 0.0
  - windows_licence: not stated
  - linux_twin_usd: 11.0
  - linux_twin_url: https://billing.linveo.com/order/config/index/intel-kvm-vps/?group_id=8&pricing_id=51
  - windows_layer_usd: 5.0
  - windows_layer_basis: arithmetic, 16.00 minus 11.00 on two printed vendor prices at the same shape; not a printed licence line
  - ipv4_included: yes
  - port_mbps: 10000
  - traffic: 8000 GB/month
  - locations: Ohio; Texas
  - cart_url: https://billing.linveo.com/order/main/packages/windows-kvm-vps
- evidence:
  - [1] 2026-10-26: quoted: 'Intel KVM VPS 16GB - Windows - Ohio ... 1 Month @ $16.00 ... 6 CPU Cores ... 100 GB NVMe SSD ... 8000 GB Bandwidth'
  - [1] 2026-10-26: quoted: 'Intel KVM VPS 16GB - Windows - Texas ... 1 Month @ $16.00 ... 6 CPU Cores ... 100 GB NVMe SSD ... 8000 GB Bandwidth'
  - [2] 2026-10-26: the Windows config page carries exactly one cycle, '<option value="130" selected="selected">1 Month @ $16.00</option>', and the only configurable field is a hostname; no licence line and no licence wording appears
  - [3] 2026-10-26: the Linux twin at the same 6 cores, 16 GB and 100 GB shape prints two cycles, '1 Month @ $11.00' and '1 Year @ $132.00', so 16.00 minus 11.00 is USD 5.00 and that is the arithmetic value of the Windows layer at this vendor
- sources:
  - [1] https://billing.linveo.com/order/main/packages/windows-kvm-vps
  - [2] https://billing.linveo.com/order/config/index/windows-kvm-vps/?group_id=13&pricing_id=130
  - [3] https://billing.linveo.com/order/config/index/intel-kvm-vps/?group_id=8&pricing_id=51

## Linveo (compute/linveo)

- `compute/linveo` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T11:15:38.153Z (live) | stale on 2026-11-22
- url https://vpspricetracker.com/provider/Linveo/vps
- disagrees on identity_kind: `compute/linveo` says email, `compute/linveo-windows` says card
- disagrees on verdict: `compute/linveo` says paid-only, `compute/linveo-windows` says qualifies-with-caveat
- free tier: USD 3.85/month (Intel KVM VPS 4GB - Ohio): 4,096 MB RAM, 2 CPU cores, 25 GB NVMe SSD, 4,000 GB bandwidth, 10 Gigabit port. The vendor's own Blesta order form (billing.linveo.com) lists the plan at USD 3.85 for 1 Month and USD 46.20 for 1 Year with no other term, and shows it in stock (an Order Now submit button; only the 60 GB Ohio plan carries an Out of Stock marker); the same price is offered in Texas. Renewal: not published. The marketing Intel page (linveo.com/intel) still starts at the 8 GB plan at USD 5.50 and lists no 4 GB card (re-read 2026-11-07). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 4,000 GB a month included per the tracker card (free_allowance is in GB a month); the overage price is not stated on the pages read | metered: yes | free allowance: 4000 | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits:
  - volume-quota (binding): 4,000 GB a month on a 10 Gbps port; the allowance, not the port, is the wall. The 25 GB NVMe is the disk limit on this plan [1]
- limits note: 4,000 GB a month on a 10 Gbps port; the allowance, not the port, is the wall. The 25 GB NVMe is the disk limit on this plan
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: order forms and client area at billing.linveo.com, with per-location configuration links (Ohio group 8, Texas group 9); the vendor documents VNC, reinstall, backups and 10 or more OS templates
- composes with: if the USD 3.85 plan can be ordered it is 4 GB of RAM and 25 GB NVMe for the lowest dollar price on a 4 GB machine among evaluated providers; the vendor's own page does not list it, so a purchase decision should wait on an order form.
- reliability: no reliability event recorded
- notes: The tracker's USD 3.85 plan is a real mismatch with the vendor's product pages, which is why confidence is reported rather than documented: the vendor's cheapest Intel plan is USD 5.50 for 8 GB and its cheapest AMD plan is USD 6.60 for 1 GB, so the 4 GB plan is an order-form-only configuration. The order form (read 2026-11-07) names the plan, prices it at USD 3.85 for 1 Month and USD 46.20 for 1 Year, and shows it in stock with an Order Now button; only the 60 GB Ohio plan carries an Out of Stock marker. The Windows card at USD 4.00 suggests the family exists at that price point.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 25
- evidence:
  - [1] 2026-10-22: card quoted: '$3.85 / month', '2 Intel Cores (shared)', '4,096 MB RAM', '25 GB NVMe', '4,000 GB/month bandwidth', '10 Gbps port speed', 'Ohio U.S.A.'; a second card at the same price is in Texas, and all 12 cards on the page carry an order link
  - [2] 2026-10-22: the vendor's Intel page starts at 'Intel KVM VPS 8GB', '$5.50', 'PER MONTH', '8192 MB RAM', '4 CPU Cores', '50 GB NVMe SSD', '4000 GB Bandwidth', '10 Gigabit Port'; the ladder above it is 16GB at 11, 30GB at 22 and 60GB at 44 in the same currency. No 4 GB plan is listed
  - [3] 2026-10-22: the AMD page starts at 'AMD RYZEN KVM VPS 1GB', '$6.60', '1024 MB RAM', '1 CPU Core (9950X)', '25 GB NVMe', '4000 GB Bandwidth', '10 Gigabit Port'
  - [4] 2026-11-07: the vendor order form lists the 4 GB Ohio plan at USD 3.85 a month and USD 46.20 a year | capture: sha256:954bd2e07df4cdf9395516a8a4b801b7f9410832d852cb906068baf407dead74 | quote: Intel KVM VPS 4GB - Ohio ... 1 Month @ $3.85 ... 1 Year @ $46.20
  - [4] 2026-11-07: the Texas variant of the 4 GB plan is offered at the same USD 3.85 a month | capture: sha256:954bd2e07df4cdf9395516a8a4b801b7f9410832d852cb906068baf407dead74 | quote: Intel KVM VPS 4GB - Texas ... 1 Month @ $3.85
  - [4] 2026-11-07: the order form states the plan's 4 GB RAM, 25 GB NVMe, 4000 GB bandwidth and 10 Gigabit port | capture: sha256:954bd2e07df4cdf9395516a8a4b801b7f9410832d852cb906068baf407dead74 | quote: 4096 MB RAM ... 25 GB NVMe SSD ... 4000 GB Bandwidth ... 10 Gigabit port
  - [4] 2026-11-07: the vendor order form renders an Order Now submit button for the Intel KVM VPS 4GB - Ohio plan, so the plan is orderable | capture: sha256:57a1a1bbc5ca5234db077398d023ae34c4a87de1b137fad57bbe51fb020026c7 | quote: <button type="submit" class="btn btn-lg btn-success float-right">Order Now <i class="fas fa-angle-double-right"></i></button>
  - [4] 2026-11-07:  | capture: sha256:57a1a1bbc5ca5234db077398d023ae34c4a87de1b137fad57bbe51fb020026c7 | quote: <option data-period="1 Month @ " data-display-price="$3.85" value="104">1 Month @ $3.85</option> <option data-period="1 Year @ " data-display-price="$46.20" value="84">1 Year @ $46.20</option>
  - [4] 2026-11-07: the vendor order form lists the 4 GB Ohio plan at USD 3.85 for 1 Month and USD 46.20 for 1 Year | capture: sha256:57a1a1bbc5ca5234db077398d023ae34c4a87de1b137fad57bbe51fb020026c7 | quote: <option data-period="1 Month @ " data-display-price="$3.85" value="104">1 Month @ $3.85</option> <option data-period="1 Year @ " data-display-price="$46.20" value="84">1 Year @ $46.20</option>
- sources:
  - [1] https://vpspricetracker.com/provider/Linveo/vps
  - [2] https://linveo.com/intel
  - [3] https://linveo.com/amd
  - [4] https://billing.linveo.com/order/main/index/intel-kvm-vps
