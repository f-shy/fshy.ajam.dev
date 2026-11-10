# jsDelivr

> jsdelivr.com | Storage, Egress and tunnels; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jsdelivr/ | JSON https://fshy.ajam.dev/api/v1/entity/jsdelivr.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## jsDelivr (npm + GitHub proxy CDN)

- `storage/jsdelivr` | qualifies | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.jsdelivr.com
- free tier: No storage quota of its own. It is a serving and permanence layer over npm and GitHub, so the quota is whatever the origin package holds. Hard limits: packages >150 MB and (for GitHub) single files >20 MB are refused by default, raisable on request. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: single files >20 MB | bytes: 20000000 | source: [1] | note: not stated
- retention: | Retention is stronger than the origin: 'Previously served immutable files may be retained in permanent storage even after upstream deletion | source: [1] | note: not stated
- egress: Fully free and explicitly unmetered. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): single files >20 MB [1]
- limits note: 150 MB per npm package, 20 MB per single GitHub file (both default, raisable via GitHub issue). Rate limiting applies to purge, not to reads. Enforcement is the technical risk, not the capability.
- interface detail: rest
- tooling: Plain GET on cdn.jsdelivr.net/npm/<pkg>@<ver>/<path> and /gh/<owner>/<repo>@<ref>/<path>. No client needed. Cache-purge API exists (email-gated).
- composes with: Chains onto npm packages or GitHub repositories: assets published to npm or GitHub releases can be served via jsDelivr edge URLs with 1-year immutable caching and unmetered egress.
- reliability: Retention is stronger than the origin: 'Previously served immutable files may be retained in permanent storage even after upstream deletion. We do not accept removal requests simply because a package or version was unpublished, deleted upstream, or is no longer needed.' Once a URL has been fetched it keeps working after you delete the npm package. That is a genuine cold-archive property. Counter-risk: a 150 MB package cap means a naive >150 MB npm tarball 403s ('Package size exceeded the configured limit of 150 MB') even though npm itself accepted it.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'no bandwidth limits or premium features and its completely free to use by anybody'
  - [2] 2026-10-21: 'no limits on bandwidth or number of requests'; 'Previously served immutable files may be retained in permanent storage even after upstream deletion'
  - [3] 2026-10-21: (README) — 'Packages larger than 150 MB or single files larger than 20 MB (in the case of GitHub) are not supported by default'
  - [4] 2026-10-21: probe: GET -> 200, Access-Control-Allow-Origin: *, Cache-Control: public, max-age=31536000, s-maxage=31536000, immutable, Server: cloudflare
  - [5] 2026-10-21: probe: GET -> 403, body 'Package size exceeded the configured limit of 150 MB.' (confirms the cap is real and enforced at fetch time)
- sources:
  - [1] https://www.jsdelivr.com/about
  - [2] https://github.com/jsdelivr/jsdelivr/blob/master/Terms%20of%20Use.md
  - [3] https://github.com/jsdelivr/jsdelivr
  - [4] https://cdn.jsdelivr.net/npm/left-pad@1.3.0/package.json
  - [5] https://cdn.jsdelivr.net/npm/onnxruntime-node@1.20.1/bin/napi-v3/win32/x64/onnxruntime.dll

## jsDelivr as the free CDN layer over GitHub repos

- `storage/jsdelivr-as-the-free-cdn-layer-over-github-repos` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:47.045Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.jsdelivr.com
- free tier: free with no limits on bandwidth or number of requests; GitHub-proxy soft limits of 10 000 actively accessed files and 100 000 files per repository | unit: objects | metered on: object-count | read on: 2026-10-30 | source: [1] | note: the file-count soft limits are not automatically enforced
- per-object cap: files up to 20 MB through the GitHub proxy, regardless of repository size | bytes: 20000000 | source: [2] | note: not stated
- retention: | Immutable: 'Previously served immutable files may be retained in permanent storage even after upstream deletion'. Deletion upstream does not remove it from jsDelivr. | source: [1] | note: not stated
- egress: Unmetered and cached at edge locations with headers 'Cache-Control: public, max-age=31536000, s-maxage=31536000, immutable' and Access-Control-Allow-Origin: *. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): per file | 20 MB [2]
- limits note: Git repo files only — release assets are NOT served (probed: /gh/cli/cli@v2.102.1/dist/README.md -> 404). ~20 MB effective per-file ceiling for the GitHub proxy (the git-unlimited-storage README states 'jsDelivr per file | 20 MB'); hard per-file/per-package caps are undocumented and enforced at request time. Does not serve the >2 GiB release assets, so the serving path for big objects stays on GitHub's own Fastly edge.
- interface detail: rest
- tooling: URL pattern https://cdn.jsdelivr.net/gh/USER/REPO@TAG/path. No client needed, no auth, no config. Purge API exists for cache busting.
- composes with: Serving layer only: pair it with Releases (storage) or a git repo (small files). One repo backs 1 TiB/day because the edge absorbs repeats with a 1-year immutable TTL.
- reliability: Immutable: 'Previously served immutable files may be retained in permanent storage even after upstream deletion'. Deletion upstream does not remove it from jsDelivr. Extension blocklist exists; binaries with unusual extensions can be refused.
- notes: Provides CDN distribution rather than origin storage. Documentation states 'there are no limits on bandwidth or number of requests' (the provider), with soft limits of 10,000 actively accessed files and 100,000 files per repository.
- evidence:
  - [1] 2026-10-21: 'there are no limits on bandwidth or number of requests'; soft limit '100 000' files per repository
  - withheld 2026-10-21: probe: GET cdn.jsdelivr.net/gh/jquery/jquery@3.7.1/dist/jquery.min.js -> 200, Cache-Control: public, max-age=31536000, s-maxage=31536000, immutable, Access-Control-Allow-Origin: *
  - withheld 2026-10-21: probe: GET cdn.jsdelivr.net/gh/cli/cli@v2.102.1/dist/README.md -> 404 (release assets not mirrored)
  - [1] 2026-10-30: jsDelivr CDN sets no limit on bandwidth or on the number of requests | capture: sha256:2f18e724ac81932cd47f54f153f7202a350bb363b577a1de43bb9073f2771431 | quote: there are no limits on bandwidth or number of requests
  - [1] 2026-10-30: jsDelivr CDN is free | capture: sha256:2f18e724ac81932cd47f54f153f7202a350bb363b577a1de43bb9073f2771431 | quote: using jsDelivr CDN is free
  - [1] 2026-10-30: the GitHub-proxy recommendation is at most 10 000 actively accessed files per repository | capture: sha256:2f18e724ac81932cd47f54f153f7202a350bb363b577a1de43bb9073f2771431 | quote: We recommend that the number of actively accessed files per repository does not exceed 10 000.
  - [1] 2026-10-30: the GitHub-proxy soft limit is 100 000 files per repository | capture: sha256:2f18e724ac81932cd47f54f153f7202a350bb363b577a1de43bb9073f2771431 | quote: The soft limit for the number of files per repository is 100 000.
  - [1] 2026-10-30: the soft limits are not automatically enforced | capture: sha256:2f18e724ac81932cd47f54f153f7202a350bb363b577a1de43bb9073f2771431 | quote: These limits are not automatically enforced by us, but you agree not to exceed them.
  - [1] 2026-10-30:  | capture: sha256:2f18e724ac81932cd47f54f153f7202a350bb363b577a1de43bb9073f2771431 | quote: _Effective date: October 5, 2026_
  - [2] 2026-10-30: a jsDelivr member states the GitHub-proxy per-file limit of 20 MB | capture: sha256:2d9aff2fdf9921dacb7594a19f8bc87205957ed03a5a3139bb131f85f89e24c1 | quote: We actually allow files up to 20 MB for GitHub regardless of the overall repo size
  - [1] 2026-10-30: served immutable files can outlive upstream deletion | capture: sha256:2f18e724ac81932cd47f54f153f7202a350bb363b577a1de43bb9073f2771431 | quote: Previously served immutable files may be retained in permanent storage even after upstream deletion.
- sources:
  - [1] https://www.jsdelivr.com/terms/acceptable-use-policy
  - [2] https://github.com/jsdelivr/jsdelivr/issues/18550

## jsDelivr

- `egress/jsdelivr` | fails-quota | evidence reported | binding per-object-cap | category CDN for package content
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-06
- url https://www.jsdelivr.com/
- free tier: free CDN for npm and GitHub content only | unit: none | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: package-file sizes; the per-file class limit could not be read | source: [1]
- retention: not applicable | source: [1]
- egress: no bandwidth cap found on a first-party page | metered: no | source: [1]
- identity: anonymous | detail: no account to read from the CDN
- interface: rest
- limits:
  - per-object-cap (binding): serves npm and GitHub content only, at package-file sizes [1]
- interface detail: https://cdn.jsdelivr.net/npm/PKG@VER/FILE
- tooling: curl
- composes with: Serves assets published in public package registries like npm. Does not support arbitrary private backend proxying.
- reliability: the policy page at /policy returned 404 on 2026-10-22; /terms and /about resolve
- notes: Open-source CDN for public software packages. Serves files directly from package registries; unmetered bandwidth claims apply to open-source repository distribution.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the CDN serves package files from its edge
- evidence:
  - probe:https://www.jsdelivr.com/policy 2026-10-22: 404 on 2026-10-22, so the per-file limit and the no-cap claim could not be read first-hand
- sources:
  - [1] https://www.jsdelivr.com/
