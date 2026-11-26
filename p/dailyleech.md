# DailyLeech

> dailyleech.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dailyleech/ | JSON https://fshy.ajam.dev/api/v1/entity/dailyleech.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DailyLeech

- `debrid/dailyleech` | paid-only | evidence documented | binding volume-quota | category multi-hoster (chat-room downloader with a daily quota) | tier Premium plan
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:52.402Z (live) | stale on 2026-12-26
- url https://dailyleech.com/
- free tier: No free quota stated: a free account is created, then a plan is picked. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the bot replies with the file name and size; no cap stated | source: [1]
- retention: unverified: not stated | source: [1]
- egress: A fresh allowance every day, metered per host; the counter and reset time are shown above the chat. | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: The page says to create a free account and pick a plan; cards and crypto are accepted. The form fields were not read, so the email requirement is unverified.
- interface: unknown
- limits:
  - volume-quota (binding): a daily allowance metered per host; sizes unverified [1]
- binding note: A per-host daily allowance is the stated metering.
- interface detail: A live chat room where a link is posted and the bot answers with the link; an API key for JDownloader is included.
- tooling: Browser chat, JDownloader.
- composes with: Torrent box (magnet link, pick files) included with the plan.
- reliability: No outage observed on the day read.
- notes: Plan price: unverified.
- evidence note: First-party home page; /pricing answered 404.
- evidence:
  - [1] 2026-11-03: an account is free, then a plan is required; cards and crypto are accepted | capture: sha256:644ffc443f122b0e25585a415e869d8b70e6cf49af1c62f5a31df00a8aab098f | quote: Create a free account, then pick a plan. Cards and crypto are both accepted.
  - [1] 2026-11-03: the allowance is daily and per host | capture: sha256:644ffc443f122b0e25585a415e869d8b70e6cf49af1c62f5a31df00a8aab098f | quote: A fresh allowance every day, metered per host so one large file never eats the rest.
  - [1] 2026-11-03: magnet links and a JDownloader API key are supported | capture: sha256:644ffc443f122b0e25585a415e869d8b70e6cf49af1c62f5a31df00a8aab098f | quote: Add a magnet link and pick exactly the files you want, or hand your API key to JDownloader.
  - [1] 2026-11-25: a free account is followed by a paid plan; cards and crypto are accepted | capture: sha256:051577c1a690f277f7a4a00a79191e4d25c018e140d1e75861c06ee1f8929584 | quote: Create a free account, then pick a plan. Cards and crypto are both accepted.
  - [1] 2026-11-25: the allowance is still daily and metered per host | capture: sha256:051577c1a690f277f7a4a00a79191e4d25c018e140d1e75861c06ee1f8929584 | quote: A fresh allowance every day, metered per host so one large file never eats the rest.
  - [1] 2026-11-25: magnet links and a JDownloader API key are still described | capture: sha256:051577c1a690f277f7a4a00a79191e4d25c018e140d1e75861c06ee1f8929584 | quote: Add a magnet link and pick exactly the files you want, or hand your API key to JDownloader.
- sources:
  - [1] https://dailyleech.com/
