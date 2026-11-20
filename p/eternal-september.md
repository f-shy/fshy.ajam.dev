# Eternal September

> eternal-september.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eternal-september/ | JSON https://fshy.ajam.dev/api/v1/entity/eternal-september.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Eternal September (news.eternal-september.org) — free NNTP read/write

- `storage/eternal-september-free-nntp-read-write` | fails-quota | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:35.941Z (live) | stale on 2026-12-04
- url https://www.eternal-september.org/
- free tier: No byte quota. Free read AND write access to all text newsgroups after online registration. 281 hierarchies, alt.* alone is 8,728 groups, free.* is 1,284. Retention: '3 years for de.*, 160 days for the Big 8, 130 days for alt.*, 90 days for other hierarchies'. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 'No articles larger than 1000 KB | bytes: 1000000 | source: [1] | note: not stated
- retention: Retention: '3 years for de.*, 160 days for the Big 8, 130 days for alt.*, 90 days for other hierarchies' | days: 160 | source: [1] | note: not stated
- egress: Free; server has a 1 Gbit connection to several backbones and peers with 40+ sites. Articles are world-readable and propagate to every peer, so egress is effectively subsidised by the whole Usenet mesh. | metered: no
- identity: email
- interface: rest
- limits:
  - retention-clamped: Retention: '3 years [1]
  - retention-clamped: Retention: 90-160 days [1]
  - per-object-cap (binding): per-object-cap: 'No articles larger than 1000 KB [1]
- limits note: Per-object-cap: 'No articles larger than 1000 KB'. Hard 1 MB per article, and 'no binaries in text-only groups': binaries are only allowed in alt.binaries.* / de.alt.dateien.*, which this server does NOT carry ('no binaries'). Request-rate: anti-spam gates. No more than 3 distinct From: addresses per 24 h, 5 per 7 days, 8 per 30 days ('Excessive nymshifting'), with cancellation at 12 nyms/60 days. Retention: 90-160 days for most hierarchies, 3 years only for de.*.
- interface detail: rest
- tooling: Standard NNTP (RFC 3977) on port 119/563. Every Usenet client works: tin, slrn, Gnus, Thunderbird, Pan; programmatically via nntplib (Python) or any NNTP library. No bespoke wrapper needed. The docs give exact per-client auth config for ~10 clients.
- composes with: Per-record unlimited is the theoretical shape: a text article can carry base64, and there are 8,728 alt.* groups x 1,284 free.* groups x unlimited articles each. The multiplier would be 'groups x posts', which is effectively unbounded. BUT the per-record cap (1000 KB) and text-only rule kill it as a bulk store. See limits.
- reliability: Two technical blockers found by probing: (1) NNTP ports are unreachable from this network. TCP to news.eternal-september.org:563 timed out and:119 also timed out, so the transport may be firewalled depending on where you run; (2) accounts are auto-closed after 18 months of inactivity. Also note the server deliberately does NOT honour Cancels/Supersedes from other servers ('an article stored on our server can neither be deleted by a Cancel nor be overwritten by a Supersedes'), which is a rare retention plus.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: No byte quota. Free read AND write access to all text newsgroups after online registration. 281 hierarchies, alt.* alone is 8,728 groups, free.* is 1,284. Retention: '3 years for de.*, 160 days for the Big 8, 130 days for alt.*, 90 days for other hierarchies'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'free read and write access to all text newsgroups'; 'no binaries'; retention '3 years for de.*, 160 days for the Big 8, 130 days for alt.*, 90 days for other hierarchies'
  - [2] 2026-10-21: 'No articles larger than 1000 KB'; 'no binaries in text-only groups'
  - [3] 2026-10-21: nymshifting limits (3/24h, 5/7d, 8/30d); 'Accounts with Eternal-September will be automatically closed after 18 months of inactivity'; Cancels/Supersedes deliberately not honoured
  - [4] 2026-10-21: 281 hierarchies; alt.* 8,728 groups; free.* 1,284 groups
  - withheld 2026-10-21: probe: TCP news.eternal-september.org:119 and :563 -> both timeout (blocked from this network)
  - [1] 2026-11-19: free read and write access is to text newsgroups only, after online registration | capture: sha256:f93deec300368f691d4d7b58a850a56e2a1432c34a6baa3a24e708029463c447 | quote: news.eternal-september.org provides free read and write access to all text newsgroups. It requires a registration that can be done [online.](https://www.eternal-september.org/RegisterNewsAccount.php)
  - [1] 2026-11-19: retention is 90 to 160 days for most hierarchies and 3 years for de.* | capture: sha256:f93deec300368f691d4d7b58a850a56e2a1432c34a6baa3a24e708029463c447 | quote: Retention is currently 3 years for de.*, 160 days for the Big 8, 130 days for alt.* and 90 days for other hierarchies.
  - [2] 2026-11-19: the per-article size cap is 1000 KB | capture: sha256:349c9aac65e5a7e99306dfbc6e0dc2139df46af0e48882d4e804edd2a8da9046 | quote: No articles larger than 1000 KB
  - [3] 2026-11-19: accounts are closed after 18 months of inactivity | capture: sha256:f211c81afb6da0b658774d3b15f7d50276997e1a8f637e0bc6e833cf2ef75df4 | quote: Accounts with Eternal-September will be automatically closed after 18 months of inactivity.
  - [3] 2026-11-19: anti-spam request-rate gates limit distinct From addresses to 3 per 24 hours, 5 per 7 days and 8 per 30 days | capture: sha256:f211c81afb6da0b658774d3b15f7d50276997e1a8f637e0bc6e833cf2ef75df4 | quote: the server will accept no more than 3 different mail addresses in the From: header within a period of 24 hours or 5 different mail addresses within 7 days or 8 different email adresses within 30 days
  - [4] 2026-11-19: the server carries 281 hierarchies | capture: sha256:c5ebfe2498be23aeb81d6d586670eb7bcfca660cafedf6b718a4804a6a14f3c6 | quote: total number of hierarchies on server: **281 **
  - [4] 2026-11-19: the alt.* hierarchy has 8728 groups | capture: sha256:c5ebfe2498be23aeb81d6d586670eb7bcfca660cafedf6b718a4804a6a14f3c6 | quote: | [Select hierarchy alt](https://www.eternal-september.org/groups.php?hierarchy=alt) | alt | Usenet alternative newsgroups | 8728 |
  - [4] 2026-11-19: the free.* hierarchy has 1284 groups | capture: sha256:c5ebfe2498be23aeb81d6d586670eb7bcfca660cafedf6b718a4804a6a14f3c6 | quote: | [Select hierarchy free](https://www.eternal-september.org/groups.php?hierarchy=free) | free | entirely unregulated newsgroups | 1284 |
  - [5] 2026-11-19: registration requires a UserID and an email address, no phone number or card | capture: sha256:f05966cd603c305db358847039e209fa24ebc0468477600982fc22fc196af81c | quote: Please enter a UserID and an email address, where you can be reached.
- sources:
  - [1] https://www.eternal-september.org/
  - [2] https://www.eternal-september.org/index.php?showpage=terms
  - [3] https://www.eternal-september.org/index.php?showpage=faq
  - [4] https://www.eternal-september.org/hierarchies.php
  - [5] https://www.eternal-september.org/RegisterNewsAccount.php

## usenet / nntp free providers

- `storage/usenet-nntp-free-providers` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:31.026Z (live) | stale on 2026-12-04
- url https://www.eternal-september.org/
- free tier: none reachable: No free binary provider with usable retention exists. The only genuinely free, posting-allowed server found (Eternal September) is text-only, explicitly 'no binaries', with 130-day… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: No free binary provider with usable retention exists. The only genuinely free, posting-allowed server found (Eternal September) is text-only, explicitly 'no binaries', with 130-day…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: No free binary provider with usable retention exists. The only genuinely free, posting-allowed server found (Eternal September) is text-only, explicitly 'no binaries', with 130-day…
  - [2] 2026-10-21: cited as the basis of the rejection: No free binary provider with usable retention exists. The only genuinely free, posting-allowed server found (Eternal September) is text-only, explicitly 'no binaries', with 130-day retention
  - [1] 2026-11-19: the free service is text-only and requires online registration | capture: sha256:7a1903f315603c844b0f1e983afce585b06276693328d88535074d2a00323b5d | quote: news.eternal-september.org provides free read and write access to all text newsgroups. It requires a registration that can be done [online.](https://www.eternal-september.org/RegisterNewsAccount.php)
  - [1] 2026-11-19: the free server explicitly carries no binaries | capture: sha256:7a1903f315603c844b0f1e983afce585b06276693328d88535074d2a00323b5d | quote: alt.* (approx. 8000 groups, no binaries)
  - [1] 2026-11-19: the alt.* retention is 130 days, matching the recorded value | capture: sha256:7a1903f315603c844b0f1e983afce585b06276693328d88535074d2a00323b5d | quote: Retention is currently 3 years for de.*, 160 days for the Big 8, 130 days for alt.* and 90 days for other hierarchies.
- sources:
  - [1] https://www.eternal-september.org/
  - [2] https://4usenet.com/articles/best-free-usenet
