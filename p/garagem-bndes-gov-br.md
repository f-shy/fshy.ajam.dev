# BNDES Garagem

> garagem.bndes.gov.br | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/garagem-bndes-gov-br/ | JSON https://fshy.ajam.dev/api/v1/entity/garagem-bndes-gov-br.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BNDES Garagem

- `compute/bndes-garagem` | fails-identity | evidence inferred | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://garagem.bndes.gov.br/sobre/
- free tier: A free acceleration programme selecting 100 impact businesses per year, 400 across the third edition to 2028, split into a Criacao track for early ventures and a Tracao track for those expanding. The call carries prizes totalling BRL 915,000: BRL 64,000 to BRL 160,000 for each of five Tracao winners, BRL 32,000 to BRL 85,000 for each of five Criacao winners, and up to BRL 30,000 under a separate Mais Brasil award for the North, Northeast and periphery-economy ventures. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: prize
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The programme selects impact businesses operating against Brazilian economic, social and environmental challenges, so the applicant is an organisation with a Brazilian operation rather than a person; the specific registration document is not stated on the pages read. [1]
- limits note: The programme selects impact businesses operating against Brazilian economic, social and environmental challenges, so the applicant is an organisation with a Brazilian operation rather than a person; the specific registration document is not stated on the pages read.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: part of limits note
- composes with: The prize is the only cash in the programme; the acceleration itself is mentoring, so the value to a compute budget is the BRL 32,000 to BRL 160,000 award rather than anything the programme spends on the venture. It composes with a Brazilian cloud account only after the award, and it does not pay for compute during the cycle.
- reliability: no reliability event recorded
- notes: The verdict rests on an inference, which is why the rung is inferred rather than documented: the programme addresses 'startups de impacto' and 'negocios de impacto' without naming a registration document, so the requirement for a Brazilian entity is reasoned from the programme's Brazilian-challenge framing and the BNDES mandate, not read from the edital. It is the document that would carry the entity requirement and the eligible-expense list.
- extras:
  - facets.class: development-bank-programme
  - facets.free_tier_kind: prize
- evidence:
  - [1] 2026-10-22: 'o programa ira selecionar 100 solucoes por ano, totalizando 400 startups aceleradas', third edition running to 2028, quoted
  - [2] 2026-10-22: 'O edital preve premios que somam ate R$ 915 mil, a serem distribuidos para ate 16 negocios'; Tracao winners 'de R$ 64 mil a R$ 160 mil', Criacao winners 'de R$ 32 mil a R$ 85 mil'; 'ate R$ 30 mil em premios' under Premio BNDES Garagem Mais Brasil, quoted, BNDES news agency
  - [3] 2026-10-22: 'No total, sera distribuidos R$ 915 mil em premios, contemplando empreendimentos de todas as regioes do pais nas categorias Criacao e Tracao', quoted
  - [2] 2026-10-22: '40% das vagas serao destinadas a empreendedores das regioes Norte, Nordeste e Centro-Oeste'; previous edition drew '1.840 inscricoes', quoted
- sources:
  - [1] https://garagem.bndes.gov.br/sobre/
  - [2] https://agenciadenoticias.bndes.gov.br/bndes/Em-novo-ciclo-BNDES-Garagem-abre-inscricoes-para-selecionar-ate-100-startups-de-impacto/
  - [3] https://garagem.bndes.gov.br/tracao/
