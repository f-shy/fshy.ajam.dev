# Webdock

> linkedin.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linkedin/ | JSON https://fshy.ajam.dev/api/v1/entity/linkedin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Webdock /

- `compute/webdock` | fails-identity | evidence reported | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.linkedin.com/posts/is-hosting_we-launched-an-infrastructure-grants-program-activity-7488379865679872000-g8zr
- free tier: An infrastructure grant of a free VPS or dedicated server for open source projects and non-profits, for 12 months, renewed annually: quoted 'Open-source projects and nonprofits can apply for a free VPS or dedicated server, 12 months, with annual renewal opportunities'. | unit: none | metered on: wall-clock | read on: 2026-07-29 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The grant is for a project or a non-profit with an application, so the applicant must bring an organisation and a written case; a private individual with no project has no route in. [1]
- limits note: The grant is for a project or a non-profit with an application, so the applicant must bring an organisation and a written case; a private individual with no project has no route in.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 12-month renewable dedicated server would be the largest single unit among documented hosts if the applicant had a project to point at.
- reliability: no reliability event recorded
- notes: The company identity is also uncertain. The post handle is 'is-hosting' and the programme is named 'Hosting for Good', which is the initiative name used by iS Hosting, and neither a first-party grants page nor a terms page was located. Do not treat this as reachable tonight.
- extras:
  - facets.class: sponsored-vps-oss
  - facets.free_tier_kind: perpetual
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 
- sources:
  - [1] https://www.linkedin.com/posts/is-hosting_we-launched-an-infrastructure-grants-program-activity-7488379865679872000-g8zr
