# CoreHost

> corehost.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/corehost/ | JSON https://fshy.ajam.dev/api/v1/entity/corehost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoreHost

- `debrid/corehost` | fails-quota | evidence documented | binding none | category managed open-source app hosting, per-app, hourly billing from a prepaid balance | tier Lite / Standard / Power / Scale
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://corehost.io/pricing
- free tier: A USD 5 starting credit: the pricing page meta description states 'Start free with $5 credit'. Product documentation notes 'Your $5 starting credit covers the first stretch; we only ask for a card when it runs low.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: apps and their disks, not objects | source: [1]
- retention: data persists while the app is paid for; 'Daily backups with one-click restore' is included on every tier | source: [1]
- egress: 'No bandwidth charges for normal use' - an unmetered claim with no published figure and no definition of 'normal'. | metered: no | free allowance: not published | source: [1]
- identity: email | detail: Account with the USD 5 credit; a card is added only 'when it runs low', so a trial can start without payment details. | country: None
- interface: rest, sftp
- limits:
  - volume-quota: disk per tier: 5 GB NVMe (Lite), 10 GB (Standard), 20 GB (Power), 40 GB (Scale), +25 GB per USD 1.20 block [1]
- limits note: The categorical limit is the catalogue: of 49 apps, none is Sonarr, Radarr, Prowlarr, Jackett, Plex, Jellyfin, Emby or a torrent client, so the price never applies to the pipeline debrid is pricing.
- binding note: Nothing binds at 1 TiB/month because no app in the catalogue streams media; the limit is fit, not quota.
- interface detail: A control panel per app; 'SFTP access to your data', 'Automatic HTTPS + custom domains', 'Resize up or down, prorated'. Prices drawn hourly from a prepaid balance.
- tooling: the catalogue is managed images: 'A deliberately short list. Every app here runs well on our platform' - 49 apps at the read date, and the media stack is not among them.
- composes with: The cheapest managed host found per app, useful for the non-media half of a stack (Homarr, Vaultwarden, Uptime Kuma, RSS) at USD 1.50-6.30; it cannot carry Plex, Jellyfin or the *arr apps.
- reliability: New and small: an Australian vendor with three regions (Australia, United States, Poland), hourly billing and no track record found. Poland is 25 percent cheaper, which suggests capacity is being bought where it is cheap.
- notes: Documented as the honest floor of managed app hosting: USD 1.50 per app is a third of ElfHosted's USD 9, and the reason is that the catalogue excludes everything that needs real disk, bandwidth or torrent egress. It is the evidence that the media apps, not the hosting, are the expensive part.
- evidence note: The pricing and catalogue pages were read on 2026-10-23 and the tier prices are quoted from them. The per-app pages are client-rendered and returned no readable content (a Prowlarr page came back as 2 words), so the card-deferral sentence comes from a search index's rendering. A signup confirms whether the USD 5 credit really starts without a card.
- extras:
  - catalogue_size: 49
  - regions: Australia, United States, Poland
- evidence:
  - [1] 2026-10-23: Lite $1.50 / Standard $2.30 / Power $3.90 / Scale $6.30 per month; Poland at $1.10/$1.70/$2.90/$4.70; 'Start free with $5 credit'; 'No bandwidth charges for normal use'; daily backups, SFTP, custom domains, hourly draw
  - [2] 2026-10-23: the full catalogue is 49 apps - Activepieces, Audiobookshelf, Homarr, Immich, Navidrome, Vaultwarden, WordPress and similar - with no Sonarr, Radarr, Prowlarr, Jackett, Plex, Jellyfin or Emby
- sources:
  - [1] https://corehost.io/pricing
  - [2] https://corehost.io/apps
