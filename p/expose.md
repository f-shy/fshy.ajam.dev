# Expose

> expose.dev | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/expose/ | JSON https://fshy.ajam.dev/api/v1/entity/expose.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Expose (expose.dev managed service), Hobby

- `egress/expose-dev-hobby` | qualifies-with-caveat | evidence documented | binding none | category tunnel (hosted): HTTP/HTTPS tunnel to a localhost web service on a managed free server in Germany | tier Hobby
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:36:40.149Z (live) | stale on 2026-12-04
- url https://expose.dev/
- price free; no per-byte price published
- disagrees on verdict: `egress/expose-dev-hobby` says qualifies-with-caveat, `egress/expose-dev-pro` says paid-only
- free tier: Free: TLS/SSL encryption, a time limit on every connection, random URLs, a single EU server; no card required | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: The pages read name a time limit per connection but publish no duration and no byte figure.
- per-object cap: not applicable: a stream
- retention: a random subdomain on every connect; the connection is time-limited | source: [2] | note: no duration is published on the pages read
- egress: no byte cap or transfer tolerance is published on the home page or the documentation pages read; the free plan has a per-connection time limit with no stated duration | metered: no | free allowance: none published | source: [1]
- identity: email | detail: a free account with full name, email address and password, or sign-in with GitHub or Google; an hCaptcha challenge is on the form; no card for the Hobby tier
- interface: cli
- limits:
  - per-ip-shaping: free plan: a time limit on every connection, a randomized tunnel name for each connection and one server in Germany; no duration and no byte figure is published [2]
- limits note: The only published limit is a time limit with no number.
- binding note: Nothing countable is published: the free plan states a per-connection time limit without a duration and no byte cap, so no quota can be shown to fail first at 1 TiB per month. The tolerance is unpublished.
- interface detail: expose share http://localhost:3000; a web dashboard shows and replays the requests
- tooling: a PHP client (PHAR archive or Composer package, bundled in Laravel Herd) logs in to the managed server with an account token
- composes with: HTTP and HTTPS only on the pages read, so it fronts a web origin and is not a UDP forward or a WireGuard ingress. The open source PHP server can be run by the user on a rented or free machine as the last option.
- reliability: The free server is one data center in Germany; a connection is cut by the time limit and then gets a new random URL.
- notes: Managed lane of an MIT-licensed PHP tunnel (github.com/exposedev/expose). /pricing answers 404 and the plan table is on the home page. The byte cap is not published on any page read.
- evidence note: Home page, authentication page and registration page read on 2026-11-03; no limit figure is published, so the byte tolerance is unverified.
- extras:
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the tunnel relays the bytes of the origin
  - volume_stated: not published on the pages read
- evidence:
  - [1] 2026-11-03: the Hobby tier is free and needs no card | capture: sha256:c3f6df0f58aab07e12548866ad2f6fc99838725fa50a2290ae605d6bd70f60cf | quote: Hobby Get up and running with a free account. No card required.
  - [2] 2026-11-03: the free plan is on one server in Germany, uses random tunnel names and has a time limit on every connection, with no duration stated | capture: sha256:39952474953bdf6e5c53781d6e370f18824e6279bc6b98df62aa2a55c291339e | quote: The network comes with a free plan that is limited to the free server in our data center in Germany, uses randomized tunnel names for every connection and has a time limit for every connection.
  - [2] 2026-11-03: sign-in is by email, GitHub or Google | capture: sha256:39952474953bdf6e5c53781d6e370f18824e6279bc6b98df62aa2a55c291339e | quote: Expose opens your browser, where you sign in with your email address, GitHub or Google.
  - [3] 2026-11-03: the traffic shared is HTTP and HTTPS | capture: sha256:e585d74bcc0bcf4d80e13a7623deabc419be4f822c41b1b89d7ec5e066b65124 | quote: Expose allows you to share any kind of HTTP/HTTPS traffic for websites that you can reach on your own computer, with anyone on the internet and there are multiple ways to share a site with Expose.
  - [4] 2026-11-03: the registration form asks for full name, email address and password | capture: sha256:db3399aeb7e00ee5f1eebc3f842012fe5f6cf40af6df5f83e22c6616dc1aa121 | quote: Full name
  - [2] 2026-11-03: the free plan runs on one server in Germany, with random tunnel names and a per-connection time limit that the page gives no number for | capture: sha256:39952474953bdf6e5c53781d6e370f18824e6279bc6b98df62aa2a55c291339e | quote: The network comes with a free plan that is limited to the free server in our data center in Germany, uses randomized tunnel names for every connection and has a time limit for every connection.
  - [1] 2026-11-03: the Hobby plan needs a free account and no card | capture: sha256:c3f6df0f58aab07e12548866ad2f6fc99838725fa50a2290ae605d6bd70f60cf | quote: Get up and running with a free account. No card required.
  - [2] 2026-11-03: sign-in is by email address, GitHub or Google | capture: sha256:39952474953bdf6e5c53781d6e370f18824e6279bc6b98df62aa2a55c291339e | quote: Expose opens your browser, where you sign in with your email address, GitHub or Google.
  - [5] 2026-11-03: sharing a TCP port is marked as a Pro feature, so the free plan carries HTTP and HTTPS only | capture: sha256:616ed6ea1fcff99d199ac3045ab7603844fb0aff5bfd27c3787776eceeca9c16 | quote: # Sharing TCP Ports ::pro
  - [3] 2026-11-03: a user shares HTTP and HTTPS traffic | capture: sha256:e585d74bcc0bcf4d80e13a7623deabc419be4f822c41b1b89d7ec5e066b65124 | quote: Expose allows you to share any kind of HTTP/HTTPS traffic for websites that you can reach on your own computer, with anyone on the internet and there are multiple ways to share a site with Expose.
  - [6] 2026-11-03: the free server accepts client connections on port 443 | capture: sha256:18290eced5171230df5fde73b7a2371e99e9387fc0db9da470845a159ee591e6 | quote: The free default server is already running on port 443.
  - [7] 2026-11-03: the managed network is a separate proprietary service from the MIT-licensed PHP core that the self-hosted record covers | capture: sha256:1a628f30a04bd5a93d10a4800f0553137d35e5357131a6280baebdcc426c5954 | quote: The managed platform itself is proprietary.
- sources:
  - [1] https://expose.dev/
  - [2] https://expose.dev/docs/getting-started/authentication
  - [3] https://expose.dev/docs/client/sharing
  - [4] https://expose.dev/register
  - [5] https://github.com/exposedev/expose/blob/master/docs/client/sharing-tcp-ports.md
  - [6] https://expose.dev/docs/server/server/starting-the-server
  - [7] https://faun.dev/toolbox/expose/

## Expose (expose.dev managed service), Pro

- `egress/expose-dev-pro` | paid-only | evidence documented | binding none | category tunnel (hosted): HTTP/HTTPS tunnel with reserved subdomains, custom domains and a global server network, USD 79 per user per year | tier Pro
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:36:40.149Z (live) | stale on 2026-12-04
- url https://expose.dev/
- price USD 79 per user per year
- disagrees on verdict: `egress/expose-dev-hobby` says qualifies-with-caveat, `egress/expose-dev-pro` says paid-only
- free tier: no free allowance on this tier; Pro is USD 79 per user per year, with no time limit | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: a stream
- retention: persistent URLs and reserved subdomains; no time limit | source: [1]
- egress: no byte cap or transfer tolerance is published on the home page or the documentation pages read; Pro has no time limit | metered: no | free allowance: none | source: [1]
- identity: email | detail: an account with full name, email address and password, or sign-in with GitHub or Google; the plan cards say no card is needed to get started, and the checkout was not opened
- interface: cli
- limits:
  - volume-quota: no byte cap and no bandwidth tolerance is published for Pro [1]
- limits note: Nothing countable is published for the paid tier either.
- binding note: Nothing countable is published: Pro states no time limit and no byte cap, so no quota can be shown to fail first at 1 TiB per month. The tolerance is unpublished.
- interface detail: expose share http://localhost:3000; a web dashboard shows and replays the requests
- tooling: a PHP client (PHAR archive or Composer package, bundled in Laravel Herd) logs in to the managed server with an account token
- composes with: HTTP and HTTPS only on the pages read, so it fronts a web origin and is not a UDP forward or a WireGuard ingress. The open source PHP server can be run by the user on a rented or free machine as the last option.
- reliability: Pro uses the nearest server of a global network; the price is net of local taxes and VAT.
- notes: Team is USD 229 per team per year for up to 10 users. Paid-tier counterpart of the Hobby record; the home page publishes no byte cap for it.
- evidence note: Home page pricing cards read on 2026-11-03; the checkout was not opened, so the payment method is unverified.
- extras:
  - ingress: http-only
  - bytes_transit: yes
  - transit_note: the tunnel relays the bytes of the origin
  - volume_stated: not published on the pages read
- evidence:
  - [1] 2026-11-03: the Pro tier costs USD 79 per user per year | capture: sha256:c3f6df0f58aab07e12548866ad2f6fc99838725fa50a2290ae605d6bd70f60cf | quote: $79 per user per year*
  - [1] 2026-11-03: Pro includes the global server network | capture: sha256:c3f6df0f58aab07e12548866ad2f6fc99838725fa50a2290ae605d6bd70f60cf | quote: Global server network
  - [2] 2026-11-03: sign-in is by email, GitHub or Google | capture: sha256:39952474953bdf6e5c53781d6e370f18824e6279bc6b98df62aa2a55c291339e | quote: Expose opens your browser, where you sign in with your email address, GitHub or Google.
  - [3] 2026-11-03: the traffic shared is HTTP and HTTPS | capture: sha256:e585d74bcc0bcf4d80e13a7623deabc419be4f822c41b1b89d7ec5e066b65124 | quote: Expose allows you to share any kind of HTTP/HTTPS traffic for websites that you can reach on your own computer, with anyone on the internet and there are multiple ways to share a site with Expose.
- sources:
  - [1] https://expose.dev/
  - [2] https://expose.dev/docs/getting-started/authentication
  - [3] https://expose.dev/docs/client/sharing
