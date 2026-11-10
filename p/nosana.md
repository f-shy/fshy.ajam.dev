# Nosana

> nosana.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nosana/ | JSON https://fshy.ajam.dev/api/v1/entity/nosana.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nosana

- `compute/nosana` | trial-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T09:23:30.180Z (live) | stale on 2026-12-03
- url https://nosana.com/
- free tier: The USD 50 is real as an announcement but not as a standing offer. Quoted from the 2026-03-13 post: 'You can now claim $50 in free GPU credits instantly on the Nosana website. No extra steps, no waiting'. Quoted from the November 2025 and October 2025 monthly posts and still live: 'Your credits will be activated and assigned within a few days', and 'you can join the early-access list. No commitment. No payment.' Quoted from the June 2026 post: 'You can verify a payment method to claim free credits or top up your balance'. The live site states only: 'Claim free credits when you log in with email' with no amount. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-off-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Also not established: whether credits cover storage or egress separately, since Nosana bills compute from the balance and does not publish a separate storage line. | metered: yes | source: [1]
- identity: card | detail: two routes with different costs. On the current route a payment method must be verified: the June 2026 post states 'You can verify a payment method to claim free credits or top up your balance'. On the early-access route there is no payment at all, quoted 'No commitment. No payment.', with credits activated within a few days. The live site states only 'Claim free credits when you log in with email'. No hold amount and no card-type rule is published; cards are attached through a Stripe SetupIntent, which creates no charge.
- interface: unknown
- limits:
  - write-gated (binding): Two gates fail before the money does: the grant is not self-serve at a stated amount, since the current route is an early-access list with activation 'within a few days' and the June 2026 route is payment-method verification; then supply fails, because the site reports 0 of 16 hosts on the USD 0.048 RTX 3060 and 2 of 39 on the USD 0.192 RTX 3090. [1]
- limits note: Two gates fail before the money does: the grant is not self-serve at a stated amount, since the current route is an early-access list with activation 'within a few days' and the June 2026 route is payment-method verification; then supply fails, because the site reports 0 of 16 hosts on the USD 0.048 RTX 3060 and 2 of 39 on the USD 0.192 RTX 3090.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The USD 50 does not chain with anything, because the cheap card it was priced against has no host and the cards that do have hosts cost four times as much. If granted, USD 50 is 260 hours on the RTX 3090 that 2 of 39 hosts offer, or 100 hours on a 5090 with 0 of 38 hosts free.
- reliability: no reliability event recorded
- notes: The June 2026 post puts the same grant behind payment-method verification, so the identity cost is card on that route and the email route has no published amount. The division is correct (50 / 0.048 = 1,042 GPU-hours) and it is not reachable. Not established: any credit expiry term. The docs state none; no page was found that states one. Also not established: whether credits cover storage or egress separately, since Nosana bills compute from the balance and does not publish a separate storage line. No third-party account of spending a Nosana credit was found. The one recorded is the better-evidenced.
- extras:
  - facets.class: decentralized-gpu-marketplace
  - facets.free_tier_kind: one-off-credit
  - facets.shape.gpu_class: RTX 3090 at USD 0.192 per GPU-hour, the only card with host capacity
  - facets.shape.gpu_count: 1
  - payment_methods.card_at_signup: only on the credit-claim route
  - payment_methods.debit: not published: https://learn.nosana.com/api/payments.html
  - payment_methods.prepaid: not published: https://learn.nosana.com/api/payments.html
  - payment_methods.virtual: not published: https://learn.nosana.com/api/payments.html
  - payment_methods.hold_amount: not published
  - payment_methods.hold_detail: payment methods are attached through a Stripe SetupIntent ('payments.addMethod(request)' posts to '/payments/setup-intent'), which Stripe documents as creating no charge: 'It’s similar to a payment, but no charge is created.' Credits are bought in advance and consumed by deployments, so a card is charged at the purchase rather than per job. No hold amount and no card-type rule is published.
  - payment_methods.identity: email or a wallet; a payment method is verified on the credit-claim route
  - payment_methods.source_url: https://learn.nosana.com/api/payments.html
  - payment_methods.read_on: 2026-11-02
  - credit_gpu_hours_ceiling: 1042
  - credit_gpu_hours_ceiling_note: Rate-card ceiling, not capacity: it assumes the NVIDIA 3060 at USD 0.048 per hour can be rented, and the site's availability column lists that card at 0 / 15 hosts on 2026-11-02.
- evidence:
  - [1] 2026-10-22: probe status 200, 347708 bytes, sha256 a21f05160be36c8ebbc3b8204fb50504ce2146c6f224be0f9d4aa3c7385141a3; the GPU table reports availability per card: NVIDIA 3060 USD 0.048 0/16 hosts, 4060 USD 0.064 0/5, 4070 USD 0.096 0/7, 3090 USD 0.192 2/39, 4090 USD 0.400 0/94, 5090 USD 0.500 0/38, H100 USD 1.500 0/0
  - [2] 2026-10-22: 47 markets; the renter price derived from nos_job_price_per_second against the NOS price implied by usd_reward_per_hour reproduces the site table exactly (3060 USD 0.0480, 3090 USD 0.1919, 4090 USD 0.4000, 5090 USD 0.5000, A100 80GB USD 0.8999), each with a 10% network fee; the nodes array is empty for every market, so this endpoint carries no supply data
  - [3] 2026-07-01: quoted: 'You can verify a payment method to claim free credits or top up your balance', which puts the credit behind a payment instrument as of June 2026
  - [4] 2026-10-22: quoted: credits.request() is 'Request free credits (subject to eligibility)' behind a checkEligibility() call, and deployments fail with INSUFFICIENT_FUNDS at zero balance; no amount, expiry or coverage term is stated in the docs
  - [5] 2026-10-22: post dated 2026-03-13 says new users claim USD 50 in free GPU credits on the site with no extra steps
  - [6] 2026-10-22: quoted: claim free credits when you log in with email; wallet is optional; probe returned status 200, 231506 bytes, sha256 da179e374df3391e2d7089bf21d53e1347361c2c04d4f942223838a5eee5a9cc
  - [4] 2026-10-22: credits.request() is 'Request free credits (subject to eligibility)', with a checkEligibility() call, so the grant is conditional and not automatic
  - [7] 2026-10-22: Nosana states on its own site that the NVIDIA 3060 is USD 0.048/hour and the 3080 USD 0.096/hour
  - [8] 2026-10-22: the October 2026 post replaces the instant claim with a list: quoted, join the early-access list, no commitment and no payment, and your free credits will be activated and assigned within a few days
  - [5] 2026-10-22: quoted: 'Instantly claim $50 in free GPU credits - directly on the site ... No extra steps, no waiting'.
  - [8] 2026-10-22: quoted: join the early-access list, no commitment, no payment, and 'Your free credits will be activated and assigned within a few days'
  - [9] 2026-10-22: 
  - [10] 2026-11-02: card payment methods are held by Stripe, which sets the verification flow | capture: sha256:799fa7dad5390a7ddeb09a432e967c87bcecd0b4c15d22cd542ab6098252126b | quote: The Payments API manages payment methods and credit purchases, backed by Stripe.
  - [10] 2026-11-02: the card rail is Stripe's | capture: sha256:799fa7dad5390a7ddeb09a432e967c87bcecd0b4c15d22cd542ab6098252126b | quote: backed by Stripe
  - [11] 2026-11-02: a SetupIntent attaches a card and charges nothing | capture: sha256:3dc3d518464e636a0175ce8acca5ddc7780a690d9ad6be985ddb94ddb484fa6c | quote: It’s similar to a payment, but no charge is created.
  - [10] 2026-11-02: the payment rail is unchanged | capture: sha256:799fa7dad5390a7ddeb09a432e967c87bcecd0b4c15d22cd542ab6098252126b | quote: The Payments API manages payment methods and credit purchases, backed by Stripe.
  - [1] 2026-11-02: Credit: USD 50, announced at https://nosana.com/blog/the-new-nosana-experience-is-now-live/ ('claim $50 in free GPU credits'). Rate: the GPU table lists the NVIDIA 3060 at USD 0.048 per hour, the lowest rate in the table. 50 / 0.048 = 1,041.67 GPU-hours, rounded to 1,042. | capture: sha256:170bb7df213e319d2197d2fa493a8c534dea96e5ff3a6457e5f141e7d372e6c2 | quote: NVIDIA 3060 $0.048/h
  - [5] 2026-11-02: The 2026-03-13 post announces USD 50 in free GPU credits claimable on the Nosana website. | capture: sha256:ff43bc50748dfd58a516169ee7ebe078bb64672d9954c47889377e6d0a32bbc4 | quote: claim $50 in free GPU credits instantly on the Nosana website
  - [1] 2026-11-02: The GPU table lists the NVIDIA 3060 at $0.048/h with availability 0 / 15 hosts. | capture: sha256:170bb7df213e319d2197d2fa493a8c534dea96e5ff3a6457e5f141e7d372e6c2 | quote: NVIDIA 3060 $0.048/h 0 / 15 hosts
  - [1] 2026-11-02: The home page describes Nosana as an open-source GPU cloud. | capture: sha256:170bb7df213e319d2197d2fa493a8c534dea96e5ff3a6457e5f141e7d372e6c2 | quote: An open-source GPU cloud built for AI and high-performance workloads
- sources:
  - [1] https://nosana.com/
  - [2] https://api.nosana.com/markets
  - [3] https://nosana.com/blog/nosana-monthly-june-2026/
  - [4] https://learn.nosana.com/api/credits.html
  - [5] https://nosana.com/blog/the-new-nosana-experience-is-now-live/
  - [6] https://nosana.com/gpu-workloads/
  - [7] https://nosana.com/blog/cloud-gpu-providers-compared/
  - [8] https://nosana.com/blog/nosana-monthly-october-edition/
  - [9] https://redlib.vanillax.me/r/Nosana_AI
  - [10] https://learn.nosana.com/api/payments.html
  - [11] https://docs.stripe.com/payments/setup-intents
