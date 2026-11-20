# disposable-mail providers

> mail.tm | Storage, Email; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mail-3/ | JSON https://fshy.ajam.dev/api/v1/entity/mail-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## disposable-mail providers as storage (mail.tm, guerrilla mail, 1secmail)

- `storage/disposable-mail-providers-as-storage` | qualifies-with-caveat | evidence documented | binding retention-clamped | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:15:53.012Z (live) | stale on 2026-12-20
- page https://fshy.ajam.dev/p/mail-3.md
- free tier: Completely free. No API key, no signup, no paid tiers. | unit: requests | metered on: request-count | read on: 2026-11-09 | source: [1] | note: The general quota limit is 8 queries per second (QPS) per IP address.
- per-object cap: not stated on https://docs.mail.tm/ | note: not applicable
- retention: We store messages for 7 days only. Sorry, we can't keep them indefinitely. | days: 7
- egress: not stated on https://docs.mail.tm/ | metered: no
- identity: anonymous | detail: mail.tm: no API key and no sign-up; an inbox account is created by one API request with an address and a password
- interface: rest
- limits:
  - retention-clamped (binding): We store messages for 7 days only. Sorry, we can't keep them indefinitely. [2]
- binding note: mail.tm stores incoming messages for 7 days, so held bytes do not persist; the per-account byte quota is an integer returned only for a created account and is unverified here
- interface detail: REST API; no API key required.
- tooling: not documented
- composes with: Not stated on https://docs.mail.tm/; mail.tm stores received messages for a bounded period rather than acting as a durable store.
- reliability: api.mail.tm/domains answers HTTP 200 with one active receiving domain (fldubai.com, replacing maxxspace.com); api.guerrillamail.com answers HTTP 200 with a JSON session; www.1secmail.com fails TLS verification (certificate not valid for the hostname), so its API could not be read
- notes: mail.tm states it is completely free with no API key, no signup and no paid tiers.
- evidence note: the mail.tm documentation states the API is free with no signup
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: 
  - [1] 2026-10-30: the mail.tm API allows 8 queries per second per IP address | capture: sha256:8388471c99b33765bda923cbd8bd39e71da90f75722b6d3eb33b521e5c433d6c | quote: The general quota limit is 8 queries per second (QPS) per IP address.
  - [1] 2026-10-30: the mail.tm API is free with no API key, no sign-up and no paid tier | capture: sha256:8388471c99b33765bda923cbd8bd39e71da90f75722b6d3eb33b521e5c433d6c | quote: Completely free. No API key, no signup, no paid tiers.
  - [3] 2026-10-30: the API schema gives each Account an integer quota property; its value is not printed | capture: sha256:bcf1cd6ef413b53d1487776fc9e5106e23d873b228fc1f15dfd8e770a09a9c0d | quote: "rdfs:label":"quota","domain":"#Account","range":"xmls:integer"
  - [1] 2026-10-30: an inbox account is created by one API request | capture: sha256:8388471c99b33765bda923cbd8bd39e71da90f75722b6d3eb33b521e5c433d6c | quote: Create a temporary email account with one request.
  - probe:https://api.mail.tm/domains 2026-10-30: api.mail.tm/domains answered HTTP 200 | capture: sha256:8072ed5d9493ccc717454d2948d3d6278efece985efdb66d70d943b72c73a85e | quote: "status": 200
  - probe:https://api.mail.tm/domains 2026-10-30: the mail.tm API lists an active receiving domain | capture: sha256:83c389a9c60c3bd2b115dc82472440e76547822c00e432c44da076ef774148e9 | quote: "domain":"maxxspace.com","isActive":true
  - probe:https://api.mail.tm/domains 2026-11-03: api.mail.tm/domains answered HTTP 200 | capture: sha256:8cad7809e7bf5f3732790a18d06d3df233f1d1eaefe1993861a0644fb6b266e7 | quote: "status": 200
  - [2] 2026-11-03: mail.tm stores incoming messages for 7 days | capture: sha256:edfb9fcdc3862ebe4a8a19aab535c3fd720dc6a902b5cfeb2416f8888b2a4e43 | quote: We store messages for 7 days only. Sorry, we can't keep them indefinitely.
  - probe:https://api.mail.tm/domains 2026-11-03: the mail.tm API listed an active receiving domain on 2026-11-03 | capture: sha256:05f79f484b362b3d6aff069f0b2b1625981011197230dcda6e5e938b5a2723c4 | quote: "domain":"fldubai.com","isActive":true
  - probe:https://api.guerrillamail.com/ajax.php 2026-11-03: api.guerrillamail.com get_email_address answered HTTP 200 | capture: sha256:bde1b6d5eda0fdd58f0aa4bb6702da0e7c7e25c521ad612c164804dac8370975 | quote: "status": 200
  - probe:https://www.1secmail.com/ 2026-11-03: www.1secmail.com presented a TLS certificate not valid for its hostname | capture: sha256:22aeac248118986032e5180ef369b2ee6f40b7defa662301ced0c22323ebaa68 | quote: Hostname mismatch, certificate is not valid for 'www.1secmail.com'.
  - probe:https://www.1secmail.com/api/v1/ 2026-11-03: the 1secmail API URL failed TLS verification and returned no status | capture: sha256:051af894a56dde4ecc71e0192d0549a044bc03ef8fd1205e93908cd2135b1721 | quote: "error": "tls_untrusted"
  - [4] 2026-11-03: Guerrilla Mail emails expire after 60 minutes | capture: sha256:9e3299d37982cdf86f5a7fc287d36884fc91bc0596d047406cddd0543f7e460c | quote: Emails expire after 60 minutes
  - probe:https://api.guerrillamail.com/ajax.php 2026-11-03: the Guerrilla Mail API returned a new inbox address on a guerrillamailblock.com domain, with a creation timestamp, as JSON | capture: sha256:8f48661cfcfdb6d3d3454927a22b19a3d35eb14ad69f79f3d69b1cc253ac4234 | quote: @guerrillamailblock.com","email_timestamp":1793668516
  - [1] 2026-11-09: the mail.tm documentation states the API is completely free with no API key, no signup and no paid tiers | capture: sha256:8388471c99b33765bda923cbd8bd39e71da90f75722b6d3eb33b521e5c433d6c | quote: Completely free. No API key, no signup, no paid tiers.
  - [1] 2026-11-09: the mail.tm documentation states the quota is 8 queries per second per IP address | capture: sha256:8388471c99b33765bda923cbd8bd39e71da90f75722b6d3eb33b521e5c433d6c | quote: The general quota limit is 8 queries per second (QPS) per IP address.
  - [2] 2026-11-09: the mail.tm FAQ states messages are stored for 7 days | capture: sha256:edfb9fcdc3862ebe4a8a19aab535c3fd720dc6a902b5cfeb2416f8888b2a4e43 | quote: We store messages for 7 days only. Sorry, we can't keep them indefinitely.
  - [2] 2026-11-09: the mail.tm FAQ states a disposable mailbox is anonymous and requires no registration | capture: sha256:edfb9fcdc3862ebe4a8a19aab535c3fd720dc6a902b5cfeb2416f8888b2a4e43 | quote: A disposable mailbox is a temporary, completely anonymous email address that requires no registration.
  - [1] 2026-11-19: the interface is a REST API | capture: sha256:fc58937d2c8d09340514f04560f54fdeb50e71035972c2badc220db9f0a1a1ee | quote: Create temporary email accounts and receive emails via REST API. No API key required.
  - [1] 2026-11-19: the API documentation states no retention period, per-object cap, chaining terms or egress charge | capture: sha256:fc58937d2c8d09340514f04560f54fdeb50e71035972c2badc220db9f0a1a1ee | quote: Completely free. No API key, no signup, no paid tiers.
  - [1] 2026-11-19: no API key, sign-up or paid tier is needed | capture: sha256:fc58937d2c8d09340514f04560f54fdeb50e71035972c2badc220db9f0a1a1ee | quote: Completely free. No API key, no signup, no paid tiers.
  - [2] 2026-11-19: the 7-day retention is unchanged | capture: sha256:edfb9fcdc3862ebe4a8a19aab535c3fd720dc6a902b5cfeb2416f8888b2a4e43 | quote: We store messages for 7 days only. Sorry, we can't keep them indefinitely.
- sources:
  - [1] https://docs.mail.tm/
  - [2] https://mail.tm/en/faq/
  - [3] https://api.mail.tm/docs.jsonld
  - [4] https://www.guerrillamail.com/GuerrillaMailAPI.html

## mail.tm

- `email/mail-tm` | qualifies-with-caveat | evidence measured | binding per-object-cap | category disposable inbox API
- needs card no, phone no, ID no, institution no | verified 2026-11-19T03:34:18.381Z (live) | stale on 2027-02-18
- url https://api.mail.tm/
- free tier: a disposable inbox with a 40 MB quota, created and read over a keyless REST API | unit: MB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 40 MB quota per inbox, reported by the account object | source: [1]
- retention: incoming messages are stored for 7 days only, then deleted | days: 7 | source: [1]
- egress: not applicable: receive-only | metered: no | source: [1]
- identity: anonymous | detail: no key, no email verification and no card; measured by creating an account
- interface: rest
- limits:
  - request-rate: 8 queries per second (QPS) per IP address general quota limit [1]
  - per-object-cap (binding): 40 MB quota per inbox, reported by the account object probe
- interface detail: /domains, /accounts, /token and /messages on api.mail.tm; SMTP delivery to in.mail.tm
- tooling: curl, any HTTP client
- composes with: the verification-code sink, measured end to end: create an inbox with no key, let a service deliver over SMTP, read the message back over the API. The scarce link is the 40 MB quota and the single shared domain.
- reliability: one active domain; a domain change would invalidate every address a script had recorded
- notes: Four requests and one SMTP message proved the whole chain. 25 MiB per message against a 40 MB inbox is the practical ceiling, so one inbox holds one message.
- extras:
  - stale_after_days: 90
- evidence:
  - probe:https://api.mail.tm/domains 2026-10-22: 200, one active domain maxxspace.com (id 6aa6b995482bea6f4a97f585, isActive true), read with no key
  - probe:https://api.mail.tm/accounts 2026-10-22: 201, a fresh account with quota 40000000, used 0, isDisabled false; no email verification and no card
  - probe:https://api.mail.tm/token 2026-10-22: 200, a 360-character JWT for the new account
  - probe:smtp://in.mail.tm:25 2026-10-22: EHLO returned 250 and an SMTP message to the created address was accepted; sendmail returned no refusal
  - probe:https://api.mail.tm/messages 2026-10-22: 200, the message listed with its subject and sender, then GET /messages/{id} returned 200 with subject, from, a text part and an html part
  - probe:https://mail.tm/en/faq 2026-11-19: incoming messages are deleted after 7 days | capture: sha256:4b82905ece2a56e358e089453ccb5b9da7994966b63a984530b212019e98040d | quote: We store messages for 7 days only. Sorry, we can't keep them indefinitely.
  - probe:https://docs.mail.tm/ 2026-11-19: the general rate limit is 8 QPS per IP address | capture: sha256:6b41150c4f73604163141ced7039795a5e4e87a66976c1fd325e5703e6dca831 | quote: The general quota limit is 8 queries per second (QPS) per IP address.
  - probe:https://api.mail.tm/domains 2026-11-19: one active domain is published, with hostname euploading.com | capture: sha256:776b6377c55784f7474d93b7099f991292a3967e651d3ae804c2c959db880393
  - probe:https://docs.mail.tm/ 2026-11-19: no key, no signup and no payment are needed to use the API | capture: sha256:6b41150c4f73604163141ced7039795a5e4e87a66976c1fd325e5703e6dca831 | quote: Completely free. No API key, no signup, no paid tiers.
- sources:
  - [1] https://api.mail.tm/
