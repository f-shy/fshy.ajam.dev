# Browser Linux emulators

> linuxontab.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linuxontab/ | JSON https://fshy.ajam.dev/api/v1/entity/linuxontab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Browser Linux emulators

- `compute/browser-linux-emulators` | self-hosted, last resort | verdict dead | evidence documented | binding retention-clamped | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:46:26.205Z (live) | stale on 2026-11-22
- url https://linuxontab.com/
- free tier: a Linux userland running in the browser tab, free with no signup on some sites | unit: none | metered on: none | read on: 2026-10-06 | source: [1] | note: WebVM is the strongest: real Debian x86 and real Tailscale networking, and it dies with the tab
- per-object cap: not applicable
- retention: dies with the tab | days: 0 | source: [1]
- egress: the user's own connection | metered: no | source: [1]
- identity: anonymous | detail: no signup on the sites that offer it
- interface: ssh
- limits:
  - retention-clamped (binding): closing the tab ends the environment; state survives only as an IndexedDB snapshot [1]
  - request-rate: the guest runs on the browser's own memory, so the machine's RAM is the ceiling [1]
- limits note: the CPU is the reader's own, so this is not remote capacity at all
- interface detail: a browser tab; no inbound endpoint
- tooling: a WASM Linux userland in the tab
- composes with: none: the machine is the reader's own laptop
- reliability: no reliability event recorded
- notes: Not remote compute: the cycles are the reader's own and the state dies with the tab. provider listings was right to refuse to count these.
- evidence note: the site was read on 2026-10-22 and states the free no-signup path, the IndexedDB snapshot on tab close, the opt-in WISP TCP egress and the guest-port tunnel. The record was already `dead` with a note that the environment ends when the tab closes, which the page confirms is a snapshot rather than a loss
- self hosted: yes
- extras:
  - shape.note: emulated x86 in the browser tab; the host's RAM bounds it
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: the tab's lifetime is the session; there is no vendor clock
  - free_tier_kind: allowance
  - ps.price: free
  - ps.durability: IndexedDB snapshot taken on close
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the browser's storage quota
  - net.out: yes
  - net.in: yes
  - net.ports: in-guest ports tunnelled out over a pairing-code WebSocket; SSH, SCP, SFTP and rsync
  - net.static_ip: no
  - net.allowance: WISP v1 over WebSocket, opt-in
- evidence:
  - [1] 2026-10-06: 'Free, no signup'; the machine is the browser tab
  - [1] 2026-10-22: 'Real x86 kernel. Runs offline. Open source stack. Free, no signup.' and 'State after closing tab: IndexedDB snapshots' and 'Networking is opt-in ... gets full TCP egress' and 'Free, no signup' with a pairing-code tunnel for SSH, quoted
- sources:
  - [1] https://linuxontab.com/
