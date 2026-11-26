# Codeship

> cloudbees.com | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudbees/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudbees.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Codeship

- `ci-cd-runners/codeship` | dead | evidence documented | binding write-gated | category CI runner | tier historical hosted CI service (end of life)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T00:19:24.678Z (live) | stale on 2026-12-20
- url https://docs.cloudbees.com/docs/cloudbees-codeship/latest/api-authentication/
- free tier: unverified: no first-party page read states a standing free allowance for private projects. The last published first-party price list starts at USD 49 per month (CodeShip Basic Starter). A former free tier for public open-source projects is described by third parties only and is not established here | unit: none | metered on: unstated | read on: 2026-11-19 | source: [1] | note: The preserved pricing page lists paid tiers of USD 49, USD 99 and USD 399 per month. The unit is none because no standing free allowance is established; a paid-only tier is not a free tier. A USD price is quoted with its ISO 4217 code.
- per-object cap: unverified: no per-object cap is stated on the pages read; the service ran builds rather than storing objects | source: [2]
- retention: unverified: no build or build-log retention period is stated on the pages read | source: [2]
- egress: unverified: no egress allowance or per-gigabyte price is stated on the pages read. The preserved pricing page describes build concurrency and parallel test pipelines, not network egress | metered: no | source: [1]
- identity: email | detail: A password account on CodeShip was required; a GitHub, GitLab or Bitbucket account alone would not work for API users, and accounts with two-factor authentication would not work. New users were invited by email address. No sign-up was performed and no card or phone requirement is established from the page read
- interface: git, rest
- limits:
  - write-gated (binding): As of January 2026, CloudBees no longer supports the CloudBees CodeShip product, so no new build can be started [2]
  - request-rate: historical paid tiers named 1, 2 or 4 concurrent builds and 2 or 4 parallel test pipelines [1]
- limits note: Concurrency figures come from the preserved paid price list and describe the retired paid tiers, not a live allowance.
- binding note: The end-of-life notice stops new builds for every tier, so product discontinuation binds before any historical concurrency figure.
- interface detail: A REST API v2 under api.codeship.com let a client list projects, trigger builds and inspect pipelines. Access to the API used a token obtained by Basic Auth from the authentication endpoint; the API is documented as part of the now unsupported product.
- endpoint: https://api.codeship.com/v2/
- tooling: A hosted CI service reached through a web console, a connected source-control repository and the REST API. A project member with a password account invoked the API with a bearer token; no client binary was supplied by the pages read.
- composes with: A push to a connected repository started a build; the API could trigger and inspect builds. The service reached end of life and CloudBees directs users to migrate to CloudBees Unify, so this chain no longer runs on Codeship.
- reliability: The hosted product reached end of life; CloudBees states that it no longer supports CodeShip and recommends migration to CloudBees Unify.
- notes: A hosted CI service that was discontinued. Both CodeShip Basic and CodeShip Pro ran on the CloudBees platform and are covered by one end-of-life notice, so one record holds the provider. A later successor, CloudBees Unify, is a distinct offer with no first-party free allowance established here.
- evidence note: The end-of-life notice and the API documentation are first-party CloudBees pages captured and quoted. No build was run and no account was opened. No first-party page read states a recurring free allowance for private projects, so the historical free tier is unverified from a first-party source.
- evidence:
  - [2] 2026-11-19: the CodeShip product reached end of life and is unsupported | capture: sha256:66aabbaf5448a87a6b7c878e1466b55df683787913cebe829e547020221093c3 | quote: As of January 2026, CloudBees no longer supports the CloudBees CodeShip product.
  - [2] 2026-11-19: the vendor directs users to migrate to CloudBees Unify | capture: sha256:66aabbaf5448a87a6b7c878e1466b55df683787913cebe829e547020221093c3 | quote: CloudBees recommends migrating to CloudBees Unify, which provides a modern, scalable, and secure CI/CD platform with enhanced features and capabilities. For more information about CloudBees Unify and how it can benefit your organization, please visit the [CloudBees Unify product page](https://www.cloudbees.com/unify).
  - [3] 2026-11-19: a password account was required for API access; social login alone was not sufficient | capture: sha256:28dfa81803d008852309e2f0921e0d7388e3c135fcf4f3bef886d886a0450330 | quote: Users that want to access the API also need to have a password account on CodeShip, so regular GitHub/GitLab/Bitbucket accounts will not work.
  - [3] 2026-11-19: new API users were invited by email address | capture: sha256:28dfa81803d008852309e2f0921e0d7388e3c135fcf4f3bef886d886a0450330 | quote: To create a new user, simply invite them using an appropriate email address.
  - [3] 2026-11-19: API access used a token obtained through Basic Auth | capture: sha256:28dfa81803d008852309e2f0921e0d7388e3c135fcf4f3bef886d886a0450330 | quote: The authentication endpoint uses [Basic Auth](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#basic_authentication_scheme) to authenticate the user and return an auth token.
  - [1] 2026-11-19: the preserved first-party price list starts at USD 49 per month with one concurrent build | capture: sha256:4a1ec7540fe31cca4f06b36f632faf382a03f00178810a628a138326e9d1a383 | quote: ### $49/MO #### Starter For the individual who wants to test and deploy with CodeShip. Unlimited builds 1 Concurrent Builds 2 Parallel Test Pipelines
- sources:
  - [1] https://web.archive.org/web/20240930103228/https://codeship.com/pricing
  - [2] https://docs.cloudbees.com/docs/cloudbees-codeship/latest/api-authentication/
  - [3] https://web.archive.org/web/20250602134714/https://docs.cloudbees.com/docs/cloudbees-codeship/latest/api-authentication/
