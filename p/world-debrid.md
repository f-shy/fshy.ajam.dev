# World-Debrid

> world-debrid.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/world-debrid/ | JSON https://fshy.ajam.dev/api/v1/entity/world-debrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## World-Debrid

- `debrid/world-debrid` | qualifies-with-caveat | evidence documented | binding pull-count | category multi-hoster (premium link generator, torrent conversion) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:39:03.000Z (live) | stale on 2026-11-23
- url https://world-debrid.com/en/plans
- price EUR 2.79/month (USD 3.13 at 0.8915 EUR/USD on 2026-10-23); EUR 2.49 per 15 days | parsed USD 3.12/mo
- free tier: Compte free à vie : 1 débridage offert chaque mois. Sans carte bancaire, sans essai limité. (Free account for life: 1 debrid offered each month. No card, no limited trial.) | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The same page states 'Trafic illimité, sans frontières' and 'Pas de quota journalier, pas de plafond mensuel' as a promise, which the 1-per-month free counter contradicts. The counter is the specific claim and wins.
- per-object cap: not applicable: a URL or magnet is unlocked, nothing is stored by the service | source: [2] | note: The free tier sentence '1 débridage offert' does not state a size limit, and none is published.
- retention: not applicable: no storage product. The status page tracks per-host unlock success rather than stored objects. | source: [3]
- egress: Download is served by the source host at its premium speed. Premium is sold as 'Unlimited unlocking' with 'Maximum speed guaranteed'; no byte allowance is published on any page read. | metered: no | free allowance: 1 debrid per month | source: [2]
- identity: email | detail: Free account by email, explicitly 'sans carte bancaire' (no bank card). Premium is Stripe (card) or a one-time purchase; the terms say prices are in euros with VAT not applicable under article 293 B of the French General Tax Code.
- interface: rest
- limits:
  - pull-count (binding): 1 debrid per month on the free plan; unlimited on Premium [1]
  - request-rate: free tier waits in queue; Premium adds 'simultaneous multi-link unlocking' [4]
  - volume-quota: none published; 'Unlimited unlocking*' carries an asterisk on the plans page with no footnote rendered [2]
  - request-rate: 1 unlock per month on the free account [1]
  - per-object-cap: free tier excludes 'fichiers volumineux'; the size is not stated [1]
- limits note: 70+ hosts claimed; the host page lists 1Fichier, Uploady, RapidGator, Turbobit, Mega, Ddownload, KatFile, Emload, MediaFire, Google Drive, Scribd, 4Shared, Filestore, NitroFlare, DailyUploads, Filespace, Mixdrop, FileFactory, DropGalaxy, Drop.download, UploadRar, Send.cm, Alfafile, HitFile, Prefiles, GigaPeta, FileDot, and marks Uptobox 'Hors service'.
- binding note: The free plan is one unlock a month, which is 0.14% of the pulls 1 TiB of monthly transfer needs, so pull count fails first by three orders of magnitude. On Premium no byte cap is published at all, so the first failure at 1 TiB is unpublished rather than documented.
- interface detail: Web console takes one link, a batch of links, a magnet or a .torrent file. No API is documented on the public pages.
- tooling: Browser only on the pages read; the generated direct link can be handed to any download manager.
- composes with: At EUR 2.79/month it is the cheapest monthly subscription among debrid providers, and its per-host success table is the only public health signal among the small providers; it is a link-unlocker, not a cache, so it does not replace a torrent-cache provider.
- reliability: Self-published per-host success rates run 93.1% (Mega) to 100% (Turbobit, Filespace, Mixdrop, Ddownload), which are vendor numbers and not independently sampled; Uptobox is marked out of service.
- notes: Two of its own sentences cannot both be true: 'Pas de quota journalier, pas de plafond mensuel' next to a 1-per-month free counter. The counter is the operative rule. DebridRank, a comparison site that ranks World-Debrid first with a tracked outbound link, describes it as 'the lowest entry price in this index' and 'a genuine free plan'; that site is a lead, not evidence, and its outbound links carry World-Debrid UTM parameters, so it may be vendor-operated. USD conversion at the 2026-10-23 exchangerate-api USD base. A French-market service that appeared without an archived footprint: the domain answered since 2011 but has no 2023-2025 capture at all, so this price cannot be compared with anything. The '1 unlock a month' free tier is the smallest permanent free allowance in the set and is explicitly a demo, not a working quota.
- evidence note: Prices, the free allowance and the host table are all from the vendor's own French and English pages. The success rates are a vendor claim at the reported rung. A single generated link would move the whole record to measured.
- extras:
  - hosts_claimed: 70+
  - hosts_listed_on_hebergeurs: 27 host pages plus Uptobox marked 'Hors service'
  - languages: 10 (per DebridRank; the site served fr and en pages directly)
  - free_plan: 1 debrid per month, no card
  - success_rates: vendor-published, 93.1%-100%
  - price_history[0].date: 2026-10-23
  - price_history[0].price: EUR 0 (1 unlock / month)
  - price_history[0].plan: Free
  - price_history[0].source_url: https://world-debrid.com/
  - price_history[1].date: 2026-10-23
  - price_history[1].price: EUR 2.79 / month (from)
  - price_history[1].plan: Premium
  - price_history[1].source_url: https://world-debrid.com/
  - price_history_status: unread
  - price_history_note: No capture of the current site exists; the domain's only captures are from 2011, before it was this service.
  - change_36m: unknown
  - currency: EUR
  - usenet: no
- evidence:
  - [2] 2026-10-23: Premium Monthly EUR 2.79/month auto-renewed ('-20% vs the 30-day one-time purchase'), Premium 15 Days EUR 2.49, Premium 30 Days EUR 3.49, Premium 90 Days EUR 9.99 (≈EUR 3.33/month), each 'Unlimited unlocking*'
  - [1] 2026-10-23: 'Compte free à vie : 1 débridage offert chaque mois. Sans carte bancaire' and '70+ hébergeurs' with the host list
  - [3] 2026-10-23: per-host success rates: RapidGator 99.7%, 1Fichier 99.7%, Turbobit 100.0%, Mega 93.1%, Send.cm 95.2%, DailyUploads 99.4%
  - [5] 2026-10-23: the full host list including Google Drive, Scribd and 4Shared, and the 'Uptobox Hors service' marker
  - [1] 2026-10-23: 'Compte free a vie : 1 debridage offert chaque mois', 'les plans Premium demarrent a 2,79 EUR/mois', and 'Plus de 70 hebergeurs'
  - [6] 2026-10-23: the domain's captures start in 2011 and there are none between 2023 and 2025, so the current site has no archived price
- sources:
  - [1] https://world-debrid.com/
  - [2] https://world-debrid.com/en/plans
  - [3] https://world-debrid.com/statut
  - [4] https://world-debrid.com/en/faq
  - [5] https://world-debrid.com/hebergeurs
  - [6] https://web.archive.org/cdx/search/cdx?url=world-debrid.com&output=json&fl=timestamp&limit=3
