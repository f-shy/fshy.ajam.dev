# Ctfile

> ctfile.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ctfile/ | JSON https://fshy.ajam.dev/api/v1/entity/ctfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ctfile (城通网盘, ctfile.com)

- `netdisk-pan/ctfile` | qualifies-with-caveat | evidence documented | binding retention-clamped | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-09T13:21:23.326Z (live) | stale on 2026-12-01
- url https://www.ctfile.com/
- free tier: 5 TB of shared space on the free tier, 20 GB per file, and no upload speed cap | unit: TB | metered on: stored-bytes | read on: 2026-10-22 | source: [1] | note: the landing page and the register page agree on 5 TB and 20 GB; the help centre adds 20 GB free and 30 GB for Standard members
- per-object cap: 20 GB per file on the free tier; 30 GB on Standard | bytes: 20000000000 | source: [2] | note: terms section 3.2.8 states the same two numbers as a default
- retention: files are deleted after 30 consecutive days without a sign-in on a free account, or 365 days on a paid account | days: 30 | source: [3] | note: terms section 3.2.5, quoted; the landing page states it as 'log in once a month to renew'
- egress: downloads are metered by tier rather than by byte: free accounts have no published volume cap but a slow channel, Standard is stated at 'up to 5MB/sec', and Super removes the limit; no per-GB egress price is published | metered: no | source: [4]
- identity: email | detail: the email path asks for an email address, a password and a 5-character image verification code, then acceptance of the terms; 'Sign up with phone instead' is the alternative; no card, no ID document and no PRC phone number are asked for on the email path
- interface: rest, webdav, cli
- limits:
  - retention-clamped (binding): 30 consecutive days without a sign-in deletes files on a free account [3]
  - per-object-cap: 20 GB per file on the free tier [3]
  - request-rate: 200,000 files and 10,000 folders per account; 10,000 file uploads per day; 5 concurrent download and 5 concurrent upload threads [3]
- binding note: The identity gate is the one that usually closes a Chinese pan, and this one is open; what binds is the 30-day inactivity clock, which makes it a working set and not an archive.
- tooling: first-party desktop client and a WebDAV endpoint; the free tier advertises WebDAV and the Super tier advertises 'WebDAV batch download'; the nfd-parser project ships a ct driver
- composes with: the only Chinese pan in this survey that a foreigner can self-register for with an email address alone, so it is the one that can sit under a self-hosted bridge without a +86 number
- reliability: Over-quota triggers deletion of the excess without prior notice, and the inactivity clock deletes a free account's files at 30 days; a monthly sign-in cron keeps it alive and nothing else does.
- notes: 5 TB free, 20 GB per file, email-only registration, WebDAV advertised. The 30-day inactivity deletion is the number that decides how it can be used: a monthly cron job keeps it, and nothing else does. Terms section 3.2.7 also caps the account at 200,000 files, which at 20 GB per file is a 4 PB nominal ceiling and therefore not the constraint.
- extras:
  - access_mode: registration-gated
  - registration: email + password + human-verification step
  - webdav_tier: advertised on the free tier and on Super as batch download
  - inactivity_days_free: 30
  - inactivity_days_paid: 365
  - file_count_cap: 200000
  - daily_upload_cap: 10000
- evidence:
  - [1] 2026-10-22: the signup form offers Email and Password with a human-verification step, and states 'Sign up with phone instead'; the page advertises 5TB free, 20GB per file, and 'Direct link sharing, WebDAV and online media playback'
  - [2] 2026-10-22: 'Free users: Max 20GB per file / Standard members: Max 30GB per file', and the registration steps are email, password, email verification with no identity document
  - [3] 2026-10-22: section 3.2.5 deletes stored files after 30 consecutive days without sign-in on a free account; 3.2.7 caps an account at 200,000 files and 10,000 uploads per day; 3.2.8 caps a file at 20GB; 3.2.9 caps 5 concurrent download and 5 concurrent upload threads
  - [4] 2026-10-22: 'Free users enjoy 5TB shared space, upgrade to membership for up to 70TB'; Standard CNY 28/month or CNY 98/year; Super CNY 38/month or CNY 258/year with 10TB shared and 2TB private
  - [4] 2026-11-03: free users get 5 TB of shared space | capture: sha256:38b10c9fd71081c03698c44f19e126ce1cc8c3607f248023342b02b33f35c7e9 | quote: Free users enjoy 5TB shared space, upgrade to membership for up to 70TB storage
  - [2] 2026-11-03: the per-file cap on a free account is 20 GB | capture: sha256:f3b0bbf1f5f3425d6674b90327807706a4485a1879abd2257f4928e5fb3a06ee | quote: Free users: Max 20GB per file
  - [3] 2026-11-03: long-term inactivity of about 30 days on a free account clears its files | capture: sha256:83bac7a60ad35b548b75a5c4a61811d2dc755d0f6af371186a1aebfde97c25f6 | quote: (~30 days for free users; ~365 days for paid members)
  - [1] 2026-11-03: the registration form takes an email and password with a phone alternative | capture: sha256:166b980491e5ddde53a7620213cb1afa54ac79e6df6e591f5b4ca756c83cdd77 | quote: Sign up with phone instead
  - [5] 2026-11-09: the current email sign-up form asks for a 5-character verification code; the same page shows the email, password and terms fields and the phone alternative | capture: sha256:aa085e0c36b24d6335be4ab545c21e0c24cf1c1a16dd330beb35011c6fe98046 | quote: input_code:"Verification Code",input_code_placeholder:"Enter code",input_code_msg:"Please enter the 5-character verification code."
  - [6] 2026-11-09: the email registration request carries email, password and a captcha only; no phone, card or identity-document field | capture: sha256:38f0b1101ee5d330dc44e3fdbe2ad4ea56454ab52524a984b3e926d4a9d07344 | quote: body:JSON.stringify({email:i.email,password:i.password,captcha:i.code,captcha_id:c,invite_code:G,ref:f})
  - [5] 2026-11-09: the free plan is 5 TB of shared space, capped at 20 GB per file and renewed by signing in once a month; the same page states no upload speed limit | capture: sha256:aa085e0c36b24d6335be4ab545c21e0c24cf1c1a16dd330beb35011c6fe98046 | quote: plan_free_feature1:"5TB Shared Space",plan_free_feature2:"Max 20GB per file",plan_free_feature3:"Login once a month to renew"
  - [5] 2026-11-09: registration yields 5 TB of shared space, above 500 GiB; the email-only sign-up opens the identity door, and the shared-space and monthly sign-in conditions make the verdict qualifies-with-caveat | capture: sha256:aa085e0c36b24d6335be4ab545c21e0c24cf1c1a16dd330beb35011c6fe98046 | quote: section_2_step_4_desc:"After successful registration, you'll get 5TB of free shared space and can start uploading files immediately"
  - [7] 2026-11-09: a free account's stored files are deleted after 30 consecutive days without sign-in; paid accounts get 365 days | capture: sha256:85b24400ecfd038bf013e624035b7f6475dc22362b638cbd2e15ca4519998261 | quote: delete stored files after 30 consecutive days without sign-in for a free account, or 365 consecutive days for a paid member
  - [7] 2026-11-09: the free 5 TB is shared space, not private storage or long-term private archiving | capture: sha256:85b24400ecfd038bf013e624035b7f6475dc22362b638cbd2e15ca4519998261 | quote: Shared space is a functional area for you to share, transfer or display content to others, rather than private storage or long-term private archiving.
  - [5] 2026-11-09: the help page states registration takes an email address, a password and agreement to the user agreement | capture: sha256:aa085e0c36b24d6335be4ab545c21e0c24cf1c1a16dd330beb35011c6fe98046 | quote: section_2_step_2_desc:"Enter your email address, set a password, and agree to the user agreement"
  - [5] 2026-11-09: registration itself grants 5 TB of shared space at no charge | capture: sha256:aa085e0c36b24d6335be4ab545c21e0c24cf1c1a16dd330beb35011c6fe98046 | quote: section_2_tip_text:"Get 5TB shared space upon registration, completely free!"
- sources:
  - [1] https://www.ctfile.com/register
  - [2] https://www.ctfile.com/help
  - [3] https://www.ctfile.com/terms
  - [4] https://www.ctfile.com/
  - [5] https://www.ctfile.com/assets/index-DqUjQ9XK.js
  - [6] https://www.ctfile.com/assets/account-pages-7k0OlWK8.js
  - [7] https://www.ctfile.com/assets/legal-pages-D5nM9Fh6.js
