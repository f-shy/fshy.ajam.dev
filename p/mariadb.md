# MariaDB Foundation

> mariadb.org | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mariadb/ | JSON https://fshy.ajam.dev/api/v1/entity/mariadb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MariaDB Foundation (MariaDB Server)

- `databases-kv/mariadb-foundation` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category open source relational database server (software the user installs and runs)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:46:17.998Z (live) | stale on 2026-12-20
- url https://mariadb.org/download
- free tier: MariaDB Server is a general purpose open source relational database management system; released under the GPLv2 open source licence and guaranteed to remain open source | unit: unlimited | metered on: none | read on: 2026-11-19 | source: [1] | note: No hosted quota applies: the software is downloaded and run by the user. Packages are available in the standard repositories of all major Linux distributions and from the MariaDB Foundation download site.
- per-object cap: unverified: no per-object or total size cap stated on the first-party pages read; capacity is set by the machine the user runs the server on | source: [2] | note: This is self-hosted software, so any cap is a property of the user's machine, not of the offer.
- retention: unverified: no retention limit stated on the first-party pages read; data persists on the user's own storage until deleted | source: [2] | note: Retention is determined by the user's own storage and backups, not by the vendor.
- egress: no egress charge or quota applies; the server runs on the user's own machine and network | metered: no | source: [1]
- identity: anonymous | detail: the MariaDB Server download page offers packages and repository setup with no account, card or sign-in; the newsletter email field on that page is an optional subscription, not a download gate
- interface: cli, unknown
- limits:
  - request-rate: max_connections defaults to 151, configurable by the user via an option file or SET GLOBAL [3]
- binding note: This is self-hosted software with no vendor-imposed quota; the only stated configurable limit is max_connections, which the user can raise, so no corpus limit binds the offer itself.
- interface detail: the MySQL/MariaDB wire protocol over TCP with the mariadb command-line client and connectors for C, Java, ODBC, Python and Node.js; the protocol token has no dedicated interface term in the vocabulary
- tooling: the user installs and runs the mariadb-server package or binary on a rented or free machine; connectors exist for C, Java, ODBC, Python and Node.js, and Galera clustering and a Kubernetes operator are available; rclone does not apply
- composes with: a MariaDB Server instance the user installs and runs on a rented or free machine is the self-hosted option of last resort; hosted managed databases such as MariaDB Cloud (MariaDB plc) are separate offers and come first whenever a hosted tier is available
- reliability: LTS releases are maintained for three years; the software is self-operated, so availability and backups depend on the user's own machine.
- notes: The MariaDB Foundation stewards the open source MariaDB Server; it is not a hosted provider. What it offers is software the user installs and runs, so this is the self-hosted option of last resort, recorded behind every hosted database in the topic. MariaDB Cloud is a separate managed offer from MariaDB plc and is not what this record describes. The only quota found on a first-party page is the configurable max_connections default of 151.
- evidence note: First-party pages read on 2026-11-19: mariadb.org/en, mariadb.org/download, mariadb.org/about and the MariaDB Community Server docs.
- self hosted: yes
- evidence:
  - [1] 2026-11-19: the server is open source under GPLv2 with no licence fee | capture: sha256:8927e19cdabb2509acc99f5136a750a65e6b26995ed9b3bded4a48fc9faa4eba | quote: MariaDB Server is released under the GPLv2 open source licence and is guaranteed to remain open source.
  - [1] 2026-11-19: what the software is | capture: sha256:8927e19cdabb2509acc99f5136a750a65e6b26995ed9b3bded4a48fc9faa4eba | quote: MariaDB Server is a general purpose open source relational database management system.
  - [2] 2026-11-19: the Foundation provides downloadable packages with no account gate on the download page | capture: sha256:9191afffd488890a9062df4587c6a07daa0c909d3d4443a8b54ae844c9d905f1 | quote: MariaDB Foundation provides packages for MariaDB versions newer than the version provided by the distribution only.
  - [3] 2026-11-19: the default client connection cap and that it is a user-configurable server setting | capture: sha256:c21dbaf4a9fea467a80307a7e6ed84174dd38e2f09a23f97c2931916904c3649 | quote: Server behavior lives in system variables, such as the `max_connections` variable, which caps how many clients can connect at once. Its default is 151
- sources:
  - [1] https://mariadb.org/en
  - [2] https://mariadb.org/download
  - [3] https://mariadb.com/docs/readme/community-server.md
