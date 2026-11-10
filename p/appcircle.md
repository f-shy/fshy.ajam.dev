# Appcircle

> appcircle.io | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/appcircle/ | JSON https://fshy.ajam.dev/api/v1/entity/appcircle.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Appcircle

- `ci-cd-runners/appcircle-starter` | qualifies-with-caveat | evidence documented | binding request-rate | category CI runner | tier Starter
- needs card no, phone no, ID no, institution no | verified 2026-11-09T12:52:26.539Z (live) | stale on 2026-12-10
- url https://appcircle.io/pricing
- free tier: Starter, labelled Always Free: 20 builds per month, 1 concurrent build, 30 minutes max build time per build | unit: mixed | metered on: unstated | read on: 2026-11-02 | source: [1] | note: the pool is a count of builds a month, not minutes or credits; no term of the unit vocabulary names a build count
- per-object cap: 30 minutes max build time per build | source: [1]
- retention: not stated | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: registration is by email address and password at my.appcircle.io, signing up with the Sign up with Company E-mail button and then verifying the address; common and disposable email domains cannot be used, so a company address is required. No card and no phone number is named on the registration page
- interface: rest
- limits:
  - request-rate (binding): 20 builds per month on Starter [1]
  - request-rate (binding): 1 concurrent build [1]
  - per-object-cap: 30 minutes max build time per build [1]
- binding note: the 20-builds-a-month pool fails first (at most 600 build minutes a month, which is a compute pool counted in builds); the schema has no term for a build-count or compute-time pool, so request-rate is the nearest
- interface detail: a hosted mobile CI/CD service with build, signing, distribution and store-publishing modules, and a REST API at api.appcircle.io authenticated by a Personal Access Key or an API Key, with the API reference published as an OpenAPI document
- tooling: builds for iOS, Android, React Native and Flutter on Apple Silicon machines, with a clean isolated environment for every build
- composes with: not stated
- reliability: no reliability event recorded
- notes: a mobile-only CI service: builds run on Apple Silicon machines, so the Starter pool is also a route to macOS build time. 20 builds of at most 30 minutes is a ceiling of 600 build minutes a month.
- evidence note: the pricing page was read on 2026-11-02 and states the Starter pool, concurrency and build time; what registration asks for is unverified
- extras:
  - derived: 20 builds x 30 minutes = 600 build minutes a month at most
- evidence:
  - [1] 2026-11-02: the Starter plan includes 20 builds a month | capture: sha256:b930e55ffa7115e5bb214f95e4bce2b1c4e4609203253450279036d04b0bb206 | quote: 20 builds per month
  - [1] 2026-11-02: a build is capped at 30 minutes | capture: sha256:b930e55ffa7115e5bb214f95e4bce2b1c4e4609203253450279036d04b0bb206 | quote: 30 minutes max build time per build
  - [1] 2026-11-02: the Starter plan runs 1 build at a time | capture: sha256:b930e55ffa7115e5bb214f95e4bce2b1c4e4609203253450279036d04b0bb206 | quote: 1 concurrent build
  - [1] 2026-11-02: the Starter plan is labelled Always Free, which is a recurring allowance and not a trial | capture: sha256:b930e55ffa7115e5bb214f95e4bce2b1c4e4609203253450279036d04b0bb206 | quote: Always Free
  - [1] 2026-11-04: the Starter plan includes 20 builds a month | capture: sha256:b930e55ffa7115e5bb214f95e4bce2b1c4e4609203253450279036d04b0bb206 | quote: 20 builds per month
  - [1] 2026-11-04: a build is capped at 30 minutes | capture: sha256:b930e55ffa7115e5bb214f95e4bce2b1c4e4609203253450279036d04b0bb206 | quote: 30 minutes max build time per build
  - probe:https://appcircle.io/pricing 2026-11-04: the pricing page answered HTTP 200 on 2026-11-04 | capture: sha256:388447d86c9801dc66dbf221897f3ee7e876e4431df0bdc09b52d218b12047ae | quote: "status": 200
  - [2] 2026-11-09: registration is by email with verification, and common or disposable email domains are refused, so a company address is required | capture: sha256:2712f4bd507abe82e4c50f3a6a4c5ef02c7a592cf5d2b9648f67909254b5a77f | quote: You cannot use common and disposable email domains for registration; instead, please register using your company email account.
  - [3] 2026-11-09: the service publishes a REST API with personal-access-key and API-key authentication, so its interface is not unknown | capture: sha256:b4385a4292cc2d26cb98b63177f3ae3d5249b674f4b6fb4817c015d1b2e9c74c | quote: The Appcircle API supports authentication with a Personal Access Key.
  - [3] 2026-11-09: the API base is api.appcircle.io and a bearer token from the auth endpoint authorises a call | capture: sha256:b4385a4292cc2d26cb98b63177f3ae3d5249b674f4b6fb4817c015d1b2e9c74c | quote: curl -X GET "https://api.appcircle.io/distribution/v2/profiles" -H "accept: application/json" -H "Authorization: Auth-Token-Goes-Here"
  - [1] 2026-11-09: the Starter plan is still labelled Always Free with 20 builds a month, 1 concurrent build and a 30 minute maximum per build | capture: sha256:b930e55ffa7115e5bb214f95e4bce2b1c4e4609203253450279036d04b0bb206 | quote: 20 builds per month
- sources:
  - [1] https://appcircle.io/pricing
  - [2] https://docs.appcircle.io/account/my-account/sign-up-login
  - [3] https://docs.appcircle.io/appcircle-api/api-authentication
