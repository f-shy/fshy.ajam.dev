# InterLIR

> interlir.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/interlir/ | JSON https://fshy.ajam.dev/api/v1/entity/interlir.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InterLIR

- `ip-proxy/interlir-ipv4-rent` | fails-identity | evidence documented | binding volume-quota | category prefix lease marketplace | tier IP Rent (from a /24)
- needs card no, phone no, ID no, institution yes | verified 2026-11-03T07:35:33.762Z (live) | stale on 2026-12-04
- url https://interlir.com/
- free tier: No free tier. Rent is listed 'from 110 euro monthly for /24', and in a second place as 'IP Rent from €99 per /24 network'; the 'Our main services' block says 'IPv4 Leasing ... Price: from 100 EUR / month'. The only free line on the page is the IPv4 reputation check ('Price: free'). | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The three 'from' prices sit on one page and do not agree: EUR 99 per /24 (the table does not say per month), EUR 110 monthly for a /24, and EUR 100 per month. A marketplace page states that 'the owners of the ips set prices themselves and can change them when they want within one click', so the listed figures are floors that depend on which block is in stock; the live price list is behind the portal login.
- per-object cap: not applicable: an address block, not an object; the smallest block is a /24 | source: [1] | note: Every rent price on the page is per /24 network, and the stock line for purchases reads 'Available stock of networks (/24-/16)'. No smaller prefix is offered.
- retention: not applicable: a leased block, not stored bytes | source: [1] | note: The page names no minimum term or notice period for a rent; 'you pay on a monthly basis' and 'We receive payment upon the initial order' are the billing statements. unverified: the minimum term, behind the portal.
- egress: not applicable: InterLIR leases address space and rewrites registry and rDNS data; it does not carry traffic. The lessee announces the block itself or through a hoster. | metered: no | free allowance: not applicable: no traffic is carried by the vendor | source: [1]
- identity: institution | detail: The sign-up block reads 'Register a company account' and 'Register a personal account and provide company documents for "Know You Customer" verification.' Payment is by 'cards, bank transfers, or cryptocurrencies(soon)'. The portal's own forms were not readable (login wall), so the exact fields are unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota (binding): smallest rent unit is a /24: 'IP Rent from €99 per /24 network'; no smaller prefix is priced on the page [1]
- limits note: The limit vocabulary has no kind for a minimum block size; volume-quota is the nearest. The prices on the page are 'from' floors that disagree across three places, and the owner of each block sets its own price, so the per-address figure below is a floor and not a quote.
- binding note: The /24 minimum binds on the size side, and a company KYC binds before any order; the vocabulary has no kind for that second gate, so the verdict records it as fails-identity.
- interface detail: A web portal at portal.interlir.com; the home page lists 'automated LOA Assignment' and the rent page says the platform 'updates the necessary network parameters and RIR databases'. The portal answers a login wall, so no API or CLI was found; no public API reference was read.
- tooling: A browser session on the portal for ordering, and the lessee's own BGP session or a hoster that announces the block; the vendor supplies the LOA and the registry-object changes.
- composes with: A rented /24 is 256 addresses in one prefix and one registry object, so it is one rung-3 unit, and the block's registrant and announcing AS are the lessee's own choices. The registry class of a delivered InterLIR block is unverified: the portal needs a company KYC, so no block was delivered and no registry object was read.
- reliability: unverified: the portal and its price list are behind a login wall, and no delivered block was inspected. The page claims 'We only provide networks from real network owners' and 'Registred broker in RIPE NCC, ARIN, LACNIC, APNIC'; neither was checked against a registry object.
- evidence note: Documented from the vendor's home page and rent page captured 2026-11-03. The three listed prices disagree with each other, the portal is unreadable, and no block was delivered.
- extras:
  - role: marketplace between block owners and renters; the vendor states it is a registered broker at four registries
  - min_prefix: /24
  - price_per_address_month: EUR 0.39 to EUR 0.43 per address per month at the listed floors (EUR 99 and EUR 110 per /24); the EUR 99 figure has no period stated
  - price_derived: EUR 99 / 256 = EUR 0.387 per address; EUR 110 / 256 = EUR 0.430 per address; EUR 100 / 256 = EUR 0.391 per address
  - registries: RIPE NCC, ARIN, LACNIC, APNIC (brokerage registrations the vendor states); the registry of a given leased block is chosen per block
  - rung: 3
  - rung_note: One /24 is one rung-3 unit; rung 5 is unverified until a delivered block's registry object is read.
- evidence:
  - [1] 2026-11-03: rent is listed from EUR 110 monthly for a /24 | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: Get Flexible and transparent pricing (from 110 euro monthly for /24 )
  - [1] 2026-11-03: the pricing table lists rent from EUR 99 per /24 network, with no period stated | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: | IPv4 Address Sales and Leasing Services | IP Rent from €99 per /24 network | IP Lease out from €99 per /24 network | IP Buy from €15 per IP | IP Sell from €20 per IP |
  - [1] 2026-11-03: the services block lists IPv4 leasing from EUR 100 a month | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: Price: from 100 EUR / month
  - [1] 2026-11-03: the vendor states it is a registered broker at RIPE NCC, ARIN, LACNIC and APNIC | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: Registred broker in RIPE NCC, ARIN, LACNIC, APNIC
  - [1] 2026-11-03: the stock the page lists runs from /24 to /16, with /24 the smallest | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: Available stock of networks (/24-/16)
  - [1] 2026-11-03: an account needs company documents for a KYC verification | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: Register a personal account and provide company documents for "Know You Customer" verification.
  - [1] 2026-11-03: payment is by card or bank transfer; cryptocurrency is listed as coming soon | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: You can pay with cards, bank transfers, or cryptocurrencies(soon)
  - [1] 2026-11-03: delivery is claimed within 24 hours of a request | capture: sha256:c65db8e2f86dd1cf160633fd1a86ce76322c5ce87b22e084c34029039d2d94d3 | quote: Your network will be served in less than 24 hours after a request.
  - [2] 2026-11-03: per-block prices are set by each block's owner, so the listed 'from' prices are floors | capture: sha256:3ed26fd53c4758787d9d80866d8be316cecf3e2a4c242ba478b93409969b81df | quote: the owners of the ips set prices themselves and can change them when they want within one click
- sources:
  - [1] https://interlir.com/
  - [2] https://interlir.com/rent-ip/
