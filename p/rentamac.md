# RentaMac

> rentamac.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rentamac/ | JSON https://fshy.ajam.dev/api/v1/entity/rentamac.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RentaMac (rentamac.io)

- `compute/rentamac` | paid-only | evidence documented | binding write-gated | category macOS host
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:03:51.315Z (live) | stale on 2026-12-26
- url https://rentamac.io/pricing
- free tier: Your access starts immediately after payment and auto-renews unless you cancel from the User Portal. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: card | detail: Email and password, or Google, create a portal account; access to the rented Mac starts only after payment and auto-renews monthly. No phone or ID document is stated.
- interface: ssh
- limits:
  - request-rate: a monthly term with continuous 24/7 access; no hourly rate and no free tier [1]
  - write-gated (binding): access starts only after payment and auto-renews, so a card is the gate [1]
- interface detail: Remote desktop through DeskIn after payment, full SSH terminal access with scp/sftp, and full root administrator privileges; credentials arrive by email after purchase.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states continuous 24/7 access on a monthly term. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: a rented Mac; the page prices the term rather than the shape
  - session_cap.restart_required: no
  - session_cap.note: continuous access with no hour cap and no resource to reap
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - ps.price: included in the monthly term
  - ps.durability: the rented device
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: any
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '1 month access. Continuous 24/7 access - not working days or limited hours. Your access starts immediately after payment and auto-renews unless you cancel from the User Portal.' and 'Billed monthly', quoted
  - [1] 2026-11-25: paid access starts on payment and auto-renews; no free tier is stated | capture: sha256:ac2ff89442ed2e95bea67572fd232621bd4f03ac12767fda8f6d5246f3e892b1 | quote: Your access starts immediately after payment and auto-renews unless you cancel from the User Portal.
  - [1] 2026-11-24: the rented Mac exposes full SSH terminal access and scp/sftp file transfer | capture: sha256:ac2ff89442ed2e95bea67572fd232621bd4f03ac12767fda8f6d5246f3e892b1 | quote: SSHFull SSH terminal access to your Mac for remote development, running builds, and file transfers (scp/sftp). Connect from any terminal using the credentials provided after purchase.
  - [1] 2026-11-24: the access interface is DeskIn remote desktop with emailed credentials | capture: sha256:ac2ff89442ed2e95bea67572fd232621bd4f03ac12767fda8f6d5246f3e892b1 | quote: Remote desktopConnect via DeskIn remote desktop software. After purchase, you’ll receive credentials by email.
  - [1] 2026-11-24: payment is required before access starts, so a card is the binding identity gate for the paid service | capture: sha256:ac2ff89442ed2e95bea67572fd232621bd4f03ac12767fda8f6d5246f3e892b1 | quote: Your access starts immediately after payment and auto-renews unless you cancel from the User Portal.
  - [2] 2026-11-24: the sign-up page asks for an email and password and offers Google sign-in | capture: sha256:2c9201722626896a09143d9bbf9359303726a29b40f9f7cc9d0292f5c54ba162 | quote: Enter your details to get started with Rent a Mac
  - [1] 2026-11-24: there is no free tier; continuous 24/7 access is a paid monthly term | capture: sha256:ac2ff89442ed2e95bea67572fd232621bd4f03ac12767fda8f6d5246f3e892b1 | quote: 1 month accessContinuous 24/7 access — not working days or limited hours. Your access starts immediately after payment and auto-renews unless you cancel from the User Portal.
  - [3] 2026-11-24: disk data is wiped after each rental session | capture: sha256:4e2ab96ffdef1c21c9228b4fcef88ed7589d658b27c914301c18b9f2b17ee38b | quote: After your session, we ensure all data is removed by performing a full system wipe.
  - [4] 2026-11-24: the rented Mac is advertised from USD 3.97 a day, with daily, weekly and monthly terms | capture: sha256:7ca1c82dcfae64fce192bac8cc8dd897f22fe9e8a684791fb97c5bd397956fa3 | quote: From $3.97/day
- sources:
  - [1] https://rentamac.io/pricing
  - [2] https://portal.rentamac.io/register
  - [3] https://rentamac.io/faq/
  - [4] https://www.rentamac.io
