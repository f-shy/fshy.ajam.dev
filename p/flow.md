# Flow Swiss Mac Bare Metal

> flow.swiss | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flow/ | JSON https://fshy.ajam.dev/api/v1/entity/flow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Flow Swiss Mac Bare Metal

- `compute/flow-swiss-mac` | paid-only | evidence documented | binding retention-clamped | category macOS host
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T15:03:49.561Z (live) | stale on 2026-12-26
- url https://doc.flow.swiss/platform/pricing/mac-bare-metal
- free tier: no free tier: Mac hardware from CHF 0.27 an hour or CHF 199 a month, with a 24-hour minimum allocation and billing while the device is stopped | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: 20 TB of outbound traffic per month is included per organization-account; inbound and internal traffic is always free. Each device has a free elastic public IPv4 address. | metered: yes | free allowance: 20 TB of outbound traffic per month | source: [1]
- identity: any-phone | detail: The registration page asks for 'First Name', 'Last Name' and 'Email'. The signup docs state 'we block all disposable email domains, including free providers like google, yahoo, etc.' and 'we also perform an SMS verification. For this a working mobile number is required.'
- interface: ssh
- limits:
  - retention-clamped (binding):  [1]
  - request-rate: CHF 0.27 an hour or CHF 199 a month [1]
  - per-ip-shaping: 20 TB of outbound traffic a month is included; inbound and internal traffic is free [1]
- interface detail: SSH on port 22 and VNC on port 5900 from the outside, with the ports configurable in security groups; the device is created in the Control Panel at my.flow.swiss.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the Mac bare-metal pricing page was read on 2026-10-22 and states the hourly rate, the 24-hour minimum, that a stopped device still bills, and the 20 TB egress allowance. The record's USD 24 credit is not on the page
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: Mac mini and Mac Studio on demand, with instant activation
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: a 24-hour minimum allocation forced by Apple's licence, and a stopped device still bills, so stopping is not a pause
  - free_tier_kind: none
  - granularity.min_billed_s: 86400
  - ps.price: SSD priced as a separate line
  - ps.durability: SSD on the device
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the allocation
  - net.out: yes
  - net.in: yes
  - net.ports: a free elastic public IPv4 per device
  - net.static_ip: yes
  - net.allowance: 20 TB a month outbound per organisation account
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Billing is per hour with a 24-hour minimum allocation period to comply with the Apple macOS License Agreement. Billing also takes place when the device is' stopped, 'Starting at CHF 0.27/hr or CHF 199/mo', 'Each Mac device comes with a free elastic public IPv4 address' and '20 TB of outbound traffic per month is included', quoted
  - [1] 2026-11-25: the page states the hourly and monthly starting prices, the 24-hour minimum allocation and billing while the device is switched off, with no free tier | capture: sha256:e6fb43d28343c9279047a08bb10c84b48943dbdaea316e75eaf3f15c1e247cd0 | quote: Mac mini and Mac Studio devices are available on-demand with instant activation. Billing is per hour with a 24-hour minimum allocation period to comply with the Apple macOS License Agreement. Billing also takes place when the device is switched off. ... Starting at CHF 0.27/hr or CHF 199/mo
  - [2] 2026-11-24: registration requires a mobile number in addition to an email | capture: sha256:2bc0bf8ff4a852f2f1a650a35b22a880c92f5afdf0a16daf647a2554cdcf86bb | quote: As an additional safeguard of the registration process, we also perform an SMS verification. For this a working mobile number is required.
  - [3] 2026-11-24: the exposed ports are configurable in the Control Panel | capture: sha256:bae54b9c545357f5dede9170a85806a91fbde4832a492635ed82aeb383e9b929 | quote: The port settings can be restricted or extended in the Control Panel via Mac Bare Metal > Networking > Security Groups > Default.
  - [1] 2026-11-24: an outbound allowance of 20 TB a month is published | capture: sha256:bdaf4dbcc8092406be6fb9860a7a2be6b6f8efb21f6a0c1dceaa1278586f55ea | quote: 20 TB Outbound Traffic. Per organization-account 20 TB of outbound traffic per month is included. Inbound and internal traffic is always free.
  - [1] 2026-11-24: the free egress allowance is 20 TB a month | capture: sha256:bdaf4dbcc8092406be6fb9860a7a2be6b6f8efb21f6a0c1dceaa1278586f55ea | quote: Per organization-account 20 TB of outbound traffic per month is included.
  - [1] 2026-11-24: the hourly rate, 24-hour minimum and billed-while-stopped rule are unchanged | capture: sha256:bdaf4dbcc8092406be6fb9860a7a2be6b6f8efb21f6a0c1dceaa1278586f55ea | quote: Billing is per hour with a 24-hour minimum allocation period to comply with the Apple macOS License Agreement. Billing also takes place when the device is switched off.
  - [4] 2026-11-24: the device exposes SSH on port 22 and VNC on port 5900 to the internet | capture: sha256:bae54b9c545357f5dede9170a85806a91fbde4832a492635ed82aeb383e9b929 | quote: For security reasons, only two TCP ports are open from the outside. These are ports 5900 (VNC) and 22 (SSH).
  - [5] 2026-11-24: SSH is enabled by default and an ordinary SSH client reaches the device | capture: sha256:1fa5d146144e29d249b6dad8f036764bf2115e210999f083a6996eaf21ddebfc | quote: To connect via SSH (Secure Shell), you can use any SSH client. Please note that SSH is enabled by default on all newly created Mac devices.
  - [6] 2026-11-24: the product documents a web console in the Control Panel for the Mac desktop | capture: sha256:fc759a14b9c2e0aae6184bcc7891222e930d25cd8a130b8dd858d0cac9258d45 | quote: Use the web console in the Control Panel to log in to your cloud-hosted Mac device. Please note that the default keyboard input source is set to U.S. English.
  - [4] 2026-11-24: the exposed ports are configurable in the Control Panel | capture: sha256:bae54b9c545357f5dede9170a85806a91fbde4832a492635ed82aeb383e9b929 | quote: The port settings can be restricted or extended in the Control Panel via Mac Bare Metal > Networking > Security Groups > Default.
- sources:
  - [1] https://doc.flow.swiss/platform/pricing/mac-bare-metal
  - [2] https://doc.flow.swiss/platform/account/sign-up
  - [3] https://doc.flow.swiss/mac-bare-metal/start
  - [4] https://doc.flow.swiss/products/mac-bare-metal/devices
  - [5] https://doc.flow.swiss/products/mac-bare-metal/how-to/connect-via-ssh
  - [6] https://doc.flow.swiss/products/mac-bare-metal/how-to/connect-via-remote-desktop
