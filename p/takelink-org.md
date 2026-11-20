# Takelink.org

> Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/takelink-org/ | JSON https://fshy.ajam.dev/api/v1/entity/takelink-org.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Takelink.org

- `debrid/takelink-org` | dead | evidence documented | binding write-gated | category Russian multi-host link straightener (dead, domain repurposed) | tier closed
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:18:27.322Z (live) | stale on 2026-11-23
- url https://web.archive.org/web/20230205043248/http://www.takelink.org/
- free tier: Was a paid multi-host straightener for letitbit, depositfiles, turbobit and similar hosts; today the domain serves unrelated content and the live origin does not answer. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable: the service is gone | source: [1] | note: unstated
- retention: not applicable | source: [1]
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: not applicable: no account can be created
- interface: unknown
- limits:
  - write-gated (binding): the domain no longer belongs to the service; the live origin answers HTTP 530 through network requests on two attempts probe:https://takelink.org/
- limits note: A 2011 blog post still describes it as 'takelink.org ... Скачать бесплатно прямые ссылки на файлообменники', and a 2012 forum post names it among services with Russian support; both predate the death.
- binding note: Nothing is served; the domain reassignment is the finding.
- interface detail: None. The 2023-02-05 capture of the domain is a Chinese-language gambling page wrapped around copied Ripple marketing text - the signature of an expired domain that was re-registered.
- tooling: part of interface detail
- composes with: Nothing to chain; it is the archetype of the Russian link-straightener that died and whose domain was sold.
- reliability: A dead multi-hoster's domain is a phishing surface: the brand still appears in old forum and blog recommendations, and the domain now serves unrelated content.
- notes: Named in the sector brief as a service Russian forums mention, so it is closed with evidence rather than left as an open question. The 2023 capture predates the check by three and a half years, which means the domain had already changed hands well before the live probe failed.
- evidence note: Two independent observations: the live origin returns HTTP 530 to network requests (twice, 2026-10-23), and the Wayback capture of 2023-02-05 is a repurposed gambling page. The service's own last state was not archived in a form that renders. Evidence dates normalised to the read date on 2026-10-23; a source that carries its own date keeps it in the proved field.
- evidence:
  - [1] 2026-10-23: the domain served a Chinese gambling page with copied Ripple copy ('澳洲幸运5开奖查询 ... Ripple is the leading provider of crypto solutions for businesses') - not the multi-hoster
  - probe:https://takelink.org/ 2026-10-23: HTTP 530 from the origin on two separate attempts; no content, no redirect to a successor
  - [2] 2026-10-23: what the service was: 'takelink.org. Скачать бесплатно прямые ссылки на файлообменники'
- sources:
  - [1] https://web.archive.org/web/20230205043248/http://www.takelink.org/
  - [2] http://blogrider.ru/blogs/78829/posts/id/4408344/servis-bistrogo-skachivaniya-s-platnikh-fayloobmennikov.php
