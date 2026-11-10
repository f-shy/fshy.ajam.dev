# ElypseCloud

> elypsecloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/elypsecloud/ | JSON https://fshy.ajam.dev/api/v1/entity/elypsecloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ElypseCloud

- `compute/elypsecloud-free` | dead | evidence documented | binding write-gated | category VPS | tier FREE
- needs card unknown, phone unknown, ID no, institution no | verified 2026-10-24T04:12:03.000Z (live) | stale on 2026-11-24
- url https://elypsecloud.com/vps-linux-gratuit
- free tier: 'CPU: 2 x E5-2697v4', 'RAM: 4 GB DDR4', 'Espace disque: 50 GB', 'Bande Passante 1 Gbit/s', 'Localisation France', 'GRATUIT'. The order button points at a store product at manager.elypsecloud.com/store/vps-linux/vps-linux-free. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not published on the page read
- retention: not published: the free-VPS page states no term, no renewal and no expiry. Whether the machine is permanent or a first-term offer is not established.
- egress: 'Bande Passante 1 Gbit/s' (a port speed, not a volume). No monthly traffic allowance is stated. | metered: no | source: [1]
- identity: email | detail: not established: the order path stops at an out-of-stock product, so the registration form was never reached and no page read states whether a card or phone is asked for
- interface: ssh, rest
- limits:
  - volume-quota: 4 GB RAM, 50 GB disk, 1 Gbit/s port as stated [1]
  - write-gated (binding): the free product is out of stock; ordering is suspended until stock returns [2]
- binding note: The store refuses the order before any resource question arises: the free product page returns 'Rupture de stock' and states the item 'a donc été suspendu jusqu'à ce que de nouveaux stocks soient disponibles'.
- interface detail: a Linux VPS with a choice of Debian 11, 12 or 13 at order time, in a French datacentre, managed from a WHMCS-style customer manager
- tooling: any SSH client once provisioned
- composes with: Nothing, until the product can be ordered: the free product is out of stock at the store and the offer is unorderable today.
- reliability: No reliability event observed. The seller is identifiable: 'ELYPSEGROUP SAS · RCS Bordeaux 978 470 680' appears in the footer of its own terms PDF, version dated 15 September 2026.
- notes: Reopening criteria: product stock availability in store.
- evidence note: The advertised shape and the out-of-stock refusal are both read from the vendor's own pages, so the row is documented about the offer and about the block. Everything about delivery is unestablished because the order cannot be placed.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 4
  - shape.disk_gib: 50
  - billing_model: free
  - term: not published
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: EUR 0.00 advertised for the free product; it is out of stock, so no billable shape exists to price
  - free_tier_kind: closed
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: not published
  - session_cap.restart_required: no
  - session_cap.note: not established; nothing was provisioned
- evidence:
  - [1] 2026-10-24: quoted: 'FREE', 'CPU: 2 x E5-2697v4', 'RAM: 4 GB DDR4', 'Espace disque: 50 GB', 'Bande Passante 1 Gbit/s', 'Localisation France', 'GRATUIT'; order link 'Commander' to the store product
  - [2] 2026-10-24: quoted: 'Rupture de stock - Cet article est actuellement en rupture de stock et a donc été suspendu jusqu'à ce que de nouveaux stocks soient disponibles.'
  - [3] 2026-10-24: quoted: 'ELYPSEGROUP SAS · RCS Bordeaux 978 470 680 · Version du 15 septembre 2026'; 'ElypseGroup SAS, exerçant sous le nom commercial ElypseCloud'
  - [4] 2026-10-24: quoted: 'Serveurs VPS, hébergement web et serveurs dédiés', 'hébergés en France', 'À partir de 0,99 €/mois'
- sources:
  - [1] https://elypsecloud.com/vps-linux-gratuit
  - [2] https://manager.elypsecloud.com/store/vps-linux/vps-linux-free
  - [3] https://elypsecloud.com/cgu
  - [4] https://elypsecloud.com/
