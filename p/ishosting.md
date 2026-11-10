# is_hosting

> ishosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ishosting/ | JSON https://fshy.ajam.dev/api/v1/entity/ishosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## is_hosting

- `compute/is-hosting` | paid-only | evidence documented | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-08T00:54:56.229Z (live) | stale on 2026-12-09
- url https://ishosting.com/en/vps
- price parsed USD 6.99/mo
- free tier: Lite (order page 2026-11-07): 1 Month USD 6.99/month, 3 Months USD 6.64/month (-5%), 6 Months USD 6.29/month (-10%), 1 Year USD 5.94/month (-15%); Xeon 2.90 GHz, 1 GB RAM, 20 GB NVMe, 1 Gbps port, 1 Tb traffic on the Japan default location, IPv4, VNC and SSH enabled, weekly backup. The plan card at /en/vps prints 'From $5.94' and '$5.64 with is*smart' with '2 Tb Bandwidth', so the card's From price is the 1-year term's per-month rate, not the 1-month rate, and traffic varies by location. The next tier, Start, is USD 10.19 / month with 2 GB RAM, 30 GB SSD and 3 TB. Billing terms are 1, 3, 6 and 12 months; the 1-year term prints USD 71.30 on the order summary and in the plan list (12 x USD 5.94 = USD 71.28, the difference is the rounded per-month rate). The plan is in stock: the order configurator rendered with no out-of-stock notice. No renewal price is printed on the order page, and the site has no guest cart page (/en/cart answers its Not Found (404) page), so the order page's payment-options ladder is the price a visitor can read before checkout. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2 TB a month included on Lite as the plan card states; no overage price published on the page read | metered: yes | free allowance: 2 TB a month | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - volume-quota (binding): 2 TB a month on a 1 Gbps port for 1 GB of RAM and 20 GB of disk. The second limit is IPv4: the Lite row prints 'IPV4 optional', so an address that accepts inbound connections is an add-on, not part of the headline price. [1]
- limits note: 2 TB a month on a 1 Gbps port for 1 GB of RAM and 20 GB of disk. The second limit is IPv4: the Lite row prints 'IPV4 optional', so an address that accepts inbound connections is an add-on, not part of the headline price.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the plan card lists 'Control panels' without naming one and offers KVM with weekly backups; no API was read
- composes with: One gigabyte of RAM and 20 GB of disk cap it at a scheduler or a proxy hop.
- reliability: no reliability event recorded
- notes: The vendor and the tracker disagree on this provider's entry price and on the disk type: the vendor's headline is USD 5.94 for a 20 GB SSD plan, while the tracker's cheapest row is USD 6.99 for a 20 GB NVMe plan in Spain. Both are recorded; neither was averaged. The core count in shape, 1, is the tracker's: the vendor's card names a clock speed, 'Xeon 2.20 GHz', and no core count. The tracker also lists a 1,024 GB/month variant for Indonesia against 2,048 GB for Spain and Kazakhstan, which is a per-location difference the vendor page does not show.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 20
  - price_on_page: USD 6.99/month for Lite on the 1-month term
- evidence:
  - [1] 2026-10-22: Lite plan card, quoted as label and value pairs: 'From' '$5.94' '/ 1 month', a second price line '$5.64' followed by the styled is*smart wordmark, CPU 'Xeon 2.20 GHz', RAM '1 Gb', drive '20GB SSD', '2 Tb' 'Bandwidth', 'IPV4 optional', '1Gbps Port', 'Weekly Backup', 'KVM Virtualization', '40 Countries'; the page's own JSON-LD declares priceCurrency USD with lowPrice 5.94, highPrice 76.49 and offerCount 6, which is where the USD label comes from
  - [1] 2026-10-22: the next tier up, quoted: 'Start' 'From' '$10.19' '/ 1 month' with CPU 'Xeon 2x2.20 GHz', RAM '2 Gb', drive '30GB SSD', '3 Tb' 'Bandwidth', '1Gbps Port'
  - [2] 2026-10-22: tracker row, cells in page order: '1 Intel Cores (shared)', '1,024 MB RAM', '20 GB NVMe', '2,048 GB/month bandwidth', '1 Gbps port speed', 'IPv4', 'Spain', price '$6.99 / month'; also listed at the same price for Indonesia with '1,024 GB/month bandwidth' and for Kazakhstan with 2,048 GB/month
  - [3] 2026-11-07: the Lite order page's payment-options ladder reads 1 Month $6.99/month, 3 Months $6.64/month -5%, 6 Months $6.29/month -10%, 1 Year $5.94/month -15%; the configurator rendered with no out-of-stock notice, so the plan is in stock; no renewal price is printed on the order page | capture: sha256:d2e2f361064388036a47d150bd61a46072bfc317857810ba13edd6b2337de11b | quote: 1 Month $6.99/month ... 1 Year $5.94/month -15% Discount
  - [3] 2026-11-07: the Lite order page prices the four billing terms as per-month rates: the 1-month term is USD 6.99 and the 1-year term USD 5.94 per month | capture: sha256:d2e2f361064388036a47d150bd61a46072bfc317857810ba13edd6b2337de11b | quote: 1 Month $6.99/month ... 3 Months $6.64/month -5% Discount ... 6 Months $6.29/month -10% Discount ... 1 Year $5.94/month -15% Discount
  - [3] 2026-11-07: the order page's payment ladder prices Lite at $6.99/month for the 1-month term and $5.94/month for the 1-year term, and the configurator rendered with no out-of-stock notice | capture: sha256:d2e2f361064388036a47d150bd61a46072bfc317857810ba13edd6b2337de11b | quote: 1 Month $6.99/month ... 3 Months $6.64/month -5% Discount ... 6 Months $6.29/month -10% Discount ... 1 Year $5.94/month -15% Discount
  - [4] 2026-11-07: the /en/cart path answers the site's Not Found page, so there is no guest cart page to read | capture: sha256:dd7e0fe5f708cb25833cdf97edda068b703554cef87075758a454e1f5ad43c53 | quote: Not Found (404)
  - [3] 2026-11-07: the payment ladder is unchanged: 1 Month $6.99/month, 3 Months $6.64/month -5%, 6 Months $6.29/month -10%, 1 Year $5.94/month -15% | capture: sha256:d2e2f361064388036a47d150bd61a46072bfc317857810ba13edd6b2337de11b | quote: 1 Month $6.99/month ... 3 Months $6.64/month -5% Discount ... 6 Months $6.29/month -10% Discount ... 1 Year $5.94/month -15% Discount
  - [3] 2026-11-07: the 1-year term of the Lite plan prints a $71.30 total on its order page, matching the summary's Pay now figure | capture: sha256:05250a5f6d03c510369c1a37add41766a173ac36d99a5e33033393be99c926b8 | quote: Pay now:$71.30
  - [5] 2026-11-07: the order summary for the 1-year term charges $71.30 for the 2026-11-07 to 2027-11-06 period | capture: sha256:05250a5f6d03c510369c1a37add41766a173ac36d99a5e33033393be99c926b8 | quote: Pay now:$71.30
- sources:
  - [1] https://ishosting.com/en/vps
  - [2] https://vpspricetracker.com/provider/is_hosting/vps
  - [3] https://ishosting.com/en/vps/751_1y
  - [4] https://ishosting.com/en/cart
  - [5] https://ishosting.com/en/vps/751_1y?billing=annual&location=jp
