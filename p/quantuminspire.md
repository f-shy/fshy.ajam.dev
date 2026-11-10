# Quantum Inspire

> quantuminspire.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/quantuminspire/ | JSON https://fshy.ajam.dev/api/v1/entity/quantuminspire.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Quantum Inspire

- `compute/quantum-inspire` | qualifies-with-caveat | evidence documented | binding request-rate | category quantum compute
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://quantuminspire.com/
- free tier: "Quantum Computing for everybody - Quick and free registration - Access to our hardware backends - Project storage - Hybrid classical-quantum computing." The hardware is described as "Currently, these are Tuna-5, Tuna-9 and Tuna-17. Tuna-5 has 5 transmons [...] Tuna-9 has 9 transmons [...] Tuna-17 has 17 transmons", alongside a 26-qubit QX emulator and a Rydberg neutral-atom emulator from TU Eindhoven. No card is asked for and no expiry is published. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-open-registration
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): "You are not allowed to have more than 3 jobs in the queue for a hardware backend", and each hardware job waits behind calibration and other users, so throughput rather than total shots is the ceiling. [1]
- limits note: "You are not allowed to have more than 3 jobs in the queue for a hardware backend", and each hardware job waits behind calibration and other users, so throughput rather than total shots is the ceiling.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Quantum Inspire is the one provider among documented hosts whose free tier is a physical device rather than a batch queue, so it composes with nothing: the 17-qubit machine cannot be used to prepare data for a GPU job, and the only chain available is the same account also using the emulator for circuit development before spending queue slots on hardware.
- reliability: no reliability event recorded
- notes: A university lab, TU Delft through QuTech, that issues accounts to email addresses with no institutional check and publishes no expiry, which is why this is the cleanest lane fit in the file for the identity question. A third-party comparison table lists QuTech as "free access" that "does not expire", which agrees with the vendor but is not the vendor speaking, so neither sentence is treated as a quota here. Two technical reliability facts from the FAQ matter more than the qubit count: the chips go offline for calibration and upgrades, which the backends page also shows by marking Spin-2+ as taken offline, and the FAQ warns that Chinese providers such as 163.com and qq.com bounce the confirmation mail often enough that users must write to support, which is a practical obstacle for an address on those domains rather than a veto. The free tier's shot allowance per job is not stated on the pages read, so no circuit-throughput figure is given.
- extras:
  - facets.class: open-science-lab
  - facets.free_tier_kind: perpetual-open-registration
  - facets.shape.gpu_class: superconducting transmon QPU, 17 qubits (Tuna-17)
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: "Quick and free registration - Access to our hardware backends", quoted
  - [2] 2026-10-22: backends described as semiconducting, superconducting and neutral atoms across multiple chips, quoted
  - [3] 2026-10-22: "Currently, these are Tuna-5, Tuna-9 and Tuna-17. Tuna-5 has 5 transmons in a starfish configuration [...] Tuna-9 has 9 transmons [...] Tuna-17 has 17 transmons in a ninja-star configuration"; a 26-qubit QX emulator and a TU Eindhoven Rydberg neutral atom emulator are also listed; Spin-2+ is "taken offline", quoted
  - [4] 2026-10-22: "You are not allowed to have more than 3 jobs in the queue for a hardware backend, in order to provide equal access opportunities for everybody", quoted
  - [4] 2026-10-22: "a typical quantum-only job on a hardware backend takes 30 to 90 seconds"; "A hybrid job ... may take up to 15 minutes or longer to execute", quoted
  - [2] 2026-10-22: the platform is described as designed and built by QuTech, quoted
- sources:
  - [1] https://quantuminspire.com/
  - [2] https://www.quantum-inspire.com/
  - [3] https://www.quantum-inspire.com/backends/
  - [4] https://quantuminspire.com/faq/
