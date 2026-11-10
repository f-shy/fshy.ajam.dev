# freemyip.com

> freemyip.com | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freemyip/ | JSON https://fshy.ajam.dev/api/v1/entity/freemyip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## freemyip.com

- `domains-dns/freemyip` | qualifies-with-caveat | evidence measured | binding retention-clamped | category free dynamic subdomain
- needs card no, phone no, ID no, institution no | verified 2026-11-03T16:43:10.325Z (live) | stale on 2027-02-02
- url https://freemyip.com/
- free tier: free dynamic DNS subdomains under freemyip.com, with no login, no ads and no expiration date stated on the home page; any subdomain of the name returns the same address | unit: objects | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: no count of subdomains per user or per address is published on the pages read
- retention: the subdomain can be kept as long as wanted if the address is updated at least once a year, even with the same address; a deleted subdomain cannot be created again for 12 months | days: 365 | source: [2]
- egress: no query cap published | metered: no | source: [2]
- identity: anonymous | detail: no login is required, according to the home page; the update URL carries a token and a domain, and the creation flow itself was not run
- interface: rest
- limits:
  - retention-clamped (binding): the address must be updated at least once a year, even when it has not changed, to keep the subdomain [2]
- binding note: the yearly update is the only stated limit; the count of names is unverified; no sign-up is asked, so the token returned at creation is the only handle, and the zone is the vendor's
- interface detail: one HTTPS GET to /update with token and domain parameters sets the address; optional parameters set an IPv4 or IPv6 address (myip), a TXT record (txt, also applied to every subdomain of the name), a verbose reply (verbose) or a delete (delete); the reply is the text OK or ERROR with HTTP status 200
- tooling: curl, a browser, a router or any scheduler that can request a URL
- composes with: a free name with a TXT parameter that the help page says also works for any subdomain of the name, so a DNS-01 challenge record can be set by inference; a CNAME or DNAME from the user's own domain can point at it; the zone is the vendor's, so it cannot be a Cloudflare zone
- reliability: an update with a token that does not exist returns HTTP 200 with the body 'ERROR' and a line naming the token, so a status-only check reports success on a failed update; the suffix is on the Public Suffix List, so the TLS limit counts per name
- notes: The only anonymous name in this set: no login, a token and a yearly update. The vendor's clock binds, not an owner's consent: a name lapses when the address is not updated for a year. The zone is the vendor's. The TLS limit does not bind, because the suffix is listed.
- evidence note: the update endpoint was called with a token that does not exist and answered 200 with an ERROR body, which proves the endpoint and the failure shape; the home and help pages were read and quoted; the creation flow was not run, because it makes a name
- evidence:
  - probe:https://freemyip.com/update?token=invalid&domain=invalid.freemyip.com&verbose=yes 2026-11-03: the update endpoint answers HTTP 200 to a request with a token that does not exist | capture: sha256:6945fd34016632931e063dbc7472dba787004c5c295c0ede049c25244d3759da | quote: "status": 200
  - probe:https://freemyip.com/update?token=invalid&domain=invalid.freemyip.com&verbose=yes 2026-11-03: the body of that 200 is the word ERROR, followed by a line naming the missing token | capture: sha256:d62b9b75d3a6cd964387a847c704a6dd1d8b588b3a603bb33d6ce0aac0453423 | quote: ERROR
  - [1] 2026-11-03: free dynamic DNS with no login | capture: sha256:d8764f1fbad17fd7832d97fe3764796423ded30fb89dccdfa9ec5c30b8d81646 | quote: Free dynamic DNS. No login required. No ads, newsletters, links to click, expiration dates, etc.
  - [2] 2026-11-03: a subdomain is kept by updating the address at least once a year | capture: sha256:150263aedbd2cea4b2c8c07f029af92f9189478fe7b39358aea41135cd7f7853 | quote: You can keep your subdomain as long as you want, but you have to update your IP at least once a year.
  - [2] 2026-11-03: a deleted subdomain cannot be re-created for 12 months | capture: sha256:150263aedbd2cea4b2c8c07f029af92f9189478fe7b39358aea41135cd7f7853 | quote: your subdomain will be permanently deleted, and it won't be possible to create the same subdomain within 12 months
  - [2] 2026-11-03: any subdomain of the name returns the same address | capture: sha256:150263aedbd2cea4b2c8c07f029af92f9189478fe7b39358aea41135cd7f7853 | quote: Yes. Any subdomain in your domain will return your IP address.
  - [2] 2026-11-03: a TXT record is set by a txt parameter on the update URL | capture: sha256:150263aedbd2cea4b2c8c07f029af92f9189478fe7b39358aea41135cd7f7853 | quote: https://freemyip.com/update?token=YOUR_TOKEN&domain=YOUR_DOMAIN.freemyip.com&txt=my%20test%20text
  - [2] 2026-11-03: the user's own domain can point at the name by CNAME | capture: sha256:150263aedbd2cea4b2c8c07f029af92f9189478fe7b39358aea41135cd7f7853 | quote: Yes. You can set a CNAME record inside your own domain to point to your subdomain at freemyip.com.
  - [3] 2026-11-03: freemyip.com is an entry of the private section of the Public Suffix List | capture: sha256:617d1b276660e5a01209d7b58159450e400cf636634a7a9c2cfd50a1c6675d01 | quote: // freemyip.com : https://freemyip.com
  - [4] 2026-11-03: Let's Encrypt finds the registered domain with the Public Suffix List | capture: sha256:b5eee1fee7260f24a875dbca422432161e1e6e37041c64df017d7057af897c00 | quote: We use the [Public Suffix List](https://publicsuffix.org/) to identify registered domains.
- sources:
  - [1] https://freemyip.com/
  - [2] https://freemyip.com/help
  - [3] https://publicsuffix.org/list/public_suffix_list.dat
  - [4] https://letsencrypt.org/docs/rate-limits/
