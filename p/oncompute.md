# Ocean Network

> oncompute.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oncompute/ | JSON https://fshy.ajam.dev/api/v1/entity/oncompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ocean Network /

- `compute/ocean-network` | trial-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://docs.oncompute.ai/ocean-network-dashboard/claim-your-compy-tokens.md
- free tier: A self-serve grant with no wallet extension and no card, but with no published amount. Quoted: sign in at the dashboard, choose 'Claim credits'; the form asks for 'Name - your full name, Email address - the address where your verification code will be sent, Discord or Telegram handle' plus four profile questions; then 'A 6-digit verification code has been sent to the email address you provided. The code expires in 10 minutes.'; then 'Verification successful - You are eligible for grant distribution' and 'The claimable amount in COMPY tokens is displayed'. The USD 100 figure is third-party: Ocean's own Substack states '$100 in complimentary compute credits to early adopters'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-off-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a verified email address, a full name and a Discord or Telegram handle: the claim form asks for 'Name - your full name, Email address - the address where your verification code will be sent, Discord or Telegram handle' plus four profile questions, then sends a 6-digit code with a 10-minute expiry. Signing in with email, Google or a passkey creates a smart wallet automatically, so no crypto wallet is needed. No card and no hold: the grant pays in COMPY. Paid jobs are funded in USDC or COMPY from an escrow balance, and whether a debit or prepaid card is accepted is not stated.
- interface: unknown
- limits:
  - write-gated (binding): The grant is an application with four profile questions and a Discord or Telegram handle on top of a verified email, and it pays in COMPY at an amount the docs never state, so the first failure is that the quantity is unknown until the claim screen renders; the second is that paid jobs need an on-chain escrow deposit, and COMPY is one of two accepted tokens. [1]
- limits note: The grant is an application with four profile questions and a Discord or Telegram handle on top of a verified email, and it pays in COMPY at an amount the docs never state, so the first failure is that the quantity is unknown until the claim screen renders; the second is that paid jobs need an on-chain escrow deposit, and COMPY is one of two accepted tokens.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the only grant in the class that needs no card and creates its own wallet, so it is the one that needs neither. It breaks on the unknown amount and on escrow: a holder of COMPY still cannot start a paid job without depositing and signing an authorization.
- reliability: no reliability event recorded
- notes: The honest term is that the flagship USD 100 is documented only by Ocean's announcement, not by its docs, and the docs describe the amount as displayed at claim time rather than fixed. Two independent third-party pages repeat USD 100 (ai-explorer.io and a Medium walkthrough dated May 2026), so the figure is probably right and its expiry, coverage and conversion are all unstated. Not established: EXPIRY, COMPY to USD ratio, and whether the grant value changed. A first-party docs ask-query returned that the docs 'do not state a fixed USDC value or conversion ratio'.
- extras:
  - facets.class: decentralized-gpu-marketplace
  - facets.free_tier_kind: one-off-credit
  - facets.shape.gpu_class: H200, H100, A100 on paid environments
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: the claim flow step by step: profile form with full name, email, Discord or Telegram handle, four questions, a 6-digit email code with a 10-minute expiry, then a claimable COMPY amount and an on-chain claim on Base
  - [2] 2026-10-22: quoted: signing in with email, Google or passkey creates a smart wallet automatically with 'No extension or seed phrase' and sponsored gas, so the grant needs no separate crypto wallet
  - [3] 2026-10-22: quoted: 'Payments are made with USDC or COMPY'; paid jobs are funded from an escrow balance that the renter deposits and authorizes, and free test jobs need no wallet but are CPU test environments
  - [4] 2026-10-22: a worked quote of '0.15 COMPY' for one job with an escrow lock requirement of about 24.5 hours, which is a job price and not a stated conversion rate
  - [5] 2026-10-22: 
- sources:
  - [1] https://docs.oncompute.ai/ocean-network-dashboard/claim-your-compy-tokens.md
  - [2] https://docs.oncompute.ai/ocean-network-dashboard/wallets-and-fiat-on-ramp.md
  - [3] https://docs.oncompute.ai/ocean-orchestrator/using-ocean-orchestrator-with-ocean-dashboard.md
  - [4] https://docs.oncompute.ai/on-mcp/walkthrough-from-connect-to-paid-compute.md
  - [5] https://oceanprotocol.substack.com/p/ocean-network-launches-beta-for-affordable
