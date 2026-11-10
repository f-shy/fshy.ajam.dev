# Bestfile

> bestfile.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bestfile/ | JSON https://fshy.ajam.dev/api/v1/entity/bestfile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bestfile

- `debrid/bestfile` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (free, ad-supported) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://bestfile.io/
- price none: no paid tier
- free tier: Unlimited free storage advertised; files up to 2.00 GB without an account, 5.00 GB for registered users; available 25 days, unlimited for registered users. | unit: unlimited | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The FAQ says files stay while accessed at least once every 50 days; the upload form shows 25 days for unregistered files.
- per-object cap: Max File Size: 2.00 GB | 5.00 GB For Registered Users. | bytes: 2147483648 | source: [1] | note: bytes = 2 x 1024^3 for an unregistered upload; the FAQ states 5GB per file.
- retention: Files available for: 25 days | Unlimited For Registered Users. | days: 25 | source: [1] | note: Registered files stay while accessed at least once every 50 days.
- egress: Downloads at full speed with no speed limit; no byte cap is printed. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The upload form lists separate limits for unregistered and registered users, so upload works without registering.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB unregistered, 5 GB registered [1]
  - retention-clamped: 25 days unregistered; registered files removed after 50 days without access [1]
- binding note: 2 GB per unregistered file is the first limit a large pull meets.
- interface detail: Web upload with up to 5 files at once; the FAQ states BestFile does not support FTP. No API page read.
- tooling: Browser only as read.
- composes with: Free with no paid tier to buy more, so the caps are the ceiling.
- reliability: The service states it asks for no subscription, so there is no paid tier that raises the caps.
- evidence note: Homepage FAQ and upload form read on 2026-11-03. The FAQ states 5GB per file while the form states 2.00 GB unregistered and 5.00 GB registered.
- evidence:
  - [1] 2026-11-03: the per-file caps are 2 GB unregistered and 5 GB registered | capture: sha256:bd4825c033417ad026a30aeda39233c38afe1ccde5c337b8af1e27c90a2b6dbf | quote: Max File Size: 2.00 GB | 5.00 GB For Registered Users.
  - [1] 2026-11-03: unregistered retention is 25 days | capture: sha256:bd4825c033417ad026a30aeda39233c38afe1ccde5c337b8af1e27c90a2b6dbf | quote: Files available for: 25 days | Unlimited For Registered Users.
  - [1] 2026-11-03: no paid tier is offered | capture: sha256:bd4825c033417ad026a30aeda39233c38afe1ccde5c337b8af1e27c90a2b6dbf | quote: Yes! Our services are free forever and we will not ask you to pay any subscription.
- sources:
  - [1] https://bestfile.io/
