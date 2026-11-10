# afraid.org FreeDNS

> afraid.org | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/afraid/ | JSON https://fshy.ajam.dev/api/v1/entity/afraid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## afraid.org FreeDNS

- `domains-dns/afraid-freedns` | qualifies-with-caveat | evidence documented | binding write-gated | category shared-registry subdomains and managed DNS
- needs card no, phone no, ID no, institution no | verified 2026-11-02T10:17:37.729Z (live) | stale on 2026-12-03
- url https://freedns.afraid.org/
- free tier: unlimited domains per account with 20 free subdomains on each, plus 5 free hostnames on a shared registry of 23,087 domains | unit: unlimited | metered on: object-count | read on: 2026-11-02 | source: [1]
- per-object cap: 5 hostnames on the shared registry and 20 subdomains on each domain you own, on the free plan | note: the paid plans raise the subdomain cap to 50, 100, 250 or 500 and add wildcard records, which the free plan lacks
- retention: a hosted domain that stays undelegated (broken) for 365 days is disabled; a shared-registry hostname lasts only while its domain stays in the registry, which the FAQ says may disappear next week | source: [2]
- egress: no query cap published | metered: no | source: [3]
- identity: email | detail: a first and last name, a user ID, a password and an e-mail address that receives the activation link, an image captcha, and a required checkbox declaring the user is not on a U.S. restricted list or in a U.S.-sanctioned territory; no phone and no card (https://freedns.afraid.org/signup/)
- interface: unknown
- limits:
  - per-object-cap: 5 free shared-registry hostnames and 20 subdomains on each domain you own [1]
  - write-gated (binding): a hostname on a Shared: Private domain can be rejected by that domain's owner, while a Shared: Public domain takes hostnames without the owner's approval [2]
  - write-gated (binding): the free plan keeps captchas, which every paid plan removes; the pricing table does not say which actions they guard [4]
- interface detail: no general record-management API is documented, and the /api/ page is behind a login, so its content is unverified: behind a sign-up; the site's client list says a client that sends a SHA1 hash of the user name and password can fetch the needed update URL itself; the free plan's programmatic path is the dynamic-update URL https://sync.afraid.org/u/<token>/ (https://v6.sync.afraid.org/u/<token>/ for IPv6), which changes the address of an existing record; other record edits, TXT included, are POSTs to https://freedns.afraid.org/subdomain/save.php with a logged-in session cookie; the interface term for the update URL would be dyndns, which the vocabulary lacks, so interface carries unknown
- tooling: curl against sync.afraid.org/u/<token>/; DD-WRT and router integrations
- composes with: a free hostname that resolves without owning a domain, which is the only thing here that does
- reliability: a shared-registry name is on someone else's domain, so its survival is their decision
- notes: The name is not yours and the owner can withdraw consent. It is a dynamic-DNS tool with a social dependency, not a name.
- evidence note: the landing, features, pricing, signup, signup Q&A and FAQ pages were read and quoted; the shared-registry cap of 5 hostnames and the 20-subdomain cap on an owned domain are first-party figures
- evidence:
  - [3] 2026-10-22: '23,246 domains in the shared domain registry'; dynamic update by URL token at sync.afraid.org/u/<token>/; free and premium subdomain and domain hosting
  - [5] 2026-10-22: the registry is a browsable list of domains a hostname may be attached to
  - [1] 2026-10-30: an account may host any number of owned domains; the same page counts 23,097 shared-registry domains | capture: sha256:8227876238a766b38022311fce710cb30bc8a342741b8dd7a98550017148f564 | quote: Unlimited number of domains per account (yes really)
  - [1] 2026-10-30: a free account gets 5 hostnames on the shared registry, a first-party figure | capture: sha256:8227876238a766b38022311fce710cb30bc8a342741b8dd7a98550017148f564 | quote: Comes with 5 free hostnames that work in the shared domain registry
  - [4] 2026-10-30: the subdomain cap is 5 on the free plan and 50, 100, 250 or 500 on the four paid plans | capture: sha256:4e93846147e892623809ea394a6d8335282bd20a0601d7e4a7717b6b6f31c5f6 | quote: Subdomain cap 5 50 100 250 500
  - [1] 2026-10-30: each domain the user owns gets 20 free subdomains | capture: sha256:8227876238a766b38022311fce710cb30bc8a342741b8dd7a98550017148f564 | quote: 20 free subdomains included on each of your own domains
  - [2] 2026-10-30: only a Shared: Private domain screens hostnames; a Shared: Public domain takes them without the owner's approval | capture: sha256:c4b6f7b8405458eb332e70a776d756fb3703e4aaa9f782d037389750e60e2b44 | quote: Shared: Public - means anyone in FreeDNS can setup a hostname using that domain without the domain owner's approval.
  - [4] 2026-10-30: the free plan keeps captchas and every paid plan removes them | capture: sha256:4e93846147e892623809ea394a6d8335282bd20a0601d7e4a7717b6b6f31c5f6 | quote: Captchas Removed No Yes Yes Yes Yes
  - [6] 2026-10-30: the signup form asks for a first and last name, a user ID, a password and an e-mail address | capture: sha256:39de7d687e77626ba2021c208378092f379348d4c3e37e70224f1a807b3cfb28 | quote: First Name Last Name UserID Password Password (confirm) E-Mail
  - [2] 2026-10-30: a TXT or other record edit outside the dynamic URL is a POST to subdomain/save.php with the logged-in session cookie; no token-based record API is documented | capture: sha256:c4b6f7b8405458eb332e70a776d756fb3703e4aaa9f782d037389750e60e2b44 | quote: You can get the dns_cookie by analyzing the saved cookie in your browser while logged in.
  - [3] 2026-10-30: the dynamic update is a GET of https://sync.afraid.org/u/<token>/, and of the v6.sync.afraid.org host for IPv6 | capture: sha256:366519d84d215ddef158e3710beae64b4dfe57a8e761162c047866fa38c9ff37 | quote: IPv6 updates? Easy, same as above, just add v6.
  - [2] 2026-10-30: a hosted domain that stays undelegated for 365 days is disabled | capture: sha256:c4b6f7b8405458eb332e70a776d756fb3703e4aaa9f782d037389750e60e2b44 | quote: If a domain remains in a broken state for 365 days, it is then disabled unless DNS authority returns.
  - [6] 2026-10-30: the signup form submits by sending an activation e-mail, so the account rests on an e-mail address | capture: sha256:39de7d687e77626ba2021c208378092f379348d4c3e37e70224f1a807b3cfb28 | quote: value="Send activation email"
  - [6] 2026-10-30: the signup form carries a required checkbox declaring the user is not in a U.S.-sanctioned territory | capture: sha256:39de7d687e77626ba2021c208378092f379348d4c3e37e70224f1a807b3cfb28 | quote: I confirm that I am not on any U.S. government restricted list and that I am not located or resident in a territory subject to U.S. sanctions
  - [6] 2026-10-30: the signup form carries an image captcha | capture: sha256:39de7d687e77626ba2021c208378092f379348d4c3e37e70224f1a807b3cfb28 | quote: [ Different Image ]
  - [4] 2026-10-30: wildcard records are absent on the free plan and unlimited on the paid plans | capture: sha256:4e93846147e892623809ea394a6d8335282bd20a0601d7e4a7717b6b6f31c5f6 | quote: Wildcard support None Unlimited
  - [3] 2026-10-30: the shared registry holds 23,097 domains | capture: sha256:366519d84d215ddef158e3710beae64b4dfe57a8e761162c047866fa38c9ff37 | quote: 23,097 domains in the shared domain registry. Click on any to attach, or use your own
  - [2] 2026-10-30: a shared-registry domain can leave the registry at any time, taking its hostnames with it | capture: sha256:c4b6f7b8405458eb332e70a776d756fb3703e4aaa9f782d037389750e60e2b44 | quote: The domain you choose may last for years and years, or it may disappear next week.
  - [7] 2026-10-30: the /api/ page redirects to the login page, so what it offers is behind a sign-in | capture: sha256:59db94e6130fbd92325701d4ae57a9233f0639d415f676182b081611d7c9989f | quote: Recover your password here
  - [1] 2026-10-31: the features page states the 5 free shared-registry hostnames of limits[0] | capture: sha256:2e69e05013470539531a6cd60e591d619812a4463d11edb675b22f6cd8fe4e7d | quote: Comes with 5 free hostnames that work in the shared domain registry
  - [1] 2026-10-31: the features page states the 20 free subdomains on each owned domain of limits[0] | capture: sha256:2e69e05013470539531a6cd60e591d619812a4463d11edb675b22f6cd8fe4e7d | quote: 20 free subdomains included on each of your own domains
  - [2] 2026-10-31: the FAQ states the Shared: Public half of the limits[1] rule | capture: sha256:c4b6f7b8405458eb332e70a776d756fb3703e4aaa9f782d037389750e60e2b44 | quote: Shared: Public - means anyone in FreeDNS can setup a hostname using that domain without the domain owner's approval.
  - [2] 2026-10-31: the FAQ states the Shared: Private half of the limits[1] rule | capture: sha256:c4b6f7b8405458eb332e70a776d756fb3703e4aaa9f782d037389750e60e2b44 | quote: Shared: Private - means the domain owner reserves the ability to reject hostnames that they deem slanderous or offensive.
  - [1] 2026-10-31: the values of limits[0] and limits[1] are unchanged on the features page and the FAQ | capture: sha256:2e69e05013470539531a6cd60e591d619812a4463d11edb675b22f6cd8fe4e7d | quote: 20 free subdomains included on each of your own domains
  - [8] 2026-11-02: the site's own client list says a client that sends a SHA1 hash of the user name and password can fetch the needed update URL itself | capture: sha256:a120d48942ee720f50e18535765dbef93d32a15c4bcd8615c666b54d22141a61 | quote: Gargoyle supports SHA1 hashing of username/password, so the client can fetch the needed update url dynamically (users need not supply the key needed to do the update).
  - [7] 2026-11-02: a request for the /api/ page without a session lands on the sign-in page, so the page content is behind a login | capture: sha256:523269e5231645c2e93013712cddaebad711d02f80b5f0a2d352d5c4b71d1b06 | quote: Keep getting thrown back here? Enable cookies.
  - probe:https://freedns.afraid.org/api/?action=getdyndns&sha=0000000000000000000000000000000000000000 2026-11-02: the /api/ endpoint ?action=getdyndns with a sha key, which third-party clients call to list update URLs, answers HTTP 200 with the text ERROR: Could not authenticate. to a placeholder key of forty zeros | capture: sha256:2907b7616e2de83d5a58ebeb7b757b4f30a8ad536ff72e26be0ce87979d60148 | quote: ERROR: Could not authenticate.
  - [9] 2026-11-02: third party: a ddclient issue ties the /api/ page to the v1 update protocol, which takes one request to get the update URL of a host and one to perform the update | capture: sha256:d4a5a3f6106cb5f22095b9c134f95abc261cbdc6f05f660f36ec15c0493345cc | quote: The [v1 update protocol](https://freedns.afraid.org/api/) is used, which requires two requests: one to get the update URL for the desired host and another to actually perform the update.
  - [10] 2026-11-02: third party: a client's README says the signed-in /api/ page offers Available API Interfaces links whose sha parameter is the account key | capture: sha256:fccc0d3026beac50c230ee84f1579442321db5e70e0642d43f07b14b955aa352 | quote: log into afraid.org and visit: http://freedns.afraid.org/api/ then click on either of the "Available API Interfaces" links and take the value of the "sha" parameter (it's a long string) from the url.
  - [11] 2026-11-02: third party: a script's comment places the API page under the Dynamic DNS menu as a Programmer's XML API with two interfaces, XML and ASCII | capture: sha256:cc4828f494dbfbe45388bd8c1acf97de7345806182f8c8f869b6189b9f10599f | quote: Dynamic DNS > Programmer's XML API > Available API Interfaces : XML | ASCII
  - [12] 2026-11-02: third party: the acme.sh maintainers say FreeDNS provides no API to update DNS records other than the IPv4 and IPv6 dynamic DNS addresses | capture: sha256:6451e746adf77b6173b87f9b3dc391f77e3c074989ee3b42762f5ac68446cfec | quote: does not provide an API to update DNS records (other than IPv4 and IPv6 dynamic DNS addresses)
  - [1] 2026-11-02: the features page counts 23,087 domains in the shared registry pool | capture: sha256:9df6de6eb5f711aef47074aad66020ada3c2efb529367e2bd8c4586813557169 | quote: currently 23,087 domains in the shared pool
  - [1] 2026-11-02: an account may host any number of owned domains | capture: sha256:9df6de6eb5f711aef47074aad66020ada3c2efb529367e2bd8c4586813557169 | quote: Unlimited number of domains per account (yes really)
  - [1] 2026-11-02: a free account gets 5 hostnames on the shared registry | capture: sha256:9df6de6eb5f711aef47074aad66020ada3c2efb529367e2bd8c4586813557169 | quote: Comes with 5 free hostnames that work in the [shared domain registry]
  - [1] 2026-11-02: each domain the user owns gets 20 free subdomains | capture: sha256:9df6de6eb5f711aef47074aad66020ada3c2efb529367e2bd8c4586813557169 | quote: 20 free subdomains included on each of your own domains
  - [13] 2026-11-02: the vendor describes the update path as a fetchable URL that auto-updates the network address, available in the Dynamic DNS section | capture: sha256:5bedaaeb1d196740356389dee453cd8d674dba3a7ae3891cc1451afa7a79e2bb | quote: a special fetchable URL to auto-update the network address in FreeDNS is available in the 'Dynamic DNS' section for those whose IP address changes at random.
- sources:
  - [1] https://freedns.afraid.org/signup/features/
  - [2] https://freedns.afraid.org/faq/
  - [3] https://freedns.afraid.org/
  - [4] https://freedns.afraid.org/pricing/
  - [5] https://freedns.afraid.org/domain/registry/
  - [6] https://freedns.afraid.org/signup/
  - [7] https://freedns.afraid.org/api/
  - [8] https://freedns.afraid.org/scripts/freedns.clients.php
  - [9] https://github.com/ddclient/ddclient/issues/180
  - [10] https://github.com/ekkis/afraid-dyndns
  - [11] https://beigebox.co.uk/programming/freedns-management-tool/
  - [12] https://github.com/acmesh-official/acme.sh/wiki/dnsapi
  - [13] https://freedns.afraid.org/signup/moreinfo/
