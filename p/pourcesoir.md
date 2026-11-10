# PourCeSoir

> pourcesoir.in | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pourcesoir/ | JSON https://fshy.ajam.dev/api/v1/entity/pourcesoir.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PourCeSoir

- `debrid/pourcesoir` | fails-egress | evidence documented | binding none | category Usenet release listing (French-language, names only, no NZB download) | tier free
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.010Z (live) | stale on 2026-12-04
- url https://pourcesoir.in/
- free tier: Free registration, then a listing of new Usenet releases with their real title and their newsgroup source name. The site serves no NZB file. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: A listing site: the reader copies the Source name into an NZB search engine elsewhere.
- per-object cap: not applicable: no object is served | source: [1]
- retention: not stated on the pages read. A third-party listing claims 'Approximately 4,000 days of archive'. | source: [2] | note: reported
- egress: Nothing is retrievable from this site: the vendor page says NZB files cannot be downloaded here, so retrieval has to go through a separate NZB search engine and a news provider. | metered: no | source: [1]
- identity: email | detail: unverified: the register page text shows a password rule of at least 6 characters and no other field was readable; the home page says registration is required and free.
- interface: unknown
- limits:
  - request-rate: none applicable: no NZB file is served; each entry gives a source name to search for elsewhere [1]
- limits note: The missing download is not a counter; no vocabulary kind names a listing that serves no object.
- binding note: No counter binds because nothing is served; the verdict carries the finding.
- interface detail: A web listing behind a login; a third-party listing calls the platform Newznab and says it needs NZB-Monkey software, but the vendor page says NZB files cannot be downloaded from the site.
- endpoint: https://pourcesoir.in/
- tooling: The Source name on each row is the search term to paste into an NZB search engine; the vendor page points to a tools page for how to fetch an item.
- composes with: A French-language release discovery step in front of an NZB indexer that serves the file; it replaces no indexer.
- reliability: unverified: one read of three pages; no outage observed.
- notes: The verdict term fails-egress stands for 'serves no file': no vocabulary term names a listing that returns no object.
- evidence note: The no-download statement and the free mandatory registration are first-party text read; the sign-up fields beyond the password rule were not readable.
- extras:
  - price: USD 0
- evidence:
  - [1] 2026-11-03: the site does not allow NZB file downloads | capture: sha256:015a75218ddc07845305997395793270de27b553fab85e7b92269954a6ca9ae4 | quote: Sur ce site il n'est pas possible de télécharger des fichiers NZB.
  - [3] 2026-11-03: registration is mandatory and free | capture: sha256:5055def9a4de0a1cf39145faf52f1fc6d17788bea97f1c975ee159da16490794 | quote: Une inscription est obligatoire car elle sécurise les données indexées sur le réseau Usenet. Cet enregistrement est gratuit!
  - [4] 2026-11-03: the register form has a password of at least 6 characters | capture: sha256:5726b80b5e15a6f670b57370c1bef1d855d30558e289b260c76968a5da8755fb | quote: Le mot de passe doit faire au minimum 6 caractères.
  - [2] 2026-11-03: third-party: the listing claims about 4,000 days of archive | quote: Approximately 4,000 days of archive
  - [2] 2026-11-03: third-party: the listing says the platform needs NZB-Monkey software | quote: Requires NZB-Monkey software.
- sources:
  - [1] https://pourcesoir.in/content/2/fonctionnement-du-site/
  - [2] https://nzbhydra.com/indexers/
  - [3] https://pourcesoir.in/
  - [4] https://pourcesoir.in/register
