# archive.org forum '10gb per item' guidance

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/archive-org-forum-10gb-per-item-guidance/ | JSON https://fshy.ajam.dev/api/v1/entity/archive-org-forum-10gb-per-item-guidance.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## archive.org forum '10gb per item' guidance

- `storage/archive-org-forum-10gb-per-item-guidance` | qualifies-with-caveat | evidence documented | binding per-object-cap | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-25T01:53:16.159Z (live) | stale on 2026-12-26
- url https://archive.org/post/379280/file-size-limit
- free tier: 1 TB size limit per item page, recommended maximum 1000 files or 500 GB per item (help centre). The forum answer of 7 Jun 2011 that gave 10 GB per item is superseded. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1] | note: the figure is per item page; the help page states no total per account
- per-object cap: 1 TB per item page; recommended maximum 500 GB or 1000 files per item | source: [1] | note: not applicable
- retention: As an archive our intention is to store and make materials in perpetuity. | source: [1]
- egress: No transfer charge is published; uploaded items can be downloaded and taken elsewhere. | metered: no
- identity: email | detail: email address (with an emailed code), screen name and password
- interface: browser, cli
- limits:
  - per-object-cap (binding): 1 TB per item page [2]
  - per-object-cap (binding): 500 GB or 1000 files per item (recommended maximum) [2]
- limits note: 1 TB is the stated size limit for an item page; 500 GB or 1000 files per item is the recommended maximum because large items can break or time out in derive.
- binding note: the size limit applies per item page (1 TB hard, 500 GB recommended); the page states no total per account
- interface detail: not documented
- tooling: the same as interface detail
- composes with: Items can be exported from the user's library and taken elsewhere; bulk or programmatic uploads use the Internet Archive Command-Line Tool.
- reliability: 10 GB per item is a 2011 forum answer, superseded by the help-centre limit of 1 TB per item page; items near the limit can break and time out in derive.
- notes: the same as the free tier
- evidence note: The 2026-11-03 evidence rows read https://help.archive.org/help/uploading-tips/ (item page size limit and recommended maximum), https://archive.org/post/ (thread file-size-limit) (the 10GB answer posted Jun 7, 2011) and https://archive.org/account/signup (email, screen name, password). Every field that decides the verdict cites those captures.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Decade-old staff answer; superseded. Real current limits are 1TB/item.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Decade-old staff answer; superseded. Real current limits are 1TB/item.
  - [2] 2026-11-03: the help centre states a 1 TB limit per item page and recommends at most 1000 files or 500 GB per item | capture: sha256:564fefcac70be53c580b0ba5f11e4bf3e503dd82ee08ca2575a1fcbd66459043 | quote: Currently, there is a 1TB size limit for item pages. However, from a systems perspective, we recommend a maximum of 1000 files or 500GB of data per item page.
  - [2] 2026-11-03: large items can break and time out in derive, which is why 500 GB is the recommended size | capture: sha256:564fefcac70be53c580b0ba5f11e4bf3e503dd82ee08ca2575a1fcbd66459043 | quote: This is because items can “break” as well as take a very long time to derive and can often timeout and fail.
  - [1] 2026-11-03: the 10 GB answer was posted on 7 Jun 2011 | capture: sha256:bac7e6ef21672c32533dade5bdae52eba0361828018f4cd029099ce407b27097 | quote: | Poster: | Jeff Kaplan | Date: | Jun 7, 2011 9:30am |
  - [3] 2026-11-03: sign-up asks for an email address (with an emailed code), a screen name and a password | capture: sha256:4b8b71aa7dd07a92b006c16919f3bc85576963d0e7852ea30ce4dd5b0a6cafee | quote: Email me a code to sign upEnter your email addressUp to 127 characters
  - [1] 2026-11-03: the forum answer gives 10 GB per item | capture: sha256:bac7e6ef21672c32533dade5bdae52eba0361828018f4cd029099ce407b27097 | quote: Items (pages) should not exceed 10GB whether there is one file or many.
  - [1] 2026-11-04: the forum answer gives 10 GB per item | capture: sha256:bac7e6ef21672c32533dade5bdae52eba0361828018f4cd029099ce407b27097 | quote: Items (pages) should not exceed 10GB whether there is one file or many.
  - [4] 2026-11-25: the Help Center states an intention to store materials in perpetuity | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: As an archive our intention is to store and make materials in perpetuity.
  - [5] 2026-11-25: the upload guide documents a command-line upload tool alongside the browser path | capture: sha256:2af054d55dffcd44c8d0693ae3231334ab0a26da635bddc2219a2aa78c8b5d20 | quote: We recommend using the Internet Archive Command-Line Tool to script your upload.
  - [4] 2026-11-25: the Help Center documents that uploaded items can be downloaded and moved elsewhere | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: If you have uploaded things to the Internet Archive, you can find a list of them from the “my library” link on your settings page. From there, you can download the items and take them anywhere.
  - [4] 2026-11-25: the Help Center documents taking uploaded items elsewhere | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: If you have uploaded things to the Internet Archive, you can find a list of them from the “my library” link on your settings page. From there, you can download the items and take them anywhere.
  - [4] 2026-11-25: the Help Center states perpetual storage intent and free upload, download and export of items | capture: sha256:fe9147750a0184115f838677d71f07380a8308305f94c6e515913845a60f9505 | quote: As an archive our intention is to store and make materials in perpetuity.
- sources:
  - [1] https://archive.org/post/379280/file-size-limit
  - [2] https://help.archive.org/help/uploading-tips/
  - [3] https://archive.org/account/signup
  - [4] https://help.archive.org/help/archive-org-information/
  - [5] https://help.archive.org/help/uploading-a-basic-guide/
