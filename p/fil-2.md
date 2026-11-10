# Filecoin Plus

> fil.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fil-2/ | JSON https://fshy.ajam.dev/api/v1/entity/fil-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filecoin Plus / DataCap free storage

- `storage/filecoin-plus-datacap-free-storage` | fails-quota | evidence documented | binding none | category contributed storage - subsidised free deals
- needs card no, phone no, ID no, institution yes | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://fil.org/filecoin-plus
- free tier: was: DataCap granted by allocators, deals free or near-free because SPs got 10x quality-adjusted power | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: never free; retrieval is a separate paid market | metered: no
- identity: institution | detail: institution
- interface: unknown
- limits note: DEAD AS OF 19 OCTOBER 2026. The Solstice upgrade (nv29, FIP-0118) ended Fil+ and DataCap outright: 'No new DataCap is minted, unused balances become inert, pending allocations can no longer be claimed, and the verified registry and DataCap actors refuse any state change.' Every new sector now gets 10x power regardless of content, so there is no longer any reason for an SP to accept free client data. Any 2025-era guide recommending Fil+ as free 20 TiB storage is now wrong.
- interface detail: Boost deal-making, allocator applications
- tooling: lotus/boost, allocator registry
- composes with: none any more
- reliability: Pending DataCap allocations became unusable at activation; unclaimed allocations are simply lost.
- notes: the same as the free tier
- evidence note: re-read on 2026-10-22 (HTTP 200, 180635 bytes, sha256 ae552419811ef0cd). The page states the number in the record. The claim is documented, not measured.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: was: DataCap granted by allocators, deals free or near-free because SPs got 10x quality-adjusted power
  - dead_end.first_recorded: 2026-10-21
  - verified[0].url: https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0118.md
  - verified[0].date: 2026-10-22
  - verified[0].http_status: 200
  - verified[0].bytes: 180635
  - verified[0].sha256: ae552419811ef0cdb702173b4cd75e2aeca8ae4b6be3ab9877d252cced460ab3
  - verified[0].pattern_found: yes
  - verified[0].what_changed: no change: the page still states the claim
- evidence:
  - [2] 2026-10-22: Fil+ is deprecated and no new datacap is minted. Re-read https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0118.md: HTTP 200, 180635 bytes, sha256 ae552419811ef0cd. Quoted: 2026-07-14 | | spec-sections | | # FIP-0118: (Solstice) Deprecate Fil+ and Fund Services via Block-Reward Split ## Simple Summary This FIP deprecates the Filecoin Plus (Fil+) datacap minting and allocation system and replaces it with a two-part mechanism: - PoRep sector quality no longer depends on content at L1. Every new sector onboarded from the activation epoch automatically receives 10× QAP over its lifetime, realized immediatel
  - [3] 2026-10-21: 'FIP-0118 ends Fil+ and DataCap: every new sector gets 10x quality-adjusted power'; 'From activation, DataCap goes away in one step. No new DataCap is minted, unused balances become inert, pending allocations can no longer be claimed'
  - [4] 2026-10-21: 'The program gives providers a bigger share of block rewards for storing vetted client data, so clients usually pay nothing'; also 'Providers Down 87%, Deals Down 97%'
  - [5] 2026-10-21: 'Documenting Client-SP Payments ... one of the simplest ways to show that deals are active' - i.e. the free era was already being wound down in Q1 2026
- sources:
  - [1] https://fil.org/filecoin-plus
  - [2] https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0118.md
  - [3] https://www.coindaro.com/filecoin-upgrade-solstice-nv29/
  - [4] https://bitquery.io/investigations/filecoin-storage-in-numbers
  - [5] https://github.com/filecoin-project/Allocator-Governance/discussions/501
