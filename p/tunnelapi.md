# TunnelAPI 1.0

> tunnelapi.in | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnelapi/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnelapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TunnelAPI 1.0

- `egress/tunnelapi-1-0` | fails-quota | evidence unverified | binding volume-quota | category overlay network or advanced tunnel tool | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T10:32:52.501Z (live) | stale on 2026-11-18
- url https://tunnelapi.in/
- price USD 0
- free tier: Free plan, 0 rupees a month: 1 user, 1 active tunnel, 2 webhook endpoints, 1K HTTP requests a month, 100 MB bandwidth a month, a random subdomain, a 2 hour session limit. | unit: MB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Free plan: 100 MB bandwidth a month and 1K HTTP requests a month, 1 active tunnel, 2 hour session limit.; ingress: http-only | metered: no | free allowance: 100 MB bandwidth a month | source: [1]
- identity: email | detail: An account on the hosted service: 'Login with Google, GitHub, or email'; the page shows no card or phone step for the Free plan. | country: None
- interface: cli
- limits:
  - volume-quota (binding): Free plan: 100 MB bandwidth a month and 1K HTTP requests a month; 1 active tunnel; 2 hour session limit [1]
- binding note: The Free plan's 100 MB bandwidth a month is the first failure, far below a 1 TiB/month need; the paid Solo plan lists 5 GB a month and Team 50 GB a month. The numbers are read in a copy of the vendor page archived 2026-06-14.
- interface detail: arm CLI (npm package api-response-manager): arm login, arm tunnel 3000 -s myapp, arm serve ./dist.
- tooling: npm install -g api-response-manager (the arm CLI)
- composes with: Needs an account before any capacity is visible.
- reliability: unverified: sustained availability; a direct probe of https://tunnelapi.in/ ended in a connection timeout, and docs.tunnelapi.in answered with content.
- notes: Hosted tunnel service with an npm CLI. Plans: Free (0 rupees a month), Solo (749 rupees a month, 5 GB bandwidth), Team (2,399 rupees a month, 50 GB bandwidth), Enterprise (custom, unlimited). Free-plan tunnels get a random subdomain on free-tunnelapi.app.
- evidence note: The pricing numbers are read in a copy of the vendor page archived 2026-06-14 (v2.6.0); the documentation site docs.tunnelapi.in is read live; the live landing page yields only its title.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [3] 2026-10-23: list entry sentence: Expose localhost to the internet. Free secure tunneling as an ngrok alternative. Appears developer focused. MIT License . Written in TypeScript.
  - [1] 2026-11-03: the Free plan (0 rupees a month) includes 100 MB bandwidth a month; page copy archived 2026-06-14 | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 100 MB Bandwidth/mo
  - [1] 2026-11-03: authentication by arm login offers Google, GitHub or email | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: Login with Google, GitHub, or email
  - [1] 2026-11-03: the arm CLI opens a tunnel to a free-tunnelapi.app hostname | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: $arm tunnel 3000 -s myapp
  - probe:tunnelapi.in 2026-11-03: a direct probe of https://tunnelapi.in/ timed out on 2026-11-03 | capture: sha256:319c71ce11506d69af439044effc355323000a358b9ed1baec57931285a5b93d | quote: "error": "timeout"
  - [1] 2026-11-03: the Free plan includes 1K HTTP requests a month | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 1K HTTP Requests/mo
  - [1] 2026-11-03: the Free plan has a 2 hour session limit | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 2 Hour Session Limit
  - [1] 2026-11-03: the Free plan allows 1 active tunnel | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 1 Active Tunnel
  - [4] 2026-11-03: the documentation site answered with content on 2026-11-03 | capture: sha256:cac3ae2697a3336b00a5acb62f68c2d9e91aa701748780ba2700f77ce33967de | quote: Welcome to TunnelAPI - the developer-first platform for secure tunneling, API Gateway, Kubernetes Ingress, and webhook testing.
- sources:
  - [1] https://web.archive.org/web/20260614184746/https://tunnelapi.in/
  - [2] https://tunnelapi.in/
  - [3] https://github.com/anderspitman/awesome-tunneling
  - [4] https://docs.tunnelapi.in

## TunnelAPI 2.0

- `egress/tunnelapi-2-0` | fails-quota | evidence unverified | binding volume-quota | category tunnel service (hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T10:32:52.502Z (live) | stale on 2026-11-18
- url https://tunnelapi.in/
- price USD 0
- free tier: Free plan, 0 rupees a month: 1 user, 1 active tunnel, 2 webhook endpoints, 1K HTTP requests a month, 100 MB bandwidth a month, a random subdomain, a 2 hour session limit. | unit: MB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Free plan: 100 MB bandwidth a month and 1K HTTP requests a month, 1 active tunnel, 2 hour session limit.; ingress: http-only | metered: no | free allowance: 100 MB bandwidth a month | source: [1]
- identity: email | detail: An account on the hosted service: 'Login with Google, GitHub, or email'; the page shows no card or phone step for the Free plan. | country: None
- interface: cli
- limits:
  - volume-quota (binding): Free plan: 100 MB bandwidth a month and 1K HTTP requests a month; 1 active tunnel; 2 hour session limit [1]
- binding note: The Free plan's 100 MB bandwidth a month is the first failure, far below a 1 TiB/month need; the paid Solo plan lists 5 GB a month and Team 50 GB a month. The numbers are read in a copy of the vendor page archived 2026-06-14.
- interface detail: arm CLI (npm package api-response-manager): arm login, arm tunnel 3000 -s myapp, arm serve ./dist.
- tooling: npm install -g api-response-manager (the arm CLI)
- composes with: Needs an account before any capacity is visible.
- reliability: unverified: sustained availability; a direct probe of https://tunnelapi.in/ ended in a connection timeout, and docs.tunnelapi.in answered with content.
- notes: Hosted tunnel service with an npm CLI. Plans: Free (0 rupees a month), Solo (749 rupees a month, 5 GB bandwidth), Team (2,399 rupees a month, 50 GB bandwidth), Enterprise (custom, unlimited). Free-plan tunnels get a random subdomain on free-tunnelapi.app.
- evidence note: The pricing numbers are read in a copy of the vendor page archived 2026-06-14 (v2.6.0); the documentation site docs.tunnelapi.in is read live; the live landing page yields only its title.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [3] 2026-10-23: list entry sentence: With a lot of features for teams and enterprises, including the AI API Gateway (a single gateway to multiple models), API Workflow, and exposing localhost to th
  - [1] 2026-11-03: the Free plan (0 rupees a month) includes 100 MB bandwidth a month; page copy archived 2026-06-14 | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 100 MB Bandwidth/mo
  - [1] 2026-11-03: authentication by arm login offers Google, GitHub or email | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: Login with Google, GitHub, or email
  - [1] 2026-11-03: the arm CLI opens a tunnel to a free-tunnelapi.app hostname | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: $arm tunnel 3000 -s myapp
  - probe:tunnelapi.in 2026-11-03: a direct probe of https://tunnelapi.in/ timed out on 2026-11-03 | capture: sha256:319c71ce11506d69af439044effc355323000a358b9ed1baec57931285a5b93d | quote: "error": "timeout"
  - [1] 2026-11-03: the Free plan includes 1K HTTP requests a month | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 1K HTTP Requests/mo
  - [1] 2026-11-03: the Free plan has a 2 hour session limit | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 2 Hour Session Limit
  - [1] 2026-11-03: the Free plan allows 1 active tunnel | capture: sha256:a4088715041943f783c2c6b3febb44a7d94f20e5551f8a21bf423cb1516097df | quote: - ✓ 1 Active Tunnel
  - [4] 2026-11-03: the documentation site answered with content on 2026-11-03 | capture: sha256:cac3ae2697a3336b00a5acb62f68c2d9e91aa701748780ba2700f77ce33967de | quote: Welcome to TunnelAPI - the developer-first platform for secure tunneling, API Gateway, Kubernetes Ingress, and webhook testing.
- sources:
  - [1] https://web.archive.org/web/20260614184746/https://tunnelapi.in/
  - [2] https://tunnelapi.in/
  - [3] https://github.com/anderspitman/awesome-tunneling
  - [4] https://docs.tunnelapi.in
