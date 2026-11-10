# Prized

> prized.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/prized/ | JSON https://fshy.ajam.dev/api/v1/entity/prized.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Prized

- `compute/prized` | qualifies-with-caveat | evidence documented | binding volume-quota | category dev environment | tier free credit (no plan)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:12.407Z (live) | stale on 2026-12-05
- url https://prized.dev/docs/billing
- price parsed USD 10.22/mo
- free tier: 'New workspaces get $30 of free credit, once per person ... and the tour starts a box on it with no card. It does not refill.' While on the credit alone: sizes Nano to Small only, one box at a time, no process at full CPU for more than 30 minutes. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: Smallest grant in this category, but the only one whose meters let a single credit run a box for multiple months.
- per-object cap: On the free credit 'Nano, Micro, Extra Small, or Small only'; Medium and larger answer `409 tier_unavailable`. A Nano is 2 vCPU / 2 GB / 40 GB at USD 0.014 an hour awake. | source: [1] | note: A Small is 4 vCPU / 16 GB / 300 GB at USD 0.137 an hour, which burns the whole USD 30 in nine days.
- retention: Asleep, a box costs only its disk at USD 0.0001 per GB-hour; a Small asleep for a month is about USD 22. Credit rolls over up to two months of the plan. | source: [1]
- egress: not published: the billing, machines, sandboxes and pricing pages state no egress allowance and no overage price; outbound traffic from a box is not filtered | metered: no | source: [1]
- identity: email | detail: 'the tour starts a box on it with no card' and the credit is once per person by email or by Google or GitHub account. No card, no phone, no ID at signup; paid plans use Stripe Checkout, cards only.
- interface: ssh, cli, rest
- limits:
  - volume-quota (binding): USD 30 one-time free credit, once per person [1]
  - volume-quota (binding): one box at a time on the credit [1]
  - volume-quota (binding): no process at full CPU for more than 30 minutes on the credit [1]
- limits note: The 30-minute full-CPU rule can pause the workspace and answer 409 workspace_held on the next create or wake; it is a use cap that no other provider here imposes.
- binding note: The 30-minute full-CPU rule is what fails first for any real build; the credit itself is generous at the Nano size.
- interface detail: SSH to the box (plain ssh or prized ssh); the prized CLI (macOS, Linux, Windows); an HTTP API for boxes and sandboxes; a browser dashboard
- tooling: not stated
- composes with: not established
- reliability: On the credit a box auto-pauses itself after 2 hours idle unless the window is changed or switched off per box; it never pauses in its first 24 hours.
- notes: USD 30 / USD 0.014 = 2,143 hours, which is 89 days of a 2 vCPU / 2 GB box with no card. The page's own claim of 'about three months on a Nano' matches. This is the longest no-card calendar coverage in this category and it is a real VM, not a sandbox, but a 2 vCPU / 2 GB box is also the smallest shape any row here offers for a full month.
- evidence note: Every number is from the billing page read. Not observed: whether the 30-minute CPU rule is enforced by cgroup throttling or by pausing, which decides whether a long build is slowed or killed.
- extras:
  - keep_rate: 1.0
  - billing_model: per-second while awake, per GB-hour while asleep
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.disk_gib: 40
  - session_cap.idle_reap_s: 7200
  - session_cap.restart_required: no
  - session_cap.note: 2-hour idle auto-pause by default on the credit; can be changed per box or switched off
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: all
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.gib: 40
  - ps.price: $0.0001 a GB-hour while asleep
  - ps.durability: disk survives a pause
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - shape_max_on_credit.vcpu: 4
  - shape_max_on_credit.ram_gib: 16
  - shape_max_on_credit.disk_gib: 300
  - term: one-time credit
  - m10h_usd: 4.2
  - m24h_usd: 10.22
  - price_arithmetic: 0.014/h x 730 = 10.22 a month; 30 / 0.014 = 2143 h = 89.3 days
  - credit_usd: 30
  - credit_months_at_shape: 2.9
  - credit_hours_at_shape: 2143
  - credit_expiry: does not refill; rollover on a paid plan is two months
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Nano (nano) 2 vCPU / 2 GB, 40 GB, $0.014 an hour awake, $0.004 an hour asleep, $10 a month to run 24/7' with 'Pausing keeps the money' and 'While the workspace runs on the free credit alone: One box at a time' and 'Credit rolls over up to two months', quoted
  - [1] 2026-10-24: quoted: 'New workspaces get $30 of free credit, once per person, as the owner walks through onboarding or first signs in with `prized login` through the browser; it spends like paid credit, and the tour starts a box on it with no card.'; 'Awake around the clock, the credit lasts about three months on a Nano, five weeks on a Micro, nine days on a Small'; 'No process at full CPU for more than 30 minutes'.
  - [1] 2026-10-24: quoted box table: 'Nano (`nano`) | 2 vCPU / 2 GB | 40 GB | $0.014 an hour | $0.004 an hour | $10 a month'; 'Small (`flow`) | 4 vCPU / 16 GB | 300 GB | $0.137 an hour'.
  - [2] 2026-11-03: outbound traffic is unfiltered; no allowance or price is stated | capture: sha256:ca43284b6e8ba73e1a26f9adff6b0b5358d540a1bf6457f18a6533b969a97f04 | quote: | Outbound | Not filtered |
  - [3] 2026-11-03: SSH access is documented | capture: sha256:aa291e2ea0d1872eec5eb3a985188183f266f7399fcdb306262c5201c8159be1 | quote: You edit and run everything on the box over SSH.
  - [4] 2026-11-03: an HTTP API and a CLI exist | capture: sha256:54772d4da94f3b9ecd5b36bd42171d01f2233ea103811c66d879bd314d262878 | quote: through the HTTP API or the `prized` CLI.
- sources:
  - [1] https://prized.dev/docs/billing
  - [2] https://prized.dev/docs/machines
  - [3] https://prized.dev/docs
  - [4] https://prized.dev/
