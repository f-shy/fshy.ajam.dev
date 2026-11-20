# ebird

> ebird.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ebird/ | JSON https://fshy.ajam.dev/api/v1/entity/ebird.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ebird / macaulay library

- `storage/ebird-macaulay-library` | fails-quota | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:35.336Z (live) | stale on 2026-12-04
- url https://support.ebird.org/en/support/solutions/articles/48000825713
- free tier: none reachable: photos must be JPG under 20 MB each and audio uncompressed WAV up to 500 MB each; every asset must be added to an eBird checklist matching the exact date, time and location, and only media of birds actually reported is accepted | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: JPG photos under 20 MB each; uncompressed WAV audio up to 500 MB each | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: a free eBird account is required to add media; *If the Add Media / Manage Media button doesn’t appear, make sure you are logged into your eBird account.* No card or phone number is stated on this page
- interface: browser
- interface detail: eBird website (Manage Media / Add Media) and eBird Mobile; media attaches to a submitted checklist
- tooling: not documented
- composes with: not recorded
- reliability: A real media archive with no total quota, but JPG under 20 MB, WAV under 500 MB, and only media of birds on an exactly matching date/location checklist is accepted; audio spectrogram generation queues at peak contribution months
- notes: A real media archive with no total quota, but JPG only under 20 MB and WAV under 500 MB, and every asset must attach to a valid checklist (species, count, location, date). Effectively 20 MB
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: A real media archive with no total quota, but JPG only under 20 MB and WAV under 500 MB, and every asset must attach to a valid checklist (species, count, location, date). Effectively 20 MB
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A real media archive with no total quota, but JPG only under 20 MB and WAV under 500 MB, and every asset must attach to a valid checklist (species, count, location, date). Effectively 20 MB
  - [1] 2026-11-19: photos are limited to JPG under 20 MB | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: Upload full-resolution images, as long as they are JPG and under 20 MB each.
  - [1] 2026-11-19: audio files are limited to 500 MB each | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: Uncompressed .WAV files, which are higher quality than .mp3 or .m4a, up to 500 MB each.
  - [1] 2026-11-19: media is uploaded and stored through the eBird website and mobile app | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: As soon as you add a photo, audio recording, or video to your eBird checklist, the media enters the Macaulay Library archival system where it is safely stored.
  - [1] 2026-11-19: media is attached to a checklist through the eBird website | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: 4. [Go to your eBird checklist](https://ebird.org/mychecklists) containing the record for that specific bird
  - [1] 2026-11-19: an eBird login is required to upload media | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: If the Add Media / Manage Media button doesn’t appear, make sure you are logged into your eBird account.
  - [1] 2026-11-19: audio processing is queued and slows at peak times | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: during the peak media contribution months of May and June this process can take longer than normal
  - [1] 2026-11-19: the record's rejection basis is confirmed against the first-party media guidelines | capture: sha256:4120cdeb2d444b1927279c63fd2439a9fa12ddce02e5ee9f81589fe6ea2b26cb | quote: Media must be added to the eBird checklist that matches the exact date, time, and location where the recording was made.
- sources:
  - [1] https://support.ebird.org/en/support/solutions/articles/48000825713
