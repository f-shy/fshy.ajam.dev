# Turbobit

> turbobit.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/turbobit/ | JSON https://fshy.ajam.dev/api/v1/entity/turbobit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Turbobit

- `storage/turbobit` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:34.760Z (live) | stale on 2026-11-25
- url https://turbobit.net
- free tier: The total volume and number of your files are unlimited | unit: unlimited | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: unverified: https://turbobit.net/?site_version=normal states no per-file size cap | source: [1] | note: not stated
- retention: unverified: https://turbobit.net/faq states 'storage time expiration' as a removal reason without a duration | source: [1] | note: not stated
- egress: If you are a free user, you may download about 5 Gb a day if downloading continually, but note that free account speed is limited. | metered: no | free allowance: about 5 Gb a day
- identity: email | detail: You can sign up fast at https://turbobit.net/reg — you will need to enter a real email address, to make up a password for your account, and to agree to the rules of our service.
- interface: rest, ftp, rclone
- limits:
  - per-ip-shaping: about 5 Gb a day [1]
  - per-ip-shaping: approximately 55-60 Kbytes/s [1]
  - per-object-cap (binding): unverified: no per-file size cap stated on https://turbobit.net/?site_version=normal [1]
- limits note: All users who have Turbo Access may enjoy the maximum download speed possible and download up to 40 Gb a day, 600 Gb per month.
- interface detail: rest
- tooling: Turbobit Uploader desktop app, FTP upload, and third-party rclone/JDownloader support; no first-party public REST API documented.
- composes with: Unlimited total per account is the headline; with email-only registration the chain is N accounts. The 40 GB/day cap is per download identity, so serving volume scales with IPs, not accounts.
- reliability: Free-tier serving is throttled to dial-up speeds and gated behind a human-verification step and a queue, so it works as storage but not as a fetch origin. Dyna mic Download Splitting means the previous file's size sets your next wait.
- notes: the same as the free tier
- evidence note: the turbobit.net FAQ states the free download speed is approximately 55-60 Kbytes/s
- evidence:
  - [1] 2026-10-21: 'Store as many files as you want — The total volume and number of your files are unlimited'
  - [2] 2026-10-21: 'If you are a free user, you may download about 5 Gb a day'; Turbo '40 Gb a day, 600 Gb per month'; 'storage time expiration' is a deletion reason
  - [3] 2026-10-21: plan table 100 GB trial / 600 GB / 3600 GB / 7200 GB / 14400 GB bandwidth blocks
  - [1] 2026-11-09: the home page states the total volume and number of files are unlimited | capture: sha256:db4cbe3a0a1ff4b104de064fbd83135426105daa4130bd2fd81a88dc8283e839 | quote: The total volume and number of your files are unlimited
  - [2] 2026-11-09: the FAQ lists storage time expiration as a removal reason | capture: sha256:382a522cd86c068299d632f7fdd3c7e01a36b51adb36bea159929685021095c1 | quote: storage time expiration
  - [2] 2026-11-09: the FAQ states a free user downloads about 5 Gb a day with limited speed | capture: sha256:382a522cd86c068299d632f7fdd3c7e01a36b51adb36bea159929685021095c1 | quote: If you are a free user, you may download about 5 Gb a day if downloading continually, but note that free account speed is limited.
  - [2] 2026-11-09: the FAQ states a real email address is needed to sign up | capture: sha256:382a522cd86c068299d632f7fdd3c7e01a36b51adb36bea159929685021095c1 | quote: You can sign up fast at https://turbobit.net/reg — you will need to enter a real email address, to make up a password for your account, and to agree to the rules of our service.
  - [2] 2026-11-09: the FAQ states the free download speed is 55-60 Kbytes/s | capture: sha256:382a522cd86c068299d632f7fdd3c7e01a36b51adb36bea159929685021095c1 | quote: The file download speed in free mode is approximately 55-60 Kbytes/s.
  - [2] 2026-11-09: the FAQ states Turbo downloads up to 40 Gb a day and 600 Gb a month | capture: sha256:382a522cd86c068299d632f7fdd3c7e01a36b51adb36bea159929685021095c1 | quote: All users who have Turbo Access may enjoy the maximum download speed possible and download up to 40 Gb a day, 600 Gb per month.
- sources:
  - [1] https://turbobit.net/?site_version=normal
  - [2] https://turbobit.net/faq
  - [3] https://turbobit.net/premium
