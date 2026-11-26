# Wercker

> wercker.com | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wercker/ | JSON https://fshy.ajam.dev/api/v1/entity/wercker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Wercker

- `ci-cd-runners/wercker` | dead | evidence documented | binding volume-quota | category CI runner
- needs card no, phone no, ID no, institution no | verified 2026-11-19T01:04:34.809Z (live) | stale on 2026-12-20
- url https://devcenter.wercker.com/
- free tier: none: the Wercker service was shut down on October 31st, 2022; no free hosted runner remains | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: before shutdown a free tier existed, but the first-party pricing page is gone and no build-minute number could be verified from a first-party page; no number is stated here
- per-object cap: not applicable: the hosted service no longer exists | source: [1]
- retention: not applicable: the hosted service no longer exists | source: [1]
- egress: not applicable: the hosted service no longer exists; no egress terms could be read | metered: no | source: [2]
- identity: email | detail: not obtainable: the hosted service was shut down. Historically the first-party docs offered a Sign in with GitHub button and a Get started for free button; registration with a username, email address and password with email activation is reported by a non-first-party source and is unverified from a first-party page. No card requirement is stated on a first-party page
- interface: git
- limits:
  - volume-quota (binding): none: the hosted service was shut down on October 31st, 2022 [1]
- binding note: the withdrawal of the service binds before any internal build limit: no hosted capacity can be obtained at any scale
- interface detail: historically a push to a connected GitHub, GitLab or Bitbucket repository started a build defined in a wercker.yml file; the first-party docs listed Steps, Pipelines, Workflows and wercker.yml sections
- endpoint: unverified: the former app.wercker.com endpoint is no longer reachable
- tooling: historically the user connected a Git repository and added a wercker.yml file to the repository root; a Wercker CLI could replicate the build locally. No hosted runner is reachable now
- composes with: historically a Git push triggered a build and a pipeline could deploy the built container; the successor OCI DevOps has no free build resource for an always-free account, so it is not a like-for-like free replacement. The product was a hosted runner, not self-hosted software the reader installs
- reliability: the first-party docs host devcenter.wercker.com failed the TLS handshake with tlsv1 alert internal error on 2026-11-19; the service shutdown was announced for October 31st, 2022
- notes: Wercker was a hosted CI/CD runner, never software the reader installs. The historical free build-minute allowance is unverified: the first-party pricing page redirected to Oracle and could not be read, and no number is proposed. A separate first-party shutdown notice on devcenter.wercker.com was named in third-party reports but the host no longer serves TLS, so the shutdown quote is taken from a third-party preservation and marked as such in confidence_note.
- evidence note: the shutdown date is quoted from the vendor notice preserved on a third-party tracker; the first-party docs entry point failed the TLS handshake in the probe on 2026-11-19. The historical free allowance in build minutes is unverified: the first-party pricing page redirects to Oracle and could not be read
- evidence:
  - [1] 2026-11-19: the vendor shutdown notice, preserved verbatim on a third-party issue, states the Wercker service ended on October 31st, 2022 | capture: sha256:d3f68f4ba42f76ed1f9d04ad75cfe25728eddbf6bce89ca1641606258071047c | quote: Important Notice: Wercker service will be shutdown on October 31st, 2022 . We recommend you to use OCI DevOps service
  - [1] 2026-11-19: the recommended replacement has no free build resource, so there is no free like-for-like successor | capture: sha256:d3f68f4ba42f76ed1f9d04ad75cfe25728eddbf6bce89ca1641606258071047c | quote: OCI DevOps doesn't have a free build resource for free-tier "always free" account types; if you migrate to OCIDevOps, you will need a paid Oracle Cloud account
  - [3] 2026-11-19: the first-party docs described Wercker as a hosted CI/CD product with Steps, Pipelines, Workflows and wercker.yml | capture: sha256:fc4795c6d7ece2f486f46c1298b71d68dce6bd71e7063f6f6f022bb74714f05a | quote: Welcome to the Wercker Documentation!
  - [3] 2026-11-19: the first-party sign-in control offered GitHub authentication | capture: sha256:fc4795c6d7ece2f486f46c1298b71d68dce6bd71e7063f6f6f022bb74714f05a | quote: alt="Sign in with GitHub"
  - probe:https://devcenter.wercker.com/ 2026-11-19: the first-party docs host failed the TLS handshake on 2026-11-19, consistent with a withdrawn service | capture: sha256:62b1f2a9267295a83ff667115e1f11281724ef7616ea54207e86597a52af8d73 | quote: "error": "tls_error"
- sources:
  - [1] https://github.com/checkstyle/checkstyle/issues/11564
  - [2] https://devcenter.wercker.com/
  - [3] https://devcenter.wercker.com/docs/
