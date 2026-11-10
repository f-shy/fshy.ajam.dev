# b2drop

> eudat.eu | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eudat/ | JSON https://fshy.ajam.dev/api/v1/entity/eudat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## B2SHARE (EUDAT)

- `storage/b2share` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic
- needs card no, phone no, ID no, institution no | verified 2026-11-01T21:26:41.690Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://b2share.eudat.eu
- free tier: 20 GB per record, 10 GB per file, and explicitly unlimited records and unlimited files. | unit: GB | metered on: unstated | read on: 2026-11-01 | source: [1]
- per-object cap: 10 GB per file | bytes: 10000000000 | source: [1] | note: not stated
- retention: a permanent service; if it draws to a close, data stays archived and accessible for at least 2 years and is migrated to other suitable repositories | source: [1] | note: permanence is tied to the EUDAT CDI consortium rather than to any one centre; the 2-year floor applies only if the service closes
- egress: Free, unmetered, direct per-file content URLs (GET /api/records/<id>/files/<name>/content). No egress terms or pricing exist; EUDAT is publicly funded. | metered: no
- identity: email | detail: a B2SHARE account is a B2ACCESS account: B2SHARE's own login page offers only "Sign in with B2ACCESS", and B2ACCESS registers either a home-organisation identity over eduGAIN, a social identity, or a local account. The local-account form asks for a user name, a password entered twice and an email address; organisation name, common name and comments are optional. No card and no phone number is asked for.
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 10 GB per file [1]
  - write-gated: review [1]
- limits note: 10 GB per file, 20 GB per record. So 20 TB needs ~1,024 records, which trips EUDAT's 'fair share' clause: 'the uploading of large number of files or creating large number of records is not considered fair use' and they ask you to contact them first. Live rate limit header: x-ratelimit-limit: 500, x-ratelimit-remaining: 499.
- interface detail: rest
- tooling: InvenioRDM-style REST API (live: GET /api/records?size=1 -> 200 with hits/entries and per-file content links); OAI-PMH; DOI minting (10.23728). Python client via plain requests. No rclone backend.
- composes with: 20 GB per record x unlimited records. 50 records = 1 TB; 1,000 records = 20 TB in one account. The docs state outright 'There is no limit to the number of files you can deposit or records you can create'.
- reliability: Rate-limited at 500 requests/window and watched for bulk growth; EUDAT says it 'will increase back-end storage capacity incrementally when necessary', which implies throttling rather than deletion, but the fair-share clause is the trigger for manual review.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'the maximum size for a record is 20 GB; and the maximum size for a file is 10 GB'
  - [2] 2026-10-21: 'There is no limit to the number of files you can deposit or records you can create'; 'fair share' principle
  - [3] 2026-11-01: B2ACCESS accepts a home-organisation identity over eduGAIN, an ORCID or a social identity, so an institutional account is one route among several rather than a requirement | capture: sha256:d28fc4a82c801057a16a6f2908b3b0469dd735243e71b4d78050a1cee92d44db | quote: Supports authentication e.g. via eduGAIN, ORCID and Social Identities
  - [4] 2026-11-01: the local B2ACCESS account is created from a user name, a password twice and an email address, with the organisation name optional and no card or phone field | capture: sha256:2fdfc951d331d3439feaa38bfb047882dd6ad436763efe86844c13fd8f757d83 | quote: - User name - Password (twice). Note that the B2ACCESS site instructs your browser to not remember your username and password. - Email address - Organisation name (optional)
  - [4] 2026-11-01: registration runs through the B2ACCESS account, whose local form asks for an email address, so the identity kind is read rather than defaulted | capture: sha256:2fdfc951d331d3439feaa38bfb047882dd6ad436763efe86844c13fd8f757d83 | quote: The home screen allows users to register with any of three different methods of authentication: organisational ID, social ID and B2ACCESS ID.
  - [1] 2026-11-01: the per-file 10 GB and per-record 20 GB caps are unchanged on the FAQ page | capture: sha256:3140dba8baad84ab7bc265b6e17eab11089f4d983a70fb9e932044895847136d | quote: Currently there is a limit of 10 GB per file and 20 GB per record.
  - [4] 2026-11-01: the local B2ACCESS account, one of the three login routes B2SHARE accepts, is created from a user name, a password entered twice and an email address, with the organisation name optional, so the reachable minimum is an email address | capture: sha256:2fdfc951d331d3439feaa38bfb047882dd6ad436763efe86844c13fd8f757d83 | quote: - User name - Password (twice). Note that the B2ACCESS site instructs your browser to not remember your username and password. - Email address - Organisation name (optional)
  - [5] 2026-11-01: B2SHARE's own login page offers a single route, B2ACCESS, so a B2SHARE account is a B2ACCESS account | capture: sha256:7061f0da09ef511faeb38030f06caf229dd49d6599e3b1d75a8ab90474e2d7ae | quote: Sign in with B2ACCESS
  - [6] 2026-11-01: registration for an upload-capable B2SHARE account is performed on the B2ACCESS site, which is what makes the B2ACCESS form fields the identity cost of this record | capture: sha256:a317d7b7184cd14b154abe9bdae892223fa3d2f348eef55c75e4c0576ff18cf9 | quote: Users must register in order to upload and share data. To register, click on the Login or Register link on the B2SHARE website. You will be referred to the B2ACCESS website where you can register your new user account.
  - [6] 2026-11-01: the three accepted identities are a local B2ACCESS ID, a social ID and an organisational ID, so an institution is one route among several and not a requirement | capture: sha256:a317d7b7184cd14b154abe9bdae892223fa3d2f348eef55c75e4c0576ff18cf9 | quote: To log in, click on the link “Login” on the home page and choose your method of authentication (B2ACCESS ID, social ID or organisational ID).
  - [1] 2026-11-01: the FAQ answers a retention question with a permanence premise and a 2-year floor with migration assistance | capture: sha256:3140dba8baad84ab7bc265b6e17eab11089f4d983a70fb9e932044895847136d | quote: In the unlikely event that the EUDAT CDI B2SHARE service would draw to a close in the future, we guarantee to keep your data archived and accessible for at least 2 years and will assist in the migration of your data to other suitable repositories.
  - [1] 2026-11-01: the permanence claim rests on the consortium behind the service, and the 2-year figure is conditional on the service closing | capture: sha256:3140dba8baad84ab7bc265b6e17eab11089f4d983a70fb9e932044895847136d | quote: EUDAT CDI B2SHARE’s basic premise is to be a permanent service.
  - [1] 2026-11-01: the free tier's own source page was read again on this date and still states the 10 GB per file and 20 GB per record caps | capture: sha256:3140dba8baad84ab7bc265b6e17eab11089f4d983a70fb9e932044895847136d | quote: Currently there is a limit of 10 GB per file and 20 GB per record.
  - [7] 2026-11-01: an anonymous GET of the records API answers 200 and carries a per-caller request allowance of 500 with a Retry-After of 60 seconds | capture: sha256:ec65fb3598ede30c9b0c867f85f99d1dc934c551a4108183ce005eb0481ba749 | quote: x-ratelimit-limit: 500
- sources:
  - [1] https://docs.eudat.eu/b2share/faq/
  - [2] https://eudat.eu/services/userdoc/b2share-faq
  - [3] https://eudat.eu/services/b2access
  - [4] https://eudat.eu/services/userdoc/b2access-usage
  - [5] https://b2share.eudat.eu/login/
  - [6] https://docs.eudat.eu/b2share/users/overview/
  - [7] https://b2share.eudat.eu/api/records?size=1

## b2drop (eudat)

- `storage/b2drop` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://b2drop.eudat.eu/themes/b2drop/apps/core/templates/faq.html
- free tier: none reachable: Free allocation is 20 GB per user ('For the current prototype there is a limit of 20GB per user'). Published documentation describes the service as a prototype. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 20 GB per user ('For the current prototype there is a limit of 20GB per user'). Well and the FAQ still calls the service a prototype.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 20 GB per user ('For the current prototype there is a limit of 20GB per user'). Well and the FAQ still calls the service a prototype.
- sources:
  - [1] https://b2drop.eudat.eu/themes/b2drop/apps/core/templates/faq.html
