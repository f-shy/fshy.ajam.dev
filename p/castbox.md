# Castbox Creator Studio

> castbox.fm | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/castbox/ | JSON https://fshy.ajam.dev/api/v1/entity/castbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Castbox Creator Studio

- `storage/castbox-creator-studio` | qualifies-with-caveat | evidence inferred | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-11-25T01:53:16.159Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://castbox.fm
- free tier: 'There is no limit on uploading storage (total) for a channel.' Per-file cap 400 MB, from a help page last updated 7 years ago ('Updated: 7 years ago'). The 400 MB figure is stale and should be treated as unverified. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 400 MB per file | bytes: 400000000 | source: [1] | note: the maximum file size is 400M, from a help article labelled Updated:7 years ago
- retention: source: [1] | note: No retention period is stated in the publisher's help articles; a published channel page carries no retention clause.
- egress: No egress charge appears in the first-party creator help articles; the publisher presents itself as a free podcast app. | metered: no
- identity: email
- interface: browser
- limits:
  - per-object-cap (binding): 400 MB per file [1]
- limits note: 400 MB per file (2019-era doc); accepted WAV/MP3/MP4/AAC/M4A. No retention or bandwidth figure published anywhere.
- interface detail: wrapper-only
- tooling: Creator Studio web dashboard only; no API. Castbox is primarily a player, so its hosting is a sideline.
- composes with: Unlimited channels x unlimited episodes, if the 'no limit on total storage' line still holds. Multiple accounts are email-only.
- reliability: Unverifiable. The hosting doc carries no date beyond 'Page updated' and the file-type doc says 'Updated: 7 years ago'.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'There is no limit on uploading storage (total) for a channel.'
  - [2] 2026-10-21: 'the maximum file size is 400M'; 'Updated: 7 years ago'
  - withheld 2026-10-21: probe: GET castbox.fm/rss/3678725 -> 302 -> castbox.fm/404.html (no public enclosure path found)
  - [3] 2026-11-25: the help center documents a web-only Creator Studio upload path | capture: sha256:d96fa34540c7fa21fbd145de32e9f43e2b81d2b4cfddc6c70f31052b515e6d95 | quote: Go to Creator Studio on our desktop site and sign in. Please note that you will need to sign up a Castbox account if you haven’t got one.
  - [2] 2026-11-25: the current help-center article states a 400M maximum file size | capture: sha256:5231399ce78fa3d8664405d1ff0d0dfbb4f660aa7647af74d2166687fee3806c | quote: In addition, the maximum file size is 400M.
  - [4] 2026-11-25: the first-party site presents Castbox as a podcast app and states no retention period | capture: sha256:8d23c8dbf500e89dbf1a5bc9e03736316facd7b62ca888d257fac455dabf580b | quote: Castbox is the best free podcast app with over 259 million volumes of content on Android, Apple iPhone, Amazon Alexa, Google Home, Carplay and Android Auto.
  - [4] 2026-11-25: the first-party site describes a free podcast app without an egress charge | capture: sha256:8d23c8dbf500e89dbf1a5bc9e03736316facd7b62ca888d257fac455dabf580b | quote: Castbox is the best free podcast app with over 259 million volumes of content on Android, Apple iPhone, Amazon Alexa, Google Home, Carplay and Android Auto.
  - [3] 2026-11-25: the help center documents a browser drag-and-drop upload path | capture: sha256:d96fa34540c7fa21fbd145de32e9f43e2b81d2b4cfddc6c70f31052b515e6d95 | quote: Select or drag and drop the audio file you’d like to upload.
  - [2] 2026-11-25: the file-size article carries its own update date | capture: sha256:5231399ce78fa3d8664405d1ff0d0dfbb4f660aa7647af74d2166687fee3806c | quote: Updated:7 years ago
  - [4] 2026-11-25: the first-party site presents a free podcast app and states no retention period or charge | capture: sha256:8d23c8dbf500e89dbf1a5bc9e03736316facd7b62ca888d257fac455dabf580b | quote: Castbox is the best free podcast app with over 259 million volumes of content on Android, Apple iPhone, Amazon Alexa, Google Home, Carplay and Android Auto.
- sources:
  - [1] https://sites.google.com/castbox.fm/castbox-help-center/podcasters/getting-started/2-start-a-podcast-hosted-on-castbox-for-free
  - [2] https://helpcenter.castbox.fm/portal/en/kb/articles/file-types-when-uploading
  - [3] https://helpcenter.castbox.fm/portal/en/kb/articles/starting-a-podcast
  - [4] https://castbox.fm
