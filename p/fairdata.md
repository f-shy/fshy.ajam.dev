# CSC Fairdata IDA

> fairdata.fi | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fairdata/ | JSON https://fshy.ajam.dev/api/v1/entity/fairdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CSC Fairdata IDA (Finland) — quota granted per CSC project, funded from the home organisation's national TB pool

- `storage/csc-fairdata-ida-quota-granted-per-csc-project-funded-fr` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-01T18:05:17.593Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.fairdata.fi/en/ida-quotas-by-organisation/
- free tier: No flat per-user number; the quota is a slice of your organisation's allocation. Published national pool (last updated 2025-02-28): University of Helsinki 1,500 TB, Aalto 480 TB, University of Oulu 465 TB, University of Turku 427 TB, Tampere universities 361.7 TB, Åbo Akademi 150 TB, and so on. You apply for a number of GiB in MyCSC and your organisation's IDA contact person approves it, 'usually within a few working days'. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free; IDA is a CSC national service and 'The use of Fairdata IDA doesn't consume Billing Units.' | metered: no
- identity: institution | detail: storage is granted to a CSC project, and the grant is approved by the IDA contact person of the home organisation named as the project's Storage Quota Owner, usually within a few working days. A CSC user account is created through the Finnish Haka or Virtu identity federations, or by applying to the CSC service desk as a collaborator of a Finnish research group or as a user whose organisation holds a contract with CSC. A CSC project can have a single member. No card and no phone number is asked for; the multi-factor setup asks for an authenticator app on a mobile device.
- interface: rest
- limits:
  - write-gated (binding): Approval. Two gates, one of them human. [1]
- limits note: Per-object-cap: not published. Retention: 'Data can be stored for a duration at least as long as the allocation grant period' (DeiC analogue); IDA requires an active CSC project and 'The validity of your CSC account can be extended by logging in to CSC's services'. request-rate: not published. Gate: CSC account (Haka/Virtu) + institutional quota owner approval. Two gates, one of them human.
- interface detail: rest
- tooling: IDA web UI plus official command-line tools ('or use IDA's command line tools'); publication path is Qvain + download through the Fairdata download service.
- composes with: Quota is per project and drawn from an institutional pool, and a CSC project 'does not have to correspond to a specific research project, and it can have only one member'. So many small projects each drawing a quota slice, each approved by the same institutional contact. The 1.5 PB Helsinki pool is the real ceiling.
- reliability: Second gate is a human approver at your home organisation; a lapsed CSC account or project takes the storage with it.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Last updated: 2025-02-28'; 'University of Helsinki | 1500', 'Aalto University | 480', 'University of Oulu | 465' (terabytes)
  - [2] 2026-10-21: captured 2026-06-08: 'A CSC project is a group of users, meaning it does not have to correspond to a specific research project, and it can have only one member'; quota chosen 'by entering a number only in gibibytes (GiB)'; 'approved ... usually within a few working days'
  - [3] 2026-10-21: 'The use of Fairdata IDA doesn't consume Billing Units.'
  - [2] 2026-11-01: the grant is a human approval by the home organisation, not a self-service allocation | capture: sha256:c099992dbc44d9ea929afb7f6f0ebdc5d89323b3e1db3261e54675cf643acbfd | quote: You will receive an email confirmation after the organisation’s IDA contact person has approved your application (usually within a few working days).
  - [1] 2026-11-01: the published national pool the record quotes is unchanged: Helsinki 1500 TB, Aalto 480 TB | capture: sha256:c7943235ba948377d4dd63c11d896f3e0fb5d44e2d32280db2295800ecf454ab | quote: | University | Quota in terabytes | | --- | --- | | Aalto University | 480 | | University of Helsinki | 1500 |
- sources:
  - [1] https://www.fairdata.fi/en/ida-quotas-by-organisation/
  - [2] https://www.fairdata.fi/en/ida/apply-for-ida-storage-space/
  - [3] https://docs.csc.fi/accounts/billing/
