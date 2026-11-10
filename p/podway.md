# Podway

> podway.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/podway/ | JSON https://fshy.ajam.dev/api/v1/entity/podway.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Podway

- `compute/podway` | qualifies-with-caveat | evidence documented | binding per-object-cap | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:55.984Z (live) | stale on 2026-12-05
- url https://podway.io/apps
- free tier: During early access, 'your first app on a Mini pod is free with no card'. The Mini pod is 'USD 4/mo - One light app, such as analytics, uptime checks or a password vault - 1 GB RAM - 1 vCPU - 6 GB disk', and every app 'runs in its own always-on cloud pod' with 'no usage meters, bandwidth bills or per-seat fees'. Larger pods: Small 'USD 7/mo - 2 GB RAM - 2 vCPU - 12 GB disk', Medium 'USD 12/mo - 4 GB RAM - 2 vCPU - 24 GB disk'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read: no bandwidth allowance or overage price appears; the page states 'Flat $4. No credits. No surprise bill.' | metered: yes | source: [1]
- identity: email | detail: no card for the first app: the page states 'During early access, your first app on a Mini pod is free with no card'. No hold exists on that path because no payment method is taken. The signup form is not quoted, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated.
- interface: unknown
- limits:
  - per-object-cap (binding): the free pod is one Mini at 1 vCPU and 1 GB with 6 GB of disk, and the app must come from the vendor's catalogue of supported open-source apps, so a custom image is not what this buys. [1]
- limits note: the free pod is one Mini at 1 vCPU and 1 GB with 6 GB of disk, and the app must come from the vendor's catalogue of supported open-source apps, so a custom image is not what this buys.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 1 vCPU and 1 GB always-on with a nightly backup covers the self-hosted service that otherwise needs a VPS: uptime monitoring, a newsletter, a password vault or an analytics endpoint, with no maintenance.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: dalisoft/awesome-hosting lists podway as 'Mini (4 USD/m) - no trial - 1 app free'. The vendor agrees on the price and makes the free app explicit but attaches it to early access, so the arrangement is promotional and can end; that is why the pod counts here as a real free allowance and not as a permanent one. Not established: whether the free pod can run an arbitrary container, which the app catalogue suggests it cannot.
- extras:
  - facets.class: new-provider
  - facets.free_tier_kind: free-forever
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
- evidence:
  - [1] 2026-10-22: 'During early access, your first app on a Mini pod is free with no card', quoted
  - [1] 2026-10-22: Mini pod 'USD 4/mo ... 1 GB RAM - 1 vCPU - 6 GB disk'; Small 'USD 7/mo ... 2 GB RAM - 2 vCPU - 12 GB disk'; Medium 'USD 12/mo ... 4 GB RAM - 2 vCPU - 24 GB disk', quoted
  - [1] 2026-10-22: 'Each app runs in its own always-on cloud pod. Choose a size that fits it. There are no usage meters, bandwidth bills or per-seat fees from Podway.', quoted
  - [1] 2026-10-22: supported catalogue includes Ghost, Umami, NocoDB, Listmonk, Uptime Kuma and Vaultwarden marked 'Free - early access', quoted
  - [2] 2026-11-03: the page states a flat price; no bandwidth allowance is stated | capture: sha256:1cb941f42033e33da9fe1812e683c6acb99cad8c3258477c2fb9cd763cb372ce | quote: Flat $4. No credits. No surprise bill.
- sources:
  - [1] https://podway.io/apps
  - [2] https://podway.io/
