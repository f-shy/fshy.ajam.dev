# Mosaic Sandbox

> mosaicos.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mosaicos/ | JSON https://fshy.ajam.dev/api/v1/entity/mosaicos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mosaic Sandbox

- `compute/mosaic` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:40:40.205Z (live) | stale on 2026-12-26
- url https://sandbox.mosaicos.com/
- free tier: no free tier: $0.05 an hour of active compute with RAM and storage included, and $0 while hibernated | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Network egress is $0: outbound traffic carries no separate charge | metered: no | free allowance: unlimited outbound traffic at no charge | source: [1]
- identity: email | detail: Sign in with Google or GitHub to obtain a live msk_live_ key; a key can also be issued by email code in a browserless flow. No card or phone number is asked for on the key-creation page; payment goes through Stripe hosted checkout when billing is set up.
- interface: rest, cli, ssh
- limits:
  - request-rate (binding): $0.05 an hour of active compute, with RAM and storage included in that rate [1]
  - retention-clamped: a hibernated sandbox costs $0, so stopping is a pause rather than a loss [1]
- interface detail: REST API, the mos CLI, Python/TypeScript/Go SDKs, MCP and native SSH; a reachable endpoint is issued when SSH is enabled at creation
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the flat hourly rate and the hibernation rule. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: first-party: ses Pricing Benchmarks Roadmap Security Get Key No walled gardens A real Linux sandbox for any agent. Start in
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: hibernation costs nothing and the page states no automatic reap; SSH is available when enabled at creation
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: included in the $0.05 hourly rate
  - ps.durability: sandbox disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.ports: SSH when enabled at creation, with a reachable endpoint issued
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$0.05/hour active compute · Includes RAM and storage. $0 while hibernated' and 'Each sandbox runs on Firecracker/KVM. Agents can connect through the REST API, the mos CLI, Python, TypeScript, and Go SDKs, MCP, or native SSH.' quoted
  - [1] 2026-11-24: Mosaic charges USD 0.05 per hour of active compute with RAM and storage included and nothing while hibernated | capture: sha256:c0f2783442a1333d0c5b0453b8dcaf253625e86cc54f211f623ab87343f14b91 | quote: $0.05/hour active compute Includes RAM and storage. $0 while hibernated
  - [2] 2026-11-24: Mosaic documents zero-charge outbound network traffic | capture: sha256:e27f537c8d589a792b3d2ca873a896993bf76bf93b6bfe1b61fdd6114f6b7404 | quote: Network egress is $0: outbound traffic carries no separate charge.
  - [2] 2026-11-24: outbound traffic is not metered or capped by a separate charge | capture: sha256:e27f537c8d589a792b3d2ca873a896993bf76bf93b6bfe1b61fdd6114f6b7404 | quote: Network egress is $0: outbound traffic carries no separate charge.
  - [1] 2026-11-24: Mosaic publishes REST, CLI and SSH access to its sandboxes | capture: sha256:c0f2783442a1333d0c5b0453b8dcaf253625e86cc54f211f623ab87343f14b91 | quote: Each sandbox runs on Firecracker/KVM. Agents can connect through the REST API, the `mos` CLI, Python, TypeScript, and Go SDKs, MCP, or native SSH.
  - [1] 2026-11-24: Mosaic documents six client surfaces for its sandboxes | capture: sha256:c0f2783442a1333d0c5b0453b8dcaf253625e86cc54f211f623ab87343f14b91 | quote: Each sandbox runs on Firecracker/KVM. Agents can connect through the REST API, the `mos` CLI, Python, TypeScript, and Go SDKs, MCP, or native SSH.
  - [3] 2026-11-24: a key can be obtained through an email code without a browser sign-in | capture: sha256:765b9cabedc8f102f4a2a6e78e275dcf2e41922c1558368eed330fd55919e3ef | quote: No browser? Get a key by email code
  - [3] 2026-11-24: the key-creation page offers a Google sign-in route | capture: sha256:765b9cabedc8f102f4a2a6e78e275dcf2e41922c1558368eed330fd55919e3ef | quote: Loading Google…
  - [3] 2026-11-24: the key-creation page offers a GitHub sign-in route | capture: sha256:765b9cabedc8f102f4a2a6e78e275dcf2e41922c1558368eed330fd55919e3ef | quote: Loading GitHub…
  - [1] 2026-11-25: the page was read on 2026-11-25 and still states this value | capture: sha256:c0f2783442a1333d0c5b0453b8dcaf253625e86cc54f211f623ab87343f14b91 | quote: Hibernation is not billed, while active compute is billed at $0.05 per hour and RAM and storage are included.
- sources:
  - [1] https://sandbox.mosaicos.com/
  - [2] https://sandbox.mosaicos.com/docs/
  - [3] https://sandbox.mosaicos.com/start/
