# samsung cloud

> techradar.com | Storage, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/techradar/ | JSON https://fshy.ajam.dev/api/v1/entity/techradar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## samsung cloud, amazon drive, ionos free tiers

- `storage/samsung-cloud-amazon-drive-ionos-free-tiers` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://www.techradar.com/pro/grab-1-54tb-free-cloud-storage-for-life-but-you-will-need-to-sign-up-43-services

## WeVPN

- `egress/wevpn` | dead | evidence reported | binding write-gated | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
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
- evidence note: Third-party report dated 2023-04-14. wevpn.com itself returned HTTP 530 on the single attempt made, so the vendor's own shutdown notice was not read. The confirmation would be an archive capture of wevpn.com from mid-2023.
- extras:
  - wg_path: none
  - wg_detail: The service no longer operates, so no config can be obtained. Successor for existing users is Windscribe, which forwards ports only on its paid Pro plan.
  - ingress: none
  - volume_stated: Not applicable: the provider stopped serving in April 2023.
  - bytes_transit: no
  - transit_note: No service operates.
- evidence:
  - [1] 2026-10-23: Published 2023-04-14: WeVPN shut down citing unforeseen financial difficulties and migrated active subscriptions to Windscribe; Windscribe did not acquire the company.
  - [2] 2026-10-23: Nothing: the attempt returned HTTP 530, which establishes nothing about the target.
- sources:
  - [1] https://www.techradar.com/news/wevpn-has-shut-down-users-now-moved-onto-windscribe
  - [2] https://wevpn.com/
