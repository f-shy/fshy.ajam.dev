# NIKON IMAGE SPACE and Nikon Imaging Cloud

> nikonusa.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nikonusa/ | JSON https://fshy.ajam.dev/api/v1/entity/nikonusa.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NIKON IMAGE SPACE and Nikon Imaging Cloud

- `netdisk-pan/nikon-image-space-nikon-imaging-cloud` | fails-quota | evidence reported | binding retention-clamped | category camera-vendor cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:56.363Z (inherited) | stale on 2026-11-19
- url https://www.nikonusa.com/content/nikon-image-space
- free tier: NIKON IMAGE SPACE, with its free tiers and the SnapBridge upload, was terminated on 2026-10-15. Its replacement, the image storage of Nikon Imaging Cloud, is 5 GB | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published; Nikon Imaging Cloud storage accepts JPG, RAW, HEIF and TIFF images | source: [2]
- retention: The service was terminated on 2026-10-15 09:00 JST and replaced by Nikon Imaging Cloud with 5 GB; stored images are not migrated, a bulk download is open from 2026-10-15 12:00 to 2027-04-15 13:00 JST, and all data is deleted at that time | days: 0 | source: [3]
- egress: Standard CDN, images only | metered: no | source: [2]
- identity: email | detail: a Nikon ID, free to create; the 5 GB image storage is not tied to a registered product
- interface: unknown
- limits:
  - per-object-cap: 5 GB account total on Nikon Imaging Cloud (the Image Space tiers ended with the service); JPG, RAW, HEIF and TIFF only [4]
  - retention-clamped (binding): the service was terminated on 2026-10-15 and all stored data is deleted on 2027-04-15 13:00 JST [3]
- binding note: Service operations ceased on 2026-10-15. Standard storage was restricted to 2 GB or 20 GB, while the unlimited SnapBridge tier returned downscaled 2-megapixel copies rather than original binary payloads.
- tooling: no public API. SnapBridge is the only ingest path
- composes with: Unlimited upload applied only to images automatically re-encoded to 2-megapixel resolution. All service operations officially terminated in October 2026.
- reliability: Terminated on 2026-10-15 09:00 JST. Stored images are not migrated to the replacement and are deleted on 2027-04-15 13:00 JST. The replacement offers 5 GB
- notes: Service officially ended on 2026-10-15. The unlimited SnapBridge tier accepted image uploads while downscaling files to 2-megapixel resolution, modifying the original bytes.
- extras:
  - access_mode: registration-gated
  - closed: 2026-10-15
  - replacement: Nikon Imaging Cloud, 5 GB
  - downscales_at_ingest: yes
  - aliases: NIKON IMAGE SPACE / Nikon Imaging Cloud
- evidence:
  - [2] 2026-10-21: 'The NIKON IMAGE SPACE service will be terminated on October 15, 2026'; '2GB of space just for signing up'
  - [4] 2026-10-21: '誰でも2GB。ニコン製品をお持ちのお客様は20GBまで無料'
  - [5] 2026-10-21: 'free, unlimited automatic upload of 2-megapixel images', so the unlimited tier is downscaled
  - [1] 2026-11-03: Nikon Imaging Cloud lists Image Space as a 5 GB image storage service with sharing, usable with cameras that Imaging Cloud does not support | capture: sha256:aa61311b19cb0e517ec26a2d176f38354eca17501cbdd41f1bbc06860ba65f23 | quote: A 5 GB image storage service with cloud sharing features.
  - [1] 2026-11-03: Nikon Imaging Cloud lists the 5 GB image storage service | capture: sha256:aa61311b19cb0e517ec26a2d176f38354eca17501cbdd41f1bbc06860ba65f23 | quote: A 5 GB image storage service with cloud sharing features.
  - [3] 2026-11-03: the replacement storage is 5 GB and accepts JPG, RAW, HEIF and TIFF files | capture: sha256:cde5973b1866141a2c33ca16a019b64f320493f97d40af535b9c2b9e46419756 | quote: （画像ストレージ容量：5GB、対応ファイル形式：JPG、RAW、HEIF、TIFF）
  - [3] 2026-11-03: bulk download ends 2027-04-15 13:00 JST and all stored images and registration data are deleted | capture: sha256:cde5973b1866141a2c33ca16a019b64f320493f97d40af535b9c2b9e46419756 | quote: 2027年4月15日（木）13:00をもって画像一括ダウンロード期間は終了し、NIKON IMAGE SPACE内に保管されている画像および登録情報などのすべてのデータは削除されます。
  - [3] 2026-11-03: the service ended 2026-10-15 09:00 JST | capture: sha256:cde5973b1866141a2c33ca16a019b64f320493f97d40af535b9c2b9e46419756 | quote: 2026年10月15日（木）9:00（日本時間）をもって、NIKON IMAGE SPACEのサービスは終了いたしました。
  - [3] 2026-11-03: 5 GB storage, JPG, RAW, HEIF and TIFF | capture: sha256:cde5973b1866141a2c33ca16a019b64f320493f97d40af535b9c2b9e46419756 | quote: （画像ストレージ容量：5GB、対応ファイル形式：JPG、RAW、HEIF、TIFF）
  - [3] 2026-11-03: stored data is deleted at the end of the bulk download period, 2027-04-15 13:00 JST | capture: sha256:cde5973b1866141a2c33ca16a019b64f320493f97d40af535b9c2b9e46419756 | quote: 2027年4月15日（木）13:00をもって画像一括ダウンロード期間は終了し、NIKON IMAGE SPACE内に保管されている画像および登録情報などのすべてのデータは削除されます。
  - [3] 2026-11-03: deletion date of stored images | capture: sha256:cde5973b1866141a2c33ca16a019b64f320493f97d40af535b9c2b9e46419756 | quote: 2027年4月15日（木）13:00をもって画像一括ダウンロード期間は終了し、NIKON IMAGE SPACE内に保管されている画像および登録情報などのすべてのデータは削除されます。
  - [1] 2026-11-03: a Nikon ID is free to create and is the login for the service | capture: sha256:aa61311b19cb0e517ec26a2d176f38354eca17501cbdd41f1bbc06860ba65f23 | quote: Create a Nikon ID and use the service (free)
  - [6] 2026-11-03: third-party report of the shutdown and the bulk download window | capture: sha256:345472c915db0fc3654e2ffdf34cc115b033c96e502df0266df074074390d1f5 | quote: Nikon Image Space will be shut down on October 15, with bulk downloads remaining available until April 15
  - [7] 2026-11-03: the first-party site states the service was terminated | capture: sha256:79a0f554b55973e1390097db69f919efbf3646bdb4c7b71945295e6d8faa20d4 | quote: The NIKON IMAGE SPACE service was terminated on October 15th, 2026.
  - [8] 2026-11-03: English copy of the notice: all data is permanently deleted at the end of the bulk download period | capture: sha256:8df7b457ee20912dcce5e42b1778707d407063f9bbd77f2ff7b77233daa72c8a | quote: All data will be permanently deleted.
  - [1] 2026-11-03: a Nikon ID is free to create | capture: sha256:aa61311b19cb0e517ec26a2d176f38354eca17501cbdd41f1bbc06860ba65f23 | quote: Create a Nikon ID and use the service (free)
- sources:
  - [1] https://imagingcloud.nikon.com/
  - [2] https://www.nikonusa.com/content/nikon-image-space
  - [3] https://nij.nikon.com/news/products/2026/0825.html
  - [4] https://info.nikonimagespace.com/ja_JP/welcome.html
  - [5] https://snapbridge.nikon.com/
  - [6] https://www.digitalcameraworld.com/cameras/cloud-storage/nikon-image-space-just-got-a-death-sentence-this-is-when-to-download-photos-by-and-what-nikon-is-replacing-it-with
  - [7] https://www.nikonimagespace.com/
  - [8] https://nikonrumors.com/2026/08/25/nikon-image-space-is-no-more-nikon-imaging-cloud-will-be-enhanced-with-5gb-of-image-storage.aspx/
