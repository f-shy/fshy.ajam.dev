# Debrid Stream

> debridstream.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/debridstream/ | JSON https://fshy.ajam.dev/api/v1/entity/debridstream.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Debrid Stream

- `debrid/debridstream` | qualifies-with-caveat | evidence documented | binding write-gated | category hosted front end for a debrid account (Android TV, Fire TV, mobile) with a web account portal | tier free (Pro is a paid unlock)
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:28:11.000Z (live) | stale on 2026-11-23
- url https://debridstream.com/
- price USD 0
- free tier: 'Free - The essentials, done well: Beautiful, snappy interface / Kids profile / JustWatch integration / Frequent updates'. Pro adds '3-day free trial' and the playback features. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The site does not print a Pro price; it defers to an in-app purchase on Google Play. A forum post put it at '£10 a year' (reported, December 2024).
- per-object cap: not applicable: a player, not a store | source: [1]
- retention: not applicable: the library is the debrid account | source: [1]
- egress: Not metered by the app. Playback pulls from the debrid provider, so the provider's caps apply; Debrid Stream publishes no traffic figure of its own. | metered: no | free allowance: not published | source: [1]
- identity: card | detail: Google Play account for the app and a paid unlock for Pro, on top of a debrid subscription. The app itself installs free. | country: None
- interface: rest
- limits:
  - write-gated (binding): playback features sit behind the Pro unlock: auto-play, link filtering, custom catalog, Trakt, OpenSubtitles and third-party addons are all Pro-only [1]
- limits note: The free tier is a browsing shell: it can list and play, but the automated-source-selection and addon ecosystem that make a debrid front end usable are paywalled. The app also cannot be driven from a desktop browser.
- binding note: No byte cap is published, so the first thing that stops a working pipeline is the Pro paywall, which removes auto-play, filtering and addon support from the free tier.
- interface detail: The site's 'Configure your account' button points at account.debridstream.com, which is where a debrid key is entered (third-party write-ups describe that portal and the Google TV app as the two ways to paste a key into a TV). No browser playback is advertised: the screens are Android TV, Fire TV and mobile.
- tooling: an installable app per platform plus the web portal. The portal exists precisely so a TV remote never has to type a 40-character key.
- composes with: The alternative front end when a television-shaped app is wanted rather than a Stremio addon list: it holds the debrid key centrally and adds Trakt scrobbling and OpenSubtitles on the paid tier.
- reliability: Store-distributed app: the free tier's feature set can change with a Play Store update, and reports of the price come from forum posts rather than the vendor.
- notes: Included because it is the one front end found that is neither an addon nor a browser tab: a hosted account service plus native TV apps. Its weakness here is the same as every app: it needs a device, and the free tier is the shell rather than the engine.
- evidence note: The landing page was read and both tiers are quoted. Not measured: installation, playback, and the actual Pro price, which is only visible inside Google Play. That the portal is the key-entry path is inferred from the button label plus third-party posts, not from the portal itself.
- extras:
  - portal: https://account.debridstream.com/
  - play_store: https://play.google.com/store/apps/details?id=com.debridstream.tv
  - pro_price: unverified: in-app purchase, forum says £10/year (Dec 2024)
- evidence:
  - [1] 2026-10-23: the platform list (Android TV, Fire TV, Mobile), the Free/Pro split and the exact Pro feature list, plus 'Configure your account' at account.debridstream.com
  - [2] 2026-10-23: third-party (December 2024): 'It's £10 a year' - the only published price found; reported, not confirmed by the vendor
  - [3] 2026-10-23: third-party: the key is pasted through the web portal or the Google TV app, which confirms the portal is the configuration path
- sources:
  - [1] https://debridstream.com/
  - [2] https://www.techkings.org/threads/debridstream-vod-app.174011/
  - [3] https://redlib.vanillax.me/r/addons_debrid_stream/comments/1pfnfra/how_to_configure_your_debridstream_account/
