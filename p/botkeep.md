# Botkeep

> botkeep.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/botkeep/ | JSON https://fshy.ajam.dev/api/v1/entity/botkeep.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Botkeep

- `compute/botkeep` | qualifies-with-caveat | evidence documented | binding retention-clamped | category platform host
- needs card no, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://botkeep.cloud/
- free tier: A perpetual free container that runs 24/7 with no renewal timer: quoted 'Standard Free includes one server, 512 MB RAM, 50% CPU and 1 GB persistent storage, running 24/7', and 'The free plan does not require periodic manual renewal'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: An inactivity rule that the plan pages do not quantify may remove idle servers, so the stated no-renewal design is a commitment and not a measured absence of a reaper; capacity at signup is also explicitly not guaranteed. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an account is required and the free plan 'is for new signups', with the terms allowing 'up to two server slots per account'. What the account requires is not quoted in any evidence row: no email, phone, card or ID requirement is stated, and the email kind is inferred from an account-based signup rather than read. The record's notes assert there is no card. No hold, debit or prepaid term is stated.
- interface: unknown
- limits:
  - retention-clamped (binding): An inactivity rule that the plan pages do not quantify may remove idle servers, so the stated no-renewal design is a commitment and not a measured absence of a reaper; capacity at signup is also explicitly not guaranteed. [1]
- limits note: An inactivity rule that the plan pages do not quantify may remove idle servers, so the stated no-renewal design is a commitment and not a measured absence of a reaper; capacity at signup is also explicitly not guaranteed.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A container with a public HTTPS URL that never sleeps is the piece earlier T3 rows lack: it can hold an inbound webhook for an Oracle or GCP box, or run the poller that keeps a pubnix account from being disabled.
- reliability: no reliability event recorded
- notes: One, whether a real deployment survives 30 days without a request; the panel markets 'zero required renewals' and the terms permit inactivity rules in the same breath. Two, whether free slots are actually available, because the page says 'Deployment is subject to available capacity'. The service is four months old, has 15 runtime nodes in four European countries, and the Founder Free offer ran 2026-10-01 to 2026-10-15, which is evidence of an active operator rather than a dormant page. A Halloween Free 3-month plan is announced to start 2026-10-24 and is not active as read. Language: the inactivity answer exists only on the Spanish locale of the home page, which is why an English-only read of this vendor misses the reaper field.
- extras:
  - facets.class: paas-never-sleep
  - facets.free_tier_kind: perpetual
  - facets.shape.vcpu: 0.5
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 1
- evidence:
  - [1] 2026-10-22: probed 200, 73590 bytes, sha256 998e3d54d2ecfa1936f5f7161bad3b20e00adda65863edb70313b3ec81e6af8d; page states '512 MB RAM, 50% CPU and 1 GB storage for your app, bot or website. No periodic manual renewal' and 'Runtime 24/7 continuous, Manual renewals 0 required', quoted
  - [2] 2026-10-22: 'Standard Free includes one server, 512 MB RAM, 50% CPU and 1 GB persistent storage, running 24/7. It is for new signups.' quoted
  - [3] 2026-10-22: 'Do I need to renew a free server every few days? No. Botkeep's Free plan is designed without a periodic manual renewal timer.' quoted; the same FAQ describes CPU as shared, not dedicated
  - [4] 2026-10-22: the Spanish locale answers the inactivity question directly: 'El modelo Botkeep no prev suspensi n programada por inactividad. El entorno est dise ado para la ejecuci n continua.' quoted, and contrasts it with 'Las cargas inactivas pueden pausarse, suspenderse o necesitar un mecanismo externo de keep-alive'
  - [5] 2026-10-22: section 5 states the free entitlement 'has no recurring price or scheduled expiry' and 'Free slots are intended for continuous operation without a periodic manual server-renewal requirement', then reserves 'reasonable queues, inactivity rules, build limits, network restrictions, log limits and fair-use controls'; section 14 allows suspension for 'prolonged inactivity', quoted
  - [5] 2026-10-22: the English plan page gives one server while the terms say 'up to two server slots per account with total account budgets of 1 GB RAM, 1 vCore (100% CPU) and 1 GB storage', so the 512 MB page figure is half the pooled account budget
- sources:
  - [1] https://botkeep.cloud/
  - [2] https://botkeep.cloud/free-discord-bot-hosting
  - [3] https://botkeep.cloud/faq
  - [4] https://botkeep.cloud/es/
  - [5] https://botkeep.cloud/terms
