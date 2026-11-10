# Global Socket

> gsocket.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gsocket/ | JSON https://fshy.ajam.dev/api/v1/entity/gsocket.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Global Socket (gsocket)

- `egress/gsocket` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category tcp tunnel software with a public relay | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-12-06
- url https://www.gsocket.io/
- price USD 0
- free tier: Global Socket allows two workstations on different private networks to communicate with each other. Through firewalls and through NAT - like there is no firewall. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No byte, port or time limit is published on the project page; the relay is volunteer-run and carries no price.; ingress: tcp | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: a shared secret string is the only credential: 'gsocket -s ExampleSecretChangeMe /usr/sbin/sshd -D'. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): No quota is published, so an unpublished tolerance on a volunteer relay is what fails at 1 TiB/month. TCP only: a WireGuard peer cannot be reached through it. [1]
- binding note: No quota is published, so an unpublished tolerance on a volunteer relay is what fails at 1 TiB/month. TCP only: a WireGuard peer cannot be reached through it.
- interface detail: gsocket CLI.
- tooling: gsocket binary (C).
- composes with: TCP ingress for a VM without a card.
- reliability: Shared secret, no account: anyone holding the secret reaches the service, and the relay operator can see connection metadata. A harness measured a 2.6-3.1 s round trip per request through the public relay, the cost of an SRP-4096 handshake per connection plus the relay hop.
- notes: A free public relay with no account and end-to-end encryption, carrying TCP only. Closest thing here to a no-identity TCP ingress, which is why it is worth a measurement even though it is not UDP. A sandbox measured a 2.6-3.1 s round trip per request through the public relay on 2026-11-05.
- evidence note: Public relay provides encrypted socket tunneling. Relay throughput allowances are unmetered in documentation.
- extras:
  - wg_path: none
  - ingress: tcp
  - volume_stated: No byte, port or time limit is published on the project page; the relay is volunteer-run and carries no price.
  - bytes_transit: yes
- evidence:
  - [1] 2026-10-23: 'two workstations on different private networks to communicate'; SSH example over the relay; 'SRP-AES-256-CBC-SHA-End2End'
  - probe:https://gs.thc.org/ 2026-11-05: a relay round trip took 2.6-3.1 s per request | capture: sha256:f42fea71c93511808d109c6a1819d6dfa7f6ffb0436ec0eac2af331a84afe87b | quote: min 2.6 s / med 3.0 s / max 3.1 s
- sources:
  - [1] https://www.gsocket.io/
