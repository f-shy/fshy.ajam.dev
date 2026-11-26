# Namecheap FreeDNS

> namecheap.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/namecheap/ | JSON https://fshy.ajam.dev/api/v1/entity/namecheap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Namecheap FreeDNS

- `domains-dns/namecheap-freedns` | qualifies | evidence documented | binding write-gated | category managed authoritative DNS
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:39.218Z (live) | stale on 2026-12-20
- url https://www.namecheap.com/domains/freedns/
- free tier: free DNS hosting for domains registered elsewhere, with dynamic DNS | unit: unlimited | metered on: object-count | read on: 2026-10-22 | source: [1]
- per-object cap: at most 150 host records per domain pointed to FreeDNS (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL) | source: [1] | note: the 150-record count is stated on Namecheap's host-records support article; a general DNS limits page gives a higher count across BasicDNS/PremiumDNS/FreeDNS together, but the FreeDNS-specific limit governs this offer
- retention: the zone persists while it is configured; verification of nameserver changes takes up to 16 hours and the registrar gives 10 days to make the change | source: [1]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: email signup; the domain must be registered elsewhere
- interface: rest
- limits:
  - per-object-cap: at most 150 host records per domain pointed to FreeDNS [1]
  - write-gated (binding): third-party domains only, and nameserver verification takes up to 16 hours [1]
- interface detail: a web panel; an API exists for registered domains and is not documented for FreeDNS
- tooling: the web panel; dynamic DNS by URL
- composes with: a backup DNS for a domain whose primary is elsewhere, which is the use Namecheap itself names
- reliability: no suspension, throttle or data-loss event is recorded on the pages read
- notes: A general DNS limits article gives a higher combined record count across BasicDNS, PremiumDNS and FreeDNS, but the FreeDNS-specific host-records article states 150, which governs this offer
- evidence note: Namecheap's FreeDNS page and host-records support article were read and quoted; the 150-record per-object cap is stated on the vendor's own article, and the third-party-domain rule and nameserver timing on its FreeDNS page
- evidence:
  - [1] 2026-10-22: 'Free 3rd-party domains support only'; nameserver verification within 16 hours; 10 days to change nameservers at the current registrar. No record count is stated
  - [2] 2026-11-19: Namecheap's own host-records article states a 150-record maximum for FreeDNS | capture: sha256:ad99b69e4f6f9e2af0e1938794cd2991b3136134a556a158acafc533731a62fb | quote: The maximum amount of the records that can be added for a domain pointed to Free DNS is 150 records (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL).
  - [2] 2026-11-19: the FreeDNS-specific record cap is 150 and is first-party | capture: sha256:ad99b69e4f6f9e2af0e1938794cd2991b3136134a556a158acafc533731a62fb | quote: The maximum amount of the records that can be added for a domain pointed to Free DNS is 150 records (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL).
  - [2] 2026-11-19: the per-object-cap limit value is 150, stated first-party | capture: sha256:ad99b69e4f6f9e2af0e1938794cd2991b3136134a556a158acafc533731a62fb | quote: The maximum amount of the records that can be added for a domain pointed to Free DNS is 150 records (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL).
  - [2] 2026-11-19: the number that previously held the record at reported is now first-party | capture: sha256:ad99b69e4f6f9e2af0e1938794cd2991b3136134a556a158acafc533731a62fb | quote: The maximum amount of the records that can be added for a domain pointed to Free DNS is 150 records (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL).
  - [2] 2026-11-19: the record cap is now first-party, moving the deciding field to documented | capture: sha256:ad99b69e4f6f9e2af0e1938794cd2991b3136134a556a158acafc533731a62fb | quote: The maximum amount of the records that can be added for a domain pointed to Free DNS is 150 records (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL).
  - [2] 2026-11-19: 150 is the FreeDNS-specific cap, so no live zone count is needed to document it | capture: sha256:ad99b69e4f6f9e2af0e1938794cd2991b3136134a556a158acafc533731a62fb | quote: The maximum amount of the records that can be added for a domain pointed to Free DNS is 150 records (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL).
  - [2] 2026-11-19: the FreeDNS record cap and the fields it decides remain as stated | capture: sha256:ad99b69e4f6f9e2af0e1938794cd2991b3136134a556a158acafc533731a62fb | quote: The maximum amount of the records that can be added for a domain pointed to Free DNS is 150 records (including A, AAAA, CNAME, MX, SRV, TXT, NS, URL).
  - [1] 2026-11-19: the service is free DNS for third-party domains and is usable as a backup | capture: sha256:5baba3ff858073fc82c066b72c6042db303fb08d5238ee849bd51df0baeb4ca4 | quote: FreeDNS is for newly-registered domains if your domain registrar does not provide DNS hosting or can be a backup DNS for your existing website.
- sources:
  - [1] https://www.namecheap.com/domains/freedns/
  - [2] https://www.namecheap.com/support/knowledgebase/article.aspx/544/51/how-do-i-set-up-host-records-for-a-domain-when-i-use-freedns
