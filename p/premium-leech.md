# Premium-Leech.com

> premium-leech.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premium-leech/ | JSON https://fshy.ajam.dev/api/v1/entity/premium-leech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Premium-Leech.com

- `debrid/premium-leech` | qualifies-with-caveat | evidence inferred | binding none | category multi-hoster (free premium link generator, long-running template) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:32.906Z (live) | stale on 2026-12-04
- url https://www.premium-leech.com/
- price USD 0 (claimed)
- free tier: Premium-Leech is a free premium link generator: the leeched files are stored on our secure server and sent to you at maximum speed without any hourly limits or ads. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No quota, no counter, no pricing and no status page. 'Unlimited' is the vendor's adjective.
- per-object cap: none published | source: [1]
- retention: The leeched files are stored on our secure server - no retention period is published for that storage | source: [1]
- egress: Sent to you at maximum speed without any hourly limits or ads. No allowance is published and no throughput was measured. | metered: no | free allowance: unlimited (claimed) | source: [1]
- identity: anonymous | detail: No signup: 'No signup required' in the page's own sentence.
- interface: unknown
- limits:
  - per-ip-shaping: generated links are single-user; no numeric concurrency or volume limit published [1]
  - request-rate: unstated; the site advertises 'no hourly limits' [1]
- limits note: The host catalogue is the artefact: 227 host pages, of which 87 appear on none of the three current host lists compared (Debridly, World-Debrid, debridr), including rapidshare, zippyshare, uploaded, share-online, netload, fileflyer, filesflash and megashares. zippyshare.com now serves a page titled 'Zippyshare.com - [now defunct] Free File Hosting', and rapidshare.com resolves to 0.0.0.0.
- binding note: No published quota and no measurement, so no constraint can be named as the one that fails first. A 227-host catalogue in which 38% of the hosts are dead brands means the likely first failure is a host that no longer exists, not a byte counter.
- interface detail: Per-host HTML pages, one per host, each a web form. No API, no plugin, no account.
- tooling: Browser only. Each host has its own static page, which is a 2010s SEO pattern rather than an API surface.
- composes with: Its catalogue overlaps the current services on 76 hosts, so it adds no coverage a paid provider among debrid providers does not already have, and it publishes no counter that a monthly plan could be built on.
- reliability: A catalogue that still lists rapidshare, zippyshare, share-online and netload has not been maintained against host churn for years, so a large share of its advertised coverage returns a dead link rather than a quota error.
- notes: PrimeLeech.com (primeleech.com) publishes the same 227-host count and the same page shape, with a different sentence set; it is documented here rather than as a second provider because counting both would double an unmeasured capacity. The 87-of-227 stale-host figure comes from a set comparison run on 2026-10-23 against the host lists of Debridly, World-Debrid and debridr (three lists, not four). Documented as a candidate that publishes no cap: it is the opposite of LeechPremium, which states 5/day and 1 GB. An operator that will not state a limit has not made a claim that can be relied on, and that absence is the finding.
- evidence note: The vendor page is captured and quoted: free, no signup, no hourly limits, 220+ hosts, script status Working. No capacity figure is published so none is measured; the stale-catalogue count is a set comparison (inferred) and no unlock was attempted.
- extras:
  - hosts_listed: 227
  - hosts_not_on_any_current_list: 87
  - sibling: primeleech.com (same 227-host count)
  - confirmed_dead_hosts_in_catalogue: zippyshare.com (defunct banner), rapidshare.com (resolves to 0.0.0.0)
  - hosts_claimed: 220+
  - script_version: 1.62 (Beta)
  - api: none found
- evidence:
  - [1] 2026-10-23: 'premium download link for free (No signup required)', 'without any hourly limits or ads', and a 227-entry host list including rapidshare, zippyshare, uploaded, share-online.biz, netload.in, fileflyer and megashares
  - [2] 2026-10-23: the page title is 'Zippyshare.com - [now defunct] Free File Hosting', so one catalogued host is confirmed dead
  - [3] 2026-10-23: resolves to 0.0.0.0 and is refused, so a second catalogued host is confirmed dead
  - [1] 2026-10-23: the free/no-signup claim, 'without any hourly limits or ads', the per-host generator list (220+ hosts claimed) and the live script/status widget
  - probe:https://www.premium-leech.com/ 2026-10-23: homepage answers: HTTP 200, 29166 bytes, sha256 ee63de181cbb7f21..., no challenge
  - [1] 2026-11-03: the vendor states free use with no hourly limits | capture: sha256:a393ad5acb511977b630c95678a8330f0d12f98969a73c6bdde8afd2eea7646b | quote: The leeched files are stored on our secure server and sent to you at maximum speed without any hourly limits or ads.
  - [4] 2026-11-03: the per-host page claims 220+ supported hosts | capture: sha256:ff5c592e268c2ff0afd83e152c6b10eb11488f585dc02877a36a37ce722dfd93 | quote: to see the 220+ other sites we support.
  - [1] 2026-11-03: no signup is required | capture: sha256:a393ad5acb511977b630c95678a8330f0d12f98969a73c6bdde8afd2eea7646b | quote: With Premium-Leech you can skip filehosting limits and payments by generating a premium download link for free (No signup required).
  - [1] 2026-11-03: no paid tier is offered; donations are optional | capture: sha256:a393ad5acb511977b630c95678a8330f0d12f98969a73c6bdde8afd2eea7646b | quote: If you like our service, please consider donating where possible (Not required).
  - [1] 2026-11-03: the vendor's status widget reads Working on the read date | capture: sha256:a393ad5acb511977b630c95678a8330f0d12f98969a73c6bdde8afd2eea7646b | quote: Script status: Working
  - [4] 2026-11-03: the per-host page repeats the 220+ host claim | capture: sha256:ff5c592e268c2ff0afd83e152c6b10eb11488f585dc02877a36a37ce722dfd93 | quote: to see the 220+ other sites we support.
- sources:
  - [1] https://www.premium-leech.com/
  - [2] https://www.zippyshare.com
  - [3] https://rapidshare.com
  - [4] https://www.premium-leech.com/premium-generator/rapidgator-generator.html
