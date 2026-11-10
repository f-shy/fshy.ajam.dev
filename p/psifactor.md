# Psifactor

> psifactor.pl | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/psifactor/ | JSON https://fshy.ajam.dev/api/v1/entity/psifactor.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Psifactor

- `compute/psifactor-free` | qualifies-with-caveat | evidence documented | binding write-gated | category LXC-VPS | tier Darmowy VPS
- needs card yes, phone no, ID no, institution no | verified 2026-11-02T02:17:38.782Z (live) | stale on 2026-12-03
- url https://psifactor.pl/?go=vps
- free tier: 'kontener LXC zarządzany przez Incus', 'do 2 GB RAM', 'do 10 GB limitu dysku (quota)', 'prawa root w VPS', 'dystrybucja Linuksa wybrana przez Ciebie'. Each container gets 'stały publiczny adres IPv6, nazwę hosta i rekord PTR', and incoming IPv4 arrives through forwarded ports on the host address. A shell account with 41 GB of quota plus 5 GB NextCloud and 5 GB Immich comes with it, and the quotas sum. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: 'możliwość podmontowania zasobów konta shell w kontenerze' with the note that the shell quota and the VPS quota 'może być efektywnie zsumowana'. The VPS page states no per-account server count.
- retention: 'Nie można posiadać VPS, o którym tu mowa, bez konta shell. Utrata konta shell, np. z powodu nieaktywności, jest równoznaczna z utratą VPS.' The administrator can delete an account at any time without warning. No idle timeout is quantified for the VPS itself.
- egress: quoted for the shell host: '1 Gbps bez limitu danych w Niemczech' (1 Gbit/s, no data limit, in Germany). No separate allowance is stated for the container. | metered: no | free allowance: no data limit stated | source: [2]
- identity: card | detail: a one-off non-refundable payment of PLN 0.01 is the identity check, and it is charged rather than pre-authorised: the signup form requires acceptance of 'bezzwrotnej wpłaty 0,01 PLN jako elementu weryfikacji tożsamości' and states 'Wpłata nie gwarantuje założenia konta'. No larger hold appears on any page read. The rail that carries the PLN 0.01, and whether a prepaid or virtual card passes for it, are not published at https://psifactor.pl/?go=newaccount, which names no card and no payment provider; the terms list identity verification as a starting condition and add nothing to it. The form asks first and last name, email, a login, an IRC nick on #wtw and the intended use; it asks for no phone and no document.
- interface: ssh, rest
- limits:
  - volume-quota: 2 GB RAM and 10 GB disk per container; 41 GB plus 10 GB of side services on the shell account [1]
  - write-gated (binding): a shell account is a precondition, and the administrator decides whether a VPS is created at all [3]
  - retention-clamped: losing the shell account, including through inactivity, loses the VPS [3]
- binding note: Two human gates stand in front of the container: the shell account is manually approved, and the terms state that the administrator alone decides whether a VPS is created, and only for users 'z dłuższym stażem'.
- interface detail: root in an Incus-managed LXC container, reachable over a static public IPv6 with a PTR record; IPv4 inbound through agreed port forwards from the host address; HTTP/HTTPS reverse proxy from host to container; SSH to the shell account with optional TOTP 2FA
- tooling: any SSH client; Incus on the vendor side
- composes with: The only free row among documented hosts that gives root and a public IPv6 with reverse DNS on a 1 Gbit/s unmetered link, which is what a WireGuard node or an IPv6-reachable monitor actually needs.
- reliability: no reliability event observed. The project states it is hobbyist and non-commercial and that it 'nie zapewniają jakości usług porównywalnych z ofertami komercyjnymi'.
- notes: The best shape and the most conditional: a root LXC container with up to 2 GB of RAM, 10 GB of disk, a static public IPv6 with a PTR record, agreed IPv4 port forwards, and a 1 Gbit/s unmetered German uplink, for a one-off PLN 0.01 identity payment. What it costs is patience and a human: the shell account is manually approved, the container is granted only to users with standing, presence on an IRC channel is a stated condition, and the administrator may delete the account at any time without warning. The PLN 0.01 is a real payment, so the identity kind is card rather than email, but it is not a hold and not a subscription. Cannot register, so 'the administrator grants it' is the one link in the chain not observed.
- evidence note: Shape, the root statement, the IPv6 arrangement, the PLN 0.01 gate and the two-stage approval are quoted from the project's own pages read. Whether a VPS is granted in practice, and how long it takes, is not established: the terms make it discretionary and this category cannot register.
- extras:
  - shape.ram_gib: 2
  - shape.disk_gib: 10
  - billing_model: free
  - term: indefinite while the shell account is active
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: PLN 0.01 once, for identity verification; the container itself is PLN 0.00 with no recurring charge and no published rate to multiply
  - free_tier_kind: free-forever-with-quota
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: agreed ports forwarded from the host IPv4, plus a full public IPv6 per container
  - network_out.static_ip: yes
  - network_out.ipv6: yes
  - session_cap.restart_required: no
  - session_cap.note: no idle kill published for the container; the shell account carries an inactivity rule that is not quantified on the pages read
  - card_hold: PLN 0.01, charged rather than pre-authorised: the signup form calls it a non-refundable payment taken as the identity check, and no larger authorisation is published on any page read
- evidence:
  - [1] 2026-10-24: quoted: 'kontener LXC zarządzany przez Incus', 'do 2 GB RAM', 'do 10 GB limitu dysku (quota)', 'prawa root w VPS', 'każdy kontener otrzymuje stały publiczny adres IPv6, nazwę hosta i rekord PTR', 'dostęp przychodzący po IPv4 odbywa się przez przekierowanie uzgodnionych portów'; page 'Ostatnia modyfikacja: 01.08.2026'
  - [2] 2026-10-24: quoted: 'Limit (quota): 41 GB + 5 GB (NextCloud) + 5 GB (Immich) [do negocjacji]'; '1 Gbps bez limitu danych w Niemczech, i7-8700, 64 GB RAM'; 'VPS w postaci kontenera typu LXC od Incus dla użytkowników z dłuższym stażem'; page 'Ostatnia modyfikacja: 17.09.2026'
  - [4] 2026-10-24: quoted: 'Akceptuję to, że założenie konta wymaga bezzwrotnej wpłaty 0,01 PLN jako elementu weryfikacji tożsamości. Wpłata nie gwarantuje założenia konta.' Form fields: 'Imię i nazwisko', 'Mój email', 'Login', 'Nick na #wtw', 'Cel korzystania', 'Potrzebne usługi'
  - [3] 2026-10-24: quoted: 'VPS jest dedykowany Użytkownikom z dłuższym stażem, którzy posiadają już konto shell. O utworzeniu VPS decyduje administrator.'; 'obecność na kanale IRC' is a basic condition; 'Administrator może również w każdym momencie ... bez ostrzeżenia, usunąć konto shell lub VPS'; page 'Ostatnia modyfikacja: 24.08.2026'
  - [1] 2026-10-24: quoted footer: 'psifactor.pl 2014-2026' and a link to a live status page at psifactor.pl/status/. The project has been running under that name since 2014
  - [4] 2026-11-02: the account fee is a non-refundable PLN 0.01 payment taken as the identity check, and it does not guarantee the account | capture: sha256:67285ab424ef8b9c07ce53080c31802787ce1361d3c2daa1766536f88a7dc456 | quote: Akceptuję to, że założenie konta wymaga bezzwrotnej wpłaty 0,01 PLN jako elementu weryfikacji tożsamości. Wpłata nie gwarantuje założenia konta.
  - [3] 2026-11-02: the terms list identity verification as a basic condition of the account and state no authorisation amount | capture: sha256:e780c5c40d4ce2b82dae04a923ad286d7cbf54e428187d34254abaaf1d9f84d8 | quote: (2) weryfikacja tożsamości potencjalnego Użytkownika.
  - [4] 2026-11-02: the PLN 0.01 is a payment that is taken and kept, not a temporary authorisation, and it does not guarantee the account | capture: sha256:67285ab424ef8b9c07ce53080c31802787ce1361d3c2daa1766536f88a7dc456 | quote: Wpłata nie gwarantuje założenia konta.
  - [4] 2026-11-02: the signup gate still reads as the terms and the form state it: a non-refundable PLN 0.01 payment, no card rail named | capture: sha256:67285ab424ef8b9c07ce53080c31802787ce1361d3c2daa1766536f88a7dc456 | quote: Wpłata nie gwarantuje założenia konta.
- sources:
  - [1] https://psifactor.pl/?go=vps
  - [2] https://psifactor.pl/?go=account
  - [3] https://psifactor.pl/?go=regulamin
  - [4] https://psifactor.pl/?go=newaccount
