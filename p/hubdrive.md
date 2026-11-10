# HubDrive

> hubdrive.bar | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hubdrive/ | JSON https://fshy.ajam.dev/api/v1/entity/hubdrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HubDrive

- `debrid/hubdrive` | qualifies-with-caveat | evidence documented | binding none | category Google Drive link shortener and file manager (Indian DDL ecosystem) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:34:43.873Z (live) | stale on 2026-11-23
- url https://hubdrive.bar/
- price USD 0
- free tier: "HubDrive is a Google Drive File Manager." Sign-up is open and no price, allowance or tier is printed on the page read. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Only the sign-in shell was reachable without an account; the numbers, if any, sit behind it.
- per-object cap: Not stated on the public page. | source: [1]
- retention: Not stated; the object lives in the user's own Drive. | source: [1]
- egress: Shortened Google Drive links. HubDrive serves a redirect, not the bytes, so there is no allowance to state. | metered: no | source: [1]
- identity: email | detail: An account is required to use the service ('Click the Sign In button'; a /sign route exists). Whether registration is email or Google OAuth was not established because the form was not opened.
- interface: unknown
- limits:
  - request-rate: unstated [1]
- limits note: Nothing measurable is published. The page is a sign-in shell, and the only figure anywhere in the family's copy is DriveSeed's 'UNLIMITED'.
- binding note: HubDrive transfers no bytes: it stores a redirect. The constraint lives on Google Drive, one hop further down, so nothing on this record binds at 1 TiB a month.
- interface detail: Web only as read: 'Click the Sign In button to begin your journey with us', with a separate /sign route. The page title describes its function: 'G-Drive File Sharing Site ! Shorten your Google Drive Links.'
- tooling: Third-party bypass lists treat hubdrive as one hostname in the appdrive lookalike family (drivehub.in, driveapp.in, driveace.in and siblings), so scraping and bypassing are done by shared scripts rather than an API.
- composes with: The link-shortening layer of the same chain: an index site posts a HubDrive short link, HubDrive redirects to the Drive file, and the file is often simultaneously wrapped by HubCloud or DriveSeed. Its value to the chain is that the short link survives a Drive id swap.
- reliability: The hostname moves: hubdrive.space redirects to hubdrive.bar, and the .space domain is what most index sites still print. Any client that stores the short host rather than the resolved Drive id inherits the move.
- notes: Weakest record among debrid providers and marked as such: the public page carries no number, so it exists to stop the subsequent audit opening it again and to map the chain, not to price anything.
- evidence note: Reached and read, but only the public shell. The rung is documented for the existence and function, and the record says plainly that the quota, if any, was not seen.
- extras:
  - hosts_seen: hubdrive.bar (live), hubdrive.space (redirects to .bar)
  - family: appdrive.in, driveapp.in, drivehub.in, gdflix.pro, drivesharer.in, drivebit.in, drivelinks.in, driveace.in, drivepro.in
- evidence:
  - [1] 2026-10-23: live sign-in page titled 'G-Drive File Sharing Site ! Shorten your Google Drive Links.' with the text 'HubDrive is a Google Drive File Manager' and a /sign route
  - [2] 2026-10-23: hubdrive.space redirects to hubdrive.bar, so the older hostname in index posts is not dead
- sources:
  - [1] https://hubdrive.bar/
  - [2] https://hubdrive.space/
