# Orgo

> orgo.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/orgo/ | JSON https://fshy.ajam.dev/api/v1/entity/orgo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Orgo

- `compute/orgo` | qualifies-with-caveat | evidence reported | binding write-gated | category container and VM sandbox
- needs card no, phone yes, ID no, institution no | verified 2026-11-24T13:21:00.908Z (live) | stale on 2026-12-09
- url https://www.orgo.ai/pricing
- free tier: a new account that passes the free checks gets USD 3 of starting credit, running one Medium Linux computer (2 vCPU, 8 GB RAM, 40 GB disk) at USD 0.055 per running hour and USD 0.0027 per stopped hour; the account can sign up free | unit: credits | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no charge per unit of traffic is published; bandwidth is capped at up to 100 Mbps on a Free account's hourly computer and up to 1,000 Mbps on a paid plan; paid plans include 1 to 20 GB of residential IP data a month and charge USD 3 per GB beyond the allowance | metered: no | source: [1]
- identity: email | detail: a human account signs in with an email address or a third-party identity; an anonymous agent signup is also documented, needing no email and no person present. The free checks apply per address, per email domain and per day, and a phone code or a card lifts them when they hold back the starting credit
- interface: rest, cli, ssh
- limits:
  - write-gated (binding): access is an API, SDK or MCP server; no plan or price appears on the extracted page [1]
- interface detail: HTTP API with Python and TypeScript SDKs, CLI (orgo), MCP server, and key-based SSH on paid plans (Linux only)
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes the product and its snapshot and clone verbs but publishes no plan or price in the extracted body, so the free-tier claim still rests on documented records card
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session clock published; a sandbox runs until it is stopped
  - persistent_storage.price: not stated
  - persistent_storage.durability: snapshot of a running computer
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: the snapshot
  - free_tier_kind: allowance
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Orgo provides cloud computers (virtual desktops) for AI agents. Provision a Linux desktop in seconds, drive it over the API/SDK or the hosted MCP server, and share, clone, or snapshot running computers.' quoted; the extracted body carries no plan and no price
  - [2] 2026-11-03: only a bandwidth rate is published for network, no volume allowance or price | capture: sha256:c9f1f936b7081e08c785b356f7be0888f7b9402ab6af7b82a7abe9fd25209bf8 | quote: A Free account's hourly computer runs at up to 100 Mbps.
  - [3] 2026-11-03: a REST HTTP API exists | capture: sha256:c34c764e50182aa017ad705666931988115f7c73b075592243d7356018d8c217 | quote: [API](https://docs.orgo.ai/api-reference/introduction.md). A plain HTTP API.
  - [4] 2026-11-03: SSH access exists, paid plans | capture: sha256:4ded39c609713c02f441d1a846e69a7834ec8c2584be2ad813682e7559ce908f | quote: Direct SSH (key access) - real key-based `sshd` access to Linux computers via your own keypair
  - [4] 2026-11-24: the free tier is USD 3 of starting credit gated by the free checks | capture: sha256:c568a3af3281e361f1ff2844205897bbe3feb7b9534f66735b8b205816767139 | quote: A new account gets $3 of starting credit the first time it is used signed in, if it passes the free checks below; if it does not, adding a card gets it.
  - [4] 2026-11-24: the free allowance is a credit balance (USD 3), not an unbounded plan | capture: sha256:c568a3af3281e361f1ff2844205897bbe3feb7b9534f66735b8b205816767139 | quote: A new account gets $3 of starting credit the first time it is used signed in, if it passes the free checks below; if it does not, adding a card gets it.
  - [4] 2026-11-24: free credit is drawn down by the running and stopped hours of the computer | capture: sha256:c568a3af3281e361f1ff2844205897bbe3feb7b9534f66735b8b205816767139 | quote: On the Free tier it runs one Medium Linux computer (2 vCPU, 8 GB RAM, 40 GB storage) billed by the hour: $0.055/hr while it runs and $0.0027/hr while it is stopped, so $3 is about 54 running hours.
  - [4] 2026-11-24: the only published per-GB traffic charge is for residential IP data, not general egress | capture: sha256:c568a3af3281e361f1ff2844205897bbe3feb7b9534f66735b8b205816767139 | quote: More data is $3 per GB from your Orgo credits or by card, in whole GB, up to 20 GB in one purchase.
  - [5] 2026-11-24: an agent signup path with no email exists; a human account still signs in by email | capture: sha256:08ae449392566a7dcf0d24a393584a21ee4896ee4f285f81f253b3a5f71eb3ff | quote: An agent can get its own account and API key in one call, with no email and no person present.
  - [5] 2026-11-24: the identity gate for an agent account is no email; the free checks are described on the pricing page | capture: sha256:08ae449392566a7dcf0d24a393584a21ee4896ee4f285f81f253b3a5f71eb3ff | quote: An agent can get its own account and API key in one call, with no email and no person present.
  - [4] 2026-11-24: the free tier is a USD 3 starting credit gated by the free checks | capture: sha256:c568a3af3281e361f1ff2844205897bbe3feb7b9534f66735b8b205816767139 | quote: A new account gets $3 of starting credit the first time it is used signed in, if it passes the free checks below; if it does not, adding a card gets it.
  - [4] 2026-11-24: the per-GB traffic charge applies to residential IP data beyond the included allowance | capture: sha256:c568a3af3281e361f1ff2844205897bbe3feb7b9534f66735b8b205816767139 | quote: More data is $3 per GB from your Orgo credits or by card, in whole GB, up to 20 GB in one purchase.
  - [5] 2026-11-24: an agent signup path with no email exists | capture: sha256:08ae449392566a7dcf0d24a393584a21ee4896ee4f285f81f253b3a5f71eb3ff | quote: An agent can get its own account and API key in one call, with no email and no person present.
  - [4] 2026-11-24: the paid plan includes real key-based SSH; the free tier uses VNC and API control | capture: sha256:c568a3af3281e361f1ff2844205897bbe3feb7b9534f66735b8b205816767139 | quote: - Direct SSH (key access) - real key-based `sshd` access to Linux computers via your own keypair, reachable over the IPv4 high-port fallback (`ssh -p <port> root@<host>`). Linux-only; distinct from the `orgo ssh` WebSocket terminal. Included on every paid plan.
  - [5] 2026-11-24: the API is the programmatic access path; rate limits are published on the plan page | capture: sha256:08ae449392566a7dcf0d24a393584a21ee4896ee4f285f81f253b3a5f71eb3ff | quote: An agent can get its own account and API key in one call, with no email and no person present.
  - [1] 2026-11-24: the product is a cloud computer driven over the API, SDK and hosted MCP server | capture: sha256:add6926a2662045e79aa91c8defd7b24ab37a48c61512c4ca88025d9dbaeaa98 | quote: Orgo provides cloud computers (virtual desktops) for AI agents. Provision a Linux desktop in seconds, drive it over the API/SDK or the hosted MCP server, and share, clone, or snapshot running computers.
  - [2] 2026-11-24: the free hourly computer is bandwidth-capped at 100 Mbps | capture: sha256:cb9067692a4560d540f3a3355631cf8d666ea43f17318f2d056d8cb24e551e33 | quote: A Free account's hourly computer runs at up to 100 Mbps.
- sources:
  - [1] https://www.orgo.ai/pricing
  - [2] https://docs.orgo.ai/guides/account-limits.md
  - [3] https://docs.orgo.ai/
  - [4] https://www.orgo.ai/pricing.md
  - [5] https://www.orgo.ai/auth.md
