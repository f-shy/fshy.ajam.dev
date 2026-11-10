# megatools

> megous.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/megous/ | JSON https://fshy.ajam.dev/api/v1/entity/megous.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## megatools

- `debrid/megatools` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding per-ip-shaping | category MEGA command-line client (public-link downloader and account client) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://megatools.megous.com/
- price USD 0
- free tier: 'Megatools is a collection of programs for accessing Mega service from a command line of your desktop or server.' Free software; the command set includes 'dl Download file from a "public" Mega link (doesn't require login)'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The project site megatools.megous.com answered HTTP 503 'We'll be back soon' (scheduled maintenance) today, so the man page was read from a mirror of the same document.
- per-object cap: not applicable: MEGA states it has no file size limit; the local disk is the cap. | source: [2]
- retention: not applicable: writes to local disk; no service-side storage. | source: [1]
- egress: MEGA's IP-based six-hour transfer window applies to the machine running megatools; there is no megatools-side quota or proxy rotation. | metered: yes | free allowance: dynamic, IP-based, six-hour window | source: [3]
- identity: anonymous | detail: 'megatools dl' takes a public link and needs no login. Account subcommands exist for private files but are not required for the public-link path.
- interface: cli
- limits:
  - per-ip-shaping (binding): MEGA counts downloads from the IP over six hours; no fixed number published [3]
- limits note: MEGA's help page lists third-party tools as a hazard: 'these tools can't detect your quota', and using them with account credentials can lock the account. Public-link download avoids the credential risk.
- binding note: The six-hour per-IP window is the only quota in the path; megatools does not rotate proxies, so it is met directly and the reset must be waited for.
- interface detail: Subcommands: df, ls, get, put, copy, rm, mkdir, export, reg, test and 'dl' for public links. Streaming is supported with '--path -', so a wrapper can pipe a public link into another process without touching disk.
- tooling: Native builds for Windows and Linux, plus source. A shell wrapper is enough; nothing needs a GUI or a display.
- composes with: The streaming flag makes it the cheapest MEGA leg for a pipeline that must not stage the file on local disk: piped output can go straight into an uploader or a hash check.
- reliability: The project site was 503 today and the man page had to be read from a mirror; the tool is maintained but the distribution site is not always up. Over-quota downloads fail mid-transfer and resume after the window resets.
- notes: Command-line suite providing native streaming access to MEGA links without requiring a browser.
- evidence note: Man page and MEGA quota page read; the project site's 503 is measured. Running 'megatools dl' against a real link would raise this to measured.
- self hosted: yes
- extras:
  - public_link_command: megatools dl <link>
  - streaming_command: megatools get --path - <remotefile>
  - site_status_today: 503 maintenance
- evidence:
  - [1] 2026-10-23: 'dl Download file from a "public" Mega link (doesn't require login)'; streaming with 'megatools get --path -'
  - [4] 2026-10-23: the project site is down for maintenance: HTTP 503, 17 words, 'This site is currently undergoing scheduled maintenance.'
  - [3] 2026-10-23: per-IP six-hour download limit for free and anonymous users; no fixed limit
  - [5] 2026-10-23: third-party tools 'can't detect your quota' and may cause account lock-ups when given credentials
- sources:
  - [1] https://xff.cz/megatools/man/megatools.html
  - [2] https://help.mega.io/files-folders/transfers/no-file-size-limits
  - [3] https://help.mega.io/plans-storage/space-storage/transfer-quota
  - [4] https://megatools.megous.com/
  - [5] https://help.mega.io/files-folders/transfers/download-files-folders
