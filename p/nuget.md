# NuGet.org

> nuget.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nuget/ | JSON https://fshy.ajam.dev/api/v1/entity/nuget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NuGet.org

- `storage/nuget-org` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.nuget.org
- free tier: 250 MB per package. No documented total-storage quota and no documented cap on package count per account; organizations are free. Over 500k packages / petabytes-scale gallery in practice. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered, Cloudflare-fronted, CORS-open. Probe: api.nuget.org v3-flatcontainer .nupkg GET -> 200, Server: cloudflare, Access-Control-Allow-Origin: *, Cache-Control: max-age=86400. | metered: no
- identity: institution
- interface: rest
- limits note: 250 MB per package (hard 413). API rate limited (429 + Retry-After). Deleting a package is strongly discouraged and effectively unsupported ('In general, we do not support deleting a package published to NuGet.org'); unlisting is the normal path. Signed packages are immutable including the nuspec.
- interface detail: rest
- tooling: Push via PUT/POST to the v2 endpoint (nuget.exe / dotnet nuget push); pull via the v3 flat-container URL pattern api.nuget.org/v3-flatcontainer/{id}/{version}/{id}.{version}.nupkg. First-class clients, anonymous read.
- composes with: UNBOUNDED in principle: unlimited packages x 250 MB. 10 TiB = ~44,000 packages. Rate limits are the binding constraint (HTTP 429 with Retry-After). Package IDs are globally unique per version and cannot be reused, so name-sharding has to be planned up front.
- reliability: No deletion path means data does not vanish. Good for archive. No total quota documented means no hard ceiling appears anywhere, but also no documented guarantee; a bulk workload has no stated allowance to point at. 429s on sustained pushes.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Nuget.org has a package size limit of about 250 MB' + the 413 error text
  - [2] 2026-10-21: 'NuGet.org allows packages up to 250MB'; 'In general, we do not support deleting a package published to NuGet.org'
  - [3] 2026-10-21: 429 with 'Rate limit is exceeded. Try again in N seconds.'
  - [4] 2026-10-21: probe: GET -> 200, Content-Length: 2441966, Server: cloudflare
- sources:
  - [1] https://learn.microsoft.com/en-us/nuget/nuget-org/publish-a-package
  - [2] https://learn.microsoft.com/en-us/nuget/nuget-org/nuget-org-faq
  - [3] https://learn.microsoft.com/en-us/nuget/api/rate-limits
  - [4] https://api.nuget.org/v3-flatcontainer/newtonsoft.json/13.0.3/newtonsoft.json.13.0.3.nupkg
