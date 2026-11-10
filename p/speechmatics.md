# Speechmatics

> speechmatics.com | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/speechmatics/ | JSON https://fshy.ajam.dev/api/v1/entity/speechmatics.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Speechmatics (Compute)

- `compute/speechmatics` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-23T11:10:48.000Z (live) | stale on 2026-11-23
- url https://www.speechmatics.com/pricing
- free tier: 'Start with $100 in free credits, no card required', with the page data carrying 'signupCredits: 100' and a footnote 'No card required'. The headline 'from $0.121/hr' is two discounts stacked: the tooltip says 'Melia 1 Pre-recorded base rate: $0.24, model training: -33%, top-tier annual commitment: -25%'. At the base Melia-1 pre-recorded rate of USD 0.24 an hour, 100 / 0.24 = 416 hours of batch transcription; at the Melia-1 real-time base of USD 0.40 an hour, 250 hours. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an account on an email alone, and the pricing page states 'Start with $100 in free credits, no card required' with the page data carrying 'signupCredits: 100' and a 'No card required' footnote. No card is taken, so no hold exists and no debit or prepaid question arises.
- interface: unknown
- limits:
  - request-rate (binding): the credit is large and the discount ladder is the trap: the advertised USD 0.121 an hour requires opting into model training and a top-tier annual commitment, so a free account pays the USD 0.24 base rate and gets 416 hours rather than 826. [1]
- limits note: the credit is large and the discount ladder is the trap: the advertised USD 0.121 an hour requires opting into model training and a top-tier annual commitment, so a free account pays the USD 0.24 base rate and gets 416 hours rather than 826.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a free CI runner plus USD 100 of batch transcription covers 416 hours of audio at the base rate, which is a podcast or lecture archive transcribed once. What breaks: the discount is paid for with training data or an annual commitment, and the enhanced-accuracy model at USD 0.75 an hour cuts the same credit to 133 hours.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The gap between the headline USD 0.121 and the base USD 0.24 is the finding: a free account has no commitment to discount, so the honest number is 416 hours. Not established: expiry of the USD 100; the pricing page does not state one. Training opt-in is a technical setting on the account, recorded here as a rate condition and not as advice.
- evidence note: the pricing page was read on 2026-10-23 and states the USD 100, the no-card rule and the stacked discounts behind the headline rate
- extras:
  - facets.class: credit-large-enough-for-real-workload
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-23: quoted: 'Start with $100 in free credits, no card required', with the page data carrying 'signupCredits: 100' and the footnote 'No card required'
  - [1] 2026-10-23: quoted rate: 'Speech to Text from $0.121/hr', with the tooltip stating 'Melia 1 Pre-recorded base rate: $0.24, model training: -33%, top-tier annual commitment: -25%'
- sources:
  - [1] https://www.speechmatics.com/pricing

## Speechmatics (Inference)

- `inference/speechmatics` | trial-only | evidence documented | binding volume-quota | category speech-to-text and text-to-speech API, one-time signup credit
- needs card yes, phone unknown, ID no, institution no | verified 2026-11-03T07:34:03.379Z (live) | stale on 2026-12-04
- url https://www.speechmatics.com/pricing
- free tier: USD 100 credit grant at signup on the Free plan, no card required; one credit is worth one US dollar, and one balance covers Speech to Text, add-ons and Text to Speech. One-time, not a monthly allowance. Melia 1 pre-recorded base rate is USD 0.24 per hour. | unit: credits | metered on: unstated | read on: 2026-11-03 | source: [1] | note: models on the pricing page: Melia 1 (multilingual, 56 languages), Enhanced, Standard, Oak 1 (clinical language) and Linden 1 (voice agents), in batch (REST) and real-time (WebSocket) modes. unverified: whether the grant expires, because no vendor page read states a validity period; unverified: the rate for Text to Speech, which the pricing page names without a number
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: no payment card on the Free plan ('no payment card required'); signup is an email with a password or a Google or GitHub account, and an email signup must verify the address by a link; unverified: whether a phone number is asked
- interface: rest
- limits:
  - volume-quota (binding): USD 100 credit grant at signup, one-time; Melia 1 pre-recorded base rate USD 0.24 per hour [2]
  - request-rate: Free plan real-time sessions are capped at 2 concurrent (Pro 50); the batch API asks for no more than 10 new jobs per second and 50 job-status requests per second, with a backstop of 20,000 concurrent jobs [3]
- binding note: the one-time USD 100 credit is the ceiling for batch work; the 2 concurrent real-time sessions cap is a second wall for live audio
- interface detail: Batch REST API and real-time WebSocket API; an API key is created in the web portal; Python and JavaScript batch libraries
- tooling: Python and JavaScript libraries, or raw HTTP and WebSocket with an API key created in the portal
- composes with: the credit pays for batch transcription of recorded audio, which a free CI runner can post file by file; pair it with a free object store for the audio. The discounted headline rate on the pricing page needs a Pro plan with model training and a top-tier annual commitment, so a Free account pays the base rate.
- reliability: the Free plan runs on the granted credit only; adding a payment card moves the account to Pro, where usage beyond the granted credits is charged to the card
- evidence note: the credit, the card-free Free plan, the signup methods and the real-time and batch limits are quoted from vendor pages; the credit's expiry and the text-to-speech rate are unverified.
- evidence:
  - [1] 2026-11-03: USD 100 free credit with no card | capture: sha256:f35ab03e8cac3fc972f9790cf630d2c126394182efa1dd12d09f0c1dc4b1f183 | quote: Start with $100 in free credits, no card required.
  - [1] 2026-11-03: the Melia 1 pre-recorded base rate is USD 0.24 per hour | capture: sha256:f35ab03e8cac3fc972f9790cf630d2c126394182efa1dd12d09f0c1dc4b1f183 | quote: Melia 1 Pre-recorded base rate: $0.24
  - [1] 2026-11-03: one credit balance covers speech-to-text, add-ons and text-to-speech | capture: sha256:f35ab03e8cac3fc972f9790cf630d2c126394182efa1dd12d09f0c1dc4b1f183 | quote: One balance covers Speech to Text, add-ons and Text to Speech.
  - [1] 2026-11-03: Melia 1 is a 56-language multilingual model | capture: sha256:f35ab03e8cac3fc972f9790cf630d2c126394182efa1dd12d09f0c1dc4b1f183 | quote: - description: Our next-generation multilingual model. Transcribes 56 languages without choosing one up front, switches language mid-sentence.
  - [2] 2026-11-03: the Free plan is a USD 100 credit grant with no payment card | capture: sha256:c8813b382b2599d00932c6424e0caf6c8f400911173dfff618fb53ffc62f90c1 | quote: * Free. Get started with a $100 credit grant at no cost, with no payment card required.
  - [2] 2026-11-03: one credit is one US dollar and new sign-ups receive USD 100 | capture: sha256:c8813b382b2599d00932c6424e0caf6c8f400911173dfff618fb53ffc62f90c1 | quote: Billing is in credits: one credit is worth one US dollar. New sign-ups receive a $100 credit grant.
  - [4] 2026-11-03: signup is by email and password or Google or GitHub | capture: sha256:43acfbfa6c74704dfad3f0abbc5eaf691debbc8aa7986ed0b1ef80c2b4e1919e | quote: 2. Sign up with email and password, or with a supported OAuth provider (Google or GitHub).
  - [4] 2026-11-03: an email signup verifies the address by a link | capture: sha256:43acfbfa6c74704dfad3f0abbc5eaf691debbc8aa7986ed0b1ef80c2b4e1919e | quote: 3. If you signed up with email, verify your email address using the link sent to your inbox.
  - [3] 2026-11-03: the Free plan allows 2 concurrent real-time sessions | capture: sha256:48e5811c56eb0cd8e009d201c4e716b6a1147bbce8472f48cb80731f909bf67c | quote: | Free | 2 |
  - [5] 2026-11-03: the batch API rate guidance is 10 new jobs per second | capture: sha256:56585e923d43e978a082027f07c6b0f7e0a34f9ca99ebc9cb4da95150c0da21c | quote: * 10 new jobs per second (POST API calls)
  - [5] 2026-11-03: the batch API has a backstop of 20,000 concurrent jobs | capture: sha256:56585e923d43e978a082027f07c6b0f7e0a34f9ca99ebc9cb4da95150c0da21c | quote: * 20,000 concurrent jobs `HTTP 429 - Max concurrent running jobs exceeded` (POST API calls).
  - [6] 2026-11-03: an API key is created in the portal | capture: sha256:ccb82a6f095a15ab2a4e7ce5b839d7533dc0ecd329cdb6018165d1cebbe7c3eb | quote: [Create an API key in the portal here](https://portal.speechmatics.com/settings/api-keys), which you'll use to securely access the API.
- sources:
  - [1] https://www.speechmatics.com/pricing
  - [2] https://docs.speechmatics.com/administration/plans.md
  - [3] https://docs.speechmatics.com/speech-to-text/realtime/limits.md
  - [4] https://docs.speechmatics.com/administration/accounts.md
  - [5] https://docs.speechmatics.com/speech-to-text/batch/limits.md
  - [6] https://docs.speechmatics.com/speech-to-text/batch/quickstart.md
