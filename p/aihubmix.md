# AIHubMix

> aihubmix.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aihubmix/ | JSON https://fshy.ajam.dev/api/v1/entity/aihubmix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AIHubMix

- `inference/aihubmix` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.aihubmix.com/cn/blogs/free-ai-models.md
- free tier: 27+ free models at zero cost (platform-subsidised), with no credit card and no trial expiry; new users get 10 free calls each on GPT-5.5-free and GPT-Image-2-free after registration. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: registration gives 10 free calls per named free model; a card is not required to sign up
- interface: rest
- limits:
  - volume-quota (binding): 10 free calls per free model for new users; free-model pool of 27+ models, further allowance after top-up [1]
- endpoint: https://api.aihubmix.com/v1
- tooling: an OpenAI-compatible API key against the unified free-model endpoint
- composes with: the per-model 10-call new-user gift and the subsidised free pool are the scarce links
- reliability: free-model availability depends on platform subsidy and can change as models are added or removed
- evidence:
  - [1] 2026-11-18: new users receive 10 free calls each on named free models | capture: sha256:f59a9ce6c3554a2fdbb017a3cfa0c55e5769931b5dbe5399baa94ab31f3d44b1 | quote: 新用户福利：注册后，GPT-5.5、GPT-Image-2 等免费模型各赠送 10 次免费调用。充值可解锁更多额度。
- sources:
  - [1] https://docs.aihubmix.com/cn/blogs/free-ai-models.md
