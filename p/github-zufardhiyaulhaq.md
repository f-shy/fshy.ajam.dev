# frp-operator

> github.com | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-zufardhiyaulhaq/ | JSON https://fshy.ajam.dev/api/v1/entity/github-zufardhiyaulhaq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## frp-operator

- `egress/frp-operator` | self-hosted, last resort | verdict fails-egress | evidence reported | binding none | category tunnel software (self-hosted) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://github.com/zufardhiyaulhaq/frp-operator
- price USD 0
- free tier: Kubernetes integration for . MIT License. Written in Go. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: No hosted allowance exists: the software runs on a host that is supplied separately.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: a source checkout | country: None
- interface: cli
- binding note: software only: no hosted endpoint is offered, so any egress it provides begins with a host that a user must get from a compute provider. Kubernetes integration for frp.
- interface detail: not established
- tooling: self-hosted binaries
- reliability: the same as interface detail
- notes: Kubernetes integration for frp. Classified from the aggregator's own sentence; no vendor page was fetched for this name.
- evidence note: Read the project README and run a client to raise this to documented; the list sentence is the only evidence here.
- self hosted: yes
- extras:
  - wg_path: none
  - ingress: tcp+udp
  - bytes_transit: yes
  - transit_note: the operator's relay
- evidence:
  - [1] 2026-10-23: list entry sentence: Kubernetes integration for . MIT License. Written in Go.
- sources:
  - [1] https://github.com/anderspitman/awesome-tunneling
  - [2] https://github.com/zufardhiyaulhaq/frp-operator

## ngrok-operator (zufardhiyaulhaq)

- `egress/ngrok-operator-zufardhiyaulhaq` | self-hosted, last resort | verdict fails-quota | evidence documented | binding volume-quota | category tunnel software (self-hosted) | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:36:39.325Z (live) | stale on 2026-12-04
- url https://github.com/zufardhiyaulhaq/ngrok-operator
- free tier: 1 GB / month of data transfer out, 20,000 HTTP requests / month and 5,000 TCP connections / month, counted by the ngrok free plan that the operator's authtoken belongs to; up to 3 online endpoints | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: The operator itself meters nothing; the byte cap is the ngrok account plan of the authtoken in the Ngrok resource.
- per-object cap: not applicable: counted per month rather than per object | source: [1]
- retention: not applicable | source: [1]
- egress: metered at 1 GB / month on the free ngrok plan; the first paid plan, Hobbyist, includes 5 GB and adds more against credit; pay-as-you-go is 5 GB included, then $0.10/GB | metered: yes | free allowance: 1 GB / month | price per TB: USD 0.10/GB | source: [2]
- identity: email | detail: an ngrok account and its authtoken, which the Ngrok resource takes in spec.authtoken; TCP endpoints on the free plan need a valid payment method added to the account; the sign-up form fields are unverified: behind a sign-up
- interface: rest
- limits:
  - volume-quota (binding): 1 GB per month of data transfer out; 20,000 HTTP requests, 5,000 TCP connections, 10,000 log events and 500 webhook verifications per month, on the ngrok free plan [1]
  - request-rate: 4,000 HTTP requests per minute and 100 TCP connections per minute on the ngrok free plan, separate from the monthly quotas [1]
- limits note: the allowance is a byte volume over a period, which none of the six kinds names; the number is in egress.free_allowance. Up to 3 online endpoints and 1 development domain on the free plan.
- binding note: 1 GB per month on the free ngrok plan is about 1,100 times below 1 TiB, so the byte quota fails first; the first paid plan, Hobbyist at $10 monthly, includes 5 GB.
- interface detail: a Kubernetes custom resource of kind Ngrok (apiVersion ngrok.com/v1alpha1) with protocol http or tcp, applied with kubectl; the operator is installed with Helm
- tooling: the user installs and runs the operator, a Helm chart, in a Kubernetes cluster that they supply; the tunnels it creates are relayed by ngrok's hosted edge
- composes with: the byte volume is relayed by the hosted ngrok service (see egress/ngrok-free for its free plan); the operator only creates and renews the tunnel from a cluster
- reliability: the last commit of the repository is dated 10 March 2023 (a dependency bump) and its example resources point at ngrok.io hostnames; no commit for more than three years
- notes: MIT licensed. The ngrok project's own Kubernetes operator is a different product that the free plan page lists as included on all plans. This record is the community operator by zufardhiyaulhaq; its tunnel capacity is the ngrok plan of the authtoken.
- evidence note: Operator behaviour is read from its README and example resource; the byte cap is read from the first-party ngrok plan pages. No tunnel was run, because that needs an ngrok account.
- self hosted: yes
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the operator runs the ngrok agent in a pod and ngrok's edge relays the bytes, which is what the 1 GB monthly counter counts
  - ingress: tcp
- evidence:
  - [3] 2026-11-03: the project is a Kubernetes operator that creates ngrok tunnels, not a relay of its own | capture: sha256:f2a07b618c73dd2f4d5a75e8fa6ac72c5702c8b2b7033a5be31ee64846af414e | quote: Ngrok operator provide developer easy access to private Kubernetes cluster for testing purpose via ngrok.
  - [4] 2026-11-03: the operator supports the http and tcp protocols only | capture: sha256:9cc5e2f8bc290129ae65ddfdcb164f1ce441dd88eb52a89a54947468856c0b12 | quote: # protocol used, currently support http & tcp
  - [4] 2026-11-03: every Ngrok resource carries an ngrok account authtoken | capture: sha256:9cc5e2f8bc290129ae65ddfdcb164f1ce441dd88eb52a89a54947468856c0b12 | quote: # ngrok authtoken
  - [1] 2026-11-03: the ngrok free plan caps data transfer out at 1 GB per month | capture: sha256:bda9952c9f038f9d45e8edd89b334a88609ce46743ffe1a04db5ed18e0e737f8 | quote: | Data transfer out | 1 GB / month |
  - [2] 2026-11-03: Free is 1 GB, Hobbyist includes 5 GB, pay-as-you-go is 5 GB then $0.10/GB | capture: sha256:0f015baedf63e3b3903a735bf16512c6305235a783e9c5cceb1c455139d4d56e | quote: | Data Transfer Out | 1 GB | 5 GB included (more with credit) | 5 GB included, then \$0.10/GB (volume discounts) |
  - [5] 2026-11-03: the Hobbyist card, the first paid plan after Free, is priced at $10 monthly | capture: sha256:7f9d14df7072d369271de115d11329687a4a855e4a73273d19116656ee5b9f50 | quote: $10 monthly
  - [6] 2026-11-03: TCP tunnels on the free plan need a payment method on the account | capture: sha256:bc2af89f9fd74c5e295d36bd0341738ae6d2297823d46a935a34a2bf317f336d | quote: TCP endpoints are only available on a free plan after [adding a valid payment method](https://dashboard.ngrok.com/settings#id-verification) to your account.
  - [7] 2026-11-03: the most recent commit listed is dated 10 March 2023 | capture: sha256:ff4c739793a2fead59aa125d96c190d1e2dfec137c3627ead668df82c17d927d | quote: Commits on Mar 10, 2023
  - [8] 2026-11-03: the operator is under the MIT License | capture: sha256:f4f8b8454bcce9b9e0941d568853081fc1d40bbbadafa861dc67a8f2a78f5108 | quote: MIT License
  - [1] 2026-11-03: the first-party ngrok Kubernetes Operator is a separate product that every plan includes | capture: sha256:bda9952c9f038f9d45e8edd89b334a88609ce46743ffe1a04db5ed18e0e737f8 | quote: * ngrok Kubernetes Operator
- sources:
  - [1] https://ngrok.com/docs/pricing-limits/free-plan-limits
  - [2] https://ngrok.com/docs/pricing-limits
  - [3] https://github.com/zufardhiyaulhaq/ngrok-operator
  - [4] https://raw.githubusercontent.com/zufardhiyaulhaq/ngrok-operator/master/examples/http/full-configuration/ngrok.yaml
  - [5] https://ngrok.com/pricing
  - [6] https://ngrok.com/docs/gateway/endpoints/tcp
  - [7] https://github.com/zufardhiyaulhaq/ngrok-operator/commits/master
  - [8] https://github.com/zufardhiyaulhaq/ngrok-operator/blob/master/LICENSE
