# beehiiv

> beehiiv.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beehiiv/ | JSON https://fshy.ajam.dev/api/v1/entity/beehiiv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## beehiiv (free plan) — 500 MB per podcast episode, newsletter attachment host

- `storage/beehiiv-500-mb-per-podcast-episode-newsletter-attachment` | fails-quota | evidence documented | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:38.757Z (live) | stale on 2026-12-04
- url https://www.beehiiv.com
- free tier: Free plan is "Free forever" with unlimited email sends (pricing page). Per-file: "The maximum file size for a single podcast episode upload is 500 MB." File blocks in posts allow attachments; images must be under 5 MB. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: maximum file size for a single podcast episode upload is 500 MB | bytes: 500000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: CDN-served post media; no egress billing on the free plan. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): maximum file size for a single podcast episode upload is 500 MB [1]
- limits note: per-object-cap 500 MB podcast audio, 5 MB images, 1 MB fonts. Email body itself is capped at Gmail's 102 KB clipping threshold, so the attachment is the only real payload path. No published aggregate byte quota on free.
- interface detail: rest
- tooling: REST API exists (beehiiv API + Zapier integration, v3 app). No rclone backend. Podcast file upload limit is 500 MB per episode.
- composes with: Episodes are per-show; multiple shows × multiple publications per account. But 500 MB × episodes is a podcasting quota, not a blob store, and the free plan's real limit is subscriber count (2,500), not bytes.
- reliability: Media re-encoding risk must be assumed for audio/video paths; original-byte retrieval is not documented. Treat as CDN surface, not storage.
- notes: the same as the free tier
- evidence note: Re-read on 2026-11-03 from vendor pages: https://www.beehiiv.com/support/article/41323776364823 (500 MB maximum for a single podcast episode upload) and https://www.beehiiv.com/pricing (Free includes up to 2,500 subscribers; every plan includes unlimited email sends). The per-object cap that binds the verdict cites a vendor capture; the image, font and email-clipping limits stay unverified.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free plan is "Free forever" with unlimited email sends (pricing page). Per-file: "The maximum file size for a single podcast episode upload is 500 MB." File blocks in posts allow attachments; images must be under 5 MB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: "maximum file size for a single podcast episode upload is 500 MB"
  - [2] 2026-10-21: Free forever, up to 2,500 subscribers, unlimited sends
  - [3] 2026-10-21: Gmail 102 KB clipping limit governs email payload
  - [1] 2026-11-03: the per-episode upload cap is 500 MB | capture: sha256:c7285ee138c1d367f02698b04be3cbb22245e0d89768b94992aa6278ca98e8df | quote: The maximum file size for a single podcast episode upload is 500 MB.
  - [2] 2026-11-03: plans are tiered on subscriber count, not stored bytes | capture: sha256:90cf63a8ddde4516a4a048253649d3dbd7e77b9f79dbbf55b8a46d28d1e28e2b | quote: Free includes up to 2,500 subscribers, Lite up to 100,000, Pro up to 250,000, and Enterprise is custom.
  - [2] 2026-11-03: sends are unmetered on every plan | capture: sha256:90cf63a8ddde4516a4a048253649d3dbd7e77b9f79dbbf55b8a46d28d1e28e2b | quote: No. Every plan includes unlimited email sends.
- sources:
  - [1] https://www.beehiiv.com/support/article/41323776364823
  - [2] https://www.beehiiv.com/pricing
  - [3] https://www.beehiiv.com/support/article/4413255394583
