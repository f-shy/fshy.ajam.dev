# Jamendo

> jamendo.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jamendo/ | JSON https://fshy.ajam.dev/api/v1/entity/jamendo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jamendo (artist upload)

- `storage/jamendo` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T13:25:55.251Z (live) | stale on 2026-12-10
- url https://www.jamendo.com
- free tier: The maximum size of a single file is 480 MB. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 480 MB per file | bytes: 480000000 | source: [1] | note: The upload help page states the maximum size of a single file is 480 MB.
- retention: unverified: no retention period stated by the provider | source: [1] | note: unverified: the upload help page describes flagged tracks as masked or removed but gives no retention period
- egress: Free streaming and free download for listeners; Jamendo monetises through licensing, not storage fees. | metered: no
- identity: email | detail: In the Create an account section, add your email address and password.
- interface: browser
- limits:
  - per-object-cap (binding): 480 MB per file [1]
  - write-gated: review step [1]
  - write-gated: review step means an upload can be refused [1]
- limits note: 480 MB per file; strict format spec (bit depth, sample rate, channel count all constrained); a track must be submitted to a Jamendo programme, so there is a review step.
- interface detail: Jamendo Artist web upload tab
- tooling: Jamendo Artist web dashboard; upload through the web tab.
- composes with: Tracks can be uploaded as singles or organized into albums.
- reliability: Lossless in, transcoded for streaming; Jamendo's model is sync licensing so the catalogue is public. No retention risk stated, but the review step means an upload can be refused.
- notes: No published per-account total; 480 MB per file, lossless only (WAV/FLAC/AIFF, 16 or 24-bit, 44.1 or 48 kHz, 1-2 channels).
- evidence note: the 480 MB per-file ceiling is stated on the Jamendo Artist upload page
- evidence:
  - [1] 2026-10-21: 'WAV, FLAC, or AIFF'; 'Bit depth: 16 or 24'; 'The maximum size of a single file is 480 MB'
  - [1] 2026-11-09: a single upload is capped at 480 MB | capture: sha256:adfb0c7cd28c6ea437ffa0469f41c42ffdb54eb5671d9a230eeeb35f8e240404 | quote: The maximum size of a single file is 480 MB.
  - [1] 2026-11-25: a single uploaded audio file is capped at 480 MB | capture: sha256:adfb0c7cd28c6ea437ffa0469f41c42ffdb54eb5671d9a230eeeb35f8e240404 | quote: The maximum size of a single file is 480 MB.
  - [1] 2026-11-25: uploads are made through the Jamendo Artist web tab | capture: sha256:adfb0c7cd28c6ea437ffa0469f41c42ffdb54eb5671d9a230eeeb35f8e240404 | quote: Navigate to the **Upload/Manage my music **tab.
  - [1] 2026-11-25: the help page describes singles and albums | capture: sha256:adfb0c7cd28c6ea437ffa0469f41c42ffdb54eb5671d9a230eeeb35f8e240404 | quote: You can upload your tracks as singles or you can organize them into albums.
  - [2] 2026-11-25: signup requires an email address and password | capture: sha256:cc3f6f6a0ab36e0183d40571d4ccd007e2c839afd6069ee955798ef7c20f6d76 | quote: In the Create an account section, add your email address and password.
  - [1] 2026-11-25: the help page describes moderation outcomes but no retention period | capture: sha256:adfb0c7cd28c6ea437ffa0469f41c42ffdb54eb5671d9a230eeeb35f8e240404 | quote: This process can result in your track being accepted, flagged or removed from Jamendo for several reasons.
- sources:
  - [1] https://support-artist.jamendo.com/upload-manage-media
  - [2] https://support-artist.jamendo.com/account-management
