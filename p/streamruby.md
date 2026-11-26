# StreamRuby

> streamruby.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/streamruby/ | JSON https://fshy.ajam.dev/api/v1/entity/streamruby.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StreamRuby

- `storage/streamruby` | qualifies-with-caveat | evidence documented | binding none | category media
- needs card no, phone no, ID no, institution no | verified 2026-11-25T19:55:23.058Z (live) | stale on 2026-12-26
- url https://streamruby.com
- free tier: Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views. | unit: GB | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: 10 GB per file on the Free Creator plan | source: [1] | note: The plan table's maximum upload file size row gives 10 GB, 20 GB and 20 GB.
- retention: Free videos are removed after 60 days without views or downloads. | source: [1] | note: On Free Creator, videos are removed after 60 consecutive days without views or downloads; this inactivity policy is separate from changes to the storage allowance.
- egress: Unlimited bandwidth | metered: no
- identity: email | detail: Email address, username, password, confirm password and a captcha
- interface: rest
- limits note: 20,000 MB (20 GB) per file per the official plan table; video-only (HLS transcode); 60-day deletion when unviewed for free tier
- interface detail: rest
- tooling: XFileSharing-style api.html + PolyUploader (github.com/spel987/PolyUploader) lists StreamRuby; XFS '?op=api' key pattern applies
- composes with: Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views. Your allowance adjusts monthly with your views.
- reliability: video-only: everything is transcoded to HLS, so it is not byte-exact storage; free-tier storage allowance is recomputed monthly from views, so it can shrink (existing videos are not deleted)
- notes: 250 GB free storage, grows +250 GB per 1,500 monthly views; 'no upper limit'; unlimited bandwidth; no credit card
- evidence note: the streamruby.com homepage states the 250 GB free allowance and unlimited bandwidth
- evidence:
  - [1] 2026-10-21: 'Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views'; 'Unlimited Bandwidth'; 'A lower allowance won't delete your existing videos'
  - [2] 2026-10-21: 20,000 MB max upload for free tier, 60-day no-download expiry (per awesome-file-hosts citations of this page)
  - [3] 2026-10-21: StreamRuby listed as a supported host
  - [1] 2026-11-09: the homepage states a 250 GB free allowance that grows with monthly views | capture: sha256:a9e5d4bc6b5130d9cd6a05056d03045f3d88a8cda003967cc355e096bc08c048 | quote: Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views.
  - [2] 2026-11-09: the plan table gives the free plan a 10 GB maximum upload size | capture: sha256:558a2d36555fbdf55d0956581955ebaaa50ccbeff47d6e30bd7f24d06cd4c92a | quote: | Maximum upload file size | 10 GB | 20 GB | 20 GB |
  - [2] 2026-11-09: the premium page footnote states that free videos are removed after 60 days without views or downloads | capture: sha256:558a2d36555fbdf55d0956581955ebaaa50ccbeff47d6e30bd7f24d06cd4c92a | quote: Free videos are removed after 60 days without views or downloads.
  - [1] 2026-11-09: the homepage lists unlimited bandwidth | capture: sha256:a9e5d4bc6b5130d9cd6a05056d03045f3d88a8cda003967cc355e096bc08c048 | quote: Unlimited bandwidth
  - [4] 2026-11-09: the registration form asks for a username, email address, password, password confirmation and a captcha | capture: sha256:b2bab94bb1b0775140552eb2c90a56c2275c427fb175fd99070f6957f0885271 | quote: Username ... Email address ... Password ... Confirm password ... Enter captcha
  - [1] 2026-11-11: the homepage states the 250 GB free allowance and that it grows by another 250 GB for every 1,500 monthly views | capture: sha256:7fa5d5a14bc2fe2dd1efc857b40a6e312389dbc14234303942400fd053c3077b | quote: Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views.
  - [1] 2026-11-11: the Free Creator plan card on the homepage lists unlimited bandwidth | capture: sha256:7fa5d5a14bc2fe2dd1efc857b40a6e312389dbc14234303942400fd053c3077b | quote: Unlimited bandwidth
  - [2] 2026-11-25: the plan table states a 10 GB maximum upload file size in the first plan column and 20 GB in the other two | capture: sha256:74b1f6214ecef6a8195cfed51ae5cd7514ab2efd2af8575e430ec7e1b33bf189 | quote: | Maximum upload file size | 10 GB | 20 GB | 20 GB |
  - [2] 2026-11-25: the plan table still states the maximum upload file sizes | capture: sha256:74b1f6214ecef6a8195cfed51ae5cd7514ab2efd2af8575e430ec7e1b33bf189 | quote: | Maximum upload file size | 10 GB | 20 GB | 20 GB |
  - [1] 2026-11-25: the homepage FAQ states the 60-day inactivity removal and separates it from allowance changes | capture: sha256:a9e5d4bc6b5130d9cd6a05056d03045f3d88a8cda003967cc355e096bc08c048 | quote: On Free Creator, videos are removed after 60 consecutive days without views or downloads. This inactivity policy is separate from changes to your storage allowance.
  - [1] 2026-11-25: the FAQ still states the 60-day inactivity removal | capture: sha256:a9e5d4bc6b5130d9cd6a05056d03045f3d88a8cda003967cc355e096bc08c048 | quote: On Free Creator, videos are removed after 60 consecutive days without views or downloads. This inactivity policy is separate from changes to your storage allowance.
  - [1] 2026-11-25: the homepage states unlimited bandwidth | capture: sha256:a9e5d4bc6b5130d9cd6a05056d03045f3d88a8cda003967cc355e096bc08c048 | quote: Unlimited bandwidth
  - [5] 2026-11-25: the API documentation gives HTTP GET endpoints on streamruby.com | capture: sha256:5814b1ecfaf11abd0e938c166cc0ee4a48d855cd394d3e5a5f828804891c998c | quote: GET https://streamruby.com/api/account/info?key=45dd5cy578znbgobv
  - [1] 2026-11-25: the homepage states the view-based monthly storage allowance | capture: sha256:a9e5d4bc6b5130d9cd6a05056d03045f3d88a8cda003967cc355e096bc08c048 | quote: Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views. Your allowance adjusts monthly with your views.
  - [1] 2026-11-25: the homepage states a 250 GB starting allowance that grows by 250 GB per 1,500 monthly views | capture: sha256:a9e5d4bc6b5130d9cd6a05056d03045f3d88a8cda003967cc355e096bc08c048 | quote: Start with 250 GB free and unlock another 250 GB for every 1,500 monthly views. Your allowance adjusts monthly with your views.
- sources:
  - [1] https://streamruby.com/
  - [2] https://streamruby.com/premium
  - [3] https://github.com/spel987/PolyUploader
  - [4] https://streamruby.com/?op=registration
  - [5] https://streamruby.com/api.html
