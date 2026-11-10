# Elende

> elende.ao | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/elende/ | JSON https://fshy.ajam.dev/api/v1/entity/elende.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Elende

- `compute/elende` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-07T14:17:06.321Z (live) | stale on 2026-12-08
- url https://elende.ao/vps-linux-kvm
- free tier: VPS Linux 1 on the vendor's own KVM page: 1 vCPU, 2 GB RAM, 20 GB disk, KVM virtualisation, 1 public IPv4, and a traffic line that states the traffic is unlimited. The monthly price on the card is 8,625.00 Kz (Angolan kwanza); the same card offers 24,600.00 Kz quarterly, 46,560.00 Kz semiannual and 87,975.00 Kz annual, and the order button carries the order label rather than the unavailable label. The tracker prices this plan at EUR 5.00 per month with 5,000 GB a month on a 0.1 Gbps port in Angola; the vendor page states no euro price, no monthly byte allowance and no port speed. Re-read 2026-11-07: the card still shows 8.625,00 Kz monthly and its price attribute still holds 87.975,00 Kz annual, 46.560,00 Kz semiannual and 24.600,00 Kz quarterly with -1 on the triennial and biennial terms, the cycle tabs 'Trimestralmente Poupe 5 %', 'Semestralmente Poupe 5 %' and '1-Ano Poupe 15 %', and the order button 'Encomendar ja!'. Add-to-cart for pid 183 resolves with status 200 on both the monthly and the annual cycle, landing on the configurator and then the checkout step with no out-of-stock marker, so the plan is in stock. No page read prints a renewal price. The configurator and checkout pages render prices client-side and in kwanza, which the cart-read tool's price scan does not cover; it found no price string on either cart page, so the cart-rendered price is unverified. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the plan card states the traffic is unlimited; no monthly byte cap, fair-use policy or overage price was found on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: ssh, rest
- limits:
  - volume-quota (binding): the two sources disagree: the tracker states a 5,000 GB monthly allowance, the vendor plan card states the traffic is unlimited and publishes no cap, fair-use figure or overage price, so the real byte wall is unverified [1]
- limits note: the two sources disagree: the tracker states a 5,000 GB monthly allowance, the vendor plan card states the traffic is unlimited and publishes no cap, fair-use figure or overage price, so the real byte wall is unverified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: KVM with full root and 1 public IPv4; the page documents no API or object client, so access is SSH plus whatever the panel exposes
- composes with: an Angola-region KVM node at a kwanza price is useful only where West African presence is required; the disk and RAM are below the archive index's needs, so it is a scheduler or crawler-front node rather than a storage host
- reliability: no reliability event recorded
- notes: Prices are recorded in EUR and accented characters are transliterated to ASCII.
- extras:
  - facets.class: price-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.disk_gib: 20
  - price_on_page: 8.625,00 Kz/month for VPS Linux 1
  - renewal_note: not published: no page read prints a renewal price; the plan card prints four term prices (monthly, quarterly, semiannual, annual) and no renewal sentence
- evidence:
  - [1] 2026-10-22: the 'VPS Linux 1' plan card shows 1 vCPU, 2 GB RAM, 20 GB disk, 1 public IPv4 and KVM virtualisation, with the monthly price rendered as '8.625,00 Kz' and the order button reading 'Encomendar ja!'
  - [1] 2026-10-22: the price element carries the four term prices in its data attribute: 87.975,00 Kz annual, 46.560,00 Kz semiannual, 24.600,00 Kz quarterly and 8.625,00 Kz monthly, with -1 for the terms not offered
  - [2] 2026-10-22: row quoted from the Cheapest VPSs table: 'EUR 5.00 / month', '1 Intel Cores (shared)', '2,048 MB RAM', '20 GB HDD', '5,000 GB/month bandwidth', '0.1 Gbps port speed', 'IPv4', 'Angola'
  - probe:https://elende.ao/cart.php?a=add&pid=183&billingcycle=monthly 2026-11-07: add-to-cart for VPS Linux 1 (pid 183) on the monthly cycle resolves to the configurator with HTTP 200 and no out-of-stock marker, so the plan is in stock | capture: sha256:24888ab3b0d04e11f4e5475d452b7c6fb6b77d3066dfbb29a54d149375344c7c | quote: "final_url": "https://elende.ao/cart.php?a=confproduct&i=0"
  - probe:https://elende.ao/cart.php?a=add&pid=183&billingcycle=annually 2026-11-07: the annual-cycle add resolves to the configurator with HTTP 200 the same way, so the annual term is orderable | capture: sha256:69acec1d4585fe725493297ffc1da2aa2f05ff26065f2f8cc22b0694ad8cc3e7 | quote: "final_url": "https://elende.ao/cart.php?a=confproduct&i=0"
  - probe:https://elende.ao/cart.php?a=view 2026-11-07: the cart view advances to the checkout step with HTTP 200 and no out-of-stock marker | capture: sha256:5b6492dc8cf0c64e3c7601952c7f4cf6719a182c9ef84bc4dd20880d23a10da5 | quote: "final_url": "https://elende.ao/cart.php?a=checkout"
  - [1] 2026-11-07: the plan card's price attribute holds -1 on triennial and biennial, then 87.975,00 Kz annual, 46.560,00 Kz semiannual, 24.600,00 Kz quarterly and 8.625,00 Kz monthly, unchanged | capture: sha256:68c351f05db4e5e6562c75f383778b0eac2773f8ded57f379d02056a8b58b9cf | quote: ["-1","-1","87.975,00 <sub> Kz</sub>","46.560,00 <sub> Kz</sub>","24.600,00 <sub> Kz</sub>","8.625,00 <sub> Kz</sub>"]
  - [1] 2026-11-07: the plan card prices VPS Linux 1 at 8.625,00 Kz a month | capture: sha256:68c351f05db4e5e6562c75f383778b0eac2773f8ded57f379d02056a8b58b9cf | quote: ["-1","-1","87.975,00 <sub> Kz</sub>","46.560,00 <sub> Kz</sub>","24.600,00 <sub> Kz</sub>","8.625,00 <sub> Kz</sub>"]
- sources:
  - [1] https://elende.ao/vps-linux-kvm
  - [2] https://vpspricetracker.com/provider/Elende/vps
