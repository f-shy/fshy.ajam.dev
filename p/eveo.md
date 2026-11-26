# EVEO Object Storage S3

> eveo.com.br | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eveo/ | JSON https://fshy.ajam.dev/api/v1/entity/eveo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EVEO Object Storage S3 (Brazil)

- `storage/eveo-object-storage-s3-the-only-zero-egress-s3-endpoint` | qualifies-with-caveat | evidence reported | binding none | category object-storage
- needs card no, phone no, ID no, institution yes | verified 2026-11-09 (live) | stale on 2026-11-24
- url https://www.eveo.com.br/object-storage-s3/
- price $10.19/TB/mo at both 5 TB and 20 TB (strict per-GB, no tiers), egress $0. R$0.05/GB × 1024 GB/TB × 0.199082 USD/BRL = $10.19. Note this is per decimal GB on the vendor's wording; if billed per GiB the figure is $10.96/TB. | parsed USD 10.19/TB-mo
- free tier: Armazenamento compatível com S3 a partir de R$ 0,05/GB, com infraestrutura no Brasil, escalabilidade e suporte especializado. | unit: GB | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Na EVEO, a saída é gratuita, operações PUT, GET, LIST não pesam na fatura. | metered: yes
- identity: institution | detail: Nome, Sobrenome, E-mail, Telefone, Empresa
- interface: s3-compatible, rclone
- limits note: com suporte a buckets de até 5PB e sem necessidade de provisionamento
- interface detail: s3
- tooling: S3-compatible with SigV4 presigned URLs. So it can sit behind Cloudflare the same way as any S3 store. rclone `s3`, restic, Veeam. Two-region replication inside Brazil, Tier III datacentres.
- composes with: Pure per-GB, so 5 TB and 20 TB cost the same per TB. No bucket cap below 5 PB.
- reliability: Enterprise-oriented Brazilian provider with Tier III DCs and two-region replication; no independent price/performance benchmark located. The zero-egress claim is on the vendor's own page and uncontradicted, but there is no published price list PDF to cross-check the R$0.05 number against, so confidence on the exact rate is medium even though confidence on the egress policy is high.
- notes: the same as the free tier
- evidence note: the cited page was read on 2026-11-09
- extras:
  - price_verbatim: $10.19/TB/mo at both 5 TB and 20 TB (strict per-GB, no tiers), egress $0. R$0.05/GB × 1024 GB/TB × 0.199082 USD/BRL = $10.19. Note this is per decimal GB on the vendor's wording; if billed per GiB the figure is $10.96/TB.
- evidence:
  - [1] 2026-10-21: «Armazene grandes volumes por apenas R$0,05/GB»; «Sem Taxas — Zero Egress e API … a saída é gratuita, operações PUT, GET, LIST não pesam na fatura»
  - withheld 2026-10-21: same page — «suporte a buckets de até 5PB e sem necessidade de provisionamento»; «Replicação em duas regiões distintas»; «imutabilidade WORM nativa»
  - withheld 2026-10-21: search snippet — «Object Storage S3 | R$ 0,05/GB Sem Egress Fee … 50 TB | R$ 16.» (the 50 TB row was truncated in the snippet and not recoverable from the page body)
  - [1] 2026-11-09: the page states the S3-compatible storage rate of R$ 0,05/GB with infrastructure in Brazil | capture: sha256:006f4eb89b634e9049e3b0978d0c9fbf5811d6369d5ad4fbdb90aea7bf022e8b | quote: Armazenamento compatível com S3 a partir de R$ 0,05/GB, com infraestrutura no Brasil, escalabilidade e suporte especializado.
  - [1] 2026-11-09: egress is free and PUT, GET and LIST operations do not count on the invoice | capture: sha256:006f4eb89b634e9049e3b0978d0c9fbf5811d6369d5ad4fbdb90aea7bf022e8b | quote: Na EVEO, a saída é gratuita, operações PUT, GET, LIST não pesam na fatura.
  - [1] 2026-11-09: buckets up to 5 PB need no provisioning | capture: sha256:006f4eb89b634e9049e3b0978d0c9fbf5811d6369d5ad4fbdb90aea7bf022e8b | quote: com suporte a buckets de até 5PB e sem necessidade de provisionamento
  - [1] 2026-11-09: the contact form requires name, surname, e-mail, telephone and company | capture: sha256:006f4eb89b634e9049e3b0978d0c9fbf5811d6369d5ad4fbdb90aea7bf022e8b | quote: Nome _\*_Sobrenome _\*_E-mail _\*_Telefone _\*_Empresa _\*_
- sources:
  - [1] https://www.eveo.com.br/object-storage-s3/
