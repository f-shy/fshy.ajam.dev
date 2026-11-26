# Ownkube

> ownkube.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ownkube/ | JSON https://fshy.ajam.dev/api/v1/entity/ownkube.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ownkube

- `compute/ownkube` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-06T17:42:12.766Z (live) | stale on 2026-12-07
- url https://ownkube.io/pricing
- free tier: No subscription and no perpetual free allowance: the entry plan is 'USD 0 / month - No subscription, top up from USD 5 - Unused credit rolls over, never expires', and new accounts start 'with USD 5 of signup credit'. Metering, quoted: 'vCPU ~USD 0.00041 / vCPU-min', 'Memory ~USD 0.0001 / GiB-min', 'Bandwidth USD 0.02 to USD 0.13 / GB'. Reserved boxes: 'Spark 1 | 0.25 vCPU | 0.5 GiB | USD 5/mo' through 'Core 8 | 8 vCPU | 16 GiB | USD 232/mo'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-off-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'vCPU ~USD 0.00041 / vCPU-min', 'Memory ~USD 0.0001 / GiB-min', 'Bandwidth USD 0.02 to USD 0.13 / GB', quoted | metered: yes | source: [1]
- identity: email | detail: email: the only sign-in methods are a GitHub account and a Google account ('Continue with GitHubContinue with Google'), each of which needs an email address; the page carries no email-and-password form. Card: not published: https://app.ownkube.io/login (2026-11-06) carries no card field. Phone: not published: the same page states no phone requirement. Country: not published: the same page states no country restriction.
- interface: unknown
- limits:
  - volume-quota (binding): the USD 5 credit is spent by the minute at about USD 0.0246 per vCPU-hour and USD 0.006 per GiB-hour, so it buys about 203 vCPU-hours and then the account pauses. [1]
- limits note: the USD 5 credit is spent by the minute at about USD 0.0246 per vCPU-hour and USD 0.006 per GiB-hour, so it buys about 203 vCPU-hours and then the account pauses.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: prepaid credit that does not expire turns a monthly budget decision into a one-off one: USD 5 left in the wallet still runs a small app a year later, and the hourly meter means a job stopped promptly costs cents.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'Free tier: the Starter plan runs everything on one instance in your own AWS account, no credit card needed (you pay AWS for the instance)'. That description is stale. The vendor now sells its own metered compute with a prepaid wallet, and the AWS bring-your-own-account arrangement is no longer on the site. The USD 5 signup credit is the only free capacity, and it is a one-off, not a monthly grant.
- extras:
  - facets.free_tier_kind: one-off-credit
  - facets.shape.vcpu: 0.25
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: 'USD 0 / month - No subscription, top up from USD 5 - Unused credit rolls over, never expires', quoted
  - [1] 2026-10-22: 'vCPU ~USD 0.00041 / vCPU-min', 'Memory ~USD 0.0001 / GiB-min', 'Bandwidth USD 0.02 to USD 0.13 / GB', quoted
  - [1] 2026-10-22: 'Spark 1 | 0.25 vCPU | 0.5 GiB | USD 5/mo' and 'Spark 2 | 0.5 vCPU | 1 GiB | USD 10/mo', quoted
  - [2] 2026-10-22: 'Start with USD 5 of signup credit' and 'Usage draws prepaid credit, and a monthly cap can pause everything with your data kept', quoted
  - [3] 2026-11-04: the only sign-in methods are a GitHub account and a Google account | capture: sha256:1c342e36cf4c547aa313cd8046d66d47d11d3fc45523bf94a9b62b5f388c24cd | quote: Continue with GitHubContinue with Google
  - [2] 2026-11-04: the wallet is prepaid credit, which is the spending model the account gate leads to | capture: sha256:f7dde95d773261ff2230aa99446766d5d7f02fdefdec5240d4dfca9f633c1e9a | quote: Usage draws prepaid credit
  - [3] 2026-11-04: an account created through GitHub or Google, which is the email kind, is still the gate | capture: sha256:1c342e36cf4c547aa313cd8046d66d47d11d3fc45523bf94a9b62b5f388c24cd | quote: Sign in or create an account.
  - [3] 2026-11-06: the only sign-in methods are a GitHub account and a Google account, so an email address is the gate, and the page carries no card, phone or country field | capture: sha256:1c342e36cf4c547aa313cd8046d66d47d11d3fc45523bf94a9b62b5f388c24cd | quote: Continue with GitHubContinue with Google
- sources:
  - [1] https://ownkube.io/pricing
  - [2] https://ownkube.io/
  - [3] https://app.ownkube.io/login
