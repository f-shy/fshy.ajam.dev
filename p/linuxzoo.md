# Linuxzoo

> linuxzoo.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linuxzoo/ | JSON https://fshy.ajam.dev/api/v1/entity/linuxzoo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Linuxzoo

- `compute/linuxzoo` | fails-egress | evidence documented | binding per-ip-shaping | category VM | tier Free learner VM
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:41:00.000Z (live) | stale on 2026-11-24
- url https://linuxzoo.net/page/notes/tech.html
- free tier: 'Learn Linux from the safety of your chair using a remote private linux machine with root access.' Machines are booked from a queue: 'Your position in the queue, your speed in getting a machine, the amount of time you get using a machine, and the things you can do with the machine once you have one are all related to the information you give during registration. This can range from 10 minutes of machine time, up to 2 hours of guaranteed time with automatic time extensions if the site is quiet (which is called HOLD time in the interface).' | unit: minutes | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: 'You are allowed to have only one account per person on this site.'
- retention: 'This previous image approach is not precise and reliable (sometimes it will not give you your most up-to-date image when you request it). It tried hard to keep your work between reboots, but this is not guarenteed.' The disk files are deleted by the daemon 'as and when required'.
- egress: 'Firstly, the machines are sandboxed from the internet, so no outgoing traffic is supported.' and 'Free users are basically sandboxed to the virtual network.' There is no outbound path at all. | metered: no | free allowance: none | source: [2]
- identity: email | detail: no card, no phone, no document.
- interface: ssh
- limits:
  - retention-clamped: 10 minutes to 2 hours of guaranteed machine time, extended only when the site is quiet [1]
  - retention-clamped: the VM is shut down within a few minutes if no browser window has a control panel on it [1]
  - volume-quota: 7 server nodes of 192 GB RAM and 1 TB disk each, modelled for about 140 concurrent users [2]
  - per-ip-shaping (binding): no outbound traffic; the guest is sandboxed to the virtual network [2]
- binding note: No outbound network means the machine cannot fetch a package, reach an API or carry a tunnel, which removes most uses before the two-hour clock even matters.
- interface detail: SSH access to the guest through a browser JavaScript terminal or a standard SSH client, plus VNC for desktop images.
- tooling: a browser, or any SSH client; VNC for the desktop images
- composes with: A root VM for a two-hour lab, with no account cost and no card, but no outbound network: useful for learning and for offline compute, useless for a tunnel or a monitor.
- reliability: The site's own front page carries a live 'Status: Stable' line and also the notice 'Patching and rebooting underway', so the service is maintained but not always up; the operator states it is a privilege rather than a right and that response time may be long.
- notes: Classified as a rejection on egress, not on money or identity: it is free, it needs only an email, and it gives root. The disqualifier is explicit and repeated on the vendor's own page: 'no outgoing traffic is supported'. That makes it a lab for learning Linux, which is what it says it is, and not a machine for a stack. A second constraint is the control-panel reap: the VM dies within minutes if no browser window is showing a control panel, so it cannot run unattended even inside the two-hour window. The per-VM shape is unpublished. The front page showed a transient 'Having a disaster' error block on the same read, so the service is live but rough.
- evidence note: The no-egress rule, the queue, the 10-minute to 2-hour window, the control-panel reap, the node count and the email requirement are all quoted from linuxzoo.net's own technical and how-to pages read. The per-VM vCPU, RAM and disk allocation is not published on any page read; only the host nodes' totals are.
- extras:
  - shape.note: not published per VM; the host nodes are 192 GB RAM and 1 TB disk each, which is capacity, not an allocation
  - billing_model: free
  - term: per booking, 10 minutes to 2 hours
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge and no payment field; the currency is queue position and wall-clock
  - free_tier_kind: always-free
  - network_out.allow_outbound: no
  - network_out.allow_inbound_listen: no
  - network_out.ports: none; the guest is sandboxed to the virtual network
  - network_out.static_ip: no
  - session_cap.wall_clock_min: 120
  - session_cap.restart_required: yes
  - session_cap.note: 10 min to 2 h of HOLD time; killed within minutes if no control panel is open in a browser
  - signup_url: https://linuxzoo.net/
  - payment_methods: none; there is no billing system
- evidence:
  - [2] 2026-10-24: quoted: 'Firstly, the machines are sandboxed from the internet, so no outgoing traffic is supported. Secondly the machines only stay running when you are logged into them and logged into linuxzoo.'
  - [2] 2026-10-24: quoted: 'As of 2025 we have 7 active server nodes, each with 192GB of RAM and 1TB of disk. The system is modelled on supporting around a maximum of 140 users at a time.'
  - [1] 2026-10-24: quoted: 'This can range from 10 minutes of machine time, up to 2 hours of guaranteed time with automatic time extensions if the site is quiet (which is called HOLD time in the interface).'
  - [1] 2026-10-24: quoted: 'if none of you web browser's windows have a control panel on them, then your VM machine will shutdown within a few minutes and you will be dequeued'
  - [3] 2026-10-24: quoted: 'You are allowed to have only one account per person on this site.' and 'When you register use one of your own email addresses and make sure it is valid and working.'
  - [4] 2026-10-24: quoted: 'Learn Linux from the safety of your chair using a remote private linux machine with root access.' and the image table naming AlmaLinux 10, Caine Forensics 10.0/13.0 and Kali 2024-4
- sources:
  - [1] https://linuxzoo.net/page/notes/howtouse.html
  - [2] https://linuxzoo.net/page/notes/tech.html
  - [3] https://linuxzoo.net/page/notes/terms.html
  - [4] https://linuxzoo.net/
