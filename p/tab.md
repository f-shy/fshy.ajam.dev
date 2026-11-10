# TAB.DIGITAL Nextcloud One

> tab.digital | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tab/ | JSON https://fshy.ajam.dev/api/v1/entity/tab.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TAB.DIGITAL Nextcloud One (cloud.tab.digital)

- `netdisk-pan/tab-digital-nextcloud` | fails-quota | evidence reported | binding write-gated | category managed Nextcloud, freemium
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:59.762Z (inherited) | stale on 2026-11-19
- url https://tab.digital/en/nextcloud-one
- free tier: 8 GB free for one user, with no payment method required. Paid: 128 GB at EUR 7.44/month, up to 1 TB on the personal ladder; business plans from EUR 61/month with 1 TB to 100 TB | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published for the free 8 GB plan | source: [2]
- retention: Until deleted. No retention clock published | source: [2]
- egress: 'Share transfer unlimited' on the free tier; traffic is not metered on the paid plans | metered: no | free allowance: unlimited on share transfer | source: [2]
- identity: email | detail: an email address and no payment method, per 'Take a free account. No payment method required, just try it'
- interface: webdav, rest, rclone
- limits:
  - write-gated (binding): the free plan is one user and 8 GB, and Talk with end-to-end encryption are paid-plan features [2]
- binding note: 8 GB free is 1.6% of a 500 GB threshold, so the quota closes it first in practice. The gate worth naming is that the free tier is a single user with no quota controls, so it cannot even be sharded internally.
- tooling: rclone webdav and the Nextcloud clients. Nextcloud Hub with Talk and Collabora on the paid plans
- composes with: 8 GB needs no payment method at all, which makes it the cheapest way to obtain an EU Nextcloud shard with zero identity cost beyond an email address. It cannot reach 500 GB without 60-plus accounts, and the provider manages users centrally on paid plans, so the shard path is per-account only
- reliability: Hosted in Milan and the Netherlands. The free 8 GB plan was explicitly confirmed to remain active following the July 2026 pricing revision: 'Q: Is the free 8 GB account going away? A: No.'
- notes: Maintains an active 8 GB free tier without requiring a credit card, surviving the July 2026 pricing update. Functions as a functional Nextcloud WebDAV testing endpoint rather than bulk storage.
- evidence note: The specific claim that would be worth re-checking live is that the free tier survived the July 2026 repricing.
- extras:
  - access_mode: registration-gated
  - free_tier_exists: yes
  - free_tier_survives_repricing: yes
  - region: Milan, Italy and the Netherlands
  - no_payment_method_required: yes
- evidence:
  - [1] 2026-10-21: 'Free 8GB', 'Subscribe 128GB (7,44 EUR per/month)', storage range '128 - 1024 GB'
  - [2] 2026-10-21: 'Nextcloud One, 1 person, EUR 7,44 per month'; 'Business per 50 users from EUR 61 per month'; storage 'up to 100TB'; 'Take a free account. No payment method required, just try it'
  - [3] 2026-10-21: 'Q: Is the free 8 GB account going away? A: No. The free 8 GB plan remains available.' beside a 2026-07-01 price-change notice
  - [1] 2026-11-03: the page lists a free 8 GB plan next to a 128 GB plan at 7,44 EUR per month | capture: sha256:a0815a4b586c829ec8e906dbf33cb188c1054375654d7df97de49106f5776540 | quote: Free 8GB [Subscribe 128GB (7,44 EUR per/month)]
  - [1] 2026-11-03: the plan table lists Share transfer unlimited | capture: sha256:a0815a4b586c829ec8e906dbf33cb188c1054375654d7df97de49106f5776540 | quote: Share transfer unlimited
  - [2] 2026-11-03: the Business plan starts from 61 EUR per month per 50 users | capture: sha256:663ee99fcab45d717f8585644e289f35e5d2cd1b3504c8fad78a4477a53659bb | quote: from €61
  - [2] 2026-11-03: a free 8 GB account is still offered with no payment method | capture: sha256:663ee99fcab45d717f8585644e289f35e5d2cd1b3504c8fad78a4477a53659bb | quote: It`s a good way to find out if Nextcloud fits your need is to take a free account. No payment method required, just try it.
- sources:
  - [1] https://tab.digital/en/nextcloud-one
  - [2] https://cloud.tab.digital/pricing
  - [3] https://tab.digital/en/keep-today-pricing
