# Hashnix.Club

> hashnix.club | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hashnix/ | JSON https://fshy.ajam.dev/api/v1/entity/hashnix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hashnix.Club

- `compute/hashnix` | qualifies-with-caveat | evidence documented | binding write-gated | category shared shell | tier membership
- needs card no, phone no, ID no, institution no | verified 2026-10-24T06:21:00.000Z (live) | stale on 2026-11-24
- url https://hashnix.club/about/
- free tier: 'Hashnix is a non-commercial, free to join pubnix. All services are provided free-of-charge as public service. Services include: Free shell account (SSH), Media portal, Group chat (dream), Site-hosting (Gopher, Gemini, HTTP), Bulletin Board (bbj), E-mail + more available programs by signing up for membership and logging into the system.' | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: no disk quota, RAM figure, traffic allowance or process limit is published on any page read; the terms, the about page, the print index and the register page were all read and none states one
- per-object cap: not applicable: the unit is a home directory, not an object
- retention: not stated: no inactivity clock, deletion policy or archival rule appears on the terms, about, print index or register pages | source: [2] | note: a documented absence, and it may not be used in arithmetic
- egress: not stated: no traffic volume, shaping tier or bandwidth figure appears on any page read | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: No card, no hold, no phone, no document. The registration form as served has exactly three inputs. A text field named 'name', a text field named 'contact', and a submit button — plus three textareas named 'message', 'purpose' and 'cert' rendered as 'about me', 'sign-up purpose' and 'SSH-pubkey (optional)'. The terms add an age gate: 'All registrants of user accounts must be 18+ years of age.'.
- interface: ssh
- limits:
  - write-gated (binding): registration is a form reviewed by a human; the form asks for username, email, 'about me', 'sign-up purpose' and an optional SSH public key [3]
  - volume-quota: no quota is published anywhere read; the limit is not knowable from the site [1]
- binding note: the account exists only after a human reads a free-text application, and no quota is published, so there is nothing to design a workload against even once accepted
- interface detail: SSH shell account, plus site hosting over Gopher, Gemini and HTTP, a bulletin board (bbj), local group chat (dream), e-mail, a media/radio portal and an Icecast stream
- tooling: any SSH client; the vendor's own CGI tools for radio and media; gopher and gemini clients
- composes with: a small open-registration pubnix with SSH, cron-capable shell and HTTP hosting, which is a place to run a script and publish a page but has no published quota to plan against
- reliability: the vendor published a key-rotation and CVE notice on 2026-05-15 and an amendment on 2026-05-20, including 'the SSH keys have been rotated and you are safe to replace previously used keystores'; no outage was observed.
- notes: The caveat is the absence of any published quota: a shell account with no stated disk, memory or traffic limit is a discretionary allocation, which is worse to plan against than a small published one. The 18+ gate is a statement of terms and was not tested. What could not be established: the actual disk and memory limits, the traffic allowance, whether cron and a listening port are permitted, and whether the human review accepts a stranger.
- evidence note: the service list, the terms and the registration form are quoted from first-party pages read. The quota is a documented absence, not a documented limit, and the record's verdict does not rest on it
- extras:
  - billing_model: free
  - term: perpetual
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: no price: the site states all services are free of charge and the form collects no payment
  - free_tier_kind: perpetual
  - network_out.allow_outbound: yes
  - network_out.ports: not stated
  - session_cap.restart_required: no
  - session_cap.note: none published
  - user_count.as_read: 2026-10-24
  - user_count.value: 60
  - age_gate: 18+ stated in the terms
- evidence:
  - [1] 2026-10-24: quoted: 'Hashnix is a non-commercial, free to join pubnix. All services are provided free-of-charge as public service.' and the service list 'Free shell account (SSH), Media portal, Group chat (dream), Site-hosting (Gopher, Gemini, HTTP), Bulletin Board (bbj), E-mail'
  - [3] 2026-10-24: the served markup: form action='register.php' with inputs named 'name' and 'contact', a submit input, and textareas named 'message', 'purpose' and 'cert'; no card, phone or document field
  - [2] 2026-10-24: quoted: 'All registrants of user accounts must be 18+ years of age.' and 'The services provided by Hashnix are provided as is. We do not warrant the reliability, accessibility or quality of our services'
  - [4] 2026-10-24: 
  - [5] 2026-10-24: quoted: 'powered by Debian 13 64-bit | hosting made possible by contabo' - the platform and the upstream host
  - [6] 2026-10-24: the portal page as served: '🚧🚧 ~ Under Construction ~ 🚧🚧', so no self-service control panel exists yet
  - [4] 2026-10-24: 
  - [5] 2026-10-24: quoted: 'powered by Debian 13 64-bit | hosting made possible by contabo' — the platform and the upstream host
- sources:
  - [1] https://hashnix.club/about/
  - [2] https://hashnix.club/about/print/terms/
  - [3] https://hashnix.club/register/
  - [4] https://hashnix.club/news/
  - [5] https://hashnix.club/
  - [6] https://hashnix.club/portal/
