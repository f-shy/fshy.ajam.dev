# iheartradio podcast hosting

> iheart.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iheart/ | JSON https://fshy.ajam.dev/api/v1/entity/iheart.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iheartradio podcast hosting

- `storage/iheartradio-podcast-hosting` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:01.974Z (live) | stale on 2026-12-04
- url https://www.iheart.com/content/iheartradio-destination-content-license-agreement/
- free tier: none reachable: no free self-serve hosting product exists. iHeartRadio is a podcast distribution/directory: podcasters submit an RSS feed hosted elsewhere, and the podcaster portal states it is currently unavailable. First-party help lists only partner hosting platforms (Omny Studio, Spreaker, Libsyn, Audioboom, PodBean, Pinecast, Podomatic). | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: No free self-serve hosting product to verify. iheart.com/podcast-hosting/ returns HTTP 406 through the reader and the only hosting-shaped documents surfaced are content licence agreements…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free self-serve hosting product to verify. iheart.com/podcast-hosting/ returns HTTP 406 through the reader and the only hosting-shaped documents surfaced are content licence agreements…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free self-serve hosting product to verify. iheart.com/podcast-hosting/ returns HTTP 406 through the reader and the only hosting-shaped documents surfaced are content licence agreements…
  - probe:https://www.iheart.com/content/iheartradio-destination-content-license-agreement/ 2026-11-19: the only hosting-shaped first-party document is a content licence agreement, not a self-serve hosting product | capture: sha256:999e5bbfae458077030def3e8e73ebc73a668fbc07b77fa895747f351817ec07 | quote: This Content License Agreement (this “Agreement”) governs your provision of podcast content to iHeartRadio
  - [2] 2026-11-19: the direct submission portal is currently unavailable | capture: sha256:c3f2d0207eded6436ebec943877f5b1a35785ac9c505264f4921d9093f7b0463 | quote: # The iHeartRadio Podcasters Portal is currently unavailable. Please check back later.
  - [3] 2026-11-19: iHeartRadio is an RSS submission/directory service, not a self-serve byte host | capture: sha256:429d80bd774c53525b388e273cc347c011d938c8a9dffe6b86dea35181c5ef6a | quote: Podcasters can submit their show to iHeartRadio directly or through a participating podcast hosting platform.
- sources:
  - [1] https://www.iheart.com/content/iheartradio-destination-content-license-agreement/
  - [2] https://podcasters.iheart.com/add-podcast
  - [3] https://help.iheart.com/hc/en-us/articles/228920687-Submitting-a-podcast-to-iHeartRadio
