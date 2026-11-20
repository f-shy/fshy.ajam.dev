# BoxedTux

> boxedtux.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/boxedtux/ | JSON https://fshy.ajam.dev/api/v1/entity/boxedtux.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BoxedTux

- `compute/boxedtux` | fails-identity | evidence documented | binding write-gated | category dev environment | tier EduCloud student vServer
- needs card no, phone no, ID no, institution yes | verified 2026-10-24T06:17:00.000Z (live) | stale on 2026-11-01
- url https://boxedtux.com/
- free tier: A free student vServer: '1 vCPU', '1 GB DDR5', '10 GB NVMe', 'IPv4 address', 'IPv6 /64 block included', 'Monthly bandwidth 200 GB', 'Port speed 50 Mbit/s', full root SSH, web console and VNC. The home page states 'Cost · no card needed'. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-24 | source: [1] | note: registration is stopped on the day read; the shape is what the page advertises for when it reopens
- per-object cap: not applicable: the unit is a virtual server, not an object
- retention: 'Renew each semester — 30-second re-verification every 6 months. Active learners can request extensions at any time.' No inactivity-deletion clock is published. | source: [1] | note: a six-month re-verification cadence, not an idle clock
- egress: 'Monthly bandwidth 200 GB' and 'Port speed 50 Mbit/s' | metered: yes | free allowance: 200 GB | source: [1]
- identity: institution | detail: 'Only academic email addresses are allowed. Not having an academic address? Contact us with proof of your student or educator status.' No card and no hold: the home page says 'Cost · no card needed'. This gate cannot be cleared at any price.
- interface: ssh
- limits:
  - volume-quota: 200 GB of monthly bandwidth on a 50 Mbit/s port [1]
  - volume-quota: 1 vCPU, 1 GB RAM, 10 GB NVMe [1]
  - write-gated (binding): academic email address or proof of student/educator status, plus a six-monthly re-verification [2]
  - write-gated (binding): new registrations are stopped: 'Due to resource limits new account registrations are currently stopped!' [2]
- limits note: Boxes run for 6-month terms with 'There isn't any grace-period! ... Expired boxes will be immediately deleted', so the term ends with no recovery window; but the eligibility gate, an institutional address, fails first.
- binding note: two gates stack: the account requires academic affiliation, and on the day read the registration form itself was closed for capacity
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: Root SSH, web console, VNC, Docker allowed, distributions from Debian to Gentoo. /register returned a 500, so the signup path itself was not read.
- composes with: Complements BoxyBSD inside one operator: BoxyBSD runs the BSD images, BoxedTux runs Ubuntu, Debian and Rocky, which is the distribution set most tooling assumes. The chain is closed because both halves need an affiliation: BoxyBSD needs a sponsor's invitation, BoxedTux needs an institution.
- reliability: no reliability event observed; the home page advertises 99.7% uptime and names DDoS protection as optional.
- notes: Worth recording rather than skipping: this is the best-specified free machine found in this class (1 GB DDR5, 10 GB NVMe, real IPv4, 200 GB traffic, 50 Mbit/s, root SSH) and it is entirely out of reach on two independent grounds. No academic affiliation, and a closed register. If the operator ever opens a non-academic programme the home page hints at ('running a non-profit or OSS project outside academia? reach out — separate program available'), the row would be worth re-testing.
- evidence note: shape, traffic and the academic gate are quoted from first-party pages read; the registration closure is quoted from the register page as served
- extras:
  - facets.class: perpetual-vps
  - facets.free_tier_kind: perpetual-6-month-renewable
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 10
  - facets.shape.gpu_count: 0
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 10
  - billing_model: free
  - term: semester, re-verified every 6 months
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no price: 'Cost · no card needed' and '0 €'
  - free_tier_kind: perpetual
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a real public IPv4 and an IPv6 /64
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: none published; re-verification every 6 months
  - registration_state.as_read: 2026-10-24
  - registration_state.state: closed
  - registration_state.quoted: new account registrations are currently stopped
- evidence:
  - [1] 2026-10-22: the spec block reads 'vCPU cores 1 vCPU / Memory 1 GB DDR5 / Storage 10 GB NVMe / IPv4 address 0 / IPv6 /64 block included / Monthly bandwidth 200 GB / Port speed 50 Mbit/s', and the cost line reads '0 EUR Cost - no card needed'; probe 200, 31698 bytes, sha256 69b56eb86c57d18fd2fef4cc62bac17c95dc3d8cceb9438bbd674eed67ef0c21
  - [1] 2026-10-22: the '// eligible' list contains only academic categories, and the FAQ states 'We will provide additional ways for legitimations wihout.edu domain at a later time', quoted
  - [1] 2026-10-22: 'Servers are granted for 6-month terms aligned with semesters. You'll get an email 2 weeks before expiry. Renewal takes 30 seconds with a quick student re-verification.', 'There isn't any grace-period! ... Expired boxes will be immediately deleted.', 'No! There aren't any upgrade options available.', quoted
  - [3] 2026-05-04: the operator announces boxedtux.com as a new free Linux VPS project built on Proxmox clusters, beside BoxyBSD, quoted
  - [2] 2026-10-24: quoted: 'Free Linux servers for students for educational purposes. Only academic email addresses are allowed.' and 'Important: Due to resource limits new account registrations are currently stopped! Please do not mail us for invite codes at this time.'
  - [1] 2026-10-24: quoted: '1 vCPU', '1 GB DDR5', '10 GB NVMe', 'IPv4 address', 'IPv6 /64 block included', 'Monthly bandwidth 200 GB', 'Port speed 50 Mbit/s', 'Cost · no card needed'
  - [1] 2026-10-24: quoted: 'Renew each semester', '30-second re-verification every 6 months. Active learners can request extensions at any time.'
  - [4] 2026-10-24: the imprint states 'BoxedTux Education Platform (non-profit project)', operated by a named individual at a postal address in Germany, and 'VAT ID (USt-IdNr.): not applicable'
- sources:
  - [1] https://boxedtux.com/
  - [2] https://boxedtux.com/register
  - [3] https://nostr.at/nevent1qqsy0rhaeqmysfgm9u6qmlwse36p40pd74cqjfxp53j900x40nhghsgzyr0stxvm4ksd6w83r5u8pw49x4v274luzwdznlwwgetn5rt5z5pz62zns5q
  - [4] https://boxedtux.com/imprint
