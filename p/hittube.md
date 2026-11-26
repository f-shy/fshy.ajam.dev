# PeerTube

> hittube.fr | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hittube/ | JSON https://fshy.ajam.dev/api/v1/entity/hittube.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PeerTube, the hittube.fr instance (50 GiB per user, no daily cap)

- `storage/peertube-hittube-fr` | qualifies-with-caveat | evidence measured | binding per-object-cap | category video platform, federated, self-hosted instance
- needs card no, phone no, ID no, institution no | verified 2026-10-22T04:30:16.000Z (live) | stale on 2026-12-07
- url https://hittube.fr
- free tier: 50 GiB per user and no daily upload cap: the instance config reports user.videoQuota 53687091200 and user.videoQuotaDaily -1 | unit: GiB | metered on: stored-bytes | read on: 2026-10-22 | source: [1] | note: registration is open with no approval and no email verification: signup.allowed true, requiresApproval false, requiresEmailVerification false. The instance is HitTube, server version 8.3.1, serverCountry France
- per-object cap: Not published as a byte cap. The instance transcodes to 720, 1080 and 2160 and sets alwaysTranscodeOriginalResolution true, so the file that comes back is a transcode and not the bytes that were uploaded | source: [1] | note: this is the constraint that decides whether the quota is usable: a storage tier that re-encodes at ingest does not return originals
- retention: No stated expiry while the instance runs. The instance is a volunteer-run server with a single administrator and a 2026-10-14 asset date. Retention depends on ongoing server operation. | source: [1]
- egress: Free and unmetered: downloads are enabled by default (publish.downloadEnabled true) and there is no egress line item. HLS is enabled and splitAudioAndVideo is false, so the stream is a single rendition set | metered: no | source: [1]
- identity: email | detail: an email address, and the instance does not verify it: signup.requiresEmailVerification is false and requiresApproval is false. No card, no phone
- interface: rest
- limits:
  - per-object-cap (binding): no byte cap published, but the instance transcodes every upload at the source resolution and sets alwaysTranscodeOriginalResolution true, so the delivered file is not the uploaded file [1]
  - write-gated: an account is required to upload; registration is open with no approval and no email verification [1]
- limits note: The instance reports 201 local videos totalling 21,058,245,956 bytes with 2 registered users, so the operator's disk holds about 21 GB of other people's content. Two users and 21 GB is the scale of the goodwill a 50 GiB quota is drawn on
- binding note: Storage allowance is 50 GiB per account with no daily cap. What binds is video transcoding. Ingested files are re-encoded and return modified bytes, functioning as video hosting rather than exact byte storage.
- interface detail: the PeerTube REST API at /api/v1, with open registration and no token required to read the config or list videos; upload needs an account and a token
- tooling: any HTTP client against /api/v1. PeerTube's own client and third-party uploaders work; there is no rclone backend and no WebDAV, so a pipeline is the upload API or nothing
- composes with: A 50 GiB per-account tier with no daily cap is the largest video-platform allocation found and it does not chain into a storage stack, because the read path returns a transcode. Its role would be as a distribution surface for content that is already video, and not as a store for arbitrary bytes
- reliability: A single-admin volunteer instance in France with two registered users and 39 followers. The config carries a custom support banner and an a-ads iframe, so it is ad-funded and personal. An instance of this size disappears with one hosting decision
- notes: Active instance provides 50 GiB per user with no daily cap and open registration without email verification. Uploaded media is transcoded on ingest, returning re-encoded renditions rather than original files.
- evidence note: the instance configuration and statistics were read live from /api/v1/config and /api/v1/server/stats on 2026-10-22. The quota, the daily cap and the transcode flag are the instance's own reported values. What would raise confidence in the capacity is an upload, which needs an account and was not created
- self hosted: no
- extras:
  - audit_status: the completeness review listed this name as unsupported and said the measured instance was gone; the instance answered live on 2026-10-22
  - instance_software: PeerTube 8.3.1
  - server_country: France
  - registration: open, no approval, no email verification
  - transcodes_at_ingest: yes
  - sibling_note: that host reports videoQuota -1 with videoQuotaDaily 5368709120, which is the opposite trade: unlimited total with a 5 GiB daily cap. The two instances together show that the quota shape is per-instance policy and not a PeerTube default
  - what_this_record_owns: the hittube.fr instance, which the audit believed was lost
- evidence:
  - probe:https://hittube.fr/api/v1/config 2026-10-22: user.videoQuota is 53687091200 and user.videoQuotaDaily is -1, so 50 GiB per user with no daily cap; signup.allowed true, requiresApproval false, requiresEmailVerification false; serverVersion 8.3.1, instance name HitTube, serverCountry France
  - probe:https://hittube.fr/api/v1/config 2026-10-22: transcoding.enabledResolutions is [720, 1080, 2160] and transcoding.alwaysTranscodeOriginalResolution is true, so every upload is re-encoded at its own resolution rather than stored as received
  - probe:https://hittube.fr/api/v1/config 2026-10-22: defaults.publish.downloadEnabled is true and videoFile.update.enabled is false, so downloads are allowed and uploaded files cannot be replaced
  - probe:https://hittube.fr/api/v1/server/stats 2026-10-22: totalUsers 2, totalLocalVideos 201, totalLocalVideoFilesSize 21058245956, totalInstanceFollowers 39, totalAdmins 1, which sizes the operator's disk and the user base
  - probe:https://hittube.fr/api/v1/videos?count=1 2026-10-22: the public video list answers anonymously with total 201, so the read path needs no account
- sources:
  - [1] https://hittube.fr/api/v1/config
