# Gemini CLI free tier

> github.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-google-gemini/ | JSON https://fshy.ajam.dev/api/v1/entity/github-google-gemini.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gemini CLI free tier (Gemini Code Assist for individuals)

- `inference/gemini-cli-free` | dead | evidence documented | binding request-rate | category coding agent CLI, Google account login
- needs card no, phone unknown, ID no, institution no | verified 2026-10-28T04:36:19.143Z (live) | stale on 2026-11-28
- url https://github.com/google-gemini/gemini-cli
- free tier: ended: Gemini CLI stopped serving the free Gemini Code Assist for individuals route on June 18, 2026, and free individual access moved to Antigravity CLI | unit: none | metered on: none | read on: 2026-10-28 | source: [1] | note: the quota page on geminicli.com still lists the individual tier at 1,000 requests per user per day and the Gemini API key tier at 250 requests per user per day, Flash only; the repository README and the vendor's transition post state the end of the free individual route
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a personal Google account; the authentication page lists 'Individual Google accounts | Sign in with Google | No, with exceptions' for the Google Cloud project requirement. Any phone check at Google account creation is unverified
- interface: cli
- limits:
  - request-rate (binding): no free requests served on the individual route since 2026-06-18; the quota page still prints 'Gemini Code Assist (Individual) | 1,000 requests' per user per day [2]
- binding note: nothing is served on the free individual route, so the last listed ceiling, a daily request count, is moot
- interface detail: gemini -p runs the agent headless and prints JSON or JSONL; headless mode reuses a cached Google OAuth credential
- tooling: gemini CLI in headless mode: gemini -p PROMPT --output-format json
- composes with: nothing chains on the free route; the successor route is recorded at coding-subs/antigravity and the Gemini API key route at inference/google-gemini-api
- reliability: the geminicli.com quota page still lists the individual tier while the repository README and the vendor post say it moved, so that page overstates what is served
- notes: The Gemini API free tier is a separate route (inference/google-gemini-api). The transition post names paid API keys for the CLI that remains, so whether an unpaid Gemini API key still works inside the CLI is unverified.
- evidence note: the end date is stated by the vendor's transition post and by the repository README; no request was made because the route needs an account
- evidence:
  - [1] 2026-10-28: the README states free individual access moved to Antigravity CLI on June 18, 2026 | capture: sha256:7cef0e91106c191e1331b8377fce35fbe5f34753d97e62c1293c47bbbc30f32b | quote: No free tier or Google AI plans: Free individual access and Google AI Pro / Ultra (Google One) moved to [Antigravity CLI](https://antigravity.google/product/antigravity-cli) on June 18…
  - [3] 2026-10-28: the vendor post announces that on June 18, 2026 Gemini CLI stops serving requests for Google AI Pro and Ultra and for free Gemini Code Assist for individuals | capture: sha256:d6f48c91b650f10c0fd35e3ee5a74e64bc07daa57d44650aa57054d8ffc50125 | quote: On June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will stop serving requests for Google AI Pro and Ultra, as well as those using it free of charge
  - [3] 2026-10-28: the vendor post keeps Gemini CLI available through paid API keys, so an unpaid key route is not confirmed | capture: sha256:d6f48c91b650f10c0fd35e3ee5a74e64bc07daa57d44650aa57054d8ffc50125 | quote: Gemini CLI will remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys.
  - [4] 2026-10-28: the Gemini Code Assist overview lists two editions, Standard and Enterprise, and no individual edition | capture: sha256:36ccdad1ac0668f43a81d86679b676256083924800bb8381d2397e661b1ad416 | quote: Gemini Code Assist is available in two editions, which are managed through Google Cloud:
  - [2] 2026-10-28: the quota page still lists 1,000 requests per user per day for the individual tier | capture: sha256:b7cd1156b3c941d10515db1054da96b41a02282e5ce10f43d6184d969c33acf9 | quote: | Google account | Gemini Code Assist (Individual) | 1,000 requests |
  - [2] 2026-10-28: the quota page lists 250 requests per user per day for an unpaid Gemini API key | capture: sha256:b7cd1156b3c941d10515db1054da96b41a02282e5ce10f43d6184d969c33acf9 | quote: 250 maximum model requests / user / day
  - [5] 2026-10-28: individual Google accounts sign in with Google and need no Google Cloud project, with exceptions | capture: sha256:f8703e33749bbc66fc68e8824a939e6c0485bb3836c27628a7e88f80ddc1af07 | quote: | Individual Google accounts | Sign in with Google | No, with exceptions |
  - [6] 2026-10-28: headless mode is a programmatic interface returning structured text or JSON | capture: sha256:a2b712c07b171d2670ebfb149f32d3aa046fa1edf7d9962719fa32e4a92143f4 | quote: Headless mode provides a programmatic interface to Gemini CLI, returning structured text or JSON output without an interactive terminal UI.
  - [6] 2026-10-28: the -p flag triggers headless mode | capture: sha256:a2b712c07b171d2670ebfb149f32d3aa046fa1edf7d9962719fa32e4a92143f4 | quote: Headless mode is triggered when the CLI is run in a non-TTY environment or when providing a query with the `-p` (or `--prompt`) flag.
  - [6] 2026-10-28: the output format is chosen with --output-format | capture: sha256:a2b712c07b171d2670ebfb149f32d3aa046fa1edf7d9962719fa32e4a92143f4 | quote: You can specify the output format using the `--output-format` flag.
  - [5] 2026-10-28: headless mode reuses a cached authentication credential | capture: sha256:f8703e33749bbc66fc68e8824a939e6c0485bb3836c27628a7e88f80ddc1af07 | quote: will use your existing authentication method, if an existing authentication credential is cached.
- sources:
  - [1] https://github.com/google-gemini/gemini-cli
  - [2] https://geminicli.com/docs/resources/quota-and-pricing/
  - [3] https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
  - [4] https://developers.google.com/gemini-code-assist/docs/overview
  - [5] https://geminicli.com/docs/get-started/authentication/
  - [6] https://geminicli.com/docs/cli/headless/
