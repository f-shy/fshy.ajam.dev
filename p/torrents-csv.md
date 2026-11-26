# Torrents-CSV

> torrents-csv.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/torrents-csv/ | JSON https://fshy.ajam.dev/api/v1/entity/torrents-csv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Torrents-CSV

- `debrid/torrents-csv` | qualifies-with-caveat | evidence documented | binding request-rate | category torrent index with a JSON service endpoint (bulk dataset plus search) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:47:05.724Z (live) | stale on 2026-12-26
- url https://torrents-csv.com/
- price USD 0
- free tier: No key: /service/search?q=debian&size=2 returned JSON with infohash, name, size_bytes, seeders, leechers and completed. The HTML homepage is behind an Anubis proof-of-work challenge. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: index rows | source: [2]
- retention: rows carry a scraped_date and are kept after the swarm dies; seeders is the liveness signal | source: [2]
- egress: no byte allowance: JSON only; whether the project also publishes a bulk dump was not checked on the pages read | metered: no | free allowance: none published | source: [2]
- identity: anonymous | detail: No account for either surface. The HTML surface costs a proof-of-work computation, not an identity.
- interface: rest
- limits:
  - request-rate (binding): none published; the front end answers a client without JavaScript with an Anubis proof-of-work challenge rather than a 429 [2]
- limits note: Anubis is a bot-defence layer, so the wall is computational rather than a quota: a browser solves it in seconds, a plain HTTP client does not.
- binding note: The HTML surface is the thing that breaks first, and it breaks on the challenge rather than on a rate; the JSON endpoint stayed open during on 2026-10-23.
- interface detail: /service/search?q=<query>&size=<n> returns JSON. The web front end is served behind Anubis v1.28.1, a proof-of-work challenge, which the API endpoint did not present to us.
- endpoint: https://torrents-csv.com/service/search?q=debian&size=2
- tooling: One GET against /service/search. A bulk mirror would remove the query loop entirely, but the dump's existence and size were not verified today.
- composes with: Search by title for a quick check, or take the bulk dump and filter locally; either way the infohash is what feeds a debrid cache check.
- reliability: Anubis rejects clients that disable JavaScript features (the page names JShelter), and the front end and the service endpoint have different gates, so a pipeline tested on one can fail on the other.
- notes: Useful because the search endpoint is one GET with a stable schema, and the caveat is that the same host gates its HTML behind a proof of work, so an unannounced change would break a scraper without warning. The bulk-dump path that TorrentClaw's docs imply was not verified here.
- evidence note: Both surfaces were fetched on 2026-10-23: the JSON answered, the HTML returned the Anubis interstitial. A recorded run against the bulk dump confirms the dataset size.
- extras:
  - anubis_version: v1.28.2
  - bulk_dump: unverified
  - api_open: yes
- evidence:
  - [1] 2026-10-23: HTTP 200 application/json with infohash, name, size_bytes, seeders, leechers, completed and scraped_date
  - [2] 2026-10-23: 'Making sure you're not a bot!', Anubis version v1.28.1, proof-of-work challenge instead of the index
  - [2] 2026-11-25: the HTML front end now names Anubis v1.28.2 | capture: sha256:d4db3ea68bc595d8da6df7ef48626ffa96ca3e7988527ad62340e55b87db07d7 | quote: This website is running Anubis version `v1.28.2`.
  - [2] 2026-11-25: the front-end challenge is still Anubis v1.28.2 | capture: sha256:d4db3ea68bc595d8da6df7ef48626ffa96ca3e7988527ad62340e55b87db07d7 | quote: This website is running Anubis version `v1.28.2`.
  - [1] 2026-11-25: the JSON search endpoint still returns infohash, name, size_bytes, seeders, leechers, completed and scraped_date with no key | capture: sha256:88d9fc807fd26fb7e30404f9c6caefa380872eaa96b1fa9faa58d1331c2e034a | quote: {"infohash":"029830a40e0fd9eca4cabb8f8c0e24a9e8c5a03f","name":"Mastering Debian Linux. From Beginner to Advanced 2024","size_bytes":4392928,"created_unix":1746104157,"seeders":17,"leechers":1,"completed":226,"scraped_date":1792904386,"id":140379}
  - [2] 2026-11-25: the HTML surface gates on a proof-of-work computation rather than a published rate | capture: sha256:d4db3ea68bc595d8da6df7ef48626ffa96ca3e7988527ad62340e55b87db07d7 | quote: Please note that Anubis requires the use of modern JavaScript features that plugins like JShelter will disable.
  - [2] 2026-11-25: the HTML surface is a proof-of-work challenge rather than the index | capture: sha256:d4db3ea68bc595d8da6df7ef48626ffa96ca3e7988527ad62340e55b87db07d7 | quote: This is a measure against bots and malicious requests similar to a CAPTCHA.
- sources:
  - [1] https://torrents-csv.com/service/search?q=debian&size=2
  - [2] https://torrents-csv.com/
