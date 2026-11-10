# Nous Portal

> nousresearch.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nousresearch/ | JSON https://fshy.ajam.dev/api/v1/entity/nousresearch.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nous Portal

- `inference/nous-portal-free` | qualifies-with-caveat | evidence reported | category inference gateway, free plan with free models only | tier Free
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T06:15:49.151Z (live) | stale on 2026-11-19
- url https://portal.nousresearch.com/manage-subscription
- free tier: Free plan at $0 per month with $0 in monthly credits: access to the models marked FREE in the catalog only, at standard rate limits; a third-party plan table reads 50 RPM / 500K TPM | unit: mixed | metered on: request-count | read on: 2026-11-04 | source: [1] | note: the free model set rotates; the portal catalog page read on 2026-11-04 lists Reflection Beam 1.0 501B A23B, Crouton Alpha, StepFun Step 3.7 Flash and Upstage Solar Mini 4 as free; the true unit is a request and token rate with no volume cap, which no unit term names
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a Nous Portal account (email, Discord or wallet login); one first-hand third-party report states the Free plan is activated through a 0-yen payment screen that requires a credit card; another directory records no card requirement, so the card requirement is reported, not documented
- interface: rest
- limits:
  - request-rate: 50 RPM / 500K TPM per a third-party plan table; unverified on the vendor page, which prints only 'standard rate limits' and no numbers; unverified: behind a sign-up [1]
- tooling: OpenAI-compatible endpoint at https://inference-api.nousresearch.com/v1 per a third-party guide; the Hermes Agent CLI logs in through OAuth
- composes with: free models only; paid models and API keys draw on prepaid credits
- reliability: the free model list rotates and one report found only 6 of 10 listed free models answering
- evidence note: plan contents and the card requirement rest on third-party pages; the vendor plan page read shows the plan names and price but not the rate limits or the signup requirement.
- evidence:
  - [1] 2026-11-04: third-party plan table: Free plan is $0 with no monthly credits, free models only, 50 RPM / 500K TPM | capture: sha256:8f9d6b027445de62dc3f9c132854e40413d5e212a4d7d33d2bb7da045e3c61c4 | quote: | Free | $0 | $0 (free models only) | — | 50 RPM / 500K TPM |
  - [2] 2026-11-04: first-hand third-party report: the Free plan needs a card at a 0-yen checkout | capture: sha256:36e06ee5c28832581a8e0e3029e2544d5c43a31890d88f86e604803472c72ba9 | quote: However, even for the free plan, you must register a credit card when signing up.
  - [3] 2026-11-04: the portal model catalog marks models FREE | capture: sha256:41c87bc8743004d617e2b6a11b5d642580338881efa8e5ffd2a1c0363bed9c7d | quote: | #1 | Upstage: Solar Mini 4 | Text | FREE | — | — |
  - [4] 2026-11-04: a directory says the public page no longer shows the 50 RPM / 500K TPM figures | capture: sha256:89cb975ec7b573a10b39bf5a40da54f68c786412898b79302a413ff6bb608553 | quote: The public free-plan page checked on 2026-10-06 no longer exposes the earlier observed 50 RPM and 500k TPM.
  - [5] 2026-11-04: API keys draw on prepaid credits, not on plan usage | capture: sha256:48de04e6871ea390bc7865b60a641978b91a02bfb5325711a4089adaf191d6d0 | quote: API keys always use your credits (pay-as-you-go), not included usage
  - [1] 2026-11-04: third-party plan table gives 50 RPM / 500K TPM | capture: sha256:8f9d6b027445de62dc3f9c132854e40413d5e212a4d7d33d2bb7da045e3c61c4 | quote: | Free | $0 | $0 (free models only) | — | 50 RPM / 500K TPM |
- sources:
  - [1] https://openclawlaunch.com/guides/nous-portal
  - [2] https://note.com/hash_13/n/n4fe7799c48af?hl=en
  - [3] https://portal.nousresearch.com/models
  - [4] https://freeinferencing.com/provider/nous_portal/
  - [5] https://portal.nousresearch.com/manage-subscription
