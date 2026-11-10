# seeweb cloud object storage

> seeweb.it | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seeweb/ | JSON https://fshy.ajam.dev/api/v1/entity/seeweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## seeweb cloud object storage

- `storage/seeweb-cloud-object-storage` | paid-only | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:18.961Z (live) | stale on 2026-12-04
- url https://www.seeweb.it/en/products/cloud-object-storage
- free tier: No free allowance. EUR 27.00 per month for 1000 GB of space with 1000 GB of outbound traffic included (inbound traffic is free); extra space EUR 27.00 per 1000 GB and extra outbound traffic EUR 11.50 per 1000 GB. 10 TiB bills as 11 x 1000 GB = EUR 297.00 per month and 20 TiB as 22 x 1000 GB = EUR 594.00 per month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: 1000 GB of outbound traffic is included each month with the base package; inbound traffic is always free; extra outbound traffic is EUR 11.50 per 1000 GB. | metered: yes
- identity: email | detail: unverified: the order flow was not entered; the documentation says credentials arrive by e-mail after the order is completed, and the payment method and any business identity asked at checkout are not known
- interface: s3
- limits:
  - volume-quota: billed in whole 1000 GB volumes, minimum 1000 GB, EUR 27.00 per volume per month; includes 1000 GB outbound traffic and 100.000 read and write accesses [1]
- limits note: No hard cap: capacity is billed per whole 1000 GB volume of the maximum space used in the month, and the base package includes 1000 GB outbound traffic and 100.000 read and write accesses.
- binding note: no free allowance and no hard cap; the cost scales linearly at EUR 27.00 per 1000 GB per month, so the price binds
- interface detail: S3 API at https://s3.it-north-1.s3seeweb.it with an IAM-style API at https://iam.it-north-1.s3seeweb.it
- tooling: aws-cli version 2 is the recommended tool; any S3 client (Cyberduck, CloudBerry Explorer) and S3 plugins of CMSs work; credentials arrive by e-mail after the order.
- composes with: any S3-compatible client can write to it; capacity is bought in 1000 GB volumes at EUR 27.00 per volume per month
- reliability: Priced offer with a 99.90% guaranteed uptime (with penalty); the S3 endpoint is in the it-north-1 region. 10 TiB costs about EUR 297.00 per month.
- notes: the same as reliability
- evidence note: The 2026-11-03 evidence rows read https://www.seeweb.it/en/products/cloud-object-storage (27.00 EUR per month for up to 1 TB and 1 TB outbound, 27.00 EUR and 11.50 EUR per extra 1000 GB, 100.000 accesses, 99.90% uptime) and https://docs.seeweb.it/en/storage/cos/ (per-TB rounding, minimum 1 TB, S3 endpoint, credentials by e-mail). The price and egress fields that decide the paid-only verdict cite vendor captures; checkout identity is unverified.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: EUR 27.00/TB/month for the base 1 TB with 1 TB outbound included, and extra traffic is EUR 11.50/TB — 6.8x Datalix for the same bytes. Italian enterprise positioning, not a price competitor.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: EUR 27.00/TB/month for the base 1 TB with 1 TB outbound included, and extra traffic is EUR 11.50/TB — 6.8x Datalix for the same bytes. Italian enterprise positioning, not a price competitor.
  - [2] 2026-10-21: cited as the basis of the rejection: EUR 27.00/TB/month for the base 1 TB with 1 TB outbound included, and extra traffic is EUR 11.50/TB — 6.8x Datalix for the same bytes. Italian enterprise positioning, not a price competitor.
  - [1] 2026-11-03: the base package costs 27.00 € a month and no free allowance is listed | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: Monthly cost *?* Up to 1 TB of occupied space and 1 TB of outbound traffic | 27.00 €
  - [1] 2026-11-03: the monthly cost is 27.00 € for up to 1 TB of space and 1 TB of outbound traffic | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: Monthly cost *?* Up to 1 TB of occupied space and 1 TB of outbound traffic | 27.00 €
  - [1] 2026-11-03: extra space costs 27.00 € every 1000 GB | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: Extra space *?* Metered storage space in 1 TB volumes | 27.00 € every 1000 GB not splittable
  - [1] 2026-11-03: extra outbound traffic costs 11.50 € every 1000 GB | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: Extra traffic *?* Metered traffic in 1 TB volumes | 11.50 € every 1000 GB not splittable
  - [2] 2026-11-03: billing is per whole TB of the maximum space used in the month, minimum 1 TB | capture: sha256:ee853b8a555aee1085acf3669e3c0d8dd66beeacbeb791a014a8653411b6d787 | quote: La tariffazione è per TByte arrotondato per eccesso, il minimo è 1 TByte.
  - [1] 2026-11-03: 1000 GB of outbound traffic is included and inbound traffic is free | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: 1000 GB of outbound traffic (inbound traffic is always free);
  - [1] 2026-11-03: outbound traffic beyond the included 1000 GB is metered at 11.50 € per 1000 GB | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: Extra traffic *?* Metered traffic in 1 TB volumes | 11.50 € every 1000 GB not splittable
  - [2] 2026-11-03: the service exposes an S3 endpoint | capture: sha256:ee853b8a555aee1085acf3669e3c0d8dd66beeacbeb791a014a8653411b6d787 | quote: endpoint_url = https://s3.it-north-1.s3seeweb.it
  - [2] 2026-11-03: the documented S3 endpoint is s3.it-north-1.s3seeweb.it | capture: sha256:ee853b8a555aee1085acf3669e3c0d8dd66beeacbeb791a014a8653411b6d787 | quote: endpoint_url = https://s3.it-north-1.s3seeweb.it
  - [2] 2026-11-03: the documentation recommends aws-cli version 2 | capture: sha256:ee853b8a555aee1085acf3669e3c0d8dd66beeacbeb791a014a8653411b6d787 | quote: Per la gestione via CLI è altamente consigliato l'utilizzo dello strumento ufficiale di Amazon AWS: la versione 2 di aws-cli.
  - [1] 2026-11-03: the base package includes 100.000 read and write accesses | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: 100.000 read and write accesses.
  - [1] 2026-11-03: the uptime guarantee is 99.90% with penalty | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: Guaranteed UpTime (with penalty) | 99.90%
  - [2] 2026-11-03: credentials arrive by e-mail after the order | capture: sha256:ee853b8a555aee1085acf3669e3c0d8dd66beeacbeb791a014a8653411b6d787 | quote: Una volta completato l'ordine, viene ricevuta una e-mail contenente le credenziali d'accesso
  - [1] 2026-11-03: the base package is still 27.00 € a month | capture: sha256:fed14430c575f7086b91cea77f1807df16e33cdd8cce6872b9ffbc9e11ef2c00 | quote: Monthly cost *?* Up to 1 TB of occupied space and 1 TB of outbound traffic | 27.00 €
- sources:
  - [1] https://www.seeweb.it/en/products/cloud-object-storage
  - [2] https://docs.seeweb.it/en/storage/cos/
