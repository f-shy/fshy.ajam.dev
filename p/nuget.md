# NuGet.org

> nuget.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nuget/ | JSON https://fshy.ajam.dev/api/v1/entity/nuget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NuGet.org

- `storage/nuget-org` | qualifies-with-caveat | evidence reported | binding none | category registry
- needs card no, phone no, ID no, institution no | verified 2026-11-25T21:21:16.189Z (live) | stale on 2026-12-10
- url https://www.nuget.org
- free tier: 250 MB per package. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: about 250 MB per package | source: [1] | note: NuGet.org allows packages up to 250MB, but we recommend keeping packages under 1MB if possible and using dependencies to link packages together.
- retention: source: [1] | note: nuget.org does not support permanent deletion of packages.
- egress: Free and unmetered, Cloudflare-fronted, CORS-open. Probe: api.nuget.org v3-flatcontainer .nupkg GET -> 200, Server: cloudflare, Access-Control-Allow-Origin: *, Cache-Control: max-age=86400. | metered: no
- identity: email | detail: To publish on nuget.org, sign in to nuget.org with a Microsoft account, and use it to create a free nuget.org account.
- interface: rest
- limits note: 250 MB per package (hard 413). API rate limited (429 + Retry-After). Deleting a package is strongly discouraged and effectively unsupported ('In general, we do not support deleting a package published to NuGet.org'); unlisting is the normal path. Signed packages are immutable including the nuspec.
- interface detail: rest
- tooling: Push via PUT/POST to the v2 endpoint (nuget.exe / dotnet nuget push); pull via the v3 flat-container URL pattern api.nuget.org/v3-flatcontainer/{id}/{version}/{id}.{version}.nupkg. First-class clients, anonymous read.
- composes with: UNBOUNDED in principle: unlimited packages x 250 MB. 10 TiB = ~44,000 packages. Rate limits are the binding constraint (HTTP 429 with Retry-After). Package IDs are globally unique per version and cannot be reused, so name-sharding has to be planned up front.
- reliability: No deletion path means data does not vanish. Good for archive. No total quota documented means no hard ceiling appears anywhere, but also no documented guarantee; a bulk workload has no stated allowance to point at. 429s on sustained pushes.
- notes: the same as the free tier
- evidence note: the publish page states the package size limit
- evidence:
  - [1] 2026-10-21: 'Nuget.org has a package size limit of about 250 MB' + the 413 error text
  - [2] 2026-10-21: 'NuGet.org allows packages up to 250MB'; 'In general, we do not support deleting a package published to NuGet.org'
  - [3] 2026-10-21: 429 with 'Rate limit is exceeded. Try again in N seconds.'
  - [4] 2026-10-21: probe: GET -> 200, Content-Length: 2441966, Server: cloudflare
  - [2] 2026-11-09: a package may be up to 250 MB | capture: sha256:678f3b1c1322e31195b663629a619bf3161dc56cd840dba91f28dc9bcb4a3661 | quote: NuGet.org allows packages up to 250MB
  - [1] 2026-11-09: the package size limit is about 250 MB | capture: sha256:ccb784147799e6cf8646804a34074cefd973b9cc20702d5ecdb4ca313ffa0c94 | quote: Nuget.org has a package size limit of about 250 MB.
  - [1] 2026-11-09: publishing needs a Microsoft account, which is an email account | capture: sha256:ccb784147799e6cf8646804a34074cefd973b9cc20702d5ecdb4ca313ffa0c94 | quote: To publish on nuget.org, sign in to nuget.org with a Microsoft account, and use it to create a free nuget.org account.
  - [5] 2026-11-25: published packages are not permanently deleted | capture: sha256:0667af8dcd881e8b0327ef8e7cf24af055e9acacb1d83390a8746f081df04028 | quote: nuget.org does not support permanent deletion of packages.
  - [2] 2026-11-25: the first-party FAQ states a 250 MB package limit and a 1 MB packaging recommendation | capture: sha256:678f3b1c1322e31195b663629a619bf3161dc56cd840dba91f28dc9bcb4a3661 | quote: NuGet.org allows packages up to 250MB, but we recommend keeping packages under 1MB if possible and using dependencies to link packages together.
  - [1] 2026-11-25: the publish page states an approximately 250 MB package size limit | capture: sha256:ccb784147799e6cf8646804a34074cefd973b9cc20702d5ecdb4ca313ffa0c94 | quote: Nuget.org has a package size limit of about 250 MB.
  - [1] 2026-11-25: publishing requires signing in with a Microsoft account and creating a free nuget.org account | capture: sha256:ccb784147799e6cf8646804a34074cefd973b9cc20702d5ecdb4ca313ffa0c94 | quote: To publish on nuget.org, sign in to nuget.org with a Microsoft account, and use it to create a free nuget.org account.
- sources:
  - [1] https://learn.microsoft.com/en-us/nuget/nuget-org/publish-a-package
  - [2] https://learn.microsoft.com/en-us/nuget/nuget-org/nuget-org-faq
  - [3] https://learn.microsoft.com/en-us/nuget/api/rate-limits
  - [4] https://api.nuget.org/v3-flatcontainer/newtonsoft.json/13.0.3/newtonsoft.json.13.0.3.nupkg
  - [5] https://learn.microsoft.com/en-us/nuget/nuget-org/policies/deleting-packages
