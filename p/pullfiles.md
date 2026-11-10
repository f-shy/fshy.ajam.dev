# PullFiles

> pullfiles.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pullfiles/ | JSON https://fshy.ajam.dev/api/v1/entity/pullfiles.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PullFiles

- `debrid/pullfiles` | qualifies-with-caveat | evidence documented | binding per-object-cap | category URL-to-browser relay (server fetches a direct link, user downloads the stream) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:32.907Z (live) | stale on 2026-12-04
- url https://pullfiles.net/
- price USD 0
- free tier: 'Grab any file from a link or URL instantly with our fast and easy online downloader. Max. File size: 1 GB.' The page advertises 'Unlimited Downloads - No restrictions on download frequency or usage' and requires no account in the visible flow. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1] | note: The client sends a URL, their server pulls it, and the browser receives the stream. Nothing is stored for later re-download.
- per-object cap: 1 GB per file ('Max. File size: 1 GB'). | bytes: 1073741824 | source: [1]
- retention: not applicable in the storage sense: there is a progress screen ('Preparing download... Downloading Secure Server') and no library. Nothing was found that says a fetched file persists. | days: 0 | source: [1]
- egress: 'Unlimited Downloads - No restrictions on download frequency or usage'; no byte allowance stated. | metered: no | free allowance: no published allowance monthly; 1 GB per file | source: [1]
- identity: anonymous | detail: No login or account appears anywhere in the pasted-URL flow.
- interface: unknown
- limits:
  - per-object-cap (binding): 1 GB per file [1]
  - request-rate: claimed unlimited ('No restrictions on download frequency or usage'); untested [1]
- limits note: The page also says '100% Secure' and 'End-to-end encryption', which cannot be true of a relay that terminates TLS on both sides; treat the security text as marketing.
- binding note: The 1 GB per-file ceiling is the only hard number: 1 TiB/month is 1024 such files, so frequency is not the wall, the single-file size is.
- interface detail: One web form: paste a direct file URL, press start, watch a progress panel. No API documentation.
- tooling: Browser only. A wrapper would need a headless browser because the transfer is streamed through the page.
- composes with: It solves the case where the local connection cannot reach a host but the relay can: the relay fetches and re-serves over HTTPS. It is a proxy, not storage, so it must be followed immediately by a real download.
- reliability: A relay is a single point of failure and a single point of visibility: the operator sees every URL and every byte, and the stream dies if the operator's egress is slow. Nothing on the page states uptime or operator identity.
- notes: Answers a narrower question than the sector asked: it will not resolve a Rapidgator page into a direct link, but it will fetch a direct link that is otherwise unreachable. Worth keeping as the last hop.
- evidence note: The page, its FAQ and its features page are captured and quoted: 1 GB per file, unlimited downloads, no registration. No URL was pulled through the relay, so neither the 1 GB ceiling nor the unlimited claim is measured.
- extras:
  - max_file_bytes: 1073741824
  - account: none
  - api: none
- evidence:
  - [1] 2026-10-23: 'Max. File size: 1 GB', 'Unlimited Downloads - No restrictions on download frequency or usage', the progress UI ('Preparing download...') and no account requirement
  - probe:https://pullfiles.net/ 2026-10-23: HTTP 200, 65612 bytes, sha256 0f299b37f44aadf7..., no challenge
  - [1] 2026-11-03: the page states a 1 GB per-file maximum | capture: sha256:3bf45dae883e5316d27b5765d6fc423b4addee504d86fd1d62ae5975dcdf92f9 | quote: Max. File size: 1 GB
  - [1] 2026-11-03: no account or login is required | capture: sha256:3bf45dae883e5316d27b5765d6fc423b4addee504d86fd1d62ae5975dcdf92f9 | quote: No registration is needed. Just paste your file link and download immediately and no login or hassle required.
  - [1] 2026-11-03: the page claims unlimited downloads with no frequency restriction | capture: sha256:3bf45dae883e5316d27b5765d6fc423b4addee504d86fd1d62ae5975dcdf92f9 | quote: No restrictions on download frequency or usage
  - [2] 2026-11-03: the features page states no daily limit and no paid tier | capture: sha256:8ae116d4f7e79b791303a02b7ba79820892d39cd804cddb9e0d3fb8d3e7824ce | quote: Download as many files as you need without restrictions. No daily limits, no premium subscriptions, no hidden fees - just unlimited access to the world's files whenever you need them.
- sources:
  - [1] https://pullfiles.net/
  - [2] https://pullfiles.net/features
