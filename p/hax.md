# Hax.co.id

> hax.co.id | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hax/ | JSON https://fshy.ajam.dev/api/v1/entity/hax.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hax.co.id

- `compute/hax-co-id` | qualifies-with-caveat | evidence unverified | binding retention-clamped | category cloud VM | tier Free IPv6 VPS
- needs card unknown, phone yes, ID no, institution no | verified 2026-11-06T17:42:12.762Z (live) | stale on 2026-11-21
- url https://hax.co.id/
- free tier: a free IPv6-only virtual server created from a web form, renewable to extend the server duration; no disk, RAM or CPU figure is published on the page read | unit: none | metered on: unstated | read on: 2026-10-24 | source: [1] | note: 'I understand that this VPS using IPv6' is a checkbox on the create form; the shape is not stated there
- per-object cap: not applicable
- retention: the provider wiki states 'All VPS are created for 1 week. You can extend lifetime of VPS not longer than 1 week after day of renewal'; expired servers are removed by the daily cleanup at 17:00 UTC, so a server lives 1 week from creation unless it is renewed, and a renewal keeps it no more than 1 week past the renewal day | days: 7 | source: [2] | note: an expiry-and-renew model, not a permanent account: a server is created for 1 week, a renewal keeps it no more than 1 week past the renewal day, and expired servers are removed by the daily cleanup
- egress: unmetered: 'All data centers provide Unlimited bandwidth'; no overage price applies | metered: no
- identity: any-phone | detail: any-phone: registration takes a Telegram ID and nothing else. The form carries one field, 'Telegram ID:', marked required, filled from the provider's own bot ('Send private message to @HaxTG_bot, type this command:'), and the provider's walkthrough states 'To register on the Hax.co.id site, you need a Telegram ID.' The login page states 'Please login using your telegram account'. Phone: required, because Telegram states 'Please also note that Telegram accounts can only be connected to a mobile number.' Card: not published: https://hax.co.id/register (2026-11-06) carries no card field. Country: not published: the registration page states no country restriction.
- interface: ssh
- limits:
  - retention-clamped (binding): a server is created for 1 week; a renewal keeps it no more than 1 week past the renewal day [2]
- limits note: Each VPS is provisioned for 7 days and a renewal extends it no more than a week past the renewal day, so an always-on server needs a manual renewal about weekly; the vendor wording at least 3 days before it expires is read by third-party users as a window that opens in the last 3 days, and expired servers are deleted daily at 17:00 UTC with no backup.
- binding note: the server expires 1 week after it is created and must be renewed, and a renewal keeps it no more than 1 week past the renewal day, so an always-on server needs a manual renewal about…
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: An IPv6-only box with root and 65,536 addresses per VM composes with a free IPv4-to-IPv6 front (Cloudflare Workers or a free tunnel) to become a reachable origin, and with an ssh cron job on a second free host to automate the renewal click.
- reliability: no suspension, throttle or data-loss event observed; an unrenewed server is terminated at the daily cleanup, which the provider wiki times at 17:00 UTC
- notes: The identity gate is read: registration takes a Telegram ID belonging to a Telegram account, and a Telegram account needs a mobile number, so the gate is a phone rather than an email address. The term is published on the provider's own wiki: 'All VPS are created for 1 week', and a renewal keeps the server no more than 1 week past the renewal day, so an always-on server needs a weekly renewal. The machine shape (vCPU, RAM and disk) is not published on the pages read, so the record stays at the unverified rung behind a sign-up.
- evidence note: the registration form, the login page, the provider's walkthrough and the provider's wiki were read on 2026-11-04 and fix the identity gate and the 1-week term; the machine shape was not read, and nothing is filled in from memory
- extras:
  - facets.class: perpetual-renewal-gated
  - facets.free_tier_kind: perpetual-renewable
  - shape_note: not published on the pages read
  - billing_model: free
  - term: renewable, 1-week term
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no charge stated
  - free_tier_kind: renewable
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: unknown
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: expiry by renewal, 1-week term
- evidence:
  - [3] 2026-10-22: front page advertises a free IPv6 VPS with a web panel and a renew action, quoted
  - [2] 2026-10-22: "All VPS are created for 1 week", seats are limited, and expired servers are cleaned up daily
  - [4] 2026-10-22: renewal page states "You can renew your VPS at least 3 days before it expires"; renewal needs the site address typed plus an arithmetic captcha
  - [5] 2026-10-22: third-party report of node sizes EU-1 at 1 GiB / 8 GB and US-OpenVZ-2 at 1.5 GiB / 10 GB, and a 4-day renewal cadence
  - [1] 2026-10-24: quoted: './Free IPv6 VPS — Get Virtual Servers provisioned and running in minutes' and './Renewable — Extend your server duration to keep your free server online'
  - [6] 2026-10-24: quoted form fields: 'Data Center', 'Operating System', 'Password', 'VPS Purpose', 'I understand that this VPS using IPv6', 'I agree that this VPS service is without technical support'
  - [6] 2026-11-03: bandwidth is stated as unmetered at every data center | capture: sha256:3e5c1d0402f7f3f1fc5585c903a504e3b5ef3591358e9c203522f34bfcc94634 | quote: All data centers provide Unlimited bandwidth
  - [6] 2026-11-03: the free VPS gives SSH access | capture: sha256:3e5c1d0402f7f3f1fc5585c903a504e3b5ef3591358e9c203522f34bfcc94634 | quote: Full SSH access to manage and install your application
  - [7] 2026-11-04: the registration page's only identity field is a Telegram ID, taken from the provider's own bot | capture: sha256:2fb98b110fe9b694b4e97540e3bc1ab3a092aa5856ff46c0c25dcd9cd3264ba8 | quote: Send private message to @HaxTG_bot, type this command:
  - [8] 2026-11-04: login is by Telegram account only, with no email-and-password form | capture: sha256:6628bcc84a83404fe2731b5ce9fd1e4a0e24a654457322f8980eb4b0d77db9c5 | quote: Please login using your telegram account
  - [9] 2026-11-04: the provider's own walkthrough states the Telegram ID requirement | capture: sha256:36fda1b601ede4be6195c81cc2462a768e1d27179743b11dda7c40ba7df8ae20 | quote: To register on the Hax.co.id site, you need a Telegram ID.
  - [10] 2026-11-04: a Telegram account, and so the Hax identity, requires a mobile number that receives a code | quote: Please also note that Telegram accounts can only be connected to a mobile number.
  - [7] 2026-11-04: the identity gate is a Telegram ID, so the gate is a phone and not an email address | capture: sha256:2fb98b110fe9b694b4e97540e3bc1ab3a092aa5856ff46c0c25dcd9cd3264ba8 | quote: Send private message to @HaxTG_bot, type this command:
  - [7] 2026-11-04: registration needs a Telegram ID and no email, which is the kind any-phone | capture: sha256:2fb98b110fe9b694b4e97540e3bc1ab3a092aa5856ff46c0c25dcd9cd3264ba8 | quote: Send private message to @HaxTG_bot, type this command:
  - [2] 2026-11-04: the provider wiki publishes the 1-week default term and the 1-week renewal limit | capture: sha256:bd295239ff1e1556827e58802793e9918cd43c639983b4e3142c77f528f28170 | quote: All VPS are created for 1 week. You can extend lifetime of VPS not longer than 1 week after day of renewal.
  - [2] 2026-11-04: an unrenewed server is terminated at the daily cleanup, whose stated time is 17:00 UTC | capture: sha256:bd295239ff1e1556827e58802793e9918cd43c639983b4e3142c77f528f28170 | quote: If you won’t extend your VPS lifetime, it will be terminated when cleanup at mentioned date will happen.
  - [4] 2026-11-04: the renewal window opens at least 3 days before the server expires | capture: sha256:16c6cd32c8ed70f3d050c6972aecf1e13121abc0a60936b1b3cb6eeba9ff6182 | quote: You can renew your VPS at least 3 days before it expires
  - [7] 2026-11-06: the registration form's only identity field is a Telegram ID, filled from the provider's own bot, and the form carries no email, phone, card or country field | capture: sha256:554dd95087129b12d746f53a0b8c9cb8cc8dcea44183e02d66a89ecd7d19048c | quote: Send private message to @HaxTG_bot, type this command:
- sources:
  - [1] https://hax.co.id/
  - [2] https://wiki.hax.co.id/ipv6-servers/getting-started/
  - [3] https://www.hax.co.id/
  - [4] https://hax.co.id/vps-renew/
  - [5] https://www.nodeloc.com/t/topic/40315
  - [6] https://hax.co.id/create-vps/
  - [7] https://hax.co.id/register
  - [8] https://hax.co.id/login
  - [9] https://wiki.hax.co.id/ipv6-servers/how-to-create-a-free-vps/
  - [10] https://telegram.org/faq
