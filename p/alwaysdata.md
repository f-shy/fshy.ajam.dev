# alwaysdata

> alwaysdata.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alwaysdata/ | JSON https://fshy.ajam.dev/api/v1/entity/alwaysdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## alwaysdata

- `compute/alwaysdata` | fails-quota | evidence documented | binding write-gated | category shared shell | tier Free (Public Cloud)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://help.alwaysdata.com/en/docs/admin-billing/billing/public-cloud-prices/
- free tier: 0 EUR a month for life: 1 GB of SSD, 256 MB of RAM, a quarter of a CPU, 3 days of backups | unit: GB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the vendor states 1 GB, a decimal unit; kept as stated
- per-object cap: not applicable
- retention: a free profile must connect to the administration interface every 120 days while it is less than a year old; otherwise the profile is suspended | days: 120 | source: [2] | note: suspension is lifted by a single login; the data is not deleted on suspension
- egress: not published as a volume; the restricted-mode page states that without a card, HTTP requests are filtered more strictly and outbound SMTP may be limited in quantity and time | metered: no
- identity: email | detail: email signup, no card required to hold the free plan. A card is what lifts restricted mode: 'fill-in your credit card details in your means of payment area (even if you have a free account)'. No hold is stated because no payment is taken on the free plan; the restriction is throttling, not a charge.
- interface: ssh
- limits:
  - volume-quota: 1 GB of disk including files, mail and databases [1]
  - write-gated (binding): a long-running service on the free plan risks suspension [1]
  - retention-clamped: free profiles suspended after 120 days without an admin-interface login (6 months for 1-4 year old profiles, yearly after 4 years) [2]
  - per-ip-shaping: without a card, HTTP processing is filtered more strictly and SMTP sending may be throttled [3]
- limits note: a 24/7 service on the free plan risks suspension, which makes it a relay endpoint rather than a node
- binding note: the free plan's footnote forbids running services, so a daemon or a listener is out of scope regardless of the 256 MB of RAM.
- interface detail: SSH to the account user, plus a web panel and an API
- tooling: SSH, the alwaysdata admin panel and API, scheduled tasks
- composes with: a French shared host with a 1 GB disk and a 120-day login clock
- reliability: no reliability event recorded
- notes: Worth recording because it looks like the answer and is not: 1 GB and SSH for 0 EUR, ruled out by one sentence in the footnote. It remains usable as a place to serve a static site or run a cron-driven script, if the script is not a service.
- evidence note: the suspension clock and the restricted-mode rules from its help pages. All read.
- extras:
  - shape.vcpu: 0.25
  - shape.ram_gib: 0.25
  - shape.disk_gib: 1
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: the clock is 120 days without an admin login, not a session cap
  - keep_rate.value: 0.0
  - keep_rate.basis: a free profile costs nothing
  - keep_rate.source: https://www.alwaysdata.com/en/pricing/
  - persistent_storage.included_gib: 1
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: SSD
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: 120 days without a login
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: no service may listen; sites are served through the shared front end
  - network_out.static_ip: no
  - free_tier_kind: always-free
  - shape_note: 256 MB of RAM is 0.25 GiB; a quarter of a CPU as the vendor states it; 1 GB decimal disk kept as stated
  - term: indefinite with a login every 120 days in the first year
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: 0 EUR a month, VAT excluded, annual or monthly payment both Free
- evidence:
  - [4] 2026-10-06: free plan at EUR 0 with 1 GB SSD, 256 MB RAM and 1/4 CPU, available for life
  - [4] 2026-10-06: a free profile is suspended after a long period without connecting to the administration interface
  - [4] 2026-10-22: read live: 1 GB SSD, 256 MB RAM, 1/4 CPU free for life on the personal plan
  - [1] 2026-10-24: quoted: 'The Free plan cannot be used for profit purposes. The creation of websites on this plan is limited to the `alwaysdata.net` account's address and it cannot be used to run services.'
  - [1] 2026-10-24: quoted table: 'Disk space 1 GB', 'RAM 256 MB', 'CPU 1/4', 'Annual payment (VAT excluded) Free'
  - [3] 2026-10-24: quoted: 'fill-in your credit card details in your means of payment area (even if you have a free account)' and 'Adding a bank account (even with direct debit) does not lift the restriction.'
  - [2] 2026-10-24: quoted: 'a profile created in less than a year must connect every 120 days'
- sources:
  - [1] https://help.alwaysdata.com/en/docs/admin-billing/billing/public-cloud-prices/
  - [2] https://help.alwaysdata.com/en/docs/admin-billing/profile/suspension/
  - [3] https://help.alwaysdata.com/en/docs/admin-billing/profile/restricted-mode/
  - [4] https://www.alwaysdata.com/en/pricing/
