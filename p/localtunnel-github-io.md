# localtunnel

> localtunnel.github.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localtunnel-github-io/ | JSON https://fshy.ajam.dev/api/v1/entity/localtunnel-github-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## localtunnel

- `egress/localtunnel` | qualifies-with-caveat | evidence documented | binding none | category tunnel (hosted, shared instance)
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-12-06
- url https://localtunnel.github.io/www/
- free tier: a unique public URL proxied to a local server, with no published limits | unit: unlimited | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: the assigned subdomain is random per run | source: [1]
- egress: no quota published anywhere: the project page states a URL and no limit | metered: no | source: [1]
- identity: anonymous | detail: no account to use the shared server
- interface: cli
- limits:
  - per-ip-shaping: no published limit: the original author wrote 'There are no limitations - abuse happens, server goes down, comes back up sometime later' [2]
  - per-ip-shaping: about 20-22 kB/s on the public instance, with multi-second stalls probe:https://eleven-ways-accept.loca.lt/
- binding note: No byte figure exists anywhere: the author says there are no limitations and the current maintainer explains outages as CPU saturation, so the failure mode is the single volunteer instance rather than a meter. A user measured about 0.8 Mbit/s download through it in 2019, which would cap a month near 260 GB, but that is that instance on that day.
- interface detail: npx localtunnel --port PORT against the shared localtunnel.me server
- tooling: the npm package, or the standalone binary
- composes with: composes with an origin and nothing that needs a published ceiling; the shared server is someone else's capacity and is the first thing to break.
- reliability: the shared server is a single volunteer-run instance with no published capacity; a harness measured about 20-22 kB/s with multi-second stalls, so a 4 MiB transfer does not complete. unverified: the age of the client repository, no capture holds a push date.
- notes: Open-source HTTP reverse tunnel service. Operates shared public gateway instances with unmetered byte allowances, constrained by server capacity and uptime. A sandbox measured about 20-22 kB/s with multi-second stalls on 2026-11-05. unverified: the age of its client repository, no capture holds a push date.
- evidence note: the public instance works end to end at about 20-22 kB/s with multi-second stalls (measured 2026-11-05); the client repository activity was not checked against a capture.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the shared server proxies the origin's bytes
- evidence:
  - [1] 2026-10-22: the project page states that it assigns a unique public URL and says nothing about a limit, which is a documented absence
  - probe:https://localtunnel.me/ 2026-10-22: the bare host answers 302 and the project docs live at localtunnel.github.io/www/, so there is no vendor pricing page to read
  - [2] 2026-11-03: a project contributor states there is no published limit on the shared server | capture: sha256:0f9481d7e29e9e13e49d3666c4ef7ba94803870678877db4435e12d79efafb6b | quote: There are no limitations - abuse happens, server goes down, comes back up sometime later :)
  - [1] 2026-11-03: the project page states a public URL proxied to a local server and lists no byte or rate limit | capture: sha256:e06dfea03a86ad96d64a06912b48b36a7067d35311a47ac16fd132f080c813f9 | quote: Localtunnel will assign you a unique publicly accessible url that will proxy all requests to your locally running webserver.
  - probe:https://eleven-ways-accept.loca.lt/ 2026-11-05: the public instance transfers at about 20-22 kB/s and stalls for seconds | capture: sha256:6a6c3be02c5b9d27b271bb356b1a20eb2c6d0b11f756ae0b892e6f049463f5e2 | quote: hit 85 s cap having pulled only 1.87 MiB
  - probe:https://eleven-ways-accept.loca.lt/ 2026-11-05: the public instance transfers at about 20-22 kB/s | capture: sha256:6a6c3be02c5b9d27b271bb356b1a20eb2c6d0b11f756ae0b892e6f049463f5e2 | quote: hit 85 s cap having pulled only 1.87 MiB
- sources:
  - [1] https://localtunnel.github.io/www/
  - [2] https://github.com/localtunnel/localtunnel/issues/288
