# LinksVIP

> linksvip.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/linksvip/ | JSON https://fshy.ajam.dev/api/v1/entity/linksvip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LinksVIP

- `debrid/linksvip-net` | qualifies-with-caveat | evidence documented | binding volume-quota | category multi-host premium link generator (Vietnamese: Fshare, 4share, Tenlua plus 20 foreign hosts) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://linksvip.net/premium.html
- price VND 150,000 per 30 days; per-host daily caps apply (3 GB/day on Rapidgator-class hosts, 80 GB/day on Fshare) | parsed USD 5.81/mo
- free tier: The service advertises get-link without a VIP account ('Get link Fshare, 4share, Tài liệu,... tốc độ cao không cần tài khoản VIP') but publishes no free byte allowance; the host table's daily maximums apply to the account, and the trial is sold, not given: 'Trial 1 ngày * 20.000đ'. | unit: none | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The paid trial at VND 20,000 for one day is the only free-adjacent path documented; the trial excludes Nitroflare, Filenext and Katfile.
- per-object cap: No single-file cap is published. The numbers in the host table are per-host daily totals: Fshare 80 GB, Mega 50 GB, 4shared 50 GB, Filefactory 25 GB, Rapidgator 3 GB, Katfile 3 GB. | source: [1] | note: Each row is 'Used / Max' per host per day, not a per-file limit.
- retention: not applicable: the service returns a direct link, it does not store the file | source: [1]
- egress: Metered per host per day. 'Tất cả các host Premium đều có giới hạn hằng ngày. Bạn vui lòng xem mục Daily Limit để biết chi tiết.' Every other host is uncapped by request count: 'Limit 50 links per host every 24 hours. All other Filehosts are unmetered.' | metered: yes | free allowance: none published; per-host daily maximums apply to paid tiers | source: [1]
- identity: card | detail: An international card is accepted directly: 'LinksVIP chấp nhận thanh toán Thẻ Ghi nợ hoặc Tín dụng quốc tế Visa/MasterCard.' Vietnamese rails are offered as an alternative (MoMo, ZaloPay, bank transfer, scratch card), so the card is the foreigner's route and the local rails are the shortcut.
- interface: rest
- limits:
  - volume-quota (binding): 80 GB/day Fshare; 50 GB/day Mega and 4shared; 25 GB/day Filefactory; 10 GB/day 1fichier, Alfafile, Prefiles, Turbobit, Uptobox, Userscloud, Wushare [1]
  - volume-quota (binding): 3 GB/day Rapidgator, Katfile, Keep2share, Filesmonster [1]
  - request-rate: 50 links per host per 24 h; other hosts unmetered [2]
- limits note: The Fshare row shows no 'Used' figure at all, which suggests it is counted differently from the foreign hosts; the vendor separately warns that its Fshare get-link is unstable.
- binding note: The 3 GB/day row (Rapidgator, Katfile, Keep2share) is the first thing that fails for a monthly transfer of 1 TiB, at roughly 30 GB/month per host; the Fshare row at 80 GB/day is the only one that clears 34 GB/day.
- interface detail: Web form: paste a host URL, receive a direct link. A community PHP wrapper (github.com/0x2f0713/Get-link-LinksVIP.net) calls the same endpoint; no official API is documented.
- tooling: Browser plus IDM/JDownloader for the returned link; a community PHP wrapper exists but is unmaintained; no rclone backend.
- composes with: LinksVIP is the cheapest way into Fshare and 4share from outside Vietnam because it takes an international card; at VND 150,000/30 days it costs less than a Fshare VIP month plus the shops it replaces, and the returned link is an ordinary HTTP URL that any download manager can resume.
- reliability: The vendor's own notice says the Fshare get-link path is unstable ('Hiện tại hệ thống Get link Fshare hoạt động không ổn định') and Rapidgator was under maintenance at read time; support runs through a Facebook page, not a ticket system.
- notes: The clearest card-payable Vietnamese service found: it is a Vietnamese-operated shop that takes Visa/MasterCard and also sells into the local wallet economy. Caveat is coverage, not access: 3 GB/day on the hosts a foreign client actually wants. Trigger condition: the card rail disappears, or the Fshare daily cap is withdrawn.
- evidence note: The premium page was fetched raw and the price table, the card sentence and the per-host maximums were read from the HTML. A successful get-link of one Fshare file from outside Vietnam would move this to measured.
- extras:
  - trial_excludes: Nitroflare, Filenext, Katfile
  - hosts_listed: 23
  - local_rails: MoMo, ZaloPay, bank transfer, scratch card ('thẻ cào')
- evidence:
  - [1] 2026-10-23: price ladder 'Trial 1 ngày 20.000đ / 7 ngày 50.000đ / 15 ngày 100.000đ / 30 ngày 150.000đ / 45 ngày 200.000đ / 60 ngày 250.000đ / 90 ngày 350.000đ / 150 ngày 500.000đ / 180 ngày 600.000đ / 365 ngày 1.100.000đ / Lifetime 6.900.000đ'; 'LinksVIP chấp nhận thanh toán Thẻ Ghi nợ hoặc Tín dụng quốc tế Visa/MasterCard.'; 'Tất cả các host Premium đều có giới hạn hằng ngày.'
  - [1] 2026-10-23: per-host daily maximum table: 'fshare.vn Fshare 80 GB', '4share.vn 80 GB', 'Mega 50 GB', 'Rapidgator 3 GB'
  - [2] 2026-10-23: 'Limit 50 links per host every 24 hours. All other Filehosts are unmetered.' and the same 80 GB Fshare row
- sources:
  - [1] https://linksvip.net/premium.html
  - [2] https://linksvip.net/get-link.html
