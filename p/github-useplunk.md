# Plunk

> github.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-useplunk/ | JSON https://fshy.ajam.dev/api/v1/entity/github-useplunk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Plunk (self-hosted)

- `email/plunk-selfhost` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category transactional sender (self-hosted)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T10:00:32.339Z (live) | stale on 2026-12-03
- url https://github.com/useplunk/plunk
- free tier: no allowance stated for self-hosted instances: https://docs.useplunk.com/concepts/billing says 'Pricing on this page applies to the hosted version at useplunk.com; self-hosted instances run on their own infrastructure' | unit: none | metered on: none | read on: 2026-10-22 | source: [1] | note: self-hosting is offered as 'Self-host for free', run on the user's own infrastructure with no per-email costs, and the software is listed as AGPL-3.0 licensed (https://www.useplunk.com/pricing)
- per-object cap: not applicable
- retention: whatever the relay and the database keep | source: [1]
- egress: the relay's terms, not the software's | metered: no | source: [1]
- identity: anonymous | detail: the software needs no account
- interface: rest
- interface detail: a self-hosted Plunk instance against your own database and relay
- tooling: docker compose, the Plunk API
- composes with: the front half of the only chain that reaches real volume, and that chain is paid: Plunk self-host in front of SES at USD 0.10 per 1,000.
- reliability: the relay bill and the deliverability belong to whoever runs the instance, not to the software
- notes: The software is free and the mail is not.
- evidence note: no probe: the application was not installed. The claim is that the software imposes no limit, which is a claim about absent code and is unmeasured
- self hosted: yes
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: the billing concepts page separates the hosted allowance from the self-hosted deployment
  - [1] 2026-11-02: the page's pricing, its free tier included, applies to the hosted version; for self-hosted instances it says only that they run on their own infrastructure, and it gives them no allowance or price | capture: sha256:9e381b3d6b2addbbeb3024fe51bb75ca935356593d90b7ea8fc68f9fe796a26b | quote: Pricing on this page applies to the hosted version at [useplunk.com](https://www.useplunk.com); self-hosted instances run on their own infrastructure.
  - [2] 2026-11-02: the vendor's pricing page offers self-hosting as 'Self-host for free' on the user's own infrastructure with no per-email costs, and lists the software as AGPL-3.0 licensed; it puts no price on the self-hosted offer | capture: sha256:5c199574f360acc9016673d6408acd08af48cc3cd43fdc763c13fd02310bbe87 | quote: AGPL-3.0 licensed. Inspect the code, self-host it, or contribute. ... Self-host for free Run Plunk on your own infrastructure — full data ownership, no per-email costs
  - [3] 2026-11-02: the repository README names the software's licence as AGPL-3.0 | capture: sha256:dd2c509e6fa126c2b2ef7684e74cbfcc37dfb13ddabfa93380d37a56984a48d7 | quote: AGPL-3.0 License - see [LICENSE](https://github.com/useplunk/plunk/blob/next/LICENSE) for details.
  - [4] 2026-11-02: the self-hosting requirements list an AWS SES account for sending emails, with Docker and Docker Compose and a domain name with subdomains for each service | capture: sha256:a51da880d5c33c896289dd0b740d72cb5081d9c230f3c230bded363951159687 | quote: Docker and Docker Compose * AWS SES account (for sending emails) * Domain name with subdomains for each service
- sources:
  - [1] https://docs.useplunk.com/concepts/billing
  - [2] https://www.useplunk.com/pricing
  - [3] https://github.com/useplunk/plunk
  - [4] https://docs.useplunk.com/self-hosting/introduction
