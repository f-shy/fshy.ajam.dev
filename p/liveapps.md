# liveapps.dev

> liveapps.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/liveapps/ | JSON https://fshy.ajam.dev/api/v1/entity/liveapps.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## liveapps.dev

- `egress/liveapps` | qualifies-with-caveat | evidence reported | binding retention-clamped | category relay (hosted, HTTPS tunnel, authless) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-10T03:20:00.000Z (live) | stale on 2026-11-25
- url https://liveapps.dev/
- free tier: Free with no account: a public HTTPS URL on *.liveapps.dev, a chosen subdomain, and one outbound WebSocket from the CLI to the relay. The page publishes no monthly quota; a sandbox measured the URL expiring after about an hour and a 30-second relay timeout that kills a multi-megabyte transfer. | unit: hours | metered on: wall-clock | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable: a tunnel; a transfer the relay timeout interrupts does not complete | source: [1]
- retention: not applicable: a live tunnel; the URL expires after about an hour | source: [1]
- egress: no byte quota is published; the relay's 30-second upstream timeout ends a transfer that has not finished, so a 4 MiB object returns a 504 page | metered: no | source: [1]
- identity: anonymous | detail: no account: the page's comparison table lists 'Account required | no', and the harness created a tunnel through the public API with no credentials
- interface: cli
- limits:
  - retention-clamped (binding): the public URL expires after about an hour probe:https://warped-wiry-wool.liveapps.dev/
  - request-rate: a 30-second relay timeout returns a 504 for a transfer that has not finished probe:https://warped-wiry-wool.liveapps.dev/
- binding note: the one-hour URL fails first for anything but a demo, and the 30-second timeout fails first inside that hour for a large transfer.
- interface detail: npx liveapps tunnel --port 3000 --name worldofz prints a https://<name>.liveapps.dev URL; the CLI keeps one outbound WebSocket to the relay
- tooling: the liveapps npm CLI on node; no agent or daemon
- composes with: a named subdomain makes it a usable webhook and demo lane; the one-hour URL and the 30-second timeout rule out file transfer and long-lived services
- reliability: the URL expires after about an hour and the relay returns a 504 after about 30 s on a transfer that has not finished; a sandbox measured a 223 ms median latency, the lowest of the authless set
- notes: The lowest median latency of the authless relays measured on 2026-11-05, at 223 ms. The 30-second relay timeout makes it a webhook and demo lane rather than a file-transfer lane, and the URL lasts about an hour.
- evidence note: the free and no-account claims are read from the vendor page; the one-hour expiry and the 30-second timeout are a sandbox measurement, so the record is reported rather than documented
- evidence:
  - [1] 2026-11-10: no account is required | capture: sha256:9cd353777c6df4bbcc4ef563d0c715873cf89782b7058a7eba38d0e45c50d868 | quote: | Account required | no |
  - [1] 2026-11-10: a custom subdomain is free | capture: sha256:9cd353777c6df4bbcc4ef563d0c715873cf89782b7058a7eba38d0e45c50d868 | quote: | Custom subdomain | yes |
  - probe:https://warped-wiry-wool.liveapps.dev/ 2026-11-05: the URL expires after about an hour | capture: sha256:de1014306d7aafba9c8afb95b55b8157e989a4a1b9e9ed7f96360b0a68698102 | quote: expires in ~1h
  - probe:https://warped-wiry-wool.liveapps.dev/ 2026-11-05: a 4 MiB transfer returns a 504 after about 30 s | capture: sha256:de1014306d7aafba9c8afb95b55b8157e989a4a1b9e9ed7f96360b0a68698102 | quote: 504 Gateway time-out after ~30 s
  - probe:https://warped-wiry-wool.liveapps.dev/ 2026-11-05: the /lat median was 223 ms | capture: sha256:de1014306d7aafba9c8afb95b55b8157e989a4a1b9e9ed7f96360b0a68698102 | quote: min 211 / med 223 / p95 295 ms
- sources:
  - [1] https://liveapps.dev/
