# CSC Fairdata IDA

> fairdata.fi | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fairdata/ | JSON https://fshy.ajam.dev/api/v1/entity/fairdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CSC Fairdata IDA (Finland) — quota granted per CSC project, funded from the home organisation's national TB pool

- `storage/csc-fairdata-ida-quota-granted-per-csc-project-funded-fr` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T04:14:18.948Z (live) | stale on 2026-12-10
- url https://www.fairdata.fi/en/ida-quotas-by-organisation/
- free tier: University of Helsinki quota: 1500 TB | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1]
- retention: source: [1] | note: Data outside a published dataset is deleted 90 days after the CSC project closes; CSC may delete data transferred to IDA more than 24 months ago that is not part of a published dataset
- egress: The use of Fairdata IDA doesn't consume Billing Units. | metered: no
- identity: institution | detail: storage is granted to a CSC project, and the grant is approved by the IDA contact person of the home organisation named as the project's Storage Quota Owner, usually within a few working days. A CSC user account is created through the Finnish Haka or Virtu identity federations, or by applying to the CSC service desk as a collaborator of a Finnish research group or as a user whose organisation holds a contract with CSC. A CSC project can have a single member. No card and no phone number is asked for; the multi-factor setup asks for an authenticator app on a mobile device.
- interface: rest
- limits:
  - write-gated (binding): approval by the organisation’s IDA contact person, usually within a few working days [1]
- limits note: Per-object-cap: not published. Retention: 'Data can be stored for a duration at least as long as the allocation grant period' (DeiC analogue); IDA requires an active CSC project and 'The validity of your CSC account can be extended by logging in to CSC's services'. request-rate: not published. Gate: CSC account (Haka/Virtu) + institutional quota owner approval. Two gates, one of them human.
- interface detail: rest
- tooling: IDA web UI plus official command-line tools ('or use IDA's command line tools'); publication path is Qvain + download through the Fairdata download service.
- composes with: Quota is per project and drawn from an institutional pool, and a CSC project 'does not have to correspond to a specific research project, and it can have only one member'. So many small projects each drawing a quota slice, each approved by the same institutional contact. The 1.5 PB Helsinki pool is the real ceiling.
- reliability: Second gate is a human approver at your home organisation; a lapsed CSC account or project takes the storage with it.
- notes: No flat per-user number; the quota is a slice of your organisation's allocation. Published national pool (last updated 2025-02-28): University of Helsinki 1,500 TB, Aalto 480 TB, University of Oulu 465 TB, University of Turku 427 TB, Tampere universities 361.7 TB, Åbo Akademi 150 TB, and so on. You apply for a number of GiB in MyCSC and your organisation's IDA contact person approves it, 'usually within a few working days'.
- evidence note: the quotas-by-organisation page lists a 1500 TB quota for the University of Helsinki
- evidence:
  - [1] 2026-10-21: 'Last updated: 2025-02-28'; 'University of Helsinki | 1500', 'Aalto University | 480', 'University of Oulu | 465' (terabytes)
  - [2] 2026-10-21: captured 2026-06-08: 'A CSC project is a group of users, meaning it does not have to correspond to a specific research project, and it can have only one member'; quota chosen 'by entering a number only in gibibytes (GiB)'; 'approved ... usually within a few working days'
  - [3] 2026-10-21: 'The use of Fairdata IDA doesn't consume Billing Units.'
  - [2] 2026-11-01: the grant is a human approval by the home organisation, not a self-service allocation | capture: sha256:c099992dbc44d9ea929afb7f6f0ebdc5d89323b3e1db3261e54675cf643acbfd | quote: You will receive an email confirmation after the organisation’s IDA contact person has approved your application (usually within a few working days).
  - [1] 2026-11-01: the published national pool the record quotes is unchanged: Helsinki 1500 TB, Aalto 480 TB | capture: sha256:c7943235ba948377d4dd63c11d896f3e0fb5d44e2d32280db2295800ecf454ab | quote: | University | Quota in terabytes | | --- | --- | | Aalto University | 480 | | University of Helsinki | 1500 |
  - [1] 2026-11-09: the quotas table lists 1500 terabytes for the University of Helsinki | capture: sha256:c7943235ba948377d4dd63c11d896f3e0fb5d44e2d32280db2295800ecf454ab | quote: | University | Quota in terabytes | | --- | --- | | Aalto University | 480 | | University of Helsinki | 1500 |
  - [2] 2026-11-09: the organisation’s IDA contact person approves the application, usually within a few working days | capture: sha256:c099992dbc44d9ea929afb7f6f0ebdc5d89323b3e1db3261e54675cf643acbfd | quote: You will receive an email confirmation after the organisation’s IDA contact person has approved your application (usually within a few working days).
  - [2] 2026-11-09: the application names the home organisation as the storage quota owner | capture: sha256:c099992dbc44d9ea929afb7f6f0ebdc5d89323b3e1db3261e54675cf643acbfd | quote: Under Storage Quota Owner, select your home organisation (if your home organisation is part of the Tampere universities, choose “Tampere university” from the dropdown menu).
  - [3] 2026-11-09: Fairdata IDA does not consume Billing Units | capture: sha256:d0dd0e9a79635d765dfce741f511240ef41008412b2ed2ae3f1d4a6cd80dc1a8 | quote: The use of Fairdata IDA doesn't consume Billing Units.
  - [1] 2026-11-25: the quotas table states allocation amounts but no per-object size cap | capture: sha256:c7943235ba948377d4dd63c11d896f3e0fb5d44e2d32280db2295800ecf454ab | quote: | University | Quota in terabytes | | --- | --- | | Aalto University | 480 | | University of Helsinki | 1500 |
  - [4] 2026-11-25: the IDA terms state continuous retention of published datasets independent of account and project validity | capture: sha256:ed38f0b0063316f60a267ccb496b039cf8bd22183e481f23d2d33d8142d59020 | quote: Services retain Research Datasets stored in the IDA service and published in Etsin continuously, regardless of the validity of the User’s account and CSC Project
  - [4] 2026-11-25: the IDA terms state deletion 90 days after project closure for data outside a published dataset | capture: sha256:ed38f0b0063316f60a267ccb496b039cf8bd22183e481f23d2d33d8142d59020 | quote: CSC will delete the Data stored in IDA (including published Data) 90 days after the CSC Project is closed, as described in the [General the provider for CSC’s Services for Research](https://research.csc.fi/terms-of-use/).
  - [4] 2026-11-25: data outside a published dataset may be deleted after 24 months even while the project is active | capture: sha256:ed38f0b0063316f60a267ccb496b039cf8bd22183e481f23d2d33d8142d59020 | quote: Unless otherwise agreed, CSC reserves the right to delete Data from the IDA service that was transferred to IDA more than 24 months ago but is not part of any Research Dataset findable in the Fairdata Etsin service.
  - [3] 2026-11-25: CSC's billing documentation states that IDA use does not consume Billing Units | capture: sha256:0ad62f71ef1d7df52e8b39964ee75235a25241222672b3069f21de63e85d2567 | quote: The use of Fairdata IDA doesn't consume Billing Units.
  - [1] 2026-11-25: the quotas table still lists the 1500 TB Helsinki pool quoted by the free tier | capture: sha256:c7943235ba948377d4dd63c11d896f3e0fb5d44e2d32280db2295800ecf454ab | quote: | University | Quota in terabytes | | --- | --- | | Aalto University | 480 | | University of Helsinki | 1500 |
  - [4] 2026-11-25: the IDA terms still state continuous retention for published datasets | capture: sha256:ed38f0b0063316f60a267ccb496b039cf8bd22183e481f23d2d33d8142d59020 | quote: Services retain Research Datasets stored in the IDA service and published in Etsin continuously, regardless of the validity of the User’s account and CSC Project
  - [4] 2026-11-25: the IDA terms still state deletion 90 days after project closure for data outside a published dataset | capture: sha256:ed38f0b0063316f60a267ccb496b039cf8bd22183e481f23d2d33d8142d59020 | quote: CSC will delete the Data stored in IDA (including published Data) 90 days after the CSC Project is closed, as described in the [General the provider for CSC’s Services for Research](https://research.csc.fi/terms-of-use/).
  - [3] 2026-11-25: CSC states IDA use consumes no Billing Units, so egress is not metered | capture: sha256:0ad62f71ef1d7df52e8b39964ee75235a25241222672b3069f21de63e85d2567 | quote: The use of Fairdata IDA doesn't consume Billing Units.
  - [2] 2026-11-25: the write gate remains approval by the home organisation's IDA contact person | capture: sha256:c099992dbc44d9ea929afb7f6f0ebdc5d89323b3e1db3261e54675cf643acbfd | quote: You will receive an email confirmation after the organisation’s IDA contact person has approved your application (usually within a few working days).
- sources:
  - [1] https://www.fairdata.fi/en/ida-quotas-by-organisation/
  - [2] https://www.fairdata.fi/en/ida/apply-for-ida-storage-space/
  - [3] https://docs.csc.fi/accounts/billing/
  - [4] https://www.fairdata.fi/en/ida-research-data-storage-service-terms-of-use/
