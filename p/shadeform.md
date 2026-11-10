# Shadeform

> shadeform.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shadeform/ | JSON https://fshy.ajam.dev/api/v1/entity/shadeform.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shadeform

- `compute/shadeform` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:35.124Z (live) | stale on 2026-12-04
- url https://www.shadeform.ai/
- free tier: no free compute allowance is stated on the pricing page, which says 'No fees, no markups' and 'You pay the same as going direct to the clouds in our network'. On-demand 'Starting from' rates per GPU-hour: H100 PCIe $1.66, A100 80GB PCIe $1.35, L40S PCIe $0.69, RTX 4090 $0.40; L4 is not listed. Spot instances are offered on select instance types at a discounted hourly price and can be reclaimed. The billing granularity and the minimum bill are not stated on the pages read | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): GPU instances across 30+ providers with centralised billing; reserved capacity carries a 12-month minimum term [1]
  - per-ip-shaping: the marketplace claims savings of up to 90% against AWS, GCP and Azure [1]
- interface detail: Access interface not documented in published terms.
- tooling: part of the free tier
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes a GPU marketplace with centralised billing and a 12-month minimum term on reservations. No free tier appears, which confirms paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: on-demand instances across providers; reserved capacity has a 12-month floor
  - free_tier_kind: none
  - reclassified_from: dead
  - net.out: yes
  - net.in: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'The GPU Cloud Marketplace · Deploy high quality GPUs at the best prices across 30+ top clouds worldwide' with 'one console to provision GPU instances across top providers with centralized billing' and 'Minimum term is 12 months (1 year)', quoted
  - [2] 2026-10-22: 'No fees, no markups.' as the page heading, with 'Using Shadeform is free. You pay the same as going direct to the clouds in our network.', quoted. The page publishes no rate table at all, so every rate in this finding comes from the instance directory, not from the pricing page
  - [3] 2026-10-22: 'Shadeform charges the same rate as going direct to the cloud provider. There is no additional fee for using Shadeform to launch instances or manage cloud accounts.' and 'When you launch an instance through Shadeform, you pay Shadeform for the GPU time and Shadeform passes the payment to the underlying cloud provider.', quoted from the Business section
  - [3] 2026-10-22: Shade Cloud is 'the name of the feature where we deploy your instances into our network of cloud accounts with each of the cloud providers. By using Shade Cloud, you can use the underlying cloud provider without having an account with them.' and 'As Shadeform is an abstraction for different clouds and data centers, we inherit the SLAs provided by cloud providers.', quoted
  - [4] 2026-10-22: 'A4000 | $0.15/hr' with 'pcie|16 GB VRAM|VM|0 available regions', vCPUs 4, Memory 21 GB, Storage 100 GB; the on-demand table on the same page lists 'A4000 | Hyperstack | $0.15 /hr' beside 'A4000 | Paperspace | $0.80 /hr', quoted. The unit is the whole VM, not a GPU attach
  - [5] 2026-10-22: sorting the directory by the Price column ascending put 'Hyperstack A4000 $0.15 - 1 16 No regions PCIe 21 100 4' first, then 'Hyperstack A4000 $0.30', 'Massed Compute A30 $0.35', 'Verda V100 $0.39', 'Massed Compute A5000 $0.44', 'IMWT A6000 $0.49', 'Hyperstack A6000 $0.50', 'Vultr A16 $0.51' and 'Massed Compute A6000 $0.57' twice, on Page 1 of 28; the descending sort started at 'Nebius B300 $88.00 $56.00 8 2304'
  - [6] 2026-10-22: the host's own on-demand rows 'NVIDIA A4000 16 6 24 $0.15', 'NVIDIA A6000 48 28 58 $0.50' and 'NVIDIA H100 80 28 180 $2.50', against Shadeform's Hyperstack rows at USD 0.15, USD 0.50 and USD 2.50: exact equality on three cards, which supports the no-markup claim for this host
  - [7] 2026-10-22: the host's hourly block reads 'A4000 $0.76 / hour' with 'NVIDIA A4000 GPU, 45GB RAM, 8 vCPU', and its monthly block on the same page reads 'A4000 $488 / month' with 44GB RAM and 8 vCPU, so USD 0.76 is the hourly rate and not a committed one; Shadeform lists the same 8 vCPU and 45 GB machine at USD 0.80/hr, a +USD 0.04 (+5.3%) gap
  - [8] 2026-10-22: 'After you verify your email address, a two-step form asks for your name and organization (your name appears on invoices and team invites; the organization names your workspace), then a few questions about what you plan to run.' and 'Add Funds makes a one-time payment through Stripe (minimum $20)', quoted
  - [8] 2026-10-22: 'Instances are billed per second against your account balance' and, of a launch with no funds, 'the console asks you to add funds before it continues', quoted; the page sets Deploy in bold inside that sentence
  - [9] 2026-10-22: Shade Cloud 'deploys the instance into its own account with the underlying cloud provider', and a Flex VM is 'a GPU instance that Shadeform virtualizes itself on a partner's bare-metal hardware, rather than one the provider virtualizes in their own cloud', quoted: the virtualisation layer is Shadeform's, the iron is a partner's
  - [10] 2026-10-22: 'Shadeform may reclaim the capacity at any time, at which point the instance is terminated', quoted; every entry of an instance type carries a rental_type, and a spot entry carries its own hourly price
  - [1] 2026-10-22: 'Deploy high quality GPUs at the best prices across 30+ top clouds worldwide.' with 'Shadeform supports over 100 regions across North America, Europe, Asia and Australia.' and, further down the same page, 'the best prices for your workloads across 150+ regions': one page carries two different region counts
  - [11] 2026-10-22: 17 clouds named across Page 1 of 2 and Page 2 of 2: Boost Run, Crusoe, Cudo Compute, Denvr Dataworks, DigitalOcean, Phyntec, Gcore, Hyperstack, Lambda, Latitude, Massed Compute, Nebius, Paperspace, Scaleway, Verda Cloud, Voltage Park and Vultr; the instance table adds IMWT and Excess Supply, which the cloud directory does not list
  - [2] 2026-11-03: the H100 PCIe tile reads Starting from $1.66/hr | capture: sha256:8da23cddcd1ed6d0651e1cabbbffb91f9d8edc3603df11a78325007b4b6d3cdb | quote: Starting from\\ \\ H100pcie\\ \\ $1.66/hr
  - [2] 2026-11-03: the A100 80GB PCIe tile reads Starting from $1.35/hr | capture: sha256:8da23cddcd1ed6d0651e1cabbbffb91f9d8edc3603df11a78325007b4b6d3cdb | quote: Starting from\\ \\ A100 80GBpcie\\ \\ $1.35/hr
  - [2] 2026-11-03: the L40S PCIe tile reads Starting from $0.69/hr | capture: sha256:8da23cddcd1ed6d0651e1cabbbffb91f9d8edc3603df11a78325007b4b6d3cdb | quote: Starting from\\ \\ L40Spcie\\ \\ $0.69/hr
  - [2] 2026-11-03: the RTX 4090 tile reads Starting from $0.40/hr | capture: sha256:8da23cddcd1ed6d0651e1cabbbffb91f9d8edc3603df11a78325007b4b6d3cdb | quote: Starting from\\ \\ RTX4090\\ \\ $0.40/hr
  - [2] 2026-11-03: no platform fee over the cloud rate | capture: sha256:8da23cddcd1ed6d0651e1cabbbffb91f9d8edc3603df11a78325007b4b6d3cdb | quote: No fees, no markups. Using Shadeform is free. You pay the same as going direct to the clouds in our network.
  - [10] 2026-11-03: spot is a discounted hourly rate that can be reclaimed at any time | capture: sha256:ea7821ba7f398085aad897e0b7a45fd7a25879f8c59bf0aa19e7f86b045770fe | quote: Spot instances let you rent GPUs at a discounted hourly price in exchange for interruptibility: Shadeform may reclaim the capacity at any time, at which point the instance is terminated.
- sources:
  - [1] https://www.shadeform.ai/
  - [2] https://shadeform.com/prices
  - [3] https://docs.shadeform.ai/getting-started/faq.md
  - [4] https://shadeform.com/directory/instances/hyperstack/A4000
  - [5] https://shadeform.com/directory/instances
  - [6] https://www.hyperstack.cloud/gpu-pricing
  - [7] https://www.paperspace.com/pricing
  - [8] https://docs.shadeform.ai/getting-started/quickstart.md
  - [9] https://docs.shadeform.ai/getting-started/concepts.md
  - [10] https://docs.shadeform.ai/guides/spotinstances.md
  - [11] https://shadeform.com/directory/clouds
