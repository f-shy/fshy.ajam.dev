# Qualcomm AI

> qualcomm.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qualcomm/ | JSON https://fshy.ajam.dev/api/v1/entity/qualcomm.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qualcomm AI Hub

- `compute/qualcomm-ai-hub` | qualifies-with-caveat | evidence documented | binding none | category cloud VM
- needs card no, phone unknown, ID no, institution no | verified 2026-11-04T06:40:26.616Z (live) | stale on 2026-12-05
- url https://workbench.aihub.qualcomm.com/docs/hub/faq.html
- free tier: Free compile, profiling and inference on real Qualcomm devices, in the cloud: 'Qualcomm AI Hub Workbench, our platform, is currently completely free to use. We encourage you to submit your models, compile them, and submit inference jobs to both iterate on performance and to check the accuracy and download the target asset'. The workflow is described as 'submit an inference job, running your compiled model on a real device hosted in the cloud', with per-layer timing and runtime logs, and a second job uploads input data and downloads outputs. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a Qualcomm MyAccount plus an API token taken from Account then Settings, with no payment step described in the getting-started docs, so no card and no hold on that path. Whether the MyAccount signup asks for a phone number is not stated in the evidence, and debit and prepaid acceptance are not stated because nothing is charged
- interface: cli
- limits note: Qualcomm publishes no request rate, job count, queue depth or model size ceiling beyond a note that models above 2 GB may fail to compile, so the constraint that fails first cannot be named from the documentation.
- binding note: the same as limits note
- interface detail: CLI: the `qai-hub` command line tool, documented at workbench.aihub.qualcomm.com/docs/hub/cli.html, plus a Python client and API documented at docs/hub/api.html.
- tooling: the `qai-hub` Python client, installed with `pip3 install qai-hub`, which also provides the `qai-hub` command line tool.
- composes with: It chains with the Qualcomm Device Cloud record already in documented records: AI Hub gives the compile and profile loop on hosted silicon, Device Cloud gives an interactive session with SSH port forwarding on a Snapdragon X Elite machine. Together they cover model work and application work without owning a phone.
- reliability: no reliability event recorded
- notes: The one gap is the ceiling: 'completely free' with no published quota means the honest reading is free until Qualcomm changes it, and a heavy user could discover a limit the docs never state. The device list page warns that some entries are proxy devices that 'do not host the actual device', so per-model metrics may be modelled rather than measured; the inference-job path explicitly runs on real hardware, and that is the path this finding rests on. No probe was run against the API, so the verdict is qualifies-with-caveat rather than qualifies: the free claim is a vendor FAQ sentence, and the row would need an account, a token and one inference job before it could be called measured.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: free-forever
  - facets.shape.gpu_class: Qualcomm Hexagon NPU / Adreno GPU on hosted Snapdragon devices
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: 'Qualcomm AI Hub Workbench, our platform, is currently completely free to use', quoted, in the fees question
  - [1] 2026-10-22: 'submit an inference job, running your compiled model on a real device hosted in the cloud and analyze the performance', quoted
  - [2] 2026-10-22: access is a Qualcomm MyAccount plus an API token from Account then Settings, with no payment step described
  - [1] 2026-10-22: compilation limits: 'The model is large (i.e. > 2GB)' is one named cause of a failed compile
  - [3] 2026-11-03: the docs index lists a command line tool | capture: sha256:13f4eda68793df91d2a698653c15baf6cc66cd0a9db30e743e5b1e1d922c7c5a | quote: - [Command line tool](https://workbench.aihub.qualcomm.com/docs/hub/cli.html)
  - [3] 2026-11-03: the docs index points to an API documentation | capture: sha256:13f4eda68793df91d2a698653c15baf6cc66cd0a9db30e743e5b1e1d922c7c5a | quote: - Search our [API documentation](https://workbench.aihub.qualcomm.com/docs/hub/api.html#hub-api) for usage information.
  - [4] 2026-11-04: the provider documents a command line tool | capture: sha256:1cd0861f7e4dae4ebe713bc189fe9d52e95daf57e61f9158cfdfb499330aca27 | quote: Qualcomm® AI Hub Workbench comes with a command line tool which you can use to do the following:
  - [5] 2026-11-04: the Python client installs as qai-hub | capture: sha256:ab0f4d4d99ca091732e07d9ac3a0305b64610bd104036ba1560d3c0f62c71815 | quote: pip3 install qai-hub
- sources:
  - [1] https://workbench.aihub.qualcomm.com/docs/hub/faq.html
  - [2] https://workbench.aihub.qualcomm.com/docs/hub/getting_started.html
  - [3] https://workbench.aihub.qualcomm.com/docs/
  - [4] https://workbench.aihub.qualcomm.com/docs/hub/cli.html
  - [5] https://workbench.aihub.qualcomm.com/docs/hub/install.html

## Qualcomm Device Cloud

- `compute/qualcomm-device-cloud` | qualifies-with-caveat | evidence reported | binding volume-quota | category dev environment
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:12.410Z (live) | stale on 2026-11-19
- url https://qdc.qualcomm.com/support/faq
- free tier: Free to use: create a Qualcomm ID, then request free minutes for a device and run interactive sessions or automated jobs on real devices, with SSH port forwarding into the session. The FAQ states new users get free pre-provisioned minutes on Snapdragon X Elite on first login for a limited time. A third-party guide states each device can be accessed free for up to 5,000 minutes. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-quota
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: the FAQ states no egress allowance and no overage price | metered: no | source: [1]
- identity: email
- interface: ssh, rest
- limits:
  - volume-quota (binding): minutes are a pooled allocation requested per device, and an organisation's minutes are shared across its users, so the 5,000-minute figure is per device rather than per account and does not grow with the number of machines; further minutes require a reviewed request. [1]
- limits note: minutes are a pooled allocation requested per device, and an organisation's minutes are shared across its users, so the 5,000-minute figure is per device rather than per account and does not grow with the number of machines; further minutes require a reviewed request.
- binding note: the same as limits note
- interface detail: SSH to compute devices through an SSH gateway (bastion); ADB for mobile and IoT devices; a RESTful API page linked from the FAQ; the web console
- tooling: standard ssh and scp clients for compute devices and adb for mobile and IoT devices, through the SSH gateway; the RESTful API at qdc.qualcomm.com/support/api/public-api-restful; the FAQ names no CLI or SDK library
- composes with: a real Snapdragon X Elite on ARM64 with SSH is the only lane in documented records for testing ARM64 build output and on-device NPU inference without buying hardware, and it pairs with a free CI runner that cross-compiles; the minutes pool is what breaks, and it is consumed by interactive time rather than by CPU work.
- reliability: no reliability event recorded
- notes: The '5,000 minutes' figure is third-party, so the record is rung `reported` while the free-to-use fact is documented on the vendor FAQ. Device minutes are shared at organisation level, which is worth knowing before relying on the number for a long job. Not probed: no Qualcomm ID was created, so the actual allowance on first login is unverified.
- extras:
  - facets.class: perpetual-free-allowance
  - facets.free_tier_kind: recurring-quota
  - facets.shape.gpu_class: Snapdragon X Elite GPU
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Is Qualcomm Device Cloud free to use? Yes.'; usage requires a Qualcomm ID; users 'request free minutes for a device'; minutes start counting only once test execution begins; additional minutes are provided after a reviewed request, quoted
  - [1] 2026-10-22: 'We are currently promoting Snapdragon X Elite devices, and new users get free pre-provisioned minutes on Snapdragon X Elite upon first login for a limited time', quoted
  - [2] 2026-10-22: 'each device can be accessed for free for up to 5000 minutes', and a form is used to unlock the free 5,000 minutes
  - [1] 2026-11-03: the FAQ describes access and sessions in minutes with no egress allowance or overage price | capture: sha256:02904efbb1b55692967c3ff29df0c7fa6e2df13b456da09ace80651d388554d1 | quote: Compute device: You can SSH to the device to interact with it.
  - [1] 2026-11-03: SSH access is documented | capture: sha256:02904efbb1b55692967c3ff29df0c7fa6e2df13b456da09ace80651d388554d1 | quote: Compute device: You can SSH to the device to interact with it.
  - [1] 2026-11-03: the FAQ links a RESTful API page | capture: sha256:02904efbb1b55692967c3ff29df0c7fa6e2df13b456da09ace80651d388554d1 | quote: RESTful API
  - [1] 2026-11-04: the FAQ documents SSH to compute devices, ADB for mobile and IoT devices, and links a RESTful API page | capture: sha256:02904efbb1b55692967c3ff29df0c7fa6e2df13b456da09ace80651d388554d1 | quote: Compute device: You can SSH to the device to interact with it.
- sources:
  - [1] https://qdc.qualcomm.com/support/faq
  - [2] https://github.com/globaledgesoft/Provisioning-Snapdragon-X-Elite-on-Qualcomm-Device-Cloud
