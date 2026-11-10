# mcp.gd

> mcp.gd | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mcp/ | JSON https://fshy.ajam.dev/api/v1/entity/mcp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## mcp.gd — MCP-native object storage for agents

- `storage/mcp-gd-mcp-native-object-storage-for-agents` | fails-quota | evidence reported | binding per-object-cap | category Agent infrastructure storage
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mcp.gd/
- price ~$51 (Starter $5/mo for 100 GB) with 100 GB/mo egress cap | parsed USD 50/TB-mo
- free tier: Free: 10 GB storage, 10 GB/month traffic, 100 MB web upload. Paid Starter $5/mo: 100 GB storage, 100 GB/mo traffic, 10 GB web upload. Marketing claims 'up to 100GB per file' and 'no storage capacity cap'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100GB per file | bytes: 100000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 10 GB/month traffic on free. A hard egress meter, which is the real binding cap. | metered: no | free allowance: 10 GB per month
- identity: email | detail: email
- interface: rest
- limits:
  - per-ip-shaping: 1 TB/day [1]
  - per-object-cap (binding): 100GB per file [1]
- limits note: Free tier 10 GB storage / 10 GB monthly traffic / 100 MB web upload. The 100 GB per-file claim appears to be a platform limit, not a free-tier allowance.
- interface detail: MCP over SSE (https://mcp.gd/mcp/sse) with OAuth 2.0 or bearer API token; REST/path API; 14 MCP tools
- tooling: Claude.ai connector, Claude Desktop, `claude mcp add --transport sse mcp-gd`, curl with Bearer token
- composes with: 10 GB free + 10 GB/month egress. The 'no storage cap, 100 GB per file' headline is contradicted by the 10 GB plan line on the same page.
- reliability: Two numbers on the same page contradict: 'Up to 100GB per file … No storage capacity cap' in the feature list vs '10GB storage and 10GB/month traffic included at no cost' in the signup step. The free-tier number is the one with a price next to it, so it is the one to believe.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free: 10 GB storage, 10 GB/month traffic, 100 MB web upload. Paid Starter $5/mo: 100 GB storage, 100 GB/mo traffic, 10 GB web upload. Marketing claims 'up to 100GB per file' and 'no storage capacity cap'.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: ~$51 (Starter $5/mo for 100 GB) with 100 GB/mo egress cap
- evidence:
  - [1] 2026-10-21: 'Up to 100GB per file. Store PDFs, spreadsheets, videos, and more as-is. No storage capacity cap.' vs 'Sign up free. No credit card required. 10GB storage and 10GB/month traffic included at no cost.'
  - [2] 2026-10-21: pricing table: Free = 10 GB storage / 10 GB monthly traffic / 100 MB web upload; Starter $5 = 100 GB / 100 GB / 10 GB
  - [3] 2026-10-21: 'Your files are stored on secure cloud infrastructure using S3-compatible storage'
  - [4] 2026-10-21: PROBE: curl -D - -> 401, Content-Length 71, nginx; /docs and /pricing -> 404 — no docs site, quota only from the landing page and third-party mirrors
- sources:
  - [1] https://mcp.gd/
  - [2] https://mcpservers.org/tr/servers/mcp-gd
  - [3] https://mcp.gd/privacy
  - [4] https://mcp.gd/api/v1/files
