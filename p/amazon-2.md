# Amazon Alexa

> amazon.science | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/amazon-2/ | JSON https://fshy.ajam.dev/api/v1/entity/amazon-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AWS Trainium Frontier

- `compute/aws-trainium-frontier` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:48.988Z (live) | stale on 2026-12-05
- url https://www.amazon.science/news/aws-trainium-frontier-competition-co-design-models-and-kernels-on-purpose-built-ai-chips
- free tier: The organiser supplies the silicon, quoted: 'Phase 1 gives every team a single Trainium2 chip and a 30-minute training budget, fast enough to test dozens of hypotheses in a single day.' Promotion buys more, quoted: 'Phase 2 promotes the top 10 teams to a full Trainium2 server with a four-hour budget, opening the door to distributed parallelism'. Prizes, quoted: 'prize money ($25,000 first place, $10,000 second, $5,000 third)'. Entry, quoted: 'Teams of one to four members are welcome'; 'The competition is open to the first 100 teams to register. Participants must be 18 or older'; 'Register by Sept 30, 2026'. Extra credits for some, quoted: 'Eligible academic teams can obtain AWS Promotional Credits covering Trainium compute and Amazon Bedrock access'. | unit: seconds | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: the page read states no egress allowance and no overage price; https://www.amazon.science/news/aws-trainium-frontier-competition-co-design-models-and-kernels-on-purpose-built-ai-chips read 2026-11-03 | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): the compute is a wall-clock budget on shared silicon rather than a balance: 30 minutes per Phase 1 run, four hours on a full server for the top ten, and the 2026 cycle closed registration on September 30, 2026 with the first 100 teams admitted. [1]
- limits note: the compute is a wall-clock budget on shared silicon rather than a balance: 30 minutes per Phase 1 run, four hours on a full server for the top ten, and the 2026 cycle closed registration on September 30, 2026 with the first 100 teams admitted.
- binding note: the same as limits note
- interface detail: unverified: the page does not say whether the Trainium2 chip is reached by SSH, console or API; it names the Neuron Kernel Interface and native PyTorch for Neuron
- tooling: not stated
- composes with: The unit is chip-minutes, not dollars: 30 minutes on one Trainium2 across up to 100 teams is the cheapest route in comparative records to touching non-NVIDIA silicon, and four hours on a full server for the top ten is the only free route found to a distributed training run on Trainium. It composes with the free Kaggle quota the same way AIMO does: practice in a notebook, then spend the contest budget on architecture rather than setup.
- reliability: no reliability event recorded
- notes: Classified as trial-only because the 2026 cycle closed: registration shut on September 30, 2026 and the finalist event is at NeurIPS 2026 in Sydney. The property that matters here is that the organiser, not the entrant, pays for the accelerator, which makes it the mirror image of MLPerf, where the entrant brings the hardware. Three explanations for why AWS runs it were considered: developer adoption of Neuron, benchmark supply for Annapurna Labs, and recruiting. The prize is small enough that adoption and recruiting fit better than a research grant, but the page supports none of the three explicitly. Unverified: the country exclusion list and whether a solo entrant can register without an AWS account, because the rules page at trainium-frontier.devpost.com/rules was not opened.
- extras:
  - facets.class: competition-grant
  - facets.free_tier_kind: allowance
  - facets.shape.gpu_class: Trainium2
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: 'Phase 1 gives every team a single Trainium2 chip and a 30-minute training budget'; 'Phase 2 promotes the top 10 teams to a full Trainium2 server with a four-hour budget'; '$25,000 first place, $10,000 second, $5,000 third'; 'Teams of one to four members are welcome'; 'The competition is open to the first 100 teams to register. Participants must be 18 or older'; 'Register by Sept 30, 2026'; 'Eligible academic teams can obtain AWS Promotional Credits covering Trainium compute'; page 200
  - [1] 2026-11-03: the page names NKI and PyTorch tooling; it states no egress term and does not say how the chip is reached | capture: sha256:3866e4f6852ff1fdca9ee42e4ce98a2b7b6b5af7e00fe8ce186ff3073ecf63f4 | quote: The Neuron Kernel Interface (NKI), native PyTorch support, and AI-assisted tooling
- sources:
  - [1] https://www.amazon.science/news/aws-trainium-frontier-competition-co-design-models-and-kernels-on-purpose-built-ai-chips

## Amazon Alexa Prize

- `compute/amazon-alexa-prize` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.amazon.science/alexa-prize/taskbot-challenge/rules
- free tier: Each selected university team receives a research grant plus free cloud, quoted from the programme's own announcements: 'Each participating team will receive a $250,000 research grant, Alexa-enabled devices, free Amazon Web Services (AWS) cloud computing services to support their research and development efforts, access to the CoBot conversational AI toolkit'. Prize money is separate: '$500,000 prize will be awarded to the team selected for creating the best socialbot. The second- and third-place teams will receive prizes of $100,000 and $50,000'. The gate, quoted from the rules: 'be enrolled as a full-time undergraduate or post-graduate student in good standing at an accredited college or university' and 'Entrants ("Entrants") must enter as part of an "Entrant Team" consisting of one or more students from a single University.' | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): the university is the unit of entry: a team must be drawn from a single accredited university with proof of enrolment, so an unaffiliated person cannot form an eligible team however strong the project. [1]
- limits note: the university is the unit of entry: a team must be drawn from a single accredited university with proof of enrolment, so an unaffiliated person cannot form an eligible team however strong the project.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The $250,000 grant plus free AWS is the largest per-team compute and cash package in the competition lane, and it is unreachable without a university affiliation. The chain available runs the other way: contribute to a university team as an enrolled student, which is an enrolment decision rather than a compute decision.
- reliability: no reliability event recorded
- notes: The clearest institutional gate, and the one most likely to be mistaken for open: the public-facing pages describe prizes and cloud support without stating the enrolment rule, which lives in the rules document. The cloud term could mean free AWS for the duration of the challenge, a fixed credit, or standard free-tier limits. The pages say 'free Amazon Web Services ... to support their research and development efforts' and never put a number on it, so the value of the compute is unverified and only the grant is quantified. The route that would price it is the participant agreement, which is not public.
- extras:
  - facets.class: competition-grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: 'be enrolled as a full-time undergraduate or post-graduate student in good standing at an accredited college or university'; 'must enter as part of an "Entrant Team" consisting of one or more students from a single University'; 'Proof of enrollment will be required to participate'; read through the search index for amazon.science
  - [2] 2026-10-22: 'Each university selected for the challenge received a $250,000 research grant, Alexa-enabled devices, free Amazon Web Services (AWS) cloud computing services to support their research and development efforts'; 'The GauchoChat team of four UCSB students ... earned $250,000'; read through the search index for amazon.science
  - [3] 2026-10-22: 'Each team will receive a $250,000 research grant, Alexa-enabled devices, free Amazon Web Services (AWS) to support their development efforts'; 'A $500,000 prize will be awarded'; read through the search index for developer.amazon.com
- sources:
  - [1] https://www.amazon.science/alexa-prize/taskbot-challenge/rules
  - [2] https://www.amazon.science/alexa-prize/socialbot-grand-challenge/2022
  - [3] https://developer.amazon.com/en-US/blogs/alexa/post/9f406f35-c997-4d17-a6ac-89a35f69b661/announcing-the-2018-alexa-prize-participant
