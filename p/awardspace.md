# AwardSpace

> awardspace.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/awardspace/ | JSON https://fshy.ajam.dev/api/v1/entity/awardspace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AwardSpace

- `compute/awardspace` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone unknown, ID no, institution no | verified 2026-11-04T11:01:13.171Z (live) | stale on 2026-12-05
- url https://www.awardspace.com/kb/what-are-the-limitations-on-web-space-and-bandwidth/
- free tier: Free plan, quoted: 'Storage: 1 GB', 'Bandwidth: 5 GB per month', 'Visits: Limited to approximately 5,000 visits per month', 'Databases: One MySQL database', 'Email: One email account'. The plan is 'Free forever' with 'No Credit Card', one domain and three subdomains, PHP and a one-click installer. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Free Hosting - Storage: 1 GB - Bandwidth: 5 GB per month - Visits: Limited to approximately 5,000 visits per month - Databases: One MySQL database - Email: One email account', quoted | metered: yes | free allowance: 5 GB per month | price per TB: not published: the free-hosting page and the limitations page state 5 GB per month as the maximum and give no overage price | source: [1]
- identity: email | detail: no card: the free-hosting page states 'No Credit Card' beside 'Free forever', so no payment method is taken and no hold exists. The signup form's own fields are not described in any evidence row, so whether an email, phone number or ID document is required is unknown; kind kept as email without an evidence row stating it.
- interface: ftp
- limits:
  - volume-quota (binding): 5 GB of transfer a month and about 5,000 visits is the wall, and there is no CPU or memory figure published, so the first thing to fail is traffic rather than compute. [1]
- limits note: 5 GB of transfer a month and about 5,000 visits is the wall, and there is no CPU or memory figure published, so the first thing to fail is traffic rather than compute.
- binding note: the same as limits note
- interface detail: web control panel with a File Manager, plus FTP: a default FTP account is created at sign-up and the free plan allows a 15 MB upload per file over FTP; SSH is not supported on the free plan; no REST API or CLI is documented (unverified)
- tooling: a default FTP account, per https://www.awardspace.com/kb/basic-features/: "we automatically create a default FTP account on your behalf"; no client is named on that page
- composes with: a free PHP host with one MySQL database and no card is a place for a small endpoint or a cron-driven page that outlives a free PaaS trial; the 5 GB monthly transfer stops it from serving anything heavy.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'Free web hosting + a free short domain, PHP, MySQL, App Installer, Email Sending & No Ads'. The vendor confirms PHP, MySQL, one mailbox and no ads, and adds the numbers the aggregator omits: 1 GB disk, 5 GB a month, about 5,000 visits. The 'free short domain' is the part that did not reproduce: the free plan includes one domain the user brings plus three subdomains on the provider's own domain. CPU and memory are unpublished, so shape is null rather than inferred from the disk.
- extras:
  - facets.free_tier_kind: free-forever
- evidence:
  - [1] 2026-10-22: 'Free Hosting - Storage: 1 GB - Bandwidth: 5 GB per month - Visits: Limited to approximately 5,000 visits per month - Databases: One MySQL database - Email: One email account', quoted
  - [2] 2026-10-22: 'Free forever', 'No Credit Card', 'one domain and add up to three free subdomains', 'Absolutely free website hosting without ads', quoted
  - [1] 2026-11-03: the free plan has a 5 GB per month bandwidth cap | capture: sha256:ca8a39c16e32aa36e4e173fa67bfc632d53ec8679b8f672b25168a5a38c34fcc | quote: - Bandwidth: 5 GB per month
  - [2] 2026-11-03: 5 GB a month is the maximum on the free plan; no overage price is stated | capture: sha256:931905a7665da6aa7059867bc625cdc98107c19ffbd2f3634f313e3927074d78 | quote: Even though 5GB of monthly traffic is the maximum bandwidth in our free hosting environment, you’re using the same high-speed network as our paying clients!
  - [2] 2026-11-03: files are managed through a web file manager | capture: sha256:931905a7665da6aa7059867bc625cdc98107c19ffbd2f3634f313e3927074d78 | quote: With our user-friendly File Manager you can upload the files for your website, download them or even you will be able to edit HTML, CSS, PHP, and other programming files.
  - [3] 2026-11-04: the free hosting plan uploads over FTP as well as the File Manager | capture: sha256:a96d78b5483ca4370855b2dc1e59caaca4b8244892c954cb3ffd4b56ab524b30 | quote: For the free hosting plan the maximum upload file size is 15 MB both for the File Manager and FTP.
  - [4] 2026-11-04: a default FTP account is created at sign-up | capture: sha256:11096764cc366e8b34c61c99321a70d856e6c577609bc98da500881bdc763454 | quote: we automatically create a default FTP account on your behalf
  - [5] 2026-11-04: SSH is not available on the free plan | capture: sha256:eb6c9e2acd037b19c2d9fb758f0b1a2b24f15815094bafc2c68cceff975488ac | quote: the free hosting plan does not support SSH
  - [4] 2026-11-04: the page names an FTP account created at sign-up and no other client | capture: sha256:11096764cc366e8b34c61c99321a70d856e6c577609bc98da500881bdc763454 | quote: we automatically create a default FTP account on your behalf
- sources:
  - [1] https://www.awardspace.com/kb/what-are-the-limitations-on-web-space-and-bandwidth/
  - [2] https://www.awardspace.com/free-hosting/
  - [3] https://www.awardspace.com/kb/file-size-limits-free-premium-hosting-accounts/
  - [4] https://www.awardspace.com/kb/basic-features/
  - [5] https://www.awardspace.com/kb/create-ssh-account/
