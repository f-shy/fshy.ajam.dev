# Obscura

> obscura.com | Egress and tunnels, IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/obscura/ | JSON https://fshy.ajam.dev/api/v1/entity/obscura.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Obscura (Egress and tunnels)

- `egress/obscura` | paid-only | evidence documented | binding none | category vpn tunnel (hosted subscription) | tier monthly
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:11:45.779Z (live) | stale on 2026-12-05
- url https://obscura.com/pricing
- price USD 8.00 per month; no yearly plan; a subscription price, not a per-TB price | parsed USD 8/mo
- free tier: No free plan and no yearly plan. The pricing page lists one price, '$8.00/ month', and the FAQ says 'Obscura is just $8/month.' Subscriptions renew monthly by card; time can also be added by top-up with a card, Bitcoin Lightning or Monero. A promotion site (nonordnovember.com) gives everyone 7 days free; up to 2 years of credit based on another VPN's plan is unlocked only with at least a 1-month purchase. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: No 12-month price exists on the pages read, so the yearly cost is 12 monthly payments: the monthly price times 12. Subscriptions 'charge your credit card monthly'; a top-up is 'a one-time payment that adds time to your account'. The top-up page's per-period prices are behind the account and were not read.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a tunnel, not stored bytes | source: [1]
- egress: No byte cap is stated on the pages read. The plan lists '5 simultaneous connections, unlimited devices' and 'Connections to 33+ countries'. Exit hops are run by Mullvad: 'a fully-independent exit hop (currently Mullvad)'. | metered: no | free allowance: none: no free plan | source: [1]
- identity: anonymous | detail: 'Log in with just a randomized account number. No names, no emails, no phone numbers necessary.' The signup page says 'All you need is an account number and payment'. Card subscriptions run through Stripe, which 'may need your email for subscriptions, but Obscura never stores it'; Bitcoin Lightning and Monero are accepted for top-ups only, not subscriptions.
- interface: unknown
- limits:
  - per-ip-shaping: the exit addresses are Mullvad's ('a fully-independent exit hop (currently Mullvad)'), shared by that provider's customers, so reputation and limits on an address apply to everyone behind… [1]
  - request-rate: 5 simultaneous connection slots per account; each WireGuard config holds 1 slot even when idle [1]
- limits note: The slot count is filed under request-rate because the vocabulary has no concurrent-connection kind.
- binding note: No byte quota, speed cap or request rate is published; the stated ceiling is 5 connection slots, which the limit vocabulary cannot name.
- interface detail: A tunnel through native apps, plus WireGuard configs generated in the account. Protocols: a two-party relay that carries WireGuard over QUIC (the vendor's wording: 'WireGuard-over-QUIC'), and plain WireGuard configs. UDP: the QUIC tunnel is UDP-based by default, with a TCP/TLS tunnel option in the app's Experimental settings. Port forwarding: unverified: no page read states it. SOCKS5: unverified: no page read states a SOCKS5 endpoint. Obfuscation: the QUIC 'stealth protocol' blends in with HTTP/3 traffic; the WireGuard-config mode does not have it. BitTorrent: unverified: no page read states a rule.
- tooling: The vendor's native apps (macOS, iOS, Android, Windows, Linux; source on GitHub), or any WireGuard client with a config generated in the account. Each config holds one of the account's 5 connection slots for as long as it exists.
- composes with: A tunnel exit in two hops: a vendor relay that sees the connecting address but cannot decrypt traffic, then a Mullvad exit; the upstream sees a Mullvad exit address.
- reliability: The first hop is the vendor's own relay and the exit is Mullvad's, so an outage at either ends the tunnel; the vendor's fallback when UDP is blocked is the TCP/TLS tunnel setting, which 'may reduce performance'.
- notes: Cheapest yearly price: no yearly plan is offered on the pages read; the only price is USD 8 a month. The product is a front end to Mullvad's exits (see the Mullvad record for that provider's own terms).
- evidence note: Documented: price, protocol, UDP/TCP fallback, sign-up gate and exit provider are quoted from the vendor's pages. Nothing was connected through the service. Port forwarding, SOCKS5 and the BitTorrent rule are unverified because no page read states them.
- evidence:
  - [1] 2026-11-04: The only price on the pricing page is USD 8.00 a month. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: $8.00/ month
  - [1] 2026-11-04: The FAQ gives the same single monthly price. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Obscura is just $8/month.
  - [1] 2026-11-04: Connection slots per account are 5. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: 5 simultaneous connections, unlimited devices
  - [1] 2026-11-04: No email or phone is needed to log in. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Log in with just a randomized account number. No names, no emails, no phone numbers necessary.
  - [2] 2026-11-04: The signup page needs an account number and payment only. | capture: sha256:3e72b7e6174f12350f14ead0cfda5063a8da5a80fbccfd2b0deaea278c2f37d5 | quote: All you need is an account number and payment - thatâ€™s it.
  - [1] 2026-11-04: The exit hop is Mullvad's. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Obscura solves this by using a fully-independent exit hop (currently Mullvad).
  - [1] 2026-11-04: Obfuscation: QUIC stealth protocol. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Our unique stealth protocol is designed to blend in with regular internet traffic.
  - [1] 2026-11-04: The plain WireGuard config mode has no obfuscation. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Note that since this uses the original WireGuard protocol, you wonâ€™t benefit from Obscuraâ€™s QUIC-based obfuscation for outsmarting internet censorship.
  - [3] 2026-11-04: A TCP/TLS tunnel option exists. | capture: sha256:8f189680bc753754538a0b0c8857f312ed6682668a509ca7a769d79bd5de3fb5 | quote: Switching to a TCP/TLS tunnel routes the tunnel over TCP instead, which most networks allow.
  - [4] 2026-11-04: The trial is 7 days for everyone. | capture: sha256:340ba07815f04435a2bcb3ec1562497d55420c1b79cf91200304cbc2a873961b | quote: Everyone gets 7 days free and is eligible for credit after submitting.
  - [4] 2026-11-04: The credit of up to 2 years needs at least a 1-month purchase. | capture: sha256:340ba07815f04435a2bcb3ec1562497d55420c1b79cf91200304cbc2a873961b | quote: Felix will give you up to 2 years of Obscura VPN credit which you can unlock with at least a 1-month purchase.
- sources:
  - [1] https://obscura.com/pricing
  - [2] https://obscura.com/signup/
  - [3] https://obscura.com/knowledge/troubleshooting-connection-issues/
  - [4] https://nonordnovember.com/

## Obscura (IP and proxies)

- `ip-proxy/obscura` | paid-only | evidence documented | binding none | category VPN subscription (exit source) | tier monthly
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:58:00.000Z (live) | stale on 2026-12-05
- url https://obscura.com/pricing
- price USD 8.00 per month; no yearly plan; a subscription price, not a per-TB price | parsed USD 8/mo
- duplicate of `egress/obscura`
- free tier: No free plan and no yearly plan. The pricing page lists one price, '$8.00/ month', and the FAQ says 'Obscura is just $8/month.' Subscriptions renew monthly by card; time can also be added by top-up with a card, Bitcoin Lightning or Monero. A promotion on the home page ('No Nord November') gives everyone a 7-day free trial; up to 2 years of credit based on another VPN's plan is unlocked only with at least a 1-month purchase. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: No 12-month price exists on the pages read, so the yearly cost is 12 monthly payments: the monthly price times 12. Subscriptions 'charge your credit card monthly'; a top-up is 'a one-time payment that adds time to your account'. The top-up page's per-period prices are behind the account and were not read.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a tunnel, not stored bytes | source: [1]
- egress: No byte cap is stated on the pages read. The plan lists '5 simultaneous connections, unlimited devices' and 'Connections to 33+ countries'. Exit hops are run by Mullvad: 'a fully-independent exit hop (currently Mullvad)'. | metered: no | free allowance: none: no free plan | source: [1]
- identity: anonymous | detail: 'Log in with just a randomized account number. No names, no emails, no phone numbers necessary.' The signup page says 'All you need is an account number and payment'. Card subscriptions run through Stripe, which 'may need your email for subscriptions, but Obscura never stores it'; Bitcoin Lightning and Monero are accepted for top-ups only, not subscriptions.
- interface: unknown
- limits:
  - per-ip-shaping: the exit addresses are Mullvad's ('Exit servers (run by Mullvad)'), shared by that provider's customers, so reputation and limits on an address apply to everyone behind it [2]
  - request-rate: 5 simultaneous connection slots per account; each WireGuard config holds 1 slot even when idle [1]
- limits note: The slot count is filed under request-rate because the vocabulary has no concurrent-connection kind. Account-number loss cannot be recovered ('there is no way to recover it').
- binding note: No byte quota, speed cap or request rate is published; the stated ceiling is 5 connection slots, which the limit vocabulary cannot name.
- interface detail: A tunnel through native apps, plus WireGuard configs generated in the account. Protocols: a two-party relay that carries WireGuard over QUIC (the vendor's wording: 'WireGuard-over-QUIC'), and plain WireGuard configs. UDP: the QUIC tunnel is UDP-based by default, with a TCP/TLS tunnel option in the app's Experimental settings. Port forwarding: unverified: no page read states it. SOCKS5: unverified: no page read states a SOCKS5 endpoint. Obfuscation: the QUIC 'stealth protocol' blends in with HTTP/3 traffic; the WireGuard-config mode does not have it. BitTorrent: unverified: no page read states a rule.
- tooling: The vendor's native apps (macOS, iOS, Android, Windows, Linux; source on GitHub), or any WireGuard client with a config generated in the account. Each config holds one of the account's 5 connection slots for as long as it exists.
- composes with: A tunnel exit in two hops: a vendor relay that sees the connecting address but cannot decrypt traffic, then a Mullvad exit; the upstream sees a Mullvad exit address.
- reliability: The first hop is the vendor's own relay and the exit is Mullvad's, so an outage at either ends the tunnel; the vendor's fallback when UDP is blocked is the TCP/TLS tunnel setting, which 'may reduce performance'.
- notes: Duplicate of egress/obscura, which holds the offer; both records cite the same vendor page.
- evidence note: Documented: price, protocol, UDP/TCP fallback, sign-up gate and exit provider are quoted from the vendor's pages. Nothing was connected through the service. Port forwarding, SOCKS5 and the BitTorrent rule are unverified because no page read states them.
- evidence:
  - [1] 2026-11-04: The only price on the pricing page is USD 8.00 a month. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: $8.00/ month
  - [1] 2026-11-04: The FAQ gives the same single monthly price. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Obscura is just $8/month.
  - [1] 2026-11-04: Connection slots per account are 5. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: 5 simultaneous connections, unlimited devices
  - [1] 2026-11-04: No email or phone is needed to log in. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Log in with just a randomized account number. No names, no emails, no phone numbers necessary.
  - [3] 2026-11-04: The signup page needs an account number and payment only. | capture: sha256:3e72b7e6174f12350f14ead0cfda5063a8da5a80fbccfd2b0deaea278c2f37d5 | quote: All you need is an account number and payment - that’s it.
  - [1] 2026-11-04: The tunnel is WireGuard over QUIC, with Mullvad exits. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Obscura’s servers relay the WireGuard tunnel between your device and Mullvad’s servers. Essentially, WireGuard-over-QUIC.
  - [1] 2026-11-04: The exit hop is Mullvad's. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Obscura solves this by using a fully-independent exit hop (currently Mullvad).
  - [1] 2026-11-04: Obfuscation: QUIC stealth protocol. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Our unique stealth protocol is designed to blend in with regular internet traffic.
  - [1] 2026-11-04: The plain WireGuard config mode has no obfuscation. | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Note that since this uses the original WireGuard protocol, you won’t benefit from Obscura’s QUIC-based obfuscation for outsmarting internet censorship.
  - [4] 2026-11-04: The default transport is UDP. | capture: sha256:8f189680bc753754538a0b0c8857f312ed6682668a509ca7a769d79bd5de3fb5 | quote: Obscura’s tunnel uses QUIC (which is UDP-based) by default.
  - [4] 2026-11-04: A TCP/TLS tunnel option exists. | capture: sha256:8f189680bc753754538a0b0c8857f312ed6682668a509ca7a769d79bd5de3fb5 | quote: Switching to a TCP/TLS tunnel routes the tunnel over TCP instead, which most networks allow.
  - [5] 2026-11-04: Crypto is for top-ups only; subscriptions are card. | capture: sha256:13168a3c827ed65356369ab43b900714f54cd5c63592bbab5862c557e7594a85 | quote: Cryptocurrency payments aren’t supported for subscriptions.
  - [6] 2026-11-04: The trial is 7 days for everyone. | capture: sha256:340ba07815f04435a2bcb3ec1562497d55420c1b79cf91200304cbc2a873961b | quote: Everyone gets 7 days free and is eligible for credit after submitting.
  - [6] 2026-11-04: The credit of up to 2 years needs at least a 1-month purchase. | capture: sha256:340ba07815f04435a2bcb3ec1562497d55420c1b79cf91200304cbc2a873961b | quote: Felix will give you up to 2 years of Obscura VPN credit which you can unlock with at least a 1-month purchase.
  - [1] 2026-11-04: the Obscura pricing page states the one price both records describe | capture: sha256:3115ee6264f42cb88dbb5241b226cf35ec97c0a6dcf8dc6cfada0b45cca0df8c | quote: Obscura is just $8/month.
- sources:
  - [1] https://obscura.com/pricing
  - [2] https://obscura.net/
  - [3] https://obscura.com/signup/
  - [4] https://obscura.com/knowledge/troubleshooting-connection-issues/
  - [5] https://obscura.com/knowledge/payments/
  - [6] https://nonordnovember.com/
