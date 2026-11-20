# pyLoad

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-pyload/ | JSON https://fshy.ajam.dev/api/v1/entity/github-pyload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## pyLoad

- `debrid/pyload` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category open-source download manager with a web UI, JSON API and Thrift backend | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://github.com/pyload/pyload
- price USD 0
- free tier: 'pyLoad is a lightweight, pure-Python download manager with a modern web UI and rich plugin ecosystem. It automates downloads from one-click hosters, cloud drives, and many other sources; supports premium accounts, captcha-solving services, and link decryption; and can run headless on servers, NAS devices, or desktops.' Free software, no vendor service and no hosted tier. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: Installed with 'pip install --pre pyload-ng[all]' and started with 'pyload'; the web UI listens on localhost:8000.
- per-object cap: not applicable to the software: the cap is the target host's. Downloads are written to ~/Downloads/pyLoad by default. | source: [1]
- retention: not applicable: local files in the pyload storage directory until the operator deletes them. | source: [1]
- egress: No service egress: the instance downloads from the host to the machine it runs on. | metered: no | free allowance: none: no service-side bytes | source: [1]
- identity: anonymous | detail: The software itself needs no identity. A public instance needs whatever its operator issued: the default is pyload/pyload, and the project tells operators to change it. No public instance that accepts anonymous links was found.
- interface: rest, cli
- limits:
  - write-gated (binding): every API call needs a session from /api/login; the shipped default is user 'pyload' and password 'pyload' and the project says to change it [1]
  - request-rate: no published rate limit; a public instance applies its own captcha and per-user limits [2]
- limits note: The wiki still documents the pre-2.0 API ('python pyLoadCore.py', Thrift 7227); the README documents pyload-ng (Python 3.9+). The two describe different generations of the same project.
- binding note: The first thing that fails is authentication: there is no anonymous add-link path. The API doc opens with 'First you need to authenticate', and the public instance found today serves a login form with a captcha before any package can be added.
- interface detail: Web UI plus a JSON-over-HTTP API: POST username and password to /api/login returns a session id, then /api/<methodName> for every method in the Api docs. A Thrift RPC backend listens on port 7227. Click'n'Load is supported through a plugin that needs node.js or a JS engine.
- endpoint: http://<instance>:8000/api/login
- tooling: pyload-ng on PyPI; LinuxServer.io and QuickBox container images; third-party Android clients over the JSON API. A public instance is reachable with any HTTP client, so the wrapper is trivial once credentials exist.
- composes with: The instance is the downloader and the storage at once, so it only helps a client that can rent a machine to run it. Paired with a free VM it turns a link list into files on that VM's disk.
- reliability: Public instances are single-operator hobby servers: the one probed (pyload.dnshome.eu) was live but login-walled with a captcha, so a wrapper cannot add a link without credentials. The legacy pyload.net site still documents Python 2.5-2.7, which is not what the current 2.x code runs.
- notes: Answers the requirements's pyLoad question: the default login is pyload/pyload; an anonymous user cannot add a link, because both the JSON API and the web UI require a session; and the instance's own quota is not readable without an account - the login page publishes no limit, and the limit is whatever its operator configured. The public instance probed was not logged into.
- evidence note: README, API wiki and a live public instance were read. Raising it to measured needs an authenticated addPackage call on a real instance, which needs credentials on 2026-10-23 does not have.
- self hosted: yes
- extras:
  - default_login: pyload / pyload
  - anonymous_add: no
  - public_instances_found: pyload.dnshome.eu (live, login + captcha); the LinuxServer/QuickBox docs describe the same default credentials on private installs
  - probe_record: scratch (removed)
  - probe_records: scratch (removed)
  - saved_body: scratch (removed)
- evidence:
  - [1] 2026-10-23: 'Default username: pyload.' and 'Default password: pyload.'; web UI at localhost:8000; pip install pyload-ng; Python 3.9+
  - [3] 2026-10-23: authentication is mandatory: POST username/password to /api/login, then call /api/<methodName>; Thrift backend on port 7227
  - [4] 2026-10-23: the legacy project home still says 'You need at least Python 2.5 or at most Python 2.7', i.e. it describes the abandoned branch
  - probe:https://pyload.dnshome.eu/login 2026-10-23: a public pyLoad instance is live but gated: HTTP 200, 14235 bytes, challenge login-wall:login. Two requests returned the same byte count with different digests (beb894a20f68df43... at 01:47, c5e8da325f5d00ae... at 02:02), so the digest is per-response; the saved body contains 'Captcha waiting', 'Username' and 'Password'.
- sources:
  - [1] https://github.com/pyload/pyload
  - [2] https://pyload.dnshome.eu/login
  - [3] https://github.com/pyload/pyload/wiki/How-to-access-the-API
  - [4] https://pyload.net/
