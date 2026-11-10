# Moonshot Kimi

> kimi.com | Coding subscriptions, Compute, Inference, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kimi/ | JSON https://fshy.ajam.dev/api/v1/entity/kimi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Moonshot Kimi

- `coding-subs/kimi` | paid-only | evidence documented | binding request-rate | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T01:56:01.641Z (live) | stale on 2026-12-11
- url https://www.kimi.com/help/membership/membership-pricing
- price parsed USD 7.33/mo
- free tier: no free tier on the current ladder; Go, Plus, Pro, Max and Ultra are all paid | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: the ladder is denominated in CNY on the domestic purchase page
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: card | detail: a paid subscription. The domestic ladder is priced in CNY, so a card that settles in CNY is the practical gate
- interface: cli, rest
- limits:
  - request-rate (binding): monthly shared quota pool; Kimi Code on the new ladder has a rolling 5-hour limit and no weekly limit; the old ladder keeps both [1]
- interface detail: Kimi Code, which the pricing page states is included on Plus and above and excluded from Go
- tooling: Kimi Code CLI
- composes with: a shared monthly quota pool covers web and Kimi Code together, so heavy chat use reduces the coding allowance
- reliability: no reliability event recorded
- notes: The first-party pricing page documents CNY 49 / 99 / 199 / 699 / 1399 across five tiers. Third-party sources have reported USD tiers of 19 / 39 / 99 / 199 under different tier names. The cheapest step that includes Kimi Code is Plus at CNY 99 a month, USD 14.81 at 0.149554 USD/CNY on 2026-11-10; the monthly_usd of 7.33 is the Go step, which excludes Kimi Code.
- evidence note: The CNY ladder is first-party and quoted from the vendor page on 2026-10-22. Alternate USD tiers do not appear on this first-party page.
- extras:
  - monthly_usd: 7.33
- evidence:
  - [1] 2026-10-22: current domestic ladder in CNY: Go 49 a month, Plus 99, Pro 199, Max 699, Ultra 1,399, with annual totals 468, 948, 1,908, 6,708 and 13,428; Go excludes Kimi Code; the shared monthly pool does not carry over unused quota
  - [1] 2026-11-10: CNY 49 a month for Go at 0.149554 USD/CNY on 2026-11-10 is USD 7.33 a month | capture: sha256:5e5bf063fae7f92968138e7dedfa3929b5077ef4ec2e13b748ecd2e80fb5c77f | quote: Go ¥49/月
  - [2] 2026-11-10: the exchange rate used is 0.149554 USD for 1 CNY on 2026-11-10 | capture: sha256:79b447c807096b54a1b24a7b902aabbd14b4f9f7a4d7ce09e61863312f9bf328 | quote: "USD": 0.149554
  - [1] 2026-11-10: Plus is CNY 99 a month and is the cheapest step that includes Kimi Code, which Go excludes; CNY 99 at 0.149554 USD/CNY on 2026-11-10 is USD 14.81 a month | capture: sha256:5e5bf063fae7f92968138e7dedfa3929b5077ef4ec2e13b748ecd2e80fb5c77f | quote: Plus ¥99/月
- sources:
  - [1] https://www.kimi.com/help/membership/membership-pricing
  - [2] https://open.er-api.com/v6/latest/CNY

## Moonshot Kimi Hosted Agents sandbox

- `compute/moonshot-kimi` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:32.000Z (live) | stale on 2026-11-22
- url https://platform.kimi.com/docs/pricing/hosted-agents.md
- free tier: no free tier: each hosted-agent session runs in its own cloud sandbox billed by runtime, with model tokens and plugin calls metered separately | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: sandbox runtime bills per session by duration; model tokens and plugin calls are metered on their own pages [1]
  - write-gated (binding): no free tier is stated, and the three meters are separate, so a free model tier would not make the sandbox free [1]
- limits note: Session cap, idle-reap and network policy are not documented. Ranked partial.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the hosted-agent pricing document was read on 2026-10-22 (Chinese). It states three separate meters: sandbox runtime, model tokens and plugin calls, and publishes no free tier, which confirms paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a session's sandbox bills by runtime; the document states no cap and points at the model page for tokens
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '托管智能体的每个会话运行在一个独立的云沙箱中，沙箱按运行时长计费' - each hosted-agent session runs in its own cloud sandbox and the sandbox bills by runtime - with model tokens and plugin calls billed separately, quoted
- sources:
  - [1] https://platform.kimi.com/docs/pricing/hosted-agents.md

## Moonshot Kimi API Platform

- `inference/moonshot-kimi-api` | fails-identity | evidence documented | binding volume-quota | category inference API, regional voucher
- needs card no, phone yes, ID no, institution no | verified 2026-10-28T04:36:18.792Z (live) | stale on 2026-11-28
- url https://www.kimi.com/en/help/kimi-api/api-free-trial
- free tier: An RMB 15 voucher granted on registration, valid for 3 months from issue, only for new users who register with a mainland China mobile number. It is applied automatically and deducted before the top-up balance. With a zero balance after the voucher, API requests return a 403 error. No free grant for a registration outside mainland China is stated on the page read | unit: mixed | metered on: wall-clock | read on: 2026-10-28 | source: [1] | note: regional-credit
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: country-phone | detail: the voucher is granted to new users who register with a mainland China mobile number | country: CN
- interface: rest
- limits:
  - volume-quota (binding): RMB 15 voucher, expires 3 months after issue; afterwards requests need a top-up balance or return 403 [1]
- binding note: the voucher is small and time-boxed, and it is granted only to mainland mobile registrations
- tooling: not stated
- composes with: the voucher is spent before the top-up balance, so a mainland account runs on it first and then on paid balance
- reliability: not assessed: no request was sent to the endpoint
- evidence note: the voucher rules are the vendor's help page; any non-mainland free grant or minimum top-up on the international platform is unverified
- evidence:
  - [1] 2026-10-28: the free voucher is for new users registering with a mainland China mobile number | capture: sha256:356915d50ce7a2e53a2865acc28f4a353d8847e621da2f500662c9e0cad4de05 | quote: - Eligible users: New users who register with a mainland China mobile number.
  - [1] 2026-10-28: the voucher is RMB 15 on registration | capture: sha256:356915d50ce7a2e53a2865acc28f4a353d8847e621da2f500662c9e0cad4de05 | quote: - Voucher amount: An RMB 15 voucher is granted upon registration.
  - [1] 2026-10-28: the voucher expires 3 months after issue | capture: sha256:356915d50ce7a2e53a2865acc28f4a353d8847e621da2f500662c9e0cad4de05 | quote: - Validity period: The voucher is valid for 3 months from the date it is issued and expires automatically afterward.
  - [1] 2026-10-28: after the voucher a top-up balance is required, otherwise requests return 403 | capture: sha256:356915d50ce7a2e53a2865acc28f4a353d8847e621da2f500662c9e0cad4de05 | quote: After the voucher is used up, API calls will be charged against your top-up balance. If your balance is zero, API requests will return a 403 error.
- sources:
  - [1] https://www.kimi.com/en/help/kimi-api/api-free-trial

## Moonshot / Kimi API Files

- `storage/moonshot-kimi-api-files` | fails-quota | evidence reported | binding per-object-cap | category Chinese LLM provider /v1/files
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://platform.kimi.com/docs/api/files-delete
- free tier: 10 GiB total storage per organization (default); 1,000 files; 100 MB per file | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100 MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. File upload/extract are not billed; only tokens are. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - per-object-cap (binding): 100 MB per file [1]
- limits note: per-object-cap 100 MB; 1,000 files; 10 GiB total. Deletion is irreversible and mandatory to free quota.
- interface detail: OpenAI-compatible /v1/files; also session filesystem browsing at /v1/sessions/{id}/filesystem
- tooling: openai-python with base_url https://api.moonshot.cn/v1; curl
- composes with: 10 GiB per org, and projects under the `2026-09-01-beta` kimi-api-version header scope lists per project. A possible multiplicative axis, unverified.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GiB total storage per organization (default); 1,000 files; 100 MB per file
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '已上传文件会占用组织总存储配额（默认 10 GiB）；达到配额上限后，新的上传会被拒绝'
  - [2] 2026-10-21: 'Each user can upload a maximum of 1,000 files, with each file not exceeding 100MB in size. The total size of all uploaded files must not exceed 10GB.'
  - [3] 2026-10-21: '组织总存储配额（默认 10 GiB）'
- sources:
  - [1] https://platform.kimi.com/docs/api/files-delete
  - [2] https://moonshot-ai.gitbook.io/moonshot-ai/api-documentation/files
  - [3] https://platform.kimi.com/docs/llms-full.txt
