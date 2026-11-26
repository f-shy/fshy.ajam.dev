# EX.UA

> bbc.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bbc/ | JSON https://fshy.ajam.dev/api/v1/entity/bbc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EX.UA

- `debrid/ex-ua` | dead | evidence documented | binding write-gated | category Ukrainian file host (closed 2016) | tier closed
- needs card no, phone no, ID no, institution no | verified 2026-11-26T02:15:10.482Z (live) | stale on 2026-12-27
- url https://www.bbc.com/ukrainian/news_in_brief/2016/11/161116_om_ex_ua
- free tier: Closed. At closure the site asked users to remove their files: 'EX.ua ... запропонував користувачам видалити файли зі своїх архівів до 30 листопада' (2016-11-16). | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the service is closed | source: [1] | note: unstated
- retention: Files were to be removed by users before 2016-11-30; the service then stopped. | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: not applicable: no account can be created | country: Ukraine
- interface: unknown
- limits:
  - write-gated (binding): service terminated 2016-11-16; files to be removed by 2016-11-30 [1]
- limits note: The service announcement cited 'direct threats and blackmailing [including at the national level] and DDOS attacks' as the reason.
- binding note: Nothing is served; the only relevant fact is the closure date.
- interface detail: None: the domain stopped serving the service. The site had earlier been seized by police in 2012 and restored.
- tooling: None.
- composes with: Nothing to chain. It is the reason a Ukrainian user looking for a domestic host has no large one left and uses Russian hosts or international debrid instead.
- reliability: The site had already been taken down once, in January 2012, during a criminal investigation, and came back; the 2016 closure was final.
- notes: Користувачі сайту можуть видалити файли зі своїх архівів до 30 листопада.
- evidence note: Two independent dated reports (BBC Ukrainian 2016-11-16 and Interfax-Ukraine 2016-11-17) agree on the closure and the 30 November deadline. Evidence dates normalised to the read date on 2026-10-23; a source that carries its own date keeps it in the proved field.
- evidence:
  - [1] 2026-10-23: 'Український ресурс EX.ua вирішив припинити роботу' and the 30 November deadline for users to remove files
  - [2] 2026-10-23: 'The Ukrainian file hosting service ex.ua has informed about the decision to terminate its operations and asked all users to remove the files from their archives on ex.ua before November 30, 2016.'
  - [1] 2026-11-26: the BBC report states this removal deadline verbatim | capture: sha256:ab8ddf59eb8fe077f85423b85615be202d0b4dda576da6297688cc3a6d98555d | quote: Користувачі сайту можуть видалити файли зі своїх архівів до 30 листопада.
- sources:
  - [1] https://www.bbc.com/ukrainian/news_in_brief/2016/11/161116_om_ex_ua
  - [2] https://en.interfax.com.ua/news/economic/384560.html
