# mail.com free

> mail.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mail-4/ | JSON https://fshy.ajam.dev/api/v1/entity/mail-4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mail.com free (65 gb — but read-gated behind premium)

- `storage/mail-com-free` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:08.542Z (live) | stale on 2026-12-04
- url https://www.mail.com/mail/email-storage/
- free tier: none reachable: The 65 GB is real and the largest free mailbox found: "mail.com offers you up to 65 GB of email storage". But the read/write path is closed on the free tier: "these protocols [POP3, IMAP… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The 65 GB is real and the largest free mailbox found: "mail.com offers you up to 65 GB of email storage". But the read/write path is closed on the free tier: "these protocols [POP3, IMAP…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The 65 GB is real and the largest free mailbox found: "mail.com offers you up to 65 GB of email storage". But the read/write path is closed on the free tier: "these protocols POP3, IMAP, SM
  - [2] 2026-10-21: cited as the basis of the rejection: The 65 GB is real and the largest free mailbox found: "mail.com offers you up to 65 GB of email storage". But the read/write path is closed on the free tier: "these protocols POP3, IMAP, SM
  - [1] 2026-11-19: the free mailbox still advertises up to 65 GB of email storage | capture: sha256:297b7bac85ee7d5f427e609bf934809e4fea29264aa89f95e4a72899ab63b890 | quote: mail.com offers you up to 65 GB of email storage, or space for about half a million emails.
  - [2] 2026-11-19: the read/write protocol path remains a paid Premium feature, so the free 65 GB cannot be used as storage | capture: sha256:c0fe89a2f1bf57ac844ca5e2bc3ec25f7d6663da2b9c8df11bccade719267131 | quote: POP3 and IMAP access is turned off by default in mail.com and is a Premium feature.
- sources:
  - [1] https://www.mail.com/mail/email-storage/
  - [2] https://www.mail.com/blog/posts/what-is-imap-pop3/86/
