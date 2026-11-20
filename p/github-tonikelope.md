# MegaBasterd

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-tonikelope/ | JSON https://fshy.ajam.dev/api/v1/entity/github-tonikelope.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MegaBasterd

- `debrid/megabasterd` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding per-ip-shaping | category MEGA-only downloader/uploader/streaming client (Java desktop app) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:52:41.420Z (live) | stale on 2026-11-23
- url https://github.com/tonikelope/megabasterd
- price USD 0
- free tier: 'Yet another unofficial (and ugly) cross-platform MEGA downloader/uploader/streaming suite.' GPL-3.0, latest release 8.61 on 2026-09-24, distributed as an executable or a jar that 'requires Java 8 or later'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No hosted version by the author. Anything presented as 'MegaBasterd online' is either a third-party container the user runs or an unofficial redistribution site.
- per-object cap: MEGA publishes no per-file cap: 'MEGA does not have any file size limits. The only limitations you face are the amount of free space on your local device (if downloading) or in your Cloud drive (if uploading).' | source: [2]
- retention: not applicable: the user writes to local disk. The MEGA-side file lives until the owner deletes it. | source: [1]
- egress: MEGA meters downloads per IP for free and anonymous users, not per file: the limit is 'based on the amount of data downloaded from your IP address over the past six hours' and has no fixed byte value. | metered: yes | free allowance: dynamic, IP-based, six-hour window; no published number | source: [3]
- identity: anonymous | detail: Public MEGA links download without a MEGA account. An account is only needed for private content or to raise the quota, and the app's own proxy rotation exists because the anonymous quota is the binding limit.
- interface: cli
- limits:
  - per-ip-shaping (binding): MEGA transfer quota counted per IP over six hours; over-quota downloads stall with HTTP 509 until the window resets [3]
  - per-ip-shaping (binding): quota only starts applying to a file once it has been transferred in full more than 10 times [3]
- limits note: The app's headline feature is working around the 509: it rotates a proxy list when MEGA blocks an IP. MEGA's own help page warns that third-party tools 'can't detect your quota', which is exactly why a client sees stalls rather than an error.
- binding note: At 1 TiB/month the IP-based six-hour window is what stops a MEGA download; the workaround is proxy rotation, which the app implements, and the fallback is waiting for the window to reset. Nothing else in the vocabulary binds because MEGA has no per-file cap.
- interface detail: A Java Swing desktop application launched from the jar or the packaged executable. No API documentation and no server mode were found in the repository or README; the closest thing to a machine interface is driving the jar under a virtual framebuffer, or the third-party Docker images that expose its window over VNC.
- tooling: Jar plus platform executables; AppImage build; community Docker images (vttc08/megabasterd) that wrap the GUI in noVNC. Automating it needs a display server or a wrapper around its GUI, which is a tooling note and not a reason to reject the provider.
- composes with: It is the MEGA leg of a pipeline: pair it with a hosted relay (saveindrive-style MEGA-to-Drive streaming) when no local machine can run the jar.
- reliability: MEGA answers over-quota requests with HTTP 509 and the window is per IP, so a shared or datacentre address exhausts it fast. MEGA's help page also warns third-party clients can lock an account when used with credentials.
- notes: The 'hosted fork' search turned up containers (self-hosted Docker with noVNC) and an unofficial site megabasterd.com that redistributes builds; neither is a hosted service that accepts a URL. The unofficial site was not used and its binaries were not downloaded.
- evidence note: Repository, README, release date and MEGA's own quota page were read. The proxy-rotation behaviour is a third-party description (deepwiki) and is marked reported. A measured rung needs a real MEGA link downloaded twice, once to quota.
- self hosted: yes
- extras:
  - hosted_forks_found: vttc08/megabasterd (Docker + noVNC, user-run); JairoQuispe/docker-megabasterd-app (Docker); megabasterd.com (unofficial redistribution site, unverified provenance)
  - quota_workaround: proxy rotation on HTTP 509, per third-party documentation
- evidence:
  - [1] 2026-10-23: GPL-3.0 MEGA downloader/uploader/streaming suite; 5.8k stars; release 8.61 dated 2026-09-24; 'requires Java 8 or later'
  - [4] 2026-10-23: README offers 'Download latest build' and a DEMO video; no hosted/online instance is offered
  - [3] 2026-10-23: the limit is 'based on the amount of data downloaded from your IP address over the past six hours'; 'MEGA does not have a fixed download limit'; quota starts after 10 full transfers; incomplete transfers discarded after 48 hours
  - [2] 2026-10-23: 'MEGA does not have any file size limits.'
  - [5] 2026-10-23: reported, third-party: 'Smart Proxy System helps bypass MEGA's download limitations by automatically rotating through a list of proxies' when MEGA returns 509
- sources:
  - [1] https://github.com/tonikelope/megabasterd
  - [2] https://help.mega.io/files-folders/transfers/no-file-size-limits
  - [3] https://help.mega.io/plans-storage/space-storage/transfer-quota
  - [4] https://raw.githubusercontent.com/tonikelope/megabasterd/master/README.md
  - [5] https://deepwiki.com/tonikelope/megabasterd/4-advanced-features
