# IPXO

> ipxo.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipxo/ | JSON https://fshy.ajam.dev/api/v1/entity/ipxo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPXO

- `ip-proxy/ipxo-ipv4-leasing` | fails-identity | evidence documented | binding volume-quota | category prefix lease marketplace | tier IPv4 leasing (marketplace, from a /24)
- needs card yes, phone yes, ID no, institution yes | verified 2026-11-03T07:35:33.762Z (live) | stale on 2026-12-04
- url https://www.ipxo.com/ipv4-leasing/
- free tier: No free IPv4 lease. The platform subscription has a Free plan at $0 ('Try the platform - free forever'), but 'IPXO platform subscriptions and IPv4 leasing are priced separately.' The 3x3 campaign rate for leased space is $0.25 per IP per month on a minimum 3-year term; the platform's yearly average lease rate is $0.38 per IP per month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The Free subscription gives access to the platform's resource view and pay-as-you-go tokens; it carries no address space. A published per-subnet price list is not on the pages read: the pricing page says 'IPv4 leasing prices depend on the IP block size, lease term, and available inventory', and the search that shows each subnet's monthly price sits behind the portal sign-up.
- per-object cap: not applicable: an address block, not an object; the smallest block is a /24 (256 IPs) | source: [2] | note: The 3x3 campaign terms state 'Minimum block size: /24 (256 IPs). No subnet size limitations apply above the minimum.' No smaller block is offered under those terms.
- retention: not applicable: a leased block, not stored bytes; campaign terms are a 3-year minimum and 10-year maximum | source: [2] | note: Campaign billing is annual in advance, and early exit is not permitted: the remaining annual fees for the full term fall due. Terms shorter than 3 years are quoted by sales at a different rate.
- egress: not applicable: IPXO sells the right to announce an address block, not a carrier port. The lessee announces the block from its own ASN or through a cloud's bring-your-own-IP feature; traffic is billed by that network, not by IPXO. | metered: no | free allowance: not applicable: no traffic is carried by the vendor | source: [3]
- identity: institution | detail: A payment method (credit card, PayPal or wire transfer) is added after that. The terms describe a 'basic Know Your Customer (KYC) process'.
- interface: rest
- limits:
  - volume-quota (binding): smallest lease unit is a /24 (256 IPs): 'Minimum block size: /24 (256 IPs).' Campaign term minimum 3 years, maximum 10 years, billed annually in advance [2]
- limits note: The vocabulary has no kind for a minimum purchase size or a contract term; volume-quota is the nearest and is used for the /24 minimum. A second gate is not a limit at all: the account must be a legal entity acting in the course of business, and a leased block is announced from an ASN the lessee names. The $0.25 per IP per month rate applies only to the campaign's 3-year terms.
- binding note: The /24 minimum binds first on the price side: 256 addresses at the campaign rate, and a 3-year commitment, are the smallest purchase. Identity binds before any of it (legal entities only, with company confirmation by support), which is why the verdict is fails-identity; the limit vocabulary has no kind for that.
- interface detail: A web portal handles search, lease, LOA, ROA, WHOIS and rDNS ('Assign IPs immediately with automated LOA, ROA, and WHOIS updates.'); the site's navigation lists 'API Access: Automate IP search and leasing workflows'. The API's endpoints and authentication were not read.
- tooling: A BGP speaker, a cloud's bring-your-own-IP service or a hoster that announces the block for the lessee; IPXO issues the LOA and ROA and keeps WHOIS and rDNS in sync. The leasing page advertises 'Deploy IPXO-leased IPs across major platforms at lower cost.'
- composes with: A leased /24 is 256 addresses in one prefix, one registry object and one announcing AS, so for a rotating egress it is one rung-3 unit with 256 source addresses; the lease supplies address space and no machine. The registry class of a delivered IPXO block is unverified: a delivered block needs a confirmed company account, so no registry object of a leased block was read.
- reliability: unverified: no delivered block was inspected, because leasing needs a confirmed company account and a payment method; the registry object and usage class of a leased /24 are behind that sign-up.
- evidence note: Per-subnet prices, the API reference and the registry object of a delivered block are unverified: behind a company sign-up.
- extras:
  - role: marketplace between address holders and lessees; the lessee's blocks are sub-allocated from the holder's registry object
  - min_prefix: /24
  - price_per_address_month: USD 0.25 on the 3-year campaign; USD 0.38 is the vendor's platform average
  - price_derived: USD 0.25 x 256 = USD 64.00 per month for a /24 at the campaign rate; USD 3 x 256 = USD 768 per year; USD 0.38 x 256 = USD 97.28 per month at the stated average, all before VAT
  - registries: ARIN, RIPE NCC, AFRINIC (the campaign's list)
  - needs_own_asn: unverified: the portal asks for the ASN where the lease is announced; the page read states 'RPKI, ROA and WHOIS managed by IPXO' and a BYOIP route for each major cloud
  - rung: 3
  - rung_note: One /24 is one rung-3 unit; rung 5 is unverified until a delivered block's registry object is read.
- evidence:
  - [2] 2026-11-03: the smallest block IPXO leases under its campaign is a /24 of 256 addresses | capture: sha256:b5848e0aed9b86c98b8b46a4460a2cc6f87215cf1c82b190d339f0d71dac77cc | quote: Minimum block size: /24 (256 IPs). No subnet size limitations apply above the minimum.
  - [2] 2026-11-03: the campaign price per address is $3 per year, $0.25 per month, plus VAT | capture: sha256:b5848e0aed9b86c98b8b46a4460a2cc6f87215cf1c82b190d339f0d71dac77cc | quote: Campaign rate: $3 USD (plus VAT, if applicable) per IPv4 address per year ($0.25/month plus VAT, if applicable, effective rate).
  - [2] 2026-11-03: the campaign rate needs a 3-year minimum term | capture: sha256:b5848e0aed9b86c98b8b46a4460a2cc6f87215cf1c82b190d339f0d71dac77cc | quote: Minimum contract term: 3 years. Terms longer than 3 years are available at the same campaign rate.
  - [3] 2026-11-03: the vendor's stated platform average lease rate is $0.38 per IP per month, beside the campaign's $0.25 | capture: sha256:c52f8541d2b420df42e12a3c49dcfa370058b56a01d38bdfebc81fc3147165ac | quote: Average rate $0.38/mo per IP
  - [3] 2026-11-03: the campaign lists ARIN, RIPE NCC and AFRINIC as the registries of the leased space | capture: sha256:c52f8541d2b420df42e12a3c49dcfa370058b56a01d38bdfebc81fc3147165ac | quote: ARIN, RIPE NCC, AFRINIC RIRs
  - [3] 2026-11-03: leases are provisioned through the portal with automated LOA, ROA and WHOIS updates | capture: sha256:c52f8541d2b420df42e12a3c49dcfa370058b56a01d38bdfebc81fc3147165ac | quote: Assign IPs immediately with automated LOA, ROA, and WHOIS updates.
  - [3] 2026-11-03: leased blocks are brought to cloud platforms through bring-your-own-IP routes | capture: sha256:c52f8541d2b420df42e12a3c49dcfa370058b56a01d38bdfebc81fc3147165ac | quote: Deploy IPXO-leased IPs across major platforms at lower cost.
  - [1] 2026-11-03: the subscription plans (Free, Starter $100 a month) do not include address space; leases are billed on top | capture: sha256:876ec0e1d2205b982a83d50aed07c453f0c45177cdd19cc143d4adbe8de89a00 | quote: IPXO platform subscriptions and IPv4 leasing are priced separately.
  - [4] 2026-11-03: the platform lists an API for IP search and leasing workflows | capture: sha256:78ba7e43c5a6e9fbd8919e5aabe540f8c58910eaf236872e1fd72e377be51a2e | quote: API Access Automate IP search and leasing workflows
  - [5] 2026-11-03: an account needs a legal entity; an individual cannot register | capture: sha256:63b9613adf760b33df4fbeadd2063bd8cccc90422745c29c24d045c7bea6dc69 | quote: The Platform is intended solely for use by legal entities acting in the course of business.
  - [5] 2026-11-03: IPXO runs a KYC check on a user at registration | capture: sha256:63b9613adf760b33df4fbeadd2063bd8cccc90422745c29c24d045c7bea6dc69 | quote: We conduct a basic Know Your Customer (KYC) process to verify the identity of the Client and Access Data.
  - [5] 2026-11-03: payment methods are a credit card, PayPal or a wire transfer | capture: sha256:63b9613adf760b33df4fbeadd2063bd8cccc90422745c29c24d045c7bea6dc69 | quote: you may pay the Fees for the Services by utilizing any of the following payment methods: (a) by providing a valid credit card, (b) by using PayPal
  - [6] 2026-11-03: registration requires a verified phone number | capture: sha256:949aacfa7a0da8e9d2eb4552e1d156c0674d148c18c364f6f5f7a7127de8bab5 | quote: Afterward, you need to verify your phone number via a phone call or SMS.
  - [6] 2026-11-03: company, contact and billing information are required before the platform can be used | capture: sha256:949aacfa7a0da8e9d2eb4552e1d156c0674d148c18c364f6f5f7a7127de8bab5 | quote: Once you make your choice, fill in your Company Information, Contacts and Billing information. Everyone must provide this information before they can start using the platform.
  - [6] 2026-11-03: a support confirmation of the company gates the first lease | capture: sha256:949aacfa7a0da8e9d2eb4552e1d156c0674d148c18c364f6f5f7a7127de8bab5 | quote: When you finish your company’s registration, your company must be confirmed by IPXO’s Customer Support.
- sources:
  - [1] https://www.ipxo.com/pricing/
  - [2] https://www.ipxo.com/ipv4-annual-lease/terms/
  - [3] https://www.ipxo.com/ipv4-leasing/
  - [4] https://www.ipxo.com/
  - [5] https://www.ipxo.com/terms-of-service-version2_0/
  - [6] https://www.ipxo.com/kb/ipxo-platform/how-to-lease-ips-from-ipxo/
