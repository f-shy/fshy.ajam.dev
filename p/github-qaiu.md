# netdisk-fast-download

> github.com | Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-qaiu/ | JSON https://fshy.ajam.dev/api/v1/entity/github-qaiu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## netdisk-fast-download (lz.qaiu.top / 189.qaiu.top)

- `netdisk-pan/netdisk-fast-download` | qualifies-with-caveat | evidence measured | binding per-object-cap | category direct-link-resolver
- needs card no, phone no, ID no, institution no | verified 2026-11-25T14:05:51.157Z (live) | stale on 2026-12-17
- url https://github.com/qaiu/netdisk-fast-download
- free tier: the public lz.qaiu.top endpoint parses share links for the drivers it lists at no charge and with no key | unit: unlimited | metered on: request-count | read on: 2026-10-22 | source: [1] | note: the free endpoint is explicitly not to be depended on; the README asks users to self-host
- per-object cap: the resolved file's own size; the resolver imposes none, and the driver's limit applies (100 MiB on classic Lanzou, 100 GB on 123pan above which a login is needed) | source: [2]
- retention: the resolved URL is short-lived and must be re-minted per request | source: [2]
- egress: the resolver returns a 302 to the pan's own CDN, so the bytes come from the pan and not from the resolver | metered: no | source: [1]
- identity: anonymous | detail: the free endpoint needs no key; the Professional endpoint requires an X-API-Key header or a token parameter
- interface: rest
- limits:
  - request-rate: no published limit on lz.qaiu.top, and the README warns that heavy use gets the server restricted by the pan vendors [1]
  - per-object-cap (binding): 123pan files above 100 MiB now require a login; classic Lanzou is capped at 100 MiB [2]
- binding note: The resolver itself is unlimited and free; what limits it is the driver table, where the pans worth resolving have the smallest per-file caps or now demand a login.
- tooling: GET /parser?url=...&pwd=... returns a 302 to the direct link; the short form /<driver>/<shareKey>@<pwd> does the same; the project is Java and self-hostable
- composes with: the read path for pans that have no WebDAV and no mountable API: resolve the share link to a direct URL, then fetch it with a plain ranged GET
- reliability: The README warns that lz.qaiu.top should not be depended on, that heavy request volume gets the server restricted by the pan vendors, and that FeijiPan blocks most mainland datacentre IPs and bans accounts frequently.
- notes: The free tier and the Professional tier split exactly along the pans that are hard: Lanzou, iLanzou, Ctfile, FeijiPan, ecpan, Fangcloud and 123pan resolve without a key, while Baidu, Xunlei, Quark, UC, 139 and 189 sit behind the key and return 401. That split is the map of which pans still resist programmatic access.
- extras:
  - access_mode: registration-gated
  - free_drivers: lz; iz; ec; fj; fc; ye; ws; le; qqw; ct; ce
  - keyed_drivers: qk; uc; p139; pwo; p189
  - professional_endpoint: https://189.qaiu.top
- evidence:
  - probe:https://lz.qaiu.top/parser?url=https%3A%2F%2Fwww.123pan.com%2Fs%2Fabc 2026-10-22: HTTP 500 with a JSON body naming the driver and the failure: '123网盘-ye: ... ShareKey格式异常'. The endpoint answers without a key and reports the driver's own error, so the free path is live and keyless
  - probe:https://189.qaiu.top/parser?url=https%3A%2F%2Fpan.baidu.com%2Fs%2Fabc 2026-10-22: HTTP 401 with {"code":401,"msg":"未提供API Key（请在请求头X-API-Key或URL参数token中提供）"}, which is the paywall between the free and Professional tiers
  - [2] 2026-10-22: the driver table lists 19 pans with a free-download column and a per-file limit column: Lanzou 100M, 123pan 100G with a login above 100M, WenShuShu 5GB, WPS 10M free, and Quark and UC marked as not downloadable without a login
  - [1] 2026-10-22: the README states the free endpoint, the Professional endpoint at 189.qaiu.top, the driver identifiers, and three warnings about depending on the public server
  - probe:https://lz.qaiu.top/parser?url=https%3A%2F%2Fwww.123pan.com%2Fs%2Fabc 2026-11-19: the keyless public endpoint still answers without a key, returning a driver error | capture: sha256:ecd1999c5af4f69ac4420fad9b5b892bdef4133f6d376d319d8d00195caa8d74 | quote: "status": 500
  - probe:https://189.qaiu.top/parser?url=https%3A%2F%2Fpan.baidu.com%2Fs%2Fabc 2026-11-19: the Professional endpoint still returns an API-key challenge, the boundary between free and keyed tiers | capture: sha256:b7f79f322cffd703fbf8101d69d94aba6cd9fbebb45026b890790c8bbd09c8a6 | quote: "status": 401
  - [1] 2026-11-19: the README still warns not to depend on lz.qaiu.top and that heavy use gets the server restricted | capture: sha256:baddab9015359dcc2d2efefd3d005b678f617108b38c6a3062fbaa3f92e319ed | quote: 请不要过度依赖 lz.qaiu.top，建议本地搭建或者云服务器自行搭建。请求量过多的话服务器可能会被云盘厂商限制
  - [3] 2026-11-25: the README names 189.qaiu.top as the Professional endpoint | capture: sha256:fa782304219f2cc962dd77ead2d6615672bce125f352c7ba971e5945a7c82122 | quote: [专业版](https://189.qaiu.top)
- sources:
  - [1] https://github.com/qaiu/netdisk-fast-download
  - [2] https://nfd-parser.github.io/
  - [3] https://raw.githubusercontent.com/qaiu/netdisk-fast-download/main/README.md

## netdisk-fast-download (NFD), the anonymous multi-pan parser

- `netdisk-pan/netdisk-fast-download-anonymous-multi-pan-parser` | qualifies-with-caveat | evidence reported | binding write-gated | category resolver, not a store
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:15:15.157Z (inherited) | stale on 2026-12-11
- url https://github.com/qaiu/netdisk-fast-download
- free tier: free software with a free public instance, no allowance stated: https://github.com/qaiu/netdisk-fast-download links a 公益 (free public) instance at lz.qaiu.top and prints no quota, unit or price | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: Not applicable, it stores nothing. What it resolves inherits the upstream per-file cap | source: [1]
- retention: Not applicable; the server caches a resolved link for a per-pan time in minutes set in its configuration (shipped values: 5 for ecpan, 20 for feijipan, 30 for lanzou), and a pan with no entry is not cached | source: [1]
- egress: Free. It issues a 302 to the real CDN origin, so the bytes never traverse the resolver and you download straight from the pan's own CDN | metered: no | source: [1]
- identity: anonymous | detail: the hosted instance is keyless. Self-hosting needs a machine the user runs and no account with any pan; individual pan downloads may still need the user's own Quark/UC cookie or 123 Authorization
- interface: rest
- limits:
  - request-rate: the server code has an optional per-IP request limiter, off unless rateLimit.enable is set; the example in the shipped configuration is 10 requests per 10 seconds on /v2/ paths [2]
  - write-gated (binding): Quark at or below 10MiB resolves without login and larger files need a valid SVIP/VIP account cookie or a downloadable H5 address; UC cannot be anonymous even for small files and still needs a cookie; feijipan and ilanzou need auth above 100 MB; 123 downloads usually need the user's own Authorization in the local configuration [1]
- binding note: The resolver is free and stores nothing, so the auth table binds it: Quark is anonymous only up to 10MiB, UC never is, feijipan and ilanzou need auth above 100 MB, and 123 usually needs the user's own Authorization. Baidu and Xunlei moved to the paid professional endpoint; Quark and UC did not.
- tooling: hosted instances first: GET https://lz.qaiu.top/parser?url=<encoded share>&pwd=<code> returns a 302 to the pan's CDN, also on the mirror lz0.qaiu.top. Last resort: the user installs and runs the open-source server (a release archive on Java 17 or later, or the Docker image) on a rented or free machine, with the API on port 6400 and the web tool on port 6401; JavaScript and Java parser plugins extend it
- composes with: Resolve a share link with a hosted instance first (lz.qaiu.top, mirror lz0.qaiu.top), then fetch the returned direct URL with a plain ranged GET. A server the user installs and runs is the last resort; a pan that blocks datacentre addresses, such as feijipan for mainland ranges, is reached through a proxy set in its configuration
- reliability: Individual parsers break whenever a provider changes its markup. The project is actively maintained, so pinning a version and watching the README changelog is the operational answer. The README warns that feijipan blocks mainland datacentre IPs and that the public instance should not be depended on
- notes: Not storage: it is the fetch path for other people's storage. The endpoint split changed: the free public instance lz.qaiu.top now also covers Quark and UC through the open-source parser, while the paid professional endpoint adds Baidu, Xunlei, Guangya, China Mobile, Unicom and Tianyi. The program can also be self-hosted by the user on a rented or free machine; the hosted lz.qaiu.top instance is the last-resort option only when no hosted parser exists, and here it is the primary free path.
- self hosted: no
- extras:
  - access_mode: anonymous
  - free_drivers: lz; iz; ec; fj; fc; ye; ws; le; qqw; ct; ce
  - keyed_drivers: qk; uc; p139; pwo; p189
  - professional_endpoint: https://189.qaiu.top
  - self_hostable: yes
  - aliases: netdisk-fast-download (NFD) — anonymous multi-pan parser
- evidence:
  - probe:https://lz.qaiu.top/parser?url=https%3A%2F%2Fabskoop.lanzoue.com%2FiyobY0jnhpdi 2026-10-21: 302 then 200, 9,314,348 B, application/octet-stream, and the ZIP passed unzip -t
  - probe:https://lz.qaiu.top/parser?url=https%3A%2F%2Fwww.ilanzou.com%2Fs%2FbyZ05Sh3&pwd=xbc6 2026-10-21: 
  - [1] 2026-10-21: the supported list and auth table: '夸克网盘(QK) 必须：必须配置 Cookie 才能解析'; '115网盘(失效)'; the professional tier adds 百度, 迅雷, 夸克, UC, 139, 联通 and 天翼
  - [1] 2026-10-30: the project README links a free public (公益) instance at lz.qaiu.top and gives no quota, unit or price | capture: sha256:e605b75950b3d7e0b2c9d6a853c6f53b1b7db06d22bbe3f63f21b3759d1c8b52 | quote: [公益解析，lz站](https://lz.qaiu.top/)
  - [3] 2026-11-01: the README names port 6400 for the API and port 6401 for the built-in web tool of the server that the user runs | capture: sha256:6db0683295073400965eaad83a2c121f5603936be7fa72d1ff7b6ad18fb59992 | quote: - 6400: API 服务端口（建议使用 Nginx 代理） ... - 6401: 内置 Web 解析工具（个人使用可直接开放此端口）
  - [3] 2026-11-01: the README warns that feijipan blocks most mainland cloud-provider addresses and that a proxy can be configured | capture: sha256:6db0683295073400965eaad83a2c121f5603936be7fa72d1ff7b6ad18fb59992 | quote: 注意⚠️小飞机解析有IP限制，多数云服务商的大陆IP会被拦截（可以自行配置代理），和本程序无关
  - [2] 2026-11-02: the shipped configuration file carries the rateLimit block commented out, with an example of 10 requests per 10 seconds on paths matching ^/v2/.* | capture: sha256:f22ce30e77f56191f653d93c68a231113c70a92484df06f884de98b135b516b4 | quote: #rateLimit: # # 是否启用限流 # enable: true # # 限流的请求数 # limit: 10 # # 限流的时间窗口(单位秒) # timeWindow: 10 # # 路径匹配规则 # pathReg: ^/v2/.*
  - [2] 2026-11-02: the shipped configuration sets the cache time of a resolved link per pan, in minutes: 5 for ecpan, 20 for feijipan and 30 for lanzou | capture: sha256:f22ce30e77f56191f653d93c68a231113c70a92484df06f884de98b135b516b4 | quote: ec: 5 # 移动云空间 ... fj: 20 # 小飞机网盘 链接有效期约30分钟 ... lz: 30 # 蓝奏云 链接有效期约45分钟
  - [4] 2026-11-02: the request interceptor skips the limiter unless rateLimit.enable is true, and answers an over-limit request with HTTP 429 | capture: sha256:e61caca43769725b1d186ca664bd5e904dcaa6b2d385f83d52e2903bd6547d93 | quote: if (!rateLimit.getBoolean("enable", false)) { ... .setStatusCode(429)
  - [5] 2026-11-02: the limiter counts requests per remote address | capture: sha256:9e4589e0e236146382c82d87fe118b24821269c7f3deb5c48d1d6590ad55d8b6 | quote: String ip = request.remoteAddress().host();
  - [6] 2026-11-02: the project documentation lists the rate limit as a configuration section of the server, with a count, a window in seconds and a path pattern | capture: sha256:535dba65a29445fdaa98f3987fcace4b946104ff34075f0bee9fd9776b07e8cf | quote: ### 限流配置 rateLimit: enable: true # 是否启用限流 limit: 10 # 限流请求数 timeWindow: 10 # 时间窗口(秒) pathReg: ^/v2/.*
  - [7] 2026-11-02: the API documentation advises against frequent requests to avoid an address ban and states no figure | capture: sha256:6a2c465b0e259425114f5c7715e7f20e227bd882817b1c38a999a2de92d40ffa | quote: 1. 请求频率: 建议不要过于频繁请求，避免IP被封
  - [3] 2026-11-04: lz.qaiu.top is a free public instance of the program, so this record describes a hosted lane | capture: sha256:6db0683295073400965eaad83a2c121f5603936be7fa72d1ff7b6ad18fb59992 | quote: [公益解析，lz站](https://lz.qaiu.top)
  - [3] 2026-11-04: the program can also be self-hosted through a Docker image | capture: sha256:6db0683295073400965eaad83a2c121f5603936be7fa72d1ff7b6ad18fb59992 | quote: #### 海外服务器Docker部署 ... docker pull ghcr.io/qaiu/netdisk-fast-download:latest
  - [3] 2026-11-25: Quark and UC moved into the open-source version; the paid endpoint now adds Baidu and Xunlei | capture: sha256:fa782304219f2cc962dd77ead2d6615672bce125f352c7ba971e5945a7c82122 | quote: 需要百度、迅雷的完整支持请使用[专业版](https://189.qaiu.top)。夸克网盘、UC网盘已包含在开源版。
  - [3] 2026-11-25: the README now gives a 10MiB anonymous threshold for Quark and an SVIP/VIP or H5 fallback above it | capture: sha256:fa782304219f2cc962dd77ead2d6615672bce125f352c7ba971e5945a7c82122 | quote: | 夸克网盘(QK) | 不超过 10MiB 可走原解析 | 不大于 `10 * 1024 * 1024` 字节（含等于该值）保持原来的分享解析。更大的文件仅在会员接口确认未过期 SVIP/VIP 时使用该账号直链；否则使用探测通过的 H5 文件地址并附上真实文件名。普通或过期 Cookie 不算会员 |
  - [3] 2026-11-25: the comparison table still shows the 10MiB anonymous Quark threshold | capture: sha256:fa782304219f2cc962dd77ead2d6615672bce125f352c7ba971e5945a7c82122 | quote: | 夸克网盘 | ≤10MiB 原解析 | √ | 10G | 更大文件要有效 SVIP/VIP，或可用的 H5 文件地址 |
  - [3] 2026-11-25: the public instance has no shared 123 account and uses the user's own Authorization | capture: sha256:fa782304219f2cc962dd77ead2d6615672bce125f352c7ba971e5945a7c82122 | quote: 123 的下载在公共解析站上基本都要你自己的 Authorization，云端没有共用账号。
  - [8] 2026-11-25: the free public instance is still answering with version 0.4.8 | capture: sha256:dd0ec906f5afa979c627a4605469d99358d95eac10a4fdb9d4ea118b52780f6d | quote: NFD网盘直链解析 0.4.8
  - [2] 2026-11-25: the shipped example still leaves the per-IP rate limiter commented out | capture: sha256:89d5450030d2dd20b9a9344bd071f0f673e370a27d0bb1fa56adcefb354b96f0 | quote: #rateLimit:
  - [7] 2026-11-26: the sentence names the RESTful API interface | capture: sha256:6a2c465b0e259425114f5c7715e7f20e227bd882817b1c38a999a2de92d40ffa | quote: NFD Parser 提供 RESTful API 接口，支持解析多种网盘分享链接并获取直链。
- sources:
  - [1] https://github.com/qaiu/netdisk-fast-download
  - [2] https://raw.githubusercontent.com/qaiu/netdisk-fast-download/main/web-service/src/main/resources/app-dev.yml
  - [3] https://raw.githubusercontent.com/qaiu/netdisk-fast-download/main/README.md
  - [4] https://raw.githubusercontent.com/qaiu/netdisk-fast-download/main/web-service/src/main/java/cn/qaiu/lz/common/interceptorImpl/DefaultInterceptor.java
  - [5] https://raw.githubusercontent.com/qaiu/netdisk-fast-download/main/web-service/src/main/java/cn/qaiu/lz/common/interceptorImpl/RateLimiter.java
  - [6] https://nfd-parser.github.io/configuration.html
  - [7] https://nfd-parser.github.io/api.html
  - [8] https://lz.qaiu.top
