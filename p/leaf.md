# Leafcloud

> leaf.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leaf/ | JSON https://fshy.ajam.dev/api/v1/entity/leaf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leafcloud

- `compute/leafcloud-run` | qualifies-with-caveat | evidence documented | binding volume-quota | category GPU cloud | tier Free Blackwell GPU Tier (Run)
- needs card yes, phone no, ID no, institution no | verified 2026-11-06T15:38:04.000Z (live) | stale on 2026-12-07
- url https://leaf.cloud/run
- free tier: 50 GPU hours a month, free, every month, on a dedicated 24GB VRAM slice of an RTX 6000 Pro Blackwell; the allowance is wall-clock metered while the slice is provisioned, renews monthly and does not carry over. Marked 'Coming Soon'. | unit: gpu-hours | metered on: wall-clock | read on: 2026-11-06 | source: [1] | note: Not open yet: the page reads 'Coming Soon' and carries a waitlist, and the Run sign-up page says sign-up is not available yet. A month is 730 hours, so the allowance is 50 of them.
- per-object cap: not applicable
- retention: Persistent storage is included with the server; a free slice that sits idle is warned and then reclaimed, and free slices are preemptible. | source: [1]
- egress: Not stated for the free tier: the page publishes no egress allowance and no egress price, so nothing is known to be charged per gigabyte and nothing is promised free. | metered: no | source: [1]
- identity: card | detail: The Run sign-up form asks for first name, last name, email and password; the free tier requires a EUR 0 card check or a 1-cent iDEAL verification from a non-disposable card, with no charge and no subscription. The general Leafcloud cloud signup is a separate flow that asks a EUR 2 downpayment and a EUR 200 GPU deposit, and the free-tier page does not say whether the free tier inherits it.
- interface: ssh
- limits:
  - volume-quota (binding): 50 GPU hours a month, wall-clock metered while the slice is provisioned; usage past 50 hours is billed at EUR 0.49 per GPU hour [1]
- limits note: Free slices are preemptible with no SLA, and a slice that sits idle is warned and then reclaimed. One account per person; free hours do not stack or carry over between months.
- binding note: The 50-hour monthly allowance is what runs out first: it is 50 of the 730 hours in a month, and past it the meter runs at EUR 0.49 a GPU hour.
- interface detail: SSH with root and Docker on a dedicated GPU slice; no console, API or CLI is documented for the free tier.
- tooling: an SSH client and Docker; the one-click images ship Open WebUI + Ollama, vLLM and JupyterLab + PyTorch.
- composes with: 50 hours a month on a 24GB Blackwell slice is a fine-tuning and inference bench; because a free slice is preemptible and reclaimed when idle, a job that must survive reclamation needs its checkpoints written to a separate object-storage record.
- reliability: Free slices are preemptible with no SLA and an idle slice is warned then reclaimed; the vendor states it may end the freemium model at any time, and the tier is marked 'Coming Soon' with sign-up not yet available.
- notes: The free tier is announced but not open: the page reads 'Coming Soon' and the Run sign-up page says 'Sign up is not available yet. Log in if you already have an account.' The paid alternative on the same infrastructure is the RTX 6000 Blackwell 1x flavor at EUR 1452.7 a month. The general cloud's own GPU gate is a EUR 200 deposit with 48 hours of free use, a separate offer from this monthly allowance.
- evidence note: The quota, the 24GB slice, the overage price, the card check and the preemption terms are quoted from the vendor's free-tier page read on 2026-11-06; the 'Coming Soon' state is on the same page and the disabled sign-up is in the Run sign-up page's own text.
- extras:
  - shape.gpu_class: NVIDIA RTX 6000 Pro Blackwell (24GB VRAM slice)
  - shape.note: a dedicated 24GB VRAM slice of an RTX 6000 Pro Blackwell; vCPU, RAM and disk are not stated on the free-tier page
  - billing_model: monthly free allowance with per-hour overage
  - free_tier_kind: recurring-allowance
  - term: monthly, no commitment
  - price_arithmetic: 50 GPU hours free a month; past 50 hours, EUR 0.49 per GPU hour
  - status: announced, waitlist only; sign-up not yet available
  - network_out.allow_outbound: yes
  - network_out.ports: not stated for the free tier
  - session_cap.restart_required: no
  - session_cap.note: an idle slice is warned and then reclaimed; free slices are preemptible
- evidence:
  - [1] 2026-11-06: the free tier is 50 GPU hours a month, free, every month | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: 50 GPU hours a month. Free, every month.
  - [1] 2026-11-06: each free slice is a dedicated 24GB VRAM slice of an RTX 6000 Pro Blackwell | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: A dedicated 24GB VRAM slice of an RTX 6000 Pro Blackwell.
  - [1] 2026-11-06: the allowance is wall-clock metered while the slice is provisioned, resets monthly and does not expire mid-cycle | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: 50 GPU hours, every month. Wall-clock metered while your slice is provisioned, just like on-demand billing. The allowance resets monthly and never expires mid-cycle.
  - [1] 2026-11-06: a card check from a non-disposable card is required, either a EUR 0 card verification or a 1-cent iDEAL payment | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: A card check is required from a non-disposable card. A €0 card verification or 1-cent iDEAL payment.
  - [1] 2026-11-06: usage past 50 hours is billed at EUR 0.49 per GPU hour to the card on file | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: Usage past 50 hours is billed automatically at €0.49 per GPU hour to the card on file.
  - [1] 2026-11-06: free slices are preemptible with no SLA, and an idle slice is warned and then reclaimed | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: Free slices are preemptible. There is no SLA on the free tier. If your slice sits idle we warn you, then reclaim it.
  - [1] 2026-11-06: one account per person, and free hours do not stack or carry over between months | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: Once you reach 50 hours, your instance pauses. Billing never starts without your explicit go-ahead. If you choose to continue, you pay €0.49 per GPU-hour beyond the free tier. Important: you get one account per person, and free hours don't stack or carry over between months.
  - [1] 2026-11-06: the freemium model is a pilot the vendor may end at any time | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: Our freemium model is a pilot, to test if it provides real value for our users. We retain the right to end this model at any time.
  - [1] 2026-11-06: the tier is marked Coming Soon | capture: sha256:76f8563d163ffca044ec96d12de652738cb812c509adbb8bf08969a419fcb5e7 | quote: Coming Soon. Free Blackwell GPU Tier
  - [2] 2026-11-06: the Run sign-up page states sign-up is not available yet | capture: sha256:a6a0d6377f0b3c80b63f95c05c5a255df4b28faf79d6a000b84cb6e4f4d62128 | quote: Sign up is not available yet. Log in if you already have an account.
  - [2] 2026-11-06: the sign-up form asks for an email address and a password; the same script defines First name and Last name fields | capture: sha256:a6a0d6377f0b3c80b63f95c05c5a255df4b28faf79d6a000b84cb6e4f4d62128 | quote: id:"email",label:"Email",type:"email"
  - [3] 2026-11-06: the general cloud registration asks a EUR 2 downpayment and a EUR 200 GPU deposit | capture: sha256:2b52a04591a2610ccb206864c1b318aa41a03ff1acd88949acafe55d7a878506 | quote: Leafcloud requires a €2 downpayment to access Leafcloud cloud resources and a €200 downpayment to enable the use of GPUs.
  - [3] 2026-11-06: the free tier's verification is a EUR 0 card check or a 1-cent iDEAL payment, with no charge | capture: sha256:2b52a04591a2610ccb206864c1b318aa41a03ff1acd88949acafe55d7a878506 | quote: We require a €0 card check or 1-cent iDEAL verification to unlock your free tier.
  - [4] 2026-11-06: the paid RTX 6000 Blackwell 1x flavor is EUR 1452.7 a month | capture: sha256:6e96a5c467693d538481a27a9568ad25a0f2c89140dbce8b652ea796f2e4eca7 | quote: | eg2.rtxp6000x1.V32-256-860 | NVIDIA RTX 6000 Blackwell | 600 | 1 | €1452.7 |
- sources:
  - [1] https://leaf.cloud/run
  - [2] https://run.leaf.cloud/_next/static/chunks/app/signup/page-34bc1d1029ce2b9d.js
  - [3] https://leaf.cloud/faq/
  - [4] https://leaf.cloud/pricing
