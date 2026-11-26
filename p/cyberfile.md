# CyberFile

> cyberfile.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cyberfile/ | JSON https://fshy.ajam.dev/api/v1/entity/cyberfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CyberFile

- `debrid/cyberfile` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file host (freemium, anonymous uploads) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:40.367Z (live) | stale on 2026-12-26
- url https://cyberfile.me/faq
- price unverified: the premium price page was not readable
- free tier: Upload files up-to 10 GB anonymously; free/non-account files kept for 14 days. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The FAQ says uploading and downloading is free for all users; no total storage or download byte allowance is printed.
- per-object cap: Each file you upload must be less than 10 GB in size for free/non accounts or less than 100 GB in size for premium accounts. | bytes: 10737418240 | source: [1] | note: bytes = 10 x 1024^3 for free and non-account uploads; premium is 100 GB.
- retention: Free/non accounts files are kept for 14 days. Premium accounts files are kept for unlimited days. | days: 14 | source: [1]
- egress: No download byte allowance or speed figure is printed on the pages read. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The homepage says 'Upload files up-to 10 GB anonymously' and offers an optional Register to link uploads to an account.
- interface: browser
- limits:
  - per-object-cap: 10 GB free and non-account, 100 GB premium [1]
  - retention-clamped (binding): 14 days free and non-account, unlimited premium [1]
- binding note: 14-day deletion on the free tier bounds how long a file can be fetched; the 10 GB cap is second.
- interface detail: Web upload with a register_non_user route; the vendor documents a REST upload API at https://api.cyberfile.me/api/v2/file/upload using an access_token and account_id from /authorize. The api.cyberfile.me hostname did not resolve from a plain client on 2026-11-25.
- tooling: Browser upload and a documented REST file-upload API requiring an access_token and account_id; the api.cyberfile.me endpoint did not resolve from a plain client on 2026-11-25.
- composes with: 10 GB anonymous files kept 14 days: a hand-off point for one large file, not storage.
- reliability: The /upgrade page answered with the homepage, so no premium price was readable.
- notes: No programmatic path found: Web upload with a register_non_user route; no API page was read.
- evidence note: FAQ and homepage read on the vendor site on 2026-11-03. Premium price unverified: the upgrade page redirected to the homepage.
- evidence:
  - [1] 2026-11-03: the per-file caps are 10 GB free and 100 GB premium | capture: sha256:40cd955ca73498f52719bd7f9f354ded30a8944894ebe3cdb3886e431dc92182 | quote: Each file you upload must be less than 10 GB in size for free/non accounts or less than 100 GB in size for premium accounts.
  - [1] 2026-11-03: free retention is 14 days | capture: sha256:40cd955ca73498f52719bd7f9f354ded30a8944894ebe3cdb3886e431dc92182 | quote: Free/non accounts files are kept for 14 days. Premium accounts files are kept for unlimited days.
  - [2] 2026-11-03: anonymous upload is offered up to 10 GB | capture: sha256:c708a7fd4a02be751ae8b002a025ffc90b3b522eea0b87481105337162cb6af6 | quote: Upload files up-to 10 GB anonymously.
  - [1] 2026-11-25: per-file caps are 10 GB free and 100 GB premium | capture: sha256:40cd955ca73498f52719bd7f9f354ded30a8944894ebe3cdb3886e431dc92182 | quote: Each file you upload must be less than 10 GB in size for free/non accounts or less than 100 GB in size for premium accounts.
  - [1] 2026-11-25: free retention is 14 days | capture: sha256:40cd955ca73498f52719bd7f9f354ded30a8944894ebe3cdb3886e431dc92182 | quote: Free/non accounts files are kept for 14 days. Premium accounts files are kept for unlimited days.
  - [1] 2026-11-25: uploading and downloading are free for all users | capture: sha256:40cd955ca73498f52719bd7f9f354ded30a8944894ebe3cdb3886e431dc92182 | quote: Yes, uploading and downloading is 100% Free for all users.
  - [2] 2026-11-25: anonymous upload is offered up to 10 GB | capture: sha256:c708a7fd4a02be751ae8b002a025ffc90b3b522eea0b87481105337162cb6af6 | quote: Upload files up-to 10 GB anonymously.
  - [3] 2026-11-25: the optional account registers a username only | capture: sha256:0b4ed1c52415841416b76dcfec175931f49cd4cd9188b596e4fc668145de4f9d | quote: IMPORTANT: Because our registration system only works with usernames, there's no way to recover your password in case you forget it.
  - [4] 2026-11-25: a REST file-upload endpoint is documented on the vendor domain | capture: sha256:d57cd6a35c839d961439495b40872b4dd1503e57c3ba05183b0404ae8a105320 | quote: https://api.cyberfile.me/api/v2/file/upload
  - [4] 2026-11-25: the REST upload API uses a token obtained at the /authorize step | capture: sha256:d57cd6a35c839d961439495b40872b4dd1503e57c3ba05183b0404ae8a105320 | quote: - access_token The access token created previously by `/authorize`.
- sources:
  - [1] https://cyberfile.me/faq
  - [2] https://cyberfile.me/
  - [3] https://cyberfile.me/register
  - [4] https://cyberfile.me/api
