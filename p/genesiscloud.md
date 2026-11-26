# Genesis Cloud

> genesiscloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/genesiscloud/ | JSON https://fshy.ajam.dev/api/v1/entity/genesiscloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Genesis Cloud

- `compute/genesis-cloud` | trial-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone yes, ID no, institution no | verified 2026-11-02T02:17:36.633Z (live) | stale on 2026-12-03
- url https://support.genesiscloud.com/support/solutions/articles/47001101437-quotas-and-instances
- free tier: trial credits exist and the amount is not published. The vendor's own billing article states 'Once your trial credits are used up, any additional charges will be billed to the card attached to your account', and the onboarding articles require an SSH public key, a verified phone number and a valid credit card before an instance launches. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: card plus phone plus an SSH key: 'Make sure to upload an SSH key, besides verifying your phone number and adding a valid credit card. Once this is done, your basic setup is done'. The card must be 3D Secure and a card already attached to another Genesis Cloud account is refused by default; Genesis places a temporary USD 1 hold that 'is not a charge and will be automatically released after 7 days', and refuses prepaid cards by default. Charges after the trial are 'billed to the card attached to your account on the first of each month'. SEPA Direct Debit in EUR is accepted 'alongside cards and wire transfers'.
- interface: ssh
- limits:
  - write-gated (binding): the onboarding wall binds before any credit is spent: phone verification, an SSH key and a card on file are all required, and a quota request follows for GPU classes. [1]
- limits note: the onboarding wall binds before any credit is spent: phone verification, an SSH key and a card on file are all required, and a quota request follows for GPU classes.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the prepaid balance lasts up to three years, which makes Genesis a place to park a balance rather than a credit to spend quickly; the trial credit itself is short-lived and unquantified.
- reliability: no reliability event recorded
- notes: The amount is the open question and it is left null rather than guessed. A vendor blog post from 2022 states USD 15 on signup; referral sites in 2026 advertise USD 100 through a referral link. Neither is a current vendor page, so neither is recorded as the amount. The GPU rate table on genesiscloud.com/pricing did not render through two extraction routes, so no rate is recorded and no GPU-hours are derivable.
- extras:
  - facets.class: trial-credit
  - facets.free_tier_kind: trial-credit
  - payment_methods.card_at_signup: yes
  - payment_methods.debit: not published: https://support.genesiscloud.com/support/solutions/articles/47001108985-payment-methods
  - payment_methods.prepaid: refused
  - payment_methods.virtual: not published: https://support.genesiscloud.com/support/solutions/articles/47001108985-payment-methods
  - payment_methods.hold_amount: USD 1
  - payment_methods.hold_detail: 'To verify that your card is valid, we place a temporary $1 hold on the card. This is not a charge and will be automatically released after 7 days.' Cards without 3D Secure, prepaid cards and cards already attached to another Genesis Cloud account are refused by default, and a card in one of those classes can be whitelisted on request.
  - payment_methods.identity: a card, a verified phone number and an SSH key
  - payment_methods.source_url: https://support.genesiscloud.com/support/solutions/articles/47001108985-payment-methods
  - payment_methods.read_on: 2026-11-02
- evidence:
  - [1] 2026-10-22: 'Once your trial credits are used up, any additional charges will be billed to the card attached to your account on the first of each month', quoted
  - [2] 2026-10-22: 'Make sure to upload an SSH key, besides verifying your phone number and adding a valid credit card. Once this is done, your basic setup is done', quoted
  - [3] 2026-10-22: 'Your account can be funded in advance in USD (other currencies are available upon request). It's flexible, valid for up to 3 years'; SEPA Direct Debit (EUR) accepted alongside cards and wire transfers, quoted
  - [4] 2026-11-02: the hold is USD 1, is not a charge, and is released after 7 days | capture: sha256:6f3de062c884bdf95bc029a79e3c815b7980f9910e5cfcf1b221e979d71ee0e4 | quote: To verify that your card is valid, we place a temporary $1 hold on the card. This is not a charge and will be automatically released after 7 days.
  - [4] 2026-11-02: prepaid cards, cards without 3D Secure and cards used on another account are refused by default | capture: sha256:6f3de062c884bdf95bc029a79e3c815b7980f9910e5cfcf1b221e979d71ee0e4 | quote: Payment Methods Not Accepted by Default: Prepaid cards Cards without 3D Secure authentication Cards already associated with another Genesis Cloud account
  - [5] 2026-11-02: the same hold text is in the 2025-03-16 archived copy of the article | capture: sha256:211bb173ff73419a22b536842cc57f4403a0c8c79dc1dc2ad91c67898fab0213 | quote: In order to verify cards are valid, we place a 1USD hold on the card that will release after 7 days.
  - [4] 2026-11-02: the card requirement is a 3D Secure secured credit card | capture: sha256:6f3de062c884bdf95bc029a79e3c815b7980f9910e5cfcf1b221e979d71ee0e4 | quote: we only accept credit cards secured with 3D Secure authentication
- sources:
  - [1] https://support.genesiscloud.com/support/solutions/articles/47001101437-quotas-and-instances
  - [2] https://support.genesiscloud.com/support/solutions/articles/47001101437
  - [3] https://www.genesiscloud.com/blog/tos-privacy-update-may-2025
  - [4] https://support.genesiscloud.com/support/solutions/articles/47001108985-payment-methods
  - [5] https://web.archive.org/web/20250316133337/https://support.genesiscloud.com/support/solutions/articles/47001108985-payment-methods?provider=wayback
