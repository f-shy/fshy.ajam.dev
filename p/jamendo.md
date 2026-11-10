# Jamendo

> jamendo.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jamendo/ | JSON https://fshy.ajam.dev/api/v1/entity/jamendo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jamendo (artist upload)

- `storage/jamendo` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.jamendo.com
- free tier: No published per-account total; 480 MB per file, lossless only (WAV/FLAC/AIFF, 16 or 24-bit, 44.1 or 48 kHz, 1-2 channels). | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 480 MB per file | bytes: 480000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free streaming and free download for listeners; Jamendo monetises through licensing, not storage fees. | metered: no
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 480 MB per file [1]
  - write-gated: review step [1]
  - write-gated: review step means an upload can be refused [1]
- limits note: 480 MB per file; strict format spec (bit depth, sample rate, channel count all constrained); a track must be submitted to a Jamendo programme, so there is a review step.
- interface detail: wrapper-only
- tooling: Jamendo Artist web dashboard; licensing API exists for consumers of the catalogue, not for uploads.
- composes with: Unlimited tracks per artist account x 480 MB. Same shape as Bandcamp but with a larger per-file cap and no sales gate.
- reliability: Lossless in, transcoded for streaming; Jamendo's model is sync licensing so the catalogue is public. No retention risk stated, but the review step means an upload can be refused.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'WAV, FLAC, or AIFF'; 'Bit depth: 16 or 24'; 'The maximum size of a single file is 480 MB'
- sources:
  - [1] https://support-artist.jamendo.com/upload-manage-media
