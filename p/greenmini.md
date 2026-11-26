# Green Mini host

> greenmini.host | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/greenmini/ | JSON https://fshy.ajam.dev/api/v1/entity/greenmini.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Green Mini host

- `compute/greenmini` | paid-only | evidence documented | binding request-rate | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:50.015Z (live) | stale on 2026-12-26
- url https://portal.greenmini.host/checkout/order
- free tier: no free tier: the Dedicated Mac mini M2 configuration at EUR 69,00 a month with a EUR 50,00 setup fee, or EUR 59,00/mo paid annually (€708,00/yr), setup €0,00, Save 14% | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Unlimited bandwidth on every service, subject to Fair Use; no traffic-based charges | metered: no | source: [1]
- identity: email | detail: the portal registration page asks for an email address and mails a link to continue; Google and GitHub OAuth buttons are offered as alternatives; no phone, card or ID document is asked for at registration
- interface: unknown
- limits:
  - request-rate (binding): EUR 59 to EUR 148 a month depending on the Mac; no hourly rate and no free tier [1]
  - retention-clamped: delivery is quoted per configuration: under 24 hours for one M4 build, up to 3 business days for others [1]
- interface detail: The order page lists SSH/VNC enabled and full admin access on every service; no API or programmatic interface is published
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the order page was read on 2026-10-22 and prices the hardware ladder. The product is a monthly rental of a Mac, which is paid-only
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.vcpu: 10
  - shape.ram: 16
  - shape.disk: 512
  - shape.gpu_class: Apple M4
  - shape.gpu_count: 1
  - shape.note: M4 10-core CPU and 10-core GPU, 16 GB unified memory, 512 GB SSD at EUR 87 a month
  - session_cap.restart_required: no
  - session_cap.note: a monthly rental with no session clock; the machine belongs to the account for the month
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - ps.gib: 512
  - ps.price: included in the monthly price
  - ps.durability: dedicated SSD
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the checkout page was read on 2026-10-22 and prices Mac mini and Mac Studio hosting from EUR 59 to EUR 148 a month: 'M4 10/10C · 16GB · 512GB SSD €87,00/mo', 'M6 12C/12C · 16GB · 256GB SSD €85,00/mo'. There is no free tier and no free month
  - [1] 2026-11-25: the annual cycle at EUR 59,00 a month carries setup EUR 0,00, while the monthly cycle carries the EUR 50,00 setup fee | capture: sha256:5313df99fb02d6abaa112774a57baf862afeb562d9fba75496deb53fa0d7648e | quote: €59,00/mo, paid annually (€708,00/yr), setup €0,00, Save 14%
  - [1] 2026-11-24: the order page publishes an unlimited-bandwidth term with Fair Use | capture: sha256:4209fbe936539e1cbeb66d91aed3d7a43fecc197007ec6373bef6de76c4e83c9 | quote: Unlimited bandwidth. Use our internet connections without limits based on Fair Use. No surprise traffic bills.
  - [2] 2026-11-24: registration asks for an email address | capture: sha256:a1b972fe5cdec64809438d14b5e95f59353cab37723402fb70a8311fb9425218 | quote: Enter your email and we will send a link to continue.
  - [1] 2026-11-24: the Mac server price ladder is unchanged, with no free tier | capture: sha256:93c271103d6de65cebbd1ea8f3f8d1462a41a000f40a481e221832b6eeee340e | quote: M6 12C/12C, 16GB, 256GB SSD | €97,00 | €50,00
  - [1] 2026-11-24: access is by SSH/VNC to a public IPv4 address with full admin rights | capture: sha256:4209fbe936539e1cbeb66d91aed3d7a43fecc197007ec6373bef6de76c4e83c9 | quote: Public IPv4 address - SSH/VNC enabled and full admin access
- sources:
  - [1] https://portal.greenmini.host/checkout/order
  - [2] https://portal.greenmini.host/register
