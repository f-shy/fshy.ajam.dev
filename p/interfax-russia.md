# QIWI Wallet

> interfax-russia.ru | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/interfax-russia/ | JSON https://fshy.ajam.dev/api/v1/entity/interfax-russia.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## QIWI Wallet

- `debrid/qiwi-wallet` | dead | evidence documented | binding write-gated | category Russian e-wallet (payment rail used by CIS file hosts and resellers) | tier wallet
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:24:30.824Z (live) | stale on 2026-11-23
- url https://www.interfax-russia.ru/view/kivi-bank-lishilsya-licenzii-qiwi-koshelek-perevody-cherez-contact-ne-dostupny
- free tier: not applicable: a payment rail, not a retrieval service | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1] | note: unstated
- retention: not applicable | source: [1] | note: unstated
- egress: not applicable | metered: no | source: [1]
- identity: card | detail: A Russian wallet, funded by Russian rails; after the licence revocation the funding path itself is closed. | country: Russia
- interface: unknown
- limits:
  - write-gated (binding): wallet top-up and withdrawal stopped on 2024-02-21 when the Central Bank revoked the licence of QIWI Bank [1]
- limits note: The wallet brand later moved to a new domain (qiwiwall) per RIA, but a moved brand is not a working top-up rail for a foreign buyer.
- binding note: No quota applies: the rail is closed. Any service that lists QIWI today is listing a payment method a buyer cannot fund.
- interface detail: Was a wallet app and a merchant payment form; as of 2024-02-21 top-ups and withdrawals stopped after the banking licence was revoked.
- tooling: None usable for a new payment.
- composes with: Several CIS services among debrid providers still list 'QIWI' among their payment methods (Megaseed.kz lists QIWI KZT and QIWI RUB; Turbobit's reseller directory lists Qiwi). Those listings are stale: the rail stopped working in Russia on 2024-02-21.
- reliability: Funds in QIWI wallets were not covered by deposit insurance and claims go into the third creditor queue, per the DIA procedure reported in 2024.
- notes: A dead rail, recorded because a reader will otherwise treat 'QIWI accepted' on a provider page as a working payment option. The rule this establishes: a payment method listed by a CIS service is a claim about the past, and must be checked against the rail's own status. QIWI KZT may still work in Kazakhstan; nothing was found either way, so the record does not claim it.
- evidence note: The licence revocation and the stopped top-up/withdrawal are quoted from Interfax-Russia's report of 2024-02-21, read. The later domain move is a RIA headline seen in search, not read in full. Evidence dates normalised to the read date on 2026-10-23; a source that carries its own date keeps it in the proved field.
- evidence:
  - [1] 2026-10-23: 'Клиенты кредитного учреждения не могут пополнить кошельки и вывести с них средства' after the Central Bank revoked the QIWI Bank licence on 2024-02-21
  - [2] 2026-10-23: a live CIS service still lists 'QIWI KZT' and 'QIWI RUB' among its payment anchors - the stale-listing case this record exists to flag
- sources:
  - [1] https://www.interfax-russia.ru/view/kivi-bank-lishilsya-licenzii-qiwi-koshelek-perevody-cherez-contact-ne-dostupny
  - [2] https://megaseed.kz/
