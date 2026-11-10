# Lambda

> lambda.ai | Compute, Inference; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lambda/ | JSON https://fshy.ajam.dev/api/v1/entity/lambda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lambda Research Grant

- `compute/lambda-research-grant` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:43.737Z (live) | stale on 2026-12-03
- url https://lambda.ai/research
- free tier: 'We're committed to supporting groundbreaking research by offering qualifying researchers up to $5,000 in cloud credits to develop and showcase their work using Lambda's Instances, with select research to be featured on our website.' The vendor's own ICLR 2026 post names the independent-researcher lane directly: 'For independent researchers who need compute, the Lambda Research Grant also offers up to $5,000 in credits for Lambda's on-demand Instances.' The application is a Typeform, reviewed on a rolling basis, and the vendor announced an expansion at CVPR 2026 'covering entire research groups, not just individual grants'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the award is a competitive Typeform review with no published eligibility rule and no published credit expiry, so neither the amount nor the deadline is knowable before the decision. [1]
- limits note: the award is a competitive Typeform review with no published eligibility rule and no published credit expiry, so neither the amount nor the deadline is knowable before the decision.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The credits are spend-only on Lambda's own instances, so they do not stack with another vendor's allowance; the useful composition is with the applicant's own publication or GitHub record, which is the evidence the review appears to weigh. Instances pricing table on the vendor's pricing page (column 'PRICE/GPU/HR', described as self-serve, first-come access; no on-demand, spot or community label, billing granularity and minimum bill not stated): NVIDIA HGX H100 80 GB $3.99, NVIDIA HGX A100 80 GB $2.79, NVIDIA HGX A100 40 GB $1.99. The 1-Click Clusters table (2 weeks to 1 year) lists NVIDIA HGX B200 rows only. No L40S, L4 or GeForce row.
- reliability: no reliability event recorded
- notes: The strongest independent-researcher lane with a published number in this class, and the one to promote first after TRC. Two gaps to be honest about. First, the vendor page publishes no eligibility rule at all: there is no institution requirement and no stated requirement of a paper, and the audience is described as 'qualifying researchers', which is undefined. Second, credit expiry is not published on any vendor page, and third-party trackers disagree about whether an affiliation is needed - one says the programme is aimed at 'academic, independent and startup researchers' while another claims an institutional affiliation is required. Because the two readings disagree and neither is the vendor, this record stays at documented and the verdict is qualifies-with-caveat rather than qualifies.
- extras:
  - facets.class: research-credit
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_class: B200 / H100 / A100 listed for the platform
- evidence:
  - [1] 2026-10-22: 'offering qualifying researchers up to $5,000 in cloud credits to develop and showcase their work using Lambda's Instances, with select research to be featured on our website', quoted; page 200; the apply CTA points to a Typeform
  - [2] 2026-06-05: 'For independent researchers who need compute, the Lambda Research Grant also offers up to $5,000 in credits for Lambda's on-demand Instances', quoted; a vendor post that names independent researchers as the audience
  - [3] 2026-06-05: the grant was expanded at CVPR 2026 to cover 'entire research groups, not just individual grants'
  - [1] 2026-10-22: the page links 'Apply for a grant' to a Typeform and describes credits for researchers developing and showcasing work on Lambda Instances, read live
  - [4] 2026-10-22: 'qualifying researchers up to USD 5,000 in cloud credits to develop and showcase their work using Lambda's Instances, with select research to be featured on our website', quoted
  - [5] 2026-10-22: a third party records no stated restriction by country, institution type, career stage or academic affiliation, and repeats the USD 5,000 figure, reported
  - [6] 2026-10-22: 'Lambda expects to sponsor hundreds of researchers in the coming year, who will receive up to $5,000 in Cloud Credits and mentoring from Lambda's Chief Scientific Officer', and applications 'accepted on a rolling basis', quoted
  - [7] 2026-11-03: NVIDIA HGX H100 80 GB is $3.99 per GPU per hour | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX H100 | 80 GB | 208 | 1800 GiB | 22 TiB SSD | $3.99 |
  - [7] 2026-11-03: NVIDIA HGX A100 80 GB is $2.79 per GPU per hour | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX A100 | 80 GB | 240 | 1800 GiB | 19.5 TiB SSD | $2.79 |
  - [7] 2026-11-03: instances are self-serve with first-come access; the page names no on-demand or spot tier | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: Deploy NVIDIA B200, H100, A100, or GH200 instances in minutes with self-serve, first-come access.
  - [1] 2026-11-03: the grant is up to $5,000 in cloud credits for Lambda Instances | capture: sha256:cb66dd12d4c1b56c049a62422a36fdaab8399a688e6c0eb39973d741525e8460 | quote: We're committed to supporting groundbreaking research by offering qualifying researchers up to $5,000 in cloud credits to develop and showcase their work using Lambda's
- sources:
  - [1] https://lambda.ai/research
  - [2] https://lambda.ai/blog/iclr-2026-12-papers
  - [3] https://lambda.ai/blog/lambda-at-cvpr-2026
  - [4] https://lambda.ai/cvpr
  - [5] https://grantedai.com/grants/lambda-research-grant-cloud-gpu-credits-mentoring-ai-researchers
  - [6] https://www.businesswire.com/news/home/20241209358457/en/Lambda-Launches-Grant-for-AI-Researchers-Expands-Research-Program
  - [7] https://lambda.ai/pricing

## Lambda

- `compute/lambda` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:28.019Z (live) | stale on 2026-12-04
- url https://lambda.ai/pricing
- free tier: no free tier: self-serve instances priced per GPU-hour: NVIDIA HGX H100 80 GB $3.99, NVIDIA HGX A100 80 GB $2.79, NVIDIA HGX A100 40 GB $1.99, NVIDIA HGX B200 180 GB $6.69 and NVIDIA Tesla V100 16 GB $0.79. The page lists no L40S, RTX 4090 or L4, names no spot tier, and states no billing granularity and no minimum bill. 1-Click Clusters of 16 or more GPUs run on terms of 2 weeks to 1 year | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.79 a GPU-hour for a V100 up to $6.69 for a B200 SXM6 on demand [1]
  - request-rate (binding): cluster reservations run from 16 to 2,000+ GPUs on a two-week to one-year term [1]
  - per-object-cap: 22 TiB of SSD on a B200 node; 5.8 TiB on a V100 node [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes on-demand and cluster rates. There is no free tier and no trial credit on it, so the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.vcpu: 208
  - shape.ram: 2900
  - shape.disk: 22528
  - shape.gpu_class: B200 SXM6
  - shape.gpu_count: 8
  - shape.note: a B200 SXM6 node: 180 GB of VRAM per GPU, 208 vCPUs, 2,900 GiB of RAM and 22 TiB of SSD
  - session_cap.restart_required: no
  - session_cap.note: self-serve, first-come instances; the page states no reap and bills while the instance exists
  - free_tier_kind: none
  - ps.gib: 22528
  - ps.price: included with the node
  - ps.durability: local SSD
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the instance's life
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Production-ready clusters from 16 to 2,000+ NVIDIA B200 or H100 GPUs' with on-demand rates: 'NVIDIA B200 SXM6 180 GB 208 vCPUs 22 TiB SSD $6.69', 'NVIDIA H100 SXM $3.99', 'NVIDIA A100 SXM 80 GB $2.79', 'NVIDIA Tesla V100 16 GB $0.79', quoted
  - [1] 2026-11-03: the instances table lists the HGX H100 at $3.99 per GPU per hour; the table lists no L40S, RTX 4090 or L4 | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX H100 | 80 GB | 208 | 1800 GiB | 22 TiB SSD | $3.99 |
  - [1] 2026-11-03: the pricing page was read on this date | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX H100 | 80 GB | 208 | 1800 GiB | 22 TiB SSD | $3.99 |
  - [1] 2026-11-03: the HGX A100 80 GB is $2.79 per GPU per hour | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX A100 | 80 GB | 240 | 1800 GiB | 19.5 TiB SSD | $2.79 |
  - [1] 2026-11-03: the HGX A100 40 GB is $1.99 per GPU per hour | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX A100 | 40 GB | 124 | 1800 GiB | 5.8 TiB SSD | $1.99 |
  - [1] 2026-11-03: the HGX B200 180 GB is $6.69 per GPU per hour | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX B200 | 180 GB | 208 | 2900 GiB | 22 TiB SSD | $6.69 |
  - [1] 2026-11-03: the Tesla V100 16 GB is $0.79 per GPU per hour | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA Tesla V100 | 16 GB | 88 | 448 GiB | 5.8 TiB SSD | $0.79 |
  - [1] 2026-11-03: the pricing page lists the on-demand H100 rate | capture: sha256:730e1b0f3ef8247953a93a191c639dfdd4d917c7f1a3320756bd69564aaea1a9 | quote: | NVIDIA HGX H100 | 80 GB | 208 | 1800 GiB | 22 TiB SSD | $3.99 |
- sources:
  - [1] https://lambda.ai/pricing

## Lambda Cloud credits

- `compute/lambda-cloud-credits` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card yes, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://lambda.ai/nvidia-inception
- free tier: Get USD 1,000 in cloud credits to build AI with on-demand GPU instances on Lambda Cloud. Covers on-demand NVIDIA B200, H100 and A100 GPUs plus GH200 Grace Hopper Superchips, with no ingress or egress fees, and covers persistent storage at USD 0.20/GB/month. One grant per company. Credits valid 12 months. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-shot-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: Requires current NVIDIA Inception membership, which requires official incorporation, plus a credit card issued in one of the listed countries. The eligible list includes the EU except Lithuania, the UK, the US, Japan, South Korea, Singapore, Taiwan, Turkey and others.
- interface: unknown
- limits:
  - write-gated (binding): Inception membership fails first on incorporation, and a card is mandatory anyway; the USD 1,000 is a trial-size amount rather than a workload. [1]
- limits note: Inception membership fails first on incorporation, and a card is mandatory anyway; the USD 1,000 is a trial-size amount rather than a workload.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 1,000 on Lambda buys several hundred hours of a single H100 at published hourly rates, enough to fine-tune a small model and not enough to pretrain. It composes with Inception membership only, and membership is the failing link.
- reliability: no reliability event recorded
- notes: Third-party listings disagree on the amount, ranging from USD 1,000 to USD 7,500. The vendor page says USD 1,000, so USD 1,000 is recorded. This is not a standalone Lambda startup program.
- extras:
  - facets.class: startup-credit
  - facets.free_tier_kind: one-shot-credit
  - facets.shape.gpu_class: H100 / B200 / A100 / GH200
- evidence:
  - [1] 2026-10-22: 'Get USD 1,000 in cloud credits', covering B200, H100, A100 and GH200 on-demand, one grant per company, valid 12 months, quoted
  - [1] 2026-10-22: 'A valid credit card is required to prevent fraud and calculate tax' and the country list for eligibility, quoted
- sources:
  - [1] https://lambda.ai/nvidia-inception

## Lambda Inference API

- `inference/lambda-inference` | dead | evidence measured | binding none | category inference API, winding down, hosts no longer resolve
- identity a placeholder: card and phone unknown | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://lambda.ai/inference
- free tier: none: the Inference API is winding down and its hosts do not resolve | unit: none | metered on: none | read on: 2026-11-04 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: unverified: no sign-up for the Inference API can be read because its hosts do not resolve; the vendor's account sign-up page is linked from the inference page
- interface: rest
- limits note: no rate or quota can be read: the API hosts do not resolve
- binding note: no limit binds: the API does not serve
- endpoint: https://api.lambda.ai/v1/chat/completions
- tooling: OpenAI-compatible client; the vendor now points users at GPU instances
- composes with: none: the vendor redirects to NVIDIA GPU instances in its cloud
- reliability: api.lambda.ai, inference.lambda.ai and api.lambdalabs.com all failed DNS resolution on 2026-11-04
- notes: dead cause: dead-service
- evidence note: three DNS-failure probe records plus the vendor's wind-down statement
- evidence:
  - [1] 2026-11-04: the vendor says the Inference API is winding down | capture: sha256:db5ffd1fb9fdd33d10369e0c4b9aa74075d21e15fa7379600b37cba0b4cb4022 | quote: As the Inference API winds down, you can continue deploying and scaling models seamlessly on NVIDIA GPU instances.
  - probe:api.lambda.ai 2026-11-04: the API host fails DNS resolution | capture: sha256:70c39baedee0e362943ab33b3f0b5dd2931a8a836ac13c3e8a1ea2e703dce419 | quote: "error": "dns"
  - probe:inference.lambda.ai 2026-11-04: the inference host fails DNS resolution | capture: sha256:ab3e3366c2ea383896f0e9da4795adb7172fc3b6de7d5ed17bdd3ad70452dead | quote: "error": "dns"
  - probe:api.lambdalabs.com 2026-11-04: the legacy API host fails DNS resolution | capture: sha256:fbfec5d2cc360a170b036dbd5a09c494feb1745328ca5e6b45c991c383425601 | quote: "error": "dns"
- sources:
  - [1] https://lambda.ai/inference
