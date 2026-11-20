# Seedbox.fr

> seedbox.fr | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedbox-2/ | JSON https://fshy.ajam.dev/api/v1/entity/seedbox-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seedbox.fr

- `debrid/seedbox-fr` | paid-only | evidence documented | binding none | category shared seedbox with media stack (French market) | tier 1 To
- needs card yes, phone yes, ID no, institution no | verified 2026-10-23T03:19:00.000Z (live) | stale on 2026-11-23
- url https://www.seedbox.fr/tarifs/
- price EUR 12.00 HT per 1 To per month (EUR 12/TB/month; EUR 14.40 TTC at 20% VAT) | parsed USD 13.43/TB-mo
- free tier: No free tier and no free trial is published. The no-risk path is the refund window: 'Satisfait ou remboursé 14 jours' with 'Sans engagement'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the page read lists 1 To at EUR 12.00 HT/month; no trial length, no free bytes, no restock statement
- per-object cap: not applicable: sold by total storage, from 500 Go to 15 To; no largest-single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: 'Debit illimite: Aucune restriction de bande passante' and 'Slots illimites' on a shared 100 Gbps network. No monthly byte figure and no throttle threshold are published anywhere on the page read. | metered: no | free allowance: unlimited claimed; no byte figure published | source: [1]
- identity: email | detail: An account and a payment method are required; no free tier exists. The page advertises French-language support and 20 years of operation, but states no identity document or phone check. | country: None
- interface: ftp, webdav
- limits:
  - per-ip-shaping: 100 Gbps shared across the server; no per-account rate is published [1]
- limits note: The page claims unlimited throughput with no restriction, which cannot be verified without an account. 1 TiB/month needs only 3.39 Mbit/s sustained, far below any plausible share of a 100 Gbps port, so the claim does not bind at this scale.
- binding note: Nothing in the vocabulary fails at 1 TiB/month: there is no byte quota, no object cap and no published rate limit. The binding fact is price (EUR 12 HT for 1 To, EUR 14.40 TTC at 20% VAT), which the vocabulary does not name.
- interface detail: 'Acces WebDAV, FTP et navigateur web integre' for the storage side; the media stack is browser-driven.
- tooling: WebDAV mount, FTP client, built-in file browser; one-click Prowlarr/Radarr/Sonarr/Jellyseerr/Jellyfin stack; no rclone or CLI is documented
- composes with: A French-market box that pairs a 1 TB WebDAV mount with a preconfigured arr stack; the EUR 12 HT entry is above the USD 5 line, so it prices the paid tier rather than answering the free question
- reliability: Unlimited bandwidth is a vendor claim with no published fair-use threshold; a client pulling 1 TiB/month has no stated protection if that claim changes.
- notes: The price is quoted hors taxe; a French or EU consumer pays VAT on top, so the comparable figure is 14.40 EUR TTC. Sustained-rate conversion: 1 TB/month = 10^12/(30x86,400) = 385,802 B/s = 3.09 Mbit/s. The 'unlimited' claim could mean genuine unmetered transit at 100 Gbps, a soft fair-use rule applied silently, or a per-user port share; the page publishes no threshold, so the claim stays unverified.
- evidence note: Price, storage range, protocols and refund window are on the live tariff page read. The unlimited-traffic claim would need a paid account and a transfer run to reach measured.
- extras:
  - sustained_mbps_from_allowance: unlimited claimed; 1 TiB/month would need 3.39 Mbit/s
  - port_gbps: 100
  - setup_fee: none stated
  - minimum_term: monthly, no commitment ('Sans engagement'); 14-day refund
  - apps: Plex, Jellyfin, Prowlarr, Radarr, Sonarr, Jellyseerr, Nextcloud, Seafile, Immich, PyLoad, Resilio, Kavita, OpenVPN
  - trial_card_required: no trial exists
  - trial_restock: not applicable
  - vat_note: 12.00 EUR HT -> 14.40 EUR TTC at the French 20% rate
- evidence:
  - [1] 2026-10-23: 1 To at EUR 12.00 HT/month (0.0120 EUR HT/Go), 'Debit illimite / Aucune restriction de bande passante', 'Slots illimites', 100 Gbps shared, 14-day refund, 500 Go to 15 To range
  - [2] 2026-10-23: 'Acces WebDAV, FTP et navigateur web integre'; one-click Prowlarr/Radarr/Sonarr/Jellyseerr/Jellyfin stack; Plex and Jellyfin streaming
- sources:
  - [1] https://www.seedbox.fr/tarifs/
  - [2] https://www.seedbox.fr/
