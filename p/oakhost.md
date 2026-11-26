# OakHost

> oakhost.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oakhost/ | JSON https://fshy.ajam.dev/api/v1/entity/oakhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OakHost

- `compute/oakhost` | paid-only | evidence documented | binding none | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-25T05:18:27.431Z (live) | stale on 2026-12-26
- url https://www.oakhost.com/mac-mini-hosting
- free tier: no free tier: dedicated Mac mini hosting from €200 a month, with the device assigned to your account within minutes of checkout | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: The Mac is dedicated to the account and assigned within minutes of checkout; FileVault is supported and the disk persists for the rental term. No deletion timer is published. | source: [1]
- egress: Every listed tier includes a static IP address and a Gbit/s uplink; no data transfer allowance or per-TB price is published. | metered: no | source: [1]
- identity: email | detail: "Email Address:" and "Password:" on the customer panel login at https://www.oakhost.com/login, whose "Sign Up Now!" link leads to https://www.oakhost.com/register; the registration page says "Creating a free account allows you to manage your subscriptions." The raw form also asks for First Name, Last Name, Confirm Password, Company, Address, Postal Code, City, Country and an EU/UK VAT ID; no card field is shown on the signup page.
- interface: browser, ssh
- limits:
  - request-rate: EUR 70 to EUR 260 a month across thirteen Mac mini tiers; most tiers are marked Out of Stock, and the orderable ones are M1.M at EUR 80 and M6.S at EUR 120 a month [1]
- binding note: No request or rate cap is published: the price, not a quota, is what binds. The dedicated Mac mini is EUR 200 a month on the M6.M row and EUR 340 a month on the M5Pro.L row, and the page states no session cap, idle reap or request allowance.
- interface detail: Browser customer panel with KVM remote management, an SSH-tunnelled remote desktop client (OakConnect) and a customer API for firewall rules and power state.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the Mac mini hosting page was read on 2026-10-22 and prices four monthly tiers. There is no free tier or trial, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: dedicated Mac mini hardware; the page prices tiers rather than shapes
  - session_cap.restart_required: no
  - session_cap.note: a dedicated Mac; the machine can be rebooted, powered on and driven into Recovery Mode, so the state belongs to the account
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - ps.price: dedicated storage in the device
  - ps.durability: dedicated disk, FileVault supported
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: managed firewall with filter rules from the control panel
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '€ 120 /mo.', '€ 130 /mo.', '€ 200 /mo.', '€ 340 /mo.' for dedicated Mac mini hosting, with 'assigned to your account within minutes after checkout', quoted
  - [1] 2026-11-25: the page lists a dedicated Mac mini tier at €200 per month, excluding VAT | capture: sha256:d2f0bf31478d067369d7216245e07b17b293ba84eaf55d68c485631feb587180 | quote: Mac M6.M Apple M6 32 GB RAM 1 TB SSD € 200 /mo. excl. VAT
  - [1] 2026-11-25: the page states the device is assigned to the account within minutes of checkout | capture: sha256:d2f0bf31478d067369d7216245e07b17b293ba84eaf55d68c485631feb587180 | quote: Your Mac is ready to go and will be assigned to your account within minutes of checkout.
  - [1] 2026-11-24: the lowest published monthly tier is EUR 70 | capture: sha256:54197005c520c579e9769da21a10ab929ac5ad82f2ac17decc161516c5d48fd2 | quote: <span class="text-2xl font-bold mx-1 ">70</span>
  - [1] 2026-11-24: the displayed monthly prices range from EUR 70 to EUR 260 | capture: sha256:54197005c520c579e9769da21a10ab929ac5ad82f2ac17decc161516c5d48fd2 | quote: <span class="text-2xl font-bold mx-1 ">260</span>
  - [1] 2026-11-24: browser access to the dedicated Mac is published | capture: sha256:e48ea19bdca45623663e81aa14b422a102739ccf8c4aed9b328e3e887af780b4 | quote: Dedicated Mac mini hosting on macOS Tahoe in Germany, ready to go within minutes - with full access through your browser.
  - [1] 2026-11-24: a customer API and remote management are published | capture: sha256:e48ea19bdca45623663e81aa14b422a102739ccf8c4aed9b328e3e887af780b4 | quote: Enroll your Mac in your automation pipeline using our customer API. Set firewall rules and manage the power state of the Mac in your existing workflow.
  - [1] 2026-11-24: the device is dedicated to the account after checkout | capture: sha256:e48ea19bdca45623663e81aa14b422a102739ccf8c4aed9b328e3e887af780b4 | quote: Your Mac is ready to go and will be assigned to your account within minutes of checkout. No waiting around for someone to manually provision the device for you.
  - [1] 2026-11-24: a static IP is included with the listed tiers | capture: sha256:e48ea19bdca45623663e81aa14b422a102739ccf8c4aed9b328e3e887af780b4 | quote: Static IP Address
  - [1] 2026-11-24: the published Mac mini row carries a monthly price, not a request or rate cap | capture: sha256:d2f0bf31478d067369d7216245e07b17b293ba84eaf55d68c485631feb587180 | quote: € 200 /mo.
  - [2] 2026-11-24: the provider's own signup page creates a free account with no payment gate | capture: sha256:15ee748eb8b66e8898f565705aa592dbaf3aae88e557be22ea81ff953cbc54fb | quote: Creating a free account allows you to manage your subscriptions.
  - [3] 2026-11-24: the customer panel login asks for an email address and password and links to the signup page | capture: sha256:950573a0da3779523cc6c7f1eb25cda947651166b41ccf55e60395e3a2e2b0ee | quote: Email Address:
- sources:
  - [1] https://www.oakhost.com/mac-mini-hosting
  - [2] https://www.oakhost.com/register
  - [3] https://www.oakhost.com/login
