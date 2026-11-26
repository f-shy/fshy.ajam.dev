# Argent Cloud

> swmansion.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/swmansion/ | JSON https://fshy.ajam.dev/api/v1/entity/swmansion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Argent Cloud (iOS simulator runners)

- `compute/argent-cloud-ios-simulator-runners` | paid-only | evidence documented | binding volume-quota | category hosted iOS Simulator runner | tier Runner, up to 6 parallel simulators
- identity a placeholder: card and phone unknown | verified 2026-11-25T16:38:09.742Z (live) | stale on 2026-12-26
- url https://argent.swmansion.com/cloud/pricing/
- free tier: no free tier: one Runner is USD 299 per month with unlimited simulator time; the Argent toolkit itself has a free open-source offer, but the Cloud hardware rental has no published free minutes or credit | unit: none | metered on: none | read on: 2026-11-25 | source: [1] | note: none-published
- per-object cap: not applicable: the unit is a reserved Mac with iOS Simulators, not an object | source: [1]
- retention: not published on the page read: no retention period for simulator state is stated | source: [1]
- egress: not published on the page read: no egress allowance or price is stated | metered: no | source: [1]
- identity: email | detail: unverified: the checkout form shows a checkout email and the docs say one API key is issued per user and sent directly; the terms charge a payment method through a payment processor (Lemon Squeezy) but name no card, and further registration fields are behind a sign-up that was not entered
- interface: unknown
- limits:
  - volume-quota (binding): one Runner is up to 6 parallel iOS Simulators on a Mac reserved for one project for the whole month; self-serve checkout covers at most 4 Runners and a larger fleet needs sales [1]
- limits note: unlimited simulator time on the reserved Runner; the constraint is the number of Runners and the 6 parallel Simulators per Runner, plus activation that may take up to 2 business days.
- binding note: the per-Runner capacity of 6 parallel Simulators and the 4-Runner self-serve checkout ceiling bind first; no free minutes exist, so the first paid month is required.
- interface detail: a pool of network-accessible iOS Simulators reached over the network; Argent, Maestro, Appium, custom scripts and CI pipelines can connect; no published API, CLI or port list
- endpoint: https://docs.swmansion.com/argent/docs/cloud/fundamentals/getting-started/
- tooling: Argent, Maestro, Appium or custom scripts that connect to a remote Simulator; the app itself is built on a machine the customer supplies, because Argent Cloud supplies only Simulators, not a Mac to build on
- composes with: this is a partial compute offer: it sells Simulators on dedicated Apple hardware but no Mac to build the app and no machine for the agent, both of which must come from another record. A hosted service, not self-hosted software. Free credits are not published, so a paid Runner is the entry point.
- reliability: activation may take up to 2 business days (48 hours) after payment because of demand; the service is built and operated by an ISO/IEC 27001 certified company and reports complete isolation between customers.
- notes: Hosted iOS Simulators on dedicated Apple hardware reserved for one project, USD 299 per Runner per month (USD 0.41/hour at 730 hours) with up to 6 parallel Simulators and unlimited simulator time. It is a partial offer: the app must be built on a Mac the customer supplies. No free tier or credit is published. The USD 0.41/hour figure is the listed USD 299/month divided by 730 hours.
- evidence note: price, capacity, unlimited time and checkout fields are quoted from the vendor's own cloud pricing and cloud pages read on 2026-11-25; the simulator-only scope and activation time are quoted from the vendor's FAQ.
- extras:
  - shape.gpu_class: dedicated Apple hardware
  - shape.note: one Runner is a Mac reserved for one project, running up to 6 parallel iOS Simulators
  - billing_model: flat monthly fee per Runner, no hourly billing and unlimited simulator time
  - free_tier_kind: none-published
  - term: monthly, one Runner reserved for the whole month
  - price_arithmetic: USD 299/month ÷ 730 hours = USD 0.41/hour
  - status: available, self-serve up to 4 Runners
  - network_out.allow_outbound: yes
  - network_out.ports: network-accessible Simulators; no port list published
  - session_cap.restart_required: no
  - session_cap.note: unlimited simulator time for the month; no per-session cap published
- evidence:
  - [1] 2026-11-25: one Runner costs USD 299 per month | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: $ 299per Runner / month
  - [1] 2026-11-25: a Runner runs up to 6 parallel iOS Simulators | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: - Up to 6 iOS simulators running in parallel
  - [1] 2026-11-25: simulator time is unlimited, with no hourly billing | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: - Unlimited simulator time, no hourly billing
  - [1] 2026-11-25: the checkout form asks for a checkout email | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: Checkout email: \*
  - [2] 2026-11-25: the product is a pool of network-accessible iOS Simulators rather than a whole Mac | capture: sha256:ac0fe9bd6c76049312e3aef564bd013b219a4f1d29edb22e401280b1c3eccadd | quote: Argent Cloud is a pool of network-accessible iOS Simulators.
  - [2] 2026-11-25: activation can take up to 2 business days after payment | capture: sha256:ac0fe9bd6c76049312e3aef564bd013b219a4f1d29edb22e401280b1c3eccadd | quote: Due to high demand, activation may take up to 2 business days (48 hours).
  - [1] 2026-11-24: the runner is a flat USD 299 per month with unlimited simulator time and no hourly billing | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: $ 299per Runner / month
  - [1] 2026-11-24: the offer is dedicated Apple hardware with unlimited simulator time | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: Pay for dedicated Apple hardware, not for minutes. One monthly price per Runner, unlimited simulator time, no hourly billing.
  - [1] 2026-11-24: one runner runs up to 6 iOS simulators in parallel | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: - Up to 6 iOS simulators running in parallel
  - [1] 2026-11-24: self-serve checkout is limited to 4 runners and larger fleets need sales | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: Self-serve checkout covers up to 4 Runners. For a bigger fleet, talk to our sales team.
  - [1] 2026-11-24: the checkout form asks for an email address | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: Checkout email: \*
  - [3] 2026-11-24: the machine is released after 900 seconds idle and the server applies a 16-minute idle limit | capture: sha256:973fe4c763c6e41828883af63198059a1dd59fed788e1c2283ca9e361e483122 | quote: | Idle release | 900 seconds (15 minutes) | Set `SIM_REMOTE_IDLE_TIMEOUT_SECS` to change it. The server has its own idle limit of 16 minutes |
  - [3] 2026-11-24: one machine can be held at most 24 hours | capture: sha256:973fe4c763c6e41828883af63198059a1dd59fed788e1c2283ca9e361e483122 | quote: | Maximum time on one machine | 24 hours | Enforced by the server |
  - [3] 2026-11-24: a file uploaded by sim-remote is capped at 1 GiB | capture: sha256:973fe4c763c6e41828883af63198059a1dd59fed788e1c2283ca9e361e483122 | quote: | Upload size | 1 GiB | Applies to every file that `sim-remote` uploads |
  - [4] 2026-11-24: no simulator state survives a session | capture: sha256:7ff28906b991b52dc6530a2291fe189b9adfc310bd81f8cf551024cb6076997f | quote: Nothing survives a session. When a machine returns to your team, Argent Cloud revokes the credentials of the session, closes the live connections, erases every simulator, and rebuilds the session volume from a clean image.
  - [5] 2026-11-24: one API key is issued per user and sent directly | capture: sha256:e3c374ff5c30a74d685dbae7a2dc6284cc411c77828bf99c24ad7f77760cce7a | quote: We issue one API key per user and send it to you directly.
  - [6] 2026-11-24: access is through an authenticated API using a licence key | capture: sha256:79f9701fe386ceac314aae857678388c833e57ae6c947afc16f8a2bad4707ca0 | quote: Access is provided through an authenticated API and is authenticated by means of a licence key issued to the Customer, of which the Provider stores only a hashed representation.
  - [6] 2026-11-24: a trial period has no fee and converts automatically to the paid monthly subscription | capture: sha256:79f9701fe386ceac314aae857678388c833e57ae6c947afc16f8a2bad4707ca0 | quote: No Fee is charged during the Trial Period. Unless the Customer cancels before the Trial Period ends in accordance with Section 8.2, the Agreement automatically converts to a paid monthly subscription
  - [1] 2026-11-25: the order form asks for a checkout email | capture: sha256:b568fb865d2596c0f23204964c214716a27d61c36f6c716be9be49ee55e0ab97 | quote: Checkout email: \*
  - [5] 2026-11-25: an API key is issued to the user directly, with no card stated | capture: sha256:e3c374ff5c30a74d685dbae7a2dc6284cc411c77828bf99c24ad7f77760cce7a | quote: We issue one API key per user and send it to you directly.
- sources:
  - [1] https://argent.swmansion.com/cloud/pricing/
  - [2] https://argent.swmansion.com/cloud/
  - [3] https://docs.swmansion.com/argent/docs/cloud/reference/sessions/
  - [4] https://docs.swmansion.com/argent/docs/cloud/reference/security-and-data/
  - [5] https://docs.swmansion.com/argent/docs/cloud/fundamentals/getting-started/
  - [6] https://argent.swmansion.com/legal/cloud-terms-of-service
