# Opus Host

> opus-host.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opus-host/ | JSON https://fshy.ajam.dev/api/v1/entity/opus-host.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Opus Host

- `compute/opus-host-free` | qualifies-with-caveat | evidence documented | binding write-gated | category VPS | tier Free Server
- needs card no, phone no, ID no, institution no | verified 2026-11-09T13:14:20.502Z (live) | stale on 2026-12-10
- url https://opus-host.de/server
- free tier: '1 vCPU, 1 GB RAM und 20 GB SSD - kostenlos nach Admin-Freigabe' and '0,00 € dauerhaft kostenlos'. The page's own plan object gives cores 1, memory_mb 1024, disk_gb 20, ipv4 1, ipv6 1, runtime_days 30, price_cents 0, is_free true, is_free_unique 1. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: one free server per account: the plan object carries 'is_free_unique': 1
- retention: The plan object carries 'runtime_days': 30, which the free-server page does not explain. The FAQ says the free package is 'dauerhaft kostenlos' and the pricing phase note says free KVM servers are released 'sofort nach kurzer Prüfung'. Whether the 30 days are a renewal cycle or a hard term is not stated on any page read, so the persistence of the machine past day 30 is unverified.
- egress: not published: neither the free-server page, the FAQ, the terms nor the plan object states a traffic allowance or a port speed for the free plan | metered: no | source: [2]
- identity: email | detail: no card and no payment data: the FAQ states the free package 'erfordert keine Zahlungsdaten'. The registration form asks full name (explicitly 'Bitte keinen Nickname verwenden'), optional company, street and number, postcode, city, two-letter country, email and password. No phone, no document, no card field.
- interface: ssh, rest
- limits:
  - volume-quota: one free server per account (is_free_unique 1) [1]
  - retention-clamped: runtime_days 30 on the free plan, unexplained [1]
  - write-gated (binding): manual administrator approval before the server is released [2]
- binding note: Every application passes a human administrator before any machine exists, so the first thing that can fail is the approval, not the machine.
- interface detail: KVM virtualisation with root, a browser console ('Konsole im Browser'), a customer portal at /dashboard and a support ticket system; the plan object sets 'hosting_provider': 'proxmox' and 'provider_mode': 'live'
- tooling: any SSH client; the vendor's web portal
- composes with: A real KVM guest with root and one IPv4 plus one IPv6 on a German host, which is the shape a WireGuard node or a cron-driven health monitor needs without a card on file.
- reliability: unverified: the server page answered with a deployment pause screen on 2026-11-09, so neither the free plan nor any traffic term is readable; the host that serves it reports a paused deployment rather than a plan page; on 2026-10-24 the vendor status page reported 99.99 percent 90-day uptime for infrastructure and 100 percent for the remaining components
- notes: The strongest niche find of this category: a real KVM guest with root, one IPv4 and one IPv6, no card, from a named German sole trader with an imprint, a phone number, a GitHub organisation and a status page. Two things are unresolved. First, runtime_days 30 on the free plan is not explained anywhere read, and it is the difference between a permanent machine and a one-month one; the fix is one approved account watched past day 30, which this category cannot do because it must not register. Second, the FAQ says 10 GB NVMe where the plan page says 20 GB SSD. Neither the egress allowance nor a port speed is published at all. The docs subdomain returned HTTP 530 on both read and fetch, and the browser navigation to it killed the page process, so the documentation route is unread rather than absent.
- evidence note: Shape, price and the absence of payment data are quoted from the vendor's own free-server page, FAQ and plan JSON read. Egress, the meaning of runtime_days and whether the machine is actually released are not established by any page read, so the row is documented about what is offered and unverified about what is delivered.
- extras:
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 20
  - billing_model: free
  - term: unstated; the plan object carries runtime_days 30
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: EUR 0.00 on the plan page, '0,00 € dauerhaft kostenlos'; no charge and no card, so there is no rate to multiply
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: not published; the plan object allocates ipv4 1 and ipv6 1
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: no idle reclaim or login clock published; the unexplained runtime_days 30 is the only timer on the record
  - payment_methods: none required for the free plan; the privacy page lists PayPal, Stripe, Sofortüberweisung and Kreditkarte for paid orders
- evidence:
  - [1] 2026-10-24: quoted: '1 vCPU, 1 GB RAM und 20 GB SSD - kostenlos nach Admin-Freigabe'; '0,00 € dauerhaft kostenlos'; feature list 'KVM-Virtualisierung', 'Konsole im Browser', 'Nach kurzer Admin-Prüfung'
  - [1] 2026-10-24: page source plan object, quoted: {"slug":"free","name":"Free Server","cores":1,"memory_mb":1024,"disk_gb":20,"ipv4":1,"ipv6":1,"runtime_days":30,"price_cents":0,"is_free":true,"is_free_unique":1,"provider_configured":true}, and 'hosting_provider':'proxmox', 'provider_mode':'live', 'catalog_available':true
  - [2] 2026-10-24: quoted: 'Unser Free-Server-Paket (1 vCPU, 1 GB RAM, 10 GB NVMe SSD) ist dauerhaft kostenlos und erfordert keine Zahlungsdaten.' Note the FAQ states 10 GB NVMe where the plan page states 20 GB SSD; the disagreement is recorded, not resolved
  - [3] 2026-10-24: registration fields read in a browser: 'Vollständiger Vor- und Nachname', 'Unternehmen (optional)', 'Straße und Hausnummer', 'Postleitzahl', 'Ort', 'Land', 'E-Mail-Adresse', 'Passwort'. No card, no phone, no document
  - [4] 2026-10-24: the imprint gives a postal address in Lahr, Germany, and a named representative; 'Zuständige Aufsichtsbehörde: LfDI Baden-Württemberg'. A named sole trader with a German address, not an anonymous reseller
  - [5] 2026-10-24: quoted: 'Infrastructur 99.99% Operational', 'Webservices 100.00% Operational', '90-day uptime'
  - [6] 2026-10-24: 5 reviews, 4.6 of 5, all five inside the last 12 months; two are marked 'Verifizierte Bewertung' and describe a bot running 'seit ein paar tagen' without interruption. Third-party and thin, so reported only
  - [1] 2026-11-09: the page answered with a deployment pause placeholder, which is the finding | capture: sha256:6a5f50c9530fc1ea60ccb91949ffcd57b27fd084f2eb61c6fef6452fa88ff955 | quote: This deployment is temporarily paused
  - [1] 2026-11-09: the page answers with a deployment pause placeholder instead of the server list, so the offer could not be read | capture: sha256:0554e8a6de39721cd16b0f11e104886d65c09539e3b9ac55d5c8801f592cbb40 | quote: This deployment is temporarily paused
- sources:
  - [1] https://opus-host.de/server
  - [2] https://opus-host.de/faq
  - [3] https://opus-host.de/register
  - [4] https://opus-host.de/legal/imprint
  - [5] https://status.opus-host.de/en
  - [6] https://erfahrungen.app/erfahrung/opus-host.de
