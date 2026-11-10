# Substack file embeds

> substack.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/substack-com/ | JSON https://fshy.ajam.dev/api/v1/entity/substack-com.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Substack file embeds

- `storage/substack-file-embeds` | qualifies-with-caveat | evidence reported | binding none | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://substack.com
- free tier: no stated total; 700 MB per PDF, XLSX/CBZ/CBR embeds supported | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, CDN-served download links on substackcdn.com, no auth for public posts | metered: no
- identity: institution
- interface: unknown
- limits note: 700 MB/PDF; only PDF, XLSX, CBZ, CBR accepted as embeddable files; paywall/email delivery adds processing; publication needs a verified email and payment setup for paid tiers
- interface detail: wrapper-only
- tooling: No public upload API. File embeds are drag-and-drop in the post editor or into email drafts; would need browser automation (Playwright) against the logged-in editor.
- composes with: 700 MB x unlimited posts x unlimited publications (each free to create). This is the largest per-file limit of any social platform checked here; 20 TiB = ~29,000 PDFs
- reliability: Attachments live with the post; editing a post can drop the embed; Substack has no delete-then-restore story. No API is the hard blocker. This is a 'if someone writes the Playwright wrapper' candidate.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'The file size limit for a PDF is 700 MB'
  - [2] 2026-10-21: 'Writers can now embed PDFs, Excel spreadsheets (XLSX), and comics files (CBZ, CBR) into their posts'
- sources:
  - [1] https://support.substack.com/hc/en-us/articles/4408381643156-How-can-I-attach-a-file-to-my-Substack-post
  - [2] https://on.substack.com/p/new-tools-paywall-embeds
