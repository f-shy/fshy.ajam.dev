# FreeVPSTrial.net

> freevpstrial.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freevpstrial/ | JSON https://fshy.ajam.dev/api/v1/entity/freevpstrial.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FreeVPSTrial.net

- `compute/freevpstrial-net` | dead | evidence documented | binding write-gated | category VPS | tier Free Trial VPS, 30 days
- needs card unknown, phone yes, ID no, institution no | verified 2026-10-24T06:58:00.000Z (live) | stale on 2026-11-24
- url https://freevpstrial.net/
- free tier: Quoted from the plan card: 'Free Trial VPS $0.00 / 30 days' with '2GB RAM', '2 vCPU cores', 'NVMe storage', '2TB bandwidth', 'Root / administrator access', 'No credit card required'. The page headline reads 'Free VPS Trial. No credit card. No drag.' | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: Quoted from the terms: 'The Free VPS Trial is a one-time offer per natural person. Strictly one account is allowed per individual, household, or IP address.'
- retention: 'The trial lasts for 30 consecutive days. At the end of the trial, the instance will be suspended. Data will be retained for a 48-hour grace period before being permanently deleted unless the account is upgraded to a paid plan.'
- egress: Quoted from the plan card: '2TB bandwidth'. No port speed is published. | metered: yes | free allowance: 2 TB | source: [1]
- identity: any-phone | detail: claimed no card, with SMS verification possible: quoted from the vendor 'While no credit card is required for the free trial, we may require SMS verification or e-mail validation to prevent automated bot abuse.' The privacy page also states it collects 'Name, email address, and phone number (for SMS verification)'. No registration form exists on the site to confirm what is actually asked for, so this is what the vendor says it would collect, not what it does.
- interface: ssh, rest
- limits:
  - write-gated (binding): SMS verification or email validation, quoted: 'we may require SMS verification or e-mail validation to prevent automated bot abuse' [2]
  - retention-clamped: 30 days, then suspended, then deleted after a 48-hour grace period [2]
  - volume-quota: one account per individual, household or IP address [2]
  - per-ip-shaping: 2 TB of bandwidth on the free plan [1]
- binding note: The gate is not identity but the absence of a route: no registration page, no control panel and no order form exists anywhere on the site, so the verification step is never reached.
- interface detail: Claimed: 'Root / administrator access' over SSH or RDP, provisioned 'after verification'. No control panel URL was reachable from the site: every call to action on the page is an empty fragment.
- tooling: claimed SSH and RDP; no client is downloadable or documented on any page read
- composes with: Nothing to chain: the offer is advertised and the route to it does not exist on the site.
- reliability: The site publishes a status page at status.html; it was not read. No reliability event observed.
- notes: Classified as inactive because no route to provision a machine is available, though website pages return HTTP 200.
- evidence note: The advertised plan, the terms, the retention rule and the identity clause are quoted from the vendor's own pages read. The claim that no signup route exists is a direct observation of the served HTML: every button links to '#' and the only external hosts on the page are gratisvps.net. What the service would deliver is unverified because there is no way to reach it.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.note: as advertised on the plan card; no disk size is stated, only 'NVMe storage'
  - billing_model: free
  - term: 30 days advertised
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: USD 0.00 as advertised; unreachable, so no rate applies
  - free_tier_kind: trial
  - network_out.allow_outbound: yes
  - network_out.ports: advertised 'Root / administrator access'; no port policy published
  - network_out.per_session_bytes: 2 TB advertised
  - session_cap.wall_clock_min: 43200
  - session_cap.restart_required: no
  - session_cap.note: 30 days advertised, then suspended and deleted after 48 hours
  - signup_url: https://freevpstrial.net/
  - signup_note: no working signup route exists: every CTA on the page is '#' and /signup and /register both 404
  - payment_methods: none advertised for the trial
- evidence:
  - [1] 2026-10-24: quoted plan card: 'Free Trial VPS $0.00 / 30 days ... ✓2GB RAM ✓2 vCPU cores ✓NVMe storage ✓2TB bandwidth ✓Root / administrator access ✓No credit card required'
  - [1] 2026-10-24: There is no registration, signup, login or order link anywhere on the page
  - [3] 2026-10-24: HTTP 404 from the origin
  - [4] 2026-10-24: HTTP 404 from the origin
  - [2] 2026-10-24: quoted: 'The trial lasts for 30 consecutive days. At the end of the trial, the instance will be suspended. Data will be retained for a 48-hour grace period' and 'The Free VPS Trial is a one-time offer per natural person. Strictly one account is allowed per individual, household, or IP address.'
  - [2] 2026-10-24: quoted: 'While no credit card is required for the free trial, we may require SMS verification or e-mail validation to prevent automated bot abuse.'
  - [5] 2026-10-24: quoted: 'To provision your VPS and prevent abuse, we collect the following: Contact Info: Name, email address, and phone number (for SMS verification).'
  - [6] 2026-10-24: the contact page offers support and sales email addresses only; no customer portal, login or order link
- sources:
  - [1] https://freevpstrial.net/
  - [2] https://freevpstrial.net/terms.html
  - [3] https://freevpstrial.net/signup
  - [4] https://freevpstrial.net/register
  - [5] https://freevpstrial.net/privacy.html
  - [6] https://freevpstrial.net/contact.html
