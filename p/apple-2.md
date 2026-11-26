# Apple Managed Apple Account

> apple.com.cn | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apple-2/ | JSON https://fshy.ajam.dev/api/v1/entity/apple-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Apple Managed Apple Account (Apple School Manager), 200 GB

- `netdisk-pan/apple-managed-apple-account-200-gb` | fails-identity | evidence reported | binding write-gated | category education-ecosystem cloud
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T15:23:47.350Z (inherited) | stale on 2026-12-10
- url https://www.apple.com.cn/education/docs/overview_of_managed_appleid.pdf
- free tier: 200 GB of free iCloud storage for each Managed Apple Account | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published per file | source: [2]
- retention: The account is owned and controlled by a school or district; no page read states what happens to the account or its storage when a student leaves | source: [1]
- egress: Normal iCloud egress, with no metering on download | metered: no | source: [2]
- identity: institution | detail: an institution: Apple School Manager lets schools create and manage Managed Apple Accounts | country: any Apple School Manager country
- interface: unknown
- limits:
  - write-gated (binding): enrolment in Apple School Manager is a prerequisite for every account [2]
- binding note: The quota is real and 200 GB is respectable, but the account belongs to a school and the interface list is empty. Either the identity gate or the absent API would stop it alone.
- tooling: none documented on the pages read: iCloud for Windows does not support Managed Apple Accounts
- composes with: 200 GB times N accounts, where every account needs a school. Since no programmatic read path exists, the capacity cannot enter any programmatic stack
- reliability: The account is owned by the institution, so the bytes are not yours and do not survive leaving it. 200 GB is also below a 500 GB threshold unless multiplied, and no API exists to multiply it with
- notes: A faculty member could obtain this; an individual registrant cannot, and even with a school the bytes are not portable.
- extras:
  - access_mode: institution
  - api: none
  - account_owner: the school
- evidence:
  - [2] 2026-10-21: '升级的 iCloud 储存空间。管理式 Apple ID 可享用 200GB 的免费 iCloud 储存空间'
  - [1] 2026-10-21: 'Managed Apple IDs are owned and controlled by the school'
  - [3] 2026-10-21: the 5 GB to 200 GB change for students and teachers
  - [4] 2026-11-03: Apple School Manager federates with Google Workspace, Microsoft Entra ID or an identity provider | capture: sha256:3f2d26a7e30ed4cc8c679df2ec905a97cac0011199f566e440b5411a47ece43f | quote: You can link to Google Workspace, Microsoft Entra ID, or your IdP, but only one at a time.
  - [1] 2026-11-25: the account is owned and controlled by the school or district | capture: sha256:bed9d851ef9e9ebd83d39cec629ee431daadbbfdd3ce9e35ed78fa226b83d42b | quote: Unlike a personal account, a Managed Apple Account is owned and controlled by a school or district.
  - [5] 2026-11-25: schools create and manage the accounts through Apple School Manager | capture: sha256:d1383bfdbead68ae279e040101033bc8270561841ad23b856fac0fc6ca5b4de2 | quote: Lastly, Apple School Manager makes it easy for schools to create and manage these accounts at scale.
  - [6] 2026-11-25: 200 GB free per Managed Apple Account | capture: sha256:2ef7d169d610488d472650982c473a7a3da2719c5659e538ec108183f11f3195 | quote: along with 200 gigabytes (GB) of free iCloud storage for each Managed Apple Account
  - [4] 2026-11-25: iCloud for Windows does not support Managed Apple Accounts | capture: sha256:3f2d26a7e30ed4cc8c679df2ec905a97cac0011199f566e440b5411a47ece43f | quote: (iCloud for Windows doesn’t support Managed Apple Accounts)
  - [5] 2026-11-25: the accounts are owned and managed by an organization | capture: sha256:d1383bfdbead68ae279e040101033bc8270561841ad23b856fac0fc6ca5b4de2 | quote: Managed Apple Accounts function much like Apple Accounts but are specifically designed for, owned, and managed by, an organization to help increase the productivity of instructors and students and provide the services users may need.
  - [1] 2026-11-25: Apple states the Managed Apple Account storage in GB | capture: sha256:bed9d851ef9e9ebd83d39cec629ee431daadbbfdd3ce9e35ed78fa226b83d42b | quote: Every Managed Apple Account is given 200 gigabytes (GB) of iCloud Drive storage.
- sources:
  - [1] https://support.apple.com/guide/schoolwork-teacher/aside/phx4f3b4c8c7/1/ios/1.0
  - [2] https://www.apple.com.cn/education/docs/overview_of_managed_appleid.pdf
  - [3] https://www.macrumors.com/2018/03/27/apple-student-icloud-storage-200gb/
  - [4] https://support.apple.com/guide/apple-school-manager/intro-to-federated-authentication-axmb19317543/web
  - [5] https://support.apple.com/guide/apple-school-manager/intro-to-managed-apple-accounts-axm78b477c81/web
  - [6] https://support.apple.com/guide/schoolwork-teacher/get-set-up-phx440748466/ios
