# Airtop

> airtop.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/airtop/ | JSON https://fshy.ajam.dev/api/v1/entity/airtop.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Airtop

- `compute/airtop` | dead | evidence documented | binding request-rate | category browser host
- needs card unknown, phone yes, ID no, institution no | verified 2026-11-06T17:48:23.918Z (live) | stale on 2026-12-07
- url https://www.airtop.ai/pricing
- free tier: Free at $0/mo with 1,000 credits a month plus a 10,000-credit one-time bonus; the bonus is a 7-day trial or until the credits are consumed | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://www.airtop.ai/pricing states credits and simultaneous sessions and no egress allowance or overage price | metered: no | source: [1]
- identity: email | detail: email: the sign-in form labels its account field 'Email' ('<label for="loginId" class="text-[13px] font-medium text-black/50 tracking-tight leading-tight">Email</label>'), and the terms require an account with a username, a password and contact information ('You may be required to sign up for an account, select a password and username ("Airtop User ID"), and provide us with certain information or data, such as your contact information.'). A phone number is optional: 'By signing up for the Services and providing us with your wireless number, you confirm that you want Airtop to send you information regarding your account or transactions with us'. A card is not published: https://www.airtop.ai/pricing lists a $0 Free plan and states no card requirement, and registration is closed ('we’re no longer accepting new signups'), so the sign-up form was not read. Country: not published at https://www.airtop.ai/pricing.
- interface: rest
- limits:
  - request-rate (binding): 1,000 credits a month on Free; the 10,000-credit bonus expires after 7 days or when consumed [1]
- interface detail: HTTP API with Node.js and Python SDKs (client.sessions.create); Playwright, Puppeteer and Selenium drive the cloud browser
- tooling: Node.js and Python SDKs; Playwright, Puppeteer and Selenium integrations
- composes with: not established
- reliability: the service shuts down on 2026-11-13 and new signups are already closed
- notes: registration closes before the shutdown on 2026-11-13, so no new account can reach the free credits
- evidence note: the pricing page was read on 2026-10-22 and states the free tier and both paid tiers; the free allowance is denominated in credits, which buy browser-session time, so the unit is mixed and not a wall-clock hour. The sign-up page read on 2026-11-04 refuses new signups ahead of the shutdown on 2026-11-13
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the page states no session cap; the 7-day clock applies to the credit bonus, not to a session
  - free_tier_kind: recurring-credit
  - death.on: 2026-11-04
  - death.cause: registration-closed
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free $0/mo · 1,000 Credits · 10,000 one-time credit bonus · Mark trial for 7 days or until credits are consumed'; paid tiers $29/mo and $189/mo, quoted
  - [2] 2026-11-03: the documentation supports Playwright, Puppeteer and Selenium alongside an HTTP API with Node and Python SDK calls | capture: sha256:6aa21814087081295458bd9ab3d1995995f2e7a19f231cd880d450f7cb75bffa | quote: We fully support Playwright, Puppeteer, and Selenium scripts
  - [1] 2026-11-03: pricing is in credits and simultaneous sessions; no egress allowance or overage price is stated | capture: sha256:f48d751ace368b39538ace54dceb56e2bb996f8085480db5122198686a1541e9 | quote: 10,000 one-time credit bonus
  - [3] 2026-11-04: the terms require an account with a username, a password and contact information | capture: sha256:d751cf8899bfe6d156f024f38bf1711ac65f48c809930bd58b39f67e3e225d4b | quote: You may be required to sign up for an account, select a password and username ("Airtop User ID"), and provide us with certain information or data, such as your contact information.
  - [4] 2026-11-04: new signups are refused ahead of the shutdown | capture: sha256:7a0edef2055411c2b1f62ed36e832a8cbc563c834ce8a2d564dc034474870cdc | quote: we’re no longer accepting new signups or upgrades to paid or higher-tier plans
  - [4] 2026-11-04: the free tier can no longer be obtained by a new account | capture: sha256:7a0edef2055411c2b1f62ed36e832a8cbc563c834ce8a2d564dc034474870cdc | quote: we’re no longer accepting new signups or upgrades to paid or higher-tier plans
  - [4] 2026-11-04: the service ends on 2026-11-13 and signups stop first | capture: sha256:7a0edef2055411c2b1f62ed36e832a8cbc563c834ce8a2d564dc034474870cdc | quote: Airtop is shutting down on November 13, 2026.
  - [4] 2026-11-04: the vendor announces the service ends on 2026-11-13 | capture: sha256:7a0edef2055411c2b1f62ed36e832a8cbc563c834ce8a2d564dc034474870cdc | quote: Airtop is shutting down on November 13, 2026.
  - [4] 2026-11-04: registration is closed, so the identity gate cannot be walked | capture: sha256:7a0edef2055411c2b1f62ed36e832a8cbc563c834ce8a2d564dc034474870cdc | quote: As we prepare to say goodbye, we’re no longer accepting new signups or upgrades to paid or higher-tier plans.
  - [5] 2026-11-06: the sign-in form's account field is an email address | capture: sha256:a18f087ae017dc6ade813f4c8583d49e4c66882472784a1b697bc5288ac11f5f | quote: <input id="loginId" type="text" name="loginId" value="" autocapitalize="none" autocomplete="username" autocorrect="off" spellcheck="false" autofocus="autofocus" placeholder="[address removed]"
  - [3] 2026-11-06: the terms require an account with a username, a password and contact information | capture: sha256:d751cf8899bfe6d156f024f38bf1711ac65f48c809930bd58b39f67e3e225d4b | quote: You may be required to sign up for an account, select a password and username ("Airtop User ID"), and provide us with certain information or data, such as your contact information.
  - [3] 2026-11-06: a wireless number is provided voluntarily, so a phone is optional | capture: sha256:d751cf8899bfe6d156f024f38bf1711ac65f48c809930bd58b39f67e3e225d4b | quote: By signing up for the Services and providing us with your wireless number, you confirm that you want Airtop to send you information regarding your account or transactions with us
  - [1] 2026-11-06: the Free plan is priced at $0 a month | capture: sha256:f48d751ace368b39538ace54dceb56e2bb996f8085480db5122198686a1541e9 | quote: $0/mo
  - [4] 2026-11-06: registration is closed, so the sign-up form cannot be read | capture: sha256:7a0edef2055411c2b1f62ed36e832a8cbc563c834ce8a2d564dc034474870cdc | quote: we’re no longer accepting new signups or upgrades to paid or higher-tier plans
  - [5] 2026-11-06: the account identifier the sign-in form asks for is an email address | capture: sha256:a18f087ae017dc6ade813f4c8583d49e4c66882472784a1b697bc5288ac11f5f | quote: <input id="loginId" type="text" name="loginId" value="" autocapitalize="none" autocomplete="username" autocorrect="off" spellcheck="false" autofocus="autofocus" placeholder="[address removed]"
- sources:
  - [1] https://www.airtop.ai/pricing
  - [2] https://docs.airtop.ai/
  - [3] https://www.airtop.ai/tos
  - [4] https://portal.airtop.ai/sign-up
  - [5] https://portal.airtop.ai/api/sign-in
