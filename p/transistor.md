# simplecast

> transistor.fm | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/transistor/ | JSON https://fshy.ajam.dev/api/v1/entity/transistor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## simplecast / transistor / captivate / libsyn — unlimited storage, no free t

- `storage/simplecast-transistor-captivate-libsyn-unlimited-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:50.377Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/transistor.md
- free tier: None reachable: All four advertise genuinely unlimited (!) audio storage or uploads, and Transistor and Captivate even leave a properly made MP3 untouched on the way through. The right behaviour, on the wr. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: Individual audio files can be up to 2 GB; video files can be up to 30 GB. | note: not applicable
- retention: not stated on https://www.simplecast.com/pricing
- egress: Monthly audio downloads are metered; the Starter plan includes 40,000 downloads. | metered: no
- identity: email
- interface: browser
- interface detail: Podcast hosting reached through the web, with an RSS feed for distribution to listening apps.
- tooling: not documented
- composes with: A single upload distributes the episode to more than 20 listening platforms.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: All four advertise genuinely unlimited (!) audio storage or uploads, and Transistor and Captivate even leave a properly made MP3 untouched on the way through — the right behaviour, on the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: All four advertise genuinely unlimited (!) audio storage or uploads, and Transistor and Captivate even leave a properly made MP3 untouched on the way through — the right behaviour, on the…
  - [1] 2026-11-19: Transistor's live pricing page still advertises unlimited audio storage | capture: sha256:3ef26f7494a4c905454e5dce660817b17f85a63fe9e595f99c00bd94194bce79 | quote: - Unlimited audio storage
  - [2] 2026-11-19: Captivate's live pricing page advertises unlimited podcasts and storage | capture: sha256:65335b0681b0bdc3fd9f7627ffbfb5b7cce463a6ca26ec766ca833e4787566ce | quote: Unlimited podcasts and storage
  - [3] 2026-11-19: Simplecast's live pricing FAQ confirms unlimited audio storage on its plans | capture: sha256:9a349bafe8d412bfd5047c79c142592c679009d7605d40f7d9b962c06bd329fa | quote: Absolutely. Who are we to put limits on your creativity?!
  - [4] 2026-11-19: Simplecast hosts an RSS feed, which is the client-facing access surface | capture: sha256:9a349bafe8d412bfd5047c79c142592c679009d7605d40f7d9b962c06bd329fa | quote: reliable hosting for your RSS feed and podcast
  - [4] 2026-11-19: all Simplecast plans publish directly to listening platforms | capture: sha256:9a349bafe8d412bfd5047c79c142592c679009d7605d40f7d9b962c06bd329fa | quote: all plans offer direct publishing to all platforms, like Apple Podcasts, Spotify, Google Podcasts, and Overcast
  - [1] 2026-11-19: Transistor states a 2 GB per-audio-file and 30 GB per-video-file limit | capture: sha256:3ef26f7494a4c905454e5dce660817b17f85a63fe9e595f99c00bd94194bce79 | quote: Individual audio files can be up to 2 GB; video files can be up to 30 GB.
  - [5] 2026-11-19: a single Libsyn upload distributes to more than 20 listening platforms | capture: sha256:a4a4baa676c413c9290a4cb6dec9526517dd1735d9b153d2398bf24d8d8532c9 | quote: Libsyn sends your podcast to Apple Podcasts, Spotify, YouTube, and more than 20 other platforms with just one upload.
  - [1] 2026-11-19: Transistor meters a monthly download allowance on the Starter plan | capture: sha256:3ef26f7494a4c905454e5dce660817b17f85a63fe9e595f99c00bd94194bce79 | quote: 40,000 monthly audio downloads
- sources:
  - [1] https://transistor.fm/pricing/
  - [2] https://www.captivate.fm/pricing/
  - [3] https://simplecast.com/pricing/
  - [4] https://www.simplecast.com/pricing
  - [5] https://libsyn.com/plans-and-pricing/
