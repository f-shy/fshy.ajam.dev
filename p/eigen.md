# The Eigenprize

> eigen.build | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eigen/ | JSON https://fshy.ajam.dev/api/v1/entity/eigen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## The Eigenprize

- `compute/the-eigenprize` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://eigen.build/winners.html
- free tier: 'No-strings-attached prize money for talented builders, scientists, operators', distributed as '1st prize $100,000', '2nd prize $30,000', '3rd prize $20,000', '4th - 23rd $5,000 ea.', totalling '$250,000' across 23 winners. Eligibility is the widest found in this class, quoted: 'Anyone who builds things, discovers things, or does things ... There is no limit on age, interest, location, etc.' The conditions are removed explicitly: 'You can spend the money however you want. We take no equity and have zero expectations.' and 'What do I have to do if I win? Nothing!' The application 'is designed to take 5-10 minutes'. The cycle is complete and paid: the site now reads 'The winners have been selected.' | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: an individual of any age in any country. 'There is no limit on age, interest, location, etc.' The first prize went to a recipient outside the United States and without an institutional affiliation.
- interface: unknown
- limits:
  - write-gated (binding): a one-shot competitive prize decided by three organisers fails first: 23 winners from an unpublished applicant count, in a cycle that closed on 2026-03-31, so there is no open application route today and the odds cannot be computed. [1]
- limits note: a one-shot competitive prize decided by three organisers fails first: 23 winners from an unpublished applicant count, in a cycle that closed on 2026-03-31, so there is no open application route today and the odds cannot be computed.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Cash with no spending restriction and no equity, so it composes with every other record: the USD 100,000 first prize is roughly 20 to 100 times the largest compute credit in documented records and can be spent at spot or marketplace rates the recipient chooses. The USD 5,000 floor for 20 of 23 winners is the part worth planning around, because it is the modal award and it is still five times the typical vendor starter credit.
- reliability: no reliability event recorded
- notes: The best-evidenced award in this class and the one to promote first, because payment is not a claim but a published list of 23 named people with amounts beside them. Two properties make it stronger than the Open Intelligence Foundation offer: the programme page names the removals explicitly ('no equity', 'zero expectations', 'nothing' required after winning), and one winner is observably outside the United States and unaffiliated. The failure mode is that the cycle is closed and the programme is three individuals, not an institution: the prize pool is described as money they pooled, the site is a static page, and the winners page closes with 'See you next time' rather than a date. So the finding is a closed cycle worth watching for the next one, not an open door. A recurring cadence is implied by 'See you next time' and by the Duct Tape Prize predecessor, and by a 'Remind me. We'll email you near the deadline' control, but no next-round date was published on any page read, so treat recurrence as likely rather than promised. Reachability note: eigenprize.build answered through a rendering provider while the origin itself timed out twice, and a mirror at eigen.build served the current content with status 200.
- extras:
  - facets.class: independent-grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: the winners page lists the podium and the field by name: First Prize at '$100,000', Second Prize at '$30,000', Third Prize at '$20,000', then twenty rows at '$5,000' each; page 200. This is a published list of named recipients, not a testimonial
  - [2] 2026-10-22: 'The winners have been selected.'; the prize table '1st prize $100,000 / 2nd prize $30,000 / 3rd prize $20,000 / 4th - 23rd $5,000 ea. / $250,000'; 'Apply. 5 - 15 mins.'; 'Nominate. $1,000 for successful nominations!'; quoted; page 200
  - [3] 2026-10-22: the programme's own terms, read through a rendering provider because the origin does not answer directly: 'Anyone who builds things, discovers things, or does things. If you are applying as a team, the prize will be shared amongst the group. There is no limit on age, interest, location, etc.'; 'You can spend the money however you want. We take no equity and have zero expectations.'; 'What do I have to do if I win? Nothing!'; 'When we ran the Duct Tape Prize and gave away 50k to builders, we met some remarkable people who did remarkable things with the money. We're scaling it up now', quoted
  - [4] 2026-10-22: 
  - [5] 2026-10-22: 
- sources:
  - [1] https://eigen.build/winners.html
  - [2] https://eigen.build/
  - [3] https://eigenprize.build/
  - [4] https://nitter.jaydenha.uk/thewildstevenp/status/2032977531557536169
  - [5] https://nitter.rdrama.net/thewildstevenp/status/2029602933470306450
