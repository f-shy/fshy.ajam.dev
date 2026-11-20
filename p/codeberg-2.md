# Codeberg Pages

> codeberg.page | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/codeberg-2/ | JSON https://fshy.ajam.dev/api/v1/entity/codeberg-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Codeberg Pages (git-pages)

- `storage/codeberg-pages` | fails-quota | evidence reported | binding write-gated | category git
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:08.916Z (live) | stale on 2026-12-04
- url https://codeberg.page
- free tier: No hard quota: 'there is no quota for valid use-cases', with a soft review threshold at 750 MiB Git storage and 1.5 GiB packages/LFS/attachments per account. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No egress quota or charge published; Codeberg runs its own pages server (git-pages) and asks users not to be wasteful rather than metering. | metered: no
- identity: email
- interface: git, cli
- limits:
  - write-gated (binding): review threshold at 750 MiB Git storage and 1 [1]
  - write-gated (binding): review request is expected [1]
- limits note: 750 MiB Git storage and 1.5 GiB packages/LFS/attachments before an admin review request is expected; files under 1 MiB are cached at the edge; each repo gets one pages site.
- interface detail: git
- tooling: git-pages accepts a direct HTTP upload ('git-pages-cli https://coolcat.wiki --password ... --upload-dir site/') or a Forgejo Actions webhook; any Forgejo host can self-host the same server.
- composes with: One account with many repos, each with its own pages branch; unlimited repos per account in practice. But 750 MiB-per-account soft line means the multiplier is accounts, not repos.
- reliability: Codeberg explicitly reviews and can deny 'unreasonable' resource usage. This is a community forge with active human moderation of storage, which is a different reliability class from a commercial CDN.
- notes: the same as the free tier
- extras:
  - unit_note: free_tier.unit is 'mixed' because the headline is denominated in MiB or KiB, which the schema enum does not carry; the verbatim free_tier.stated keeps the true unit.
  - dead_end.failure_class: write-gated
  - dead_end.why: No hard quota: 'there is no quota for valid use-cases', with a soft review threshold at 750 MiB Git storage and 1.5 GiB packages/LFS/attachments per account.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'no quota for valid use-cases', 'If you intend to use more than: 750 MiB for Git storage, 1.5 GiB of packages, LFS and attachments ... request these resources first'
  - [2] 2026-10-21: pages-server 'in maintenance mode', Codeberg Pages migrating to git-pages
  - [3] 2026-10-21: files under 1 MiB are cached at the edge
  - [1] 2026-11-19: Codeberg Pages has no hard published quota for valid use cases | capture: sha256:53e057811ba24b7f7719ef73555ee6030c3d84a8e5b158aea574efa6ace517a6 | quote: there is no quota for valid use-cases!
  - [1] 2026-11-19: Larger projects are reviewed and can be denied as unreasonable use | capture: sha256:53e057811ba24b7f7719ef73555ee6030c3d84a8e5b158aea574efa6ace517a6 | quote: However, we will review larger projects and reserve the right to deny service if we consider your resource usage unreasonable, or if your usage impacts the quality and stability for other users.
  - [2] 2026-11-19: Codeberg Pages is migrating to the git-pages server | capture: sha256:75ab521af041a4cb32f5fbafa4776c7d68449eebc50e37e9e377b89204b42fab | quote: Codeberg Pages itself is in the process of migrating to the new [git-pages](https://git-pages.org/) server and is still a fully supported feature of Codeberg.
- sources:
  - [1] https://docs.codeberg.org/getting-started/faq/
  - [2] https://codeberg.org/Codeberg/pages-server
  - [3] https://docs.codeberg.org/codeberg-pages/troubleshooting/
