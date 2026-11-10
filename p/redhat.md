# Red Hat

> redhat.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/redhat/ | JSON https://fshy.ajam.dev/api/v1/entity/redhat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Red Hat Developer Sandbox

- `compute/red-hat-developer-sandbox` | qualifies-with-caveat | evidence documented | binding retention-clamped | category kubernetes | tier Developer Sandbox
- needs card no, phone yes, ID no, institution no | verified 2026-10-24T06:04:10.000Z (live) | stale on 2026-11-24
- url https://developers.redhat.com/developer-sandbox
- free tier: 'The Developer Sandbox provides you with a 30-day trial experience to a selection of Red Hat products.' and 'It is free. There is no credit card required. All you need is a Red Hat account.' One private OpenShift project on a shared multi-tenant cluster. | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1]
- per-object cap: one project per sandbox, on a pre-configured resource quota that 'cannot be changed'
- retention: 'Your Developer Sandbox is active for 30 days'. Work can be exported before the trial ends and imported into a fresh 30-day trial: 'you can export your work before one trial ends, and import it when you've started your next 30 day trial'.
- egress: not published: neither the overview, the FAQ nor the try-it page states a traffic allowance for the sandbox. Routes and services are exposed through the shared cluster's router, which is normal OpenShift ingress. | metered: no | source: [1]
- identity: any-phone | detail: no card, no payment data, no national ID. A Red Hat account plus a validated phone number: 'We require a valid phone number to reduce the creation of fraudulent accounts'. The FAQ does not say which countries' numbers are accepted, and no country list is published on the page read.
- interface: rest, cli
- limits:
  - retention-clamped (binding): the sandbox is deleted 30 days after it starts [1]
  - volume-quota: pods are deleted after 12 consecutive hours of running; Linux VMs are shut down after 1 hour of continuous operation [1]
  - write-gated: phone-number validation at signup [1]
- binding note: Thirty days is a hard stop with no renewal in place, and the 1-hour VM shutdown means a VM cannot be a WireGuard node or an always-on monitor even inside that window.
- interface detail: `oc` CLI over the cluster API with a login token, plus the OpenShift web console and OpenShift Dev Spaces (a browser VS Code). Pods are ordinary OpenShift workloads; Linux VMs are available through OpenShift Virtualization.
- tooling: the `oc` or `kubectl` CLI, or the web console; Dev Spaces needs only a browser
- composes with: A real Kubernetes namespace with 14 GB of RAM to schedule against for 30 days, no card, which is the cheapest place to run a long-lived container or a small VM without owning a host.
- reliability: no reliability event observed. Shared multi-tenant cluster, so a neighbour's load is a plausible cause of a slow pod; the vendor publishes no status page for the sandbox on the pages read.
- notes: The largest no-card machine quota documented: 14 GB of RAM against a real Kubernetes API for 30 days. Three caveats. First, the phone requirement is the identity cost and the FAQ gives no country list, so whether a non-Chinese, non-institutional number passes is unverified. Second, the 14 GB figure comes from podman-desktop.io rather than developers.redhat.com; the exact quota is readable only inside a live namespace with `oc describe quota`. Third, the 1-hour VM shutdown makes OpenShift Virtualization useless for an always-on node even though it is advertised. A separate OpenShift Dedicated trial exists on the same page at 60 days, but it provisions into a Google Cloud account the applicant owns, which brings its own card question and was not pursued.
- evidence note: The 30-day term, the no-card statement, the phone requirement and the 12-hour/1-hour workload reaps are quoted from Red Hat's own FAQ read. The 14 GB RAM and 40 GB storage quota is from podman-desktop.io, a Red Hat-adjacent documentation site, not from a page on developers.redhat.com, so it is reported rather than documented.
- extras:
  - shape.ram_gib: 14
  - shape.disk_gib: 40
  - shape.note: the quota is cluster-wide across all pods in the namespace, not a per-machine shape; vCPU is not published
  - billing_model: free
  - term: 30 days from sandbox start
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: no charge and no payment field; the cost is 30 days of clock, not money
  - free_tier_kind: trial
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: through the cluster router via a Route or Service; no raw node port
  - network_out.static_ip: no
  - session_cap.wall_clock_min: 43200
  - session_cap.restart_required: no
  - session_cap.note: 30 days for the sandbox; 12 h per pod; 1 h per Linux VM
  - signup_url: https://developers.redhat.com/developer-sandbox
  - payment_methods: none; no payment field on the sandbox signup
- evidence:
  - [1] 2026-10-24: quoted: 'Q: What is my cost for the Developer Sandbox? A: It is free. There is no credit card required. All you need is a Red Hat account.'
  - [1] 2026-10-24: quoted: 'Your Developer Sandbox is active for 30 days and has specific built-in functionality.'
  - [1] 2026-10-24: quoted: 'Pods are automatically deleted after running for 12 consecutive hours. However, this does not affect the availability of your applications; you simply need to start a new pod. Note that Linux virtual machines (VMs) will be shutdown after one hour of continuous operation.'
  - [1] 2026-10-24: quoted: 'Why do I have to validate my phone number to access the Developer Sandbox? We require a valid phone number to reduce the creation of fraudulent accounts on the Developer Sandbox.'
  - [2] 2026-10-24: quoted: 'Get instant access to an environment for evaluation and experimentation', with 'Red Hat OpenShift', 'Red Hat OpenShift AI', 'Red Hat OpenShift Virtualization' and 'Red Hat OpenShift Dev Spaces' listed in the cluster
  - [3] 2026-10-24: quoted: 'The Developer Sandbox is a free, private OpenShift environment including one project and a resource quota of 14 GB RAM, and 40 GB storage. It lasts 30 days.' Reported, not first-party
  - [4] 2026-10-24: quoted: 'OpenShift Dev Spaces namespace and storage strategy, CPU and memory quotas, and other properties of the workspace server, are pre-configured and cannot be changed.'
- sources:
  - [1] https://developers.redhat.com/developer-sandbox/FAQ
  - [2] https://developers.redhat.com/developer-sandbox
  - [3] https://podman-desktop.io/docs/openshift/developer-sandbox
  - [4] https://developers.redhat.com/developer-sandbox/ide

## Red Hat OpenShift (Harbor backend)

- `compute/openshift` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T06:40:26.615Z (live) | stale on 2026-12-05
- url https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing
- free tier: not stated: https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing prints no free amount, unit or period; its only free route is a link to start a free trial in the developer sandbox, as an OpenShift Dedicated trial cluster, or as a self-managed OpenShift Container Platform trial | unit: none | metered on: wall-clock | read on: 2026-10-30 | source: [1] | note: the pricing page links a trials page that gives the lengths: the hosted Developer Sandbox costs nothing for 30 days with no stated requirements; the OpenShift Dedicated trial cluster runs 60 days in a Google Cloud account and incurs its infrastructure costs; the self-managed OpenShift Container Platform trial runs 60 days on infrastructure the user supplies; product trials require a Red Hat account
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing read 2026-11-04 prints no egress allowance or overage price | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - write-gated (binding): no self-serve price on the page; the free route is a Red Hat product trial [1]
  - request-rate: the page no longer publishes per-core or per-node subscription rates [1]
- interface detail: CLI: the OpenShift CLI (`oc`) documented in the OpenShift Container Platform CLI reference, installed by binary download or RPM.
- tooling: the OpenShift CLI, `oc`, to create applications and manage projects from a terminal.
- composes with: not established
- reliability: no reliability event recorded
- notes: The page that the record cites no longer carries a price list: it is a product navigation page, and its only free route is a 60-day trial. The prior 404 on the default read was a partial extraction, not a dead page.
- evidence note: the page was reached on 2026-10-22 through the firecrawl provider after the default read returned 404. It carries no price table and points at a trials page, so the record's free-tier claim is not established by it and the rung stays reported on that field
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a trial licence, not a machine the vendor runs
  - free_tier_kind: trial
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the Red Hat OpenShift pricing page was read on 2026-10-22 through the firecrawl provider and now serves a navigation and support page whose only free path is '- Start a trial' at redhat.com/en/products/trials; the pricing table the record cited is no longer on the page
  - [1] 2026-10-30: the pricing page names free trials with no amount, unit or period, and prints no other free allowance | capture: sha256:ed3229e36a03e55df543caa3797306df5e50dbaadd29b99a7d7c8af8388ce5be | quote: Get started in the developer sandbox, launch a trial cluster of Red Hat OpenShift Dedicated, or set up a trial of self-managed Red Hat OpenShift Container Platform.
  - [1] 2026-10-30: the free tier source page was read on the date set | capture: sha256:ed3229e36a03e55df543caa3797306df5e50dbaadd29b99a7d7c8af8388ce5be | quote: Get started in the developer sandbox, launch a trial cluster of Red Hat OpenShift Dedicated, or set up a trial of self-managed Red Hat OpenShift Container Platform.
  - [2] 2026-10-30: the Developer Sandbox trial lasts 30 days at no cost with no stated requirements; the same page gives 60 days for the Dedicated and self-managed trials and requires a Red Hat account for product trials | capture: sha256:8c66bf6077e50c3f3afc664a964042583efe4bfcd5a5d5a41c996bc957fec008 | quote: Trial length: 30 days
  - [2] 2026-10-30: the OpenShift product trials require a Red Hat account | capture: sha256:8c66bf6077e50c3f3afc664a964042583efe4bfcd5a5d5a41c996bc957fec008 | quote: These product trials are not intended for production use and include access to the latest and previous versions of the product. They require a Red Hat account.
  - [1] 2026-10-30: the cited page states no free amount, so free_tier.unit none still holds | capture: sha256:ed3229e36a03e55df543caa3797306df5e50dbaadd29b99a7d7c8af8388ce5be | quote: Get started in the developer sandbox, launch a trial cluster of Red Hat OpenShift Dedicated, or set up a trial of self-managed Red Hat OpenShift Container Platform.
  - [1] 2026-11-04: the pricing page lists hourly prices and billing parties and prints no egress allowance or overage price | capture: sha256:ed3229e36a03e55df543caa3797306df5e50dbaadd29b99a7d7c8af8388ce5be | quote: Reserved instances of Red Hat OpenShift are available for as little as $0.076/hour.*
  - [3] 2026-11-04: OpenShift documents a command-line client, oc | capture: sha256:fb82dc8aab5bf5163432f71e2dae83d51b6da05e53a32f93787b7a11cb485606 | quote: With the OpenShift CLI (`oc`), you can create applications and manage OpenShift Container Platform projects from a terminal.
  - [3] 2026-11-04: the provider documents the oc command line client | capture: sha256:1532eb17ce1f1ed86d10d12e171a0f92a4e55fc93eb40de8097e92551e8e2b80 | quote: With the OpenShift CLI (`oc`), you can create applications and manage OpenShift Container Platform projects from a terminal.
- sources:
  - [1] https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing
  - [2] https://www.redhat.com/en/technologies/cloud-computing/openshift/try-it
  - [3] https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html
