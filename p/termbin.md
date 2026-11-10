# termbin.com

> termbin.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/termbin/ | JSON https://fshy.ajam.dev/api/v1/entity/termbin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## termbin.com

- `storage/termbin-com` | fails-quota | evidence reported | binding none | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://termbin.com
- free tier: approx. 1 MB per paste, no account, no count limit. Measured: 1,000,000 bytes stored and retrievable; 2,400,000 bytes -> connection reset. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free direct GET over HTTPS, plain text, no metering. | metered: no
- identity: anonymous
- interface: rest
- limits note: ~1 MB per paste; no expiry documented; no delete path; no listing.
- interface detail: rest
- tooling: plain TCP: `nc termbin.com 9999` returns the URL on the socket. Works with any netcat, and with bash /dev/tcp where nc is absent (used for the probes here).
- composes with: Unlimited pastes x ~1 MB. Its distinguishing property is that it needs no HTTP client and no TLS. A raw TCP sink. Useful as an out-of-band manifest/credential store, useless as a bulk tier.
- reliability: Oversized input exceeding the buffer threshold causes an immediate TCP connection reset, losing partial data without descriptive error messages. Slugs consist of random 4 to 5 character identifiers.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: approx. 1 MB per paste, no account, no count limit. Measured: 1,000,000 bytes stored and retrievable; 2,400,000 bytes -> connection reset.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'echo just testing! | nc termbin.com 9999' -> 'https://termbin.com/test'; returns a URL on the socket
  - [2] 2026-10-21: probe: printf ... >&3 to /dev/tcp/termbin.com/9999 -> ; GET -> 200
  - [3] 2026-10-21: probe: 1,000,000-byte payload -> , GET bytes=1000000; 2,400,000-byte payload -> cat: write error: Connection reset by peer
- sources:
  - [1] https://termbin.com/
  - [2] https://termbin.com/9ffz
  - [3] https://termbin.com/c609
