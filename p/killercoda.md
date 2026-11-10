# Killercoda

> killercoda.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/killercoda/ | JSON https://fshy.ajam.dev/api/v1/entity/killercoda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Killercoda (Free membership)

- `compute/killercoda-free` | qualifies-with-caveat | evidence documented | binding retention-clamped | category sandbox | tier Free membership
- needs card unknown, phone unknown, ID no, institution no | verified 2026-10-24T06:56:00.000Z (live) | stale on 2026-11-24
- url https://killercoda.com/faq
- disagrees on verdict: `compute/killercoda` says trial-only, `compute/killercoda-free` says qualifies-with-caveat
- free tier: 'You can use Killercoda completely for free!' and 'If you open any scenario then you can use it for one hour max, after which the environment of the scenario is deleted. Then you can reload your browser tab to get a new environment which you can use for one hour.' and 'There are no daily or monthly usage limits.' | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: 'Open up to 3 scenarios at the same time' is a paid-PLUS feature, so a free account holds one environment at a time
- retention: 'All environments are ephemeral, isolated from each other, and deleted once the browser tab is closed.' Nothing persists between sessions.
- egress: not published: no traffic allowance is stated in the FAQ or the pricing page. The environments are built to run labs, so outbound package installs work, but no figure is given. | metered: no | source: [1]
- identity: email | detail: no card, no phone, no document: 'Users wanting to use your scenarios will just need to register for free on Killercoda.' The FAQ adds 'Are some email domains blocked? Yes, certain email domains are blocked due to security measures', so the email must be from a domain the vendor accepts, and the list is not published.
- interface: rest
- limits:
  - retention-clamped (binding): one hour per environment, then it is deleted [1]
  - retention-clamped (binding): the environment is deleted when the browser tab closes [1]
  - per-ip-shaping: short-term rate limits on how often environments can be started, and a Captcha when many users share an IP [1]
  - write-gated: registration required; some email domains are blocked [1]
- binding note: One hour and a tab close is the whole lifetime, which is the shortest useful window among evaluated providers after Binder's ten-minute reap.
- interface detail: A browser terminal into an ephemeral Linux environment, plus a remote desktop for some scenarios. No SSH from outside and no public inbound port for user services.
- tooling: a browser; a free account
- composes with: A one-hour Linux sandbox with no card, useful for a throwaway shell or a Kubernetes exercise, and too short-lived to be a node.
- reliability: no reliability event observed. The FAQ names short-term rate limits and Captcha challenges when many users share an IP, which is a capacity control rather than an outage.
- notes: Free, no card, no phone, and renewable all day because there are no daily caps: the constraint is that each environment dies at one hour or when the tab closes. That makes it a lab bench rather than a host. Two things are unverified: the per-environment shape (no vCPU or RAM figure is published on any page read) and which email domains are blocked. The existing `killercoda` record prices it as a trial at 1 hour with a 4-hour paid tier; this record adds the no-daily-cap statement and the registration detail that the earlier one lacked.
- evidence note: The one-hour limit, the tab-close deletion, the absence of daily or monthly caps, the registration requirement and the blocked-domain policy are quoted from Killercoda's own FAQ read. The per-environment vCPU and RAM are not published anywhere read, so no shape is recorded.
- extras:
  - shape.note: not published on the FAQ or the pricing page
  - billing_model: free
  - term: per environment, one hour
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge and no payment field; ten one-hour environments a day cost nothing because there are no daily caps
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: browser terminal and remote desktop only; no public port for a user service
  - network_out.static_ip: no
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: yes
  - session_cap.note: one hour, deleted at tab close, no daily cap
  - signup_url: https://killercoda.com/
  - payment_methods: none; the free membership takes no payment
- evidence:
  - [1] 2026-10-24: quoted: 'If you open any scenario then you can use it for one hour max, after which the environment of the scenario is deleted. Then you can reload your browser tab to get a new environment which you can use for one hour. This one hour limit is raised to four hours with a paid membership. There are no daily or monthly usage limits.'
  - [1] 2026-10-24: quoted: 'All environments are ephemeral, isolated from each other, and deleted once the browser tab is closed.'
  - [1] 2026-10-24: quoted: 'To protect the platform there are short-term rate limits, for example on how often you can start environments. And if too many users connect from the same IP address there will be Captcha Bot Detection challenges shown.'
  - [1] 2026-10-24: quoted: 'Users wanting to use your scenarios will just need to register for free on Killercoda.' and 'Are some email domains blocked? Yes, certain email domains are blocked due to security measures.'
  - [2] 2026-10-24: quoted: 'Use all free scenarios as much as you want (excluding Courses)' under FREE, and 'Use scenarios for up to 4 hours instead of just one' and 'Open up to 3 scenarios at the same time' under PLUS
- sources:
  - [1] https://killercoda.com/faq
  - [2] https://killercoda.com/pricing

## Killercoda (compute/killercoda)

- `compute/killercoda` | trial-only | evidence reported | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:12.404Z (live) | stale on 2026-11-19
- url https://killercoda.com/faq/
- disagrees on verdict: `compute/killercoda` says trial-only, `compute/killercoda-free` says qualifies-with-caveat
- free tier: free scenario runs up to 1 hour; PLUS up to 4 hours and 3 concurrent environments | unit: hours | metered on: wall-clock | read on: 2026-10-06 | source: [1] | note: the 1-hour figure was right; the durable framing was not
- per-object cap: not applicable
- retention: if you open any scenario you can use it for one hour maximum, after which the environment is deleted | days: 0 | source: [1]
- egress: not published: the FAQ and the pricing page state no egress allowance and no overage price | metered: no | source: [1]
- identity: email | detail: an account; no card
- interface: unknown
- limits:
  - retention-clamped: 1 hour per scenario, then the environment is deleted [1]
  - request-rate: a browser terminal with no published inbound SSH [1]
- limits note: PLUS raises a session to 4 hours and allows 3 concurrent environments
- interface detail: a browser terminal or Theia IDE in the scenario page; no SSH endpoint, CLI or API is documented on the pages read
- tooling: a browser terminal; no SSH endpoint is published
- composes with: a lab for an hour, then deleted
- reliability: no reliability event recorded
- notes: A learning lab. The one-hour deletion is the product working as intended, not a limitation to work around.
- evidence note: re-read live on 2026-10-22 for the free-tier and limit figures
- extras:
  - billing_model: flat-pool
  - session_cap.wall_clock_min: 60
  - session_cap.restart_required: yes
  - session_cap.note: 1 h, 4 h on PLUS
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: none
  - network_out.static_ip: no
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-06: 'you can use it for one hour max, after which the environment of the scenario is deleted'
  - [1] 2026-10-22: read live: one-hour free scenario, then deletion
  - [1] 2026-11-03: the FAQ gives the cost as free and lists no egress allowance or overage price | capture: sha256:ab84bc7ca39cb210cb7d8c494c2eacdfafaa25072c324dc23a1cada618c28eec | quote: You can use Killercoda completely for free!
  - [2] 2026-11-03: the environment is reached through a browser terminal or IDE | capture: sha256:7cda02c2b441708df434a8ce4dd606196280a25a53a72a54fe88ce7e9b266122 | quote: Creators can select the Theia IDE to be shown by default instead of just a simple terminal:
- sources:
  - [1] https://killercoda.com/faq/
  - [2] https://killercoda.com/creators
