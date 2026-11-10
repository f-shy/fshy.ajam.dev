# SciServer

> sciserver.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sciserver/ | JSON https://fshy.ajam.dev/api/v1/entity/sciserver.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SciServer

- `compute/sciserver` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.sciserver.org/compute-images/
- free tier: Anyone can create a free account and run Jupyter notebooks on SciServer Compute containers that sit next to the hosted data. The persistent quota is 10 GB per user and "you may only create up to three containers". The site describes its purpose as letting researchers work with terabytes or petabytes "without needing to download any large datasets", and the default image ships Python 3.7, R 3.6.2, Jupyter Notebook 6.0.3, JupyterLab 1.2.6, TensorFlow 2.0.0 and PyTorch 1.4.0. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-open-registration
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): 10 GB of persistent storage per user is the hard ceiling, temporary volumes carry no quota but are deleted after a stated grace period, and no CPU or memory quota per container is published anywhere read. [1]
- limits note: 10 GB of persistent storage per user is the hard ceiling, temporary volumes carry no quota but are deleted after a stated grace period, and no CPU or memory quota per container is published anywhere read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The composition is data locality rather than raw capacity: SciServer hosts SDSS, GALEX and Gaia releases next to the containers, so a 10 GB quota is not a limit on the analysis because the terabyte inputs never enter the user volume, which is the opposite trade from every other free tier in documented records.
- reliability: no reliability event recorded
- notes: Two facts argued against a stronger verdict. The image list is frozen around 2019 and 2020, with Python 3.7 and PyTorch 1.4 presented as current, which means the platform's software is roughly six years old and modern packages may not be installable on that base; and no per-container CPU or memory ceiling is published, so the compute side of the offer cannot be sized from the documentation. The 10 GB figure is quoted from the project's own 2021 how-to because the current policy page sits behind a login, and a 2021 figure for a live quota is older than a reader should trust without rechecking. Registration needs only an email or a linked identity. The image-era facts are the ones most likely to be stale in six months.
- extras:
  - facets.class: open-science-platform
  - facets.free_tier_kind: perpetual-open-registration
- evidence:
  - [1] 2026-10-22: "you may only create up to three containers", quoted
  - [1] 2026-10-22: the default image ships Python 3.7 (Anaconda 2019.10), R 3.6.2, Jupyter Notebook 6.0.3, JupyterLab 1.2.6, TensorFlow 2.0.0 and PyTorch 1.4.0, and "Both machine learning libraries work with CPU only. GPU hardware acceleration is not yet available in this image", quoted
  - [2] 2026-10-22: User Volumes under "Storage" are backed up and permanent "but there is a quota limit of 10GB"; "Temporary" volumes have no quota because they are deleted, quoted
  - [3] 2026-10-22: "bringing the analysis to the data"; the system hosts scientific datasets alongside the compute so large data need not be downloaded, quoted
  - [4] 2026-10-22: reported by the project at ADASS 2018: "Researchers, educators, students, and citizen scientists can create a free account to get 10 GB of file storage space", cited as a third-party statement of the same figure
- sources:
  - [1] https://www.sciserver.org/compute-images/
  - [2] https://www.sciserver.org/wp-content/uploads/2021/09/sciserver-how-to-2021-09-22.pdf
  - [3] https://www.sciserver.org/about/
  - [4] https://adass2018.astro.umd.edu/abstracts/F2.html
