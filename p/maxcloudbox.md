# MaxCloudBox

> maxcloudbox.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/maxcloudbox/ | JSON https://fshy.ajam.dev/api/v1/entity/maxcloudbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MaxCloudBox

- `debrid/maxcloudbox` | paid-only | evidence documented | binding volume-quota | category cloud torrent seedbox with cloud-host import (hosted) | tier Trial (3 days)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://maxcloudbox.com/
- free tier: No free allowance stated; account creation is advertised as free ('Create an account It's Free!') and the plans start at a 3-day trial for $1.00. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: no per-file cap stated; storage is 20 GB on the 3-day trial and 100 GB on the 30-day and longer plans | source: [1]
- retention: Seedbox keeps a torrent until a 1:10 ratio or 10 days. | days: 10 | source: [1]
- egress: Unlimited downloads and gigabit speeds are stated for every plan; no volume cap stated. | metered: no | free allowance: none stated | source: [1]
- identity: email | detail: Registration page: the new account password is sent to the email address entered; Google sign-in is offered.
- interface: webdav
- limits:
  - volume-quota (binding): private cloud storage 20 GB on the 3-day trial, 100 GB (plus extra) on longer plans [1]
- binding note: Storage size is the only metered figure stated; downloads are stated as unlimited.
- interface detail: WebDAV access, remote downloader, remote file uploader, FTP and cloud-host connectors (Dropbox, Box, Mega, pCloud, 1fichier, Google Drive, OneDrive) are listed.
- tooling: Browser and WebDAV clients.
- composes with: Plans: 3 days $1.00, 10 days $3.68, 30 days $8.68, 90 days $24.68, 180 days $48.68.
- reliability: No outage observed on the day read.
- notes: Closer to a seedbox with a cloud-torrent front end than a multi-hoster.
- evidence note: First-party home page and registration page.
- evidence:
  - [1] 2026-11-03: the cheapest plan is $1.00 for 3 days | capture: sha256:f0c009adae111c6ee1fc1fa5b5e9eeae295774344c88297fd9daefb850f0c900 | quote: ## $1.00 Per 3 days
  - [1] 2026-11-03: the 30-day plan is $8.68 | capture: sha256:f0c009adae111c6ee1fc1fa5b5e9eeae295774344c88297fd9daefb850f0c900 | quote: ## $8.68 Per 30 days
  - [1] 2026-11-03: longer plans carry 100 GB of storage | capture: sha256:f0c009adae111c6ee1fc1fa5b5e9eeae295774344c88297fd9daefb850f0c900 | quote: - 100GB NVMe SSD Powered Private Cloud Storage
  - [1] 2026-11-03: seeding runs to a 1:10 ratio or 10 days | capture: sha256:f0c009adae111c6ee1fc1fa5b5e9eeae295774344c88297fd9daefb850f0c900 | quote: - Seedbox (seed torrent until 1:10 ratio or 10 days)
  - [1] 2026-11-03: WebDAV access is included | capture: sha256:f0c009adae111c6ee1fc1fa5b5e9eeae295774344c88297fd9daefb850f0c900 | quote: - WebDAV Access
  - [2] 2026-11-03: registration sends the password to the email address | capture: sha256:3bc738174ca82c760a46b4d0f667a53c71ce156823f00d86b8644fafd31b5002 | quote: Your new account password will be sent to your email address.
- sources:
  - [1] https://maxcloudbox.com/
  - [2] https://maxcloudbox.com/register
