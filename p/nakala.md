# NAKALA

> nakala.fr | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nakala/ | JSON https://fshy.ajam.dev/api/v1/entity/nakala.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NAKALA (IR* Huma-Num, CNRS / French national HSS data repository)

- `storage/nakala` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nakala.fr
- disagrees on verdict: `storage/nakala` says qualifies-with-caveat, `storage/nakala-no-formal-size-limit-but-a-humanid-gate-and-a-con` says fails-identity
- free tier: Public deposits are explicitly uncapped: 'Il n'existe aucune limite pour les dépôts publics' (there is no limit for public deposits), and 'Un accès à vos données sans limite de volumétrie, ni de temps' (access to your data with no volume or time limit). The only quota is on PRIVATE staging: 10,000 private deposits or 100 GB equivalent. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Publication mints a DOI via DataCite and is irreversible. Deletion requires a request to Huma-Num, so this is a permanent archive, not scratch space. | source: [1] | note: not stated
- egress: Free. Files are served from Huma-Num/IN2P3-hosted infrastructure in France with no metering and no egress charge; public deposits are downloadable by any visitor and IIIF image endpoints are exposed for tif/tiff/jpg/jpeg/jp2. | metered: no
- identity: institution
- interface: rest, rclone
- limits note: Private staging capped at 10,000 deposits / 100 GB; public deposits uncapped. Publication mints a DOI via DataCite and is irreversible. Deletion requires a request to Huma-Num, so this is a permanent archive, not scratch space. Eligibility is the real limit: the depositor must belong to the French academic world, or be part of a project whose lead team is French-academic.
- interface detail: rest
- tooling: Documented REST API split into search / datas / collections / groups / users / vocabularies, with a per-account API key ('Certaines opérations nécessitent ... sa clé d'API disponible dans son compte personnel'); swagger at api.nakala.fr/doc, separate test instance apitest.nakala.fr. Also OAI-PMH (api.nakala.fr/oai2?verb=Identify), a SPARQL triplestore, IIIF Image API, and a published notebook at gitlab.huma-num.fr/huma-num-public/notebook-api-nakala. No rclone backend.
- composes with: Unlimited public deposits per account, no volume cap per deposit. So the account is the only unit and it does not need multiplying for 500 GB. Groups feature shares deposit rights across a project team, so a lab can pour many researchers' output into one quota-free surface.
- reliability: CRITICAL liveness flag: nakala.fr and api.nakala.fr both returned HTTP 503 on 6 consecutive probes across ~25 minutes (site and API, direct and through the proxy), so the quota is docs-verified but the service was NOT live at probe time. Budget-stable (CNRS-funded national infrastructure) but treat availability as unconfirmed.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Il n'existe aucune limite pour les dépôts publics' and 'Le nombre de dépôts privés par déposant est limité à 10 000 (ou l'équivalent de 100 Go)'
  - [2] 2026-10-21: REST API endpoint list, api.nakala.fr/doc, OAI-PMH, SPARQL, IIIF
  - [3] 2026-10-21: probe: GET -> 503 six times; GET https://api.nakala.fr/oai2?verb=Identify -> 503 (service down at probe time)
- sources:
  - [1] https://documentation.huma-num.fr/nakala/
  - [2] https://documentation.huma-num.fr/nakala-API/
  - [3] https://nakala.fr/

## Nakala (Huma-Num, France) - no formal size limit, but a HumanID gate and a conversation with the team

- `storage/nakala-no-formal-size-limit-but-a-humanid-gate-and-a-con` | fails-identity | evidence reported | binding none | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nakala.fr/
- disagrees on verdict: `storage/nakala` says qualifies-with-caveat, `storage/nakala-no-formal-size-limit-but-a-humanid-gate-and-a-con` says fails-identity
- free tier: 'There is no formal limitation on the size of data deposited'; above ~10 GB per file you must contact the Nakala team first. Private pre-publication space is capped far lower (9,999 items or 100 GB), so the large-volume path is publish-as-you-go. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 GB per file | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free public HTTPS with a DOI per deposit; no egress metering published. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits:
  - per-object-cap: 10 GB per file [1]
- limits note: Account path is HumanID -> request Nakala access -> 'Discuss the scientific and technical project associated with the deposit with HumaNum's team'. Research data only, must be documented to a metadata schema, licence from a closed list, ORCID checked on authors. Published deposits cannot be deleted unilaterally.
- interface detail: rest
- tooling: Nakala REST API plus nakalot (multipart batch uploader driven by a CSV/XLS manifest); OAI-PMH.
- composes with: Per deposit, unlimited deposits - but the gate is identity, not bytes.
- reliability: MESR-funded national infrastructure, data preserved at CINES after audit; ~100 TB of storage on the ISIDORE/Nakala stack. French research context in practice.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 'There is no formal limitation on the size of data deposited'; above ~10 GB per file you must contact the Nakala team first. Private pre-publication space is capped far lower (9,999 items or 100 GB), so the large-volume path is publish-as-you-go.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Il n'y a pas formellement de limitation pour la taille des donnees deposees. Cependant... superieur a 10 GOs par fichier, il est necessaire de prendre contact avec l'equipe NAKALA'
  - [2] 2026-10-21: 'Request a HumanID login'; 'Discuss the scientific and technical project... with HumaNum's team'; mandatory pre-curation for level 2/3
  - [3] 2026-10-21: 'Espace de depot limite a 9 999 donnees ou a 100 Go' for the private status
- sources:
  - [1] https://documentation.huma-num.fr/nakala-faq/
  - [2] https://documentation.huma-num.fr/en/nakala-workflow-en/
  - [3] https://www.orient-mediterranee.com/wp-content/uploads/2024/01/2023_NAKALA-Decouverte-Webinaire2909.pdf
