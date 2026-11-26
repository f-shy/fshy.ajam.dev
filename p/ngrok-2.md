# ngrok

> ngrok.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ngrok-2/ | JSON https://fshy.ajam.dev/api/v1/entity/ngrok-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ngrok

- `egress/ngrok-free` | fails-quota | evidence documented | binding volume-quota | category tunnel (hosted)
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T19:55:31.198Z (live) | stale on 2026-12-26
- url https://ngrok.com/docs/pricing-limits/free-plan-limits
- free tier: 1 GB out, 20,000 HTTP requests and 5,000 TCP connections per month; 3 endpoints | unit: GB | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: counted per month rather than per object
- retention: not applicable | source: [1]
- egress: metered at 1 GB/month, which is 33.3 MiB/day | metered: yes | free allowance: 1 GB/month | price per TB: USD 0.10/GB | source: [1]
- identity: email | detail: an ngrok account; TCP tunnels need a card on file
- interface: cli, rest
- limits:
  - volume-quota (binding): 1 GB per month of data transfer out; 20,000 HTTP requests, 5,000 TCP connections, 10,000 log events and 500 webhook verifications per month [1]
  - request-rate: 4,000 HTTP requests per minute and 100 TCP connections per minute, separate from the monthly quotas [1]
- limits note: 3 online endpoints, 3 concurrent agents, 1 user and 1 development domain
- binding note: 1 GB per month is about 1,100 times below 1 TiB, so the byte quota fails first by three orders of magnitude. The docs state the consequence as an upgrade recommendation rather than a throttle: once a limit is hit or the credit is gone, the endpoints stop being always available and the recommendation is to move to pay-as-you-go.
- interface detail: ngrok http; the dev domain is <name>.ngrok-free.app
- tooling: part of interface detail
- composes with: composes with an origin and no domain; the 1 GB monthly allowance is what stops it being the front of anything served.
- reliability: an interstitial page intercepts HTML browser traffic on the free tier
- notes: The record merged rate and quota into one request-rate entry. The docs separate three kinds of limit and the rate row is a distinct constraint that binds before the monthly count on a burst. Replaces the note about the vocabulary with the ratio and the documented consequence.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the agent dials out and ngrok's edge relays the bytes, which is what the 1 GB monthly counter counts
  - ingress: none
- evidence:
  - [1] 2026-10-22: Data transfer out 1 GB/month, 20,000 HTTP requests/month, 5,000 TCP connections/month, 3 endpoints and one dev domain
  - [2] 2026-10-23: 'No. ngrok supports HTTP, HTTPS, TCP, and TLS endpoints.'
  - [3] 2026-10-23: endpoints are limited to http, https, tcp and tls
  - [1] 2026-11-25: the free plan allows 3 online endpoints, 3 concurrent agents, 1 user and 1 development domain | capture: sha256:12cf55d71dac0e00e2d9b06c26f110dcc54fdd664df4bbd2758ac8bfb49f5546 | quote: | Online endpoints | Up to 3 | | Concurrent agents | 3 | | Users | 1 | | Development domains | 1 |
  - [1] 2026-11-25: the free plan allows 1 GB out, 20,000 HTTP requests and 5,000 TCP connections a month and up to 3 online endpoints | capture: sha256:12cf55d71dac0e00e2d9b06c26f110dcc54fdd664df4bbd2758ac8bfb49f5546 | quote: | Data transfer out | 1 GB / month | ... | HTTP requests | 20,000 / month | ... | TCP connections | 5,000 / month | ... | Logs & events | 10,000 / month | ... | Webhook verifications | 500 / month | ... | Online endpoints | Up to 3 |
  - [1] 2026-11-25: the free plan's monthly quotas are 1 GB out, 20,000 HTTP requests, 5,000 TCP connections, 10,000 log events and 500 webhook verifications | capture: sha256:12cf55d71dac0e00e2d9b06c26f110dcc54fdd664df4bbd2758ac8bfb49f5546 | quote: | Data transfer out | 1 GB / month | ... | HTTP requests | 20,000 / month | ... | TCP connections | 5,000 / month | ... | Logs & events | 10,000 / month | ... | Webhook verifications | 500 / month |
  - [1] 2026-11-25: the free plan's rate limits are 4,000 HTTP requests a minute and 100 TCP connections a minute | capture: sha256:12cf55d71dac0e00e2d9b06c26f110dcc54fdd664df4bbd2758ac8bfb49f5546 | quote: | HTTP request rate | 4,000 / min | | TCP connection rate | 100 / min |
  - [1] 2026-11-25: free plan data transfer out is 1 GB per month | capture: sha256:12cf55d71dac0e00e2d9b06c26f110dcc54fdd664df4bbd2758ac8bfb49f5546 | quote: | Data transfer out | 1 GB / month |
  - [4] 2026-11-25: a card must be added before TCP endpoints can be used on a free account | capture: sha256:948bfb6ac2ff07c38b57fb220cc3378ab453c087e2deec602af74fe14811beec | quote: You must add a credit or debit card before you can use TCP endpoints on a free account. We require a valid card as a way to combat abuse and keep the internet a safe place. This card will NOT be charged.
- sources:
  - [1] https://ngrok.com/docs/pricing-limits/free-plan-limits
  - [2] https://ngrok.com/compare/wireguard
  - [3] https://ngrok.com/docs/gateway/endpoints/protocols
  - [4] https://ngrok.com/docs/errors/err_ngrok_8013
