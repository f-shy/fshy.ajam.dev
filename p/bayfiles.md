# bayfiles

> bayfiles.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bayfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/bayfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bayfiles / anonfiles

- `storage/bayfiles-anonfiles` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:38:40.819Z (live) | stale on 2026-12-04
- url https://bayfiles.com/
- free tier: none reachable: Both gone, and they are not the same story. AnonFiles shut down August 2023 citing the volume of excess use; BayFiles' 2023-era successor domain no longer resolves. Neither has a free successor operatin | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: Max 20 GB per file | source: [1] | note: 20 GB per-file ceiling stated on the first-party homepage
- retention: For as long as possible | source: [1] | note: retention stated as for as long as possible, subject to the terms
- egress: unlimited downloads and no speed limits; hourly and daily traffic quotas are listed | metered: no
- identity: email
- interface: rest, browser
- interface detail: REST POST upload API returning a share URL in JSON, plus browser download URLs
- tooling: curl -F file=@ to POST an upload; GET the returned URL to download
- composes with: direct share URLs returned on upload; files retrieved by that URL
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Both gone, and they are not the same story. AnonFiles shut down August 2023 citing the volume of excess use; BayFiles' 2023-era successor domain no longer resolves. Neither has a free successor operatin
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Both gone, and they are not the same story. AnonFiles shut down August 2023 citing the volume of excess use; BayFiles' 2023-era successor domain no longer resolves. Neither has a free successor operatin
  - [2] 2026-10-21: cited as the basis of the rejection: Both gone, and they are not the same story. AnonFiles shut down August 2023 citing the volume of excess use; BayFiles' 2023-era successor domain no longer resolves. Neither has a free successor operatin
  - probe:https://bayfiles.com/ 2026-11-19: a probe today could not resolve the BayFiles host | capture: sha256:21c6e7b3c3c518bf8b85edf02216632d8955ab2bf647b4a6e7386df3a8710dea | quote: "status": null
  - probe:https://anonfiles.com/ 2026-11-19: a probe today could not resolve the AnonFiles host | capture: sha256:9e642996b8abe84caffb66434a3ebe97122c7b399b9fd9674ad2128678e99564 | quote: "status": null
  - [3] 2026-11-19: the offer has a REST upload API returning a JSON download URL | capture: sha256:336394ffc9250205fb5556d87d5ef49646386b1f0d829fa7fec333dca746c885 | quote: You send us files with POST and we will store them and return an url for you in JSON.
  - [3] 2026-11-19: curl -F is the documented upload tool | capture: sha256:336394ffc9250205fb5556d87d5ef49646386b1f0d829fa7fec333dca746c885 | quote: curl -F "file=@test.txt" https://api.bayfiles.com/upload
  - [4] 2026-11-19: the per-object ceiling is 20 GB | capture: sha256:b5fade677eeee9c3600a04884b8ac779363f42f0dd5065a5cdac0ea932b6a85d | quote: Max 20 GB per file - unlimited downloads and no speed limits.
  - [5] 2026-11-19: the stated retention is for as long as possible | capture: sha256:1caaab2c46e3caead4b1c369fec4005eaf0492a62a224267b33c8c74d0177907 | quote: For as long as possible
  - [6] 2026-11-19: the archived first-party AnonFiles notice confirms the shutdown | capture: sha256:3d45252b717a89fdb9712cda3917757f0f394d3708c5530ccad923c62f620b82 | quote: Domain 4sale.
  - probe:https://bayfiles.com/ 2026-11-19: the live BayFiles domain did not resolve on the read date | capture: sha256:1f71f9d54f08c9b8586300dff5b6eedd7bd38438c6b108bf61a3c9b052e2c17a | quote: "status": null
  - [6] 2026-11-19: the first-party AnonFiles shutdown notice states the service ended because of the extreme volume of abuse | capture: sha256:3d45252b717a89fdb9712cda3917757f0f394d3708c5530ccad923c62f620b82 | quote: After trying endlessly for two years to run a file sharing site with user anonymity we have been tired of handling the extreme volumes of people abusing it and the headaches it has created for us.
- sources:
  - [1] https://bayfiles.com/
  - [2] https://anonfiles.com/
  - [3] https://web.archive.org/web/20230810101823/https://bayfiles.com/docs/api?provider=wayback
  - [4] https://web.archive.org/web/20230810101823/https://bayfiles.com/?provider=wayback
  - [5] https://web.archive.org/web/20230810101823/https://bayfiles.com/faq?provider=wayback
  - [6] https://web.archive.org/web/20230913092920/https://anonfiles.com/?provider=wayback
