# cron-job.org

> cron-job.org | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cron-job/ | JSON https://fshy.ajam.dev/api/v1/entity/cron-job.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cron-job.org

- `dev-services/cron-job-org` | qualifies | evidence documented | binding request-rate | category hosted HTTP cron scheduler | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T00:43:02.028Z (live) | stale on 2026-12-01
- url https://cron-job.org/en/faq/
- free tier: Entirely free of charge, with no limit on the number of cronjobs per account (fair usage expected); each job runs up to 60 times an hour, i.e. every minute | unit: unlimited | metered on: none | read on: 2026-10-30 | source: [1] | note: Financed by voluntary donations. Sustaining members get a higher API limit of 5,000 requests a day; scheduling has no paid tier. Status pages, status badges and failure notifications by email or webhook are part of the free service.
- per-object cap: up to 64 KB of each response is read; a larger response aborts the execution | source: [1]
- retention: response headers and bodies stored for 2 days; the last 50 executions of each job are viewable | days: 2 | source: [1]
- egress: not applicable: an outbound HTTP caller; at most 64 KB of each response is read | metered: no | source: [1]
- identity: email | detail: The console sign-up form asks for first name, last name, email address and a password; there is no payment step because the service is free.
- interface: rest
- limits:
  - request-rate (binding): each job runs up to 60 times an hour (every minute) [1]
  - request-rate (binding): API: 100 requests per day by default, 5,000 per day for sustaining members [2]
  - request-rate (binding): API per-method limits such as 5 requests per second, or 1 request per second and 5 requests per minute [2]
  - per-object-cap: 64 KB of response output read per execution [1]
  - retention-clamped: response headers and bodies kept 2 days; last 50 executions per job [1]
- limits note: An execution times out after 30 seconds. A job that fails more than 25 times in a row is disabled automatically.
- binding note: The one-minute minimum interval and the 30-second timeout bound what a job can drive; the 100-a-day API limit binds only on programmatic job management.
- interface detail: a REST API with JSON payloads, authenticated by an API key in an Authorization bearer header; keys are generated in the console and can be restricted to listed IP addresses
- endpoint: https://api.cron-job.org/
- tooling: any HTTP client against the REST API, or the web console. As a last resort the scheduler source (chronos, GPL) is on GitHub: the user installs and runs the server software on a rented or free machine.
- composes with: Calls a free HTTP endpoint (a serverless function or a CI trigger URL) as often as once a minute, so it supplies the schedule that a free compute host without cron lacks, as long as each call finishes within 30 seconds.
- reliability: Slight delays at peak hours with no punctuality guarantee; jobs that failed often or ran long may be delayed on purpose, and a job is disabled after more than 25 consecutive failures.
- evidence note: Free tier, limits and sign-up fields are read on first-party pages. The API answered HTTP 401 to a request without a key and the public executor-node list answered HTTP 200 with JSON, so the endpoint is live; a job execution is not measured.
- evidence:
  - [3] 2026-10-30: the service is free and financed by donations | capture: sha256:990913bd1c03072320aa821b99be07e6e5562437914330105097970a6a982ccc | quote: Our service is absolutely free and financed entirely by voluntary donations.
  - [1] 2026-10-30: the FAQ states the service costs nothing | capture: sha256:85be34f0c99be427fdecc0b4d1d10a5d4553d82e68d86239fb07b97a57f2933f | quote: Our service is entirely free of charge.
  - [1] 2026-10-30: no cap on the number of jobs per account, with fair usage expected | capture: sha256:85be34f0c99be427fdecc0b4d1d10a5d4553d82e68d86239fb07b97a57f2933f | quote: We do not limit the number of cronjobs per account, but we expect fair usage of our services.
  - [1] 2026-10-30: the minimum interval is one minute | capture: sha256:85be34f0c99be427fdecc0b4d1d10a5d4553d82e68d86239fb07b97a57f2933f | quote: Every cronjob can be executed up to 60 times an hour, i.e. every minute.
  - [1] 2026-10-30: an execution times out after 30 seconds | capture: sha256:0869e866e634375a759267c3d3d3ba46e85f4883c82e890b0099299de0e017eb | quote: If your URL/script does not finish after 30 seconds, it will timeout and we will close the connection to prevent delays in the execution of the jobs of other users.
  - [1] 2026-10-30: at most 64 KB of each response is read | capture: sha256:0869e866e634375a759267c3d3d3ba46e85f4883c82e890b0099299de0e017eb | quote: Our system reads up to 64 KB of the output of your URLs/scripts.
  - [1] 2026-10-30: response headers and bodies are kept for 2 days | capture: sha256:0869e866e634375a759267c3d3d3ba46e85f4883c82e890b0099299de0e017eb | quote: We store response headers and bodies for 2 days.
  - [1] 2026-10-30: the last 50 executions per job are viewable | capture: sha256:0869e866e634375a759267c3d3d3ba46e85f4883c82e890b0099299de0e017eb | quote: Yes, for every cronjob you can view the last 50 executions with detail information like scheduled date, execution date and response headers/body.
  - [1] 2026-10-30: a job is disabled after more than 25 consecutive failures | capture: sha256:0869e866e634375a759267c3d3d3ba46e85f4883c82e890b0099299de0e017eb | quote: In some cases we disable your cronjob automatically, e.g. when it subsequently fails more than 25 times (which is a strong indicator for an invalid/expired URL).
  - [1] 2026-10-30: no punctuality guarantee; delays at peak hours | capture: sha256:0869e866e634375a759267c3d3d3ba46e85f4883c82e890b0099299de0e017eb | quote: Nevertheless, there may be slight delays during peak hours, i.e. we cannot give a promise or a guarantee on punctuality.
  - [2] 2026-10-30: the API allows 100 requests per day by default | capture: sha256:a7bdacffd554a07c6e3dadb526872ad5d10fc45b8c83ed80020d65fbe0ebf0e1 | quote: By default, this limit is 100 requests per day, but can be increased upon request.
  - [2] 2026-10-30: sustaining members get 5,000 API requests per day | capture: sha256:a7bdacffd554a07c6e3dadb526872ad5d10fc45b8c83ed80020d65fbe0ebf0e1 | quote: For sustaining members, a higher limit of 5,000 requests per day applies.
  - [2] 2026-10-30: some API methods are limited to 1 request per second and 5 per minute | capture: sha256:a7bdacffd554a07c6e3dadb526872ad5d10fc45b8c83ed80020d65fbe0ebf0e1 | quote: Max. 1 request per second and 5 requests per minute.
  - [2] 2026-10-30: most API methods are limited to 5 requests per second | capture: sha256:a7bdacffd554a07c6e3dadb526872ad5d10fc45b8c83ed80020d65fbe0ebf0e1 | quote: Max. 5 requests per second.
  - [2] 2026-10-30: the REST API authenticates with an API key in a bearer header | capture: sha256:a7bdacffd554a07c6e3dadb526872ad5d10fc45b8c83ed80020d65fbe0ebf0e1 | quote: All requests to the API must be authenticated via an API key supplied in the `Authorization` bearer token header.
  - [2] 2026-10-30: API keys can be restricted to listed IP addresses | capture: sha256:a7bdacffd554a07c6e3dadb526872ad5d10fc45b8c83ed80020d65fbe0ebf0e1 | quote: Access via a specific API key might be restricted to certain IP addresses, if configured in the Console.
  - [3] 2026-10-30: cronjobs are managed programmatically through a REST API | capture: sha256:990913bd1c03072320aa821b99be07e6e5562437914330105097970a6a982ccc | quote: Manage your cronjobs from your scripts and applications via a simple REST API.
  - [3] 2026-10-30: status monitor jobs and status pages are part of the service | capture: sha256:990913bd1c03072320aa821b99be07e6e5562437914330105097970a6a982ccc | quote: Create status monitor jobs and publish status pages for your websites and services.
  - [3] 2026-10-30: status badges are part of the service | capture: sha256:990913bd1c03072320aa821b99be07e6e5562437914330105097970a6a982ccc | quote: Embed the status of your jobs into your websites, dashboards and markdown documents.
  - [3] 2026-10-30: failure notifications are part of the service | capture: sha256:990913bd1c03072320aa821b99be07e6e5562437914330105097970a6a982ccc | quote: Get notified when one of your jobs fail or starts working again after prior failure.
  - [3] 2026-10-30: notifications can go to a webhook | capture: sha256:990913bd1c03072320aa821b99be07e6e5562437914330105097970a6a982ccc | quote: We can also notify you via webhook or Slack, Telegram, Discord, etc.
  - [4] 2026-10-30: the sign-up is free | capture: sha256:e2779d932a7d472521a0a3d21c3bb29145018165cf20bf5b9ec9addde27f1f37 | quote: Don't have an account yet? Sign up for free, it only takes a minute.
  - [4] 2026-10-30: the sign-up form asks for an email address, alongside first name, last name and password fields | capture: sha256:e2779d932a7d472521a0a3d21c3bb29145018165cf20bf5b9ec9addde27f1f37 | quote: Email address
  - probe:https://api.cron-job.org/jobs 2026-10-31: the REST API at api.cron-job.org answered HTTP 401 to a request without an API key | capture: sha256:a639c47abb9b837cc47dd42b52e481cec94f8741ae96cd5622763f41f61cebd7 | quote: "status": 401
  - probe:https://api.cron-job.org/executor-nodes.json 2026-10-31: the public executor-node list at api.cron-job.org answered HTTP 200 with JSON | capture: sha256:ec97516596cd83f2ca18a58272ddce3dac5303a3efc184c379ed56f3174f5d94 | quote: "status": 200
  - [5] 2026-10-30: the scheduler daemon source is published on GitHub | capture: sha256:67f8bae119f1e0c4891552841b58c136dbc92eadbb4799b91a19c757567285cb | quote: chronos is cron-job.org's cron job execution daemon and is responsible for fetching the jobs.
- sources:
  - [1] https://cron-job.org/en/faq/
  - [2] https://docs.cron-job.org/rest-api.html
  - [3] https://cron-job.org/en/
  - [4] https://console.cron-job.org/signup
  - [5] https://github.com/pschlan/cron-job.org
