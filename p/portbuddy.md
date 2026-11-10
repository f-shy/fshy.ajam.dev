# Port Buddy

> portbuddy.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/portbuddy/ | JSON https://fshy.ajam.dev/api/v1/entity/portbuddy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Port Buddy

- `egress/port-buddy` | qualifies-with-caveat | evidence documented | binding none | category udp tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:00.065Z (live) | stale on 2026-12-05
- url https://portbuddy.dev/
- price USD 0
- free tier: HTTP and UDP tunnels are free. No credit card. TCP tunnels from $5/month. Transfer is unmetered on every plan: no bandwidth caps, no overage charges. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Transfer is unmetered on every plan: no bandwidth caps, no overage charges. HTTP and UDP tunnels are free; TCP tunnels start at USD 5/month. | metered: no | free allowance: unmetered, per the vendor's own sentence; no number because no cap is claimed | source: [1]
- identity: email | detail: "Start for free" and "No credit card"; the free tier requires an account, no card. | country: None
- interface: cli, rest
- limits:
  - per-ip-shaping: no byte number: the vendor states transfer is unmetered with no caps and no overage charges, and its terms name 'high-traffic production workloads beyond your subscription limits' as abuse of the infrastructure [1]
  - per-object-cap: HTTP tunnel requests are capped at 10 MB [3]
- limits note: the vendor reserves the right to throttle, suspend or block an account or tunnel it judges abusive
- binding note: The vendor claims no byte cap on any plan, so nothing in the vocabulary binds at 1 TiB/month. The unestablished part is not volume but performance and stability: no live tunnel was run, and the free endpoint is a vendor-assigned hostname that would break a stable WireGuard address if it changes per session.
- interface detail: CLI install and a web dashboard; "Install the CLI".
- tooling: The vendor CLI: "$portbuddy tcp 5432"; a udp subcommand is advertised.
- composes with: Port Buddy UDP plus a local wg-quick listener gives an endpoint with no VM, at the cost of a vendor-controlled hostname.
- reliability: Tunnel hostname is vendor-assigned; the public port comes from a reservation in the range 40000-60000 that is reused for the same local port, so the address tends to keep working; a UDP tunnel with no traffic for five minutes is cleaned up.
- notes: Not a PaaS: a tunnel in front of a client process, so it belongs with ngrok, pinggy and zrok rather than with the platforms. Free tier is advertised as one HTTP or UDP tunnel. The record's egress field said 'none published' and the plan carries an explicit unmetered sentence that was not found on the page first read. Turns 'none published' into a documented absence with the vendor's own words, which is the strongest form a no-number finding can take. Replaces a volume-quota entry that read 'no published byte allowance' with the vendor's affirmative no-cap statement, which is a different claim. No byte constraint is claimed by the vendor, so volume-quota is the wrong kind; what a reader plans against is a vendor-controlled hostname and an unmetered but unstated relay capacity. The record's note reasoned that a free tier is 'normally shaped below 1 TiB', which the vendor's own page now contradicts. The offer and the absence of a cap are both on a vendor page with a URL and a date, which is the documented rung. The record was unverified because the first page read carried no volume sentence. Names what remains unproven now that the offer itself is documented.
- evidence note: The free UDP offer and the no-cap sentence are quoted from the vendor with a date. What stays unverified is the transport: no tunnel was run, so throughput, session lifetime and hostname churn on the free tier are unmeasured, and a measured push would raise the rung.
- extras:
  - wg_path: inside-udp
  - wg_detail: The free tier exposes a public UDP endpoint that forwards datagrams to a local UDP socket, so a WireGuard handshake can be carried inside it.
  - ingress: udp
  - volume_stated: The vendor publishes no monthly byte allowance for the free UDP tunnel; the only stated limits are tunnel count and TCP being paid.
  - bytes_transit: yes
  - transit_note: Port Buddy relays the datagrams; the local process terminates them.
- evidence:
  - [2] 2026-10-23: "HTTP and UDP tunnels are free. No credit card." and "UDP is free; tcp tunnels from $5/month"
  - [4] 2026-10-23: 'You get back a public host and port, such as net-proxy-2.portbuddy.dev:41207, and datagrams sent there are forwarded to your local socket. Unlike TCP tunnels, UDP is available on every plan.'
  - [3] 2026-11-03: an HTTP tunnel caps a single request at 10 MB | capture: sha256:4871a63ec0a1412975aafc8ef3571ba679b6609e65d8e13dd91cfec19f0d370f | quote: Requests are capped at 10 MB, which is worth knowing before you test a large file upload.
  - [5] 2026-11-03: the terms give a fair-use line for traffic with no byte figure | capture: sha256:b7e897cb7242d9bf6fa9aa3988e4001c46907eac2a69126b83f2f06d30439385 | quote: Using the Service for high-traffic production workloads beyond your subscription limits, or otherwise abusing infrastructure resources.
  - [5] 2026-11-03: the terms reserve throttling, suspension and blocking | capture: sha256:b7e897cb7242d9bf6fa9aa3988e4001c46907eac2a69126b83f2f06d30439385 | quote: to investigate, monitor for abuse, throttle, suspend, block, or permanently terminate any account or tunnel
  - [4] 2026-11-03: an idle UDP tunnel is removed after five minutes; the same page says a reservation is reused for the same local port | capture: sha256:9e350a05949d561e879a1a764817a089f84ae39d427cb64c3210cbb629dd20c4 | quote: A UDP tunnel that sees no traffic at all for five minutes is cleaned up, since there is no connection close to detect.
  - [2] 2026-11-03: the vendor states no bandwidth cap and no overage charge on any plan | capture: sha256:261b04340a015b22823ff2ec890414171b2175ce14e0f54634289a66ce246654 | quote: Transfer is unmetered on every plan: no bandwidth caps, no overage charges.
  - [5] 2026-11-04: the terms name high-traffic production use beyond subscription limits as abuse and publish no byte cap | capture: sha256:b7e897cb7242d9bf6fa9aa3988e4001c46907eac2a69126b83f2f06d30439385 | quote: Using the Service for high-traffic production workloads beyond your subscription limits, or otherwise abusing infrastructure resources.
- sources:
  - [1] https://portbuddy.dev/install
  - [2] https://portbuddy.dev/
  - [3] https://portbuddy.dev/docs/http-tunnels
  - [4] https://portbuddy.dev/docs/udp-tunnels
  - [5] https://portbuddy.dev/terms
