# GetMac

> getmac.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getmac/ | JSON https://fshy.ajam.dev/api/v1/entity/getmac.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GetMac

- `compute/getmac` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted macOS VM / CI runner | tier Free plan
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.836Z (live) | stale on 2026-12-26
- url https://getmac.io/pricing
- free tier: USD 0 a month with 100 compute minutes per month and up to 1 concurrent virtual machine | unit: minutes | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: Compute minutes are consumed with a machine-type multiplier: the Mac M4 Base is 1x, the M4 Pro is 2x and the M4 Max is 4x; only the 4-core 8 GB Base is generally available. The Developer plan is USD 11.99 a month with 1000 compute minutes.
- per-object cap: not an object-storage offer; no per-file size ceiling is published on the pricing or instance pages | source: [1]
- retention: not stated on the pricing page; CI runners are provisioned per workflow job and deleted when the job completes, while dashboard VMs persist until stopped | source: [2]
- egress: not published: the pricing page states no egress allowance or transfer price; the paid Team plan rate is quoted at USD 0.011 per compute minute against GitHub Hosted at USD 0.062 per minute | metered: no | source: [1]
- identity: email | detail: the marketing page says no credit card is required; the dashboard sign-in page offers Continue with Google, Continue with GitHub or an Email field with Continue with email. No phone or ID document is requested on that page.
- interface: ssh, rest, browser
- limits:
  - volume-quota (binding): 100 compute minutes a month on Free; up to 1 concurrent virtual machine; extra usage needs a paid plan [1]
  - per-object-cap: machine type multiplier: Mac M4 Base 4 cores/8 GB at 1x, M4 Pro 2x and M4 Max 4x, the latter two marked Coming Soon [1]
  - write-gated: a GetMac account is required; sign-in offers Google, GitHub or an email address [3]
- limits note: The pricing page does not state a job wall-clock cap, an idle reap rule or an egress quota.
- binding note: The 100 compute minutes a month and single concurrent VM limit what a Free account can run before it must move to a paid plan.
- interface detail: a REST API for VM management, an integrated remote terminal and remote display in the dashboard, and SSH access to a virtual machine; GitHub Actions and GitLab CI jobs use a custom runner label
- endpoint: unverified: no API endpoint URL is stated on the pages read
- tooling: a GitHub account to install the GetMac GitHub App, or the GetMac dashboard; Golang and Python SDKs are published; a GitHub Actions workflow sets runs-on: getmac
- composes with: the free 100 compute minutes a month cover short Xcode and Fastlane CI jobs through a drop-in GitHub Actions runner label, with longer or parallel jobs requiring a paid plan.
- reliability: The vendor states a 99.9% uptime SLA on owned Apple Silicon hardware in a TIER III data center; runner jobs use fresh isolated macOS environments. The pricing page does not state a job timeout or idle reap rule.
- notes: The operator's provider list prices GetMac at USD 0.66/h billed per minute, which corresponds to the paid Team plan at USD 0.011 per compute minute (derived: 0.011 x 60 = USD 0.66 per hour); the Free plan is 100 compute minutes a month. The free allowance is a small monthly quota, hence the caveat.
- evidence note: the pricing page, landing page, documentation index and dashboard sign-in page were read on 2026-11-25; the quoted lines establish the free allowance, concurrent VM cap, no-card statement and signup gate. The sign-in page's public form was read directly; the rung stays documented because no live VM was measured.
- self hosted: no
- extras:
  - shape.vcpu: 4
  - shape.ram_gib: 8
  - shape.note: Mac M4 Base at a 1x compute-minute multiplier; M4 Pro and M4 Max are marked Coming Soon
  - billing_model: monthly compute-minute allowance, paid plans add minutes
  - free_tier_kind: recurring-allowance
  - price_arithmetic: Free: 100 compute minutes a month; Team: USD 33.99 a month for 3000 minutes (USD 0.01133 per minute)
  - session_cap.restart_required: no
  - session_cap.note: no job wall-clock cap or idle reap rule published on the pricing page
  - network_out.allow_outbound: yes
  - network_out.ports: not published
- evidence:
  - [1] 2026-11-25: the Free plan is USD 0 a month and includes 100 compute minutes a month | capture: sha256:8c4ed07f2363156dace2b1aec88d2e0b9501e79a1b57eb23e47099de510ea99f | quote: Includes 100 compute minutes per month
  - [1] 2026-11-25: the Free plan allows up to 1 concurrent virtual machine | capture: sha256:8c4ed07f2363156dace2b1aec88d2e0b9501e79a1b57eb23e47099de510ea99f | quote: Up to 1 concurrent virtual machine
  - [1] 2026-11-25: the smallest instance is a 4-core 8 GB Mac M4 at a 1x multiplier, with larger multipliers marked Coming Soon | capture: sha256:8c4ed07f2363156dace2b1aec88d2e0b9501e79a1b57eb23e47099de510ea99f | quote: 4 Cores - 8GB • Perfect for development and testing
  - [1] 2026-11-25: the paid Team rate used in the savings calculator is USD 0.011 per compute minute | capture: sha256:8c4ed07f2363156dace2b1aec88d2e0b9501e79a1b57eb23e47099de510ea99f | quote: Estimates based on new GitHub standard pricing ($0.062/min) vs GetMac Team plan pricing ($0.011/min).
  - [4] 2026-11-25: the landing page says no credit card is required | capture: sha256:552bd8cd19eb787f8360346bb8ccc94df31c8c66049c2b2d43237bedeec61912 | quote: No credit card required • 5-minute setup
  - [4] 2026-11-25: a REST API and SSH access are offered for the VMs | capture: sha256:552bd8cd19eb787f8360346bb8ccc94df31c8c66049c2b2d43237bedeec61912 | quote: Automate with our REST API
  - [4] 2026-11-25: the hardware is owned Apple Silicon in a TIER III data center with a 99.9% uptime SLA | capture: sha256:552bd8cd19eb787f8360346bb8ccc94df31c8c66049c2b2d43237bedeec61912 | quote: 99.9% uptime SLA, because every build matters
  - [3] 2026-11-25: the dashboard sign-in offers Google, GitHub or email, with no card field | capture: sha256:d90e7eff97f8040df80a8fe2adceb1dc8971dbf39dc0023d5b861939f8c37076 | quote: Choose a sign-in method to continue to the dashboard
  - [3] 2026-11-25: an email sign-in option exists | capture: sha256:d90e7eff97f8040df80a8fe2adceb1dc8971dbf39dc0023d5b861939f8c37076 | quote: Continue with email
  - [1] 2026-11-24: the Free plan costs USD 0 per month and includes 100 compute minutes per month | capture: sha256:848a33a1c702be9d9be8ed5c741cf24a895d5bf48181df45fac6600c03db5749 | quote: Includes 100 compute minutes per month
  - [1] 2026-11-24: the Free plan allows up to 1 concurrent virtual machine | capture: sha256:848a33a1c702be9d9be8ed5c741cf24a895d5bf48181df45fac6600c03db5749 | quote: Up to 1 concurrent virtual machine
  - [1] 2026-11-24: the paid Developer plan is USD 11.99 per month with 1000 included minutes | capture: sha256:848a33a1c702be9d9be8ed5c741cf24a895d5bf48181df45fac6600c03db5749 | quote: $11.99/ month Includes 1,000 compute minutes per month
  - [1] 2026-11-24: minutes are charged as base minutes multiplied by the machine-type multiplier | capture: sha256:848a33a1c702be9d9be8ed5c741cf24a895d5bf48181df45fac6600c03db5749 | quote: Usage = Base Minutes × Machine Type Multiplier
  - [4] 2026-11-24: the service offers a REST API, SSH, a dashboard terminal and display, and states no credit card is required | capture: sha256:552bd8cd19eb787f8360346bb8ccc94df31c8c66049c2b2d43237bedeec61912 | quote: No credit card required • 5-minute setup
  - [5] 2026-11-24: the dashboard asks the user to choose a sign-in method before continuing | capture: sha256:b65a638372be4c16daeb02b0701def8ba6fe3ff88b16d8d667f3b2de72fdaac0 | quote: Choose a sign-in method to continue to the dashboard
  - [6] 2026-11-24: a GitHub Actions job can run up to 6 hours and a manual instance is deleted after 60 minutes | capture: sha256:c19a35166dd3de5a5c8bc83660db0144d288dcd49e4fb1e15150b353b47ebccc | quote: A job can run for up to 6 hours on a GetMac runner. Instances you create by hand are for debugging only and are deleted after 60 minutes.
  - [7] 2026-11-24: VM data is deleted on termination and CI runner data does not persist beyond the job | capture: sha256:411cdec26cce5b53f7b364e2eda382d8efbc6bd3240bbee719772ac45ac4f713 | quote: When a virtual machine is terminated, deleted, or expires:
  - [7] 2026-11-24: free trials may be changed, suspended or discontinued without notice | capture: sha256:411cdec26cce5b53f7b364e2eda382d8efbc6bd3240bbee719772ac45ac4f713 | quote: We reserve the right to modify, suspend, or discontinue any free trial or promotion at any time without prior notice.
- sources:
  - [1] https://getmac.io/pricing
  - [2] https://getmac.io/docs
  - [3] https://cloud.getmac.io
  - [4] https://getmac.io/
  - [5] https://cloud.getmac.io/auth/signin?callbackUrl=%2Fprojects
  - [6] https://getmac.io/docs/github-runners/getting-started
  - [7] https://getmac.io/terms-of-service
