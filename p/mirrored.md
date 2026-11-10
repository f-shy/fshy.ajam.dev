# Mirrorcreator

> mirrored.to | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mirrored/ | JSON https://fshy.ajam.dev/api/v1/entity/mirrored.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mirrorcreator (mirrored.to)

- `debrid/mirrored-to` | qualifies | evidence documented | binding none | category multi-host mirror uploader | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://www.mirrored.to/
- price USD 0, plus the destination host's own cost
- free tier: Upload once and the file is mirrored to the hosts the user selects, yielding one aggregate link; 'Over 40 hosts to choose from'. | unit: objects | metered on: uploaded-bytes | read on: 2026-10-23 | source: [1] | note: No free allowance is printed; the free product is the service itself.
- per-object cap: not stated on the page read | source: [1]
- retention: not applicable: the copies live on the destination hosts, under each host's own retention | source: [1]
- egress: Downloads come from the destination hosts, so their limits apply, not Mirrorcreator's. The service itself publishes no byte allowance and no price. | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: Uploads can be anonymous where a destination allows it, or made into the user's own accounts ('if the hosting sites support anonymous file uploads, you can even upload files without the need for registration'). No Mirrorcreator account was required on the page read.
- interface: unknown
- limits:
  - pull-count: unstated; the service bounds a run by the number of selected destinations [1]
- limits note: Uploading into the user's own accounts means the destination host's quota, not Mirrorcreator's, is what runs out first. Anonymous destinations avoid that at the cost of the files being outside the account's control.
- binding note: Mirrorcreator stores nothing itself, so no byte counter of its own can bind at 1 TiB. The constraint moves to whichever destination host is selected.
- interface detail: Web form. The site names Google Drive, Mediafire, GoFile, Yandex Disk among the 40+ destinations, and states 'The files you upload are stored on your own accounts on hosting sites'.
- tooling: Browser only as read. No API found on the page; a wrapper would have to drive the form per host.
- composes with: The inverse of a debrid: instead of pulling one link from many hosts, it pushes one file to many hosts.
- reliability: An aggregate link is only as alive as the destinations behind it; when one host removes a file the aggregate page keeps listing a dead mirror until somebody clicks it.
- notes: The domain is mirrored.to but the site brands itself Mirrorcreator, the older name; MirrorAce is a separate site on the same idea and is recorded dead.
- evidence note: The 40+ host claim, the own-account behaviour and the aggregate-link behaviour are read from the vendor page. Nothing was uploaded.
- extras:
  - hosts_claimed: 40+
  - brand: Mirrorcreator
- evidence:
  - [1] 2026-10-23: 'Over 40 hosts to choose from', 'The files you upload are stored on your own accounts on hosting sites', and the example destinations Google Drive, Mediafire, GoFile, Yandex Disk
- sources:
  - [1] https://www.mirrored.to/
