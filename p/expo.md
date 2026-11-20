# Expo

> expo.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/expo/ | JSON https://fshy.ajam.dev/api/v1/entity/expo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Expo

- `compute/expo` | qualifies-with-caveat | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:41.666Z (live) | stale on 2026-12-05
- url https://expo.dev
- free tier: Expo and the SDK are free and open source under MIT; EAS has a free tier metered on build minutes, OTA updates and hosting bandwidth | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: EAS Update global edge bandwidth: 100 GiB on Free and Starter, then $0.10 per GiB on Starter; the Hosting table lists no bandwidth row | metered: yes | free allowance: 100 GiB of EAS Update global edge bandwidth on the Free plan | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): EAS bills build minutes, OTA updates and hosting bandwidth; the free tier's minute count is not published on this page [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the page was read on 2026-10-22 and states the licence position and that EAS has a free tier with the three meters named. It does not publish the free tier's minute count, so no figure is given
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a build is a job with its own timeout; the free tier's minute pool is unstated here
  - free_tier_kind: allowance
  - granularity.min_billed_s: 60
  - burst_x: 2.4032
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Expo and the Expo SDK are free and open source (MIT license). EAS has a free tier and usage-based paid plans for build minutes, OTA updates, hosting bandwidth, and priority support.'…
  - [2] 2026-11-03: EAS Update global edge bandwidth is 100 GiB on Free, then $0.10 per GiB on Starter | capture: sha256:57ba013c713b80abef59829dadf62a18b998a0030a57629b779086ade502174e | quote: | Global edge bandwidth | 100 GiB | 100 GiB, then $0.10 per GiB
- sources:
  - [1] https://expo.dev
  - [2] https://expo.dev/pricing
