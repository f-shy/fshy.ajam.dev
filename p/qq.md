# WeChat Official Account

> qq.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qq/ | JSON https://fshy.ajam.dev/api/v1/entity/qq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## WeChat Official Account — uploadimg (图文消息图片, the uncapped endpoint)

- `storage/wechat-official-account-uploadimg` | fails-egress | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.weixin.qq.com/doc/service/api/material/permanent/api_uploadimage
- free tier: NO documented count cap. The docs state explicitly: "该接口所上传的图片，不占用公众号的素材库中图片数量的100000个的限制". Images uploaded via this endpoint do NOT count against the 100,000-image library limit. Per-file cap 1 MB, JPG/PNG only. | unit: MB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file cap 1 MB | bytes: 1000000 | source: [1] | note: not stated
- retention: | Images are permanent in practice (they must survive in published articles forever), but the service is tuned for article inline images, so bulk non-image binary upload is impossible and a hotlink-blocked 403 can appear without warning. | source: [1] | note: not stated
- egress: Free and unmetered. The response hands back a public CDN URL on mmbiz.qpic.cn ("url": "http://mmbiz.qpic.cn/XXXXX"), which is served by Tencent's CDN with no access_token and no auth header. This is the only genuinely anonymous read path found in this entire slot. | metered: no | source: [2]
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): Per-file cap 1 MB [1]
- limits note: 1 MB per image, jpg/png only. access_token required to UPLOAD (2h expiry, refresh loop needed). Download is anonymous. mmbiz.qpic.cn applies a Referer/hotlink check. Direct GETs without a WeChat/weixin Referer can be refused, which breaks plain curl fetch fan-out and CDN-fronting.
- interface detail: rest
- tooling: Trivial. One multipart POST: curl -F media=@test.jpg "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=ACCESS_TOKEN". No wrapper needed; any HTTP client plus a token-refresh loop (access_token lives 7200s) is the whole client.
- composes with: The absence of a count cap means one account is already unbounded in object count; the binding limit becomes 1 MB/file. 1 account = effectively millions of 1MB objects. Multiple Official Accounts (1 per entity) multiply further, but count is not the constraint. File size is.
- reliability: Images are permanent in practice (they must survive in published articles forever), but the service is tuned for article inline images, so bulk non-image binary upload is impossible and a hotlink-blocked 403 can appear without warning.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: NO documented count cap. The docs state explicitly: "该接口所上传的图片，不占用公众号的素材库中图片数量的100000个的限制" — images uploaded via this endpoint do NOT count against the 100,000-image library limit. Per-file cap 1 MB, JPG/PNG only.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: '该接口所上传的图片，不占用公众号的素材库中图片数量的100000个的限制，图片仅支持jpg/png格式，大小必须在1MB以下' plus response field url = 'http://mmbiz.qpic.cn/XXXXX'
  - [3] 2026-10-21: probe: GET -> 400 text/plain (endpoint live and reachable anonymously; the 400 is a fabricated media id, not an auth wall)
- sources:
  - [1] https://developers.weixin.qq.com/doc/service/api/material/permanent/api_uploadimage
  - [2] http://mmbiz.qpic.cn/XXXXX
  - [3] https://mmbiz.qpic.cn/mmbiz_jpg/<synthetic-id>
