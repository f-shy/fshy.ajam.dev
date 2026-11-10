# upload.am

> upload.am | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upload/ | JSON https://fshy.ajam.dev/api/v1/entity/upload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## upload.am

- `debrid/upload-am` | qualifies-with-caveat | evidence documented | binding volume-quota | category free cloud storage with server-side remote upload from a URL | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://upload.am/en/features/remote-upload-from-url
- price USD 0
- free tier: 'On the Free plan that means up to 25 GB of storage and 5 GB per file.' Remote upload 'is included on the Free plan', but 'An upload.am account' is required. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: The same page's feature blurb advertises '25 GB free forever' and 'No ads on download pages'.
- per-object cap: 5 GB per file on the Free plan ('a file within your plan's size limit. On the Free plan that means up to 25 GB of storage and 5 GB per file'). | bytes: 5368709120 | source: [1]
- retention: unverified: the page describes expiry controls for links the user creates, but no default retention period for stored files. | source: [1]
- egress: No traffic allowance stated; files are served from the account's links with optional password, download limit and expiry. | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: 'An upload.am account. Remote upload lives in the cabinet, so register for free if you have not already.' Registration was not attempted, so the fields are unverified beyond an account being required.
- interface: unknown
- limits:
  - volume-quota (binding): 25 GB stored on the Free plan [1]
  - per-object-cap: 5 GB per file on the Free plan [1]
  - write-gated: an account is required; executable and script types are blocked [1]
- limits note: The fetch only works on a direct link that needs no login on the source site; a host page with a download button is refused before the transfer starts.
- binding note: At 1 TiB/month the 25 GB storage allowance binds first and hard: the 5 GB per-file cap is generous relative to it, and deleting after download does not change the fact that the account holds 25 GB at a time.
- interface detail: Web cabinet only: paste an http(s) link, the server fetches it in the background, and the file appears in a folder where it can be previewed, renamed, shared or versioned. Private-range and credential-bearing URLs are refused.
- tooling: Browser. No API is documented on the feature pages read, so a wrapper drives the cabinet.
- composes with: It is the storage end of a relay: pull a direct link into a durable account and share it with controls the original host lacks. 25 GB fits a small working set, not the hot tier at 10 TiB.
- reliability: Remote fetch is asynchronous and failures arrive by email, so a wrapper cannot tell success from a silent queue. The service refuses private-network URLs and executable types, which will reject some legitimate archives.
- notes: The clearest published free URL-pull-to-storage allowance found: 25 GB stored, 5 GB per file, account required, direct links only. Useful as a staging buffer, not as the 10 TiB tier.
- evidence note: The plan limits and the remote-upload mechanics are quoted from the vendor page; no fetch was executed, which a measured rung needs.
- extras:
  - free_storage_gb: 25
  - free_max_file_gb: 5
  - account_required: yes
- evidence:
  - [1] 2026-10-23: 'On the Free plan that means up to 25 GB of storage and 5 GB per file'; remote upload included on Free; account required; direct-link-only and private-address refusal
  - probe:https://upload.am/ 2026-10-23: HTTP 200, 159846 bytes, sha256 35bba2652a616824..., no challenge
- sources:
  - [1] https://upload.am/en/features/remote-upload-from-url
