# Apple

> apple.com | Storage, Compute, Debrid; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apple/ | JSON https://fshy.ajam.dev/api/v1/entity/apple.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Apple Books (iTunes Connect / Partner)

- `storage/apple-books` | qualifies-with-caveat | evidence documented | binding per-object-cap | category Book publishing / distribution
- needs card yes, phone no, ID no, institution no | verified 2026-11-01T18:05:08.100Z, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://itunespartner.apple.com/books/
- free tier: 2 GB per book file, from Apple's own preparation page: 'Ideally, books should be under 1GB, but we allow up to 2GB on Apple Books. Books created with Pages must be under 1GB.' The asset file is an EPUB. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 2 GB, and 1 GB for a book created with Pages | bytes: 2000000000 | source: [2] | note: not stated
- retention: source: [2] | note: not stated
- egress: Apple-served; no hot-link. | metered: no
- identity: card | detail: an Apple Account with two-factor authentication and a card on file: Apple requires a valid credit card to sign up for iTunes Connect. Selling adds banking details and a tax form. No phone number is named.
- interface: cli
- limits:
  - per-object-cap (binding): per-object-cap 2 GB, and 1 GB for a Pages-made book [1]
- limits note: per-object-cap ~2 GB (secondary source only); EPUB fixed-layout allowed.
- interface detail: Transporter app / iTunes Connect web / content feed.
- tooling: Transporter CLI-adjacent, plus feed delivery.
- composes with: 2 GB ceiling, EPUB/PDF only, so it is a publishing channel rather than a store.
- reliability: Apple requires a card on file and an Apple Account with two-factor authentication to sign up, a tax form for every partner, and banking details to sell. The 2 GB per-file ceiling and the 1 GB ceiling for a Pages-made book are stated on Apple's preparation page.
- notes: 2 GB per book file, per the widely-cited store-limit table (Apple Books 2048 MB). Vendor page does not publish a per-file number in the fetchable docs.
- evidence note: the per-file ceiling, the account requirement and the banking and tax gate are quoted from Apple's own support pages, read on 2026-11-01.
- evidence:
  - [2] 2026-10-21: store size limits table 'Apple Books | 2048 MB'
  - [3] 2026-10-21: opened; contains only news items, no per-file size statement (so the 2 GB claim is unverified at source)
  - [4] 2026-11-01: signing up for iTunes Connect requires a valid credit card on file | capture: sha256:69ca35067aa826644af9b3d0d98782c5a982fef34b4486a5633d863d0628beb3 | quote: Use or create an Apple Account with two-factor authentication and a valid credit card on file to sign up for iTunes Connect.
  - [4] 2026-11-01: the account needs two-factor authentication, a legal entity and a card on file, plus a tax ID for a company | capture: sha256:69ca35067aa826644af9b3d0d98782c5a982fef34b4486a5633d863d0628beb3 | quote: An Apple Account enabled with two-factor authentication. ... A U.S. tax ID if you’re a company or a U.S.-based individual. ... Use or create an Apple Account with two-factor authentication and a valid credit card on file to sign up for iTunes Connect.
  - [1] 2026-11-01: Apple states a 2 GB per-file ceiling for an Apple Books asset, and 1 GB for a book made in Pages | capture: sha256:a2a30934e993debcc77ea14d8396d50e7a9e84c448696f9977dae0d1eeb235e3 | quote: Ideally, books should be under 1GB, but we allow up to 2GB on Apple Books. Books created with Pages must be under 1GB.
  - [1] 2026-11-01: the object ceiling is 2 GB, and 1 GB for a Pages-made book | capture: sha256:a2a30934e993debcc77ea14d8396d50e7a9e84c448696f9977dae0d1eeb235e3 | quote: Ideally, books should be under 1GB, but we allow up to 2GB on Apple Books. Books created with Pages must be under 1GB.
  - [1] 2026-11-01: the bound is a stated 2 GB per file, 1 GB for a Pages-made book | capture: sha256:a2a30934e993debcc77ea14d8396d50e7a9e84c448696f9977dae0d1eeb235e3 | quote: Ideally, books should be under 1GB, but we allow up to 2GB on Apple Books. Books created with Pages must be under 1GB.
  - [1] 2026-11-01: Apple's own preparation page states the per-file ceiling the row holds, in place of the third-party table | capture: sha256:a2a30934e993debcc77ea14d8396d50e7a9e84c448696f9977dae0d1eeb235e3 | quote: Ideally, books should be under 1GB, but we allow up to 2GB on Apple Books. Books created with Pages must be under 1GB.
  - [4] 2026-11-01: the card-on-file and two-factor requirement of the Apple Books account | capture: sha256:69ca35067aa826644af9b3d0d98782c5a982fef34b4486a5633d863d0628beb3 | quote: Use or create an Apple Account with two-factor authentication and a valid credit card on file to sign up for iTunes Connect.
  - [1] 2026-11-01: the record's headline figure is stated on Apple's own page, so the record is no longer inferred from a third-party table | capture: sha256:a2a30934e993debcc77ea14d8396d50e7a9e84c448696f9977dae0d1eeb235e3 | quote: Ideally, books should be under 1GB, but we allow up to 2GB on Apple Books. Books created with Pages must be under 1GB.
  - [1] 2026-11-01: a first-party page carries the record's number | capture: sha256:a2a30934e993debcc77ea14d8396d50e7a9e84c448696f9977dae0d1eeb235e3 | quote: Ideally, books should be under 1GB, but we allow up to 2GB on Apple Books.
  - [4] 2026-11-01: the Apple Books account is free to open and needs the fields the rows list | capture: sha256:69ca35067aa826644af9b3d0d98782c5a982fef34b4486a5633d863d0628beb3 | quote: We’re excited to see you getting started with Apple Books. The first thing you’ll need to do is sign up for an account — it’s free!
- sources:
  - [1] https://itunespartner.apple.com/books/support/9-prepare-book
  - [2] https://help.vellum.pub/uploading/
  - [3] https://itunespartner.apple.com/books/faq
  - [4] https://itunespartner.apple.com/books/support/4850-create-apple-books-account

## Apple Xcode Cloud

- `compute/xcode-cloud` | qualifies-with-caveat | evidence documented | binding write-gated | category macOS host
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T04:48:23.425Z (live) | stale on 2026-11-22
- url https://developer.apple.com/xcode-cloud/
- free tier: 25 compute hours a month included with Apple Developer Program membership, which is USD 99 a year; extra hours are sold from $49.99 a month for 100 | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: card | detail: 'Included with Apple Developer Program membership' - the membership is the gate and it is paid, quoted from developer.apple.com/xcode-cloud read 2026-10-22
- interface: unknown
- limits:
  - request-rate: 25 compute hours a month included, then 100 hours for $49.99, 250 for $99.99, 1,000 for $399.99 and 10,000 for $3,999.99 [1]
  - write-gated (binding): the hours are gated on an Apple Developer Program membership; there is no free account path to them [1]
  - per-object-cap: a workflow is configured in Xcode and runs against an app target, so it is a build of self-hosted code [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: Product documentation read on 2026-10-22 confirms 25 included compute hours per month with Apple Developer Program membership (USD 99 annually) and four paid tier upgrades.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: none
  - shape.note: Apple-run build infrastructure; the page sells hours, not shapes
  - session_cap.restart_required: no
  - session_cap.note: 25 compute hours a month is the allowance; a workflow is a build with its own timeout
  - free_tier_kind: allowance
  - reclassified_from: dead
  - ps.price: build artefacts are retained per Apple's policy
  - ps.durability: build artefacts
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the build's artefact retention
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '## Get started for free with Xcode' with '25 compute hours/month · Included with Apple Developer Program membership' and 'Apple Developer Program membership includes 25 compute hours per month', against '100 compute hours/month US$49.99/month' through '10,000 compute hours/month US$3,999.99/month', quoted
- sources:
  - [1] https://developer.apple.com/xcode-cloud/

## Vidi · Media Center

- `debrid/vidi-media-center` | self-hosted, last resort | verdict qualifies | evidence documented | binding none | category paid one-time media centre app for Apple platforms, Stremio addon API, debrid-aware | tier app purchase
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://apps.apple.com/us/app/vidi-media-center/id6648776878
- price USD 4.99
- free tier: No free tier: 'USD 4.99 · Designed for iPad'. One-time App Store purchase, no subscription line on the listing. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: A regional price was seen only through a search index (INR 499 on the Indian storefront); the USD 4.99 is from the US listing read directly.
- per-object cap: not applicable: a player | source: [2]
- retention: not applicable: progress syncs through iCloud; media stays with the debrid provider | source: [1]
- egress: No allowance: playback goes to whatever URL the installed addon returns. The app itself carries no traffic. | metered: no | free allowance: not applicable | source: [1]
- identity: card | detail: Apple ID with a payment method for a USD 4.99 purchase. No account with the developer. | country: None
- interface: rest
- limits:
  - write-gated: the App Store purchase is the gate; after it, the app imposes no published request or byte limit [1]
- limits note: The addon-API subset is the functional limit: an addon that relies on parts of the Stremio API Vidi does not implement will install and then misbehave, which is a support burden rather than a measurable cap.
- binding note: Nothing here counts bytes or requests; any 1 TiB/month wall is met at the addon or the debrid provider, not at the player.
- interface detail: 'Currently Vidi only supports addons using the Stremio addon API', with a subset documented on the vendor site. Native player with 'HDR10, HDR10+, and Dolby Vision'; progress syncs 'between your devices with iCloud'.
- tooling: App Store install for iPhone, iPad, Mac (Apple silicon), Apple TV and Vision. No server, no web app.
- composes with: The Apple-platform front end for the same addon URL a Stremio client would use: the debrid key lives inside the addon, so one key serves Vidi on an Apple TV and Stremio Web anywhere else.
- reliability: A single-developer App Store app: the risk is abandonment and iOS-version drift, not quota. It reached the App Store, which most addon front ends never do.
- notes: The only debrid front end with a publishable per-month cost of essentially zero after the first year: USD 4.99 once, versus USD 9/month for a hosted addon or USD 24/month for a hosted stack. It is the cheapest way to get a TV-native player with no server to run, on a device in Apple's ecosystem.
- evidence note: The US App Store listing and the vendor site were read. Not measured: installation and playback, and which addons pass the API subset.
- self hosted: yes
- extras:
  - developer: Plata o Plomo AB
  - api_subset: https://vidi.plomo.se/addons
  - license_shape: one purchase, all platforms, family sharing, no subscription
  - alternatives_seen: Streamyfin, Infuse, Swiftfin, Odin (Jellyfin clients, not debrid front ends)
- evidence:
  - [1] 2026-10-23: the price and platform list: '$4.99', 'Designed for iPad', iOS 17+/iPadOS 17+/macOS 14+ (M1)/tvOS 17+/visionOS 1.0+, 'Currently Vidi only supports addons using the Stremio addon API', iCloud progress sync, HDR10/HDR10+/Dolby Vision
  - [2] 2026-10-23: 'Purchase once and get it for all supported platforms', 'Family sharing enabled', 'No subscriptions', 'Supports Stremio Addons', 'Available on iOS, iPadOS and tvOS'
  - [3] 2026-10-23: reported, not read: a search index shows the Indian storefront listing '₹ 499', which would make the price regional rather than a single global number
- sources:
  - [1] https://apps.apple.com/us/app/vidi-media-center/id6648776878
  - [2] https://vidi.plomo.se/
  - [3] https://apps.apple.com/in/app/vidi-media-center/id6648776878
