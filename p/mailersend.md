# MailerSend

> mailersend.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mailersend/ | JSON https://fshy.ajam.dev/api/v1/entity/mailersend.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MailerSend

- `email/mailersend` | fails-quota | evidence documented | binding request-rate | category transactional sender
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T05:33:30.050Z (live) | stale on 2026-12-05
- url https://www.mailersend.com/pricing
- free tier: 500 emails/month on the Free plan once the account is approved, with a daily quota of 100 API and SMTP relay requests; 1 domain, 1 API token, 1 webhook, 1 template | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: Sandbox mode, open with no payment method, gives 100 emails a month with a cap of 100 API requests a day, to any 2 recipients until the account is approved, with no time limit
- per-object cap: not applicable
- retention: 1-day activity data retention on the free plan | days: 1 | source: [1]
- egress: not applicable: an outbound sender | metered: no | source: [1]
- identity: card | detail: signup needs an email address, confirmed from a verification email sent to that address; approval then asks for details of the company or organization and how the service will be used, and takes up to 48 hours; Sandbox mode needs no payment method; the Free plan is subscribed on the Plan and billing page with an organization address and credit card information, after the account is approved, and is not charged
- interface: rest
- limits:
  - request-rate (binding): 500 emails per month [1]
  - request-rate (binding): 100 API or SMTP relay requests per day on the Free plan; every request counts against the quota, which resets at midnight UTC [2]
- limits note: counts of things, not rates, so no vocabulary kind names them: 1 sending domain, 1 API token, 1 webhook, 1 template. The daily 100 is a quota of API and SMTP relay requests on the rate-limit, SMTP relay and developer pages and in the plans table (Daily API requests), and the plans help page prose calls it a daily limit of 100 emails; how many emails one request may carry on the Free plan is not stated
- interface detail: the MailerSend email API and SMTP relay
- tooling: curl, any SMTP client
- composes with: composes with a domain and with nothing that needs volume.
- reliability: sending pauses when the monthly limit is reached and resumes when the 30-day period resets; the Free plan allows no extra usage
- notes: The 14-day Professional trial at the top of the pricing page needs a payment method and ends on the Free plan; Sandbox mode needs no payment method.
- extras:
  - stale_after_days: 90
- evidence:
  - [1] 2026-10-22: the Free column reads '500 emails /month', 1 domain, 1-day retention and '100' daily API requests
  - probe:smtp://smtp.mailersend.net:587 2026-10-22: banner 250, STARTTLS completed and AUTH LOGIN returned 334; EHLO advertises 8BITMIME and no SIZE extension
  - [3] 2026-10-30: the Free plan sends 500 emails a month after approval, with a daily limit of 100 | capture: sha256:e001c62342515d98999ec2419834e3feb3a51988a999648ea007d8052ade193e | quote: Once approved, the Free plan allows you to send up to 500 emails a month for free, with a daily limit of 100 emails.
  - [4] 2026-10-30: Sandbox mode sends 100 emails a month, to 2 recipients until approval | capture: sha256:b5ef3fb2b60bcdf994077330814f71bdd93114d9465c48877b6c306c51cea629 | quote: You can send to any 2 recipients in Sandbox mode, until your account is approved, after which your 100 monthly emails can go to any recipient.
  - [1] 2026-10-30: the Free plan needs an organization address and a credit card on file | capture: sha256:e04f553ab7ed38fe36dce2571fa42d54916e068c356975ff8e473b473f53143d | quote: Simply go to the Plan and billing page and enter your organization’s address and credit card information to complete your subscription.
  - [3] 2026-10-30: the Free plan keeps activity data 24 hours | capture: sha256:e001c62342515d98999ec2419834e3feb3a51988a999648ea007d8052ade193e | quote: | Activity retention | 24 hours | 24 hours | 7 days | 30 days |
  - [3] 2026-10-30: sending pauses at the limit until the 30-day period resets | capture: sha256:e001c62342515d98999ec2419834e3feb3a51988a999648ea007d8052ade193e | quote: If you reach this limit within the 30-day usage period, your sendings will be paused until a new period begins and your email limit is reset.
  - [3] 2026-10-30: the plans help page calls the daily 100 a limit of emails | capture: sha256:e001c62342515d98999ec2419834e3feb3a51988a999648ea007d8052ade193e | quote: Once approved, the Free plan allows you to send up to 500 emails a month for free, with a daily limit of 100 emails.
  - [4] 2026-10-30: the 14-day trial ends on the Free plan | capture: sha256:b5ef3fb2b60bcdf994077330814f71bdd93114d9465c48877b6c306c51cea629 | quote: If you haven't chosen a plan by the time your 14 days are up, your account moves to the Free plan.
  - [1] 2026-10-30: a card is asked for the Free plan and is not charged | capture: sha256:e04f553ab7ed38fe36dce2571fa42d54916e068c356975ff8e473b473f53143d | quote: You won't be charged for anything on the Free plan; we just ask that you provide this information to prevent abuse of the platform.
  - probe:smtp.mailersend.net:587 2026-10-31: the MailerSend SMTP relay answers on port 587 with a 220 ESMTP banner | capture: sha256:21ba8b1bab525e6e89e778a2ad76f72cca8dfb34d1db49abb91165c33c3ddcd9 | quote: "banner": "220 smtp.mailersend.net ESMTP"
  - [1] 2026-10-30: the Free plan sends 500 emails a month | capture: sha256:e04f553ab7ed38fe36dce2571fa42d54916e068c356975ff8e473b473f53143d | quote: This plan lets you send up to 500 emails per month for free!
  - [1] 2026-10-31: the pricing page, the free tier's source_url, states the 500-email Free plan when read on 2026-10-31 | capture: sha256:e04f553ab7ed38fe36dce2571fa42d54916e068c356975ff8e473b473f53143d | quote: This plan lets you send up to 500 emails per month for free!
  - [3] 2026-10-31: the Free plan sends 500 emails a month after approval, with a daily limit of 100 | capture: sha256:e001c62342515d98999ec2419834e3feb3a51988a999648ea007d8052ade193e | quote: Once approved, the Free plan allows you to send up to 500 emails a month for free, with a daily limit of 100 emails.
  - [1] 2026-10-31: the Free plan allows 100 requests a day, 1 domain, 1 API token, 1 webhook and 1 template | capture: sha256:e04f553ab7ed38fe36dce2571fa42d54916e068c356975ff8e473b473f53143d | quote: Our Free plan has a few limits per account: 1 template, 1 domain, 1 user (plus 1 accountant), 1 API token, 1 webhook, and 100 daily requests.
  - [3] 2026-10-31: the Free plan column (first) keeps activity data 24 hours | capture: sha256:e001c62342515d98999ec2419834e3feb3a51988a999648ea007d8052ade193e | quote: | Activity retention | 24 hours | 24 hours | 7 days | 30 days |
  - [1] 2026-10-31: the Free plan needs an organization address and a credit card on file | capture: sha256:e04f553ab7ed38fe36dce2571fa42d54916e068c356975ff8e473b473f53143d | quote: Simply go to the Plan and billing page and enter your organization’s address and credit card information to complete your subscription.
  - [3] 2026-10-31: sending pauses at the limit until the 30-day period resets | capture: sha256:e001c62342515d98999ec2419834e3feb3a51988a999648ea007d8052ade193e | quote: If you reach this limit within the 30-day usage period, your sendings will be paused until a new period begins and your email limit is reset.
  - [4] 2026-10-31: Sandbox mode sends 100 emails a month with a cap of 100 API requests a day | capture: sha256:b5ef3fb2b60bcdf994077330814f71bdd93114d9465c48877b6c306c51cea629 | quote: 100 emails a month, with a cap of 100 API requests a day
  - [4] 2026-10-31: the 14-day Professional trial needs a payment method and Sandbox mode is the alternative without one | capture: sha256:b5ef3fb2b60bcdf994077330814f71bdd93114d9465c48877b6c306c51cea629 | quote: When you sign up, we'll offer you a choice: start your free 14-day Professional trial by adding a payment method, giving you full access to send to real recipients and Professional features, or skip this and try Sandbox mode instead.
  - [2] 2026-11-02: the Free plan's daily quota is 100 requests, counted for the API and the SMTP relay | capture: sha256:5cb41ee904ece1f1f4a4a58f3a42b83d2b73e3bfffcf97a594ad2eb6cbd8a326 | quote: Free plan: 100 requests per day
  - [5] 2026-11-02: every API or SMTP relay request counts against the daily request quota, which resets at midnight UTC | capture: sha256:ac224243b6b8197354ea6b73567ad58b3dcced84e138e6817191df6747de92c3 | quote: MailerSend has a daily request quota for API and SMTP relay services, which varies depending on your subscription plan. Every request made counts against your daily quota, which is reset daily at midnight UTC
  - [5] 2026-11-02: the daily request quota table lists 100 requests a day for the Free plan | capture: sha256:ac224243b6b8197354ea6b73567ad58b3dcced84e138e6817191df6747de92c3 | quote: | Free | 100 |
  - [2] 2026-11-02: every API or SMTP relay request counts against the daily quota, which resets at midnight UTC | capture: sha256:5cb41ee904ece1f1f4a4a58f3a42b83d2b73e3bfffcf97a594ad2eb6cbd8a326 | quote: MailerSend has a daily request quota for API and SMTP relay services. Every request is counted against the quota and is reset daily at midnight UTC.
  - [6] 2026-11-02: the developer documentation counts the daily quota in API and SMTP relay requests | capture: sha256:fa3470eab9dbd9683a06b1c3ef8bc46ca9bf5c7769bc2b2494320b50f89e8261 | quote: MailerSend has a daily request quota for API and SMTP relay services. Every request is counted against the quota and is reset daily at midnight UTC.
  - [7] 2026-11-02: signup is confirmed by a verification email sent to the address given | capture: sha256:f87692e5dd76b55ec2b737a347ce0982f5d0928610860d736af658ee63de6318 | quote: Confirm your email address from the verification email sent to the address you signed up with.
  - [7] 2026-11-02: account approval asks for details of the company or organization and the planned use | capture: sha256:f87692e5dd76b55ec2b737a347ce0982f5d0928610860d736af658ee63de6318 | quote: This involves providing details about your company or organization and explaining how you plan to use MailerSend.
  - [7] 2026-11-02: account approval can take up to 48 hours | capture: sha256:f87692e5dd76b55ec2b737a347ce0982f5d0928610860d736af658ee63de6318 | quote: The approval process is usually very quick but can take up to 48 hours.
  - [7] 2026-11-02: the payment method is asked only for the 14-day Professional trial, and skipping it leads to Sandbox mode | capture: sha256:f87692e5dd76b55ec2b737a347ce0982f5d0928610860d736af658ee63de6318 | quote: start your free 14-day Professional trial by adding a payment method, giving you full access to send to real recipients and Professional features, or skip this and try Sandbox mode instead
  - [7] 2026-11-02: the getting-started guide was captured on 2026-11-02 and states the signup step the record cites | capture: sha256:f87692e5dd76b55ec2b737a347ce0982f5d0928610860d736af658ee63de6318 | quote: Confirm your email address from the verification email sent to the address you signed up with.
  - [2] 2026-11-02: the SMTP relay help page still lists a Free plan quota of 100 requests a day | capture: sha256:5cb41ee904ece1f1f4a4a58f3a42b83d2b73e3bfffcf97a594ad2eb6cbd8a326 | quote: Free plan: 100 requests per day
  - [1] 2026-11-04: the Free plan is 500 emails a month, unchanged | capture: sha256:e04f553ab7ed38fe36dce2571fa42d54916e068c356975ff8e473b473f53143d | quote: This plan lets you send up to 500 emails per month for free!
- sources:
  - [1] https://www.mailersend.com/pricing
  - [2] https://www.mailersend.com/help/smtp-relay
  - [3] https://www.mailersend.com/help/plans-features-and-limits
  - [4] https://www.mailersend.com/help/sandbox-mode-and-the-professional-trial
  - [5] https://www.mailersend.com/help/rate-limits-how-to-reduce-403-422-429-errors
  - [6] https://developers.mailersend.com/general.html
  - [7] https://www.mailersend.com/help/getting-started
