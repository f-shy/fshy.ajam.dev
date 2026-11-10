# Seznam.cz Email

> seznam.cz | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seznam/ | JSON https://fshy.ajam.dev/api/v1/entity/seznam.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Seznam.cz (email-as-storage)

- `storage/seznam-cz` | qualifies-with-caveat | evidence reported | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.seznam.cz
- free tier: Mailbox is byte-unlimited: 'Uživatel může schránku využívat v neomezené velikosti', with a 120,000-message cap that can be raised repeatedly | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No metered egress; IMAP/POP access is included | metered: yes
- identity: any-phone
- interface: sftp, rclone
- limits note: 35 MB attach send from web (25 MB mobile), 50 MB receive per message; 120,000 messages/mailbox
- interface detail: sftp
- tooling: IMAP (standard clients, rclone 'imap' style tooling via a mail-to-blob shim); no dedicated backend
- composes with: One mailbox x 120,000 messages x 35-50 MB per message is a multi-TB theoretical ceiling; identities are the limit
- reliability: message-count cap plus per-message size cap is the real ceiling; touchy about bulk IMAP
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 'Create a new e-mail address with Seznam. Or use your existing one: Gmail, Outlook, or another. / Create @seznam.cz address · Use my existing email · Use phone number'
  - [2] 2026-10-21: phone flow: 'In the next step, you will verify your phone number by entering the SMS code'; raw HTML has three <input name="phone" maxlength="3"> prefix boxes plus a disabled suffix box
  - [2] 2026-10-21: existing-email flow: 'To verify your email address, enter the verification code we sent to your email'
- sources:
  - [1] https://www.seznam.cz
  - [2] https://registrace.seznam.cz/

## Seznam.cz Email — unlimited-size mailbox, message-count-bound

- `storage/seznam-cz-email-unlimited-size-mailbox-message-count-bou` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.seznam.cz
- free tier: Docs page states verbatim: "Uživatel může schránku využívat v neomezené velikosti. V praxi je každá schránka založena s limitem na 120 000 zpráv, který lze opakovaně navyšovat." = unlimited mailbox size; in practice each mailbox starts with a 120,000-message limit that can be raised repeatedly (on request). This is the only webmail found where the published limit is a MESSAGE COUNT, not a byte quota. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 35 MB | bytes: 35000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered by the provider. No transfer meter is published or charged; mail is delivered by SMTP/IMAP, not metered HTTP GET. No egress pricing exists for a mailbox. | metered: no
- identity: email
- interface: rest, rclone
- limits:
  - per-object-cap (binding): per-object-cap 35 MB [1]
- limits note: Per-object-cap 35 MB attach send from web (25 MB from mobile app), 50 MB receive per message. That is the real per-blob size. 120,000 messages/mailbox is the binding constraint (a pull-count-style ceiling on object count, raisable on request). Sending-rate limits exist but are explicitly unpublished: "Tyto limity nejsou veřejné.".
- interface detail: rest
- tooling: Native IMAP, probe-verified live: `imap.seznam.cz:993` -> `* OK Seznam IMAP server ready` / `* CAPABILITY XLIST IMAP4rev1 AUTH=PLAIN AUTH=LOGIN AUTH=OAUTHBEARER AUTH=XOAUTH2 SASL-IR CHILDREN SORT I18NLEVEL=1 UIDPLUS ID MOVE UNSELECT`. Any IMAP client or imapsync/offlineimap works. No rclone backend.
- composes with: Each account is byte-unlimited (message-count-bound), so a second account carries a second allowance. 120,000 messages × the 35 MB send cap = ~4.2 TB per account before the message-count ceiling even binds; raise the count via support and the ceiling moves. Free registration, no paid tier required.
- reliability: Operators state up front that they watch for excess use of the unlimited claim: rules are tuned to catch anyone probing "kde je ta skutečná hranice" (where the real boundary is). Message-count ceiling is enforced silently at fill time.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: "neomezené velikosti" + "120 000 zpráv" + 35/50 MB attach caps, read live 2026-10-21
  - withheld 2026-10-21: probe: openssl s_client -connect imap.seznam.cz:993 -> * OK Seznam IMAP server ready + CAPABILITY incl. AUTH=PLAIN/OAUTHBEARER
  - [2] 2026-10-21: 2008 origin of the unlimited policy, incl. the anti-probing warning
- sources:
  - [1] https://o-seznam.cz/napoveda/email/mohlo-by-se-hodit/limity-schranky/
  - [2] https://blog.seznam.cz/2008/12/spustili-jsme-neomezenou-velikost-emailove/
