# CloudBrowser AI

> cloudbrowser.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudbrowser/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudbrowser.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CloudBrowser AI

- `compute/cloudbrowser` | trial-only | evidence documented | binding retention-clamped | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-06T17:48:23.920Z (live) | stale on 2026-12-07
- url https://cloudbrowser.ai/
- free tier: a 7-day free trial on the Basic plan and a free open-source MCP connector; browser hours beyond the trial need a paid plan from $25 a month for 250 hours | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the page read states no egress allowance and no overage price per TB | metered: no | source: [1]
- identity: email | detail: email: an account needs an email address and authentication ('An email address and authentication information are necessary for an account; payment and usage information are necessary for a paid plan.'). A card is not required for the 7-day trial: the same statement makes payment information necessary for a paid plan, and the trial page states 'Start a 7-day free trial on Basic. No browser to install, no servers to run.'. A phone is not required: the policy's account data is 'your email address, password authentication records, language preferences, account identifiers, API credentials and security events', which names no phone. Country: not published at https://cloudbrowser.ai/privacy-policy.
- interface: rest
- limits:
  - request-rate: 250 browser hours a month on the $25 tier [1]
  - retention-clamped (binding): the free period is 7 days on Basic and ends regardless of usage [1]
  - request-rate: 10 concurrent instances on Basic and 25 on Premium, three tabs each [1]
- interface detail: HTTP API to open a browser, then Chrome DevTools Protocol with Puppeteer or Playwright; official .NET and Node.js SDKs; a remote MCP server; a web dashboard
- tooling: HTTP API plus CDP with Puppeteer or Playwright; official .NET and Node.js SDKs
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the 7-day trial, the $25 tier and 250 browser hours. The free half is a trial, so the verdict moves to trial-only rather than paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the trial clock is 7 days; a session itself has its own limit per plan
  - free_tier_kind: trial
  - reclassified_from: dead
  - ps.price: saved sessions store cookies and localStorage
  - ps.durability: saved session
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until removed
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: premium proxies included on every plan
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'The open-source MCP connector is free. Browser usage requires a CloudBrowser account and a paid plan after the 7-day Basic trial.' and 'Start with a 7-day free trial on Basic' with '$25/month' and '250 browser hours/mo', quoted
  - [1] 2026-11-03: the pricing section lists browser hours and concurrency and states no egress allowance or overage price | capture: sha256:7145d4284d77d8f8bbbccc5f177efc19de817856ad00fc079cf71c4bd76d5a97 | quote: 250 browser hours/mo
  - [1] 2026-11-03: browsers are opened over an HTTP API and driven over CDP | capture: sha256:7145d4284d77d8f8bbbccc5f177efc19de817856ad00fc079cf71c4bd76d5a97 | quote: Open stealth Chrome with one HTTP call, then drive it over CDP with Puppeteer or Playwright.
  - [2] 2026-11-04: the first step of the documented quickstart is an account | capture: sha256:69540af350abe495fc12b77a1ec1f7426d01a829f87e9b448beff8892a3376d4 | quote: Create an account
  - [3] 2026-11-04: the account needs an email and authentication, and payment details only for a paid plan | capture: sha256:3153cd6069cbb6ff6d83d7e3e563bfabd8ada91dd44c3da69723a9faedc552c6 | quote: An email address and authentication information are necessary for an account; payment and usage information are necessary for a paid plan.
  - [3] 2026-11-06: an email address and authentication are necessary for an account, and payment information only for a paid plan | capture: sha256:3153cd6069cbb6ff6d83d7e3e563bfabd8ada91dd44c3da69723a9faedc552c6 | quote: An email address and authentication information are necessary for an account; payment and usage information are necessary for a paid plan.
  - [2] 2026-11-06: the trial starts on Basic with nothing installed and no server | capture: sha256:69540af350abe495fc12b77a1ec1f7426d01a829f87e9b448beff8892a3376d4 | quote: Start a 7-day free trial on Basic. No browser to install, no servers to run.
  - [3] 2026-11-06: the account data the policy lists is an email address and authentication records, with no phone | capture: sha256:3153cd6069cbb6ff6d83d7e3e563bfabd8ada91dd44c3da69723a9faedc552c6 | quote: your email address, password authentication records, language preferences, account identifiers, API credentials and security events
- sources:
  - [1] https://cloudbrowser.ai/
  - [2] https://cloudbrowser.ai/sdk
  - [3] https://cloudbrowser.ai/privacy-policy
