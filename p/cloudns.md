# ClouDNS

> cloudns.net | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudns/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudns.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ClouDNS

- `domains-dns/cloudns-free` | qualifies-with-caveat | evidence documented | binding per-object-cap | category managed authoritative DNS
- needs card no, phone no, ID no, institution no | verified 2026-11-02T10:17:37.731Z (live) | stale on 2026-12-03
- url https://www.cloudns.net/managed-dns/
- free tier: Free Forever: 1 DNS zone, 50 DNS records, 500,000 queries per month, 1 mail forward, 1 dynamic DNS hostname, 4 unicast nameservers | unit: objects | metered on: object-count | read on: 2026-10-22 | source: [1]
- per-object cap: 50 DNS records and 1 zone | source: [1] | note: the tightest record cap in this class
- retention: a zone with no DNS queries for over 30 days can be deleted without notice, the free plan named in particular | days: 30 | source: [2]
- egress: 500,000 DNS queries per month on Free, the only published query cap in this class | metered: yes | free allowance: 500,000 queries per month | source: [1]
- identity: email | detail: a first and last name, an e-mail address, a password and an hCaptcha; no phone and no card on the signup form (https://www.cloudns.net/index/show/signup/); an identity verification can be requested after signup
- interface: unknown
- limits:
  - per-object-cap (binding): 1 zone and 50 records [1]
  - request-rate: 500,000 DNS queries per month [1]
  - retention-clamped: a zone with no DNS queries for over 30 days can be deleted without notice [2]
- interface detail: the HTTP API at https://api.cloudns.net/ (auth-id and auth-password) manages zones and records, but the plan table marks HTTP API access absent on Free and present from Premium S at $2.95/month; the free plan's programmatic path is the DynURL of its one dynamic hostname, https://ipv4.cloudns.net/api/dynamicURL/?q=<token> (the ipv6.cloudns.net host for an AAAA record), which belongs to one A or AAAA record whose Dynamic URL is activated in the panel and changes the address of that record; its interface term would be dyndns, which the vocabulary lacks, so interface carries unknown
- tooling: on Free, curl or wget against the DynURL from cron, and the wiki's DynURL guides for Windows, Linux, Synology, MikroTik and pfSense; the HTTP API needs a paid plan
- composes with: the plan table gives Free no secondary DNS zones and no zone transfers, which rules out an AXFR pairing with another provider but not a second provider whose records are mirrored by hand
- reliability: a zone with no DNS queries for over 30 days, or a Free zone delegated to non-ClouDNS nameservers, can be suspended or deleted without notice
- notes: The Free plan holds 1 DNS zone and 50 DNS records.
- evidence note: the managed-DNS page was read and states the Free Forever column explicitly.
- evidence:
  - [1] 2026-10-22: Free Forever: 4 unicast DNS servers, 1 DNS zone, 50 DNS records, 500K DNS queries per month, 1 mail forward, 1 dynamic DNS hostname; a paid tier raises queries to 500M a month
  - [3] 2026-10-30:  | capture: sha256:2c90d10b40101d9329a85b5e2d446b5697994687f18d9f8d5e6cb6c7e5b928eb | quote: placeholder="First and last name"
  - [4] 2026-10-30: the plan table marks HTTP API access absent on Free; the raw page shows it ticked on Premium S, M, L and Enterprise | capture: sha256:3a1c2a1ba0abbf3a53f018827155777c7300a517d4ea45c73681ec0f34408761 | quote: HTTP API access: | - |
  - [4] 2026-10-30: the HTTP API access row is '-' for Free DNS and ticked for every paid column, Premium S at $2.95/month the cheapest | capture: sha256:63f4add13669d2df1fe1cf23725b6087c9733cbe00f24be9c2afc9e84928355f | quote: Integrate your system with ClouDNS system and manage all resources via HTTP API.
  - [5] 2026-10-30: each A and AAAA record gets its own DynURL; the page links guides for Windows, Linux, Synology, MikroTik and pfSense | capture: sha256:d2944842fad40cd5f40f26d268d8fa4b3cff221f6bd9a9d69ebbd13f14c61ca4 | quote: Dynamic DNS service by ClouDNS provides a unique URL called DynURL with each A (IPv4) and AAAA (IPv6) record.
  - [2] 2026-10-30: a zone with no DNS queries for over 30 days can be deleted without notice, the free plan named in particular | capture: sha256:c8284f272077fd66be4f68fa390f521ac8f1973bb059a677feb55faa36d4602a | quote: The customer agrees that his DNS zones can be deleted, if they are inactive (there are no DNS queries for the DNS zone) for over 30 days, especially if he is using free DNS hosting plan without prior notification.
  - [4] 2026-10-30: the free plan has no secondary DNS zones | capture: sha256:3a1c2a1ba0abbf3a53f018827155777c7300a517d4ea45c73681ec0f34408761 | quote: | *?* Secondary DNS zones: | - | | | | |
  - [2] 2026-10-30: a Free zone is delegated to ClouDNS nameservers only, and one delegated elsewhere can be suspended or deleted | capture: sha256:c8284f272077fd66be4f68fa390f521ac8f1973bb059a677feb55faa36d4602a | quote: The Customer agrees that all NS records for a Free DNS zone must point only to ClouDNS name servers.
  - [3] 2026-10-30: the signup form carries an hCaptcha | capture: sha256:2c90d10b40101d9329a85b5e2d446b5697994687f18d9f8d5e6cb6c7e5b928eb | quote: class="h-captcha"
  - [2] 2026-10-30: an identity verification can be requested after signup | capture: sha256:c8284f272077fd66be4f68fa390f521ac8f1973bb059a677feb55faa36d4602a | quote: We reserve the right to request customer identity verification at our discretion
  - [6] 2026-10-30: the record-management API is at api.cloudns.net with auth-id and auth-password | capture: sha256:7c65ff145745b4d803a75a69c4dddbf371a908f22ce2b22c06ad1f10d9e9c8ac | quote: The HTTP API is available at: https://api.cloudns.net/
  - [7] 2026-10-30: the dynamic update is a GET of ipv4.cloudns.net/api/dynamicURL/?q=<token>, or the ipv6 host for an AAAA record | capture: sha256:b4d4667e15a31bb6f9f81a06da59e328cbde32b270732381b009fc4d6fb0d050 | quote: https://ipv4.cloudns.net/api/dynamicURL/?q=your-string-here
  - [5] 2026-10-30: the free plan includes Dynamic DNS, whose DynURL is the free plan's programmatic path | capture: sha256:d2944842fad40cd5f40f26d268d8fa4b3cff221f6bd9a9d69ebbd13f14c61ca4 | quote: ClouDNS provides Free Dynamic DNS with all DNS hosting plans.
  - [4] 2026-10-30: the free plan has no zone transfers | capture: sha256:3a1c2a1ba0abbf3a53f018827155777c7300a517d4ea45c73681ec0f34408761 | quote: | *?* Zone transfers: | - | | | | |
  - [4] 2026-10-30: the free plan holds 50 records in 1 zone with 500K queries a month, 1 dynamic DNS hostname, unchanged | capture: sha256:3a1c2a1ba0abbf3a53f018827155777c7300a517d4ea45c73681ec0f34408761 | quote: | *?* DNS Records: | 50 | 200 | 2,000 | 20,000 | Unlimited |
  - [4] 2026-10-31: the Free DNS column of the plan table gives 1 DNS zone and 50 DNS records | capture: sha256:3a1c2a1ba0abbf3a53f018827155777c7300a517d4ea45c73681ec0f34408761 | quote: | *?* DNS zones: | 1 | 5 | 50 | 400 | Unlimited | | *?* DNS Records: | 50 | 200 | 2,000 | 20,000 | Unlimited |
  - [4] 2026-10-31: the Free DNS column of the plan table is '-' for Secondary DNS zones and for Zone transfers, so Free has neither | capture: sha256:3a1c2a1ba0abbf3a53f018827155777c7300a517d4ea45c73681ec0f34408761 | quote: | *?* Secondary DNS zones: | - | | | | | ... | *?* Zone transfers: | - | | | | |
  - [3] 2026-10-31: the signup form has a name, an e-mail and a password field and an hCaptcha, and no phone and no card field | capture: sha256:f331ab23860509b0db91de1bc3b07c839ba9fe47126fda2a142b9d5dc4e4986b | quote: placeholder="First and last name" ... placeholder="Enter your e-mail" ... placeholder="Password" ... class="h-captcha"
  - [2] 2026-10-31: an identity verification can be requested after signup | capture: sha256:c8284f272077fd66be4f68fa390f521ac8f1973bb059a677feb55faa36d4602a | quote: We reserve the right to request customer identity verification at our discretion
  - [8] 2026-10-31: the free plan's signup link is https://www.cloudns.net/index/show/signup/ | capture: sha256:bf4d9e73c58e5a1eb4d9e4534a2d47312d611c5fa7adb8b63bf498f05f96a077 | quote: [Sign Up for free](https://www.cloudns.net/index/show/signup/)
  - [3] 2026-10-31: the signup form asks for an e-mail address; it has no phone and no card field | capture: sha256:f331ab23860509b0db91de1bc3b07c839ba9fe47126fda2a142b9d5dc4e4986b | quote: name="mail" placeholder="Enter your e-mail"
  - [5] 2026-11-02: each A and AAAA record gets its own DynURL | capture: sha256:a394d3c4356abd505d0fff59fe5a3df0a106d08e8e5583cf5bb11bf50ff833e1 | quote: Dynamic DNS service by ClouDNS provides a unique URL called DynURL with each A (IPv4) and AAAA (IPv6) record.
  - [5] 2026-11-02: the vendor describes dynamic DNS as changing the IP address of one or multiple DNS records automatically | capture: sha256:a394d3c4356abd505d0fff59fe5a3df0a106d08e8e5583cf5bb11bf50ff833e1 | quote: Dynamic DNS is a DNS service, which provides the option to change the IP address of one or multiple DNS records automatically when the IP address of your device is changed dynamically by the internet provider.
  - [7] 2026-11-02: the Dynamic URL of an A or AAAA record is activated in the panel of its zone | capture: sha256:c50f89ff2c91994c1c5bcca80f9e64db93ad77087c9b5769fa3db4ce9123288e | quote: Find the A or AAAA record which you would like to be updated dynamically and click on the arrows on the row for this record. Afterwards, you have to Activate the Dynamic URL in the pop-up.
  - [4] 2026-11-02: the plan table marks HTTP API access absent on Free | capture: sha256:3a1c2a1ba0abbf3a53f018827155777c7300a517d4ea45c73681ec0f34408761 | quote: | *?* HTTP API access: | - | | | | |
- sources:
  - [1] https://www.cloudns.net/managed-dns/
  - [2] https://www.cloudns.net/tos/
  - [3] https://www.cloudns.net/ajaxPages.php?action=index&show=registerForm&registrationAction=signup-url&register=signup-url
  - [4] https://www.cloudns.net/premium/
  - [5] https://www.cloudns.net/dynamic-dns/
  - [6] https://www.cloudns.net/wiki/article/42/
  - [7] https://www.cloudns.net/wiki/article/255/
  - [8] https://www.cloudns.net/index/show/signup/
