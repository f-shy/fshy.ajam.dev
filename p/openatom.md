# AtomGit Notebook

> openatom.cn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openatom/ | JSON https://fshy.ajam.dev/api/v1/entity/openatom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AtomGit Notebook

- `compute/atomgit-notebook` | qualifies-with-caveat | evidence reported | binding retention-clamped | category GPU cloud
- needs card no, phone yes, ID no, institution no | verified 2026-11-06T17:18:19.273Z (live) | stale on 2026-11-21
- url https://www.openatom.cn/journalism/detail/Q5U5ZPm9veBs
- free tier: 'Notebook Space 1000': 1,000 core-hours of free compute a month for Notebook and Space, with GPU/NPU acceleration named in general and no accelerator model named. The announcement prices no card and no hour in currency, so H100, A100 80 GB, L40S, RTX 4090 and L4: not listed. | unit: core-hours | metered on: wall-clock | read on: 2026-11-06 | source: [1] | note: recurring-allowance
- per-object cap: not applicable | source: [1]
- retention: the two-hour session cap plus the temporary filesystem bind first: the environment is wiped on close, so an experiment that is not pushed to a repository is lost at the 2-hour boundary | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | detail: The signup asks for a username, a mobile number and a password, and its phone entry says foreign numbers are not supported yet, so the gate is a mainland-China mobile number. An email address must also be associated with the account. No card and no identity document is named on the page. | country: CN
- interface: rest
- limits:
  - retention-clamped (binding): the two-hour session cap plus the temporary filesystem bind first: the environment is wiped on close, so an experiment that is not pushed to a repository is lost at the 2-hour boundary [1]
- limits note: the two-hour session cap plus the temporary filesystem bind first: the environment is wiped on close, so an experiment that is not pushed to a repository is lost at the 2-hour boundary
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A free Ascend NPU lane is the only free path in comparative records to hardware that is not NVIDIA, which matters when a model must be validated on 910B before it is worth renting; it composes with a code host, because the filesystem is temporary and the repository is the only durable store.
- reliability: no reliability event recorded
- notes: The announcement names GPU/NPU support in general and no accelerator model, so the Ascend attribution rests on the third-party hands-on row in evidence, not on the announcement. The unit is the finding: a core-hour is not a GPU-hour, and the per-shape vCPU count is published on no page read, so the allowance in instance-hours is unresolved. GitCode and AtomGit merged and both names appear for this product.
- extras:
  - facets.class: recurring-monthly-quota
  - facets.free_tier_kind: recurring-allowance
  - facets.shape.gpu_class: Ascend 910B (NPU)
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: quoted, OpenAtom Foundation announcement of the AtomGit launch: Notebook Space 1000
  - [2] 2026-10-22: quoted, Beihang University School of Software announcement: Notebook Space 1,000
  - [3] 2026-10-22: quoted hands-on account 2026-07-13: single 910B card, maximum 2 hours per session, 50 GB temporary storage, environment deleted on close, quota visible as remaining core-hours
  - [4] 2026-10-22: quoted forum post 2026-09-01: 1,000 core-hours a month, and the arithmetic that 1000 / 32 vCPU is about 31 instance-hours while a 4-core shape gives about 250
  - [5] 2026-11-02: the account page lists the three signup fields, the second a mobile number, and says foreign numbers are not supported | capture: sha256:8f4a73f3e8362a1fe497b08bd56b171c2f77bb2888e7d5b0237192d8c29f54e3 | quote: 当你在 GitCode 账号注册时，系统会要求你提供以下信息： 1. 用户名（用户名只能包含字母、数字、- ,且必须以字母开头,长度为3~20） 2. 手机号（暂不支持国外手机号） 3. 密码（密码最少包含一个大写字母、一个小写字母、一个数字以及三者的组合, 长度为6~20之间）
  - [6] 2026-11-02: an email address must be associated with the account | capture: sha256:3887665a68518a60eabc5add6fce87e0341cfee1345e679b35fab2ca768fabea | quote: GitCode 要求用户将有效的电子邮件地址与其 GitCode 帐户相关联。
  - [5] 2026-11-02: the signup field for the account is a mobile number, which is the country-phone kind | capture: sha256:8f4a73f3e8362a1fe497b08bd56b171c2f77bb2888e7d5b0237192d8c29f54e3 | quote: 手机号（暂不支持国外手机号）
  - [1] 2026-11-06: Notebook and Space carry 1,000 core-hours of free compute a month, with no accelerator model named | capture: sha256:6ce72eed9c95314013b0675741f2cb4370b9e04b2108eb40b56da1b40dfb1eee | quote: 平台还为开发者提供Notebook与Space每月1000核时免费算力
  - [1] 2026-11-06: the allowance is denominated in core-hours, not hours of wall clock or GPU-hours | capture: sha256:6ce72eed9c95314013b0675741f2cb4370b9e04b2108eb40b56da1b40dfb1eee | quote: 平台还为开发者提供Notebook与Space每月1000核时免费算力
  - [1] 2026-11-06: the monthly core-hour allowance is unchanged | capture: sha256:6ce72eed9c95314013b0675741f2cb4370b9e04b2108eb40b56da1b40dfb1eee | quote: 平台还为开发者提供Notebook与Space每月1000核时免费算力
  - [1] 2026-11-06: the allowance is 1,000 core-hours a month and the page names no accelerator model | capture: sha256:6ce72eed9c95314013b0675741f2cb4370b9e04b2108eb40b56da1b40dfb1eee | quote: 平台还为开发者提供Notebook与Space每月1000核时免费算力
  - [1] 2026-11-06: the 1,000 core-hour monthly allowance is unchanged | capture: sha256:6ce72eed9c95314013b0675741f2cb4370b9e04b2108eb40b56da1b40dfb1eee | quote: 平台还为开发者提供Notebook与Space每月1000核时免费算力
- sources:
  - [1] https://www.openatom.cn/journalism/detail/Q5U5ZPm9veBs
  - [2] https://soft.buaa.edu.cn/news_nry.jsp?urltype=news.NewsContentUrl&wbnewsid=12102&wbtreeid=1116
  - [3] https://hwcomputing.csdn.net/6a54ad5c662f9a54cb8ee102.html
  - [4] https://linux.do/t/topic/2839878
  - [5] https://gitcode.com/GitCode/GitCode-Docs/wiki/%E7%94%A8%E6%88%B7.md
  - [6] https://docs.gitcode.com/docs/help/home/user_center/account_manage
