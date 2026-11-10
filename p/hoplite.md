# Hoplite

> hoplite.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hoplite/ | JSON https://fshy.ajam.dev/api/v1/entity/hoplite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hoplite

- `compute/hoplite` | qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-03T01:29:47.994Z (live) | stale on 2026-12-04
- url https://hoplite.sh
- free tier: Free plan at $0 a month: 'Run agents yourself, with a monthly usage allowance. Nothing charged.'; 5 concurrent cloud sessions and 5 projects; the allowance is drawn in credits, one credit being US$1 of usage; its dollar size is not published, and Free also has a daily limit | unit: credits | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: The allowance's dollar size is not published: 'Billing displays included usage as a percentage on every plan, including trials, rather than disclosing its dollar size.' Only part of it is usable per UTC day. Free sandboxes are clamped to Small (2 vCPU, 8 GiB, USD 0.16 an hour at the credit rate). https://hoplite.sh itself states no allowance.
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: not published | metered: no | source: [2]
- identity: card | detail: The Free plan needs a card that is not charged: a new workspace's signup opens a Stripe setup checkout for a billing address and card, and prepaid cards are not accepted. Repository access is through a GitHub App installation. Whether a phone number is asked is unverified: the public pages do not say.
- interface: rest, cli
- limits:
  - write-gated (binding): the Free plan allows 5 concurrent cloud sessions and 5 projects; at a usage limit work pauses until the limit resets or credits are added [2]
- interface detail: a REST API described by an OpenAPI specification, authenticated with a scoped API key sent as X-Api-Key or Bearer; an MCP server at https://api.hoplite.sh/mcp behind OAuth; a CLI published on npm as @usehoplite/cli
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page, the billing documentation and the site index were read on 2026-10-30: they publish the Free plan with a monthly allowance of undisclosed size, the card requirement, the sandbox rates and the access interfaces
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a thread runs in an isolated environment; the page states no clock
  - free_tier_kind: allowance
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: the site was read on 2026-10-22 and describes cloud coding agents whose threads work in isolated development environments, with a CLI that imports local history; it publishes no plan, price or free tier
  - [1] 2026-10-30: the Free plan at USD 0 carries a monthly usage allowance | capture: sha256:a318873201b2da384de5632ddd1d60e813c1662290c1b29fff2243740776e01c | quote: Run agents yourself, free — just you, with a monthly usage allowance. Nothing charged.
  - [1] 2026-10-30: usage beyond the allowance is drawn in credits of US$1 each, at token and sandbox rates | capture: sha256:a318873201b2da384de5632ddd1d60e813c1662290c1b29fff2243740776e01c | quote: One credit is US$1 of usage, at per-model token rates and per-size sandbox rates.
  - [3] 2026-10-30: the dollar size of the included allowance is not published | capture: sha256:25f3e3d2a73806b849472c3ae8def59d0b69a44839a0d4b8a97ed818dec295c0 | quote: Billing displays included usage as a percentage on every plan, including trials, rather than disclosing its dollar size.
  - [3] 2026-10-30: a Free sandbox is at most the Small size | capture: sha256:25f3e3d2a73806b849472c3ae8def59d0b69a44839a0d4b8a97ed818dec295c0 | quote: Sandboxes without a configured size are Medium, clamped to your plan (Free tops out at Small, Plus at Large).
  - [3] 2026-10-30: the Small sandbox is 2 vCPU and 8 GiB at USD 0.16 an hour | capture: sha256:25f3e3d2a73806b849472c3ae8def59d0b69a44839a0d4b8a97ed818dec295c0 | quote: | Small | 2 vCPU · 8 GiB | $0.16 |
  - [3] 2026-10-30: the Free allowance has a per-UTC-day ceiling | capture: sha256:25f3e3d2a73806b849472c3ae8def59d0b69a44839a0d4b8a97ed818dec295c0 | quote: Only part of the included allowance can be used per UTC day; purchased prepaid credits remain available after that daily ceiling is reached.
  - [1] 2026-10-30: the Free plan requires a card, which is not charged | capture: sha256:a318873201b2da384de5632ddd1d60e813c1662290c1b29fff2243740776e01c | quote: Card required — nothing charged
  - [3] 2026-10-30: signup saves a card and a billing address without charging them | capture: sha256:25f3e3d2a73806b849472c3ae8def59d0b69a44839a0d4b8a97ed818dec295c0 | quote: enrolling a new workspace opens a Stripe setup checkout for a billing address and card.
  - [3] 2026-10-30: a prepaid card does not pass the Free-plan card gate | capture: sha256:25f3e3d2a73806b849472c3ae8def59d0b69a44839a0d4b8a97ed818dec295c0 | quote: Prepaid cards are not accepted;
  - [2] 2026-10-30: repository access needs a GitHub App installation | capture: sha256:cdd6bfadae6c9579e008692c4e6a23633b7f953b89e41276f3c4b56d306db197 | quote: - Repository access is scoped through a GitHub App installation.
  - [1] 2026-10-30: work stops at a usage limit until it resets or credits are added; the same page lists 5 concurrent cloud sessions and 5 projects for Free | capture: sha256:a318873201b2da384de5632ddd1d60e813c1662290c1b29fff2243740776e01c | quote: At a usage limit, work pauses until it resets or you add credits.
  - [4] 2026-10-30: Hoplite publishes an OpenAPI contract for its API | capture: sha256:9503e95d529ca91a2b09a22e9fa391a36ec20aef5c34d0c8898cc1d8c5cae7fd | quote: [OpenAPI specification](https://hoplite.sh/openapi.json): Read the reviewed Hoplite API contract, operation schemas, and required permissions.
  - [4] 2026-10-30: the API takes a scoped API key as X-Api-Key or Bearer | capture: sha256:9503e95d529ca91a2b09a22e9fa391a36ec20aef5c34d0c8898cc1d8c5cae7fd | quote: [API authentication](https://hoplite.sh/docs/api/authentication): Create a scoped API key and send it using X-Api-Key or Bearer authentication.
  - [4] 2026-10-30: a CLI is published on npm and Homebrew | capture: sha256:9503e95d529ca91a2b09a22e9fa391a36ec20aef5c34d0c8898cc1d8c5cae7fd | quote: [CLI](https://hoplite.sh/docs/cli): Install the published @usehoplite/cli npm package or usehoplite/tap/hoplite Homebrew formula.
  - [1] 2026-11-03: the Free plan card carries a monthly usage allowance and no charge | capture: sha256:a4cc00f39ab21c9dcc9aab5fb793683b1e2622499fe060de69c17dcfdaf76d5e | quote: Run agents yourself, with a monthly usage allowance. Nothing charged.
  - [1] 2026-11-03: Free has a daily limit besides the monthly included usage; the page gives no dollar size for either | capture: sha256:a4cc00f39ab21c9dcc9aab5fb793683b1e2622499fe060de69c17dcfdaf76d5e | quote: Every plan includes model and sandbox usage each month, per seat on paid plans. Free also has a daily limit.
  - [3] 2026-11-03: the Free monthly allowance is stated in credits, with a five-project limit | capture: sha256:a57cc5985548f548988af2efe3e72068e542406450775c020658033ea892cea7 | quote: Free workspaces receive a monthly allowance of included credits and can have up to five projects.
  - [3] 2026-11-03: neither the monthly allowance nor the daily ceiling is published in dollars; billing shows a percentage | capture: sha256:a57cc5985548f548988af2efe3e72068e542406450775c020658033ea892cea7 | quote: Billing displays included usage as a percentage on every plan, including trials, rather than disclosing its dollar size.
- sources:
  - [1] https://hoplite.sh/pricing
  - [2] https://hoplite.sh
  - [3] https://hoplite.sh/docs/workspace/billing
  - [4] https://hoplite.sh/llms.txt
