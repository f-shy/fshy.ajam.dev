# Path.net

> path.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/path/ | JSON https://fshy.ajam.dev/api/v1/entity/path.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Path.net

- `egress/path-net` | paid-only | evidence unverified | binding none | category L4 anycast DDoS protection for game traffic | tier paid
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T12:11:59.479Z (live) | stale on 2026-11-19
- url https://path.net/
- price unverified
- free tier: No public plan, price or free tier: the service is sold after a consultation ('Talk with the Path team to explain your needs and goals.'). | unit: none | metered on: unstated | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unverified. Third-party pages disagree by two orders of magnitude: one reseller review lists 'VPS from $29/mo', a directory lists a Starter plan at EUR 300/mo, and a forum post estimates 'around $3/tb bandwidth'. None is first party.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: No self-serve sign-up is shown; the consultation form asks for name, email, company and a short description, with phone optional. Whether a card is taken at onboarding is unverified. | country: None
- interface: unknown
- limits:
  - volume-quota: unverified: no first-party allowance or price was read [1]
- binding note: Cannot be named: with no first-party allowance, price or forwarding model, no constraint can be shown to fail first.
- interface detail: not read
- tooling: unknown
- composes with: the same as tooling
- reliability: unverified: a direct HTTP request to https://path.net/ answers 307 redirecting to itself (11 hops); the landing page is readable only through a rendering reader.
- notes: BuyVM's wiki says its DDoS-protected IPs 'use the Path Network', which makes Path a wholesaler behind retail hosts rather than a self-serve product.
- evidence note: The landing page was read through a rendering reader and states that the getting-started path is a consultation with the vendor; no plan, price or allowance appears on it, so those stay unverified.
- extras:
  - wg_path: unknown
  - wg_detail: The gaming page says the filter 'Detects and blocks malicious traffic across Rust, FiveM, OpenVPN, WireGuard, and more'; the forwarding model and any UDP allowance are not stated.
  - ingress: udp
  - volume_stated: Unverified. Third-party pages disagree by two orders of magnitude: one reseller review lists 'VPS from $29/mo', a directory lists a Starter plan at EUR 300/mo, and a forum post estimates 'around $3/tb bandwidth'. None is first party.
  - bytes_transit: yes
  - transit_note: assumed from the product class, not from a page read
- evidence:
  - [1] 2026-10-23: nothing: the reader returned status 508 too-many-redirects at the sixth hop, so no page content was obtained
  - [1] 2026-11-04: the getting-started path is a consultation with the vendor, with no self-serve plan or price shown | capture: sha256:8c442892a74041bedf593dbb909fbf26ebc52967e771ada9ebddf425e0a273ef | quote: Talk with the Path team to explain your needs and goals. No technical prep required.
  - [2] 2026-11-04: the consultation form lists a phone number as optional beside the other fields | capture: sha256:3e72d6b86dbf5bb29a29d475fc6fe81c412b526d0a092d8c6a1ac7e7f1be4b88 | quote: Phone number (optional)
  - [3] 2026-11-04: the vendor names WireGuard among the protocols its gaming filter recognises | capture: sha256:20818ab6c1dedba9c84dda1ef3dcdbb121b516c31add52f568563ac0e6e7c48a | quote: Detects and blocks malicious traffic across Rust, FiveM, OpenVPN, WireGuard, and more without interrupting or slowing down gameplay.
  - probe:path.net 2026-11-04: a direct probe of the landing page answers 307 with a self-redirect | capture: sha256:346682c7e6800c993baf19ea1d57a56633eeff982b02450b0ced8f889a62e714 | quote: "status": 307
  - [1] 2026-11-04: the getting-started path is a consultation with the vendor | capture: sha256:8c442892a74041bedf593dbb909fbf26ebc52967e771ada9ebddf425e0a273ef | quote: Talk with the Path team to explain your needs and goals. No technical prep required.
  - [1] 2026-11-04: the landing page was read and its getting-started path is a consultation with the vendor | capture: sha256:8c442892a74041bedf593dbb909fbf26ebc52967e771ada9ebddf425e0a273ef | quote: Talk with the Path team to explain your needs and goals. No technical prep required.
- sources:
  - [1] https://path.net/
  - [2] https://path.net/get-a-consultation
  - [3] https://path.net/services/layer-7-gaming
