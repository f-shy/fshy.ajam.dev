# MeggaFast

> meggafast.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/meggafast/ | JSON https://fshy.ajam.dev/api/v1/entity/meggafast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MeggaFast

- `debrid/meggafast-meggabox-125gb` | paid-only | evidence documented | binding none | category shared seedbox (small slots) | tier MeggaBox 125GB
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:15.242Z (live) | stale on 2026-12-04
- url https://meggafast.com/order/
- free tier: No free tier and no trial is published for seedboxes; the entry box is MeggaBox 125GB at GBP 4.00/month plus an 8% PayPal transaction fee. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The site's free trial offer is for its Xtream-TV service, not for seedboxes.
- per-object cap: not applicable: sold by total disk (125, 250, 500 and 950 GB); no single-file cap is published | source: [1]
- retention: for the life of the subscription; no inactivity deletion is stated | source: [1]
- egress: 'Unlimited Downloads / Uploads' on a 1 GB port with 'FTP over TLS (faster)'; public trackers are allowed at a 2:1 ratio. | metered: no | free allowance: unlimited stated | source: [1]
- identity: email | detail: The order form asks for a username and password and redirects to PayPal; the home page lists crypto and PayPal guest checkout. Email, phone and document requirements were not read: unverified. | country: None
- interface: ftps
- limits:
  - per-ip-shaping: 1 Gbit port; public trackers limited to a 2:1 ratio [1]
- limits note: Shared boxes: 125 GB GBP 4.00, 250 GB GBP 5.00, 500 GB GBP 6.00, 950 GB GBP 9.00 a month; dedicated seedboxes: 1 TB GBP 15.00, 2 TB GBP 20.00, 4 TB GBP 30.00 a month.
- binding note: No quota or object cap is published; the 125 GB disk is the number a buyer can plan around.
- interface detail: 'FTP over TLS (faster)' plus a user dashboard to reset and clean up the box; the dedicated seedbox tiers add SSH root access.
- tooling: FTP over TLS client and the vendor dashboard; no API or CLI is documented on the page read
- composes with: A GBP 4 125 GB seedbox with an FTPS pull path; paid through a PayPal redirect
- reliability: 'Unlimited' is a claim with no fair-use numbers published on the page read; the 8% PayPal fee is added to the price.
- notes: Dedicated Seedbox 1TB is listed at GBP 15.00/month on the same page.
- evidence note: Plan, price, protocol and payment route are on the vendor pages read on 2026-11-03. A measured rung needs a slot and a timed transfer.
- extras:
  - port_gbps: 1
  - minimum_term: monthly
  - trial_card_required: no seedbox trial exists
- evidence:
  - [1] 2026-11-03: the entry box is 125 GB at GBP 4.00/month plus an 8% PayPal fee | capture: sha256:e2218db0fdfd03e5e3308471ccb299970257db7d6eeaccd72726f0bbfadbe1d9 | quote: MeggaBox 125GB £4.00 / Month +8% paypal Transaction fee
  - [1] 2026-11-03: unlimited transfer on a 1 GB port, FTP over TLS, public trackers at a 2:1 ratio | capture: sha256:e2218db0fdfd03e5e3308471ccb299970257db7d6eeaccd72726f0bbfadbe1d9 | quote: Unlimited Downloads / Uploads, User Dashboard FTP over TLS (faster) 1 GB Port connection Public trackers Allowed 2:1 ratio on Public Trackers
  - [1] 2026-11-03: payment is completed on PayPal | capture: sha256:e2218db0fdfd03e5e3308471ccb299970257db7d6eeaccd72726f0bbfadbe1d9 | quote: You will be redirected to paypal to complete your order
  - [2] 2026-11-03: crypto and PayPal guest checkout are accepted | capture: sha256:94e5af65784495af0ad7ee7c030768e0364d5ac58accb46b2953148dc6febc49 | quote: PAYMENT OPTIONS INCLUDE CRYPTO AND PAYPAL GUEST CHECKOUTS
- sources:
  - [1] https://meggafast.com/order/
  - [2] https://meggafast.com/
