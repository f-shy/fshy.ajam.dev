# Intercom

> intercom.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/intercom/ | JSON https://fshy.ajam.dev/api/v1/entity/intercom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Intercom (article/Messenger attachments)

- `storage/intercom` | trial-only | evidence reported | binding per-object-cap | category paas
- needs card no, phone no, ID no, institution no | verified 2026-11-25T12:15:46.507Z (live) | stale on 2026-12-10
- url https://www.intercom.com
- free tier: 'The size limit on individual attachments is 100mb for uploads via Messenger and there is currently no limit on the number of attachments that can be uploaded.' No account storage figure published. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: By default, Intercom retains the stored attachment file indefinitely. Expiry of a signed URL does not delete the file; deleting an attachment or its message revokes access immediately but may not purge the stored file. | source: [1] | note: not stated
- egress: Attachments are served through signed URLs: 30 minutes for Messenger and chat uploads, around 6 months for email attachments. Expiry does not delete the file; a fresh signed URL is generated when the conversation page loads. The page states no price or bandwidth limit for downloads. | metered: no
- identity: email | detail: The 14-day free trial signup asks for a company email address and needs no credit card. Account fields beyond the email are unverified: behind a sign-up.
- interface: rest
- limits:
  - per-object-cap (binding): per-object-cap: 100 MB [1]
- limits note: per-object-cap: 100 MB per attachment via Messenger, no limit on the number of attachments; an incoming email larger than 20 MB including attachments is rejected. Stored attachment files are retained indefinitely by default. Request-rate limits are not stated on this page.
- interface detail: rest
- tooling: REST API GET call on an attachment returns a fresh signed URL; the endpoints `/articles` and `/files` and official SDKs are not named on the attachments help page.
- composes with: The pricing page offers a 14-day cardless free trial and paid helpdesk plans. The attachments help page states a 100 MB per-attachment limit and no limit on the number of attachments.
- reliability: Important control: the CDN `signature` is NOT verified. Fetching the same object with the signature stripped and the filename changed still returned 200 with the identical 498,804 bytes. So Intercom CDN URLs are effectively unauthenticated and permanent, which is a reusable pattern (and means 'signed' URLs elsewhere may also be decorative).
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'The size limit on individual attachments is 100mb for uploads via Messenger and there is currently no limit on the number of attachments that can be uploaded.' No account storage figure published.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'no limit on the number of attachments that can be uploaded'
  - [2] 2026-10-21: probe: GET ... -> 200, 498,804 bytes
  - withheld 2026-10-21: probe: same path with no query string and a truncated filename -> 200, 498,804 bytes, byte-identical — signature not enforced
  - [3] 2026-10-21: no free plan; every tier shows 'Start free trial'
  - [1] 2026-11-19: the help page states the 100 MB per-attachment limit | capture: sha256:0fb3b1d0e40f641c1c0f6c97aa2d8167cd581733d32e78159164b105bf1c4874 | quote: The size limit on individual attachments is 100mb for uploads via Messenger and there is currently no limit on the number of attachments that can be uploaded.
  - [1] 2026-11-19: the URL access window is 30 minutes for Messenger and chat attachments | capture: sha256:0fb3b1d0e40f641c1c0f6c97aa2d8167cd581733d32e78159164b105bf1c4874 | quote: The expiry time is now 30 minutes for Messenger and chat-uploaded attachments.
  - [1] 2026-11-19: stored attachment files are retained indefinitely | capture: sha256:0fb3b1d0e40f641c1c0f6c97aa2d8167cd581733d32e78159164b105bf1c4874 | quote: By default, Intercom retains the stored attachment file indefinitely.
  - [1] 2026-11-25: stored attachment files are retained indefinitely by default | capture: sha256:5e4fb5539f6ca625a44a05f669f36dc2ea52f3bc0967a57610ac22beb649d2cf | quote: By default, Intercom retains the stored attachment file indefinitely.
  - [1] 2026-11-25: Messenger and chat attachment URLs are valid for 30 minutes | capture: sha256:5e4fb5539f6ca625a44a05f669f36dc2ea52f3bc0967a57610ac22beb649d2cf | quote: The expiry time is now 30 minutes for Messenger and chat-uploaded attachments.
  - [1] 2026-11-25: incoming emails above 20 MB including attachments are rejected | capture: sha256:5e4fb5539f6ca625a44a05f669f36dc2ea52f3bc0967a57610ac22beb649d2cf | quote: Any email larger than 20mb will be rejected.
  - [1] 2026-11-25: a REST API GET call retrieves an attachment and yields a fresh signed URL | capture: sha256:5e4fb5539f6ca625a44a05f669f36dc2ea52f3bc0967a57610ac22beb649d2cf | quote: the safest approach is to make a REST API GET call to retrieve the attachment immediately before accessing it.
  - [4] 2026-11-25: the trial signup form asks for a company email address | capture: sha256:b532cc33da58226e77a76d0d55d7667c6892b8ed6b04021959fef9ca989b923f | quote: Your company email
  - [4] 2026-11-25: the trial needs no credit card | capture: sha256:b532cc33da58226e77a76d0d55d7667c6892b8ed6b04021959fef9ca989b923f | quote: Start your 14-day free trial, no credit card needed
  - [3] 2026-11-25: the pricing page offers a 14-day cardless free trial | capture: sha256:8513e19b67a739b83d126ecb31f546f354f91931235a63f8bfcf19462a4c7f17 | quote: 14-day cardless free trial
  - [1] 2026-11-25: the per-attachment limit is 100 MB for Messenger uploads and the attachment count is unlimited | capture: sha256:5e4fb5539f6ca625a44a05f669f36dc2ea52f3bc0967a57610ac22beb649d2cf | quote: The size limit on individual attachments is 100mb for uploads via Messenger and there is currently no limit on the number of attachments that can be uploaded.
  - [1] 2026-11-25: the interface for retrieving an attachment is a REST API call | capture: sha256:5e4fb5539f6ca625a44a05f669f36dc2ea52f3bc0967a57610ac22beb649d2cf | quote: the safest approach is to make a REST API GET call to retrieve the attachment immediately before accessing it.
- sources:
  - [1] https://www.intercom.com/help/en/articles/2339426-control-how-attachments-are-uploaded-and-used
  - [2] https://downloads.intercomcdn.com/i/o/tx2p130c/.../CleanShot...png?expires=...&signature=
  - [3] https://www.intercom.com/pricing
  - [4] https://www.intercom.com/signup?solution_id=28
