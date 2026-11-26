# Epho

> epho.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/epho/ | JSON https://fshy.ajam.dev/api/v1/entity/epho.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Epho

- `compute/epho` | qualifies-with-caveat | evidence documented | binding volume-quota | category agent sandbox | tier usage-based agent sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-25T02:12:34.751Z (live) | stale on 2026-12-26
- url https://epho.io/
- free tier: USD 10 of starting credit on signup, roughly 60 hours of the default 2 vCPU/2 GiB instance; OpenCode Zen models ending in -free need no provider key. | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: The USD 10 is a one-time starting credit, not a recurring allowance; it is consumed by sandbox compute at the published per-second rates.
- per-object cap: not applicable: the unit is a sandbox, not an object | note: Up to 20 input files and 32 repositories per request are documented; no storage object cap is published.
- retention: A chat's sandbox stops when a turn ends and resumes for the next one; files and agent session survive. Artifact download URLs are presigned for about ten minutes and renewable. | source: [1]
- egress: Not published as a volume or price; the sandbox runs on the vendor's boxes and artifacts return as presigned URLs. | metered: no | source: [1]
- identity: email | detail: A team API key is required and, per a third-party review, sign-up involves email verification. The exact fields of the registration form were not read: the app.epho.io registration page redirected to sign-in and presented a login wall to every reader.
- interface: rest, chat
- limits:
  - volume-quota (binding): USD 10 starting credit on signup; a turn is refused with 402 at zero balance [1]
  - request-rate: teams start with five active turns; extra turns queue at no cost until a slot opens [1]
  - per-object-cap: up to 32 repositories and 20 input files per request [1]
- limits note: A run is metered from boot to teardown and stops when the run does; one live turn per chat.
- binding note: The USD 10 starting credit is the first allowance to run out; the five-turn active limit is a concurrency gate that queues rather than stops work.
- interface detail: One REST endpoint POST /api/v1/chat plus /chat/async, streaming server-sent events and a chat_id for a durable multi-turn sandbox; MCP servers and repository tokens are declared in the request.
- endpoint: https://app.epho.io/api
- tooling: A single HTTP POST with a JSON body and an API key; no SDK or daemon is required.
- composes with: Runs can be driven from scripts, CI, cron or a Slack bot, and model tokens bill to the caller's own provider key with no Epho markup.
- reliability: A dropped stream does not kill a run: events are persisted and replayed on reconnect; the platform re-queues a run on a fallback sandbox backend when a box dies mid-run.
- notes: A hosted coding-agent sandbox sold per second: USD 0.0000438/s for the default box and USD 10 of starting credit. The registration form was behind a login wall, so its exact fields are unverified; a third party reports email verification.
- evidence note: Per-second rates and credit are quoted from the vendor home page read on 2026-11-25; the email-verification step is reported by a third party because the registration page was a login wall.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.disk_gib: 10
  - shape.note: default instance 2 vCPU, 2 GiB RAM, 10 GiB disk; other sizes available via the instance field
  - billing_model: per-second compute, prepaid credit
  - free_tier_kind: one-time credit
  - term: per-second, no recurring free allowance
  - price_arithmetic: 2 × $0.0000164 + 2 × $0.0000053 + 10 × $0.000000036 = $0.0000438 per second; $10 / $0.0000438 ≈ 228,310 s ≈ 63.4 h
  - status: live
  - network_out.allow_outbound: yes
  - session_cap.restart_required: no
  - session_cap.note: sandbox stops at the end of a turn and resumes for the next one; model tokens bill on the caller's own provider key
- evidence:
  - [1] 2026-11-25: CPU price per vCPU-second | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: $0.0000164
  - [1] 2026-11-25: memory price per GiB-second | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: $0.0000053
  - [1] 2026-11-25: disk price per GiB-second | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: $0.000000036
  - [1] 2026-11-25: the default instance and its per-second cost | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: default instance: 2 vCPU · 2 GiB · 10 GiB ≈ $0.0000438/s · a one-minute run ≈ $0.0026
  - [1] 2026-11-25: the starting credit | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: starting credit: $10 on signup — roughly 60 hours of the default instance
  - [1] 2026-11-25: free model option without a provider key | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: the opencode zen models ending in `-free` run without any provider credential. one epho key and a curl is the entire setup.
  - [1] 2026-11-25: balance gate | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: the meter: read it any time with GET /credits — a turn is refused with 402 once the balance hits zero.
  - [1] 2026-11-25: active-turn limit | capture: sha256:984d0647ee7a1df2e96177a43b4da653a07b577239ca3568821c47ea6b1d7593 | quote: yes — each chat gets its own isolated environment, so fan out as wide as you like. teams start with five active turns; anything past the cap sits in a queue, emits a `queued` status and costs nothing until a slot opens. one live turn per chat, though — parallel work wants parallel chats.
  - [2] 2026-11-25: third-party account of the signup gate | capture: sha256:36f91cf5209d58478a3e5707587f5024ad7e7b05b4b494b9a647b905d37ae5e1 | quote: - $10 free compute credit upon sign-up and email verification
  - [1] 2026-11-24: the default instance is 2 vCPU, 2 GiB, 10 GiB at about 0.0000438 dollars per second and one minute costs about 0.0026 dollars | capture: sha256:a686287037676a31329a2c2ba42a08bbc70b02102b4aa933836e465cfd0a63e6 | quote: default instance: 2 vCPU · 2 GiB · 10 GiB ≈ $0.0000438/s · a one-minute run ≈ $0.0026
  - [1] 2026-11-24: a 10-dollar start credit is granted on signup, about 60 hours of the default instance | capture: sha256:a686287037676a31329a2c2ba42a08bbc70b02102b4aa933836e465cfd0a63e6 | quote: starting credit: $10 on signup — roughly 60 hours of the default instance
  - [1] 2026-11-24: CPU is 0.0000164 dollars per vCPU-second and memory 0.0000053 dollars per GiB-second | capture: sha256:a686287037676a31329a2c2ba42a08bbc70b02102b4aa933836e465cfd0a63e6 | quote: cpu $0.0000164 per vCPU · per second
  - [1] 2026-11-24: model tokens are never billed by Epho and ride on the caller's provider key at the provider price | capture: sha256:a686287037676a31329a2c2ba42a08bbc70b02102b4aa933836e465cfd0a63e6 | quote: model tokens: never billed by epho. they ride on your provider_api_key, at your provider's price.
  - [1] 2026-11-24: a turn is refused with 402 once the credit balance reaches zero | capture: sha256:a686287037676a31329a2c2ba42a08bbc70b02102b4aa933836e465cfd0a63e6 | quote: the meter: read it any time with GET /credits — a turn is refused with 402 once the balance hits zero.
  - [1] 2026-11-24: nothing idles, is stored or keeps billing after a run; produced artifacts come back on a presigned URL good for about ten minutes | capture: sha256:a686287037676a31329a2c2ba42a08bbc70b02102b4aa933836e465cfd0a63e6 | quote: anything the agent produces comes back as artifacts with a presigned download url, good for about ten minutes and re-mintable from the response endpoint.
  - [3] 2026-11-24: the default team cap is five active turns and extra work stays queued | capture: sha256:9ebc8ad20402ee2886272e561e1bf20620cd24fbfd7b554a64562becc3c64e98 | quote: Teams can run multiple chats concurrently. The default team cap is five active turns; work above the cap stays queued and emits the `queued` phase.
  - [4] 2026-11-24: an account and a team API key are required before the first request; the provider key is separate | capture: sha256:c61675c36d8d043636f87e3d56c2240ce90a560746100edb63464f4104836a5e | quote: Create an account at [app.epho.io](https://app.epho.io/), open the API keys page, and create a team key.
  - [5] 2026-11-24: the registration form asks for Name, Email address, Password and Confirm password, with Google and GitHub options and no phone or card field | capture: sha256:798f0fc2a234090039221b90b9a2d8a388edbe6082739c57e6a046db194a28f0 | quote: [Google](https://web.archive.org/web/20261011144051/https://app.epho.io/auth/google/redirect) [GitHub](https://web.archive.org/web/20261011144051/https://app.epho.io/auth/github/redirect)
  - [6] 2026-11-24: the API is team-scoped and every run is a turn inside a durable chat; the sandbox is stopped so compute billing ends | capture: sha256:d01d63ad5b1f5f306feeef11c46970c25adaed424b7db1455c37c2cd5c27db5c | quote: Epho accepts a team-scoped API key.
- sources:
  - [1] https://epho.io/
  - [2] https://techshark.io/tools/epho/
  - [3] https://epho.io/docs/chats-and-turns
  - [4] https://epho.io/docs/quickstart
  - [5] https://web.archive.org/web/20261011144051/https://app.epho.io/register
  - [6] https://epho.io/docs
