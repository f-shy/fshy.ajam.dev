# Beyond.pl

> beyond.pl | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/beyond/ | JSON https://fshy.ajam.dev/api/v1/entity/beyond.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Beyond.pl

- `compute/beyond-pl` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-06T18:41:34.652Z (live) | stale on 2026-12-07
- url https://www.beyond.pl/en/services/gpu-as-a-service-gpuaas/
- free tier: no free tier or credit is stated on the GPU as a Service page; the published rate is a reserved price for DGX B200 and the rest is quoted. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable | source: [1] | note: the published unit is an 8-GPU DGX B200 node
- retention: not applicable | source: [1] | note: a machine record
- egress: Egress fees are stated as included for AI storage (USD 146 per TB per month); no egress term is stated for GPU compute. | metered: no | source: [1]
- identity: any-phone | detail: Beyond.pl Customer Panel registration (my.beyond.pl, where AI/GPU servers are ordered) asks for a phone number first, verified by an automated call that shows a 6-digit code to enter on that phone, then a registration form, an e-mail activation link and payer billing data. The billing form's fields are unverified: behind a sign-up. The sales enquiry form for reserved DGX B200 and clusters requires full name, business e-mail, company name, phone number, country, type and quantity of GPUs and reservation time, behind reCAPTCHA. That the ai.beyond.pl GPU Instances console uses the same panel is unverified: ai.beyond.pl answered a maintenance page.
- interface: unknown
- limits:
  - write-gated (binding): reserved DGX B200 (8 GPUs) is USD 5.10 per GPU-hour with the rate depending on capacity and contract duration; every other configuration is quoted through an enquiry form [1]
- limits note: sales-gated reserved 8-GPU nodes; the self-service GPU Instances console was behind a login
- binding note: the same as limits note
- interface detail: a GPU Instances option links to a separate console at ai.beyond.pl, which could not be read; no API or CLI is documented on the page read
- tooling: not stated: the GPU as a Service page documents no client; GPU Instances link to a console at ai.beyond.pl that sits behind a login
- composes with: The published rate is for reserved 8-GPU DGX B200 capacity from a Polish data center, with other terms and single-GPU configurations quoted through an enquiry form. It prices no H100, A100, L40S, RTX 4090 or L4.
- reliability: unverified: no status page or incident history was read
- notes: Per-card rates on the vendor's own page: NVIDIA DGX B200 (8 GPUs) reserved USD 5.10 per GPU-hour, net of taxes; dedicated clusters custom quote; AI storage USD 146 per TB per month. H100, A100 80GB, L40S, RTX 4090 and L4: not listed. A third-party index lists a single B200 row with 1 month and 12 month reserved terms at the same rate.
- evidence:
  - [1] 2026-11-03: the only published GPU rate is USD 5.10 per GPU-hour for reserved DGX B200 (8 GPUs); the rate depends on capacity and contract duration | capture: sha256:7b0c233e8f044c2948c4a55fb54e3ca731b03606e27df9c1ad113c47896cd983 | quote: NVIDIA DGX B200 (8 GPUs)<br>Reserved Instances pricing<br>$5.10<br>/hour/GPU<br>Pricing depends on capacity and contract duration.
  - [1] 2026-11-03: dedicated clusters are a custom quote | capture: sha256:7b0c233e8f044c2948c4a55fb54e3ca731b03606e27df9c1ad113c47896cd983 | quote: Dedicated GPU clusters<br>Custom enterprise pricing<br>Custom quote
  - [1] 2026-11-03: AI storage is USD 146 per TB per month with egress fees included | capture: sha256:7b0c233e8f044c2948c4a55fb54e3ca731b03606e27df9c1ad113c47896cd983 | quote: $146<br>/TB/month<br>Egress fees included.
  - [1] 2026-11-03: the GPU enquiry form requires full name, business e-mail, company name and phone number | capture: sha256:7b0c233e8f044c2948c4a55fb54e3ca731b03606e27df9c1ad113c47896cd983 | quote: Full name \* Business e-mail \* Company name \* Phone number \*
  - [1] 2026-11-03: a GPU Instances option links to a separate console at ai.beyond.pl | capture: sha256:7b0c233e8f044c2948c4a55fb54e3ca731b03606e27df9c1ad113c47896cd983 | quote: GPU compute for development, experimentation and selected production workloads. | [Launch GPU](https://ai.beyond.pl/)
  - [2] 2026-11-03: the Beyond.pl customer account registration first asks for a phone number for anti-spam verification | capture: sha256:cd3ec8618f6bbd06f27fff0c58518eebcf6c890012f524c8d383be9f83ec791e | quote: W kolejnym kroku zostaniemy poproszeni o podanie numeru telefonu w celu weryfikacji antyspamowej.
  - [2] 2026-11-03: the phone number is verified by an automated call, with a 6-digit code to enter on that phone | capture: sha256:cd3ec8618f6bbd06f27fff0c58518eebcf6c890012f524c8d383be9f83ec791e | quote: wykonane zostanie połączenie telefoniczne na wskazany numer, a na ekranie wyświetli się 6 cyfr
  - [2] 2026-11-03: registration ends with an e-mail activation link | capture: sha256:cd3ec8618f6bbd06f27fff0c58518eebcf6c890012f524c8d383be9f83ec791e | quote: Przedostatnim krokiem rejestracji jest kliknięcie w link aktywacyjny, który otrzymasz w wiadomości e-mail.
  - [3] 2026-11-03: AI/GPU servers are ordered from the Customer Panel after login | capture: sha256:c57d19e1115b94a660b6b8c07d74463b11a4a522ce383aaafdd0e5dee9f04121 | quote: After logging into the Customer Panel, on the main page (or on the list of AI/GPU servers), click the Order button.
  - [1] 2026-11-03: the Beyond.pl site links its Customer Panel to my.beyond.pl, the host where the registration guide sends the account sign-up | capture: sha256:38069281bec52621bd87d22e0673e99c41c57e34a615730e695289958c0eacee | quote: * [Customer Panel](https://my.beyond.pl/login)
  - [1] 2026-11-06: the GPUaaS pricing table prices one card only, the reserved 8-GPU DGX B200 at USD 5.10 per GPU-hour; the page prices no H100, A100 80GB, L40S, RTX 4090 or L4 and states no free or credit-backed GPU hours | capture: sha256:3b13ab8f66fd9081a650e69e194c23ddd23415053cb6c33940c32f27ff687c5c | quote: NVIDIA DGX B200 (8 GPUs) Reserved Instances pricing $5.10 /hour/GPU
- sources:
  - [1] https://www.beyond.pl/en/services/gpu-as-a-service-gpuaas/
  - [2] https://www.e24cloud.com/account/registration/
  - [3] https://docs.ai.beyond.pl/ai-servers/ordering/
