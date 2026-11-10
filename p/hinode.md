# Hinode

> hinode.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hinode/ | JSON https://fshy.ajam.dev/api/v1/entity/hinode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hinode

- `compute/hinode` | trial-only | evidence documented | binding volume-quota | category GPU cloud | tier trial and prepaid GPU machines
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-03T07:36:21.683Z (live) | stale on 2026-12-04
- url https://hinode.run/
- free tier: a one-time trial: eligible new accounts get $10 to try after a $1 card check and refund, up to 7 days, on any GPU size on one machine; files are kept for 24 hours after the trial ends. Paid use is prepaid credit added from $10, billed by the minute: machines from $1.40 an hour for an L4 (24 GB) and $2.64 for an L40S (48 GB), up to $7.41 for a 96 GB RTX PRO 6000 with 256 GB of RAM. The page lists no H100, A100 or RTX 4090. | unit: credits | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: one-time
- per-object cap: not applicable: the unit is a machine-hour, not an object | source: [1]
- retention: files are kept for 24 hours after the trial ends; a paused machine keeps its disk as a snapshot, billed at $2.70 a month in the page's example, and deleting the machine ends that charge | days: 1 | source: [1]
- egress: traffic out is $0.10 per GB; disks are $0.15 per GB-month written and shared files $0.10 per GB-month | metered: yes | source: [1]
- identity: card | detail: the trial needs a $1 card check that is refunded: 'Eligible new accounts get $10 to try after a $1 card check and refund.' Paid credit is prepaid from $10; the payment methods for it, and any phone or ID check, are not stated on the page read.
- interface: ssh
- limits:
  - volume-quota (binding): the trial is $10 of credit on one machine for up to 7 days, about 4 hours 52 minutes on the smallest L4 before storage, traffic and the stop margin, subject to a daily trial allowance [1]
- limits note: the trial credit is the binding number; workspace and machines pause after 15 minutes with no input, no GPU work, no traffic and no running process
- binding note: the $10 trial credit, 7-day window and one machine bound the free route; paid use is prepaid per minute with no stated cap
- interface detail: the home page says to work over SSH, in VS Code or with an AI assistant, and an app catalog installs ComfyUI, PyTorch, JupyterLab, Ollama and vLLM in one click. No public API is documented on the page read.
- tooling: a cloud Linux workspace (a slice of an L4 at $0.24 an hour) plus attached whole-card machines of 24, 48 or 96 GB VRAM; SSH, VS Code, a desktop and Android app, and one-click ComfyUI, vLLM and Ollama installs. Machines pause themselves after 15 minutes idle.
- composes with: the trial is one machine for up to 7 days, so it fits a single short render or fine-tune run, not a standing service; the paused-machine disk is billed per month.
- reliability: unverified: no status page or incident history was read; the page lists limited regional availability (US and EU) as a drawback
- notes: the price grid also has 32, 64, 128 and 256 GB RAM columns: the L4 is $1.40 at 32 GB of RAM and $4.79 at 256 GB; the L40S is $2.64 at 32 GB and $6.38 at 256 GB.
- evidence note: the rates and the trial terms are read on the vendor's own home page on 2026-11-03
- evidence:
  - [1] 2026-11-03: the L4 machine starts at $1.40 an hour | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: MACHINE · 24 GB from$1.40/hr NVIDIA L4
  - [1] 2026-11-03: the L40S machine starts at $2.64 an hour | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: MACHINE · 48 GB from$2.64/hr NVIDIA L40S
  - [1] 2026-11-03: machines range from $1.40 to $7.41 an hour | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: Start the card the job needs. From $1.40 to $7.41 an hour.
  - [1] 2026-11-03: billing is prepaid by the minute and the trial needs a $1 card check | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: By the minute, from prepaid credit added from $10. Eligible new accounts get $10 to try after a $1 card check and refund.
  - [1] 2026-11-03: the trial is up to 7 days and files are kept 24 hours after it | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: The trial lasts up to 7 days; we stop before credit runs out and keep files for 24 hours after it ends.
  - [1] 2026-11-03: the trial is subject to a daily allowance | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: Eligible new accounts get $10 after a $1 card check and refund, subject to the daily trial allowance.
  - [1] 2026-11-03: storage and traffic prices | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: Disks are $0.15 per GB-month written, shared files $0.10 per GB-month, and traffic out $0.10 per GB.
  - [1] 2026-11-03: machines pause themselves when idle | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: The workspace and every machine pause themselves after 15 minutes with no input, no GPU work, no traffic and none of your processes running
  - [1] 2026-11-03: access is over SSH, VS Code or an AI assistant | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: Work over SSH, in VS Code or with your AI assistant.
  - [1] 2026-11-03: the 24 GB VRAM row of the price grid runs from $1.40 to $4.79 with RAM from 32 to 256 GB | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: | 24 GB VRAM | $1.40 | $1.89 | $2.19 | $4.79 |
  - [1] 2026-11-03: the 48 GB VRAM row of the price grid runs from $2.64 to $6.38 with RAM from 32 to 256 GB | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: | 48 GB VRAM | $2.64 | $3.17 | $4.24 | $6.38 |
  - [1] 2026-11-03: a paused machine's disk keeps billing at $2.70 a month in the page's example until the machine is deleted | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: What is on it keeps billing at $2.70/mo; deleting the machine is what ends that.
  - [1] 2026-11-03: the trial buys about 4 hours 52 minutes on the smallest L4 | capture: sha256:f741abd19b15eeca7fc9c74ba1a6e59f33e9d8342f1961121ffcfde8e7ba6a3f | quote: About 4 hours 52 minutes on the smallest L4, before storage, traffic and the stop margin.
  - [2] 2026-11-03: the price index lists an L40S at $2.64 an hour | capture: sha256:db0d7b440b53cf41f40dd3c7eff9d7cbd88ec8bc0c6be1f8b22d7483f9e14ca1 | quote: | [L40S](https://computeprices.com/providers/hinode/gpus/l40s)1× | $2.64/hr |
- sources:
  - [1] https://hinode.run/
  - [2] https://computeprices.com/providers/hinode
