# Jules

> jules.google | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jules/ | JSON https://fshy.ajam.dev/api/v1/entity/jules.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jules

- `compute/jules` | qualifies | evidence documented | binding request-rate | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:22.456Z (live) | stale on 2026-12-05
- url https://jules.google/docs/usage-limits
- free tier: Jules free plan: 15 daily tasks on a rolling 24-hour window, 3 concurrent tasks, Gemini 2.5 Pro, quoted: "Daily Tasks (rolling 24 hours) | 15", "Concurrent Tasks | 3", "Model Access | Gemini 2.5 Pro" | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a Google account: the getting-started guide says to sign in with a Google account, accept a one-time privacy notice and connect a GitHub account to the repositories Jules works on; paid plans need a Google AI subscription on an individual @gmail.com account. The guide describes no card or phone step for the free plan.
- interface: cli
- limits:
  - request-rate (binding): a rolling 24-hour window of 15 tasks stops new work first; the product disables the New task button and waits for the window to roll. [1]
- limits note: a rolling 24-hour window of 15 tasks stops new work first; the product disables the New task button and waits for the window to roll.
- binding note: the same as limits note
- interface detail: the Jules Tools CLI and the web app; the REST endpoints the CLI calls are undocumented; not probed
- tooling: the Jules web app at jules.google.com and the Jules Tools CLI (npm package @google/jules); the CLI also exports settings, environment variables, scheduled tasks, memories and every session to a local folder
- composes with: each task runs in a fresh virtual machine that clones a connected GitHub repository, so each free daily task is a short-lived build and test machine; dev servers and watch scripts are not supported in setup scripts, and the route stops taking new work after November 11, 2026
- reliability: scheduled shutdown announced October 29, 2026: sessions can continue until November 11, 2026, Jules is read-only after that until the end of the year, and it winds down on December 31, 2026
- notes: A coding subscription: Jules is a coding agent with a free plan, and higher task limits come with the Google AI Pro and Ultra plans. No coding-subs record holds it, and none is proposed because the product is winding down (see reliability_note); the vendor points users to Google Antigravity, recorded at coding-subs/antigravity. It sits in compute because each task runs in its own virtual machine. The free tier is capped by tasks, not by tokens or minutes, and the page states no per-task wall clock. The free plan gets Gemini 2.5 Pro while the paid plans start with Gemini 3 Pro. The age requirement is 18 or older.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: recurring-allowance
- evidence:
  - [1] 2026-10-22: the plan table gives Free 15 daily tasks, 3 concurrent tasks and Gemini 2.5 Pro, quoted; the same page says paid plans need a @gmail.com Google AI subscription, so the free tier is the only lane open to a non-gmail identity
  - [2] 2026-10-22: "Each task runs in a fresh virtual machine where Jules clones your repo, installs dependencies, and makes changes based on your prompt." and the VM has internet access, quoted
  - [1] 2026-10-22: probe GET returned status 200, 40672 bytes, sha256 87619148901a658f49550c35666481065d00f6859baa204122be72d157c58f15, no challenge detected, at 2026-10-22T15:23:27Z
  - [1] 2026-10-30: the free Jules plan still allows 15 tasks in a rolling 24 hours, against 100 on Pro and 300 on Ultra | capture: sha256:41adfb75ccebfd274db5ad6df0d17e86d28a5927fe5ffc6e8215e0f5a7503985 | quote: | Daily Tasks (rolling 24 hours) | 15 | 100 | 300 |
  - [1] 2026-10-30: the free plan still allows 3 concurrent tasks | capture: sha256:41adfb75ccebfd274db5ad6df0d17e86d28a5927fe5ffc6e8215e0f5a7503985 | quote: | Concurrent Tasks | 3 | 15 | 60 |
  - [1] 2026-10-30: the free plan gets Gemini 2.5 Pro and the paid plans start with Gemini 3 Pro | capture: sha256:41adfb75ccebfd274db5ad6df0d17e86d28a5927fe5ffc6e8215e0f5a7503985 | quote: | Model Access | Gemini 2.5 Pro | Higher access to the latest model (starting with Gemini 3 Pro) | Priority access to the latest model (starting with Gemini 3 Pro) |
  - [3] 2026-10-30: the vendor's changelog dated October 29, 2026 sets the end of new work at November 11, 2026 and the wind-down at December 31, 2026 | capture: sha256:61e7d5c95b7303cf562b1a82665dd1dc1ba7899dca86e6191b3be3ac77fc20d7 | quote: After November 11, 2026, we will be turning Jules to read-only until the end of the year.
  - [3] 2026-10-30: new sessions end on November 11, 2026 | capture: sha256:61e7d5c95b7303cf562b1a82665dd1dc1ba7899dca86e6191b3be3ac77fc20d7 | quote: You have until November 11, 2026 to continue finishing up sessions.
  - [4] 2026-10-30: the sign-in step of the getting-started guide is a Google account, followed by a GitHub connection | capture: sha256:6729315cc22f00363e11c8c6538245d8823f46d9b2f6c83b0bae7312c984d8b2 | quote: Sign in with your Google account.
  - [3] 2026-10-30: the vendor documents a CLI, Jules Tools, installed from npm | capture: sha256:61e7d5c95b7303cf562b1a82665dd1dc1ba7899dca86e6191b3be3ac77fc20d7 | quote: To export, install Jules Tools and sign in:
  - [1] 2026-10-30: Jules is sold as a benefit of the Google AI Pro and Ultra subscriptions, with a free plan below them | capture: sha256:41adfb75ccebfd274db5ad6df0d17e86d28a5927fe5ffc6e8215e0f5a7503985 | quote: Jules in Pro is included as a benefit of the Google AI Pro plan.
  - [5] 2026-11-03: the plans page still lists the free plan at 15 daily tasks on November 3, 2026, before the November 11 cutoff | capture: sha256:41adfb75ccebfd274db5ad6df0d17e86d28a5927fe5ffc6e8215e0f5a7503985 | quote: | Daily Tasks (rolling 24 hours) | 15 | 100 | 300 |
  - [6] 2026-11-03: the product home page still advertises the free plan with 15 tasks per day on November 3, 2026; no closure of sign-ups is stated | capture: sha256:fd0f33b421f06c380acbf611255cabce40f501f4c1a791b693a6228aabcaba78 | quote: - 15 tasks per day
  - [7] 2026-11-03: the turndown notice dated October 29, 2026 is unchanged on November 3, 2026: sessions until November 11, 2026, wind-down on December 31, 2026 | capture: sha256:0750d640bde327fc115b1034e1d8b32c4f390b512bb208da0c0b8ab6f32474f4 | quote: Jules will wind down on December 31, 2026. You have until November 11, 2026 to continue finishing up sessions.
  - [4] 2026-11-03: the getting-started guide still gives a Google account sign-in as the first step on November 3, 2026 | capture: sha256:6729315cc22f00363e11c8c6538245d8823f46d9b2f6c83b0bae7312c984d8b2 | quote: Sign in with your Google account.
  - [1] 2026-11-04: the free Jules plan still allows 15 tasks in a rolling 24 hours, against 100 on Pro and 300 on Ultra | capture: sha256:41adfb75ccebfd274db5ad6df0d17e86d28a5927fe5ffc6e8215e0f5a7503985 | quote: | Daily Tasks (rolling 24 hours) | 15 | 100 | 300 |
- sources:
  - [1] https://jules.google/docs/usage-limits
  - [2] https://jules.google/docs/faq/
  - [3] https://jules.google/docs/changelog/
  - [4] https://jules.google/docs/
  - [5] https://jules.google/docs/usage-limits/
  - [6] https://jules.google/
  - [7] https://jules.google/docs/changelog/2026-10-29/
