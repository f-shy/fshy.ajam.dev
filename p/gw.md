# gw.run

> gw.run | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gw/ | JSON https://fshy.ajam.dev/api/v1/entity/gw.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gw.run

- `egress/gw-run` | fails-egress | evidence unverified | binding none | category tunnel service (hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T10:32:52.502Z (live) | stale on 2026-11-18
- url https://gw.run/
- price USD 0
- free tier: Specifically focusing on securely exposing internal web apps to a group of people; not for publicly facing apps. Share access via email address then allow users to log in with common login providers like Google. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No allowance is published in the list entry.; ingress: http-only | metered: no | free allowance: none published | source: [2]
- identity: email | detail: an account on the hosted service, terms not read | country: None
- interface: cli
- binding note: No allowance is published, so the byte wall is unknown; the transport column is what the list states. Group access to internal web apps.
- interface detail: not established
- tooling: vendor client
- composes with: Needs an account before any capacity is visible.
- reliability: unverified: no page of https://gw.run/ was readable; an archived capture is an access-denied page citing an IP allow list.
- notes: https://gw.run/ returned an origin error and www.gw.run was refused (exit 4) twice on 2026-10-23; nothing about the service is established beyond the aggregator sentence. Group access to internal web apps. The URL was fetched and produced no product page; see confidence_note.
- evidence note: https://gw.run/ returned an origin error and www.gw.run was refused (exit 4) twice on 2026-10-23; nothing about the service is established beyond the aggregator sentence. A vendor page read would raise this to documented; only the aggregator was read for this name.
- extras:
  - wg_path: none
  - ingress: http-only
  - volume_stated: No allowance is published in the list entry.
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Specifically focusing on securely exposing internal web apps to a group of people; not for publicly facing apps. Share access via email address then allow users
  - [3] 2026-11-03: an archived capture of https://gw.run/ from 2024-03-22 is an access-denied page for a client address missing from the site's allow list | capture: sha256:2a40b6f0821dfaac20f644c9713791a98210f83c85c4458bc2bb68f5c8b716d7 | quote: is not on the access allow list for our site
  - probe:gw.run 2026-11-03: a direct probe completed a TLS 1.3 handshake whose certificate chain did not verify locally and read no HTTP status | capture: sha256:2a2dab24e3c624be3e1efa073187530604f0ff9ad61243d98a9deeac69c77bbe | quote: "error": "tls_untrusted"
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://gw.run/
  - [3] https://web.archive.org/web/20240322011850/https://gw.run/
