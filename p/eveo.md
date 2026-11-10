# EVEO Object Storage S3

> eveo.com.br | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eveo/ | JSON https://fshy.ajam.dev/api/v1/entity/eveo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EVEO Object Storage S3 (Brazil)

- `storage/eveo-object-storage-s3-the-only-zero-egress-s3-endpoint` | qualifies-with-caveat | evidence reported | binding none | category object-storage
- needs card yes, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.eveo.com.br/object-storage-s3/
- price $10.19/TB/mo at both 5 TB and 20 TB (strict per-GB, no tiers), egress $0. R$0.05/GB × 1024 GB/TB × 0.199082 USD/BRL = $10.19. Note this is per decimal GB on the vendor's wording; if billed per GiB the figure is $10.96/TB. | parsed USD 10.19/TB-mo
- free tier: R$0.05/GB/month, billed on stored GB only; buckets up to 5 PB, no provisioning. Positioned as «Armazenamento sem taxas de download (egress) ou API». | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: ZERO, stated as the product's entire pitch: «Zero Egress e API … a saída é gratuita, operações PUT, GET, LIST não pesam na fatura» (egress is free; PUT/GET/LIST operations do not weigh on the invoice). Also «paga apenas pelo GB armazenado … e acessa o que é seu sem taxas de pedágio». No retrieval fee. WORM immutability native. | metered: yes
- identity: card | detail: card
- interface: s3-compatible, rclone
- limits note: Brazil-only geography. The same intercontinental-latency objection as Rollin Host for the hot set, though as an archive tier it is fine. The R$0.05/GB figure is the advertised rate and no volume staircase is published, so there may be no discount at 20 TB; ask. Enterprise sales motion («Simule seu Storage», «Solicite uma proposta») rather than self-serve checkout.
- interface detail: s3
- tooling: S3-compatible with SigV4 presigned URLs. So it can sit behind Cloudflare the same way as any S3 store. rclone `s3`, restic, Veeam. Two-region replication inside Brazil, Tier III datacentres.
- composes with: Pure per-GB, so 5 TB and 20 TB cost the same per TB. No bucket cap below 5 PB.
- reliability: Enterprise-oriented Brazilian provider with Tier III DCs and two-region replication; no independent price/performance benchmark located. The zero-egress claim is on the vendor's own page and uncontradicted, but there is no published price list PDF to cross-check the R$0.05 number against, so confidence on the exact rate is medium even though confidence on the egress policy is high.
- notes: the same as the free tier
- extras:
  - price_verbatim: $10.19/TB/mo at both 5 TB and 20 TB (strict per-GB, no tiers), egress $0. R$0.05/GB × 1024 GB/TB × 0.199082 USD/BRL = $10.19. Note this is per decimal GB on the vendor's wording; if billed per GiB the figure is $10.96/TB.
- evidence:
  - [1] 2026-10-21: «Armazene grandes volumes por apenas R$0,05/GB»; «Sem Taxas — Zero Egress e API … a saída é gratuita, operações PUT, GET, LIST não pesam na fatura»
  - withheld 2026-10-21: same page — «suporte a buckets de até 5PB e sem necessidade de provisionamento»; «Replicação em duas regiões distintas»; «imutabilidade WORM nativa»
  - withheld 2026-10-21: search snippet — «Object Storage S3 | R$ 0,05/GB Sem Egress Fee … 50 TB | R$ 16.» (the 50 TB row was truncated in the snippet and not recoverable from the page body)
- sources:
  - [1] https://www.eveo.com.br/object-storage-s3/
