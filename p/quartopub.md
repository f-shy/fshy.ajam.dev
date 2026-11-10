# Quarto Pub

> quartopub.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quartopub/ | JSON https://fshy.ajam.dev/api/v1/entity/quartopub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Quarto Pub

- `compute/quarto-pub` | dead | evidence documented | binding none | category publishing host | tier closed to new sign-ups
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://quartopub.com/
- free tier: no free tier available: 'Quarto Pub is closed to new sign-ups. Existing users can still sign in to manage their content.' | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: The site recommends Posit Connect Cloud instead.
- per-object cap: not applicable: the unit is a session, not an object
- retention: not applicable to a new user: sign-ups are closed
- egress: not applicable: sign-ups are closed | metered: no | source: [1]
- identity: email | detail: not available: sign-ups are closed
- interface: cli
- limits:
  - write-gated: sign-ups closed permanently [1]
- binding note: a closed signup is reached before any quota
- interface detail: the Quarto CLI publishes to it, for existing accounts
- tooling: the Quarto CLI, for existing accounts only
- composes with: nothing: closed, and it never ran compute anyway
- reliability: the vendor points users at Posit Connect Cloud as the replacement
- notes: Quarto Pub is a publishing destination for HTML documents and presentations rather than an arbitrary compute host; no background compute is provided.
- evidence note: the closure sentence is quoted from the site's own front page today.
- extras:
  - billing_model: free
  - price_arithmetic: not applicable: closed
  - free_tier_kind: closed
  - session_cap.restart_required: no
  - session_cap.note: not applicable
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: quoted: 'Quarto Pub is closed to new sign-ups. Existing users can still sign in to manage their content.'
  - [1] 2026-10-24: quoted: 'For more capable free hosting, publish to Posit Connect Cloud.'
- sources:
  - [1] https://quartopub.com/
