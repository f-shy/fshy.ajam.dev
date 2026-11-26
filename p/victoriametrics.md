# VictoriaMetrics Cloud

> victoriametrics.com | Databases and KV; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/victoriametrics/ | JSON https://fshy.ajam.dev/api/v1/entity/victoriametrics.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VictoriaMetrics Cloud

- `databases-kv/victoriametrics-cloud` | trial-only | evidence documented | binding volume-quota | category managed metrics, logs and traces (time-series observability database) | tier Free 30-day trial / paid capacity tiers (from $200/month Initial Tier)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T02:46:18.052Z (live) | stale on 2026-12-20
- url https://victoriametrics.com/products/cloud/
- free tier: A free 30-day trial grants $200 in credits to spend across VictoriaMetrics, VictoriaLogs and VictoriaTraces deployments; it starts when the first deployment is created. Ongoing paid tiers start from $200/month for the Initial Tier (500k active time series, 16.6k datapoints/sec, 170 GB daily read volume). | unit: credits | metered on: wall-clock | read on: 2026-11-19 | source: [1] | note: The only free allowance is the time-limited 30-day trial with $200 credits; there is no permanent free tier. Credits cover compute, storage and network; egress beyond them is metered.
- per-object cap: unverified: no single-object cap is published; the Initial Tier capacities are 500k active time series, 16.6k datapoints/sec and 170 GB daily read volume, which are deployment limits rather than a per-object cap. | source: [2]
- retention: A deployment chooses a retention period; the price calculator offers 1, 6, 12 or 18 months. At trial expiry existing trial deployments are automatically deleted; after the trial ends, deployments are stopped and deleted after 7 days if no payment method is found. | source: [1] | note: days is null because retention is a user-selected tier setting, not a single fixed window; the 7-day post-trial deletion is a grace period, not a data-retention policy.
- egress: Egress traffic is charged $0.09 per GB, matching AWS' rate; estimated traffic costs typically range from $1 to $30 per month. Storage is $0.511 per Gb per month; backups are included at no extra cost and usage is metered hourly. | metered: yes | free allowance: trial credits ($200 granted at registration) | price per TB: $0.09 per GB for egress | source: [3]
- identity: email | detail: Registration is via Google sign-in or email and password; adding a payment method is not required to register or use deployments during the 30-day trial, and the trial grants $200 in credits.
- interface: rest, cli, browser
- limits:
  - volume-quota (binding): Initial Tier: 500k active time series, 16.6k datapoints/sec, 170 GB daily read volume [2]
  - retention-clamped: 30-day trial with $200 credits; after trial expiry deployments are stopped and deleted after 7 days if no payment method is added [1]
- binding note: Each deployment has predefined capacity limits and alerts on spikes; the Initial Tier's active-series, ingestion-rate and daily-read-volume ceilings bind before any per-object cap, which is not published.
- interface detail: Prometheus remote-write and vmagent ingest; OpenTelemetry, CloudWatch, InfluxDB, Datadog, New Relic, OpenTSDB and Graphite protocols; the deployment endpoint works as a Grafana data source. Programmatic access uses bearer tokens and console API keys; Terraform automation is supported.
- tooling: Prometheus, vmagent, Grafana data source, OpenTelemetry collectors, curl/REST queries; self-hosted VictoriaMetrics open-source components are the last-resort option
- composes with: A managed VictoriaMetrics endpoint drops in as a Prometheus remote-write target and Grafana data source; the open-source single-node or cluster binaries that the user installs and runs are the last resort when a hosted deployment is not used.
- reliability: Usage is metered hourly and billed monthly; each deployment has predefined limits and sends alerts on spikes rather than charging overages. Trial deployments are deleted when credits expire; egress is charged $0.09 per GB.
- notes: VictoriaMetrics Cloud has a 30-day $200-credit trial but no permanent free tier; ongoing capacity tiers start from $200/month and egress is $0.09 per GB. Registration is email/password or Google with no card until the trial ends. Self-hosted open-source VictoriaMetrics is the last resort, not the hosted offer described here.
- evidence note: Pricing, egress, trial and registration facts are from first-party VictoriaMetrics product, FAQ, billing and registration pages captured on 2026-11-19. No numeric per-object cap is published and is left unverified.
- self hosted: no
- evidence:
  - [2] 2026-11-19: paid managed tiers start from $200 per month | capture: sha256:0329a1ae8b8434948a9f24eb74c3f27177fe5d8a14dc54b5587646e041389812 | quote: From $200/month.
  - [2] 2026-11-19: the Initial Tier allows 500k active time series | capture: sha256:0329a1ae8b8434948a9f24eb74c3f27177fe5d8a14dc54b5587646e041389812 | quote: 500k
  - [2] 2026-11-19: a card or AWS billing is needed only after the trial | capture: sha256:0329a1ae8b8434948a9f24eb74c3f27177fe5d8a14dc54b5587646e041389812 | quote: AWS Marketplace & credit card payment available (after your trial ends)
  - [3] 2026-11-19: egress is metered at $0.09 per GB | capture: sha256:3e612cc1fcfc8bb91eb138d84105dc2eb913759f8f23bba3e5a43343166e11e5 | quote: Yes. We charge $0.09 per GB for egress traffic, which matches AWS’ rate.
  - [1] 2026-11-19: registration supports Google sign-in | capture: sha256:af59a3d525cdd946e801e7a30e35347430527f47120629af930669a3db6bcf7b | quote: Sign up with Google.
  - [1] 2026-11-19: registration supports email and password | capture: sha256:af59a3d525cdd946e801e7a30e35347430527f47120629af930669a3db6bcf7b | quote: Email and password.
  - [1] 2026-11-19: the trial requires no card at signup | capture: sha256:af59a3d525cdd946e801e7a30e35347430527f47120629af930669a3db6bcf7b | quote: Adding a payment method is not required to register or make use of deployments during the trial period.
  - [1] 2026-11-19: trial deployments are deleted when credits run out | capture: sha256:af59a3d525cdd946e801e7a30e35347430527f47120629af930669a3db6bcf7b | quote: Once the credits are expired, existing trial deployments will be automatically deleted.
- sources:
  - [1] https://docs.victoriametrics.com/victoriametrics-cloud/account-management/registration-and-trial/
  - [2] https://victoriametrics.com/products/cloud/
  - [3] https://docs.victoriametrics.com/victoriametrics-cloud/cloud-faq/
