# AgentComputer

> agentcomputer.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/agentcomputer/ | JSON https://fshy.ajam.dev/api/v1/entity/agentcomputer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AgentComputer

- `compute/agentcomputer` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:17:39.261Z (live) | stale on 2026-12-26
- url https://agentcomputer.ai/pricing
- free tier: no free tier: pay-as-you-go at $0.07 a CPU-hour, $0.04375 a GB-hour of memory, and storage at $0.000683 a GB-hour running or $0.000027 stopped | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: ssh, cli, browser
- limits:
  - request-rate (binding): $0.07 a CPU-hour and $0.04375 a GB-hour of memory while the machine runs [1]
  - retention-clamped: storage is billed at $0.000683 a GB-hour running and $0.000027 stopped, so a stopped machine still costs 4% of its running storage rate [1]
- interface detail: The computer-guest image ships with browser access and SSH; the user installs the `computer` CLI and signs in through a browser flow that stores a local API key.
- tooling: the user installs the `computer` CLI with the staging installer (`curl -fsSL https://agentcomputer.ai/install.sh | bash`), signs in with `computer login`, connects with `computer ssh` and `computer open --vnc`, and publishes ports with `computer ports publish`
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes a full usage ladder with no free tier. The record claimed a free tier from the card, which the page contradicts, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page prices a stopped state separately, so stopping is supported and is not a reap
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: $0.000683 a GiB-hour running, $0.000027 stopped
  - ps.durability: billed storage in both states
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the storage is billed
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'CPU Time $0.07 per CPU-hour · Memory $0.04375 per GB-hour · Hot Storage $0.000683 per GB-hour (running) · Cold Storage $0.000027 per GB-hour (stopped)', quoted; the page publishes no free tier
  - [1] 2026-11-25: the pricing table gives only pay-as-you-go rates and no free tier | capture: sha256:f2386cb76a1ff3f84db8fa6f63566281cc675a38062d7f81decebc23160b06f4 | quote: | CPU Time | $0.07 per CPU-hour | | --- | --- | | Memory | $0.04375 per GB-hour | | Hot Storage | $0.000683 per GB-hour (running) | | Cold Storage | $0.000027 per GB-hour (stopped) |
  - [1] 2026-11-24: the pricing page lists pay-as-you-go meters with no free plan | capture: sha256:f2386cb76a1ff3f84db8fa6f63566281cc675a38062d7f81decebc23160b06f4 | quote: Pay-as-you-go pricing based on actual resource usage
  - [2] 2026-11-24: every computer is preconfigured with browser access and SSH, so the interface is not unknown | capture: sha256:3b4f4ccdbb55d156832b1e6199ee0c2678439bda2946a9509b40c346af00dac8 | quote: Every computer boots from the [computer-guest](https://github.com/AgentComputerAI/computer-guest) image as root fs, which comes pre-configured with browser access, SSH, and everything agents need.
  - [2] 2026-11-24: the documented access surfaces are a browser and SSH | capture: sha256:3b4f4ccdbb55d156832b1e6199ee0c2678439bda2946a9509b40c346af00dac8 | quote: Use the browser for the primary surface, or SSH when you want a terminal-first workflow.
  - [2] 2026-11-24: a `computer` CLI is installed and used, with a browser sign-in that stores a local API key | capture: sha256:3b4f4ccdbb55d156832b1e6199ee0c2678439bda2946a9509b40c346af00dac8 | quote: Run `computer login` to open the browser sign-in flow and store a local API key for later CLI requests.
- sources:
  - [1] https://agentcomputer.ai/pricing
  - [2] https://agentcomputer.ai/docs
