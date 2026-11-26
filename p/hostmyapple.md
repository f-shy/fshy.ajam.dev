# HostMyApple

> hostmyapple.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostmyapple/ | JSON https://fshy.ajam.dev/api/v1/entity/hostmyapple.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostMyApple

- `compute/hostmyapple` | paid-only | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:50.016Z (live) | stale on 2026-12-26
- url https://hostmyapple.com/mac-vps-hosting
- free tier: no free tier: macOS packages from $24.99 a month with 3 GB of RAM and 60 GB of SSD, up to $54.99 for 6 GB and 100 GB | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $24.99 to $54.99 a month depending on RAM and disk [1]
  - per-ip-shaping: 'Unlimited Bandwidth' and 'No data caps' - a claim about a missing limit, recorded as such and not converted into a capacity figure [1]
- limits note: Session cap, idle-reap and network policy are not documented. Ranked partial.
- interface detail: The Mac VPS page lists a dedicated IP address with Remote Desktop, SSH and full Administrator access; no API is published
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the Mac VPS page was read on 2026-10-22 and prices four monthly packages. There is no free tier; the record's free-tier claim is contradicted
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.ram: 3
  - shape.disk: 60
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: the Lite package at 3 GB of RAM and 60 GB of SSD; the Max package is 6 GB and 100 GB
  - session_cap.restart_required: no
  - session_cap.note: a monthly rental of an Apple Silicon VM; no session clock
  - free_tier_kind: none
  - granularity.min_billed_s: 2592000
  - ps.gib: 60
  - ps.price: included in the monthly price
  - ps.durability: SSD
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.allowance: 'Unlimited Bandwidth', a documented absence rather than a number
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$24.99/mo Instant Activation', '60GB SSD Disk Space', 'Unlimited Bandwidth', and 'No data caps or fees, 100% Unlimited Usage', quoted across the four macOS packages
  - [1] 2026-11-25: the macOS packages are paid, from USD 24.99 a month for the Lite package with 3072MB RAM and 60GB SSD to the Max package with 6144mb RAM and 100GB SSD | capture: sha256:9ab2599c0a65a78bba7a1f38bb7b9c39b1b92cbdd4300c5555d7f878af33137b | quote: $24.99/mo Instant Activation :) ... The macOS Tahoe Lite package with 3072MB of RAM and 60GB of Solid State Drive space is the perfect solution for iMessage use, small website and light desktop use. ... The macOS Tahoe Max package features 6144mb of RAM and 100GB of Solid State Drive space.
  - [1] 2026-11-24: the macOS VPS packages still start at $24.99/mo, with unlimited bandwidth and no data caps | capture: sha256:9ab2599c0a65a78bba7a1f38bb7b9c39b1b92cbdd4300c5555d7f878af33137b | quote: $24.99/mo Instant Activation :)
  - [1] 2026-11-24: the page still advertises unlimited bandwidth with no data caps or fees | capture: sha256:9ab2599c0a65a78bba7a1f38bb7b9c39b1b92cbdd4300c5555d7f878af33137b | quote: No data caps or fees, 100% Unlimited Usage
  - [1] 2026-11-24: access is by Remote Desktop and SSH with full admin rights on a dedicated IP | capture: sha256:9ab2599c0a65a78bba7a1f38bb7b9c39b1b92cbdd4300c5555d7f878af33137b | quote: All Mac VPS cloud servers come with a dedicated IP address with Remote Desktop, SSH and full Administrator access.
- sources:
  - [1] https://hostmyapple.com/mac-vps-hosting
