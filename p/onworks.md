# OnWorks

> onworks.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onworks/ | JSON https://fshy.ajam.dev/api/v1/entity/onworks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OnWorks

- `compute/onworks-workstation` | fails-quota | evidence documented | binding retention-clamped | category desktop | tier Free online workstation
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:59:00.000Z (live) | stale on 2026-11-24
- url https://www.onworks.net/playonline/runonworks.php
- free tier: 'It is a free emulation platform that does not even ask you to be registered in it. Therefore, once we have opted for a workstation, after 25 seconds you can work with the Operating System.' Operating systems offered include Ubuntu 22, Fedora, Debian, CentOS, Parrot Security OS and Windows via Wine. | unit: minutes | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: one workstation per session; no per-account limit exists because there is no account
- retention: 'OnWorks destroys the open session if it detects that you have accumulated five minutes of inactivity.' Work can be saved only by exporting the whole OS image to Google Drive, or by uploading files through the site's file manager.
- egress: not published: no traffic allowance or port speed is stated anywhere read | metered: no | source: [1]
- identity: anonymous | detail: no account, no email, no card, no phone: 'It is a free emulation platform that does not even ask you to be registered in it.' Nothing is filled in to start a workstation.
- interface: rest
- limits:
  - retention-clamped (binding): the session is destroyed after five minutes of inactivity [1]
  - volume-quota: the per-workstation vCPU, RAM and disk are not published; the site only quotes each distribution's own minimum requirements [2]
- binding note: Five minutes of no input ends the session, which is the shortest idle reap documented and rules out anything unattended.
- interface detail: A browser-delivered desktop inside a virtualised workstation, with a file manager for upload and download and Google Drive image export. No SSH, no API, and no way to attach from outside.
- tooling: a browser only
- composes with: Nothing for a stack: no SSH, no inbound port, and a five-minute idle reap, so it cannot be a node, a monitor or a build runner.
- reliability: no reliability event observed. The site is ad-funded and the pages are heavy with promotional blocks.
- notes: OnWorks provides free ephemeral browser-based Linux desktops with no SSH or inbound ports and a five-minute idle timeout. Machine configurations are shared and temporary.
- evidence note: The anonymous access, the 25-second start and the five-minute idle destruction are quoted from OnWorks' own run page read. The workstation's vCPU, RAM and disk are not published anywhere on the site; only each distribution's minimum requirements are quoted, which is not the allocation.
- extras:
  - shape.note: not published; the site quotes only each distribution's own minimum requirements
  - billing_model: free
  - term: per session
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge and no account; the currency is the five-minute idle timer
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: none; browser desktop only
  - network_out.static_ip: no
  - session_cap.idle_reap_s: 300
  - session_cap.restart_required: yes
  - session_cap.note: destroyed after 5 minutes of inactivity; no wall-clock cap published
  - signup_url: https://www.onworks.net/
  - payment_methods: none; there is no account to bill
- evidence:
  - [1] 2026-10-24: quoted: 'It is a free emulation platform that does not even ask you to be registered in it. Therefore, once we have opted for a workstation, after 25 seconds you can work with the Operating System.'
  - [1] 2026-10-24: quoted: 'Finally note that OnWorks destroys the open session if it detects that you have accumulated five minutes of inactivity.'
  - [1] 2026-10-24: quoted: 'you are going to use free resources so if we detect that you run workstations but you perform no action during more than 5 minutes, we free your session for another user'
  - [2] 2026-10-24: quoted: 'Free Cloud Hosting by OnWorks ... allows to run your workstations Linux online, Windows online emulator or MACOS online emulator only using your web browser', with 'Ubuntu 22', 'Parrot Security OS' and 'Wine' listed
  - [3] 2026-10-24: the distribution page quotes Kali's own minimum requirements and the site's own advertising blocks; it states no allocation for the hosted workstation
- sources:
  - [1] https://www.onworks.net/playonline/runonworks.php
  - [2] https://www.onworks.net/
  - [3] https://www.onworks.net/os-distributions/debian-based/free-kali-linux-online
