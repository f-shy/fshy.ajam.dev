# Garnix

> garnix.io | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/garnix/ | JSON https://fshy.ajam.dev/api/v1/entity/garnix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Garnix

- `ci-cd-runners/garnix` | dead | evidence measured | binding none | category CI runner | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:00:40.516Z (live) | stale on 2026-12-20
- url https://garnix.io/pricing
- free tier: none: the hosted service shut down on 2026-07-15. The pricing page still lists a Free plan of 1,500 CI minutes a month with 500 pull-request deployment minutes, an Individual plan at USD 25 a month with 10,000 minutes, and USD 0.006 per additional minute, but the sign-up host app.garnix.io does not resolve | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the listed plans are not purchasable; they are kept here as the former offer
- per-object cap: former caps: 2 hours per build and 30 minutes without output; the Nix eval stage was limited to 4GB | source: [2] | note: the service is gone; these caps describe the former hosted runner
- retention: all user data, build artifacts included, was deleted on 2026-07-15 | source: [1]
- egress: not applicable: the build and cache hosts no longer resolve | metered: no | source: [1]
- identity: email | detail: not applicable now: the sign-up host app.garnix.io does not resolve. The former service was reached by installing the garnix GitHub App on a GitHub org or account
- interface: git
- limits:
  - retention-clamped: all user data and build artifacts deleted on 2026-07-15 [1]
  - per-object-cap: former cap: 2 hours per build, 30 minutes without output [2]
  - request-rate: former Free plan: 1,500 CI minutes a month; USD 0.006 per additional minute [3]
- limits note: there is no allowance to bind: the hosted service is gone
- binding note: there is no service to bind: the sign-up and cache hosts answer NXDOMAIN
- interface detail: the former service built the flake outputs of a GitHub repository that had the garnix GitHub App installed and a top-level flake.nix; only x86_64-linux was enabled by default
- tooling: a flake.nix and the garnix GitHub App; app.garnix.io and cache.garnix.io no longer resolve
- composes with: none: the hosted service is gone, and the hosted runners of this topic replace it
- reliability: app.garnix.io and cache.garnix.io answer NXDOMAIN while the garnix.io marketing pages and the pricing table still serve
- notes: Rejected as a CI runner service: the hosted service ended on 2026-07-15, two months after the 2026-05-28 announcement, and its data was deleted the same day. The former Free plan was 1,500 CI minutes a month and the former price USD 0.006 per further minute; neither can be bought. Any hosted runner in this topic comes first. Last resort: the code is published as garnix-io/garnix-ci, which the user would install and run on a rented or free machine; a public community instance is unverified.
- evidence note: the shutdown date and the deletion of user data are quoted from the vendor's own announcement; the sign-up host and the binary cache host were resolved through a public DNS-over-HTTPS resolver on 2026-10-30 and both answered NXDOMAIN
- self hosted: no
- evidence:
  - [1] 2026-10-30: the hosted service shut down on 2026-07-15 | capture: sha256:a63f18465e334664605df9bbcedb4721c1fb78db040ea3397a3c7a11ced68880 | quote: Sadly, as part of this transition, the hosted garnix service will shut down on July 15th 2026.
  - [1] 2026-10-30: all user data, build artifacts included, was deleted on 2026-07-15 | capture: sha256:a63f18465e334664605df9bbcedb4721c1fb78db040ea3397a3c7a11ced68880 | quote: We will also be deleting all user data on July 15th. This includes build artifacts.
  - [4] 2026-10-30: the shutdown announcement is dated 2026-05-28 | capture: sha256:06cf77d74e83b9c75eb7da39671f35b425d8dbad2cf5f97e1f98ba4fbde08a9a | quote: May 28, 2026Alex David, Sönke Hahn and Julian K. Arni
  - probe:https://dns.google/resolve?name=app.garnix.io&type=A 2026-10-30: the sign-up and dashboard host app.garnix.io answers NXDOMAIN | capture: sha256:0858481160b13f6a58159040be99f67c346fc70c6571bfd7989ad8674173c3e5 | quote: "Status":3
  - probe:https://dns.google/resolve?name=cache.garnix.io&type=A 2026-10-30: the binary cache host cache.garnix.io answers NXDOMAIN | capture: sha256:a3685e428c177686c6416cbdc2c740a8108215b2af476f8fbcdf179808ebbfbf | quote: "Status":3
  - probe:https://app.garnix.io/signup 2026-10-30: a GET of the sign-up page fails on name resolution | capture: sha256:b05f1ff6e1fac73e129f3a77db05e4fce89f39c80996f9882dca299a48b363f3 | quote: "error": "dns"
  - [3] 2026-10-30: the pricing page still lists a Free plan of 1,500 minutes a month | capture: sha256:3a7323e9843f0d1a812d29b31e3a371e1f6a39766668c70aba6580907b4861d8 | quote: 1,500 minutes/month
  - [3] 2026-10-30: the listed price per additional minute is USD 0.006 | capture: sha256:3a7323e9843f0d1a812d29b31e3a371e1f6a39766668c70aba6580907b4861d8 | quote: Additional minutes (both CI and pull-request deployment) beyond those included in the plan are priced at 0.006 USD per minute.
  - [3] 2026-10-30: the Individual plan listed USD 25 a month | capture: sha256:3a7323e9843f0d1a812d29b31e3a371e1f6a39766668c70aba6580907b4861d8 | quote: $25/month
  - [3] 2026-10-30: the Individual plan listed 10,000 minutes a month | capture: sha256:3a7323e9843f0d1a812d29b31e3a371e1f6a39766668c70aba6580907b4861d8 | quote: 10,000 minutes/month
  - [3] 2026-10-30: the Free plan listed 500 pull-request deployment minutes | capture: sha256:3a7323e9843f0d1a812d29b31e3a371e1f6a39766668c70aba6580907b4861d8 | quote: 500 pull-request deployment minutes
  - [2] 2026-10-30: a build was capped at 2 hours in total and 30 minutes without output | capture: sha256:7304c5c7f60a3ad8c7d2464c39386f78d04770ee5f23dc3fcd86bc203990782f | quote: I also set max-silent-time (the amount of time that can pass without a line printed to stdout or stderr before a build is stopped) to 30 minutes and timeout (the total amount of time a build is allowed to take) to 2 hours.
  - [5] 2026-10-30: the Nix eval stage was limited to 4GB | capture: sha256:4c7df5b730c43a1768773a0d26f2301c6e60791915233ee65d1b39e21fdf917c | quote: The eval stage is limited to 4GB.
  - [6] 2026-10-30: the default configuration built only x86_64-linux | capture: sha256:01c7d9e1b7918d29332209fb40605f3a1d157c61855218a0b5ab42f1951c1845 | quote: As you can see, the default configuration values only enable x86_64-linux builds.
  - [7] 2026-10-30: the service was reached through the garnix GitHub App on a GitHub org or account | capture: sha256:1fd7275477304d02501b053d1720aba15e07da33af6ec16c689fe0170a443276 | quote: Select a GitHub org or account.
  - [8] 2026-10-30: the service code is published as garnix-io/garnix-ci, a CI for flake-based GitHub repositories | capture: sha256:8464b7fb0bb8869685c56cb1fb91f1bfd7e25c321cfd3870590e6ba7708c33ab | quote: Garnix is a CI service for nixified, flake-based github repos.
  - [1] 2026-11-03: the hosted garnix service shut down on 2026-07-15 | capture: sha256:a63f18465e334664605df9bbcedb4721c1fb78db040ea3397a3c7a11ced68880 | quote: Sadly, as part of this transition, the hosted garnix service will shut down on July 15th 2026.
  - probe:https://app.garnix.io/signup 2026-11-03: the sign-up host fails name resolution on 2026-11-03 | capture: sha256:257f6d2bad93cbe127a470a87e04cf7747b07a8e92c7eced7dab434044957af6 | quote: "error": "dns"
  - [1] 2026-11-04: the hosted service shut down on 2026-07-15, so the free tier is none | capture: sha256:a63f18465e334664605df9bbcedb4721c1fb78db040ea3397a3c7a11ced68880 | quote: Sadly, as part of this transition, the hosted garnix service will shut down on July 15th 2026.
- sources:
  - [1] https://garnix.io/blog/shutting-down/
  - [2] https://garnix.io/blog/october-1-release-notes/
  - [3] https://garnix.io/pricing
  - [4] https://garnix.io/blog/
  - [5] https://garnix.io/docs/ci/steps/
  - [6] https://garnix.io/docs/ci/yaml_config/
  - [7] https://garnix.io/docs/getting-started/github-app/
  - [8] https://github.com/garnix-io/garnix-ci
