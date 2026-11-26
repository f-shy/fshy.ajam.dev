# Gotify Cloud

> gotify.net | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gotify/ | JSON https://fshy.ajam.dev/api/v1/entity/gotify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gotify Cloud

- `dev-services/gotify-cloud` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category self-hosted push notification server (open-source gotify/server, installed and run by the user) | tier Self-hosted
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.791Z (live) | stale on 2026-12-20
- url https://gotify.net/
- free tier: The gotify/server binary and the gotify/server Docker image are published at no cost under the MIT license: the user installs and runs the server on a machine the user supplies, with a REST API for sending messages and a WebSocket stream for receiving them. The project publishes no hosted SaaS subscription and no usage quota. | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: The unit counted is not a quota: the software is free and the user supplies the machine. Hosted Gotify is sold by third parties who install and run the same software on a rented machine, and those hosted lanes are named before this option.
- per-object cap: unverified: no per-message size cap is stated on the first-party pages read | source: [2]
- retention: Messages remain in the server's own database file, which the install guide tells the user to include in backups; the API exposes endpoints to delete all messages, all messages of an application, or a single message. No automatic expiry is stated on the pages read. | source: [2] | note: The Docker example mounts the data directory at /var/gotify/data; if that directory is not kept, the history is lost with the container.
- egress: not metered by the project: the server runs on a machine the user supplies, so outbound traffic follows that host's network terms; messages reach clients over a WebSocket stream opened by the server | metered: no | source: [3]
- identity: anonymous | detail: No registration with the project is needed: the user installs the server and sets its administrator password locally, and the owner creates application and client tokens inside the server. The Docker Compose example sets the initial administrator password with GOTIFY_DEFAULTUSER_PASS, and the owner changes it after first sign-in.
- interface: rest, cli
- limits:
  - write-gated (binding): an application token is required to push a message, and from Gotify 3 that token is shown only once, on creation or rotation [4]
- limits note: No request rate, message count, retention window or object size is published by the project; the machine the user runs sets the practical ceiling.
- binding note: Pushing a message needs an application token that is shown only once at creation or rotation, so losing it stops writes until a new token is made.
- interface detail: A REST API at the server's own URL takes messages with an application token in an X-Gotify-Key header, a token query parameter or an Authorization bearer header; basic auth is for creating a client token only. Messages stream to clients over WebSocket at /stream. The gotify/cli tool and any HTTP client can push. No hosted endpoint is published by the project.
- endpoint: unverified: the endpoint is the machine the user runs; no first-party hosted endpoint is published
- tooling: The user installs and runs the server: a platform zip from the gotify/server GitHub releases, or the multi-arch Docker image gotify/server with a mounted data directory for the SQLite database and images, configured through a gotify-server.env file. Application and client tokens are created inside the server. The gotify/cli tool or any HTTP client pushes messages; the Android app or the built-in web UI receives them over the WebSocket stream.
- composes with: This offer is software the user installs and runs on a machine of the user's choosing; the user also supplies the database backup, TLS termination and upkeep. Hosted push services are considered before this option.
- reliability: The project states no quota, throttle or automatic message expiry on the pages read. The application token is shown only once from Gotify 3, so it must be stored when issued. History lives in the server's data directory and is lost if that directory is not kept across a container replacement.
- notes: Gotify is software the reader installs and runs. No official hosted SaaS tier was found on the first-party site or the repository: the project's pricing and cloud paths answered 404. Third parties sell managed Gotify on rented machines; those are hosted lanes of the same software and are named before this option.
- evidence note: The software, install path, API authentication and token handling are read on the first-party site, the project repository, the install guide, the push guide and the API reference. The server was not installed or run, so no operating figure is measured.
- self hosted: yes
- evidence:
  - [1] 2026-11-19: the project distributes a server with a WebUI, an Android client and a CLI | capture: sha256:e7d3c79ed172a873fe65673fe8df6d49db01f514f4c333a2f24f4843fc03bd58 | quote: The heart of this project. gotify/server features a WebUI and functionality for:
  - [1] 2026-11-19: the server sends messages over a REST API | capture: sha256:e7d3c79ed172a873fe65673fe8df6d49db01f514f4c333a2f24f4843fc03bd58 | quote: sending messages via a REST-API
  - [5] 2026-11-19: self-hosting is a stated requirement of the project | capture: sha256:68766217db95ad19107e25b208095faaa791813a155583687b11efbbad5ddb01 | quote: Also, a requirement was that it can be self-hosted. We know there are many free and commercial push services out there.
  - [5] 2026-11-19: the source is published under the MIT license | capture: sha256:68766217db95ad19107e25b208095faaa791813a155583687b11efbbad5ddb01 | quote: This project is licensed under the MIT License
  - [5] 2026-11-19: receiving messages uses WebSocket | capture: sha256:68766217db95ad19107e25b208095faaa791813a155583687b11efbbad5ddb01 | quote: receive messages via WebSocket
  - [3] 2026-11-19: the user runs the server from a Docker image and mounts a data directory | capture: sha256:466e7ebc73a16932892a1bb6e5fdde9fb1f73a1c9415997a186af24a873aa075 | quote: docker run -p 80:80 -v /var/gotify/data:/app/data gotify/server
  - [3] 2026-11-19: the user must keep the mounted data directory in backups | capture: sha256:466e7ebc73a16932892a1bb6e5fdde9fb1f73a1c9415997a186af24a873aa075 | quote: include this directory in your backups.
  - [3] 2026-11-19: the published Docker images cover several CPU architectures | capture: sha256:466e7ebc73a16932892a1bb6e5fdde9fb1f73a1c9415997a186af24a873aa075 | quote: are multi-arch Docker images supporting amd64, i386, arm64, armv7, and riscv64.
  - [3] 2026-11-19: the initial administrator password is set locally through an environment variable in the Docker Compose example | capture: sha256:466e7ebc73a16932892a1bb6e5fdde9fb1f73a1c9415997a186af24a873aa075 | quote: GOTIFY_DEFAULTUSER_PASS: 'admin'
  - [4] 2026-11-19: an application token is required to push and is shown only once from Gotify 3 | capture: sha256:35bedc07a6155e999814f4d89dc000004927df8a5e0589ba072d21fdcd52b559 | quote: Starting with Gotify 3, tokens are only shown once, on creation or rotation.
  - [2] 2026-11-19: the application token can be sent in an X-Gotify-Key header or a token query parameter | capture: sha256:9f5f609dbc3cbe0fd471919247154f520aab3ffc8208b4828709c29b516f1ee6 | quote: The token can be transmitted in a header named `X-Gotify-Key`, in a query parameter named `token`
  - [2] 2026-11-19: basic authentication is limited to creating a client token | capture: sha256:9f5f609dbc3cbe0fd471919247154f520aab3ffc8208b4828709c29b516f1ee6 | quote: There is also the possibility to authenticate through basic auth, this should only be used for creating a clientToken.
  - [2] 2026-11-19: the API provides an endpoint to delete all messages, so retention is controlled by the owner | capture: sha256:9f5f609dbc3cbe0fd471919247154f520aab3ffc8208b4828709c29b516f1ee6 | quote: Delete all messages.
- sources:
  - [1] https://gotify.net/
  - [2] https://gotify.net/api-docs
  - [3] https://gotify.net/docs/install
  - [4] https://gotify.net/docs/pushmsg
  - [5] https://github.com/gotify/server
