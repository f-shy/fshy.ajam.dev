# open heritage

> openheritage3d.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openheritage3d/ | JSON https://fshy.ajam.dev/api/v1/entity/openheritage3d.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Audiovisual / heritage: Open Heritage 3D (CyArk + UC San Diego CHEI)

- `storage/audiovisual-heritage-open-heritage-3d` | fails-quota | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:31:28.059Z (live) | stale on 2026-11-19
- url https://openheritage3d.org
- free tier: No published quota. The project is a consortium repository. 'we invite others to join the Open Heritage 3D project and contribute their datasets'. With 200+ datasets and DOIs under the 10.26301 prefix. Contribution is by organisational agreement, not self-serve signup. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Each project page lists its data types with sizes (10.3 GB of terrestrial LiDAR on a sampled project) and states that links to all available data types are emailed; no metering is stated. | metered: no
- identity: institution | detail: unverified: the about page invites others to join and contribute datasets but states no application form, fee or identity requirement
- interface: unknown
- limits:
  - write-gated (binding): invite others to join the Open Heritage 3D project and contribute their datasets [1]
- limits note: Organisational membership required; heritage-3D scope (photogrammetry, laser scan, point clouds); no published per-file or total figures at all.
- interface detail: wrapper-only
- tooling: Web catalogue with per-project pages and DOI resolution; no public upload API and no documented deposit endpoint. Joining requires contacting the consortium (CHEI at UCSD, CyArk, Politecnico di Torino G4CH, Washington and Lee).
- composes with: Not chainable by an individual. The unit is an institutional partnership. A single organisation could contribute many datasets, but the door is a consortium agreement.
- reliability: Stable academic consortium with DOI permanence and mirrored preservation, but there is no self-service path. This is a partnership, not a storage provider.
- notes: the same as the free tier
- evidence note: The 2026-11-03 evidence rows read https://openheritage3d.org/about (invitation to join and contribute datasets) and https://openheritage3d.org/project.php?id=07af-c325 (download links are emailed). No page read states that contribution is by organisational agreement, and the identity requirement is unverified, so the rung stays reported.
- extras:
  - dead_end.failure_class: write-gated
  - dead_end.why: No published quota. The project is a consortium repository — 'we invite others to join the Open Heritage 3D project and contribute their datasets' — with 200+ datasets and DOIs under the 10.26301 prefix. Contribution is by organisational agreement, not self-serve signup.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'we invite others to join the Open Heritage 3D project and contribute their datasets'; consortium led by CHEI/UCSD, CyArk, G4CH Politecnico di Torino, Washington and Lee
  - [2] 2026-10-21: live catalogue, 200+ projects each with a 10.26301/* DOI (probe: 200, full table returned)
  - [3] 2026-11-03: a project page does not serve the files directly: download links are emailed | capture: sha256:b5d3fd0bf6d1909877258323ce1d119f1f74803ab02e5e3b1d225c7f612c3039 | quote: Download (Links to all available data types will be emailed)
  - [1] 2026-11-03: the site invites others to join and contribute datasets; no self-serve upload or quota is described | capture: sha256:35feec4edd0c5a0c4477b1e78039451435db787b41a2ff7184955934d40f965f | quote: we invite others to join the Open Heritage 3D project and contribute their datasets to this growing library of data.
  - [1] 2026-11-04: the site invites others to join and contribute datasets; no self-serve upload or quota is described | capture: sha256:35feec4edd0c5a0c4477b1e78039451435db787b41a2ff7184955934d40f965f | quote: we invite others to join the Open Heritage 3D project and contribute their datasets to this growing library of data.
- sources:
  - [1] https://openheritage3d.org/about
  - [2] https://openheritage3d.org/data
  - [3] https://openheritage3d.org/project.php?id=07af-c325

## open heritage 3d (cyark + hes + usf)

- `storage/open-heritage-3d` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://openheritage3d.org/joinusPage
- free tier: none reachable: Fully consortium-gated and mediated through Dropbox: 'Once the data is packaged it can be uploaded via a Dropbox request link assigned by the Open Heritage Alliance', with a DOI and a… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Fully consortium-gated and mediated through Dropbox: 'Once the data is packaged it can be uploaded via a Dropbox request link assigned by the Open Heritage Alliance', with a DOI and a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Fully consortium-gated and mediated through Dropbox: 'Once the data is packaged it can be uploaded via a Dropbox request link assigned by the Open Heritage Alliance', with a DOI and a…
  - [2] 2026-10-21: cited as the basis of the rejection: Fully consortium-gated and mediated through Dropbox: 'Once the data is packaged it can be uploaded via a Dropbox request link assigned by the Open Heritage Alliance', with a DOI and a metada
  - [3] 2026-10-21: cited as the basis of the rejection: Fully consortium-gated and mediated through Dropbox: 'Once the data is packaged it can be uploaded via a Dropbox request link assigned by the Open Heritage Alliance', with a DOI and a metada
- sources:
  - [1] https://openheritage3d.org/joinusPage
  - [2] https://www.re3data.org/repository/r3d100013317
  - [3] https://isprs-annals.copernicus.org/articles/X-M-1-2023/215/2023/isprs-annals-X-M-1-2023-215-2023.pdf
