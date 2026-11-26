# BrowserCloud

> browsercloud.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/browsercloud/ | JSON https://fshy.ajam.dev/api/v1/entity/browsercloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BrowserCloud

- `compute/browsercloud` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-06T17:48:23.919Z (live) | stale on 2026-12-07
- url https://browsercloud.io/pricing
- free tier: 1 browser-hour on the free tier, against 120 hours a month on the next tier with 1,000,000 credits and 50 concurrent browsers | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no egress allowance published at https://browsercloud.io/pricing; proxy traffic is metered in credits per MB | metered: no | source: [1]
- identity: email | detail: email: signing up retains an email address and a password and nothing else ('The only information we retain, as a part of signing up, is your email address and password.'). A card is not required at sign-up: the register form at https://browsercloud.io/user/register/ asks for an email address, a password and its repeat, and a card is handled by Paddle ('Payment information is transmitted via encrypted connection to Paddle.'). A phone is not required: the privacy statement names only an email address and a password for signing up. Country: not published at https://www.browsercloud.io/privacy.
- interface: rest
- limits:
  - request-rate (binding): 1 browser-hour on Free, 120 hours a month on the next tier [1]
  - request-rate (binding): 50 concurrent browsers on the first paid tier, 100 on the second [1]
- interface detail: HTTP API (page scrape, PDF, screenshot, custom scripts); Puppeteer and Playwright over a remote browser connection; Browser Use, n8n, Make and Zapier integrations
- tooling: Puppeteer and Playwright clients, HTTP API, and Go, PHP and Python framework guides
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free tier as 1 browser-hour against 120 on the first paid tier. One hour a month is the number that decides it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: 1 browser-hour in total a month on Free; a single session cannot exceed it
  - free_tier_kind: allowance
  - burst_x: 1.0
  - net.out: yes
  - net.in: no
  - net.static_ip: no
  - net.allowance: dedicated clusters advertise no credit limits
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Browser hours 1h' on the free tier against 'Browser hours 120h' at '1,000,000 credits/month' and '3,000,000 credits/month' on the paid tiers, with 50 and 100 concurrent browsers, quoted
  - [2] 2026-11-03: the documentation index lists an HTTP API, plus Puppeteer and Playwright connections | capture: sha256:495384537ef74d841e005c0199d3289b0deabbf7e8d5a0ded0c2d90d0c13d28a | quote: [Data Scraping](https://browsercloud.io/docs/http-api/data-scraping)
  - [1] 2026-11-03: proxy traffic is metered in credits per MB; no egress allowance or overage price is stated | capture: sha256:d27e40041fb00b27e9ae175073522dbb30e45c4c638cd12d244267005463effb | quote: 1 MB Residential80 credits
  - [3] 2026-11-04: signing up collects an email address and a password and nothing else | capture: sha256:1aa821102ac03279c3566e21f6e9c37465cd95e2f62db2068185970f5aa4d9f4 | quote: The only information we retain, as a part of signing up, is your email address and password.
  - [3] 2026-11-04: a card is captured by the payment processor, not at sign-up | capture: sha256:1aa821102ac03279c3566e21f6e9c37465cd95e2f62db2068185970f5aa4d9f4 | quote: Payment information is transmitted via encrypted connection to Paddle.
  - [3] 2026-11-06: signing up collects an email address and a password and nothing else | capture: sha256:2e503fd6b9ada91c63a8e339794f2c028d04f21dee387368c3cc0b0d5e0e1ce7 | quote: The only information we retain, as a part of signing up, is your email address and password.
  - [3] 2026-11-06: a card is captured by the payment processor, not at sign-up | capture: sha256:2e503fd6b9ada91c63a8e339794f2c028d04f21dee387368c3cc0b0d5e0e1ce7 | quote: Payment information is transmitted via encrypted connection to Paddle.
  - [4] 2026-11-06: the register form asks for an email address, a password and its repeat, and no phone or card field | capture: sha256:937a0221adfe747a95ab24dd4dc6c1a800c107b78bb53d176d9c041402fa2e8c | quote: Repeat password
- sources:
  - [1] https://browsercloud.io/pricing
  - [2] https://browsercloud.io/docs
  - [3] https://www.browsercloud.io/privacy
  - [4] https://browsercloud.io/user/register/
