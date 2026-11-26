# AMD Radeon

> amd.com.cn | Inference, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/amd-2/ | JSON https://fshy.ajam.dev/api/v1/entity/amd-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AMD

- `inference/amd` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway with free public endpoints
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://developer.amd.com.cn/radeon/tokenfactory
- free tier: 12 public free model API endpoints listed on the TokenFactory page, marked 'Free' and 'Ready-to-use free API endpoints'; no numeric token or request quota is stated. | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account is needed for a key; the page itself states no identity gate and lists 12 public free model APIs
- interface: rest
- limits:
  - volume-quota (binding): 12 public free model APIs; no numeric quota stated on the page [1]
- endpoint: https://developer.amd.com.cn/radeon/api/v1
- tooling: OpenAI-compatible endpoints with the vendor's own clients
- composes with: the free public endpoints are the scarce link, and busy/idle status is shown per model
- reliability: models display a busy percentage; some endpoints are shown Busy (73-90 percent) at capture time
- notes: Page shows 12 free endpoints and 3 dedicated (credit-funded) ones; no numeric request or token quota is stated, so the free allowance is unverified beyond the word 'Free'.
- evidence:
  - [1] 2026-11-18: the TokenFactory page lists public free model APIs | capture: sha256:414a70dad266b32967f124406b8eb91084c2fe888e189849c6b470d5d58c58d3 | quote: Public Free Model APIs
  - [1] 2026-11-18: the free endpoints are described as ready-to-use free API endpoints | capture: sha256:414a70dad266b32967f124406b8eb91084c2fe888e189849c6b470d5d58c58d3 | quote: Ready-to-use free API endpoints
- sources:
  - [1] https://developer.amd.com.cn/radeon/tokenfactory

## AMD Radeon Cloud

- `compute/amd-radeon-cloud` | qualifies-with-caveat | evidence documented | binding request-rate | category GPU cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T04:58:13.794Z (live) | stale on 2026-12-19
- url https://developer.amd.com.cn/radeon/tokenfactory
- free tier: AMD runs two sites. On the China site the AMD AI Developer Program is free to join and new members start with 100 points, which is 100 GPU-hours at 1 point per hour; further points come from courses and activities, and an account may redeem at most 20 points a day. Token Factory, an OpenAI-compatible inference endpoint listing 16 public free models, is free, always on, and spends no credits. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: any-phone
- interface: ssh, rest, cli
- limits:
  - request-rate (binding): the 100 starting points buy 100 GPU-hours and redemptions are capped at 20 points a day, so the grant arrives in five daily slices; one account may hold one instance at a time and an instance bills while idle, so a forgotten container spends its credits in wall clock. [1]
- limits note: the 100 starting points buy 100 GPU-hours and redemptions are capped at 20 points a day, so the grant arrives in five daily slices; one account may hold one instance at a time and an instance bills while idle, so a forgotten container spends its credits in wall clock.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A recurring 20 GPU-hours a day on a ROCm container with SSH, a CLI and a persistent volume is the first free allowance found among evaluated offerings that is not a one-time credit or a notebook tab, and it composes with Token Factory: inference costs nothing, so the 20 hours can be spent entirely on training.
- reliability: no reliability event recorded
- notes: The China site signs in with a mobile number or email plus a slider captcha, or with a ModelScope, CSDN or GitHub account, so the identity is a phone number and not a national ID; whether the AMD China account itself demands a real-name check after signup is unverified. The Global site at radeon-global.anruicloud.com signs in with email or GitHub, needs no China number, and its credit route is unstated in the documentation. Open question: does the Global site grant the same points, or none? The docs say the Global site does not use the developer program, which suggests it has no free credit at all - that asymmetry is the thing to settle.
- extras:
  - facets.class: vendor-developer-program
  - facets.free_tier_kind: one-time-credit
  - facets.shape.vcpu: 16
  - facets.shape.ram_gib: 55
  - facets.shape.gpu_class: AMD Radeon (ROCm)
  - facets.shape.gpu_count: 1
- evidence:
  - [2] 2026-10-22: quoted: the program is free and needs no AMD hardware; 'The program says new members start with 100 points'; '1 point buys 1 hour of compute on the China site'; 'Each account can exchange up to 20 points a day, so a single exchange is for 1 to 20 hours'
  - [3] 2026-10-22: quoted: 'A running instance spends 1 credit per GPU every hour', the rate is shown per size as '1 GPU, 16 cores, 55GB, 1 credit / hour', an idle instance still spends credits, and the instance is deleted when credits run out
  - [4] 2026-10-22: quoted: 'Each account can have one instance at a time. Destroy it to launch another.'; persistent /workspace is 25 GB and some accounts can choose 100 GB; a launch fails for no free node, insufficient credits, or an account still under review
  - [1] 2026-10-22: read: 19 models total, 16 of them 'Public Free Model APIs' described as ready-to-use free API endpoints served by the AMD GPU Cloud, including DeepSeek-V4.1-Flash and DeepSeek-V4-Flash
  - [5] 2026-09-19: the route that finds it, translated: a ModelScope notebook page offers an AMD GPU environment with 192 GB of VRAM after linking an AMD developer account, one user reports 8 hours maximum per boot and persistence only inside /workspace
  - [2] 2026-11-06: the Global site has its own accounts and does not use the AMD AI Developer Program, so it grants no developer points | capture: sha256:acd5c25148d85cea81c10c549f4936ae3b46dd30053ab4a83e604f78a16dfa49 | quote: The China site runs on AMD AI Developer Program accounts. You need one to sign in there, and its developer points are how you get GPU credits. The Global site has its own accounts and doesn’t use this program.
  - [1] 2026-11-18: not stated | capture: sha256:2b384ab76e3ae8f8f78a964604a747bf8a27e15cbdf122b1f584ff95be934791 | quote: ### Public Free Model APIs
- sources:
  - [1] https://developer.amd.com.cn/radeon/tokenfactory
  - [2] https://amd-aim.github.io/radeon-cloud-docs/guides/developer-program/
  - [3] https://amd-aim.github.io/radeon-cloud-docs/guides/credits/
  - [4] https://amd-aim.github.io/radeon-cloud-docs/resources/faq/
  - [5] https://linux.do/t/topic/2922778
