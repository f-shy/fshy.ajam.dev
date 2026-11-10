# EZ-Homelab

> ez-homelab.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ez-homelab/ | JSON https://fshy.ajam.dev/api/v1/entity/ez-homelab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EZ-Homelab

- `debrid/ez-homelab` | paid-only | evidence documented | binding none | category managed media stack on rented AWS EC2 (Plex, Jellyfin, Sonarr, Radarr and more) | tier Entertainment package
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://ez-homelab.com/hosting/plex
- free tier: No free tier: 'From $29/mo' for 'Plex + Jellyfin + Sonarr + Radarr + 6 more on your own EC2'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: EBS-backed server storage, sized per selected apps ('Custom Storage - Adjust per-app storage') | source: [2]
- retention: 'EBS backups included ... on-demand' | source: [1]
- egress: No allowance published on the media pages. Because the server is EC2, AWS's own egress pricing is the underlying cost, and the vendor says the price is 'based on actual AWS infrastructure costs plus a small platform fee'. | metered: no | free allowance: not published | source: [2]
- identity: card | detail: Paid subscription. If the EC2 instance runs in the same AWS account, an AWS account with a card is also required - that point is unresolved (see notes). | country: None
- interface: rest
- limits:
  - volume-quota: server size and EBS volume are chosen from the app selection; no fixed allowance is published [2]
- limits note: The published comparison on the vendor's own page puts a Plex-only container at '~$11/mo (Plex only)' on Elestio and 'DIY / VPS $5-10/mo + Plex Pass', which is a rare case of a vendor printing the cheaper alternatives beside its own price.
- binding note: No byte counter is published, and the package is priced by picking a bigger EC2 instance, so the first wall is spend rather than a named quota - the vocabulary has no kind for that.
- interface detail: The apps keep their own interfaces (Plex/Jellyfin web and apps, *arr web UIs) on a dedicated EC2 instance; the vendor supplies provisioning, monitoring, backups and TLS.
- tooling: managed deployment of the same open-source apps that would otherwise be run; nothing to install locally. Whether the EC2 instance is in the vendor's AWS account or a separate one is not stated in readable text, which changes whether USD 29 is the whole bill.
- composes with: A hosted *arr + media server without a seedbox's disk: the library is EBS-backed, so it scales by paying AWS rather than by picking a bigger seedbox tier.
- reliability: Single-vendor management layer over AWS: the infrastructure has an SLA, the orchestrator does not. A 2026-founded service with no track record found.
- notes: The 'your own EC2' wording matters: if the instance is billed to the same AWS account, the true monthly total is USD 29 plus EC2 plus EBS plus egress, and it stops being comparable to a USD 24 ElfHosted stack that sells no storage. A test purchase confirms the threshold; on 2026-10-23 did not make one.
- evidence note: Two vendor pages read on 2026-10-23. The unresolved question - whether USD 29 includes the EC2 bill or sits on top of it - is what keeps this at documented rather than measured, and it is a factor-of-two error on the cheapest comparison among debrid providers.
- extras:
  - vendor_comparison: Elestio ~$11/mo Plex-only; DIY VPS $5-10/mo + Plex Pass
  - packages: Entertainment, Cloud, DevOps, Smart Home
- evidence:
  - [1] 2026-10-23: 'From $29/mo', 'Includes Plex + Jellyfin + Sonarr + Radarr + 6 more on your own EC2', 'Dedicated server - Yes, your EC2', GPU transcoding, EBS backups, and the price table naming Elestio at '~$11/mo (Plex only)'
  - [2] 2026-10-23: the Entertainment package contains 'Media Streaming Plex, Jellyfin, or similar' plus 'Media Management Sonarr, Radarr, Prowlarr', and the pricing model: 'based on actual AWS infrastructure costs plus a small platform fee'
- sources:
  - [1] https://ez-homelab.com/hosting/plex
  - [2] https://ez-homelab.com/pricing
