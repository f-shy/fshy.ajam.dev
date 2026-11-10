# serv00

> serv00.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serv00/ | JSON https://fshy.ajam.dev/api/v1/entity/serv00.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## serv00

- `compute/serv00` | qualifies-with-caveat | evidence documented | binding volume-quota | category shared shell | tier Free account
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://www.serv00.com/
- free tier: 3 GB of SSD storage, unlimited data transfer, support for up to 100 websites and 16 databases; registration is free and reviewed by hand | unit: GB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the vendor writes 3 GB, a decimal unit; the figure is kept as stated and not converted to GiB
- per-object cap: not applicable
- retention: A user account that has not been properly logged in by the DevilWEB or SSH panel for a period of 90 days will be automatically removed from the system without the possibility of recovering the data collected on that account. | days: 90 | source: [2] | note: the 90-day clock is reset by a DevilWEB panel login as well as by SSH
- egress: unlimited data transfer; the home page states 'unlimited data transfer' with no volume, no shaping tier and no price beyond the allowance | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: email address, first name, last name, one anti-bot question and a reCAPTCHA; the form carries no card field and no phone field. The application is then reviewed by hand: 'Your application has been successfully submitted and is now awaiting manual review. This process usually takes anywhere from a few hours up to 72 hours.' No card, no phone, no document.
- interface: rest, cli
- limits:
  - volume-quota (binding): 3 GB of SSD storage per account (vendor's decimal GB) [1]
  - retention-clamped: account deleted after 90 days without a DevilWEB or SSH login [2]
  - request-rate: a concurrent system-process limit exists; the number is not published, and exceeding it returns 'Server refused to start a shell/command' [3]
  - volume-quota (binding): a port can be reserved from 1024 to 64000, TCP or UDP, with `devil port add`; the number of reservations per account is not published [4]
- limits note: resource limits beyond the 3 GB disk are not published on the pricing page
- binding note: 3 GB of disk and an unpublished concurrent-process ceiling are hit long before the unlimited traffic term matters; the process ceiling blocks SSH itself, not just the workload.
- interface detail: SSH on port 22, plus web hosting
- tooling: SSH, cron, a FreeBSD userspace, a web panel
- composes with: 3 GB of disk with a shell and cron, behind a non-profit gate
- reliability: no reliability event recorded
- notes: Two caveats that decide the row. First, the account is not instant: the form says a few hours up to 72 hours of manual review, so it cannot be relied on tonight. Second, the home page counter read 167,472 of 170,000 accounts, which is 2,528 slots, so registration may close without notice. RAM and vCPU are not published; do not fill them in from a forum.
- evidence note: disk, traffic, account count and the review sentence from the vendor's own pages read; the port range from the docs. RAM and vCPU are not published anywhere read, so they are null rather than guessed.
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: serv00.com
  - port: 22
  - ms: 509
  - ok: yes
  - banner: SSH-2.0-OpenSSH_9.9 FreeBSD-20250219
  - peer: 128.204.218.63
- extras:
  - shape.disk_gib: 3
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: no session cap is published; the published reap is 90 days without a login, and a concurrent-process ceiling can refuse a shell
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://serv00.com/
  - persistent_storage.included_gib: 3
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while active
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: one reserved port in 1024-64000 per reservation, TCP or UDP
  - free_tier_kind: always-free
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - shape_note: vendor states 3 GB (decimal) of SSD; kept as stated, not converted. No RAM or vCPU figure is published on any page read.
  - term: indefinite while the account logs in at least once per 90 days
  - price_arithmetic: no charge; the offer is free
- evidence:
  - probe:serv00.com:22 2026-10-22: TCP connect succeeded in 0.51 s to 128.204.218.63 and read banner SSH-2.0-OpenSSH_9.9 FreeBSD-20250219
  - [5] 2026-10-22: '3 GB for free, no adverts, no hooks'
  - [1] 2026-10-24: quoted: 'offering 3 GB of SSD disk space, unlimited data transfer, and support for up to 100 websites and 16 databases'; and 'total accounts created on the servers 167472 / 170000'
  - [6] 2026-10-24: quoted: 'Your application has been successfully submitted and is now awaiting manual review. This process usually takes anywhere from a few hours up to 72 hours.' The fetched form has fields for first name, last name, username, email and one question, and no card or phone input.
  - [2] 2026-10-24: quoted: 'A user account that has not been properly logged in by the DevilWEB or SSH panel for a period of 90 days will be automatically removed'
  - [4] 2026-10-24: quoted: 'select the port number (from 1024 to 64000), its type'; and 'devil port add PORT TYPE'
  - [7] 2026-10-24: quoted: 'Binexec allows you to manage the ability to run your own software on the serv00.com server.'
  - [3] 2026-10-24: admin reply quoted: 'The message "Server refused to start a shell/command" usually indicates that you have exceeded the limit of concurrently running system processes.'
- sources:
  - [1] https://www.serv00.com/
  - [2] https://www.serv00.com/terms-of-service
  - [3] https://forum.serv00.com/d/1754-ssh-cant-loginhelp
  - [4] https://docs.serv00.com/Port_reservation/
  - [5] https://serv00.com/pricing
  - [6] https://www.serv00.com/register-account/
  - [7] https://docs.serv00.com/Binexec/
