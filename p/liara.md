# Liara

> liara.ir | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/liara/ | JSON https://fshy.ajam.dev/api/v1/entity/liara.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Liara

- `compute/liara` | trial-only | evidence documented | binding retention-clamped | category platform host
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T06:20:49.285Z (live) | stale on 2026-12-05
- url https://liara.ir/blog/nowruz-98/
- free tier: 'هزینه اعتبار اولیه لیارا برای افتتاح حساب، ۵۰۰ هزارتومان شد. شما می‌توانید تنها با ثبت‌نام در لیارا، این اعتبار هدیه را دریافت کنید' (the initial credit for opening a Liara account is now IRR-equivalent 500,000 toman, and you receive this gift credit just by registering). The vendor's own channel announced the same rise from 200,000 to 500,000 toman, and the platform also sells 'هاست ابری رایگان' (free cloud hosting) on a resource-limited plan. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: signup-credit
- per-object cap: not applicable | source: [1]
- retention: One charge, then a hard stop: the 500,000 toman is a single signup gift with no renewal, and Liara charges 200,000 toman a month for an IPv4 address alone, so the credit buys about one month of a small server plus one address and then the account needs an Iranian payment route. | source: [1]
- egress: VPS plan: 2,500 toman per GB of download traffic, upload traffic free; no included download allowance is stated on the page. The egress terms of the free cloud host plan are not published on the page read. | metered: yes | source: [1]
- identity: email | detail: an email address or an Iranian mobile number, with email sufficient: the login screen reads 'enter your email or mobile number to sign in or register; sign in with email'. Registering alone grants the 500,000 toman credit. No card is needed to register and no hold is stated. The record's notes state that paying beyond the credit needs an Iranian card or gateway, which the pricing pages do not enumerate, so debit and prepaid acceptance are not stated.
- interface: cli, rest
- limits:
  - retention-clamped (binding): One charge, then a hard stop: the 500,000 toman is a single signup gift with no renewal, and Liara charges 200,000 toman a month for an IPv4 address alone, so the credit buys about one month of a small server plus one address and then the account needs an Iranian payment route. [1]
- limits note: One charge, then a hard stop: the 500,000 toman is a single signup gift with no renewal, and Liara charges 200,000 toman a month for an IPv4 address alone, so the credit buys about one month of a small server plus one address and then the account needs an Iranian payment route.
- binding note: the same as limits note
- interface detail: Liara API and Liara CLI, per the docs.liara.ir documentation index, which lists "Liara API"
- tooling: the provider documents its own CLI, "Liara CLI", on docs.liara.ir
- composes with: The signup credit plus a free-hosting plan is the composition that works: the free plan holds a small app with no clock, and the 500,000 toman buys a real server for the month when the app needs CPU, with the caveat that the IPv4 line item eats 40 percent of the credit before any compute is bought.
- reliability: no reliability event recorded
- notes: The one Iranian provider found where the door is an email address rather than an Iranian mobile number, which makes it the exception in a market where national identity is usually the first gate. Two limits notable: the credit is denominated in a currency that loses value, so the USD equivalent moves with the rial and is not stated here as a number; and paying beyond the credit needs an Iranian card or gateway, which the pricing pages do not enumerate. The PaaS lane is more useful than the VPS lane because it does not need an IPv4 surcharge. The one recorded is the better-evidenced.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: signup-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: an update on Liara's own blog: ' . ', quoted
  - [2] 2026-10-22: the vendor's official Telegram channel: ' ' (the free initial credit rose to 500,000 toman) and an earlier post raising it to 200,000, quoted
  - [3] 2026-10-22: the login screen reads ' : ' (enter your email or mobile number to sign in or register; sign in with email), quoted, so email is an accepted identity
  - [4] 2026-10-22: pricing terms: ' . ... IPv4 ' (2,500 toman per GB downloaded, upload free, and 200,000 toman a month added for an IPv4 address), quoted
  - [5] 2026-10-22: ' ' (to get free hosting, register and choose a free plan) and ' ' (the free host has resource limits), quoted
  - [5] 2026-10-22: page states that free hosting and free databases are not provided while international connectivity is limited, translated from Persian, while the marketing copy below still offers a free plan
  - [6] 2026-10-22: 
  - [7] 2026-11-04: the Liara documentation index lists a Liara API reference | capture: sha256:028fbca36008d02a0e9f4303285b16e959172c54b6018364c795733b76946bc2 | quote: #### Liara API
  - [7] 2026-11-04: the Liara documentation index lists a Liara CLI reference | capture: sha256:028fbca36008d02a0e9f4303285b16e959172c54b6018364c795733b76946bc2 | quote: #### Liara CLI
  - [4] 2026-11-04: VPS pricing page: 2,500 toman per GB of download traffic, upload free | capture: sha256:824a6767c0079f59d03754e98390b91fc01a300ad1a299fb86312002f85ceada | quote: هزینه‌ی مصرف هر گیگابایت ترافیک دانلود، ۲۵۰۰ تومان و ترافیک آپلود رایگان است.
  - [7] 2026-11-04: the documentation index lists a Liara API reference | capture: sha256:028fbca36008d02a0e9f4303285b16e959172c54b6018364c795733b76946bc2 | quote: #### Liara API
  - [7] 2026-11-04: the documentation index lists a Liara CLI reference | capture: sha256:028fbca36008d02a0e9f4303285b16e959172c54b6018364c795733b76946bc2 | quote: #### Liara CLI
- sources:
  - [1] https://liara.ir/blog/nowruz-98/
  - [2] https://t.me/s/liara_cloud?before=267
  - [3] https://console.liara.ir/
  - [4] https://liara.ir/products/iranian-vps/
  - [5] https://liara.ir/products/free-cloud-host/
  - [6] https://t.me/s/liara_cloud?before=123
  - [7] https://docs.liara.ir/
