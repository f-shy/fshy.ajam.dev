# FileSharingTalk NZBs

> filesharingtalk.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filesharingtalk/ | JSON https://fshy.ajam.dev/api/v1/entity/filesharingtalk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileSharingTalk NZBs

- `debrid/filesharingtalk` | qualifies-with-caveat | evidence reported | binding request-rate | category Usenet NZB index (vBulletin forum, no API) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-11-18
- url https://filesharingtalk.com/nzbs/
- free tier: Reported allowance on a free account: 2 NZBs per day; no API because it is a forum. The NZB section lists current releases and has a Register link. | unit: objects | metered on: request-count | read on: 2026-11-03 | source: [1] | note: The allowance is third-party; a second listing describes the site as forum-based NZB link sharing rather than NZB files, so what a download returns was not confirmed.
- per-object cap: not applicable: an NZB pointer file or a link, never the payload | source: [2]
- retention: not stated on the pages read. A third-party listing claims 'Approximately 500 days'. | source: [3] | note: reported
- egress: No byte metering; the answer is an NZB pointer file or a link. | metered: no | source: [2]
- identity: email | detail: unverified: the register form was not read; the section shows a Register link and third-party listings call registration open. A forum sign-up normally takes an email address.
- interface: unknown
- limits:
  - request-rate (binding): reported: 2 NZBs per day on a free account, no API [1]
- binding note: The two NZBs a day is the only numeric limit named, and it is third-party.
- interface detail: A vBulletin forum with a releases section; NZBs are fetched through the web UI after login. Third-party listings state it has no API.
- endpoint: https://filesharingtalk.com/nzbs/
- tooling: A wrapper has to log in and drive the forum pages; Prowlarr and NZBHydra2 cannot add a forum as a Newznab indexer. That is a tooling note, not a verdict.
- composes with: A manual fallback for a name that the API indexers lack; 2 NZBs a day makes it a last-resort grab, not a bulk path.
- reliability: A third-party listing reports 99% uptime and a 1,776ms response time; the section loaded today.
- evidence note: The live release list and the Register link are first-party; the allowance, the price and the open registration are third-party.
- extras:
  - price: USD 0 (free); USD 2 to 30 donor plans (reported)
- evidence:
  - [2] 2026-11-03: the NZB section lists a 2026 release on the read date, so it is live | capture: sha256:fc1aa63b69354553c7f22e34cd5de00a8b7d027ff21f793158ec677940f42050 | quote: Whos Coming for Christmas 2026 1080p WEB h264-EDITH
  - [2] 2026-11-03: the section exposes a registration link | capture: sha256:fc1aa63b69354553c7f22e34cd5de00a8b7d027ff21f793158ec677940f42050 | quote: - [Register](https://filesharingtalk.com/nzbs/register.php?s=1dae7f65d80e73f5168062e3cb52110e)
  - [1] 2026-11-03: third-party: a free account gets 2 NZBs per day and there is no API | capture: sha256:8b2ad2f0d700a37b464f5b17e1b9fc9cfed7b2b5e66e5db2ba050be1300de759 | quote: 2 NZBs /day (Forum, so there is no API)
  - [3] 2026-11-03: third-party: paid donor plans run from USD 2 to USD 30 for 1 month to 5 years | quote: Donor $2-$30 for 1 month to 5 years
- sources:
  - [1] https://github.com/openlemmy/reddit-backups/wiki/Indexers
  - [2] https://filesharingtalk.com/nzbs/
  - [3] https://nzbhydra.com/indexers/
