# InstaVM

> instavm.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/instavm/ | JSON https://fshy.ajam.dev/api/v1/entity/instavm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## InstaVM

- `compute/instavm` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T13:20:54.188Z (live) | stale on 2026-12-25
- url https://instavm.io/pricing
- free tier: Free has a $0 base price, $50 of credits to start, 10 GB of included volumes and 5 active VMs, with a card kept on file and no charge to start; compute bills $0.000014 per vCPU-second and $0.0000045 per GB-RAM-second, and extra allocated volume storage $0.0002 per GB-hour | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Free plan includes egress to known package managers and common AI APIs; Pro adds unrestricted egress or granular domain/CIDR allowlists. No egress allowance or overage price is published on the pricing page. | metered: no | source: [1]
- identity: card | detail: a card is kept on file to deter abuse, with no charge to start; the signup page offers Google, GitHub or email and asks for full name, email and a password of at least 6 characters
- interface: rest, ssh, cli
- limits:
  - request-rate (binding): 5 simultaneously active VMs on Free, 100 on Pro [1]
  - per-object-cap: 10 GB of included volume storage on Free; volume billing uses allocated size, not bytes written [1]
- interface detail: RESTful API, the instavm Python SDK, the instavm CLI and ssh instavm.dev
- tooling: the instavm Python SDK (from instavm import InstaVM), the instavm CLI, and ssh instavm.dev
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The $50 is a one-time credit, while the active-VM count and the 10 GB volume are recurring plan limits, so both are recorded
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session clock published; the active-VM count is the bound
  - persistent_storage.included_gib: 10
  - persistent_storage.price_gib_month: extra volume billed on allocated size
  - persistent_storage.durability: volume
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while the volume exists
  - network_out.allow_outbound: yes
  - network_out.ports: Free includes egress to known package managers and common AI APIs only; Pro adds unrestricted egress or allowlists
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free has a $0 base price, $50 in free credits to start, 10 GB of included volumes ... No credit card required', and 'Your plan only limits how many can be active at once: 5 on Free, 100 on Pro', quoted
  - [1] 2026-11-03: free plan egress is allowlisted; no price | capture: sha256:5fc2050f1d5467b16e6d9c3541b1d012a4610acbd68dbc62b6353ebc7899b920 | quote: Free includes egress to known package managers and common AI APIs.
  - [2] 2026-11-03: a REST API exists | capture: sha256:7b08b57c223b2b40d18981275272c2cd781aff5b7683fca23855ed1a797dccce | quote: Execute AI agent code in isolated microVMs with RESTful API access and persistent state.
  - [2] 2026-11-03: an ssh interface exists | capture: sha256:7b08b57c223b2b40d18981275272c2cd781aff5b7683fca23855ed1a797dccce | quote: Run `ssh instavm.dev` from local shells, CI, or remote runners to create, connect, clone, share, and destroy VMs.
  - [1] 2026-11-03: free plan egress scope | capture: sha256:5fc2050f1d5467b16e6d9c3541b1d012a4610acbd68dbc62b6353ebc7899b920 | quote: Free includes egress to known package managers and common AI APIs.
  - [2] 2026-11-04: the home page documents a RESTful API | capture: sha256:7b08b57c223b2b40d18981275272c2cd781aff5b7683fca23855ed1a797dccce | quote: Execute AI agent code in isolated microVMs with RESTful API access and persistent state.
  - [2] 2026-11-04: the documented Python SDK is InstaVM | capture: sha256:7b08b57c223b2b40d18981275272c2cd781aff5b7683fca23855ed1a797dccce | quote: client = InstaVM(api_key="your_api_key")
  - [2] 2026-11-18:  | capture: sha256:4ae209473047cf343977a00b98d9b40fecfdcc6cc7fd6ada98cb6e94ab87ae86 | quote: When the session ends (kill, context exit, or lifetime expiry), VM state is destroyed.
  - [1] 2026-11-24: Free allows 5 active VMs, 100 on Pro, and 10 GB of included volumes with $0.0002 per GB-hour beyond | capture: sha256:5fc2050f1d5467b16e6d9c3541b1d012a4610acbd68dbc62b6353ebc7899b920 | quote: | Concurrent VMs | 5 | 100 | Unlimited |
  - [3] 2026-11-24: signup requires a card on file even on the free plan | capture: sha256:10b8348d7878da3f69029a9e8b3f8fb8641c4db03df3609e1c3e74da546984f8 | quote: Start for free. A card is kept on file to deter abuse; there is no charge to get started.
  - [3] 2026-11-24: a card is required at signup; registration also asks for name, email and password | capture: sha256:10b8348d7878da3f69029a9e8b3f8fb8641c4db03df3609e1c3e74da546984f8 | quote: Start for free. A card is kept on file to deter abuse; there is no charge to get started.
  - [1] 2026-11-24: the free plan requires a card on file and bills usage beyond the starting credits | capture: sha256:5fc2050f1d5467b16e6d9c3541b1d012a4610acbd68dbc62b6353ebc7899b920 | quote: Card on file, no charge to start
  - [1] 2026-11-24: free egress is limited to package managers and AI APIs; Pro adds unrestricted or allowlisted egress | capture: sha256:5fc2050f1d5467b16e6d9c3541b1d012a4610acbd68dbc62b6353ebc7899b920 | quote: Free includes egress to known package managers and common AI APIs. Pro adds unrestricted egress or granular domain/CIDR allowlists.
  - [2] 2026-11-24: the home page documents an SSH command interface | capture: sha256:4ae209473047cf343977a00b98d9b40fecfdcc6cc7fd6ada98cb6e94ab87ae86 | quote: ssh instavm.dev create --vcpu 4 --memory 8192
- sources:
  - [1] https://instavm.io/pricing
  - [2] https://instavm.io
  - [3] https://dashboard.instavm.io/auth/signup
