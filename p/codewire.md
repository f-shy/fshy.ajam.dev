# Codewire

> codewire.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codewire/ | JSON https://fshy.ajam.dev/api/v1/entity/codewire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Codewire

- `compute/codewire` | paid-only | evidence documented | binding volume-quota | category cloud sandbox | tier Cloud (private beta, pay as you go)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.709Z (live) | stale on 2026-12-26
- url https://codewire.sh/pricing
- free tier: Local VMs are free forever. Cloud VMs bill per second, only while they run, with no plans and no seats. Local sandboxes are always free. In the cloud you pay only while your sandboxes run. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The only free capacity is local, on the user's own machine, and needs no account. The hosted cloud lane has no published free allowance: a card tops up €20 of credit when the balance is empty, with automatic €20 top-ups; the cloud lane is a private beta requiring a signup request. Rates are €0.0438 per vCPU-hour, €0.0141 per GB-hour of memory and €0.000087 per GB-hour of disk.
- per-object cap: not applicable: the billed unit is vCPU, memory and disk while a sandbox runs, not an object; a sandbox can have up to 16 vCPU, 32 GB memory and 200 GB disk | source: [1]
- retention: Storage is kept when a sandbox stops; running sandboxes stop after 24 hours without a card or a failed top-up, and their storage is kept. Credits do not expire. | source: [1]
- egress: not published: the pricing page states no egress allowance or price; outbound traffic passes through the credential proxy under per-sandbox network policies | metered: no | source: [1]
- identity: email | detail: The signup form asks for Name, Email and Password (at least 12 characters with uppercase, lowercase, a number and a symbol), then an optional invite code and 'What would you like to build?' for review; the cloud lane is a private beta accessed by request. Local VMs need no account. Billing needs a card to top up €20 of credit.
- interface: cli, ssh, rest
- limits:
  - volume-quota (binding): no hosted free allowance: a card tops up €20 of credit when the balance is empty, with automatic €20 top-ups [1]
  - retention-clamped: without a card or after a failed top-up, new sandboxes and starts are refused and running sandboxes stop after 24 hours [1]
  - volume-quota (binding): 10 sandboxes included on the cloud plan; several can run at once up to the organization's limit [1]
- limits note: A sandbox can have up to 16 vCPU, 32 GB of memory and 200 GB of disk on the calculator; the resources page permits up to 256 vCPU and 1 TiB of memory on a hosted sandbox. Disks only grow. Without a card, or if a top-up fails, new sandboxes and starts are refused at once, and running sandboxes stop after 24 hours. Human developer seats are USD 18 per developer per month; agents are not seats.
- binding note: The hosted lane has no free credit, so a balance topped up by card binds first, ahead of the 24-hour stop without a card and the organization's sandbox limit.
- interface detail: One CLI and SDK (TypeScript, Python, Go) drive local and cloud sandboxes with the same commands; cw info NAME shows a hosted sandbox's policy and enforcement status, preview URLs expose services, and SSH is available from any device.
- endpoint: https://codewire.sh
- tooling: the open-source Codewire CLI (curl -fsSL https://get.codewire.sh | sh), SDKs for TypeScript, Python and Go, and integrations for Rex, Orca, Claude, Codex, Cursor, Kimi, Pi and Gemini CLI.
- composes with: The hosted cloud lane is the offer for readers without their own machine: sandboxes run on private bare-metal machines in Amsterdam and Frankfurt, with a credential proxy and an encrypted agent-to-agent mesh. Running Codewire locally or on a Kubernetes cluster is the self-hosted last resort and is not the answer while the hosted lane is available.
- reliability: Hosted cloud is in private beta with an access-request form; without a card or after a failed top-up new sandboxes are refused and running ones stop after 24 hours; no published SLA.
- notes: Codewire sells hosted cloud sandboxes billed per second in a private beta, with no hosted free tier; only local VMs on the user's own machine are free. The hosted lane is the offer recorded here; the open-source CLI and Kubernetes control plane are a self-hosted last resort, not the answer while the hosted lane exists.
- evidence note: The hosted rates, free-local-only statement, 24-hour stop, top-up amount and signup fields are quoted from Codewire's own pricing and signup pages read 2026-11-25.
- self hosted: no
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 8
  - shape.disk_gib: 100
  - shape.gpu_class: not published
  - shape.gpu_count: 0
  - shape.note: the default cloud sandbox is 2 vCPU / 8 GB / 100 GB; sizes up to 16 vCPU, 32 GB and 200 GB are offered
  - billing_model: per-second vCPU, memory and disk charges drawn from a card-topped balance
  - free_tier_kind: none-hosted
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: named hosts and ports via network policy; preview URLs
  - session_cap.restart_required: no
  - session_cap.note: running sandboxes stop after 24 hours without card credit
- evidence:
  - [1] 2026-11-25: local sandboxes are always free and cloud sandboxes are billed only while running | capture: sha256:fc7b30ae37bbd1531b496a96908fdba68ebcd4234f6b1e85f05665b1a9a4bcf6 | quote: Local sandboxes are always free. In the cloud you pay only while your sandboxes run.
  - [1] 2026-11-25: the hosted vCPU rate is €0.0438 per vCPU-hour | capture: sha256:2132ecf0976305d0c1e07ea3570b30bc74bca29236f0765a489daca0a5db2856 | quote: <tr><td>vCPU</td><td class="m">€0.0438 per vCPU-hour</td>
  - [1] 2026-11-25: running sandboxes stop after 24 hours without a card or a failed top-up but storage is kept | capture: sha256:fc7b30ae37bbd1531b496a96908fdba68ebcd4234f6b1e85f05665b1a9a4bcf6 | quote: Without a card, or if a top-up fails, new sandboxes and starts are refused at once, and running sandboxes stop after 24 hours.
  - [2] 2026-11-25: the signup form asks for name, email, password and an optional invite code | capture: sha256:c1c788c6ca9532f4b510016d7e40e04436708fd5b2aaee05b9cb2593cac4d1b3 | quote: Invite code (optional)
  - [1] 2026-11-24: local VMs are free forever with no plans or seats and hosted VMs bill per second only while running | capture: sha256:7836e12ed1d249fc6c2866598e76db739ce49fc8bbc70aeb6ace589d0603b685 | quote: Local VMs are free forever. Cloud VMs bill per second, only while they run, with no plans and no seats.
  - [1] 2026-11-24: the per-second rate card is EUR 0.0438 per vCPU-hour, EUR 0.0141 per GB-hour of memory and EUR 0.000087 per GB-hour of disk | capture: sha256:de33267a107c7e6b3857ae3ed1b7dbeedf51385ec696fb7393811316da9694f7 | quote: <tr><td>vCPU</td><td class="m">€0.0438 per vCPU-hour</td><td class="m r" data-pricing-cost="cpu">€0.0876</td></tr>
  - [1] 2026-11-24: a default 2 vCPU and 8 GB sandbox costs EUR 0.2091 per hour and a month is 730 hours | capture: sha256:de33267a107c7e6b3857ae3ed1b7dbeedf51385ec696fb7393811316da9694f7 | quote: Billed per second on the sandbox’s size while it runs. A month is 730 hours.
  - [1] 2026-11-24: adding a card tops up EUR 20 of credit when the balance is empty, with automatic EUR 20 top-ups | capture: sha256:7836e12ed1d249fc6c2866598e76db739ce49fc8bbc70aeb6ace589d0603b685 | quote: Adding a card tops up €20 of credit when your balance is empty; automatic top-ups add €20 at a time.
  - [1] 2026-11-24: without a card, creates are refused at once and running sandboxes stop after 24 hours with storage kept | capture: sha256:7836e12ed1d249fc6c2866598e76db739ce49fc8bbc70aeb6ace589d0603b685 | quote: Without a card, or if a top-up fails, new sandboxes and starts are refused at once, and running sandboxes stop after 24 hours. Their storage is kept.
  - [1] 2026-11-24: the cloud plan includes 10 sandboxes at 2 vCPU and 8 GB RAM and 100 GB disk each | capture: sha256:7836e12ed1d249fc6c2866598e76db739ce49fc8bbc70aeb6ace589d0603b685 | quote: 10 sandboxes included
  - [3] 2026-11-24: a hosted sandbox may reach the public Internet and private, loopback, link-local and carrier-grade NAT ranges are excluded | capture: sha256:a30629bdede84e5b2e01b40b9f5b8a3e01c5500acf9969dbb95d792beaaff272 | quote: A hosted sandbox may reach the public Internet; private, loopback, link-local and carrier-grade NAT ranges are excluded.
  - [4] 2026-11-24: organization limits are 10 creates and starts per minute per person and 32 vCPU and 64 GiB across active sandboxes | capture: sha256:4a474c8b8cadea60824b2ba8fb132cb63f7f8c38c24c2faacbb38f0f4610c59c | quote: Creates and starts | 10 of each per minute, per person
  - [2] 2026-11-24: the signup form asks for a name, email, password, optional invite code and a free-text purpose | capture: sha256:c1c788c6ca9532f4b510016d7e40e04436708fd5b2aaee05b9cb2593cac4d1b3 | quote: Invite code (optional)
  - [2] 2026-11-24: the signup password must have at least 12 characters with uppercase, lowercase, a number and a symbol | capture: sha256:c1c788c6ca9532f4b510016d7e40e04436708fd5b2aaee05b9cb2593cac4d1b3 | quote: Use at least 12 characters with uppercase, lowercase, a number, and a symbol.
- sources:
  - [1] https://codewire.sh/pricing
  - [2] https://codewire.sh/signup
  - [3] https://codewire.sh/docs/networking/egress
  - [4] https://codewire.sh/docs/environments/resources
