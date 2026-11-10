# DigitalPlat FreeDomain

> github.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-digitalplatdev/ | JSON https://fshy.ajam.dev/api/v1/entity/github-digitalplatdev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DigitalPlat FreeDomain

- `domains-dns/digitalplat-freedomain` | qualifies-with-caveat | evidence documented | binding per-object-cap | category free registrable subdomain
- identity a placeholder: card and phone unknown | verified 2026-11-03T16:43:10.325Z (live) | stale on 2026-12-04
- url https://github.com/DigitalPlatDev/FreeDomain
- free tier: free registration under the suffixes .DPDNS.ORG, .US.KG, .QZZ.IO, .XX.KG and .QD.JE, with the user's own authoritative nameservers entered in the dashboard; the default limit is 1 domain per user account | unit: objects | metered on: object-count | read on: 2026-11-03 | source: [1]
- per-object cap: 1 domain per user account by default; sub-subdomains under the assigned name are made at the user's DNS provider
- retention: the dashboard is the source of truth for status and expiration date; renewal windows, fees and slot rules are not stated on the pages read and are said to change | source: [2]
- egress: no query cap published; the service holds no zone, so queries go to the user's chosen DNS provider | metered: no | source: [3]
- identity: any-phone | detail: the account tutorial's preparation list names an email address, a name, a valid phone number in the format the form requests and a complete contact address; the dashboard registration form itself was not read: unverified whether the phone is checked by a code
- interface: unknown
- limits:
  - per-object-cap (binding): the default limit is 1 domain per user account [4]
  - write-gated: supported suffixes, registration pauses, slot requirements, prices and limits change, and a registration may consume a slot or create a charge; a third-party report says .US.KG and .XX.KG paused new registrations and .QZZ.IO went paid-only, while the repository still lists them [5]
- binding note: 1 domain per account is the stated cap, and the operator reserves registration pauses and slot or charge requirements per suffix; the zone is the registrant's through delegation, and the suffix listing keeps the TLS limit per name
- interface detail: a web dashboard at dash.domain.digitalplat.org that needs an account (unverified: behind a sign-up); the tutorial has an API chapter whose content was not read. The service stores only the delegation: A, CNAME, MX and TXT records are managed at the external DNS service the nameservers name
- tooling: the DigitalPlat dashboard, then an external authoritative DNS service of the user's choice
- composes with: the delegation can point at an external DNS service such as Cloudflare, which makes the name a zone of the registrant's; the suffix is on the Public Suffix List
- reliability: the operator can pause a suffix, change slots or charges, or suspend a domain, and a third party reports two suffixes paused and one gone paid-only
- notes: The zone is the registrant's: the service stores only NS delegation, so a Cloudflare zone or any DNS host can serve it. The operator can still withdraw it, because a suffix can be paused, put behind a slot or charge, or a domain suspended. The TLS limit does not bind, because the suffixes are listed and each name counts alone. The dashboard is behind a login wall, so the live slot and renewal rules are unverified.
- evidence note: the repository README, FAQ and tutorial pages were read and quoted; the dashboard answered a login wall, so the live registration form, the current slot rule and the renewal terms are unverified; the suffix status report is third-party
- evidence:
  - [1] 2026-11-03: registration with the user's own DNS provider through custom nameservers | capture: sha256:111644cb4781c958c38c55fca44de7e0fb0671795481cf22ca2660e7f4ad0eff | quote: Register a domain, connect your preferred DNS provider through custom nameservers, and use the included learning guide to take a project from registration to deployment.
  - [4] 2026-11-03: the default limit is 1 domain per user account | capture: sha256:a0e627bbd217dc00ff6fead6fb55999dc1d770fc689eba9e3d83d64c4cf9af6b | quote: Currently, the default limit is 1 domain per user account.
  - [4] 2026-11-03: sub-subdomains are made at the user's DNS provider under the assigned name | capture: sha256:a0e627bbd217dc00ff6fead6fb55999dc1d770fc689eba9e3d83d64c4cf9af6b | quote: You can still create subdomains under your assigned domain via your DNS provider (e.g., `example.foo.us.kg`).
  - [3] 2026-11-03: the service holds only the delegation and has no ordinary record editor | capture: sha256:59278d75277ccb0ff4dfbb524f80d00656c2b33b1c9cf95185e7d887808718b2 | quote: It does not provide an ordinary DNS record editor.
  - [6] 2026-11-03: the account needs a valid phone number among its contact data | capture: sha256:369e86edfa863c9dd8e1278b58ffb6ef3f520841aeed21ad6920195ff5ba9d14 | quote: A valid phone number in the format requested by the form
  - [5] 2026-11-03: a registration may consume a slot or create a charge | capture: sha256:8be93869284b31dac69c9a569eaa1919ef8ff37f2f3cae528e0ca8f9c0639d95 | quote: Registration can create external state and may consume a slot or create a charge.
  - [5] 2026-11-03: suffixes, pauses, slot requirements, prices and limits are changeable at the operator's notice board | capture: sha256:8be93869284b31dac69c9a569eaa1919ef8ff37f2f3cae528e0ca8f9c0639d95 | quote: Supported suffixes, registration pauses, slot requirements, prices, limits, renewal windows, and policies may change.
  - [2] 2026-11-03: a domain can expire or be suspended at the registration level | capture: sha256:ef0731021c4661e4ca9efdfcacd013bbc5899fc49a9f3054ce632fb70537ff23 | quote: If the domain expires or becomes suspended, read the official status and instructions.
  - [7] 2026-11-03: the operator offers free registration under qzz.io, dpdns.org, us.kg and xx.kg | capture: sha256:e5975e5d5137eb988e8de0ddc3c212d0681040f6cc6bc452c931963ff95363a0 | quote: offering free registration and administration to individuals and communities worldwide.
  - [8] 2026-11-03: a third-party post reports .qzz.io moved to paid-only | capture: sha256:702de298864f02abf26b210e95279380ff31271f7f822d7e25b5a963016bf6a1 | quote: `.qzz.io`**, also run under the DigitalPlat umbrella, moved to paid-only.
  - [9] 2026-11-03: DigitalPlat's suffixes (qzz.io, us.kg, xx.kg, dpdns.org) are entries of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // DigitalPlat : https://www.digitalplat.org/
  - [10] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
- sources:
  - [1] https://github.com/DigitalPlatDev/FreeDomain
  - [2] https://github.com/DigitalPlatDev/FreeDomain/blob/main/documents/tutorial/platform/1.4-status-and-renewal.md
  - [3] https://github.com/DigitalPlatDev/FreeDomain/blob/main/documents/tutorial/index.md
  - [4] https://github.com/DigitalPlatDev/FreeDomain/blob/main/documents/domains/faq.md
  - [5] https://github.com/DigitalPlatDev/FreeDomain/blob/main/documents/tutorial/platform/1.2-domain-registration.md
  - [6] https://github.com/DigitalPlatDev/FreeDomain/blob/main/documents/tutorial/platform/1.1-account-registration.md
  - [7] https://nic.us.kg/
  - [8] https://dev.to/mattleeee/free-domain-options-in-2026-from-euorg-to-digitalplat-dpdnsorg-3k3o
  - [9] https://publicsuffix.org/list/public_suffix_list.dat
  - [10] https://letsencrypt.org/docs/rate-limits/
