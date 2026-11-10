# Hotjar

> hotjar.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hotjar/ | JSON https://fshy.ajam.dev/api/v1/entity/hotjar.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hotjar

- `dev-services/hotjar` | qualifies-with-caveat | evidence documented | binding volume-quota | category website experience analytics: session replays, heatmaps, funnels and surveys (hosted) | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://www.hotjar.com/pricing/
- free tier: Free plan at $0 forever: up to 200k monthly sessions, 1 project, 1 month of data access, replays, heatmaps and funnels, error and performance monitoring and basic surveys; session replays capture 5% of sessions up to 10k a month and the APIs are not included | unit: mixed | metered on: request-count | read on: 2026-11-01 | source: [1] | note: The allowance mixes monthly analytics sessions with a capped share of recorded replays, so no single unit of the vocabulary fits. The sign-up page of the Free plan is hosted by Contentsquare.
- per-object cap: unverified: no per-session or per-event size is stated on the pages read
- retention: 1 month of analytics data access on Free, against 13 months on Growth and above; session replays are accessible 1 month | days: 30 | source: [1]
- egress: unverified: no export allowance is stated on the pricing page; the APIs row lists Not included for Free | metered: no | source: [1]
- identity: email | detail: The sign-up page asks for a country and an email address, or Google sign-in; the pricing page states no credit card term for Free. Whether a later step asks for a card or a phone number is unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota (binding): up to 200k monthly sessions and 1 project on Free [1]
  - volume-quota (binding): session replay capture of 5% of sessions, at most 10k a month [1]
  - retention-clamped: 1 month of analytics data access and of session replay access [1]
- limits note: Free has no APIs and no alerts.
- binding note: The 5% replay sample capped at 10k a month limits what can be watched, before the 200k analytics sessions matter.
- interface detail: A tracking script feeds the web app; the pricing table lists the APIs as not included on Free and an MCP connection as up to 300 tool calls a month, and the interface vocabulary has no term for a browser-only service.
- tooling: the tracking script and the web app; an MCP connection with up to 300 tool calls a month
- composes with: Session replays, heatmaps and funnels for one free-hosted site, with analytics collected on up to 200k sessions a month and replays on a 5% sample.
- reliability: no throttle, ban or data loss is stated on the pages read beyond the 1-month data access
- evidence note: Plan limits are quoted from the first-party pricing page and the sign-up fields from the sign-up page. No account was opened, so the card term and later steps are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Free plan has 200k monthly sessions at $0 forever | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: Start seeing what your users actually do and why 200k monthly sessions $0/ forever
  - [1] 2026-11-01: the Free plan includes 1 month of data access, 1 project, replays, heatmaps and funnels, error monitoring and basic surveys | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: Free plan includes: - 1 month data access - 1 project - Replays, Heatmaps & Funnels - Error & performance monitoring - Basic surveys
  - [1] 2026-11-01: Free is up to 200k monthly sessions with 1 month of analytics data access and 1 project | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: | Monthly sessions | Up to 200k | 7k - 10m | 1m - unlimited | 1m - unlimited |
  - [1] 2026-11-01: analytics data access is 1 month on Free and 13 months on the paid plans | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: | Analytics Data Access | 1 month | 13 months | 13 months | 13 months |
  - [1] 2026-11-01: the APIs are not included on Free | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: | APIs | Not included | Not included | Included | Included |
  - [1] 2026-11-01: alerts are not included on Free | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: | Alerts | Not included | Not included | Included | Included |
  - [1] 2026-11-01: Free captures 5% of sessions as replays up to 10k a month | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: | Monthly session replay capture | 5% sessions captured (max. 10k) | 15% sessions captured (min. 20k) | Up to 100% sessions captured | Up to 100% sessions captured |
  - [1] 2026-11-01: session replay access is 1 month on Free | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: | Session Replay Access | 1 month | 2 months | 2 months, up to 24 | 3 months, up to 24 |
  - [1] 2026-11-01: the MCP connection on Free is up to 300 tool calls a month | capture: sha256:82c75412268d7295316d15b400655094b5154ac74c53447f1ff3baa1e5dd37dd | quote: | MCP | Up to 300 tool calls/month | Up to 36k tool calls/year | Up to 72k tool calls/year | Up to 108k tool calls/year |
  - [2] 2026-11-01: the sign-up page offers an email address or Google sign-in and lists countries | capture: sha256:13f2dd9ad75ade9984fb93fa793419ff5d6c6bf6b54505363910b64b29286815 | quote: Create your account Email Continue with email OR Continue with Google
- sources:
  - [1] https://www.hotjar.com/pricing/
  - [2] https://app.contentsquare.com/signup
