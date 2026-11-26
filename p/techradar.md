# samsung cloud

> techradar.com | Storage, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/techradar/ | JSON https://fshy.ajam.dev/api/v1/entity/techradar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## samsung cloud, amazon drive, ionos free tiers

- `storage/samsung-cloud-amazon-drive-ionos-free-tiers` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:35.014Z (live) | stale on 2026-12-04
- url https://www.techradar.com/pro/grab-1-54tb-free-cloud-storage-for-life-but-you-will-need-to-sign-up-43-services
- free tier: none reachable: All three providers retired free cloud storage tiers. Amazon Drive was discontinued. Samsung Cloud transitioned consumer storage to Microsoft OneDrive. IONOS discontinued its free tier. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: All three abandoned free cloud storage within the last five years. Amazon Drive was retired outright; IONOS dropped its free tier. Listed here so…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: All three abandoned free cloud storage within the last five years. Amazon Drive was retired outright; IONOS dropped its free tier. Listed here so nobo
  - [1] 2026-11-19: TechRadar still lists Samsung, Amazon and Ionos among providers that gave up free cloud storage in the past five years | capture: sha256:6a6ffa6ebfb65f1c1a77c350f3bf81253511c91f502c62427ad49e1a81dfc5a0 | quote: Over the past five years, dozens of cloud storage companies have either given up on free cloud storage (e.g Samsung, Amazon and Ionos) or closed shop altogether (e.g. Flipdrive, Ganso).
- sources:
  - [1] https://www.techradar.com/pro/grab-1-54tb-free-cloud-storage-for-life-but-you-will-need-to-sign-up-43-services

## WeVPN

- `egress/wevpn` | dead | evidence reported | binding write-gated | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:55:01.927Z (live) | stale on 2026-12-10
- url https://www.techradar.com/news/wevpn-has-shut-down-users-now-moved-onto-windscribe
- price not applicable
- free tier: The service is closed: WeVPN is shutting down, the company confirmed in a short statement published on its website, and users with active subscriptions can migrate to Windscribe. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Not applicable: the provider stopped serving in April 2023.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: Not applicable; existing subscriptions were migrated to Windscribe at no charge for the remaining term. | country: None
- interface: unknown
- limits:
  - write-gated (binding): the service is closed, so every constraint is moot [1]
- binding note: A dead provider has no binding constraint; the record exists so the name is not researched again.
- interface detail: Service closed.
- tooling: none
- composes with: the same as tooling
- reliability: Service closed April 2023.
- notes: WeVPN discontinued operations in 2023. Customer accounts were transitioned to Windscribe.
- evidence note: Third-party report dated 2023-04-14. The vendor's own shutdown notice could not be read: wevpn.com had no DNS answer on 2026-11-25.
- extras:
  - wg_path: none
  - wg_detail: The service no longer operates, so no config can be obtained. The successor Windscribe includes port forwarding only on its paid plans.
  - ingress: none
  - volume_stated: Not applicable: the provider stopped serving in April 2023.
  - bytes_transit: no
  - transit_note: No service operates.
- evidence:
  - [1] 2026-10-23: Published 2023-04-14: WeVPN shut down citing unforeseen financial difficulties and migrated active subscriptions to Windscribe; Windscribe did not acquire the company.
  - [2] 2026-10-23: Nothing: the attempt returned HTTP 530, which establishes nothing about the target.
  - [1] 2026-11-25: a report published 2023-04-14 says WeVPN shut down and moved active subscribers to another provider | capture: sha256:bd8f9a77318ed14e780a192fcffc2a60f69a2682545e7dfdf4b3582b7f6bf7ef | quote: Published 14 April 2023 ... Virtual Private Network (VPN) service provider WeVPN is shutting down, the company confirmed in a short statement published on its website. Users who still have active subscriptions will be able to use a different provider for the time that remains, free of charge.
  - [3] 2026-11-25: the successor's port forwarding is paid-only | capture: sha256:532f49f2566aec08aa4c50f4c2fda88f54d1d2374e2f8aa12036d53cc062b65a | quote: Port forwarding is only included on Windscribe's paid plans. However, the free plan does have a generous data allowance and access to all Windscribe servers.
  - [1] 2026-11-25: the shutdown report still describes a closed service | capture: sha256:bd8f9a77318ed14e780a192fcffc2a60f69a2682545e7dfdf4b3582b7f6bf7ef | quote: Virtual Private Network (VPN) service provider WeVPN is shutting down, the company confirmed in a short statement published on its website. Users who still have active subscriptions will be able to use a different provider for the time that remains, free of charge.
  - probe:https://wevpn.com/ 2026-11-25: the first-party name had no answer on 2026-11-25 | capture: sha256:eeac690edf868324ae164d46ee16774ffb63215538050ab37d104a6db8b566b6 | quote: "error": "transport"
- sources:
  - [1] https://www.techradar.com/news/wevpn-has-shut-down-users-now-moved-onto-windscribe
  - [2] https://wevpn.com/
  - [3] https://windscribe.com/features/port-forwarding/
