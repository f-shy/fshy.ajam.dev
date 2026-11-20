# tunnl.gg

> tunnl.gg | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tunnl/ | JSON https://fshy.ajam.dev/api/v1/entity/tunnl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tunnl.gg

- `egress/tunnl-gg` | fails-egress | evidence reported | binding request-rate | category http tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-11-20
- url https://tunnl.gg/
- price USD 0
- free tier: A free localhost tunnel with a stable HTTPS URL. No signup, no client install. Stable URLs are tied to your SSH key; the server is open source (MIT). | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte allowance. Limits are per request and per connection: 128 MB per request and response body, 1 GB per direction per WebSocket connection, 3 tunnels per IP.; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: Any SSH key works; there is no account, sign-up or key registration. The subdomain is derived from the public key with HMAC-SHA256. | country: None
- interface: ssh
- limits:
  - request-rate (binding): 50 requests/s per tunnel, 25/s per visitor IP, 10 new SSH connections per minute per IP [1]
  - per-object-cap: 128 MB request and response body; 1 GB per direction per WebSocket [1]
  - per-object-cap: about 2.37 MiB (2,486,272 bytes) per request on the free anonymous tier probe:https://amber-mountain-1194d880.tunnl.gg/
- binding note: 1 TiB/month is 3.24 Mbit/s sustained, which the byte path could carry, but the 50 requests/s per tunnel and 128 MB body caps define what the service is for. Only port 80 is forwarded, so a UDP datagram has no path at all.
- interface detail: ssh -l stable -t -R 80:localhost:3000 proxy.tunnl.gg.
- tooling: OpenSSH only: ssh -t -R 80:localhost:3000 proxy.tunnl.gg.
- composes with: A zero-install webhook or demo endpoint; no path to UDP.
- reliability: TLS terminates at the edge, so it is not end-to-end encrypted; a phishing interstitial appears for first-time visitors; the server is MIT and self-hostable. A harness measured a 908 ms median latency and both 4 MiB transfers stopping at exactly 2,486,272 bytes, a per-request cap of about 2.37 MiB on the free anonymous tier.
- notes: SSH-based reverse tunneling service. Provides stable public hostnames derived from client SSH keys without requiring account registration.
- evidence note: A measured run would show the real throughput ceiling; the protocol limitation is already decisive for UDP. The anonymous tier caps a request at about 2.37 MiB and measures a 908 ms median latency (measured 2026-11-05).
- extras:
  - wg_path: none
  - wg_detail: Only port 80 is forwarded over SSH and served as HTTPS: ssh -t -R 80:localhost:3000 proxy.tunnl.gg. There is no UDP or raw TCP listener.
  - ingress: http-only
  - volume_stated: No byte allowance. Limits are per request and per connection: 128 MB per request and response body, 1 GB per direction per WebSocket connection, 3 tunnels per IP.
  - bytes_transit: yes
  - transit_note: The tunnl.gg edge terminates TLS and forwards down the SSH connection.
- evidence:
  - [1] 2026-10-23: SSH reverse tunnel on port 80 with a stable HTTPS URL per SSH key; limits table with 3 tunnels per IP, 50 requests/s per tunnel, 128 MB bodies, 1 GB per WebSocket direction.
  - [2] 2026-10-08: Launch date and pitch: stable localhost URLs over SSH with no installs, free to use, open-source MIT server.
  - probe:https://amber-mountain-1194d880.tunnl.gg/ 2026-11-05: both 4 MiB transfers stopped at exactly 2,486,272 bytes on the free anonymous tier | capture: sha256:d9a4448eae1c50e6b5c21e5805559775d026004936c60f84b1b2b08670a30998 | quote: EXACT same byte count (2,486,272 B
- sources:
  - [1] https://tunnl.gg/
  - [2] https://www.producthunt.com/products/tunnl-gg
