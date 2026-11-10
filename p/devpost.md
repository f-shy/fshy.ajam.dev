# Test Flight

> devpost.com | Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/devpost/ | JSON https://fshy.ajam.dev/api/v1/entity/devpost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DigitalOcean Gradient AI

- `compute/digitalocean-gradient-ai` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card unknown, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://digitalocean.devpost.com/
- free tier: The prize carries cloud credit alongside cash, quoted from the listing: '$ 20,000 in cash', and the prize rows '1 winner - $8,000 USD in cash - $600 in DigitalOcean credits' and '2nd Place ... $4,000 USD in cash'. Entry is a DigitalOcean signup through an MLH link, and the resources page states: 'Signup for a DigitalOcean account! - Head over to https://mlh.link/digitalocean-signup for $200 in free credits.' The event ran, quoted: 'Jan 28 - Mar 18, 2026 | Online | Public | 2592 participants'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: email: entry is 'Signup for a DigitalOcean account' through an MLH link that carries '$200 in free credits'; no other identity requirement appears on the pages read.
- interface: unknown
- limits:
  - write-gated (binding): the $200 credit is a signup promotion and the useful prize credit is $600 for one winning team out of 2,592 entrants, so the credit that is certain is small and the credit that is large is a lottery. [1]
- limits note: the $200 credit is a signup promotion and the useful prize credit is $600 for one winning team out of 2,592 entrants, so the credit that is certain is small and the credit that is large is a lottery.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The signup credit is the composable part: USD 200 at DigitalOcean's own prices buys a GPU droplet for a weekend or a small always-on instance for months, and it stacks with the MLH attendee trial because the two arrive through different links. The prize credit does not compose, because it arrives only after a win.
- reliability: no reliability event recorded
- notes: A cloud vendor sponsors a hackathon, the participants get a signup credit, and the winners get a larger credit: the recurring shape of this kind of offer. The $200 is either a genuine no-conditions credit or a trial that converts to billing at expiry; the resources page calls it 'free credits' and gives no expiry, while MLH's own attendee row calls a different offer a '60-day free trial', which suggests the two are different products.
- extras:
  - facets.class: hackathon-credit
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'The DigitalOcean Gradient(TM) AI Hackathon challenges developers, builders, and creators to design and launch new, working AI-powered applications'; 'Signup for a DigitalOcean account'; 'In Partnership with Major League Hacking'; page 200
  - [2] 2026-10-22: 'Signup for a DigitalOcean account! - Head over to https://mlh.link/digitalocean-signup for $200 in free credits'; 'Having trouble claiming credits? Head over to https://discord.mlh.io/ and open a ticket'; read through the search index for devpost.com
  - [3] 2026-10-22: MLH's 'All Attendees' prize row: '$100, 60-day free trial of DigitalOcean', '90-day extended trial of Balsamiq Cloud', '$20 worth of credits for Linode'; read through the search index for mlh.com
- sources:
  - [1] https://digitalocean.devpost.com/
  - [2] https://digitalocean.devpost.com/resources
  - [3] https://www.mlh.com/challenges/01a06f9d-f1a8-0c75-88f3-037bed6db6c4

## Global AI Hackathon

- `compute/global-ai-hackathon` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card unknown, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://qwencloud-hackathon.devpost.com/
- free tier: 'Compete for total $70,000+ in cash and cloud credits, get featured on the Qwen Cloud blog, and earn an invite to join the AI Catalyst program.' The free part, quoted: 'Get free Qwen Cloud credits to build, deploy, and scale your agent', and the entry steps, quoted: 'Register on Devpost (2 minutes)', 'Sign up for Qwen Cloud. Click here to Sign up for your free trial' (5 minutes), 'Join the Qwen Cloud Discord (2 minutes)'. Scale, quoted: '$ 45,000 in cash', '8440 participants', 'May 25 - Jul 20, 2026'. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: two accounts, both by plain signup: 'Register on Devpost (2 minutes)' and 'Sign up for Qwen Cloud. Click here to Sign up for your free trial'. No card, phone or ID document is stated, and the Qwen Cloud signup form itself was not read
- interface: unknown
- limits:
  - write-gated (binding): the token allowance per track is the binding constraint: a Showrunner track that generates video under 'a limited token budget' spends the free credit in hours, and the country exclusion list is not published on the page. [1]
- limits note: the token allowance per track is the binding constraint: a Showrunner track that generates video under 'a limited token budget' spends the free credit in hours, and the country exclusion list is not published on the page.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The composable part is not the prize but the free tier behind the hackathon: a Qwen Cloud account with credits reaches Qwen models through one interface, which is a second path to the same models earlier readings record under Alibaba and under the open-weight license. It composes with the AIMO pattern, where a token budget rather than a GPU is the unit that runs out first.
- reliability: no reliability event recorded
- notes: The origin refused the page reader (403) and the body arrived through a rendering provider, so the quotes come from a rendered read of the live page, not from the origin's own HTML. The page does not say why countries are excluded, and the excluded list lives in the rules tab, which was not read, so the record states the existence of the restriction and not its content. The event ended July 20, 2026; the series is described as recurring, which is why the record is trial-only rather than dead.
- extras:
  - facets.class: hackathon-credit
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'Compete for total $70,000+ in cash and cloud credits'; 'Get free Qwen Cloud credits to build, deploy, and scale your agent'; 'Register on Devpost (2 minutes)'; 'Sign up for Qwen Cloud'; 'This track has the highest token allowance'; page 403 at origin, body rendered through a provider
  - [1] 2026-10-22: '$ 45,000 in cash'; '8440 participants'; 'May 25 - Jul 20, 2026'; 'This hackathon has ended'; read through the search index for devpost.com
- sources:
  - [1] https://qwencloud-hackathon.devpost.com/

## Inference-Time Compute Hackathon

- `compute/inference-time-compute-hackathon` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:43:14.342Z (live) | stale on 2026-12-05
- url https://inference-time-compute.devpost.com/
- free tier: 'Participants will also receive serious compute support, including 8x H100s per team, meals, snacks, workspace for the full 24 hours, and $100 in compute credits from Prime Intellect.' Prizes, quoted: 'Teams will compete for a $50k top prize and $100k+ in total prizes.' Entry, quoted: 'Apply solo or as a pre-formed team of 2-4. Solo applicants may be matched with teammates before the event', and 'This is an in-person hackathon, and participants are expected to be present in San Francisco for the full event.' | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: no egress allowance or overage price on https://inference-time-compute.devpost.com/, read 2026-11-04 | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the clock binds first: eight H100s are attached to a 24 hour event in San Francisco, so the whole allocation is 192 H100-hours and none of it survives the weekend. [1]
- limits note: the clock binds first: eight H100s are attached to a 24 hour event in San Francisco, so the whole allocation is 192 H100-hours and none of it survives the weekend.
- binding note: the same as limits note
- interface detail: not published: the page describes an in-person event allocation and names no REST API, CLI, SSH or SDK for the compute
- tooling: not stated
- composes with: 192 H100-hours for one weekend is the densest short-lived allocation among evaluated providers, and it composes with the $100 Prime Intellect credits because those can be spent after the event on the same model code. What it does not do is leave anything behind: the event ends, the machines go back, and the project must be runnable on rented hardware afterwards.
- reliability: no reliability event recorded
- notes: Included as the clearest example of the shape that recurs across evaluated offerings: eight accelerators for a weekend, awarded to everyone who attends rather than to a winner. The arithmetic is 8 x 24 = 192 GPU-hours per team, and the event is dated by the Devpost listing rather than by a date sentence on the page, so the expiry of this instance is inferred from the listing rather than documented. Three explanations for why sponsors fund this were considered: model adoption, recruiting, and eval supply. The page names four sponsors across three track themes, which fits adoption and recruiting better than any research purpose.
- extras:
  - facets.class: hackathon-credit
  - facets.free_tier_kind: allowance
  - facets.shape.gpu_class: H100
  - facets.shape.gpu_count: 8
- evidence:
  - [1] 2026-10-22: 'Participants will also receive serious compute support, including 8x H100s per team, meals, snacks, workspace for the full 24 hours, and $100 in compute credits from Prime Intellect'; '$50k top prize and $100k+ in total prizes'; 'Apply solo or as a pre-formed team of 2-4'; 'participants are expected to be present in San Francisco for the full event'; page 200
  - [1] 2026-11-04: the page offers this and its text carries no traffic-out term, allowance or price | capture: sha256:a64c67169961b7c98809fb5de77fee4c12c61ff097ed3db441e64b51bef1be99 | quote: Participants will also receive serious compute support, including 8× H100s per team, meals, snacks, workspace for the full 24 hours, and $100 in compute credits from Prime Intellect.
- sources:
  - [1] https://inference-time-compute.devpost.com/

## Test Flight

- `compute/test-flight` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://test-flight-glasswing.devpost.com/
- free tier: 'One weekend, and $300,000 in compute credits on the line for the team that wins.' The table, quoted: 'Grand Prize 1 winner $300K in compute credits, awarded to the winning team. Compute provided by our partners. Second Place 1 winner $40K of compute credits Third Place 1 winner $15K of compute credits'. Entry, quoted: 'technical builders, individually or in teams of up to four. Solo applicants and partial teams are matched with other qualified builders. Admission is by application and reviewed on a rolling basis'; 'Free to participate'; 'Applications close September 19, 2026'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: prize
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): in-person attendance in Boston for a two-day event, admission by application, and a closed cycle: the 2026 event ran September 26 to 27 and applications closed September 19, 2026, so nothing is claimable until a next edition is announced. [1]
- limits note: in-person attendance in Boston for a two-day event, admission by application, and a closed cycle: the 2026 event ran September 26 to 27 and applications closed September 19, 2026, so nothing is claimable until a next edition is announced.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 300,000 of compute is the largest compute-denominated award documented, and it must be spent in a partner account rather than on a card: at Lambda's documented on-demand rate of USD 3.99 per H100 GPU-hour (compute/lambda) the grand prize is about 75,000 H100-hours, which is 300,000 divided by 3.99.
- reliability: no reliability event recorded
- notes: Recurrence is plausible, because a venture firm runs this as deal flow and the page is written as a recurring event, but no next date was published, so recurrence stays unverified. The failure mode is the gate rather than the money: a two-day in-person event in Boston cannot be entered from outside the United States without travel, and 'admission is by application' means the field is curated before the competition begins.
- extras:
  - facets.class: hackathon-credit
  - facets.free_tier_kind: prize
- evidence:
  - [1] 2026-10-22: '$300,000 in compute credits on the line for the team that wins'; 'Grand Prize 1 winner $300K in compute credits'; 'Second Place 1 winner $40K of compute credits'; 'Third Place 1 winner $15K of compute credits'; 'Applications close September 19, 2026'; 'Free to participate'; page 200
  - [1] 2026-10-22: 'Compute and engineering support are provided throughout the weekend, backed by AWS, Microsoft Azure, and TensorWave', quoted
- sources:
  - [1] https://test-flight-glasswing.devpost.com/
