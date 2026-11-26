# Burrowbox

> burrowbox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/burrowbox/ | JSON https://fshy.ajam.dev/api/v1/entity/burrowbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Burrowbox

- `compute/burrowbox` | qualifies-with-caveat | evidence documented | binding write-gated | category persistent desktop machine sandbox | tier tiny, prepaid credit
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T02:12:34.732Z (live) | stale on 2026-12-26
- url https://burrowbox.dev/
- free tier: Welcome credit: USD 1, added once your email is confirmed and your card is saved; machines cannot be started without a card on file with auto-refill. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The USD 1 is a one-time welcome credit, not a recurring allowance, and it is gated on both email confirmation and a saved card. A card on file with auto-refill is required to start any machine; without a card, creating or starting a machine returns 402.
- per-object cap: Not applicable: the unit is a machine, not an object. Machine sizes are tiny (0.5 vCPU, 4 GB RAM, 8 GB disk), small (1 vCPU, 6 GB, 12 GB), medium (2 vCPU, 8 GB, 16 GB) and large (4 vCPU, 12 GB, 20 GB). | source: [2]
- retention: A stopped machine keeps its entire filesystem snapshot, installed apps, browser profiles with cookies, and open windows and tabs until the user destroys it; stopped (snapshot) machines cost USD 0.001 per hour. | source: [2]
- egress: A VPN add-on is priced separately: Proxy at +USD 0.03/h and USD 10/GB, Unlock at +USD 0.06/h and USD 15/GB and USD 3 per 1k connections; no base egress allowance is stated on the billing page. | metered: yes | source: [1]
- identity: card | detail: Registration posts email, password and name (POST /api/auth/register) and sends a confirmation email; the billing page states the welcome credit is added once the email is confirmed and a card is saved, and that starting machines requires a card on file with auto-refill. No phone or ID document is stated.
- interface: rest, cli
- limits:
  - volume-quota: USD 1 one-time welcome credit, only after email confirmation and a saved card [1]
  - write-gated (binding): Without a card, creating or starting a machine returns 402; auto-refill charges the card when the balance falls below a chosen threshold (default USD 5) by a set amount (default USD 20) [1]
- limits note: Running machines are stopped when the balance reaches zero and their state is kept; admin accounts do not need a card.
- binding note: The card on file with auto-refill is the first gate: no card means no machine can start at all, even with welcome credit, and the credit itself is conditioned on the card being saved.
- interface detail: An MCP endpoint per machine plus a REST API (POST /api/machines, GET /api/machines/{id}/screenshot.jpg) and a dashboard; bearer tokens are API keys (tmk_), machine tokens (tmm_) or OAuth tokens (tmo_).
- endpoint: https://burrowbox.dev/api
- tooling: Any MCP client, including Claude Code and Cursor, connects over HTTP to a machine's MCP URL; a REST API and a web dashboard also drive machines.
- composes with: A machine's persistent browser logins and credential vault survive stop/start, so a long agent task can resume signed in; a per-machine token can be handed to a customer's agent while the platform key stays on the operator's server.
- reliability: A running machine with an empty balance is stopped and keeps its state; the whole disk is snapshotted on stop and a save point is taken every 30 minutes while running, so at most 30 minutes of change can be lost on a crash.
- notes: A persistent Linux desktop machine with a signed-in browser and credential vault, not a short-lived ephemeral sandbox. Price at the 2 vCPU/8 GB medium size is USD 0.16 per running hour, billed by the minute; a stopped snapshot is USD 0.001 per hour. The USD 1 welcome credit is a one-time credit gated on email confirmation and a saved card, and a card with auto-refill is required before any machine can start. The list price at 2 vCPU/4 GB would be USD 0.11/h on the small size, but the small has 1 vCPU/6 GB, so no 2 vCPU/4 GB shape is sold here.
- evidence note: Prices, credit, card gate and machine sizes are quoted from the vendor's billing, machines and authentication docs read on 2026-11-25; identity fields are from the registration API description on the same site.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 8
  - shape.disk_gib: 16
  - shape.note: the medium size; no GPU is offered
  - billing_model: prepaid credit charged by the minute with card auto-refill
  - free_tier_kind: one-time-credit
  - status: hosted, available
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.restart_required: no
  - session_cap.note: a machine can be always on, set to a TTL, or stopped with its disk snapshotted
- evidence:
  - [1] 2026-11-25: a one-time USD 1 welcome credit is given after email confirmation and saving a card | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: Welcome credit: $1, added once your email is confirmed and your card is saved.
  - [1] 2026-11-25: a saved card with auto-refill is required to start machines | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: To start machines you need a card on file with auto-refill: when your balance falls below a threshold you choose (default $5), the card is charged a set amount (default $20) and the credit is added right away.
  - [1] 2026-11-25: the medium machine is priced at USD 0.16 per running hour | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: medium | $0.16 / h | $115.20 |
  - [1] 2026-11-25: a stopped machine is billed USD 0.001 per hour | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: Stopped (snapshot) | $0.001 / h | $0.72 |
  - [2] 2026-11-25: the machine sizes and their CPU, RAM and disk allocations | capture: sha256:e034f065c9d02350e6050d91a994a4b225b09651c1c8a109d2029d6fbea82a7a | quote: size | `tiny` (½ vCPU, 4 GB RAM, 8 GB disk), `small` (1 vCPU, 6 GB, 12 GB), `medium` (2 vCPU, 8 GB, 16 GB), `large` (4 vCPU, 12 GB, 20 GB)
  - [3] 2026-11-25: registration asks for email, password and name and sends a confirmation email | capture: sha256:ad05247d173cd0771f0e258879a023a94d6432343d4f321489e2a1ad682dd39f | quote: POST | `/api/auth/register` | `email`, `password`, `name` | Creates the account and signs in. A confirmation email is sent.
  - [1] 2026-11-24: billing is prepaid credit charged by the minute | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: Burrowbox uses prepaid credit, charged by the minute.
  - [1] 2026-11-24: the tiny machine costs USD 0.07 per hour running, USD 50.40 per 30 days always on | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: | tiny | $0.07 / h | $50.40 |
  - [1] 2026-11-24: a one-time USD 1 welcome credit is added after email confirmation and saving a card | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: Welcome credit: $1, added once your email is confirmed and your card is saved.
  - [1] 2026-11-24: without a card, machine creation or start returns 402 | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: creating or starting a machine returns `402`
  - [1] 2026-11-24: a failed auto-refill charge pauses top-ups and running machines stop when the balance reaches zero | capture: sha256:96a21fde998b025b86c9b73464304763edd057b406a5ba655bea79436257a80a | quote: If a charge fails (declined, or the bank asks for authentication): auto-refill pauses and you get an email.
  - [4] 2026-11-24: sign-ups are invite-only and require an invited email | capture: sha256:8f00e18a9afe367d4c67a93e2fa5bfc46947c813294604710587fcb3c727a188 | quote: Sign-ups are invite-only right now.
  - [4] 2026-11-24: sign-up is free and a card is needed to run machines, with USD 1 of credit | capture: sha256:8f00e18a9afe367d4c67a93e2fa5bfc46947c813294604710587fcb3c727a188 | quote: Free to sign up. Add a card to run machines and get $1 of credit.
  - [4] 2026-11-24: the published rate is from 7 cents per hour running and 0.1 cents per hour stopped | capture: sha256:8f00e18a9afe367d4c67a93e2fa5bfc46947c813294604710587fcb3c727a188 | quote: From 7¢/h while running, 0.1¢/h while stopped.
  - [3] 2026-11-24: registration uses email, password and name, and sign-in and sign-up are rate-limited per IP and email | capture: sha256:ad05247d173cd0771f0e258879a023a94d6432343d4f321489e2a1ad682dd39f | quote: "POST" | "/api/auth/register" | `email`, `password`, `name`
  - [5] 2026-11-24: egress VPN add-on is charged USD 10.00 per GB for proxy and USD 15.00 per GB for unlock | capture: sha256:edd6e9d595626847046f6711d88dd9d2b61954f450a198a35e4232489f856bc2 | quote: | Traffic | $10.00 / GB | $15.00 / GB |
  - [2] 2026-11-24: a machine has a ttlMinutes deadline and onExpire stop or destroy behaviour | capture: sha256:e034f065c9d02350e6050d91a994a4b225b09651c1c8a109d2029d6fbea82a7a | quote: | `ttlMinutes` | number | none | Keep on for this long, then apply `onExpire` |
- sources:
  - [1] https://burrowbox.dev/docs/billing
  - [2] https://burrowbox.dev/docs/machines
  - [3] https://burrowbox.dev/docs/authentication
  - [4] https://burrowbox.dev/app/register
  - [5] https://burrowbox.dev/docs/vpn
