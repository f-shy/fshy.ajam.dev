# Graphide

> graphide.com | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/graphide/ | JSON https://fshy.ajam.dev/api/v1/entity/graphide.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Graphide

- `ci-cd-runners/graphide` | trial-only | evidence documented | binding write-gated | category hosted GitHub Actions runner service with CI optimization agents | tier 7-day or USD 10 trial, then a fixed monthly quote
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T07:00:00.000Z (live) | stale on 2026-12-20
- url https://graphide.com/pricing/
- free tier: a 7-day or USD 10 CI usage trial with a card at checkout, nothing charged, then one fixed monthly price quoted from current usage | unit: mixed | metered on: wall-clock | read on: 2026-11-19 | source: [1]
- per-object cap: unverified: no per-object or build wall-clock cap stated in the first-party pages read | source: [1]
- retention: unverified: no number is stated in the first-party pages read | source: [1]
- egress: unverified: no egress allowance or price stated on the pricing page | metered: no | source: [1]
- identity: card | detail: a card is required at checkout for the trial; the page states one free trial per person and per card
- interface: git, browser
- limits:
  - volume-quota: trial ends at 7 days or USD 10 of CI usage, whichever comes first, or when the vendor contacts the account [1]
  - write-gated (binding): one free trial per person and per card; a card is required at checkout [1]
  - volume-quota: a fixed monthly price replaces the trial, quoted from usage; the price may change if monthly usage rises more than 60% from the starting level [1]
- binding note: a card and a vendor quote gate every account after the 7-day or USD 10 trial, so there is no standing free runner minute allowance
- interface detail: GitHub Actions jobs are routed to Graphide runners by a GitHub App; an AI agent tunes caches and machine size per job. Runs only for repositories of GitHub organizations.
- endpoint: unverified: no public API endpoint stated on the pages read
- tooling: hosted Linux runners for GitHub Actions; per-job machines destroyed when the job ends
- composes with: a GitHub Actions workflow on a Graphide runner label runs on a per-job machine, with the vendor's agents tuning caches and test splits
- reliability: 
- notes: A hosted GitHub Actions runner service with agent-driven CI tuning. The trial is metered by time and dollars and ends after 7 days or USD 10; the ongoing price is a quote, not a published rate.
- evidence note: all values are quoted from the first-party pricing page read on 2026-11-19. Build concurrency, retention and egress are unverified: the page publishes no numbers for them. The speed claims are the vendor's and are not measured here.
- evidence:
  - [1] 2026-11-19: the trial lasts 7 days or USD 10 with a card at checkout | capture: sha256:bc5f37bf54dd4b66eba5d3f2ef0cee067aa90e0ff31bfeb7b3a7ff611cc41a88 | quote: Put in a card at checkout; nothing is charged. The trial lasts 7 days or $10 of CI usage, whichever comes first, or until we contact you.
  - [1] 2026-11-19: a fixed monthly quote follows the trial | capture: sha256:bc5f37bf54dd4b66eba5d3f2ef0cee067aa90e0ff31bfeb7b3a7ff611cc41a88 | quote: Graphide CI is a service, not a plan to pick. You get our runners, plus a team of AI agents that tunes each job and keeps it fast as your code changes. You pay one fixed monthly price, which we quote from what you run today.
- sources:
  - [1] https://graphide.com/pricing/
