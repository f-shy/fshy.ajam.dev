# Zenifra

> zenifra.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zenifra/ | JSON https://fshy.ajam.dev/api/v1/entity/zenifra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zenifra

- `inference/zenifra` | paid-only | evidence documented | binding volume-quota | category inference gateway (Brazilian platform)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://www.zenifra.com/ia
- free tier: Nos planos, cada membro paga um preço fixo por mês e recebe uma chave de API própria, com uso renovado a cada 5 horas e toda semana. Na IA por demanda, a organização paga por milhão de tokens com o crédito, sem mensalidade. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Zenifra account and an organization API key funded by PIX or boleto; no free inference credit stated
- interface: rest
- limits:
  - volume-quota (binding): member plans from BRL 20 a month with use renewed every 5 hours and weekly; per-1M-token credit pricing otherwise [1]
- endpoint: https://ai.zenifra.com/v1
- composes with: The platform's general free cloud promotion covers apps and databases, not a free model-inference allowance.
- reliability: the API key pauses at its budget limit until the window renews, with no extra charge
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Zenifra AI charges per million tokens from organization credit or via fixed member plans, with no free inference tier | capture: sha256:d34d548b69776e732469635c1a0659c1d5406b66baca392a31b992a79880ef98 | quote: Na IA por demanda, a organização paga por milhão de tokens com o crédito, sem mensalidade.
- sources:
  - [1] https://www.zenifra.com/ia
