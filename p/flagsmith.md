# Flagsmith

> flagsmith.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flagsmith/ | JSON https://fshy.ajam.dev/api/v1/entity/flagsmith.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Flagsmith

- `dev-services/flagsmith` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted feature flags and remote config | tier Free
- needs card no, phone unknown, ID no, institution no | verified 2026-11-02T00:37:55.412Z (live) | stale on 2026-12-03
- url https://www.flagsmith.com/pricing
- free tier: Free: up to 50,000 requests a month, 1 team member, 1 project, unlimited feature flags, environments, identities and segments, up to 100,000 users in experiments, API access | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: Only /flags, /identities, /traits and /environment-document count; one SDK instantiation that fetches flags is one request. Over the limit a free account is warned by email, and 7 days later the API stops answering until 30 days after the warning or an upgrade. Each project holds up to 1000 features and 500 segments.
- per-object cap: a flag string value is at most 20,000 bytes and an identity trait value at most 2,000 bytes | bytes: 20000 | source: [2]
- retention: unverified: no retention period for flags, identities or audit logs on the Free plan is stated on the pages read
- egress: not applicable: a flag service metered by request count; no traffic allowance is published | metered: no | source: [1]
- identity: email | detail: The sign-up form asks for first name, last name, email address and a password, with no payment field; the sign-up page states a free for life plan. After registration the user is prompted to create an organisation. Whether a later step asks for a phone number is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 50,000 requests per month [1]
  - request-rate: Management API: 500 requests per minute [2]
  - per-object-cap: flag string value 20,000 bytes; identity trait value 2,000 bytes [2]
- limits note: 1 team member and 1 project on Free; 1000 features and 500 segments per project.
- binding note: A server-rendered page fetches flags once per view, so 50,000 views a month uses the allowance; past it the Flags API is blocked 7 days after the warning email.
- interface detail: Flags API at https://edge.api.flagsmith.com/api/v1/ with a public Environment Key in the X-Environment-Key header (a GET /flags/ without a key answered 401); Management API with a secret Organisation API Token, 500 requests per minute.
- endpoint: part of interface detail
- tooling: Flagsmith SDKs or any HTTP client; the Management API covers everything the dashboard does.
- composes with: Remote config and kill switches for a small app on free compute, fetched once per page view or session to stay inside 50,000 requests a month.
- reliability: On the Free plan the API stops answering after the plan limit is exceeded and the 7-day warning passes; the block clears 30 days after the warning or on upgrade. SDK requests are not rate limited.
- notes: Start-Up raises the allowance to 1,000,000 requests a month after a 14-day trial. Flagsmith is also open-source software that the user can install and run on a rented or free machine; that is the last resort after the hosted Free plan.
- evidence note: Every value is quoted from the first-party pricing page, system limits, API docs and sign-up page; the Flags API host was probed and answered 401 without a key. A flag read with an Environment Key on a free account would move it to measured.
- evidence:
  - [1] 2026-10-31: Free includes up to 50,000 requests a month | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Up to 50,000 Requests Per Month*
  - [1] 2026-10-31: Free includes up to 100,000 users in experiments | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Up to 100,000 Users in Experiments
  - [1] 2026-10-31: Free has 1 team member | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: 1 Team Member
  - [1] 2026-10-31: Free has 1 project; Start-Up has unlimited projects | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Projects 1 Unlimited
  - [1] 2026-10-31: Free has unlimited feature flags | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Unlimited Feature Flags
  - [1] 2026-10-31: Free has unlimited environments | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Unlimited Environments
  - [1] 2026-10-31: Free has unlimited identities and segments | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Unlimited Identities and Segments
  - [1] 2026-10-31: one SDK instantiation is one request | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Each time you instantiate one of our client SDKs and get the flags for a user or application, you make 1 request.
  - [1] 2026-10-31: only some endpoints count | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: We don't charge for every single API call. The following endpoints count against your monthly limit:
  - [1] 2026-10-31: a free plan over the limit has 7 days | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: If you're on a free plan, you'll have 7 days to upgrade your plan before any action is taken.
  - [1] 2026-10-31: a team member logs in with an email address | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Each Team Member can log in with their own email address.
  - [1] 2026-10-31: Start-Up includes 1,000,000 requests a month | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: Up to 1,000,000 Requests Per Month*
  - [1] 2026-10-31: Start-Up starts with a 14-day trial | capture: sha256:232fab569e6f9ad4b5eaba25fdc35cf0418eddb7820e630fda66b25aa0ef5a8b | quote: [14 Day Free Trial](https://app.flagsmith.com/signup?plan=startup-v2)
  - [2] 2026-10-30: a project holds up to 1000 features | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: - 1000 features per project
  - [2] 2026-10-30: a project holds up to 500 segments | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: - 500 segments per project
  - [2] 2026-10-30: a flag string value is at most 20,000 bytes | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: - Maximum size of a flag string value is 20,000 bytes
  - [2] 2026-10-30: a trait value is at most 2,000 bytes | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: - Maximum size of an identity trait value is 2,000 bytes
  - [2] 2026-10-30: the API stops answering a free plan over its limit | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: If you are on our Free Plan, we will stop answering requests from our API if you go over your [Free Plan limit](https://www.flagsmith.com/pricing).
  - [2] 2026-10-30: the block follows a warning by 7 days | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: We will send you a warning email 7 days before we block your requests, to give you time to upgrade your account.
  - [2] 2026-10-30: the block clears after 30 days or on upgrade | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: This block is cleared 30 days after the warning email was first sent, or when you upgrade to a paid plan.
  - [2] 2026-10-30: the Management API allows 500 requests a minute | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: are subject to a default rate limit of 500 requests per minute.
  - [2] 2026-10-30: SDK requests are not rate limited | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: Requests made by our SDKs are not rate limited, by design
  - [2] 2026-10-30: a self-hosted deployment exists | capture: sha256:bd9c8eac694f5d2e3cd0178a8b2a346852da7463227ab38bf221fda2cd6db76f | quote: If you are self-hosting, you have the flexibility to modify this limit by adjusting the value of the environment variable `USER_THROTTLE_RATE`.
  - [3] 2026-10-31: the Flags API uses a public Environment Key | capture: sha256:55a1dae30f5e26d6abbb5b12801dabf79191d438ae3190e427a91883523689e6 | quote: - Authentication: Uses a public, non-secret Environment Key.
  - [3] 2026-10-31: the Management API uses a secret Organisation API Token | capture: sha256:55a1dae30f5e26d6abbb5b12801dabf79191d438ae3190e427a91883523689e6 | quote: - Authentication: Uses a secret Organisation API Token.
  - [3] 2026-10-31: the Management API covers the dashboard | capture: sha256:55a1dae30f5e26d6abbb5b12801dabf79191d438ae3190e427a91883523689e6 | quote: Anything you can do in the Flagsmith dashboard, you can also do via the Management API.
  - [4] 2026-10-31: the Flags API is served at edge.api.flagsmith.com/api/v1 | capture: sha256:ab25338a9f52fc994ce3dde9339c4852a6c56d61cb3f202556d735f60cb2e9a2 | quote: GET https://edge.api.flagsmith.com/api/v1/flags/
  - [4] 2026-10-31: the Flags API takes the X-Environment-Key header | capture: sha256:ab25338a9f52fc994ce3dde9339c4852a6c56d61cb3f202556d735f60cb2e9a2 | quote: #### Authorization: X-Environment-Key
  - [5] 2026-10-31: the sign-up page states a free for life plan | capture: sha256:564baf01c7008f9023aae9aaf78b5efdaa6a4ab4ee50df2ca7e2b7771d7b5ea1 | quote: We have a 100% free for life plan for smaller projects.
  - [5] 2026-10-31: the sign-up asks for first name, last name, email address and password | capture: sha256:564baf01c7008f9023aae9aaf78b5efdaa6a4ab4ee50df2ca7e2b7771d7b5ea1 | quote: First Name Last Name Email Address Password
  - probe:https://edge.api.flagsmith.com/api/v1/flags/ 2026-10-31: edge.api.flagsmith.com/api/v1/flags/ answers 401 without a key | capture: sha256:a0fd0cf0a70669b1e25e116b8123241b1a30daf9207d9b64358a8ba4090e002b | quote: "status": 401
  - [6] 2026-11-01: after registration the user is prompted to create an organisation | capture: sha256:0622f3338b6aa3ad934408c4ec2841baf16e5df7be196a9ad255806ead5f04bb | quote: After registration, you’ll be prompted to create an organisation:
  - [5] 2026-11-01: the sign-up form asks for first name, last name, email address and password | capture: sha256:564baf01c7008f9023aae9aaf78b5efdaa6a4ab4ee50df2ca7e2b7771d7b5ea1 | quote: First Name Last Name Email Address Password
- sources:
  - [1] https://www.flagsmith.com/pricing
  - [2] https://docs.flagsmith.com/administration-and-security/governance-and-compliance/system-limits
  - [3] https://docs.flagsmith.com/integrating-with-flagsmith/flagsmith-api-overview
  - [4] https://docs.flagsmith.com/sdk-api/sdk-v-1-flags
  - [5] https://app.flagsmith.com/signup
  - [6] https://www.flagsmith.com/blog/typescript-feature-flags-next-js-example
