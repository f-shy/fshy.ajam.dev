# klokintegration.se

> klokintegration.se | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/klokintegration/ | JSON https://fshy.ajam.dev/api/v1/entity/klokintegration.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## klokintegration.se

- `inference/klokintegration` | trial-only | evidence documented | binding volume-quota | category inference subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://klokintegration.se
- free tier: A free 30-day trial is offered, using email and a Google document as the source. After the trial the service is a fixed monthly fee with fair use. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a trial uses email and a Google document as the source; a token is needed for the document API
- interface: rest
- limits:
  - volume-quota (binding): 30-day free trial, then a fixed monthly fee with fair use [1]
- endpoint: https://api-gw.klok.ipaas.se/proxy/kloker-key/v1
- tooling: a hosted AI-worker service with a document API, reachable through an API token; the page describes an email or Slack interface
- composes with: the 30-day free trial and the email/Google-document source requirement bind before the fixed monthly fee
- reliability: uploaded files are kept seven days and extracted text is kept by the file hash for 90 days by default
- notes: the only free offer found is a 30-day trial probation for a hosted knowledge worker, not a standing free inference API tier
- evidence:
  - [1] 2026-11-18: a free 30-day trial probation is offered with email and a Google document as the source, followed by a fixed monthly fee | capture: sha256:47be15c61a905d822e1c99716c5a92b6732464a44697d63f105c3b9ab0f26d43 | quote: Gratis provanställning i 30 dagar med mejl och ett Google-dokument som källa
- sources:
  - [1] https://klokintegration.se
