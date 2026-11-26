# Apify AI

> apify.com | Crawling, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apify/ | JSON https://fshy.ajam.dev/api/v1/entity/apify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Apify

- `crawler-scraper/apify` | qualifies-with-caveat | evidence documented | binding per-object-cap | category crawl API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://apify.com/pricing
- free tier: USD 5 of platform usage a month on the Free plan, 5 concurrent runs | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: the unit is a compute unit | source: [1]
- retention: included usage resets monthly | source: [1]
- egress: not applicable: dataset records | metered: no | source: [1]
- identity: email | detail: the Free plan is a signup; no card stated
- interface: rest
- limits:
  - request-rate: USD 5 included usage a month; USD 0.2 per compute unit on Free; 5 concurrent runs [1]
  - request-rate: proxy traffic USD 8 a gigabyte on Free with 5 IPs included; SERP USD 2.50 per 1,000 [1]
  - per-object-cap (binding): USD 5 of included usage a month buys about 25 compute units at USD 0.20 a unit, so the run length is what the plan buys, not the run count [1]
- limits note: the per-unit price is the binding number: an actor's memory and run time decide how many runs a plan buys
- interface detail: REST and a large Actor store; actors run on the platform's compute
- tooling: not established
- composes with: A place to run somebody else's scraper, which is a different shape from a crawl API that returns pages
- reliability: no reliability event recorded
- notes: The unit is a compute unit, not a page, so the free allowance buys an unknown number of pages before an Actor's own price is counted. The cheapest thing here is the Actor store, not the compute.
- evidence:
  - [1] 2026-10-22: Free USD 0 with USD 5 of included usage a month, USD 0.2 per compute unit, 16 GB memory, 5 concurrent runs; proxy USD 8 a GB; SERP USD 2.50 per 1,000
- sources:
  - [1] https://apify.com/pricing

## Apify AI Code Sandbox

- `compute/apify-ai-code-sandbox` | qualifies-with-caveat | evidence documented | binding volume-quota | category container sandbox (Apify Store Actor) | tier Free plan / pay-per-usage Actor
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.836Z (live) | stale on 2026-12-26
- url https://apify.com/apify/ai-code-sandbox
- free tier: USD 5 of platform usage a month on the Free plan, renewing every month, no credit card; the Actor itself is free to use and the sandbox bills the Apify platform usage (compute units at USD 0.2 per CU on Free, where 1 CU = 1 GB RAM for 1 hour) | unit: credits | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: USD 5 a month of prepaid platform usage, not a fixed number of sandbox hours: how many hours it buys depends on the memory allocated. Unused credits expire at the end of the billing cycle; on the free plan access is blocked until the next cycle instead of billing.
- per-object cap: not an object-storage offer; the sandbox filesystem write API accepts files up to 500 MB | source: [2] | note: The per-file ceiling from the /fs write endpoint, not a total volume cap.
- retention: filesystem changes are backed up to the Actor key-value store and restored after a container migration; an idle container shuts down after 900 seconds by default and can be set to never | source: [2] | note: No fixed retention period is published; the idle timeout controls the container's lifetime.
- egress: data transfer is a metered platform service charged against the same prepaid usage; bridges expose a sandbox's internal HTTP server at a public URL | metered: yes | free allowance: included in the USD 5 monthly platform-usage credit on Free | source: [1]
- identity: email | detail: The signup page offers Continue with Google, Continue with GitHub or an Email field; the account quickstart says creating an account is free and requires no credit card. The free plan renews USD 5 of usage credit a month and pauses access rather than billing when it runs out.
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): USD 5 of platform usage a month on Free; excess blocks access until the next billing cycle; compute is USD 0.2 per CU on Free (1 CU = 1 GB RAM for 1 hour) [1]
  - retention-clamped: the container shuts down after 900 seconds of inactivity by default; set to 0 to disable [2]
  - write-gated: running the Actor and reading private run or storage data needs an authenticated Apify account; searching Actors and reading documentation works without one [3]
- limits note: 5 concurrent runs and 16 GB maximum RAM on Free. Every request to the running Actor has a 5-minute ceiling. The setup script has a 5-minute timeout. Each filesystem write accepts up to 500 MB.
- binding note: The USD 5 monthly platform-usage credit is what runs out first; the free account pauses until the next cycle rather than being billed.
- interface detail: a streamable-HTTP MCP endpoint with execute, read-file, write-file and list-files tools; a /exec code execution API; a /fs filesystem API; an interactive browser shell at /shell; the Apify CLI and REST API start and manage the Actor run
- endpoint: https://UNIQUE-ID.runs.apify.net
- tooling: an Apify account and token, the Apify CLI, the JavaScript or Python apify-client, or any MCP client; the sandbox ships Claude Code, Codex CLI and OpenCode, installed on first use
- composes with: the USD 5 monthly platform credit can fund small Python and Node jobs exposed over MCP or REST, with bridges for a service launched inside the sandbox; jobs needing more than the monthly credit need a paid plan.
- reliability: An idle container shuts down after 900 seconds by default; idle shutdown can be disabled. Every request to the Actor has a 5-minute ceiling and the startup script has a 5-minute timeout. Free-account access pauses when the monthly usage credit runs out.
- notes: The operator's provider list prices this offer at USD 1.60/h billed per second at 2 vCPU/4 GB, a workload figure that the vendor page does not publish; the vendor publishes a compute-unit rate instead. A 4 GB sandbox at USD 0.2/CU draws 1 CU per wall-clock hour, so USD 5 of monthly credit covers 6.25 hours at that size (derived: USD 5 / USD 0.2 per CU = 25 CU; 4 GB = 4 CU/hour, so 25 CU / 4 CU per hour = 6.25 hours). The 100% CPU figure in the list is not confirmed by a vendor page.
- evidence note: The Actor page, pricing page, account quickstart and signup page were read on 2026-11-25; the quoted sentences establish the pay-per-usage model, the USD 5 monthly credit, the CU rate and the signup gate. The rung stays documented because no live run was measured.
- extras:
  - shape.ram_gib: 4
  - shape.note: the vendor publishes memory as the billing unit and a 16 GB maximum on Free
  - billing_model: pay per platform usage against a recurring monthly credit
  - free_tier_kind: recurring-allowance
  - price_arithmetic: USD 5 of platform usage a month; USD 0.2 per compute unit on Free; 1 CU = 1 GB RAM for 1 hour
  - session_cap.wall_clock_min: 5
  - session_cap.idle_reap_s: 900
  - session_cap.restart_required: no
  - session_cap.note: each request to the Actor has a 5-minute ceiling; idle timeout defaults to 900 seconds and can be disabled
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: bridges expose a sandbox HTTP server at a public path
- evidence:
  - [2] 2026-11-25: the Actor provides a secure execution environment for AI-generated code and is paid per platform usage | capture: sha256:54675272eaff5d5561769ea39cbb1fdbca6952291ba868e04d47e57e4cc9d2a0 | quote: Provides a secure execution environment for code generated by AI agents. Interact with the sandbox through web shell, REST API, or MCP. Supports Python and Node.js runtimes, Claude Code, Codex CLI, and OpenCode coding agents, and persists state.
  - [2] 2026-11-25: the Actor itself charges nothing on top and only the Apify platform usage is billed | capture: sha256:54675272eaff5d5561769ea39cbb1fdbca6952291ba868e04d47e57e4cc9d2a0 | quote: This Actor is paid per platform usage. The Actor is free to use, and you only pay for the Apify platform usage, which gets cheaper the higher subscription plan you have.
  - [1] 2026-11-25: the Free plan is USD 0 a month and includes USD 5 of usage a month | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: | Free | $0 | $0 | $5 |
  - [1] 2026-11-25: compute is measured in compute units of 1 GB RAM for 1 hour and bills at USD 0.2 per CU on Free with 16 GB maximum RAM and 5 concurrent runs | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: | Free | $0.2 / CU | 16 GB | 5 |
  - [1] 2026-11-25: the free plan needs no credit card | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: No credit card is required. The free plan includes Apify Proxy, which is limited to use within the platform and does not extend to external clients.
  - [1] 2026-11-25: unused usage credits expire at the end of the billing cycle and the free account is blocked until the next cycle when credit runs out | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: Note that unused usage credits are not rolled over to the next billing cycle, and they expire at the end of the billing cycle.
  - [4] 2026-11-25: signup offers Google, GitHub or an email address and no card field | capture: sha256:4631182c9f4b927f497a94777649bf9516e61c2b6541c44f2c516b2073305789 | quote: or Email Next
  - [5] 2026-11-25: creating an account is free, needs no card, renews USD 5 of usage credit monthly, and pauses access rather than billing when exhausted | capture: sha256:3bee9c9c2441d0806dd7a684d33a104be42547290eeb675b9da30467f7359c26 | quote: Creating an account is free and requires no credit card: the free plan renews $5 of usage credit every month, and if that credit runs out, access pauses until the next month instead of being billed. There is nothing to cancel.
  - [2] 2026-11-25: a filesystem write accepts up to 500 MB | capture: sha256:54675272eaff5d5561769ea39cbb1fdbca6952291ba868e04d47e57e4cc9d2a0 | quote: PUT /fs/{path} — write/replace a file (creates parent dirs; up to 500 MB).
  - [2] 2026-11-25: the container shuts down after inactivity by default | capture: sha256:54675272eaff5d5561769ea39cbb1fdbca6952291ba868e04d47e57e4cc9d2a0 | quote: The container shuts down automatically after this many seconds of inactivity (no requests or shell interaction). Set to 0 to disable.
  - [5] 2026-11-25: running Actors needs authentication while searching Actors and reading schemas works without an account | capture: sha256:3bee9c9c2441d0806dd7a684d33a104be42547290eeb675b9da30467f7359c26 | quote: Running Actors and reading private run or storage data requires authentication. Searching Actors, inspecting their schemas, and searching documentation can be done without an account through the restricted discovery connection below.
  - [1] 2026-11-24: the Free plan price and included monthly usage | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: | Free | $0 | $0 | $5 | No Apify Store discount | Community support |
  - [1] 2026-11-24: the Free plan compute-unit price, memory ceiling and concurrent-run limit | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: | Free | $0.2 / CU | 16 GB | 5 |
  - [1] 2026-11-24: the definition of a compute unit | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: 1 CU = 1 GB of RAM running for 1 hour.
  - [1] 2026-11-24: the free plan needs no credit card and its proxy is platform-only | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: No credit card is required. The free plan includes Apify Proxy, which is limited to use within the platform and does not extend to external clients.
  - [1] 2026-11-24: data transfer is a metered platform service and free access stops when usage runs out | capture: sha256:4cd21942523469e99322ddf2ddf67f6db86349eacf15b163d88902cf95c63e31 | quote: The Apify platform has a number of services that are charged based on usages, such as Actors, proxies, data transfer, and storage.
  - [2] 2026-11-24: the Actor is pay-per-usage with no developer charge on top | capture: sha256:433b53224ae6374f949e604c6eb43d63ac0608c8000b57cd22cee529717870cc | quote: This Actor is paid per platform usage. The Actor is free to use, and you only pay for the Apify platform usage, which gets cheaper the higher subscription plan you have.
  - [2] 2026-11-24: the interfaces are MCP, REST and a browser shell | capture: sha256:433b53224ae6374f949e604c6eb43d63ac0608c8000b57cd22cee529717870cc | quote: Connect over MCP, a REST API, or an interactive browser shell.
  - [2] 2026-11-24: the default idle timeout | capture: sha256:433b53224ae6374f949e604c6eb43d63ac0608c8000b57cd22cee529717870cc | quote: Seconds of inactivity before automatic shutdown (default `900`; `0` disables). Activity includes HTTP requests and shell interaction.
  - [2] 2026-11-24: the 500 MB cap per file written through the filesystem API | capture: sha256:433b53224ae6374f949e604c6eb43d63ac0608c8000b57cd22cee529717870cc | quote: PUT /fs/{path}` — write/replace a file (creates parent dirs; up to 500 MB).
- sources:
  - [1] https://apify.com/pricing
  - [2] https://apify.com/apify/ai-code-sandbox
  - [3] https://docs.apify.com/platform/actors
  - [4] https://console.apify.com/sign-up
  - [5] https://apify.com/agents.md
