# BERO HOST

> bero-host.de | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bero-host/ | JSON https://fshy.ajam.dev/api/v1/entity/bero-host.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BERO HOST (compute/bero-host)

- `compute/bero-host` | paid-only | evidence reported | binding volume-quota | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://bero-host.de/kvm-rootserver
- disagrees on verdict: `compute/bero-host` says paid-only, `compute/bero-host-ipv6-anniversary-xs` says dead
- free tier: EUR 39/year recurring for the EPYC Turin Anniversary S in Frankfurt, with coupon LET10 taking 10 percent off the first term only to EUR 35.10: 2 cores on an AMD EPYC Turin 9275F, 6 GB DDR5, 60 GB NVMe, 25 TB of traffic, 1 IPv4 and a /64 IPv6, annual billing only. Anniversary M is EUR 49/year for 4 cores, 12 GB and 120 GB; L is EUR 69 for 4 cores, 20 GB and 200 GB; XL is EUR 89 for 6 cores, 24 GB and 300 GB; XXL is EUR 129 for 8 cores, 32 GB and 300 GB. A separate Ryzen 9 9950X line runs from EUR 39/year for 2 cores, 6 GB and 60 GB to EUR 199/year for 6 cores, 24 GB and 200 GB, all with the same 25 TB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 25 TB a month included per package; no overage price and no post-allowance throttle stated | metered: yes | free allowance: 25 TB per month | source: [2]
- identity: email | detail: not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 25 TB a month on every anniversary package, which is the largest allowance among evaluated providers and still a counter rather than a port; 25 TB a month averages about 79 Mbit/s, so on the small plans the counter and the usual 1 Gbit port are close together. The post states the yearly prices are recurring and remain valid for renewals while the service stays active, and it states no overage term. [1]
- limits note: 25 TB a month on every anniversary package, which is the largest allowance among evaluated providers and still a counter rather than a port; 25 TB a month averages about 79 Mbit/s, so on the small plans the counter and the usual 1 Gbit port are close together. The post states the yearly prices are recurring and remain valid for renewals while the service stays active, and it states no overage term.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the vendor advertises its own web interface and automatic setup within 30 seconds; no API or CLI is documented on the pages read
- composes with: EUR 129 a year for 8 cores, 32 GB, 300 GB of NVMe and 25 TB a month is the lowest annual cost per gigabyte of RAM among evaluated providers and the only record that undercuts the Kimsufi dedicated box on RAM per euro while staying virtual; that makes it the candidate for the archive index and build work, with 25 TB a month the reason it is not also the mirror.
- reliability: no reliability event recorded
- notes: The anniversary packages exist only in the forum post: the vendor page the thread links to carries the older prepaid KVM line at 4.95 EUR to 44.95 EUR a month, so the promo line is not on the URL the provider itself gave. The thread also advertises an IPv6-only VPS series in its title.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 32
  - facets.shape.disk_gib: 300
- evidence:
  - [2] 2026-10-22: the offer thread, posted October 3, 2026, quoted from its table: 'Anniversary XXL | 8 Cores | 32 GB | 300 GB | 1 IPv4 | /64 IPv6 | 25 TB | EUR 129 | EUR 116.10 | approx EUR 9.68/mo'; 'The listed yearly prices are recurring prices' and 'They remain valid for renewals as long as the service stays active'; 'Location: Frankfurt, Germany', 'Traffic: 25 TB included per package'
  - [1] 2026-10-22: the vendor page redirects to /server/prepaid-kvm-rootserver-mieten and lists a different product line: 'KVM Paket 3k ... 1 Kern ... 3 GB ... 20 GB ... 4,95 EUR INKL. MWST.' through 'KVM Paket 48k ... 12 Kerne ... 48 GB ... 320 GB ... 44,95 EUR INKL. MWST.'; it carries no anniversary package and no 25 TB row
- sources:
  - [1] https://bero-host.de/kvm-rootserver
  - [2] https://lowendtalk.com/discussion/221713/bero-host-10th-anniversary-deals-epyc-turin-ryzen-9950x-ipv6-only-vps

## BERO HOST, Anniversary XS (IPv6-only)

- `compute/bero-host-ipv6-anniversary-xs` | dead | evidence documented | binding volume-quota | category IPv6-only VPS | tier Anniversary XS (IPv6-only)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:16:40.000Z (live) | stale on 2026-11-24
- url https://bero-host.de/server/prepaid-ipv6-rootserver-mieten
- disagrees on verdict: `compute/bero-host` says paid-only, `compute/bero-host-ipv6-anniversary-xs` says dead
- free tier: No free tier. The provider's forum post advertises an IPv6-only Anniversary XS at EUR 12 a year (EUR 10.80 with coupon LET10) for 1 core, 1 GB and 10 GB NVMe with 25 TB traffic. The vendor page the offer points at says the product is no longer available. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not applicable
- retention: the vendor's IPv6 line is prepaid and the page states 'Dieses Produkt ist nicht mehr verfügbar oder hat keine individuelle Konfiguration verfügbar.' ('This product is no longer available or has no individual configuration available.') | source: [2]
- egress: the forum post states 25 TB included per package on the IPv6-only line; the vendor page's own live line states 'Fair Use Traffic' with no figure | metered: yes | free allowance: 25 TB, per the offer post only | source: [1]
- identity: email | detail: a BERO HOST account with 'Registrierung' and 'Login' links; the form was not read. No card hold is stated. The vendor's billing is prepaid, which the page advertises as 'Keine versteckten Kosten oder Mahnungen'. | country: DE
- interface: ssh
- limits:
  - volume-quota (binding): 25 TB included per package, per the offer post [1]
- binding note: the offer is withdrawn before traffic matters: the vendor's own IPv6 page returns 'no longer available' for the configuration.
- interface detail: KVM root server with full root access, one-click reinstall and a KVM console, per the vendor page's feature list; the vendor states every server gets its own IPv6 network.
- tooling: any SSH client over IPv6
- composes with: would be the best traffic allowance in evaluated offerings at 25 TB, but the product is withdrawn, so it is a watch item rather than a row a buyer can take.
- reliability: no reliability event observed; the vendor advertises a 750 Gbit/s DDoS filter that 'filters all incoming packets during an attack'
- notes: The promotional offer is dated October 3 2026. The 25 TB monthly transfer provides a high bandwidth allowance for active nodes.
- evidence note: the withdrawal is quoted from the vendor's own page read; the price and the 25 TB are from the provider's own LowEndTalk offer post, which is first-party but not the shop. The two disagree, and the shop is the one that decides availability.
- evidence:
  - [2] 2026-10-24: quoted: 'PREPAID IPv6 Rootserver JETZT AB 3,50 € MIETEN ... Dieses Produkt ist nicht mehr verfügbar oder hat keine individuelle Konfiguration verfügbar.' - the page's own configuration block reports the product as unavailable
  - [2] 2026-10-24: quoted: 'Eigenes IPv6-Netz - Jeder Server besitzt ein eigenes IPv6-Netz.' and 'Fair Use Traffic - Nutze soviel Traffic wie dein Server benötigt.' and 'Unsere Server stehen in Frankfurt'
  - [1] 2026-10-24: quoted offer table row: 'Anniversary XS | 1 Core | 1 GB | 10 GB | 0 IPv4 | /64 IPv6 | 25 TB | €12 | €10.80 | €0.90/mo' under the heading 'IPv6-only EPYC Turin VPS ... Location: Frankfurt, Germany ... IPv4: Not included'
  - [3] 2026-10-24: the URL the offer post links to redirects to /server/prepaid-kvm-rootserver-mieten and carries only the dual-stack prepaid KVM line at 4,95 € to 14,95 € incl. VAT, each with 'IPv4: 1 Adresse' - the anniversary IPv6 packages are not on it
- sources:
  - [1] https://lowendtalk.com/discussion/221713/bero-host-10th-anniversary-deals-epyc-turin-ryzen-9950x-ipv6-only-vps
  - [2] https://bero-host.de/server/prepaid-ipv6-rootserver-mieten
  - [3] https://bero-host.de/kvm-rootserver
