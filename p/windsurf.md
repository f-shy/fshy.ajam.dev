# Windsurf

> windsurf.com | Coding subscriptions; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/windsurf/ | JSON https://fshy.ajam.dev/api/v1/entity/windsurf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Windsurf

- `coding-subs/windsurf` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-10T01:56:02.007Z (live) | stale on 2026-12-11
- url https://windsurf.com/pricing
- free tier: the Windsurf SKU is served on Devin's ladder: Free USD 0, 'Light quota to code with agents', Unlimited inline edits, Unlimited Tab completions | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1] | note: windsurf.com/pricing returns 308 to devin.ai/pricing, and windsurf.com itself redirects to devin.ai/desktop. There is no separate Windsurf price list. Pricing follows Devin.
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: email | detail: through the Devin ladder; the Free plan is USD 0 and the paid tiers are bought with a card
- interface: rest
- limits:
  - request-rate (binding): the Free plan's agent quota is described as 'Light quota to code with agents' with no number, on the Devin ladder the host now serves [1]
- limits note: no countable allowance is stated for agent work on any tier. Inline edits and Tab completions are stated as unlimited on Free. Paid plans refresh their allowance on a daily and weekly basis on the Devin ladder this host serves; no window is stated for the Free plan's light quota
- binding note: the unpublished agent quota binds, and it is the same quota system Devin sells, so pairing Windsurf with Devin buys no independence
- interface detail: an editor and a desktop client served from devin.ai/desktop; the plan table that windsurf.com/pricing serves lists Devin API among the product's features, and the Devin API reference documents a REST API at https://api.devin.ai/v3/organizations/* reached with a service-user key
- tooling: not established
- composes with: the editor and agent quota are the scarce link; the product now shares a ladder and a quota system with Devin, so it is not an independent second quota in a stack
- reliability: the windsurf.com host 308-redirects every path probed to devin.ai on 2026-10-22, so a client pinned to the old host follows a redirect on each request
- notes: Windsurf did not die and its pricing page did not move to a subdomain: the brand, the host and the ladder are Devin's now, and every windsurf.com path probed resolves there. The verdict is qualifies-with-caveat because the surviving free tier is real and its allowance is the word 'light'. The record keeps its own slug and its own redirect evidence; the price list is Devin's and lives in devin.json.
- evidence note: the redirect is measured: HTTP 308 with Location: https://devin.ai/pricing, and the landing host 308s to devin.ai/desktop. The price list behind it is Devin's, read the same minute.
- evidence:
  - [2] 2026-10-22: HTTP/1.1 308 Permanent Redirect with Location: https://devin.ai/pricing; following it returns 200 with the same byte count as a direct fetch of devin.ai/pricing, and the extracted text is identical between the two hosts. The raw bytes are not byte-stable across fetches because the page carries per-request tokens, so a body digest cannot serve as an identity check here
  - probe:windsurf.com/pricing 2026-11-03: windsurf.com/pricing still answers HTTP 308 to https://devin.ai/pricing, then 200 at the final URL | capture: sha256:6cbd226c5eabe596482d2bd54e2ce5a46ac53124b4ec3567fd3cd5a51b566a40 | quote: "status": 308
  - [1] 2026-11-03: the paid-plan allowance has a daily and a weekly window; the Free plan's window is not stated | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: Each paid plan comes with a usage allowance that refreshes automatically on a daily and weekly basis.
  - [1] 2026-11-03: windsurf.com/pricing resolves to the Devin ladder, whose Free plan is unchanged | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: The Free plan includes a light quota to code with agents, limited model availability, unlimited inline edits, and unlimited Tab completions.
  - [2] 2026-11-09: the served plan table names Devin API as an included feature | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: Devin API
  - [3] 2026-11-09: the Devin API named by the served plan table is a documented REST API | capture: sha256:4af7207085855d3d31e9c285f65254de40f1acd228babdd96ab334b11a2aa9b1 | quote: The Devin API enables you to integrate Devin into your applications, automate workflows, and build powerful tools.
  - [2] 2026-11-09: the served plan table names Devin API | capture: sha256:1d924604388e1889832f09b082f05d5cb33d9477e53fcf3c476a13fd1c17017b | quote: Devin API
  - [1] 2026-11-10: the plan table lists the Devin API among the product's features | capture: sha256:54e5100038aba40e09fb596d575c42870cdbf14c2db156a35bb64d4b3ca4ddd0 | quote: Devin Cloud DeepWiki Devin API Ask Devin
- sources:
  - [1] https://devin.ai/pricing
  - [2] https://windsurf.com/pricing
  - [3] https://docs.devin.ai/api-reference/overview
