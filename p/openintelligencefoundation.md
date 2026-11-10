# Open Intelligence Foundation

> openintelligencefoundation.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openintelligencefoundation/ | JSON https://fshy.ajam.dev/api/v1/entity/openintelligencefoundation.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Open Intelligence Foundation

- `compute/open-intelligence-foundation` | qualifies-with-caveat | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://openintelligencefoundation.ai/request-funding.html
- free tier: The application is a single web form with eight fields, none institutional. Quoted labels from the page: 'Your Name *', 'Email *', 'Twitter/X Handle', 'GitHub Profile', 'Project Name *', 'Project Description *', 'Funding Amount Needed *', 'Primary Use of Funds *' with the options 'GPUs/Compute Credits / Equipment/Hardware / Conference/Travel / Living Expenses / Software/Tools / Other', and 'Supporting Documents (Optional) ... (PDF, DOC, DOCX, TXT - Max 10MB)'. Only name, email, project name, project description, amount and use are marked required; X handle and GitHub are optional. The stated ceiling is 'Up to $10,000 per grant - Larger grants available for select projects'. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: name plus email address. Whether payout mechanics actually reach a non-US bank is not stated anywhere and is the open question.
- interface: rest
- limits:
  - write-gated (binding): a discretionary human decision on an eight-field form is the only gate, and the published page sets no award count, no pool size and no acceptance rate, so the probability of an award is unknown and cannot be planned against. [1]
- limits note: a discretionary human decision on an eight-field form is the only gate, and the published page sets no award count, no pool size and no acceptance rate, so the probability of an award is unknown and cannot be planned against.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the one award in the class that can be spent anywhere, because the use-of-funds list includes 'Living Expenses' and 'Equipment/Hardware' beside compute: cash from it buys whichever vendor prices the workload cheapest, so it composes with every other record in documented records rather than locking the award to one vendor's credit.
- reliability: no reliability event recorded
- notes: The form's own use-of-funds list and both published awards show this is not compute credit, and the money is not necessarily compute at all. The site's own footer says 'Independently operated, not yet 501(c)(3)', so it is not a registered US charity and no 990 filing exists to check its finances against.
- extras:
  - facets.class: independent-grant
  - facets.free_tier_kind: one-time-grant
- evidence:
  - [1] 2026-10-22: the complete field list quoted above, read from the served HTML source; the form is a plain POST with enctype multipart/form-data to the endpoint https://oif-forms.move37-dns.workers.dev, carrying _form_type=funding and a honeypot field; no third-party form vendor, no captcha element and no payment-provider element appears in the 24,452-byte page; probe status 200, sha256 41c7acc5d202c5558f862affb8ab045ee71bec4feb2a523e07589364f2d5f7e6, last-modified 2026-06-02
  - [2] 2026-10-22: 'Up to $10,000 per grant - Larger grants available for select projects'; 'We review your application within a few days - no committees, no bureaucracy'; '100% of donations go to builders, zero fees'; 'No reporting requirements. Come back when you need more support'; 'Global by design. Intelligence has no borders. We fund builders anywhere in the world'; 'No equity, no control, no board seats', quoted; page 200
  - [3] 2026-10-22: the post-submission page states the cadence: 'Within 24 hours: You'll receive an email confirmation', '2-3 days: Our team reviews your submission', 'Within 1 week: We'll reach out with next steps'; the contact address on that page is obfuscated by Cloudflare email-protection and is a personal address, not a grants desk
  - [4] 2026-10-22: the form backend is live and rejects GET with 'HTTP/1.1 405 Method Not Allowed' and Content-Type text/plain, so the endpoint exists and answers only to POST; this establishes the submission path is operating, not a dead action attribute
  - [5] 2026-06-23: the grantee's own comment, quoted: 'The 410+ new MLX models were built on a Mac Studio that the Open Intelligence Foundation donated to us', with the foundation's short link oif.to in the same comment; the grantee's profile lists an institutional post, so grantee 2 holds one while being described as an independent builder
  - [2] 2026-10-22: the featured-projects block labels the two awards 'GPU Funding' for the first grantee and 'Compute Funding' for the second grantee, and reads 'More projects coming soon', quoted; page 200
  - [6] 2026-10-22: the sponsorship page: '100% of your contribution goes directly to funding projects'; tiers 'Supporter ($1,000+)', 'Champion ($10,000+)', 'Visionary ($50,000+)', 'Founding Partner ($100,000+)'; fields are name, email, 'Company/Organization', tier, amount, message and a 'Public recognition / Remain anonymous' choice, quoted; page 200
  - [2] 2026-10-22: the sponsors block names exactly one sponsor, 'CRS Credit API', marked 'FOUNDING SPONSOR', described as 'Providing world-class credit infrastructure for modern fintech companies'; no other sponsor is listed, quoted; page 200
  - [1] 2026-10-22: the footer states '2025 Open Intelligence Foundation. Independently operated, not yet 501(c)(3).' and names a co-founder and CTO, linking to a personal social profile and to crscreditapi.com, quoted from the served HTML
  - [2] 2026-10-22: 'Up to $10,000 per grant - Larger grants available for select projects', 'rapid, no-strings-attached funding to independent AI builders', 'We review your application within a few days - no committees, no bureaucracy', 'No reporting requirements', quoted; page 200
  - [1] 2026-10-22: the funding form's fields: name, email, X handle, GitHub profile, project name and description, funding amount needed, primary use of funds with 'GPUs/Compute Credits' as a listed option, optional supporting documents; page 200; no institution, degree or publication field appears
  - [7] 2026-10-22: the founding announcement: the programme was founded by the CTO of the sponsor company CRS Credit API, and the page announces the first grantee
  - [8] 2026-10-22: 
  - [7] 2026-10-22: 
- sources:
  - [1] https://openintelligencefoundation.ai/request-funding.html
  - [2] https://openintelligencefoundation.ai/
  - [3] https://openintelligencefoundation.ai/thank-you.html
  - [4] https://oif-forms.move37-dns.workers.dev
  - [5] https://www.linkedin.com/posts/maziyarpanahi_650-clinical-ai-models-now-run-on-your-iphone-activity-7475097768534130688-_IW7
  - [6] https://openintelligencefoundation.ai/become-sponsor.html
  - [7] https://crscreditapi.com/open-intelligence-foundation-first-grantee-prince-canuma
  - [8] https://web.archive.org/web/20260227150928/https://openintelligencefoundation.ai/?provider=wayback
