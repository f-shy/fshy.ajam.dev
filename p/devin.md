# Devin

> devin.ai | Coding subscriptions, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/devin/ | JSON https://fshy.ajam.dev/api/v1/entity/devin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Devin

- `coding-subs/devin` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-10T01:56:02.007Z (live) | stale on 2026-12-11
- url https://devin.ai/pricing
- free tier: Free: USD 0, 'Light quota to code with agents', limited model availability, Unlimited inline edits, Unlimited Tab completions | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the free tier's agent allowance is the word 'light' and no number. The two components with a number are the two that are unlimited, which is the inverse of what a reader needs
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: the paid ladder is bought with a card; the Free plan is USD 0 and the page does not state a card at signup
- interface: rest, cli
- limits:
  - request-rate (binding): the Free plan's agent quota is described as 'Light quota to code with agents' with no number; Pro 'Increased quotas', Max 'Significantly higher quotas' [1]
- limits note: no plan on the ladder states a countable allowance for agent work. Inline edits and Tab completions are stated as unlimited on Free, which is a documented absence and not a limit. Paid plans refresh their allowance on a daily and weekly basis; no window is stated for the Free plan's light quota
- binding note: the unpublished agent quota binds before anything else, because it is discretionary and there is no number to design against
- interface detail: a web application, a desktop client, a command-line client and a REST API: docs.devin.ai documents the Devin API at https://api.devin.ai/v3/organizations/*, reached with a service-user key, and Devin CLI, a local command-line coding agent
- tooling: a script reaches the agent through the Devin API with a service-user key (Authorization: Bearer), creating a session at POST https://api.devin.ai/v3/organizations/ORG/sessions; Devin CLI runs a local command-line agent from the same vendor
- composes with: the agent allowance is the scarce link: it is discretionary and unpublished, so it cannot be sized before it is spent
- reliability: no reliability event recorded
- notes: The page was live the whole time: a raw fetch returns 200 with 582848 bytes and the full ladder. The distinction the verdict vocabulary exists to carry is dead versus paid-only versus free-with-a-discretionary-allowance, and this is the third. The free agent quota is the word 'light', so the row is qualifies-with-caveat rather than qualifies. Whether a script can drive it is not established: the page advertises a desktop client and no API key.
- evidence note: the ladder, the prices and the Free plan's four stated features are quoted from devin.ai/pricing read 2026-10-22 at 200, 582848 bytes.
- evidence:
  - [1] 2026-10-22: the full ladder: Free USD 0 'Light quota to code with agents', Unlimited inline edits, Unlimited Tab completions; Pro USD 20 a month; Max USD 200 a month; Teams USD 80 a month for the team plan plus USD 40 a month per full dev seat. The page is 582848 bytes at HTTP 200 and carries a 'Compare Plans Free $0/month Pro $20/month Max $200/month Team $80/month' row
  - [1] 2026-10-30: the Free plan is unchanged: a light agent quota with no number, unlimited inline edits and unlimited Tab completions | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: The Free plan includes a light quota to code with agents, limited model availability, unlimited inline edits, and unlimited Tab completions.
  - [1] 2026-11-03: the paid-plan allowance has a daily and a weekly window; the Free plan's window is not stated | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: Each paid plan comes with a usage allowance that refreshes automatically on a daily and weekly basis.
  - [1] 2026-11-03: the Free plan is still USD 0 with a light, unnumbered agent quota | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: The Free plan includes a light quota to code with agents, limited model availability, unlimited inline edits, and unlimited Tab completions.
  - [2] 2026-11-09: Devin publishes a REST API that a client can call | capture: sha256:4af7207085855d3d31e9c285f65254de40f1acd228babdd96ab334b11a2aa9b1 | quote: The Devin API enables you to integrate Devin into your applications, automate workflows, and build powerful tools.
  - [3] 2026-11-09: Devin publishes a command-line client | capture: sha256:6285771ae8284453eb34130daee78a9a18e4af014378b10abab9f05ae5673193 | quote: Get up and running in 2 minutes with Devin CLI, a local command-line coding agent with deep Devin Cloud integration.
  - [2] 2026-11-10: the API reference documents a REST API at api.devin.ai/v3/organizations/* | capture: sha256:9a8deaa427e5ff0bb435b3b28d3b49c90f6dc5954fb83f47f29fef866e2d2157 | quote: The Devin API enables you to integrate Devin into your applications, automate workflows, and build powerful tools.
- sources:
  - [1] https://devin.ai/pricing
  - [2] https://docs.devin.ai/api-reference/overview
  - [3] https://docs.devin.ai/cli/index.md

## Devin , including

- `compute/devin-including` | qualifies-with-caveat | evidence documented | binding request-rate | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:40:18.802Z (live) | stale on 2026-12-05
- url https://devin.ai/pricing
- free tier: Devin Free: "Free $0", "Light quota to code with agents", "Limited model availability", "Unlimited inline edits", quoted from the 2026-10-01 capture of the pricing page | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: cli, rest
- limits:
  - request-rate (binding): the quota is real but unpublished, so the first failure is a quota message with no number in it. [1]
- limits note: the quota is real but unpublished, so the first failure is a quota message with no number in it.
- binding note: the same as limits note
- interface detail: REST API at api.devin.ai/v3 with service-user tokens; Devin CLI installed by a shell script; the web app
- tooling: Devin CLI (cli.devin.ai); the REST API is called with curl
- composes with: Devin Free plus DeepWiki is a free way to read an unfamiliar repository, which is the expensive first hour of any new codebase; the agent quota is too small to build anything.
- reliability: no reliability event recorded
- notes: Windsurf no longer has a pricing page of its own; windsurf.com/pricing redirects to devin.ai/pricing, so one account covers both brands. The capture also records "Free use of SWE-2 Free in Devin Desktop and CLI through October 16, 2026", a promotional window that closed six days before this read. No quota count is published for Free, which is the missing number.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: recurring-allowance
- evidence:
  - [2] 2026-10-22: the Wayback capture of devin.ai/pricing from 2026-10-01 gives Free at $0 with a light quota, limited model availability and unlimited inline edits, quoted
  - [3] 2026-10-22: the Free plan "lets you try Devin with limited usage. It includes: Limited Devin usage, Access to Devin Review, Access to DeepWiki", quoted
  - [4] 2026-10-22: 
  - [1] 2026-11-03: the pricing page meters usage, not egress, and states no egress allowance or price | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: Purchase extra usage at API pricing
  - [5] 2026-11-03: a REST API exists | capture: sha256:4af7207085855d3d31e9c285f65254de40f1acd228babdd96ab334b11a2aa9b1 | quote: Learn how to programmatically interact with Devin using our REST APIs
  - [6] 2026-11-04: the docs document the Devin CLI | capture: sha256:3afe74679cc6d006064e740d2cfe9fdae6486df6cd60302e286f1fc65182866a | quote: You can also install [Devin CLI](https://docs.devin.ai/cli.md) to use Devin directly from your command line:
  - [5] 2026-11-04: the API overview documents the REST API; the quickstart calls it with curl | capture: sha256:4af7207085855d3d31e9c285f65254de40f1acd228babdd96ab334b11a2aa9b1 | quote: Learn how to programmatically interact with Devin using our REST APIs
- sources:
  - [1] https://devin.ai/pricing
  - [2] https://web.archive.org/web/20261001040715/https://devin.ai/pricing
  - [3] https://docs.devin.ai/admin/billing/self-serve
  - [4] https://windsurf.com/pricing
  - [5] https://docs.devin.ai/api-reference/overview
  - [6] https://docs.devin.ai/
