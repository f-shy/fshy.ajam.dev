# MultiUp.io

> multiup.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/multiup/ | JSON https://fshy.ajam.dev/api/v1/entity/multiup.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MultiUp.io

- `debrid/multiup` | qualifies-with-caveat | evidence documented | binding per-object-cap | category multi-host mirror uploader with remote URL pull (server-side fetch to 30+ hosts) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:51.629Z (live) | stale on 2026-12-26
- url https://multiup.io/en/upload/from-links
- price USD 0
- free tier: The service is free and ad-funded: 'All which is here is free. This service is supplied to you in the state and its use is completely free. This service is self-financed by advertisements.' A remote pull from a link is an account feature: the from-links page shows 'Account required'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: Free account storage and daily volume are not published on the pages read; only per-host file caps are shown.
- per-object cap: Per destination host, shown next to each: 1fichier 300 GB, GoFile 500 GB, MediaFire 20 GB, KatFile 5 GB, Ddownload 2 GB, 4Shared 2 GB, Filer.net 512 MB. A file must fit every host it is sent to. | bytes: 536870912 | source: [2] | note: 512 MB is the smallest cap on the page (Filer.net); the user picks the hosts, so the effective cap is the smallest selected.
- retention: unverified: retention follows each destination host's own policy, and no aggregate statement exists. | source: [1]
- egress: Downloads happen from the destination hosts, each with its own free-tier rules; MultiUp itself serves only the index page (multiup.io/download/NUMBERS/FILE_NAME). | metered: no | free allowance: host-dependent | source: [1]
- identity: email | detail: An account is required for remote upload, and the service is a standard web registration; the exact fields were not read because registration was not attempted.
- interface: browser
- limits:
  - per-object-cap (binding): 512 MB (smallest host cap, Filer.net); up to 300 GB on 1fichier, 500 GB on GoFile [2]
  - write-gated: remote pull requires an account; the form states 'Account required' [2]
- limits note: The premium page lists only resellers of premium keys (GeekDot, PremiumKeys, 24instant and others), not a price or a feature table, so what premium adds is not documented on that page.
- binding note: A 1 TiB/month plan is limited first by which hosts accept the file size, and the smallest useful host caps at 512 MB. The account gate comes before that, but once past it the byte ceiling is per object, not per month.
- interface detail: A web upload form at /en/upload/from-links that accepts HTTP or FTP source links, a host checklist, a terms checkbox and 'Parallel upload'. No API documentation page was found.
- tooling: Browser. The service is designed for interacting uploaders; no CLI or API is documented, so a wrapper drives the form.
- composes with: It turns one URL into N host copies, which is the mirror half of a storage plan: the same file survives one host dying. It does not download to the caller at all, so it composes with a later fetch from whichever host is alive.
- reliability: Mirroring multiplies failure: each destination host can reject, throttle or delete the copy independently, and the index page then lists mixed online/offline links. The site is ad-funded and has run since 2008.
- notes: The best URL-to-many-hosts relay found: one pull, thirty copies, no bandwidth through the caller. The caveat is the account and the 512 MB floor when Filer.net is selected. No programmatic path found: A web upload form at /en/upload/from-links that accepts HTTP or FTP source links, a host checklist, a terms checkbox and 'Parallel upload'. No API documentation page was found.
- evidence note: The account requirement and the per-host caps are quoted from the live pages. No remote pull was executed, which is what a measured rung needs.
- extras:
  - destination_hosts: 30+
  - smallest_cap: 512 MB (Filer.net)
  - largest_cap: 500 GB (GoFile, BuzzHeavier, Chomikuj, DataNodes, Drive.Google, FireLoad, FTP, FTP2, Media.cm, Mega.nz, Send.now, Theuser.cloud, VikingFile)
- evidence:
  - [2] 2026-10-23: 'You can remotely upload files from HTTP or FTP'; 'Account required'; the host checklist with per-host caps (1fichier 300.00 GB, GoFile 500.00 GB, Filer.net 512.00 MB)
  - [1] 2026-10-23: 'All which is here is free ... self-financed by advertisements'; the output link shape https://multiup.io/download/NUMBERS/FILE_NAME and the 30+ destination hosts
  - [3] 2026-10-23: the only monetisation shown is a list of third-party key resellers; no price or feature table appears
  - probe:https://multiup.io/en/upload/from-links 2026-10-23: HTTP 200, 133537 bytes, sha256 7597d0194c17c414..., no challenge
  - [2] 2026-11-25: the from-links form still accepts HTTP or FTP URLs and states that an account is required | capture: sha256:cc6c1fd3580d693a34af09fc9c493eb77da9967187eeaccdf42561ab05b5680e | quote: You can remotely upload files from HTTP or FTP ... Account required ... Parallel upload
  - [2] 2026-11-25: host caps still run from 512 MB on Filer.net to 300 GB on 1fichier and 500 GB on GoFile | capture: sha256:cc6c1fd3580d693a34af09fc9c493eb77da9967187eeaccdf42561ab05b5680e | quote: Filer.net (512.00 MB) ... 1fichier.com (300.00 GB) ... GoFile.io (500.00 GB)
  - [2] 2026-11-25: the 500 GB ceiling is shared by several listed hosts, not only GoFile | capture: sha256:cc6c1fd3580d693a34af09fc9c493eb77da9967187eeaccdf42561ab05b5680e | quote: BuzzHeavier.com (500.00 GB) ... Chomikuj.pl (500.00 GB) ... GoFile.io (500.00 GB)
  - [2] 2026-11-25: the 500 GB ceiling is shared by several listed hosts | capture: sha256:cc6c1fd3580d693a34af09fc9c493eb77da9967187eeaccdf42561ab05b5680e | quote: BuzzHeavier.com (500.00 GB) ... Chomikuj.pl (500.00 GB) ... GoFile.io (500.00 GB)
  - [1] 2026-11-25: the service mirrors uploads to host sites and returns an index link, not a download stream | capture: sha256:f8b8765f92b658c786a453bdaffc51ff082df447c653ed7b8564155c09a0d844 | quote: MultiUp.io is a multiupload website, that is: you upload a file on our server, this one is uploaded automatically, on several hosting-file websites. In the end you obtain a link of the shape : https://multiup.io/download/NUMBERS/FILE_NAME
  - [1] 2026-11-25: service still states a free ad-funded tier | capture: sha256:f8b8765f92b658c786a453bdaffc51ff082df447c653ed7b8564155c09a0d844 | quote: No, absolutely not. All which is here is free. This service is supplied to you in the state and its use is completely free. This service is self-financed by advertisements.
- sources:
  - [1] https://multiup.io/en/faq
  - [2] https://multiup.io/en/upload/from-links
  - [3] https://multiup.io/en/premium
