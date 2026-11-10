# Open Context

> opencontext.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opencontext/ | JSON https://fshy.ajam.dev/api/v1/entity/opencontext.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Open Context (archaeology / cultural heritage data publisher)

- `storage/open-context` | fails-quota | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://opencontext.org
- free tier: No published byte cap. 'Essentially, we provide publication services for the vast bulk of media that typically cannot fit into a conventional book or article publication.' Volume is negotiated with editors, not metered. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and open: content is published with no paywall and no metering, and is archived with leading digital libraries. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest
- limits note: No self-serve upload at all; structured data (spreadsheets/relational) plus media only; PDFs generally excluded unless documenting a dataset; editorial vetting with orange-dot status levels before release.
- interface detail: rest
- tooling: Read side is a real API plus OAI-PMH and DOI resolution; the WRITE side is deliberately not programmatic. 'The first step is to contact the Open Context editorial team.. we think it's important to start with a personal contact rather than an impersonal upload button.' No upload endpoint.
- composes with: Unlimited projects, but each is editorially co-produced, so throughput is bounded by the editorial team, not by quota.
- reliability: Genuinely open door ('Anyone can publish their research with Open Context — from individuals to teams') but human-in-the-loop by design, so it is an archive of last resort, not storage.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No published byte cap — 'Essentially, we provide publication services for the vast bulk of media that typically cannot fit into a conventional book or article publication.' Volume is negotiated with editors, not metered.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Anyone can publish their research with Open Context — from individuals to teams'; 'The first step is to contact the Open Context editorial team'
  - [2] 2026-10-21: publishing and preservation service description
- sources:
  - [1] https://www.opencontext.org/about/publishing
  - [2] https://opencontext.org/about/
