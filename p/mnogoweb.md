# Mnogoweb

> mnogoweb.ru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mnogoweb/ | JSON https://fshy.ajam.dev/api/v1/entity/mnogoweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mnogoweb

- `compute/mnogoweb` | paid-only | evidence reported | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://mnogoweb.ru/vps.html
- free tier: RUB 190 per month from the vendor's own page title, which states that VPS/VDS servers start at RUB 190 with hourly billing. The plan table itself is a JavaScript calculator that renders only a loading placeholder to a text extractor, so the shape comes from the index row: 5 GB NVMe, 1 GB RAM, 1 core at 2.3 GHz, 0.2 TB traffic on a 50 Mbit/s port, Moscow or Novosibirsk. The page states three plan lines (budget, standard, storage) and a 50 Mbit/s ceiling on the budget line against up to 250 Mbit/s on the other two. | unit: GiB | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no byte allowance stated on the page read; the budget line is capped at 50 Mbit/s, the other two at 250 Mbit/s | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits:
  - per-ip-shaping (binding): The budget line is capped at 50 Mbit/s and the page states no byte allowance, so throughput is the wall on the cheap plan; the index row's 0.2 TB is a rendering of the same 50 Mbit/s port, not a separate meter. [1]
- limits note: The budget line is capped at 50 Mbit/s and the page states no byte allowance, so throughput is the wall on the cheap plan; the index row's 0.2 TB is a rendering of the same 50 Mbit/s port, not a separate meter.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: browser control panel with VNC, ISO mount, firewall rules and resource resize; no API documented on the page read
- composes with: RUB 190 with hourly billing and a Moscow and a Novosibirsk location is the cheapest hourly Russian box among evaluated providers, which makes it a candidate for short-lived jobs that must egress from inside Russia.
- reliability: no reliability event recorded
- notes: Source: vps.today index row, then the vendor page. The price is the vendor's own floor statement, not a plan row. verification criteria: the calculator's cheapest rendered configuration and its per-hour rate. Rendering and provenance: currency written as RUB.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 5
- evidence:
  - [1] 2026-10-23: page title quoted: 'VPS/VDS серверы от 190 ₽ с почасовой оплатой'; plan area renders 'Loading... 'Калькулятор загружается...'; comparison table states 'Максимальная скорость сети | 50 Мбит/с | До 250 Мбит/с | До 250 Мбит/с' for the three plan lines; locations listed: Москва, Новосибирск, Казахстан, Нидерланды, Финляндия, США
  - [2] 2026-10-23: index row quoted: 'Mnogoweb | 5 GB NVMe | 1 GB | 1 x 2.3 GHz | 0.2 TB 50 Mbit/s | Россия (Москва, Новосибирск) KVM IPv6 DDoS ПО ! | 190 руб.'
- sources:
  - [1] https://mnogoweb.ru/vps.html
  - [2] https://vps.today/
