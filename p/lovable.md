# Lovable

> lovable.dev | Coding subscriptions, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lovable/ | JSON https://fshy.ajam.dev/api/v1/entity/lovable.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lovable (Coding subscriptions)

- `coding-subs/lovable` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted AI app builder
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:28:03.774Z (live) | stale on 2026-12-05
- url https://docs.lovable.dev/introduction/subscription-plans
- free tier: Free: 5 build credits a day, capped at 30 a month, so the cap is spent in the first 6 days of each calendar month; Pro starts at USD 25 a month for 100 credits, plus 5 daily build credits with no monthly cap | unit: credits | metered on: request-count | read on: 2026-11-02 | source: [1] | note: a credit is not a fixed unit of work: each message is charged on the work done, so the 30 free credits buy a variable number of messages
- per-object cap: not applicable: the plan meters credits, not stored bytes
- retention: not applicable: no stored bytes are metered
- egress: not published on the pages read: no egress term was found, so nothing is asserted | metered: no
- identity: email | detail: sign-up offers email, Google, GitHub or Apple and opens a Free personal workspace; the sign-up page shows an account form with an Email option and no card or phone field. Paid plans are billed through Stripe; what checkout asks for is unverified: behind a sign-up
- interface: rest, git
- limits:
  - volume-quota (binding): Free: 5 build credits a day, 30 a month; the monthly cap is reached on the sixth day and daily credits resume on the 1st at 00:00 UTC [1]
  - write-gated: the Lovable REST API and workspace API keys need a Business or Enterprise plan; Free and Pro workspaces see an upgrade prompt [2]
- limits note: the 30-credit Free cap binds first; the API gate is a plan gate, and the API itself spends no build credits
- binding note: 30 build credits a month on Free, spent in the first 6 days of the month
- interface detail: a web app where a prompt builds a project. Git sync with GitHub, GitLab and Bitbucket is on every plan. The Lovable REST API at api.lovable.dev/v1 (Lovable-API-Key header, keys start lov_) manages and deploys existing projects, needs a Business or higher plan, and spends no build credits. AI project creation and editing run through the Lovable MCP server, which is open to every plan and spends the same credits as the web app
- tooling: hosted service with a web editor; no local client is documented. An MCP client such as Claude or Cursor can drive project creation and messages through the MCP server on any plan
- composes with: Pro, USD 25 a month for 100 credits (USD 250 a year), adds code editing and download, custom domains and credit rollover; the Lovable API needs Business, whose 100-credit tier is USD 50 a month. Plan mode costs 1 credit a message; Build mode messages are priced by the work done, from 0.50 credits for a one-line style change to 1.70 for a landing page with 3 generated images. Chat messages usually cost a fraction of a credit and draw first on a separate daily chat allowance of unpublished size
- reliability: the chat allowance and the monthly Cloud and AI grants are stated as temporary offers subject to change; the chat pricing is stated to apply through 2026-10-31, a date that had passed on the day read, and whether it was extended is unverified
- notes: A hosted AI app builder rather than a coding-agent subscription: the unit is a credit, charged per message. The same vendor's Free plan, Cloud grant and sign-up are also recorded under compute/lovable. Monthly Cloud (20 credits), AI (4 credits) and connector (1 credit) grants come on top of build credits on every plan.
- evidence note: plan table, credit rules, API and MCP terms are quoted from first-party pages read on 2026-11-02; the size of the daily chat allowance is not published, and the checkout requirements of Pro were not seen
- evidence:
  - [1] 2026-11-02: Free gets 5 daily build credits capped at 30 a month; Pro and Business get 5 per day | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: | Daily build credits\* | 5/day, 30/month | 5 per day | 5 per day | — |
  - [1] 2026-11-02: the Free monthly cap of 30 is spent in the first 6 days of each calendar month | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: on Free, you receive daily build credits for the first 6 days each month (6 × 5 = 30), then none until the next month starts.
  - [1] 2026-11-02: Free has no subscription credits; Pro and Business start at 100 a month | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: | Monthly subscription credits | — | From 100/month | From 100/month | Volume-based |
  - [1] 2026-11-02: the Pro tier with 100 monthly credits is USD 25 billed monthly or USD 250 billed annually | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: | 100 | \$25 | \$250 (\$21/month) |
  - [1] 2026-11-02: Pro is sold in credit tiers from 100 credits a month upward | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: Pro and Business plans come in monthly credit tiers, from 100 to 10,000 credits per month.
  - [1] 2026-11-02: Free has no code editing; Pro and above can edit code | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: | Edit code | — | Yes | Yes | Yes |
  - [1] 2026-11-02: Git sync is included on every plan, Free included | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: | Git sync (GitHub, GitLab, and Bitbucket) | Yes | Yes | Yes | Yes |
  - [1] 2026-11-02: the Lovable API is included from Business upward and not on Free or Pro | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: | Lovable API | — | — | Yes | Yes |
  - [3] 2026-11-02: a Plan mode message costs 1 credit plus any subagent research | capture: sha256:34467b9f0eb0fcb7281c343c56c6e525f74c97dc8f3adf0673fa135d6db7864b | quote: | Plan mode | 1 credit per message, plus the cost of any subagent research Lovable runs while planning |
  - [3] 2026-11-02: a Build mode message has no fixed credit cost | capture: sha256:34467b9f0eb0fcb7281c343c56c6e525f74c97dc8f3adf0673fa135d6db7864b | quote: | Build mode | Cost depends on the complexity of the request and the work completed |
  - [4] 2026-11-02: a one-line style change cost 0.50 credits in the published examples | capture: sha256:c4dfe04ec9e712c743cd1ef298c1ec0cba194e938f14597cc0eb8476fecbe7e8 | quote: | “Make the button gray” | Updates the button styles | 0.50 |
  - [4] 2026-11-02: a landing page with 3 generated images cost 1.70 credits in the published examples | capture: sha256:c4dfe04ec9e712c743cd1ef298c1ec0cba194e938f14597cc0eb8476fecbe7e8 | quote: | “Build me a landing page, use images” | Creates a landing page with 3 generated images, theme, and 5 sections | 1.70 |
  - [3] 2026-11-02: a chat message costs typically a fraction of a credit | capture: sha256:34467b9f0eb0fcb7281c343c56c6e525f74c97dc8f3adf0673fa135d6db7864b | quote: Lovable prices each message on the work it does to answer, typically a fraction of a credit.
  - [3] 2026-11-02: the chat pricing model and daily chat allowance are stated as a temporary offer through 2026-10-31 | capture: sha256:34467b9f0eb0fcb7281c343c56c6e525f74c97dc8f3adf0673fa135d6db7864b | quote: applies through October 31, 2026
  - [5] 2026-11-02: API keys need a Business or Enterprise workspace and an owner or admin role | capture: sha256:b6727fd629fe73129959755fbe0939b660ded8ff5bf31909dc124c7c87a0c389 | quote: Creating API keys requires a Business or Enterprise plan, and an owner or admin role in the workspace.
  - [5] 2026-11-02: the REST API manages and deploys existing projects and spends no AI build credits | capture: sha256:b6727fd629fe73129959755fbe0939b660ded8ff5bf31909dc124c7c87a0c389 | quote: The public API manages and deploys existing projects, and its current endpoints, including deployment builds, do not consume AI build credits.
  - [6] 2026-11-02: every API key has its own rate limit | capture: sha256:9eb7a685ef045b0e4e11d2a468c8b9520efc96d333a8f7816ce186777747eb82 | quote: Each API key has its own rate limit.
  - [6] 2026-11-02: the API needs a verified account email | capture: sha256:9eb7a685ef045b0e4e11d2a468c8b9520efc96d333a8f7816ce186777747eb82 | quote: Your Lovable account email must be verified before you can call the API.
  - [2] 2026-11-02: Free and Pro workspaces cannot create workspace API keys | capture: sha256:a3b0dd522295f9457168065cc3fa16bb0cc0c2b2ad78a0a35d145f119dcb5eba | quote: Free and Pro workspaces show an upgrade prompt for workspace API keys.
  - [7] 2026-11-02: the MCP server, which can create and edit projects, is open to every plan | capture: sha256:76a5f80e1f8b332319d38dda43224cc99d96955251efb86132bc863858838055 | quote: The Lovable MCP server is available on all plans.
  - [7] 2026-11-02: building through the MCP server spends the same credits | capture: sha256:76a5f80e1f8b332319d38dda43224cc99d96955251efb86132bc863858838055 | quote: Standard Lovable credits apply to `create_project` and `send_message` calls. Other tools are free.
  - [8] 2026-11-02: sign-up takes an email, Google, GitHub or Apple login and opens a Free workspace | capture: sha256:6aae78b13bc7b05c8e646050521070711ddb5cd047aa15bbbf951415875b5931 | quote: with email, Google, GitHub, or Apple. Your account comes with a personal workspace on the free plan
  - [9] 2026-11-02: the sign-up page shows an account form with an Email option and no card or phone field | capture: sha256:a1830e938fd4c19c273259acb51cbe8e8a1c1cb44183673daa3d6b344797ba3f | quote: Create your account
  - [3] 2026-11-04: Free still gets 5 daily build credits capped at 30 a month | capture: sha256:34467b9f0eb0fcb7281c343c56c6e525f74c97dc8f3adf0673fa135d6db7864b | quote: | Free | Included | 5 per day, up to 30 per month | 20 credits per month | 4 credits per month | 1 credit per month |
- sources:
  - [1] https://docs.lovable.dev/introduction/subscription-plans
  - [2] https://docs.lovable.dev/features/api-keys
  - [3] https://docs.lovable.dev/introduction/credits-and-usage
  - [4] https://lovable.dev/pricing
  - [5] https://docs.lovable.dev/integrations/lovable-api
  - [6] https://docs.lovable.dev/api-reference/introduction
  - [7] https://docs.lovable.dev/integrations/lovable-mcp-server
  - [8] https://docs.lovable.dev/introduction/getting-started
  - [9] https://lovable.dev/signup

## Lovable (Compute)

- `compute/lovable` | qualifies-with-caveat | evidence documented | binding request-rate | category cloud VM
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-04T10:27:57.620Z (live) | stale on 2026-12-05
- url https://docs.lovable.dev/introduction/subscription-plans
- free tier: Lovable Free: "Daily build credits 5/day, 30/month", "Monthly Cloud grant 20 credits", "Monthly AI grant 4 credits", quoted; the footnote says "on Free, you receive daily build credits for the first 6 days each month (6 x 5 = 30), then none until the next month starts" | unit: credits | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: the sign-up page shows 'Create your account' with an Email field; no card or phone field is shown on that page, and any later step is unverified
- interface: unknown
- limits:
  - request-rate (binding): the 30-credit monthly cap exhausts on the sixth day of the month, so two thirds of every month has zero build capacity on the free plan. [1]
- limits note: the 30-credit monthly cap exhausts on the sixth day of the month, so two thirds of every month has zero build capacity on the free plan.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the 20-credit monthly Cloud grant hosts a small app and its backend after the 30 monthly build credits are gone; on Free, code cannot be edited or downloaded inside Lovable, but Git sync with GitHub, GitLab and Bitbucket is included, so the code moves through a repository
- reliability: no reliability event recorded
- notes: The credit is not a token. The pricing page's own examples price a one-line style change at 0.50 and a landing page with three generated images at 1.70, so the unit varies by task. A daily chat allowance also exists with no published number.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: recurring-allowance
- evidence:
  - [1] 2026-10-22: the Free column gives 5 daily build credits capped at 30 a month, a 20-credit monthly Cloud grant and a 4-credit monthly AI grant, quoted
  - [2] 2026-10-22: one credit balance covers build, chat, Cloud hosting with database, network, storage and compute, and AI gateway calls in deployed apps, quoted
  - [3] 2026-10-22: the pricing page prices single messages at 0.50 to 1.70 credits by example, so the 30 monthly free credits buy roughly 18 to 60 build messages
  - [1] 2026-10-22: probe GET returned status 200, 456647 bytes, sha256 a336e9b45071de52ed367c54abb3a21be3f189b82f5dfc7b67f843b964299233, no challenge detected, at 2026-10-22T15:23:48Z
  - [1] 2026-10-30: the Free plan's allowance is denominated in credits: 5 build credits a day capped at 30 a month | capture: sha256:bd0ea813de51ddac1a8065285de3cb53c7a0c63c72924a095bea629a675810ac | quote: Daily build credits\* | 5/day, 30/month | 5 per day | 5 per day
  - [4] 2026-10-30: the sign-up form asks for an email address | capture: sha256:41c89e05b149c00ce43319c08bef5997002f79e181325fb192988cefb20c3e5f | quote: Create your account Or Email
  - [1] 2026-10-30: the Free plan has no code editing and no code download, while Git sync is included on every plan | capture: sha256:bd0ea813de51ddac1a8065285de3cb53c7a0c63c72924a095bea629a675810ac | quote: | Edit code | — | Yes | Yes | Yes |
  - [1] 2026-10-30: the Free plan still grants 5 build credits a day for the first 6 days of each month, 30 in total, with 20 Cloud and 4 AI credits a month | capture: sha256:bd0ea813de51ddac1a8065285de3cb53c7a0c63c72924a095bea629a675810ac | quote: on Free, you receive daily build credits for the first 6 days each month (6 × 5 = 30), then none until the next month starts.
  - [1] 2026-11-03: the Free plan still grants 5 build credits a day up to 30 a month, exhausted on the sixth day | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: For example, on Free, you receive daily build credits for the first 6 days each month (6 × 5 = 30), then none until the next month starts.
  - [1] 2026-11-04: the Free plan still grants 5 daily build credits capped at 30 a month | capture: sha256:8a8c5d3e99fdcc4e4a0eab46a5b82f7b6fc694f859daf9e5367c3dad713af729 | quote: 5/day, 30/month
- sources:
  - [1] https://docs.lovable.dev/introduction/subscription-plans
  - [2] https://docs.lovable.dev/introduction/credits-and-usage
  - [3] https://lovable.dev/pricing
  - [4] https://lovable.dev/signup
