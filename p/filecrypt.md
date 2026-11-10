# Filecrypt

> filecrypt.cc | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filecrypt/ | JSON https://fshy.ajam.dev/api/v1/entity/filecrypt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filecrypt

- `debrid/filecrypt` | qualifies-with-caveat | evidence documented | binding write-gated | category link container / link protector (one URL resolves to a list of host links) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://filecrypt.cc/
- price USD 0
- free tier: Opening a container costs nothing and needs no account: a container URL answers 200 to an anonymous GET. Creating one is offered on a public Create page ('You can also create a test container containing any link you want here https://filecrypt.cc/Create.html'). The site root redirects an anonymous visitor to /Login.html, which is the management side of the service, not the container side. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No price list, no quota page and no account requirement were found on the container path.
- per-object cap: not applicable: a container holds links, not bytes. The size shown on a container page is the sum of the linked host files. | source: [1]
- retention: unverified: no page states how long a container survives. Containers dated 2024-2025 still appear in search results with live host links, so retention is at least months for popular containers, but no policy is published. | source: [1]
- egress: No egress of its own: the container page lists links to other hosts and the browser or downloader fetches from those hosts. | metered: no | free allowance: none: no service-side bytes | source: [2]
- identity: anonymous | detail: No account was needed to fetch a container page or to reach the Create page. The /Login.html redirect applies to account management.
- interface: unknown
- limits:
  - write-gated (binding): some containers put a 'Security Check' captcha in front of the link list; others serve the table directly [3]
  - request-rate: unstated; the root and container pages sit behind Cloudflare [2]
  - request-rate: no published limit; the anonymous container page returned 200 with a language selector and no link list, indicating links are produced client-side or require additional steps [4]
- limits note: The captcha is per container, not per account, so it cannot be paid away. Cloudflare fronts the whole site and the root response carries a challenge-platform signature.
- binding note: The captcha on a protected container is what stops an unattended wrapper first; account quotas do not exist on this path, and a container holds links rather than bytes so no volume quota applies.
- interface detail: HTML container pages. The machine interfaces are Click'n'Load (a page script POSTs the link list to a local JDownloader listener on 127.0.0.1:9666) and the DLC container file offered on the page. No documented JSON API for resolving a container was found, so a wrapper parses the page.
- tooling: JDownloader's filecrypt plugin is the mature client; the board records that its direct-link parsing broke in 2024 while CNL and DLC kept working. A HTTP wrapper is feasible because the container page is server-rendered HTML.
- composes with: A container is the index, not the storage: resolving it yields one link per host, and those links are what a debrid service, a leech site or a JD instance consumes. It composes with every other row among debrid providers.
- reliability: Containers rot when the underlying host files are removed: pages show an online count (e.g. '4/13 Online') so dead links are visible. Cloudflare challenges and per-container captchas break unattended resolution.
- notes: The container page is the only part of debrid that answers 'resolve a link with no install and no account' cleanly: it turns one protected URL into the host list. It does not produce a direct file link, and it does not bypass the host's own limits. Relevant because DDL posts increasingly wrap their mirrors in a container rather than printing five host URLs, so any pipeline that scrapes DDL indexes needs a container resolver as a second stage. Not the storage topic's: the container holds no bytes.
- evidence note: Two container probes and the root probe are measured; the captcha and creating-without-account statements come from pages and a third-party issue comment. Solving a captcha and diffing the resolved list would raise this to measured.
- extras:
  - container_probe_record: scratch (removed)
  - root_probe_record: scratch (removed)
  - machine_interfaces: Click'n'Load to 127.0.0.1:9666, DLC export, HTML parse
  - container_path: /Container/<id>.html
  - client_side_render: yes
  - known_clients: JDownloader plugin, Filecrypt Link Unlocker userscript (seen in search results, not executed)
- evidence:
  - probe:https://filecrypt.cc/ 2026-10-23: the root redirects anonymously to /Login.html: HTTP 200 at 01:59:05Z, 5388 bytes, sha256 66e512e7a1fde0b97cdb6f02b67174d29f0e5f1629958fbf50721a5e8fdc22d6, challenge signature cloudflare-challenge. The same 5388-byte page hashed differently on an earlier request, so the digest is per-response and the byte count is the stable fact.
  - probe:https://filecrypt.cc/Container/4537F7C9C6.html 2026-10-23: a container resolves anonymously: HTTP 200, 300000 bytes read (truncated prefix), sha256 3fa5c06cea42eff610275db57549150c626e8c7030c037198918108ec5508f1f, no challenge detected
  - [3] 2026-10-23: a protected container serves a 'Security Check' captcha before its link table
  - [5] 2026-10-23: reported, third-party: 'You can also create a test container containing any link you want here https://filecrypt.cc/Create.html' and a real container URL; the DLC button exports the list
  - [6] 2026-10-23: reported: the JD plugin's direct-link parsing broke in 2024 because filecrypt changed the site; CNL and DLC were unaffected
  - [4] 2026-10-23: HTTP 200 with a language selector (English, German, Italian, French, Russian, Spanish, Polish, Dutch, Turkish, Japanese, Chinese, Czech) and no link list in the extracted text
  - [2] 2026-10-23: the reader was redirected to https://filecrypt.cc/Login.html and returned 'login wall' rather than the home page
- sources:
  - [1] https://filecrypt.cc/Container/4537F7C9C6.html
  - [2] https://filecrypt.cc/
  - [3] https://www.filecrypt.cc/Container/5A442B9C26
  - [4] https://filecrypt.cc/Container/4C4DAE699C.html
  - [5] https://github.com/rogerfar/rdt-client/issues/68
  - [6] https://board.jdownloader.org/showthread.php?t=96509
