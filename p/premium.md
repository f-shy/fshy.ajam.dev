# premium.to

> premium.to | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/premium/ | JSON https://fshy.ajam.dev/api/v1/entity/premium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## premium.to

- `debrid/premium-to` | paid-only | evidence documented | binding volume-quota | category premium link generator (credit-based, host list only) | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://premium.to/
- free tier: No free tier is published. The landing page is a host table and nothing else: no price, no allowance, no signup link, no FAQ, no terms. The only other page is an OpenSearch XML descriptor. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: What the page does state: a host list (alfafile, turbobit, filer.net, 1fichier, ddownload, rapidgator, filestore.to, mega.nz) with asterisks marking 'limited traffic' and 'no guarantee', plus torrent and usenet rows.
- per-object cap: unstated on the page; the asterisks mark hosts where traffic is limited | source: [1]
- retention: unverified: no statement. | source: [1]
- egress: Not published. A credit balance is implied by the service type but no price or allowance appears on any page reached. | metered: yes | free allowance: none published | source: [1]
- identity: email | detail: No signup page is linked from the landing page, so the registration fields are unverified. A paid credit service of this shape normally requires an email account; that is inference, not observation.
- interface: rest, unknown
- limits:
  - request-rate: unstated [1]
  - volume-quota (binding): unstated; credits are implied, not documented [1]
- limits note: The asterisks are the only limit information on the site: 'limited traffic' on alfafile and turbobit, 'no guarantee' on ddownload and rapidgator. Neither is quantified.
- binding note: If the service sells credits, the credit balance is what fails first at 1 TiB/month; because no rate is published, only the kind can be named, not the point of failure.
- interface detail: The OpenSearch descriptor publishes a GET endpoint: 'https://premium.to/getfile.php?link={searchTerms}'. That is a browser search shortcut, but it is also a public HTTP entry point that takes a link, which a wrapper can call.
- endpoint: part of interface detail
- tooling: The site links to JDownloader, so a JD plugin or manual paste is the intended client. No API documentation exists.
- composes with: A credit service would slot in exactly where a debrid account does, but without a published price the cost per TB cannot be computed, so it cannot be ranked against the debrid services.
- reliability: The public endpoint returned HTTP 200 with a zero-byte body when handed a non-host URL, which is the classic false 200: a wrapper must check bytes, not status. The site publishes no status page and no terms.
- notes: A name that recurs in old debrid lists, still resolving, with almost no published information. The endpoint existing does not make it usable: the empty 200 means a caller learns nothing without a valid host link, and the host list is the only evidence the service does anything.
- evidence note: The host list, the absence of pricing and the endpoint are all observed; the paid-only verdict is inferred from the absence of any free path. One probe of the endpoint produced a measured empty 200.
- extras:
  - open_search_endpoint: https://premium.to/getfile.php?link={searchTerms}
  - page_word_count: 65
  - pricing_published: no
- evidence:
  - [1] 2026-10-23: the host table with 'limited traffic' and 'no guarantee' asterisks, torrent and usenet rows, and the total absence of price, allowance or signup text (65 words on the page)
  - [2] 2026-10-23: OpenSearch template GET https://premium.to/getfile.php?link={searchTerms}, i.e. the public link-taking endpoint
  - probe:https://premium.to/getfile.php?link=https%3A%2F%2Fexample.com%2F 2026-10-23: HTTP 200 with 0 bytes and sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; the probe flags it as a false 200 of kind 'empty'
  - probe:https://premium.to/ 2026-10-23: landing page answers: HTTP 200, 4385 bytes, sha256 796b1480e67fb78a...
- sources:
  - [1] https://premium.to/
  - [2] https://premium.to/premiumto.xml
