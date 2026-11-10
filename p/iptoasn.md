# IPtoASN

> iptoasn.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iptoasn/ | JSON https://fshy.ajam.dev/api/v1/entity/iptoasn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPtoASN

- `data-apis/iptoasn` | qualifies | evidence measured | binding none | category IP to ASN and country database download | tier Free database download
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://iptoasn.com/
- free tier: free IP to ASN and IP to country database files, updated hourly: IPv4, IPv6 and combined TSV files in gzip, no account; the hosted API was phased out on December 31, 2020 | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: the IPv4 to ASN file ip2asn-v4.tsv.gz was 8,697,031 bytes with HTTP 200 when probed.
- per-object cap: ip2asn-v4.tsv.gz is 8,697,031 bytes | bytes: 8697031 | source: [2]
- retention: each file is the current snapshot; the page says it is updated hourly | source: [1]
- egress: not applicable: static files served through Cloudflare with no published meter | metered: no | source: [1]
- identity: anonymous | detail: no account; plain HTTPS downloads
- interface: unknown
- binding note: static files with no published download limit.
- interface detail: plain HTTPS download of gzip-compressed TSV files from https://iptoasn.com/data/ (ip2asn-v4, ip2asn-v4-u32, ip2country-v4, ip2country-v4-u32, ip2asn-v6, ip2country-v6 and ip2asn-combined) with the columns range_start, range_end, AS_number, country_code, AS_description; the interface vocabulary has no term for a file download (https-download)
- endpoint: https://iptoasn.com/data/ip2asn-v4.tsv.gz
- tooling: curl or wget and gunzip, any TSV reader or SQL loader; the author's iptoasn-webservice source turns the files into a lookup API, which the user installs and runs on a rented or free machine and which is the last resort after the downloads
- composes with: The one free ASN and country mapping with no account and no per-request limit, usable as a local join table in a pipeline. Bulk path: the files themselves, IPv4 to ASN 8,697,031 bytes gzipped.
- reliability: the hosted API was phased out on 2020-12-31 due to increasing traffic; ip2asn-v4.tsv.gz had Last-Modified Sun, 01 Nov 2026 09:38:42 GMT in an answer dated Mon, 02 Nov 2026 10:42:50 GMT, while the page says the data is updated hourly
- notes: Free requests: unmetered (static files). Rate limit: none published. The data v1.0. Bulk path: the TSV files, IPv4, IPv6 and combined. Last resort: run the author's API server over the files.
- evidence note: The IPv4 to ASN file was downloaded in full on 2026-11-02 (HTTP 200, 8,697,031 bytes) and the page was quoted; the other files were not downloaded and the hourly update claim was observed once, not tracked.
- extras:
  - bulk_path: the gzip TSV files (IPv4, IPv6, combined)
  - free_requests: unmetered downloads
- evidence:
  - [1] 2026-11-02: a free IP to ASN and country database, updated hourly | capture: sha256:5f78aa8d3fefb10a7d7416e360d1795969add4386e47ddb6a6e5839f30a0e93c | quote: Free IP to ASN & Country mapping database. Updated hourly.
  - [1] 2026-11-02: the hosted API was phased out on 2020-12-31 | capture: sha256:5f78aa8d3fefb10a7d7416e360d1795969add4386e47ddb6a6e5839f30a0e93c | quote: The public API was phased out on December 31, 2020 due to increasing traffic.
  - [1] 2026-11-02: the databases stay downloadable and an own API server is the stated route | capture: sha256:5f78aa8d3fefb10a7d7416e360d1795969add4386e47ddb6a6e5839f30a0e93c | quote: You can still download the databases above and [run your own API server](https://github.com/jedisct1/iptoasn-webservice) for production use.
  - [1] 2026-11-02: the data is under the Public Domain Dedication and License v1.0 | capture: sha256:5f78aa8d3fefb10a7d7416e360d1795969add4386e47ddb6a6e5839f30a0e93c
  - [1] 2026-11-02: the IP to ASN file columns | capture: sha256:5f78aa8d3fefb10a7d7416e360d1795969add4386e47ddb6a6e5839f30a0e93c | quote: `range_start range_end AS_number country_code AS_description`
  - [1] 2026-11-02: a combined IPv4 and IPv6 file is offered | capture: sha256:5f78aa8d3fefb10a7d7416e360d1795969add4386e47ddb6a6e5839f30a0e93c | quote: * [Download ip2asn-combined.tsv.gz](https://iptoasn.com/data/ip2asn-combined.tsv.gz)
  - probe:https://iptoasn.com/data/ip2asn-v4.tsv.gz 2026-11-02: the IPv4 to ASN file answered HTTP 200 | capture: sha256:bcfb577227d09b49fcc33790d22d90757d5c0b6d663432c84defdf10faa8003a | quote: "status": 200,
  - probe:https://iptoasn.com/data/ip2asn-v4.tsv.gz 2026-11-02: the IPv4 to ASN file is 8,697,031 bytes | capture: sha256:bcfb577227d09b49fcc33790d22d90757d5c0b6d663432c84defdf10faa8003a | quote: "bytes": 8697031,
  - probe:https://iptoasn.com/data/ip2asn-v4.tsv.gz 2026-11-02: the file carried a Last-Modified of 2026-11-01 09:38:42 GMT | capture: sha256:bcfb577227d09b49fcc33790d22d90757d5c0b6d663432c84defdf10faa8003a | quote: "last-modified": "Sun, 01 Nov 2026 09:38:42 GMT"
  - probe:https://iptoasn.com/data/ip2asn-v4.tsv.gz 2026-11-02: the answer was dated 2026-11-02 10:42:50 GMT | capture: sha256:bcfb577227d09b49fcc33790d22d90757d5c0b6d663432c84defdf10faa8003a | quote: "date": "Mon, 02 Nov 2026 10:42:50 GMT"
- sources:
  - [1] https://iptoasn.com/
  - [2] https://iptoasn.com/data/ip2asn-v4.tsv.gz
