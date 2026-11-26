# Ionic Appflow

> ionic.io | CI runners; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ionic/ | JSON https://fshy.ajam.dev/api/v1/entity/ionic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ionic Appflow

- `ci-cd-runners/appflow` | trial-only | evidence documented | binding write-gated | category CI runner | tier Hobby (free)
- needs card no, phone no, ID no, institution no | verified 2026-11-19T01:03:40.930Z (live) | stale on 2026-12-20
- url https://ionic.io/docs/appflow
- free tier: a free Hobby plan that requires an Ionic Account and is for trying some of Appflow's features; new customer sales of Appflow were discontinued on February 11, 2025, and all Appflow features and services sunset effective December 31, 2027 | unit: mixed | metered on: unstated | read on: 2026-11-19 | source: [1] | note: the vocabulary has no term for a build-credit allowance, so mixed stands in; native build usage is stated in credits, with 1 Android build minute = 1 credit and 1 iOS build minute = 2 credits
- per-object cap: unverified: no per-object or build wall-clock cap stated in the first-party pages read | source: [2]
- retention: unverified: no build or artifact retention period stated in the first-party pages read | source: [2]
- egress: unverified: no egress allowance or price for hosted builds stated in the first-party pages read | metered: no | source: [2]
- identity: email | detail: an Ionic Account is required; the personal account settings page shows a Name, Email and Username and a changeable password. The sign-up page is a login wall and its exact form fields are unverified: behind a sign-up. No card, phone or identity document was seen at signup.
- interface: git, cli, rest
- limits:
  - volume-quota: native build usage is metered in plan credits: 1 Android build run time minute = 1 credit and 1 iOS build run time minute = 2 credits; if a credit limit applies to a plan, usage is tracked toward it on the dashboard [3]
  - write-gated (binding): all Appflow features and services sunset effective December 31, 2027, and new customer sales were discontinued on February 11, 2025 [4]
  - write-gated (binding): the Appflow CLI is available to enterprise customers only [5]
- binding note: new customer sales of Appflow were discontinued in February 2025 and all features sunset on December 31, 2027, so a reader cannot start a new hosted lane after that date, which binds before any build-credit allowance is reached
- interface detail: builds trigger from a connected git repository or from the Appflow dashboard; the Appflow CLI drives native builds and deployments from an external CI system with a Personal Access Token; the Appflow CLI is available to enterprise customers only
- endpoint: unverified: no public API endpoint is stated on the pages read
- tooling: hosted native build stacks for iOS and Android; Capacitor, Cordova, React Native and native projects; no Mac hardware needed for iOS builds because builds run in Ionic's cloud
- composes with: a push to a connected git repository or a call from the Appflow CLI starts a hosted native binary build, then publishes to the Apple App Store or Google Play Store or delivers a Live Update. The CLI can be driven from Azure DevOps, GitLab CI, Jenkins, GitHub Actions, Travis or CircleCI, but the build itself runs on Appflow runners.
- reliability: Ionic warns that applications still relying on Appflow infrastructure after the December 31, 2027 sunset may experience build pipeline failures and live update failures resulting in whitescreens
- notes: A hosted mobile CI/CD service. The free Hobby plan is unverified in its credit total and build cap because the sign-up page is a login wall and these values are behind a sign-up. New customer sales ended February 11, 2025 and the whole service sunsets December 31, 2027, so this is a trial-only offer. Self-hosted alternatives named by Ionic (Capgo, Volt Builder) are not this hosted offer.
- evidence note: all values are quoted from first-party Ionic pages. The free Hobby credit allowance, build wall-clock cap, retention and egress terms are unverified: behind a sign-up. Native build usage is metered in plan credits; the credit total on the free Hobby plan is not published on any page read.
- evidence:
  - [1] 2026-11-19: Appflow has a free Hobby plan that requires an Ionic Account | capture: sha256:73d5fb3671e19ba43f391f7573cdfa8cd47d7787e8defdc06b4d5c92671b89b7 | quote: Appflow requires an <a href="https://dashboard.ionicframework.com/signup" target="_blank" rel="noopener noreferrer" class="">Ionic Account</a> and comes with a free “Hobby” plan for those interested in playing around with some of its features.
  - [6] 2026-11-19: new customer sales of Appflow were discontinued | capture: sha256:69478fd5adf321a7c210fd9f92bf462253e2a3dfbba441d8864f089e0e8377b5 | quote: Today, we have discontinued new customer sales for all Ionic commercial products and services—including Ionic Appflow, Identity Vault, Portals, and all other paid components of the ecosystem.
  - [6] 2026-11-19: existing Appflow users keep access through December 31, 2027 | capture: sha256:69478fd5adf321a7c210fd9f92bf462253e2a3dfbba441d8864f089e0e8377b5 | quote: You’ll continue to have access through December 31, 2027.
  - [4] 2026-11-19: all Appflow features and services end on December 31, 2027 | capture: sha256:9f1d9257b9c2dfb59b5449f9d4a01a1841ec1a32a561d9f25655f10eb89bfcae | quote: All Appflow features and services will be sunset effective December 31, 2027.
  - [3] 2026-11-19: one Android build minute costs one plan credit | capture: sha256:240acdcffa3cdc94ed32ddd87753dff9d4c3195d57ebc9465855938bcfa5f46b | quote: 1 Android build run time minute = 1 credit^
  - [3] 2026-11-19: one iOS build minute costs two plan credits | capture: sha256:240acdcffa3cdc94ed32ddd87753dff9d4c3195d57ebc9465855938bcfa5f46b | quote: 1 iOS build run time minute = 2 credit*^
  - [5] 2026-11-19: the CLI path into Appflow is limited to enterprise customers | capture: sha256:eb6a89355c98de937e19bebd3b9b1e25134c55233ab6f7e638b9a927890da0df | quote: Appflow CLI is available to our enterprise customers only
  - [7] 2026-11-19: an Ionic account carries a Name, Email and Username | capture: sha256:726a2f6eb9b1e3165bdb997326392b96f1076f28876d4945e788171c19e8758c | quote: Modify Basic Info such as your Name, Email, and Username
  - [2] 2026-11-19: Appflow Enterprise plan sales are discontinued | capture: sha256:48d65cd2ab5bf88188b27e838213a6931a66f597d598ad551647c6cc4557eaf3 | quote: Sales of Appflow Enterprise plans have been discontinued.
- sources:
  - [1] https://ionicframework.com/docs
  - [2] https://ionic.io/docs/appflow
  - [3] https://ionic.zendesk.com/hc/en-us/articles/17808670917655-How-is-my-usage-calculated
  - [4] https://ionic.zendesk.com/hc/en-us/articles/29907381079831-Native-Builds-and-Live-Updates
  - [5] https://ionic.io/docs/appflow/cli/overview
  - [6] https://ionic.io/blog/important-announcement-the-future-of-ionics-commercial-products
  - [7] https://ionic.zendesk.com/hc/en-us/articles/360005174253-Getting-around-Personal-Account-Settings
