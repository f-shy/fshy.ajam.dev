# Hurricane Electric Free DNS

> he.net | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/he/ | JSON https://fshy.ajam.dev/api/v1/entity/he.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hurricane Electric Free DNS

- `domains-dns/he-dns` | qualifies-with-caveat | evidence documented | binding write-gated | category managed authoritative DNS
- needs card no, phone yes, ID no, institution no | verified 2026-11-02T10:17:37.730Z (live) | stale on 2026-12-03
- url https://dns.he.net/
- free tier: free hosted forward and reverse DNS with multiple domains per account, in open beta, for IPv6 certification or tunnelbroker account holders, colocation customers and transit customers | unit: objects | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: no record count is published
- retention: zones persist while the account is active | source: [1]
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: one free registration shared by ipv6.he.net, tunnelbroker.net and dns.he.net, whose form requires an account name, a password, an e-mail address that receives the activation link, a first and last name, a country, a street address, a city, a state or region, a postal code, a phone number and a captcha code; the phone number is posted to the server for a check as it is filled and the form has no field for a code from the phone; whether a code is sent to the phone after the form is submitted is unverified: behind a sign-up; no card is asked; existing admin.he.net customers ask support for a password (https://tunnelbroker.net/register.php, https://ipv6.he.net/certification/register.php, https://dns.he.net/)
- interface: unknown
- limits:
  - write-gated (binding): the service is in open beta and is limited to IPv6 certification or tunnelbroker account holders, colocation customers and transit customers; no record count and no query cap is published [1]
- interface detail: no record-management API is documented on dns.he.net or dns.he.net/docs.html; the programmatic path is the dyndns-compatible endpoint https://dyn.dns.he.net/nic/update?hostname=<record>&password=<key>&myip=<address> (GET, POST, or HTTP basic auth with the record name as the user), one request for IPv4 and one for IPv6, and txt= in place of myip= for a TXT record first created in the panel; the dynamic service is included free with a dns.he.net account; the update URL changes the address of an A or AAAA record, or the value of a TXT record, that already exists, and its interface term would be dyndns, which the vocabulary lacks, so interface carries unknown
- tooling: the web panel for zone and record management; the dyndns URL for dynamic A, AAAA and TXT records; no SDK and no documented REST API
- composes with: reverse DNS and secondary zones, which the other free providers in this set do not do as readily
- reliability: the registration form is withheld from some source networks, which receive 'Your IP address is not permitted to register at this time (This network is restricted)' in its place
- notes: An unpublished cap is a discretionary throttle. A design that depends on it has no ceiling to plan against, which is worse than a small published one. The interface field is 'unknown' rather than 'rest' because the only programmatic path is a key-based dyndns URL, which cannot create a zone or enumerate records.
- evidence note: the service page was read and states the eligibility gate and the dyndns syntax.
- evidence:
  - probe:https://dns.he.net/ 2026-10-22: 200, 16,458 bytes, the service page and login portal; the service answers and requires an account
  - [1] 2026-10-22: 'The Open Beta has been expanded and now includes our IPv6 certification or tunnelbroker account holders, Colocation customers and those with Transit services'; 'Multiple domains per account.'; the dyndns update syntax with separate ipv4 and ipv6 values and a txt= variant for Let's Encrypt DNS-01, where the dynamic record must be created in the panel first
  - [2] 2026-10-30: the shared Hurricane Electric registration form marks the phone number as required, beside the account name, e-mail, names, country and full postal address | capture: sha256:0ac6b1658850670eb65337e26f8f7631f673078036b98319df46c84bcebb66ac | quote: * Phone:
  - [3] 2026-10-30: the registration page withholds the form from some source networks | capture: sha256:c113ba8895bad0f22dd78938a0e63fb4f0e4e0f2f9145b24af03adb529be016d | quote: Your IP address is not permitted to register at this time (This network is restricted)
  - [4] 2026-10-30: the dynamic-update service is included free with a dns.he.net account | capture: sha256:39fb027a5a5c5576ba02689be2435613a2e17a1c9c5bbe7ce067367cf53151aa | quote: We do not currently charge for this service. it is included for free with your dns.he.net account.
  - [2] 2026-10-30: the account is activated by an e-mail link; the same registration covers ipv6.he.net, tunnelbroker.net and dns.he.net | capture: sha256:0ac6b1658850670eb65337e26f8f7631f673078036b98319df46c84bcebb66ac | quote: After completing registration, an email will be sent to complete activating your account.
  - [1] 2026-10-30: the eligible account is a free registration, not a paid relationship | capture: sha256:f7f8753e76eb424cc8da7c2ca4ee446d32e16f1e5061c33ea259c03993162a36 | quote: If you do not have an account, you can sign up for a free one
  - [4] 2026-10-30: the update path is dyn.dns.he.net/nic/update with hostname, password and myip parameters; the docs document no other API | capture: sha256:39fb027a5a5c5576ba02689be2435613a2e17a1c9c5bbe7ce067367cf53151aa | quote: curl "https://dyn.dns.he.net/nic/update?hostname=dyn.example.com&password=password&myip=192.168.0.1"
  - [1] 2026-10-30: the service remains an open beta for IPv6 certification or tunnelbroker account holders, colocation and transit customers | capture: sha256:f7f8753e76eb424cc8da7c2ca4ee446d32e16f1e5061c33ea259c03993162a36 | quote: The Open Beta has been expanded and now includes our
  - [4] 2026-11-02: the dynamic DNS service updates the IPv4 and IPv6 address of A and AAAA records of domains managed on dns.he.net, through a simple web request or any dyndns compatible client | capture: sha256:39fb027a5a5c5576ba02689be2435613a2e17a1c9c5bbe7ce067367cf53151aa | quote: Our dynamic DNS service will allow you to update the IPv4 and IPv6 address of your A and AAAA records of domains that you manage using dns.he.net through the use of a simple web request or using any dyndns compatible client.
  - [2] 2026-11-02: the registration form carries a captcha code input beside the phone number input | capture: sha256:5d186f8f229a9b0031e9759eb56dd6fde1ddf41dea90c5411f245ef38fa034dc | quote: <input type="text" name="captcha_code" id="captcha_code" needed="needed" />
  - [4] 2026-11-02: the zone to be updated dynamically is created before the dynamic DNS service is used | capture: sha256:39fb027a5a5c5576ba02689be2435613a2e17a1c9c5bbe7ce067367cf53151aa | quote: To use the dynamic DNS feature, you will first need to create a domain or subdomain (the zone) that you want to use with the dynamic DNS service.
  - [1] 2026-11-02: a dynamic TXT record cannot be created or deleted through the update URL | capture: sha256:f7f8753e76eb424cc8da7c2ca4ee446d32e16f1e5061c33ea259c03993162a36 | quote: You will not be able to dynamically create and delete these TXT records as doing so would subsequently remove your ddns key associated with the record.
  - [2] 2026-11-02: the registration form's phone number is a plain text input marked needed | capture: sha256:5d186f8f229a9b0031e9759eb56dd6fde1ddf41dea90c5411f245ef38fa034dc | quote: <input type="text" name="phone" id="phone" value="" needed="needed" />
  - [2] 2026-11-02: the registration form posts each field marked needed to the server for a check as it is filled and shows the error text the server returns | capture: sha256:5d186f8f229a9b0031e9759eb56dd6fde1ddf41dea90c5411f245ef38fa034dc | quote: $.post('/register.php?ajax=true', { field: obj.attr('name'), value: obj.val() }, function(data) { if(data.length > 0) { obj.next('span').addClass('fieldError').text(data);
  - [3] 2026-11-02: the registration form that dns.he.net links to carries the same captcha code input | capture: sha256:078c934a9a60b6521f67fc8fac7bd472344a39736d24f5dbe1ac94ae03c729ec | quote: <input type="text" name="captcha_code" id="captcha_code" needed="needed" />
  - [5] 2026-11-02: third party: a user on the vendor's forum reports that registration refused an outlook.com address (April 2021) | capture: sha256:6e389c1235358fd5a735060ab7deb1ac6644d145117bfd4edd7591dcbe31120d | quote: Outlook.com addresses aren't allowed.
  - [6] 2026-11-02: third party: a user reports that registration answered Invalid registration data until the postal code and the phone number had an accepted format (May 2021) | capture: sha256:ba78ee67693483d8e9e54103ad3a13ffd3eb956078637277a07b1bfa84e83b03 | quote: 经过不断的尝试，初步确定是邮编和电话格式的原因
  - [2] 2026-11-02: the registration form's only stated activation step is an e-mail sent after registration | capture: sha256:0ac6b1658850670eb65337e26f8f7631f673078036b98319df46c84bcebb66ac | quote: After completing registration, an email will be sent to complete activating your account.
- sources:
  - [1] https://dns.he.net/
  - [2] https://tunnelbroker.net/register.php
  - [3] https://ipv6.he.net/certification/register.php
  - [4] https://dns.he.net/docs.html
  - [5] https://forums.he.net/index.php?action=printpage;topic=4094.0
  - [6] https://www.ivu4e.cn/blog/service/2021-05-27/672.html
