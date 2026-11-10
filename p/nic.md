# EU.org

> nic.eu.org | Domains and DNS; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nic/ | JSON https://fshy.ajam.dev/api/v1/entity/nic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EU.org

- `domains-dns/eu-org` | qualifies-with-caveat | evidence documented | binding write-gated | category free registrable subdomain
- needs card no, phone yes, ID no, institution no | verified 2026-11-02T10:17:37.009Z (live) | stale on 2026-12-03
- url https://nic.eu.org/
- free tier: free subdomain registration under EU.org; no page read states a renewal rule or a renewal fee | unit: objects | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: no record count is published; the cap is the review, not a number
- retention: no term, expiry date or renewal step is stated on the home, policy, registration or direct-subdomain pages, and none exists in the account-area templates and registry source published for the eu.org project: its domain list shows Created and Updated dates, its domain page offers Delete Domain, or Undelete during the grace period, and has no renewal control, and its one expiry job removes a deleted domain after a 30-day grace period | source: [1] | note: forum posters report subdomains still active with no renewal, and state that EU.org does not reclaim domains; two threads report a subdomain missing from an account, which other posters attribute to an account takeover
- egress: no query cap published | metered: no | source: [1]
- identity: email | detail: a contact with a name, an e-mail address (the form warns that Gmail addresses cannot receive the validation e-mail), a postal address of at least two lines and a country, with phone and fax optional; then a domain request whose nameservers already serve the zone, validated by a person in what the registration page calls a few days; no card (https://nic.eu.org/arf/en/contact/create/, https://nic.eu.org/register.html)
- interface: unknown
- limits:
  - write-gated (binding): every registration needs a human to validate it and 'can take a few days'; no approval rate and no queue length is published [2]
- interface detail: no API is documented: the contact and the domain request go through the web form at https://nic.eu.org/arf/; EU.org publishes only the NS delegation, so record management and any dynamic update are those of the DNS host the delegation names
- tooling: the nic.eu.org web form, then your own DNS provider
- composes with: a free domain that can be a Cloudflare zone, which is the only free option in this set that can
- reliability: the operator is a volunteer organisation and the review queue is the service
- notes: The gate is a person, not a number: a manual validation with no published queue length or approval rate. That is a discretionary throttle, and a design that depends on it has no ceiling to plan against.
- evidence note: the home, registration, general policy, direct-subdomain policy and contact-creation pages were read and quoted; they give the review time as a few days and state no renewal rule; the registry source and account-area templates published for the eu.org project hold no term, expiry or renewal feature for a live domain, but that source was last pushed in 2021 and the account area behind the sign-in is not readable without an account
- evidence:
  - [2] 2026-10-22: the six-step registration process, whose step 6 is 'Wait for an e-mail reply indicating that your request has been validated. This step requires human intervention and can take a few days.'
  - [3] 2026-10-22: the general policy: small commercial sites are accepted but 'VERY STRONGLY' asked to reserve a domain at an ICANN-accredited registrar instead
  - [1] 2026-10-30: registration is free; the home page says nothing of renewal | capture: sha256:f4bb66fa3a008d98dda2d873ef9b32a71cfc9a0d947154a0881e46f8bc5d9929 | quote: The main goal of EU.org is to provide free subdomain registration to users or non-profit organizations who cannot afford the fees demanded by some NICs.
  - [2] 2026-10-30: every request is validated by a person, in what the page calls a few days; the registration steps state no term and no renewal | capture: sha256:f15379ca018f5ef8babd8dd3f309efb5daa56abdb586aa6b3a928d5fcb5b4890 | quote: Wait for an e-mail reply indicating that your request has been validated. This step requires human intervention and can take a few days.
  - [4] 2026-10-30: a Gmail address cannot receive the contact validation e-mail | capture: sha256:e2b9fc59902554e6402a2446cbd16a861870446aefe8d31cdca9c1efd7e72d49 | quote: Don't use Gmail addresses here, you will not be able to validate your contact.
  - [5] 2026-10-30: EU.org serves only the NS delegation; records live on the DNS host the delegation names | capture: sha256:76bfe9aaa94003d8379aab6cc86d2bc2d0937c5f38621d1e4bb452008b21084c | quote: To minimize administration, only domain delegation (NS records) is provided.
  - [2] 2026-10-30: the account and the domain request are made in the web application at nic.eu.org/arf/ | capture: sha256:16d2f528d6a8f187618c9905237975c4aa0fa08e09990716b54070f070db7360 | quote: Create an account and request your domain here.
  - [4] 2026-10-30: the contact form asks for a name, an e-mail address and a postal address; name, e-mail, address lines 1 and 2 and country are required | capture: sha256:e2b9fc59902554e6402a2446cbd16a861870446aefe8d31cdca9c1efd7e72d49 | quote: Name E-mail Address (line 1) Address (line 2) Address (line 3)
  - [4] 2026-10-30: the phone field carries no required attribute, so a phone number is optional | capture: sha256:e2b9fc59902554e6402a2446cbd16a861870446aefe8d31cdca9c1efd7e72d49 | quote: <input type="text" name="ph1" maxlength="30" id="id_ph1">
  - [6] 2026-11-02: the registry configuration sets 30 grace days for restoring a deleted domain | capture: sha256:ed009fc2a52bb3eeb6c1fbae54a3606ba99bb3ef35313b2d3bf16f4be34e1e93 | quote: # number of grace days for domain restoration DEFAULT_GRACE_DAYS=30
  - [7] 2026-11-02: a registrant reports in a November 2024 thread that a subdomain registered earlier is still alive and was never renewed | capture: sha256:cc73235d4b3ec06ddd184748d95c5a20b039b37cf0063cc7eae71fb5045dcda0 | quote: 反正我之前注册的一个子域名到现在还活着了 也没有续期
  - [8] 2026-11-02: the repository is described as the source code for the eu.org project and its last push was on 2021-01-20 | capture: sha256:5d344789178ff8b01296541e818fb0e5631c07d9789289a950973b5a17edb413 | quote: "description": "Source code for the eu.org project", ... "pushed_at": "2021-01-20T13:47:58Z"
  - [9] 2026-11-02: the registry's sample crontab has one expiry job, a daily run described as domain grace period expiration | capture: sha256:d07bbdf62776af0f427488ecf6279b895e051d4cb33469e0b1ff584f6ca9ac86 | quote: # domain grace period expiration 0 0 * * * autoreg /usr/local/bin/autoreg-expire
  - [10] 2026-11-02: the registry's domains table holds created_on, updated_on and end_grace_period and no expiry or renewal column | capture: sha256:f0de87a5faacefc96997671d6eff4452bb83f7bc83d544260c78a4f6291ccc8e | quote: created_on TIMESTAMP WITH TIME ZONE, updated_by INTEGER REFERENCES admins(id) DEFAULT 0, updated_on TIMESTAMP WITH TIME ZONE, end_grace_period TIMESTAMP WITH TIME ZONE,
  - [11] 2026-11-02: the account area's domain page offers Delete Domain, or Undelete until the end of the grace period, and has no renewal control | capture: sha256:42145255e1be0fb561ad33d80898e8df120b62e6251603ac7a41528ac660c632 | quote: <INPUT class="miniaction" TYPE="submit" NAME="del" VALUE="{% trans "Delete Domain" %}">
  - [12] 2026-11-02: the account area's domain list has the columns Domain, Created, Updated, DNSSEC and Flags and no expiry column | capture: sha256:fec085d767c5cac896bcf30a3ed7e9a86e8a1f94c5bdb6500f8e719411554a1c | quote: <tr><th>{% trans "Domain" %}</th><th>{% trans "Created" %}</th><th>{% trans "Updated" %}</th><th>DNSSEC</th><th>{% trans "Flags" %}</th></tr>
  - [13] 2026-11-02: the account application's routes include domain edit, delete and undelete and list no renewal or extension route | capture: sha256:f286a869ea9b5e0e042e4671f53c48d440091faca218081813d9fcfe799b1271 | quote: re_path(r'^domain/del/(?P<fqdn>[a-z0-9\.-]+)/$', whois_views.domaindelete, name='domaindelete'), re_path(r'^domain/undel/(?P<fqdn>[a-z0-9\.-]+)/$',
  - [14] 2026-11-02: the repository README calls this the software that has run most of eu.org since 1996 | capture: sha256:5bdb8db10612c7bcd674ef2bd5c219af96a40fa232331d30a1c74724bca98bb2 | quote: Autoreg (formerly known as AutoReg 4.1, short name AR41, now retired), is the software that's been running most of eu.org since 1996.
  - [2] 2026-11-02: step 6 of the six registration steps: every request is validated by a person, in what the page calls a few days; the steps state no term or renewal | capture: sha256:16d2f528d6a8f187618c9905237975c4aa0fa08e09990716b54070f070db7360 | quote: Wait for an e-mail reply indicating that your request has been validated. This step requires human intervention and can take a few days.
  - [15] 2026-11-02: a registrant whose subdomains vanished from an account says there is no precedent of a domain being reclaimed and suspects an account takeover | capture: sha256:03c2d99e493c49b167eb0bd9862bc1f9307fdcf4e76e2c75169507b5000ff3ef | quote: 好像没有域名被收回的先例，估计被盗号过户给其他账号了。
  - [16] 2026-11-02: a poster in a thread about a subdomain missing from an account says EU.org does not reclaim domains and that long-idle subdomains are still present | capture: sha256:934f50971a0607b9750e1e35f2ac02b64964239b0e43602498ddbf356cde4631 | quote: eu不存在收回域名的情况，我的闲置很长时间了，查看还都在。
  - [1] 2026-11-02: the home page states free subdomain registration and says nothing of a term, expiry or renewal | capture: sha256:59648ecbbdad87d14f4ecff82695b81e190cad881abf4f90579b077b4b2f9afb | quote: The main goal of EU.org is to provide free subdomain registration to users or non-profit organizations who cannot afford the fees demanded by some NICs.
- sources:
  - [1] https://nic.eu.org/
  - [2] https://nic.eu.org/register.html
  - [3] https://nic.eu.org/policy.html
  - [4] https://nic.eu.org/arf/en/contact/create/
  - [5] https://nic.eu.org/top-policy.html
  - [6] https://raw.githubusercontent.com/pbeyssac/autoreg/master/autoreg/conf.py
  - [7] https://www.nodeloc.com/t/topic/29964
  - [8] https://api.github.com/repos/pbeyssac/autoreg
  - [9] https://raw.githubusercontent.com/pbeyssac/autoreg/master/sample-config/crontab
  - [10] https://raw.githubusercontent.com/pbeyssac/autoreg/master/postgres/autoreg.schema
  - [11] https://raw.githubusercontent.com/pbeyssac/autoreg/master/autoreg/arf/templates/whois/domainedit.html
  - [12] https://raw.githubusercontent.com/pbeyssac/autoreg/master/autoreg/arf/templates/whois/domainlist.html
  - [13] https://raw.githubusercontent.com/pbeyssac/autoreg/master/autoreg/arf/arf/urlsubs.py
  - [14] https://raw.githubusercontent.com/pbeyssac/autoreg/master/README.md
  - [15] https://www.nodeseek.com/post-104532-1
  - [16] https://www.hostloc.net/thread-274687-1-1.html
