# molab

> marimo.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/marimo/ | JSON https://fshy.ajam.dev/api/v1/entity/marimo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## molab

- `compute/molab` | qualifies | evidence documented | binding volume-quota | category notebook runtime | tier free public preview
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://docs.marimo.io/guides/molab/
- free tier: free: 4 CPUs and 32 GB RAM per notebook, an NVIDIA RTX Pro 6000 Blackwell with 96 GB VRAM attachable to any notebook, sessions up to 12 hours, 90-minute idle shutdown | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: No published monthly hour cap. The vendor says the service stays free while capacity is not oversubscribed.
- per-object cap: not applicable: the unit is a session, not an object
- retention: a limited amount of persistent storage per notebook; files uploaded through the sidebar or cached with mo.persistent_cache are persisted, subject to limits on file size and duration that may change at molab's discretion | source: [1]
- egress: no published egress allowance or price | metered: no | source: [1]
- identity: email | detail: a browser session at molab.new; the documentation describes no card and no phone step. Not stated explicitly as 'no card', so read as the absence of a stated gate rather than a documented one.
- interface: rest
- limits:
  - volume-quota (binding): 12 hours maximum session, 90 minutes idle shutdown, no published monthly cap [1]
- limits note: There is no published GPU-hours figure at all, and the vendor reserves both the price and the resource parameters, so the card can be withdrawn or resized with no notice period and no number a plan can be built on.
- binding note: nothing is metered, so nothing runs out on a schedule; the 12-hour session is the wall, and the vendor reserves the right to change the resources
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 96 GB VRAM card in a browser tab for 12 hours at a time is the largest single free GPU in evaluated offerings that needs only an email, and it composes with molab's GitHub mirroring to hold the notebook source outside the evaluation period.
- reliability: the vendor states the free service continues only while resources are not oversubscribed, so capacity is the risk rather than a counter
- notes: No monthly GPU-hour quota is published, which is the one number a planner needs. The idle rule (90 minutes) is far more generous than Colab's or Kaggle's, and 12 hours matches Colab's cap with much better hardware.
- evidence note: compute, GPU, session length and idle timeout are quoted from the vendor's docs page today. The absence of a card gate is inferred from the docs describing none.
- extras:
  - facets.class: enforcement
  - facets.free_tier_kind: public-preview
  - facets.shape.vcpu: 4
  - facets.shape.ram_gib: 32
  - facets.shape.gpu_class: RTX Pro 6000 Blackwell
  - facets.shape.gpu_count: 1
  - shape.vcpu: 4
  - shape.ram_gib: 32
  - shape.gpu_class: NVIDIA RTX Pro 6000 Blackwell
  - shape.gpu_count: 1
  - shape.note: the GPU is opt-in per notebook and comes with 96 GB VRAM
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00: public preview, no card
  - free_tier_kind: free-preview
  - unattended: no
  - unattended_mechanism: unverified: the docs describe no scheduler and no headless submit; a 90-minute idle shutdown implies the browser session must stay active
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: unstated
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.wall_clock_min: 720
  - session_cap.idle_reap_s: 5400
  - session_cap.restart_required: no
  - session_cap.note: 12 h maximum; 90 min idle shutdown
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-22: quoted: 'Notebooks can run for as long as 12 hours before molab shuts them down. Notebooks that are idle for more than 90 minutes are automatically shut down.'
  - [1] 2026-10-22: quoted: an NVIDIA RTX Pro 6000 Blackwell GPU with 96 GB of VRAM and 125 TFLOPS can be attached to any notebook; default 4 CPUs and 32 GB RAM; notebooks run as long as 12 hours; idle over 90 minutes shuts down
  - [2] 2026-06-01: quoted: the public preview of molab runs natively on CoreWeave Cloud with opt-in GPUs and 12 hour sessions
  - [3] 2026-09-01: forum report, translated: molab has an NVIDIA RTX Pro 6000 Blackwell in public beta limited to 12 hour sessions, and has no public IP interface, with tunnelling generally blocked, so it is training only rather than serving
  - [4] 2026-10-22: 
  - [2] 2026-10-22: 
  - [1] 2026-10-24: quoted: 'By default, each notebook runs with 4 CPUs and 32 GB of RAM.'
  - [1] 2026-10-24: quoted: 'You can attach an NVIDIA RTX Pro 6000 Blackwell GPU — with 96 GB of VRAM and 125 TFLOPS — to any notebook.'
  - [1] 2026-10-24: quoted: 'Notebooks can run for as long as 12 hours before molab shuts them down. Notebooks that are idle for more than 90 minutes are automatically shut down.'
  - [1] 2026-10-24: quoted, bold markers in the original: 'Is molab free? Yes.'
  - [1] 2026-10-24: quoted: 'Notebooks get a limited amount of persistent storage' — persisted only through the sidebar upload or mo.persistent_cache
  - [1] 2026-10-24: quoted: 'notebooks are public but undiscoverable by default'
- sources:
  - [1] https://docs.marimo.io/guides/molab/
  - [2] https://marimo.io/blog/reintroducing-molab
  - [3] https://linux.do/t/topic/2696589
  - [4] https://marimo.io/blog/newsletter-25

## molab (marimo cloud)

- `storage/molab` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://molab.marimo.io
- free tier: 'Notebooks get a limited amount of persistent storage'. Size deliberately undisclosed; 'Cached files are subject to limitations on file size and persistence duration, which may change at molab's discretion.'. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No published meter; notebooks are public and embeddable, so serving is expected behaviour. | metered: no
- identity: email
- interface: s3-compatible, rest
- limits note: 12 h max session; 4 CPUs / 32 GB RAM default; only sidebar-uploaded or cached files persist; retention 'at molab's discretion'.
- interface detail: rest
- tooling: marimo notebooks as Python files; server-backed preview; remote storage integrations (GDrive, HF, S3-compatible) rather than a real disk API.
- composes with: Per-notebook storage only, and only for files uploaded via the sidebar or written through `mo.persistent_cache`. No bulk upload path, so no chaining.
- reliability: Persistence exists but is explicitly discretionary and undocumented in size. Unusable as a storage substrate, fine as a free 32 GB-RAM compute box that can fetch and re-upload.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'Notebooks get a limited amount of persistent storage' — size deliberately undisclosed; 'Cached files are subject to limitations on file size and persistence duration, which may change at molab's discretion.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Notebooks get a limited amount of persistent storage'; 'subject to limitations on file size and persistence duration'
  - [1] 2026-10-21: '4 CPUs and 32 GB of RAM' default; 12 h sessions
- sources:
  - [1] https://docs.marimo.io/guides/molab/
