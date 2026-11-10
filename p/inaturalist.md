# iNaturalist

> inaturalist.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inaturalist/ | JSON https://fshy.ajam.dev/api/v1/entity/inaturalist.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iNaturalist

- `storage/inaturalist` | fails-quota | evidence reported | binding per-object-cap | category citizen-science observation platform
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.inaturalist.org
- free tier: No per-account quota published or enforced (395,436,915 observations live at time of probe). But per-object: 20 MB/file upload cap, AND every image is re-encoded to a 2048 px longest edge. So the stored 'original' is not your original. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 20 MB/file | bytes: 20000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, no auth, static.inaturalist.org serves 5 sizes; API 100 req/min (asked to stay at 60) | metered: no
- identity: email | detail: Email. Verified the live signup form at /users/new: user[login], user[email], user[password] only, plus a reCAPTCHA widget. No affiliation field exists.
- interface: rest
- limits:
  - per-object-cap (binding): 20 MB/file [1]
- limits note: 20 MB/file; downsample to 2048×2048 max on the longest edge; API 100 req/min
- interface detail: REST v1 + v2. POST /v1/observation_photos and POST /v1/photos accept multipart `file`; pyinaturalist wraps it.
- tooling: pyinaturalist (`add_photo_to_observation`, `upload`), REST directly
- composes with: Good write API, bad read fidelity. Every returned photo is ≤2048 px; the size ladder is square/large/medium/small/original and 'original' is a misnomer.
- reliability: Measured on a live asset: /photos/753863865/original.jpg = 3,881,965 bytes at dimensions reported as 1536×2048, i.e. already clamped. Mods state plainly: 'That term [original] is probably misleading ... everything larger is reduced to 2048.'
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No per-account quota published or enforced (395,436,915 observations live at time of probe). But per-object: 20 MB/file upload cap, AND every image is re-encoded to a 2048 px longest edge — so the stored 'original' is not your original.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: total_results 395436915; photo objects carry original_dimensions {width,height} capped at 2048
  - [3] 2026-10-21: large,medium,small,square}.jpg — 200 in all five, 3,881,965 / 1,164,886 / 340,333 / 92,808 / 14,515 bytes
  - [4] 2026-10-21: 'The term original is probably misleading ... everything larger is reduced to 2048'
  - [5] 2026-10-21: form fields user[login], user[email], user[password] + reCAPTCHA
  - [6] 2026-10-21: staff: the forum has 'a storage limit to our subscription', i.e. this is not a general-purpose host
- sources:
  - [1] https://forum.inaturalist.org/t/size-recommendations-or-requirements-for-uploaded-photos/72657
  - [2] https://api.inaturalist.org/v1/observations?per_page=1&photos=true
  - [3] https://static.inaturalist.org/photos/753863865/{original
  - [4] https://forum.inaturalist.org/t/original-image-not-showing-in-full-resolution/80010
  - [5] https://www.inaturalist.org/users/new
  - [6] https://forum.inaturalist.org/t/image-for-linking-to-in-an-observation/15426
