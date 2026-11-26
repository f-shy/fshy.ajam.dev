# Blue Claw

> blueclaw.network | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blueclaw/ | JSON https://fshy.ajam.dev/api/v1/entity/blueclaw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blue Claw

- `inference/blueclaw` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://blueclaw.network
- free tier: No free allowance is stated. Sign in with an email 6-digit code, then buy prepaid USD credits in the console; per-request pricing is metered against a live price sheet. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign in with an email address and a 6-digit code, then buy prepaid credits; no password
- interface: rest
- limits:
  - volume-quota (binding): prepaid USD credits metered against a live per-model price sheet [1]
- endpoint: https://openai.blueclaw.network/v1
- tooling: an OpenAI-compatible base URL with streaming, tool calling and open-model presets
- composes with: the prepaid credit purchase is the scarce link; there is no standing free tier
- reliability: no content logging by default; limited operational metadata retained for abuse prevention and billing; no TEE, E2EE or confidential-compute guarantee yet
- notes: no standing free text allowance; an email code is needed to sign in and prepaid credits to make requests
- evidence:
  - [1] 2026-11-18: sign-in is a 6-digit email code with no password; making requests then requires buying prepaid credits | capture: sha256:e5af2f9927a4dc68aa7e547b61aa9e33156000d993b0f22ba26abd76c6162775 | quote: Sign in with your email — we send a 6-digit code, no password — then buy prepaid credits in the console to start making requests.
- sources:
  - [1] https://blueclaw.network
