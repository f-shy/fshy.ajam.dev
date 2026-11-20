# SSH-J.com

> bitbucket.org | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitbucket-org-valdikss/ | JSON https://fshy.ajam.dev/api/v1/entity/bitbucket-org-valdikss.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SSH-J.com

- `egress/ssh-j` | fails-egress | evidence documented | binding none | category anonymous ssh jump host (no public ports) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://bitbucket.org/ValdikSS/dropbear-sshj/
- price USD 0
- free tier: Public SSH Jump and Port Forwarding server. No software, no registration, just an anonymous SSH server for forwarding. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No allowance is published; the server is one operator's box.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: 'Run ssh ssh-j.com and it will display usage information' - no account exists. | country: None
- interface: ssh
- binding note: No quota is published, but the shape fails first: 'No public ports, only in-SSH connectivity', so there is no listening port for an outside peer and no UDP.
- interface detail: ssh ssh-j.com
- tooling: system ssh.
- composes with: Outbound only.
- reliability: One volunteer server; the README says the code is 'bad and provided as-is'.
- notes: A free anonymous jump host is useful for reaching out, not for being reached.
- evidence note: Would change only if the operator opened public ports; the README describes a jump host.
- extras:
  - wg_path: none
  - ingress: none
  - volume_stated: No allowance is published; the server is one operator's box.
  - bytes_transit: yes
  - transit_note: The operator's server relays the SSH session.
- evidence:
  - [1] 2026-10-23: 'Dropbear SSH server modified to be used as a public SSH jump & port forwarding service. on https://SSH-J.com'
  - [2] 2026-10-23: 'No public ports, only in-SSH connectivity' (third party)
- sources:
  - [1] https://bitbucket.org/ValdikSS/dropbear-sshj/
  - [2] https://github.com/anderspitman/awesome-tunneling
