# fshy

> A catalogue of free, nearly free and cheapest-paid cloud capacity: storage, compute and GPU time, model inference, egress and tunnels, proxies, crawling, debrid, netdisks, databases, email, DNS and domains, CI runners, developer services, data APIs and coding subscriptions. 4,866 records from 3,445 providers. Each record states its quota, the limit that runs out first, the identity a signup costs (email, phone, card, ID), its evidence and how fresh that evidence is. For research and education only. It is not legal advice, and it makes no statement about whether a use is permitted.

Every file here is generated from the published records and nothing else. Data as of 2026-11-10, the date of the published data. Version `e7cf1b4a40af`: the first 12 hex digits of the SHA-256 of every record's Markdown, topic by topic in the one order (hosted before self-hosted, then verdict, provider name, record id); it changes whenever a record does.

Start with a topic's index: one line per record with its verdict, free tier, identity, card, phone, evidence, stale date, parsed price and summary. Each line links the provider's page in Markdown, `https://fshy.ajam.dev/p/<id>.md`, which holds every record of that provider in full. Every wiki page that has a Markdown version names it in `<link rel="alternate" type="text/markdown">`. Before quoting a value, read how to read a record in https://fshy.ajam.dev/llms-full.txt.

Four rules hold in these files and in the API alike. Card, phone and ID requirements are yes, no or unknown (1, 0 or NULL), and unknown never means no. A record goes stale on its `stale on` date (`stale_on`); compare it with today. A price that did not parse is unknown (NULL), not free. A self-hosted record (`self_hosted`, labelled `self-hosted, last resort`) is software or a node that the user installs, runs and maintains, and every list puts it after every hosted record. Self-hosted options are listed last, because this site is for users who have no hardware.

To report an error in a record or an offer that is missing, open an issue with the Correction form or the New offer form: https://github.com/f-shy/fshy.ajam.dev/issues/new/choose. A report is checked against the provider's own pages before a record changes. The code and the records are under the 0BSD licence, https://github.com/f-shy/fshy.ajam.dev/blob/main/LICENSE; a quote from a provider's page stays with its owner.

## Topics

- [Storage](https://fshy.ajam.dev/t/storage.md): Where bytes can live: object storage, drives, registries, academic repositories, hosts used as storage. 1,720 records: 371 usable, 33 trial, 103 paid only, 1,035 rejected, 108 dead; 70 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/storage/rejected.md; in full: https://fshy.ajam.dev/t/storage/llms-full.txt
- [Compute](https://fshy.ajam.dev/t/compute.md): Machines, sandboxes, notebooks, GPU time, platform hosts and how long each runs before it is reaped. 1,411 records: 482 usable, 133 trial, 509 paid only, 173 rejected, 80 dead; 34 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/compute/rejected.md; in full: https://fshy.ajam.dev/t/compute/llms-full.txt
- [Inference](https://fshy.ajam.dev/t/inference.md): Model APIs that answer a completion request, keyless or behind a free key. 108 records: 40 usable, 26 trial, 20 paid only, 10 rejected, 12 dead. Rejected and dead: https://fshy.ajam.dev/t/inference/rejected.md; in full: https://fshy.ajam.dev/t/inference/llms-full.txt
- [Egress and tunnels](https://fshy.ajam.dev/t/egress.md): Ways to get traffic out or a service in: tunnels, relays, IPv6 brokers, UDP forwards. 457 records: 56 usable, 23 trial, 125 paid only, 129 rejected, 21 dead; 103 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/egress/rejected.md; in full: https://fshy.ajam.dev/t/egress/llms-full.txt
- [IP and proxies](https://fshy.ajam.dev/t/ip-proxy.md): Exit addresses: proxy lists, VPN exits, address sources and what the upstream sees. 87 records: 23 usable, 6 trial, 43 paid only, 9 rejected, 6 dead. Rejected and dead: https://fshy.ajam.dev/t/ip-proxy/rejected.md; in full: https://fshy.ajam.dev/t/ip-proxy/llms-full.txt
- [Crawling](https://fshy.ajam.dev/t/crawler-scraper.md): Crawl, search, reader and unblocker APIs for reading the web at scale. 59 records: 38 usable, 9 trial, 1 paid only, 3 rejected, 8 dead. Rejected and dead: https://fshy.ajam.dev/t/crawler-scraper/rejected.md; in full: https://fshy.ajam.dev/t/crawler-scraper/llms-full.txt
- [Debrid](https://fshy.ajam.dev/t/debrid.md): A debrid service downloads files from many file hosts through one account, at full speed. Also premium-link generators, usenet and retrieval services. 526 records: 299 usable, 17 trial, 90 paid only, 50 rejected, 52 dead; 18 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/debrid/rejected.md; in full: https://fshy.ajam.dev/t/debrid/llms-full.txt
- [Netdisk and pan](https://fshy.ajam.dev/t/netdisk-pan.md): Netdisks, also called pan drives: cloud drives, many of them from China, and public AList and OpenList instances, and whether they mount. 104 records: 52 usable, 2 trial, 2 paid only, 32 rejected, 14 dead; 2 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/netdisk-pan/rejected.md; in full: https://fshy.ajam.dev/t/netdisk-pan/llms-full.txt
- [Databases and KV](https://fshy.ajam.dev/t/databases-kv.md): Hosted databases, vector stores and key-value stores. 23 records: 18 usable, 2 trial, 0 paid only, 0 rejected, 3 dead. Rejected and dead: https://fshy.ajam.dev/t/databases-kv/rejected.md; in full: https://fshy.ajam.dev/t/databases-kv/llms-full.txt
- [Email](https://fshy.ajam.dev/t/email.md): Sending, receiving, forwarding and inbox APIs. 38 records: 24 usable, 2 trial, 8 paid only, 3 rejected, 0 dead; 1 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/email/rejected.md; in full: https://fshy.ajam.dev/t/email/llms-full.txt
- [Domains and DNS](https://fshy.ajam.dev/t/domains-dns.md): Managed DNS, free domains and certificate authorities. 33 records: 26 usable, 0 trial, 5 paid only, 1 rejected, 1 dead. Rejected and dead: https://fshy.ajam.dev/t/domains-dns/rejected.md; in full: https://fshy.ajam.dev/t/domains-dns/llms-full.txt
- [CI runners](https://fshy.ajam.dev/t/ci-cd-runners.md): Hosted CI runners and registries, and what they will run. 34 records: 20 usable, 2 trial, 5 paid only, 1 rejected, 3 dead; 3 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/ci-cd-runners/rejected.md; in full: https://fshy.ajam.dev/t/ci-cd-runners/llms-full.txt
- [Developer services](https://fshy.ajam.dev/t/dev-services.md): Monitoring, error tracking, analytics, scheduled jobs, queues, realtime and authentication services. 61 records: 51 usable, 4 trial, 0 paid only, 2 rejected, 0 dead; 4 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/dev-services/rejected.md; in full: https://fshy.ajam.dev/t/dev-services/llms-full.txt
- [Data APIs](https://fshy.ajam.dev/t/data-apis.md): Data APIs with free calls, and their bulk downloads: maps, IP location, markets, weather, news and open data. 155 records: 126 usable, 3 trial, 5 paid only, 12 rejected, 8 dead; 1 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/data-apis/rejected.md; in full: https://fshy.ajam.dev/t/data-apis/llms-full.txt
- [Coding subscriptions](https://fshy.ajam.dev/t/coding-subs.md): Coding-agent subscriptions and their price per unit of work. 50 records: 20 usable, 1 trial, 19 paid only, 2 rejected, 2 dead; 6 self-hosted of any group, listed last. Rejected and dead: https://fshy.ajam.dev/t/coding-subs/rejected.md; in full: https://fshy.ajam.dev/t/coding-subs/llms-full.txt

## Best per need

- [Free S3-compatible storage, no card](https://fshy.ajam.dev/need/s3-storage-no-card.md): Usable storage offers with a stated free allowance, in the storage topic or in egress, with an S3 interface whose identity requirement was read and does not include a card. A paid plan with no free allowance is not listed. Sorted by USD per TB-month where a price parsed.
- [Bulk storage by price per TB-month](https://fshy.ajam.dev/need/storage-by-price.md): Storage offers with a parsed price per TB-month, usable or paid-only, cheapest first. Prices in other currencies are converted only with a dated exchange rate that a record cites.
- [Free storage with no card](https://fshy.ajam.dev/need/free-storage-no-card.md): Usable storage with a stated free allowance, in the storage topic or in egress with an S3 interface, with a stated identity requirement that is not a card, best verdict and strongest evidence first. A paid plan with no free allowance is not listed.
- [Free or trial GPU time](https://fshy.ajam.dev/need/free-gpu.md): Compute offers that mention GPU in their category or text and are usable or trial. Read the free tier line for hours per week or month.
- [Free compute with no card](https://fshy.ajam.dev/need/compute-no-card.md): Usable compute offers whose stated identity requirement is not a card.
- [Cheapest rented machines by USD a month](https://fshy.ajam.dev/need/cheapest-machines.md): Compute offers with a parsed monthly USD price, cheapest first. A rented machine is a service; nothing here is hardware to buy.
- [Inference APIs with no card and no phone](https://fshy.ajam.dev/need/inference-no-card-no-phone.md): Usable model-inference endpoints, in the inference topic or categorised as inference elsewhere, whose stated identity needs neither a card nor a phone.
- [Usable with no account at all](https://fshy.ajam.dev/need/anonymous.md): Usable offers in any topic whose identity requirement is anonymous.
- [Offers that name a crypto payment rail](https://fshy.ajam.dev/need/accepts-crypto.md): Records whose payment or identity text names a cryptocurrency. Not a verdict on the offer.
- [Debrid and retrieval services by monthly price](https://fshy.ajam.dev/need/debrid-cheapest.md): Debrid offers with a parsed monthly USD price, cheapest first, then the offers with no parsed price. An offer priced per TB and not per month is ranked in debrid-by-tb, because a price per TB and a price per month are not one unit.
- [Debrid and retrieval services priced per TB](https://fshy.ajam.dev/need/debrid-by-tb.md): Debrid offers priced per TB-month and not per month, cheapest first. The offers with a monthly price are ranked in debrid-cheapest.
- [Free tunnels and egress paths](https://fshy.ajam.dev/need/egress-tunnels.md): Usable ways to get traffic in or out: tunnels, relays, IPv6 brokers, VPN egress.
- [Free email sending and receiving](https://fshy.ajam.dev/need/email.md): Usable transactional senders, mailboxes, forwarding and inbox APIs.
- [Free databases and key-value stores](https://fshy.ajam.dev/need/databases.md): Usable hosted databases, vector stores and key-value stores.
- [Free CI runners](https://fshy.ajam.dev/need/ci-runners.md): Usable hosted CI runners and registries, and hosted build services whose free allowance is counted in build minutes.
- [Free DNS, domains and certificates](https://fshy.ajam.dev/need/dns-domains.md): Usable managed DNS, free domains and certificate authorities.
- [Coding subscriptions by price](https://fshy.ajam.dev/need/coding-subscriptions.md): Coding-agent subscriptions with a parsed monthly price, cheapest first, then the rest.
- [Mountable pan drives and public instances](https://fshy.ajam.dev/need/pan-drives.md): Usable netdisk and pan-drive offers, including public AList and OpenList instances.
- [Free crawling, search and reader APIs](https://fshy.ajam.dev/need/crawling.md): Usable crawl, search, reader and unblocker APIs.
- [Free proxies and exit addresses](https://fshy.ajam.dev/need/proxies.md): Usable proxy lists, VPN exits and address sources.

## Query it

- [MCP endpoint](https://fshy.ajam.dev/about/#api): POST JSON-RPC 2.0 to `https://fshy.ajam.dev/mcp` (Streamable HTTP; a GET there answers 405), stateless and read-only; tools help, search, filter, get, entity, need, sql, worklist. Connect: `claude mcp add --transport http fshy https://fshy.ajam.dev/mcp`
- [help.txt](https://fshy.ajam.dev/api/v1/help.txt): the query primer: tables, columns, vocabularies and worked SQL; read it first
- [search](https://fshy.ajam.dev/api/v1/search?q=gpu+hours&topic=compute): full-text search; `q` words, optional `topic`
- [records](https://fshy.ajam.dev/api/v1/records?topic=storage&no_card=1&sort=usd_per_tb_month): filter and sort record cards; `free=1` keeps the records with a free allowance
- [sql](https://fshy.ajam.dev/api/v1/sql?q=SELECT+rid,verdict+FROM+record+LIMIT+5): read-only SQLite over the store
- [record](https://fshy.ajam.dev/api/v1/record/compute/oracle-cloud): one record as JSON, `/api/v1/record/<topic>/<slug>`
- [entity](https://fshy.ajam.dev/api/v1/entity/oracle.json): one provider and all its records as JSON, `/api/v1/entity/<id>.json`
- [schema.sql](https://fshy.ajam.dev/api/v1/schema.sql): the store's schema; [vocab.json](https://fshy.ajam.dev/api/v1/vocab.json): its vocabularies
- [fshy-public.sqlite.gz](https://fshy.ajam.dev/data/fshy-public.sqlite.gz): the whole store as one SQLite file, gzip. data/manifest.json gives public_db.gzip_sha256, the SHA-256 of this download, and public_db.sha256, the SHA-256 of the SQLite file after gunzip

## Optional

- [llms-full.txt](https://fshy.ajam.dev/llms-full.txt): how to read a record, and the index of the parts that hold every record in full (21,438 KB, about 5,794K tokens in all, split by topic and verdict group)
- [Graveyard](https://fshy.ajam.dev/graveyard/): offers that no longer exist, with the evidence of their end
- [Changes](https://fshy.ajam.dev/changes/): corrections to earlier claims, newest first
