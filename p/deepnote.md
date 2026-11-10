# Deepnote

> deepnote.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deepnote/ | JSON https://fshy.ajam.dev/api/v1/entity/deepnote.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Deepnote (Free)

- `compute/deepnote-free` | qualifies-with-caveat | evidence documented | binding volume-quota | category notebook runtime | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:51:16.011Z (live) | stale on 2026-12-04
- url https://deepnote.com/pricing
- free tier: Free forever, including the Basic machine at 5 GB RAM and 2 vCPU marked Unlimited; background execution and scheduled notebooks are Team features at USD 39 per editor per month | unit: unlimited | metered on: none | read on: 2026-10-24 | source: [1] | note: The machine time is unlimited on the Basic machine and an idle session stops after 15 minutes; free GPU hours: none stated, and the Team plan lists $50 worth of GPU every month (unverified whether the Free column of the GPU machine row is ticked, because the captured text does not render check marks). The capability that makes it useful for an unattended job is not in the free plan.
- per-object cap: not applicable: the unit is a session, not an object
- retention: not stated on the pricing page | source: [1]
- egress: no egress allowance or price published | metered: no | source: [1]
- identity: email | detail: an account; the pricing page states no card for the Free plan
- interface: rest, cli
- limits:
  - volume-quota (binding): 0 hours of unattended execution: background execution and scheduled notebooks are Team-tier features [1]
- binding note: the free machine time is unlimited, so the thing that fails is not a counter but the absence of any unattended mode
- interface detail: a browser notebook with a Python environment and integrations
- tooling: the web editor; background execution and scheduling need the Team plan
- composes with: an interactive notebook with generous free machine time, and no way to run it without a human present
- reliability: no reliability event recorded
- notes: The free tier is genuinely unlimited on the Basic machine, which makes it the best free interactive notebook for a long CPU session. It fails evaluated providers's question because a run ends with the tab. No idle timeout is published.
- evidence note: the machine shape and the tier gating are quoted from the pricing page today. RAM is the vendor's '5 GB' in decimal; kept as stated.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 5
  - shape.note: vendor states 5 GB RAM, 2 vCPU on the Basic machine; Plus (16 GB / 4 vCPU) is not in the free plan
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00 for the Free plan
  - free_tier_kind: free-forever
  - unattended: no
  - unattended_mechanism: none on Free; background execution is a Team feature
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: unstated
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.idle_reap_s: 900
  - session_cap.restart_required: no
  - session_cap.note: idle shutdown after 15 minutes of inactivity on Free (24 hours on Team); the maximum wall-clock lifetime is not published
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: the Machines table names 'Basic (5 GB RAM, 2 vCPU)' and gives the Free column 'Unlimited'
  - [1] 2026-10-24: the Team plan bullet list contains 'Background execution' and 'Scheduled notebooks'; the Free plan bullet list on the same page contains neither, which is an absence rather than a sentence the vendor wrote
  - [1] 2026-10-24: quoted: '$39 per editor/month billed yearly' for Team, the tier that carries background execution
  - [1] 2026-10-24: quoted: 'A free version for aspiring data analysts and scientists.'
  - [1] 2026-11-03: the Machines table names the Basic machine at 5 GB RAM and 2 vCPU as Unlimited on Free | capture: sha256:e5431771146a7b8b099e2cc2734a4ebc97af84bc1eb01958ab1f4c61009e06ab | quote: Basic (5 GB RAM, 2 vCPU)
  - [1] 2026-11-03: the Free plan has a 15 minute inactivity period; Team has 24 hours | capture: sha256:e5431771146a7b8b099e2cc2734a4ebc97af84bc1eb01958ab1f4c61009e06ab | quote: Inactivity period 1. Free 15 minutes
  - [1] 2026-11-03: the Free plan inactivity period is 15 minutes | capture: sha256:e5431771146a7b8b099e2cc2734a4ebc97af84bc1eb01958ab1f4c61009e06ab | quote: Inactivity period 1. Free 15 minutes
  - [1] 2026-11-03: the Team plan list carries a monthly GPU credit; the Free plan list carries none | capture: sha256:e5431771146a7b8b099e2cc2734a4ebc97af84bc1eb01958ab1f4c61009e06ab | quote: $50 worth of GPU every month
- sources:
  - [1] https://deepnote.com/pricing

## Deepnote Education plan

- `compute/deepnote-education-plan` | fails-identity | evidence documented | binding none | category notebook runtime
- needs card unknown, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://deepnote.com/docs/edu-overview
- free tier: 'Our Education plan is 100% free for students, teachers, and researchers who connect their accounts to school email addresses. The free Education plan provides access to most of the Team plan features other than advanced computing machines, Scheduling and Deepnote AI.' The GitHub pack describes the same offer as 'unlimited basic machines with up to 5GB RAM and 2vCPU'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: a school email address connected to the account: the edu page states the plan is '100% free for students, teachers, and researchers who connect their accounts to school email addresses'. Whether any further enrollment document is checked is not stated, and no card, hold, debit or prepaid term is stated.
- interface: rest
- limits note: The primary constraint is machine hardware specification: 2 vCPU and 5 GB RAM on basic instances.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A free 2 vCPU notebook is a real development surface for analysis work, but it duplicates what Google Colab's free tier gives without any enrollment, so it adds no capacity that is not already reachable.
- reliability: no reliability event recorded
- notes: The pack page and the vendor page disagree on scope: the pack promises 'unlimited basic machines', the vendor page says advanced machines are excluded. Both are documented, and the vendor page is the authority on the plan itself. This is a case where the aggregator's description is generous and the underlying product page is the one that binds.
- extras:
  - facets.class: student-pack
  - facets.free_tier_kind: recurring-credit
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 5
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: '100% free for students, teachers, and researchers who connect their accounts to school email addresses'; the Education plan excludes 'advanced computing machines, Scheduling and Deepnote AI'.
  - [2] 2026-10-22: 'unlimited basic machines with up to 5GB RAM and 2vCPU' under the Deepnote offer, which is a smaller reading than the vendor's own edu page implies.
- sources:
  - [1] https://deepnote.com/docs/edu-overview
  - [2] https://education.github.com/pack

## Deepnote (Storage)

- `storage/deepnote` | fails-quota | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://deepnote.com
- free tier: Free plan: 3 editors, 5 projects, Basic machine (5 GB RAM, 2 vCPU) unlimited. No free-tier disk figure is published anywhere on the pricing page or docs. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not published; no per-GB transfer price on the pricing page. | metered: no
- identity: email
- interface: rest, git
- limits:
  - per-object-cap (binding): 100 MB per file [1]
- limits note: 100 MB per file via the web upload UI; /work is object-storage-backed and slow for many small files; /tmp is fast but lost on restart; 7-day revision history on Free.
- interface detail: rest
- tooling: Notebook API, git sync, terminal; `/work` is a normal POSIX directory backed by object storage.
- composes with: 5 projects x (undisclosed GB) x N free accounts. The project cap is the hard multiplier ceiling.
- reliability: /work does persist across restarts (docs contrast it with /tmp, which 'will be lost when the machine restarts'), but the capacity is unpublished and the 5-project cap makes this uninteresting.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Free plan: 3 editors, 5 projects, Basic machine (5 GB RAM, 2 vCPU) unlimited. No free-tier disk figure is published anywhere on the pricing page or docs.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free: 3 editors, 5 projects, 'Basic (5 GB RAM, 2 vCPU) unlimited'
  - [2] 2026-10-21: '/work is backed by object storage'; '/tmp ... will be lost when the machine restarts'; 100 MB web upload cap
- sources:
  - [1] https://deepnote.com/pricing
  - [2] https://deepnote.com/docs/importing-data-to-deepnote
