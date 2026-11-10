# OpenCode Go

> opencode.ai | Coding subscriptions, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opencode/ | JSON https://fshy.ajam.dev/api/v1/entity/opencode.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenCode Go

- `coding-subs/opencode-go` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T00:38:57.492Z (live) | stale on 2026-12-04
- url https://opencode.ai/docs/go
- free tier: Go is USD 10 a month, Go Plus USD 40 and Go Teams USD 20 per member a month; two models, Beam Free and Iceman Contributor Free, are Free with an Unlimited monthly limit 'limited time', and free models stay usable after the paid limit is reached | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the paid limit is a monthly dollar amount per model, not a token count
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: card | detail: billing details in the console; Go and Go Plus cover a single-member workspace, and Go Teams at USD 20 per member a month covers a workspace with several members
- interface: rest, cli
- limits:
  - request-rate (binding): per-model monthly dollar ceiling; the 5-hour cap is 20 per cent of it, the weekly cap 50 per cent, the month 100 per cent [1]
  - request-rate (binding): no per-request limit is published. The page publishes an estimated request count per model and names the token shape each estimate assumes, for example GLM-5.3/5.2 at 700 input, 52,000 cached and 150 output tokens per request, under 'The estimates use the following token counts per request; actual usage varies' [1]
- interface detail: an API key from the OpenCode console; endpoints are published per model family at opencode.ai/inference/go/{openai,anthropic,google}/
- tooling: OpenCode TUI, or any client pointed at the published endpoint
- composes with: the only plan found in this topic that publishes both a per-model dollar ceiling and the API endpoint that spends it
- reliability: no reliability event recorded
- notes: The plan publishes a per-model dollar ceiling. The GLM-5.3 cap of USD 15 a month at USD 1.40 per 1M input represents about 10.7M input tokens with no output.
- evidence note: the ceilings, the reset windows and the endpoints are quoted from the vendor page read. The dollar ceiling has not been converted to tokens by measurement.
- evidence:
  - [1] 2026-10-22: Go USD 10 a month and Go Plus USD 40; usage limits are monthly dollar amounts per model, with 5-hour, weekly and monthly allowances at 20, 50 and 100 per cent; 16 of the 36 Go ceilings are USD 15, 13 are USD 60, two are USD 30, two are USD 80 and three are Unlimited; the page publishes estimated request counts per model against a named token shape and states no per-request limit; exceeded limits fall back to pay-as-you-go credit if enabled, otherwise requests are blocked and the free models remain usable
  - [2] 2026-10-22: the pay-as-you-go Console prices 14 model ids at Free for input, output and cached read, all marked Free or limited time
  - [1] 2026-10-30: the Go tables list two models at Free with an Unlimited monthly limit marked limited time: Beam Free and Iceman Contributor Free | capture: sha256:51fe9964a7e0cfc7c9150c69471d7ef790f1863a68639e91f813fdad48b94089 | quote: | Iceman Contributor Free | Free | Free | Free | - | Unlimited<br /><small>limited time</small> |
  - [1] 2026-10-30: a multi-member workspace can now subscribe through Go Teams at $20 per member a month | capture: sha256:51fe9964a7e0cfc7c9150c69471d7ef790f1863a68639e91f813fdad48b94089 | quote: Go Teams covers every member of a workspace with several members, at $20 per member per month.
  - [1] 2026-10-30: the 5-hour, weekly and monthly allowances are still 20, 50 and 100 per cent of each model's monthly dollar limit | capture: sha256:51fe9964a7e0cfc7c9150c69471d7ef790f1863a68639e91f813fdad48b94089 | quote: Each model has the following usage limits: 5-hour — 20% of the monthly limit; weekly — 50%; and monthly — 100%.
  - [1] 2026-10-30: the token shape behind the published request estimates is unchanged | capture: sha256:51fe9964a7e0cfc7c9150c69471d7ef790f1863a68639e91f813fdad48b94089 | quote: GLM-5.3/5.2 — 700 input, 52,000 cached, 150 output tokens per request
  - [1] 2026-10-30: free models stay usable after a paid limit is reached | capture: sha256:51fe9964a7e0cfc7c9150c69471d7ef790f1863a68639e91f813fdad48b94089 | quote: If you reach the usage limit, you can continue using the free models.
  - [1] 2026-10-30: the Go models are reachable at published per-family endpoints under opencode.ai/inference/go/ | capture: sha256:51fe9964a7e0cfc7c9150c69471d7ef790f1863a68639e91f813fdad48b94089 | quote: You can also access Go models through the following API endpoints.
  - [3] 2026-10-22: the Go page copy of 2026-10-22 lists LongCat 2.5 Preview Free at Free with an Unlimited monthly limit marked limited time | capture: sha256:d9473f1f1765a7f6cb3a282c6fd539da48bf1c7852a9dbddd57bd7c7135fd674 | quote: <td>LongCat 2.5 Preview Free</td><td>Free</td><td>Free</td><td>Free</td><td>-</td><td><strong>Unlimited</strong><br/><small>limited time</small></td>
  - [3] 2026-10-22: the Go page copy of 2026-10-22 lists Beam Free at Free with an Unlimited monthly limit marked limited time | capture: sha256:d9473f1f1765a7f6cb3a282c6fd539da48bf1c7852a9dbddd57bd7c7135fd674 | quote: <td>Beam Free</td><td>Free</td><td>Free</td><td>Free</td><td>-</td><td><strong>Unlimited</strong><br/><small>limited time</small></td>
  - [3] 2026-10-22: the Go page copy of 2026-10-22 lists MiniMax M3.1 Flash Free at Free with an Unlimited monthly limit marked limited time | capture: sha256:d9473f1f1765a7f6cb3a282c6fd539da48bf1c7852a9dbddd57bd7c7135fd674 | quote: <td>MiniMax M3.1 Flash Free</td><td>Free</td><td>Free</td><td>Free</td><td>-</td><td><strong>Unlimited</strong><br/><small>limited time</small></td>
  - [1] 2026-11-03: the paid limit is a monthly dollar amount per model, not a token count | capture: sha256:6b75608b1c9d7f5197dfbfd5feb43e59a36c6070cefa7a2a90bea851137b2680 | quote: Usage limits are defined as monthly dollar amounts.
- sources:
  - [1] https://opencode.ai/docs/go
  - [2] https://opencode.ai/docs/zen
  - [3] https://web.archive.org/web/20261022103549/https://opencode.ai/v2/docs/console/go/

## OpenCode Zen free models

- `inference/opencode-zen-free` | fails-identity | evidence measured | binding none | category inference endpoint, access-gated
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:56:11.137Z (live) | stale on 2026-12-05
- url https://opencode.ai/zen/v1
- free tier: the Zen pricing table lists 11 model ids at Free for input and output; 10 of them are also Free for cached read (Big Pickle, Pulse Alpha Free, GLM-5.3-Flash Free, DeepSeek V4.1 Flash Free, Beam Free, Flint 40B Free, MiMo-V2.6-Flash Free, Nemotron 3 Ultra Free, Nemotron 3.5 Lightning Free, Nemotron 3.5 Super VL Free) and Jev 1.13 Free has no cached read price | unit: unlimited | metered on: request-count | read on: 2026-10-22 | source: [1] | note: 'Free' in the price column is not 'reachable': the free tier is restricted to the OpenCode client
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an OpenCode account, and the request must originate from the OpenCode client. The 403 body names the restriction: 'OpenCode's free tier can only be used from within OpenCode'
- interface: rest
- limits note: no rate or quota is published: the gate is access, not allowance; some free models are excluded by region (Pulse Alpha Free is not available in the European Union, Iceland, Liechtenstein, Norway, Cuba, Iran, North Korea, Russia, Ukraine or Venezuela)
- endpoint: https://opencode.ai/zen/v1/chat/completions
- tooling: any OpenAI-compatible client; curl against POST {base}/chat/completions
- composes with: Programmatic automation cannot be chained: the free tier responds exclusively within the official OpenCode desktop application.
- reliability: the restriction is enforced on the request path, not the account, so no header or key makes an external call succeed
- evidence note: four calls across two sessions with two User-Agents. The 403 is a named policy gate and not an outage, and the body says so.
- probe:
  - records[0].probe_id: opencode-spacebunny
  - records[0].requested_model: space-bunny-free
  - records[0].http_run1: 403
  - records[0].http_run2: 400
  - records[0].answered_run1: no
  - records[0].answered_run2: no
  - records[0].echo_match: yes
  - records[0].latency_ms_run1: 860
  - records[0].latency_ms_run2: 1066
  - records[0].completion_tokens_run1: 0
  - records[0].needle_echoed_run1: no
  - records[0].body_bytes_run1: 701
  - records[0].body_sha256_16_run1: f45bbd157c6d06d8
  - records[0].reasoning_only: no
  - records[0].error_run1: {"type":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/","title":"Error 1010: Access denied","status":403,"detail":"The site owner has b
  - records[0].error_run2: {"type": "server_error", "message": "Upstream request failed: Model is unavailable."}
  - records[1].probe_id: opencode-longcat
  - records[1].requested_model: longcat-2.5-preview-free
  - records[1].http_run1: 403
  - records[1].http_run2: 403
  - records[1].answered_run1: no
  - records[1].answered_run2: no
  - records[1].echo_match: yes
  - records[1].latency_ms_run1: 799
  - records[1].latency_ms_run2: 811
  - records[1].completion_tokens_run1: 0
  - records[1].needle_echoed_run1: no
  - records[1].body_bytes_run1: 701
  - records[1].body_sha256_16_run1: 615fa2152362733d
  - records[1].reasoning_only: no
  - records[1].error_run1: {"type":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/","title":"Error 1010: Access denied","status":403,"detail":"The site owner has b
  - records[1].error_run2: {"type": "FreeTierError", "message": "OpenCode's free tier can only be used from within OpenCode. Download it at https://opencode.ai and keep building."}
  - runs: probes-w.json; probes-w-run2.json
- evidence:
  - probe:https://opencode.ai/zen/v1/chat/completions 2026-10-22: longcat-2.5-preview-free returned 403 FreeTierError 'OpenCode's free tier can only be used from within OpenCode' in both runs, and with both a curl and a Python User-Agent
  - probe:https://opencode.ai/zen/v1/chat/completions 2026-10-22: 
  - [1] 2026-10-22: 14 model ids priced Free for input, output and cached read, including Big Pickle, GLM-5.3-Flash Free, DeepSeek V4.1 Flash Free and LongCat 2.5 Preview Free
  - [1] 2026-10-28: the pricing source page is still the same URL and still says free-tier chat models require the OpenCode client | capture: sha256:da634c9ea813aac8e7bad961c98ca4ce42c77f0a1bec32e9644ea50e0fc7d579 | quote: Free-tier chat models require OpenCode; use paid models or [Go](/console/go) from other clients.
  - [1] 2026-11-04: the pricing table was re-read on 2026-11-04 | capture: sha256:326792aff60749c6ec2f8891374ca98b9eff1dcf7bfe0a3ada1fd9188cd360c2 | quote: | Pulse Alpha Free | Free | Free | Free | - |
  - probe:https://opencode.ai/docs/zen 2026-11-04: the pricing table row format: Free for input, output and cached read; 11 such rows with Jev 1.13 Free lacking the cached read price | capture: sha256:a69a6f1a251d829845409164cf1931f115bfebb91cea7697528262fa66da787a | quote: <td>Pulse Alpha Free</td><td>Free</td><td>Free</td><td>Free</td><td>-</td>
  - probe:https://opencode.ai/docs/zen 2026-11-04: Pulse Alpha Free carries a regional exclusion list | capture: sha256:a69a6f1a251d829845409164cf1931f115bfebb91cea7697528262fa66da787a | quote: It’s not available in the European Union, Iceland, Liechtenstein, Norway, Cuba, Iran, North Korea, Russia, Ukraine, or Venezuela.
  - probe:https://opencode.ai/docs/zen 2026-11-04: the pricing source page still lists the free models | capture: sha256:a69a6f1a251d829845409164cf1931f115bfebb91cea7697528262fa66da787a | quote: <td>Pulse Alpha Free</td><td>Free</td><td>Free</td><td>Free</td><td>-</td>
  - [1] 2026-11-04: the pricing table the free-tier text rests on was read on 2026-11-04 | capture: sha256:326792aff60749c6ec2f8891374ca98b9eff1dcf7bfe0a3ada1fd9188cd360c2 | quote: | Pulse Alpha Free | Free | Free | Free | - |
- sources:
  - [1] https://opencode.ai/docs/zen
