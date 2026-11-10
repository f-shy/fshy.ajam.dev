# FileMirage

> filemirage.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filemirage/ | JSON https://fshy.ajam.dev/api/v1/entity/filemirage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileMirage

- `debrid/filemirage` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (free, ad-supported, API) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://filemirage.com/
- price unverified: no plan price was readable
- free tier: 100% free with ads; unlimited storage as long as each file does not exceed 50GB; files remain available for 30 days of inactivity. | unit: unlimited | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The FAQ states no upload or download speed limits.
- per-object cap: Each file can be up to 50GB in size. | bytes: 53687091200 | source: [1] | note: bytes = 50 x 1024^3.
- retention: Files remain available for 30 days of inactivity. If a file is accessed within that period, the timer resets. | days: 30 | source: [1] | note: Expired or deleted files cannot be recovered.
- egress: No speed limits on uploads or downloads; no byte cap printed. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The homepage says 'Share large files effortlessly—up to 50GB per file, no sign-up needed.'.
- interface: rest
- limits:
  - per-object-cap: 50 GB per file [1]
  - retention-clamped (binding): 30 days of inactivity; access resets the timer [1]
- binding note: No byte cap is printed, so the 30-day inactivity window is the first thing a stored file meets.
- interface detail: The FAQ says developers can use an API to integrate upload and management; the API documentation page was not read.
- tooling: API stated on the FAQ; the API page was not read.
- composes with: 50 GB per file with no sign-up and a 30-day inactivity timer that resets on access.
- reliability: The pricing page states paid plans accept crypto payments only; no plan price was readable.
- evidence note: Homepage FAQ and pricing FAQ read on 2026-11-03. Paid plan prices unverified: the pricing page showed only a FAQ.
- evidence:
  - [1] 2026-11-03: per-file cap 50 GB | capture: sha256:1af651dd6a56747448226ec4ad980203a760ce526196d7a18825235621e9071b | quote: Each file can be up to 50GB in size.
  - [1] 2026-11-03: 30-day inactivity retention | capture: sha256:1af651dd6a56747448226ec4ad980203a760ce526196d7a18825235621e9071b | quote: Files remain available for 30 days of inactivity. If a file is accessed within that period, the timer resets.
  - [1] 2026-11-03: no sign-up is needed | capture: sha256:1af651dd6a56747448226ec4ad980203a760ce526196d7a18825235621e9071b | quote: Share large files effortlessly—up to 50GB per file, no sign-up needed.
  - [2] 2026-11-03: paid plans are payable in crypto only | capture: sha256:0646abf06efe3184699c0e399e2c4b2a49e6dc3ee35aacf853b109f48369e24a | quote: We accept crypto payments only, more options coming soon.
- sources:
  - [1] https://filemirage.com/
  - [2] https://filemirage.com/pricing
