# BlazingSystems — Repository Allocation and Migration Status

**Snapshot:** 2026-10-29. Account: [BlazingSystems](https://github.com/BlazingSystems).  
**Scope:** 20 repositories accessible to the connected GitHub installation; this is not an assertion that no other private/inaccessible repositories exist. All were visible as public and writable at discovery.  
**Safety:** Non-destructive migration branches and draft PRs only. Source repo history and original development PRs remain intact. No production release or financial/hardware gate is changed.

## Official portfolio roles

- [BlazingSystems](https://github.com/BlazingSystems/BlazingSystems): profile and navigation.
- [BlazingSystems-Projects](https://github.com/BlazingSystems/BlazingSystems-Projects): curated demonstrations.
- [BlazingSystems-Labs](https://github.com/BlazingSystems/BlazingSystems-Labs): engineering validation-stage work.
- [BlazingSystems-Experiments](https://github.com/BlazingSystems/BlazingSystems-Experiments): ongoing experiments and **original active draft PRs**.
- [BlazingSystems-Archives](https://github.com/BlazingSystems/BlazingSystems-Archives): sanitized historical work.
- [Forked-Projects](https://github.com/BlazingSystems/Forked-Projects): third-party attribution and research.

## Dedicated destination allocation

| Project | Existing destination | Exact origin checkpoint | Migration stage | Latest controlled operation |
| --- | --- | --- | --- | --- |
| Project Phoenix | [CoinOperatedEcosystem](https://github.com/BlazingSystems/CoinOperatedEcosystem) | Experiments OpenWrt/Android/Windows/ESP sources, many active stacked draft PRs | STRUCTURE_CREATED | [Draft PR #1](https://github.com/BlazingSystems/CoinOperatedEcosystem/pull/1): documented subsystem folders; no application source |
| ThreadHarbor | [ThreadHarbor](https://github.com/BlazingSystems/ThreadHarbor) | [Experiments PR #209](https://github.com/BlazingSystems/BlazingSystems-Experiments/pull/209), `a5ef1e1c959da06674540ffcd88c89fe01ee4261` | SOURCE_STAGED | [Draft PR #1](https://github.com/BlazingSystems/ThreadHarbor/pull/1): 27/27 source Git blobs identical; [destination CI passed](https://github.com/BlazingSystems/ThreadHarbor/actions/runs/40639809082); emulator/device acceptance pending |
| BlazeFM | [BlazeFM](https://github.com/BlazingSystems/BlazeFM) | `BlazingSystems-Labs/android/blazefm/` @ `5d8e4f1d95b6bfc551996634df9c6f7b86af56b4` | SOURCE_STAGED | [Draft PR #1](https://github.com/BlazingSystems/BlazeFM/pull/1): 109/109 exact source blobs and modes; [Android CI passed](https://github.com/BlazingSystems/BlazeFM/actions/runs/40641252842); hardware/policy acceptance pending |
| BlazeNetMonitor | [BlazeNetMonitor](https://github.com/BlazingSystems/BlazeNetMonitor) | [Experiments draft PR #206](https://github.com/BlazingSystems/BlazingSystems-Experiments/pull/206), `3f762cdf436f2c996eb39088a33468e85c23143a` | SOURCE_STAGED | [Draft PR #1](https://github.com/BlazingSystems/BlazeNetMonitor/pull/1): 40/40 exact source blobs/modes (including binary icon); [Windows CI passed](https://github.com/BlazingSystems/BlazeNetMonitor/actions/runs/40641677234); installer/signing and physical Windows acceptance pending |
| Blaze Ultimate Optimizer | [Blaze-Ultimate-Optimizer](https://github.com/BlazingSystems/Blaze-Ultimate-Optimizer) | `BlazingSystems-Labs/BlazeUltimateOptimizer/` | NOT_STARTED | Preview source and binary assets need provenance/license/security review |
| EasyMode for OpenWrt | [EasyMode](https://github.com/BlazingSystems/EasyMode) | `BlazingSystems-Experiments/experiment/openwrt/easymode-project/`; both main and v7 production variants | BLOCKED — authoritative revision & package inventory | Source main has 304 files / 39.3 MB; `easymode-v7-production@f79abca8183bdf0ad2847cddbc8d5989e656025d` has 519 / 58.1 MB. Release/firmware assets and hardware-specific gates require review before copying. |
| Blaze MCU Studio | [BlazeMCUstudio](https://github.com/BlazingSystems/BlazeMCUstudio) | [Experiments draft PR #211](https://github.com/BlazingSystems/BlazingSystems-Experiments/pull/211), `ae5d53df408ad277c030251ac3f8cfa4b96a479c` | SOURCE_STAGED | [Destination draft PR #1](https://github.com/BlazingSystems/BlazeMCUstudio/pull/1): 72/72 exact source blobs also match updated upstream PR #211; Windows regression correction `8ee37ff62f93cf1a22e7a97ac73baa65ac2a1ddd`, ESP8266/ESP32 compile passed; updated full CI pending; physical hardware remains unverified |
| Blaze Unified Electronics Simulator | [BlazeUnifiedElSim](https://github.com/BlazingSystems/BlazeUnifiedElSim) | Existing separately owned development, exact original source revision to be located | NOT_STARTED | Repository confirmed accessible; initial README only; no conflicting source migration performed |
| Blaze Messenger destination candidate | [BlazeMessenger](https://github.com/BlazingSystems/BlazeMessenger) | LAN Messenger and ConnectIT maintain independent development and must not be conflated | BLOCKED — product authority | Repository confirmed accessible but README-only; whether it is for LAN Messenger or ConnectIT is not established by its name |

### Destinations not visible under their expected names

The connected repository list does not contain exact-name standalone destinations `LAN-Messenger`, `ConnectIT`, `Blaze-Gen2-Portable-Studio`, or `BlazeDroid`. The existing [BlazeMessenger](https://github.com/BlazingSystems/BlazeMessenger) must **not** be assumed to represent LAN Messenger and ConnectIT simultaneously: these are separate projects with separate owners. Their source currently remains in Experiments PR branches. Source for other apps must be resolved without repurposing `AndroidDevel`, `BlazeExeCute`, or `BlazeWeb` without evidence.

### Other existing repositories

[AndroidDevel](https://github.com/BlazingSystems/AndroidDevel), [BlazeExeCute](https://github.com/BlazingSystems/BlazeExeCute), [BlazeWeb](https://github.com/BlazingSystems/BlazeWeb), [samdenty-esp32-port](https://github.com/BlazingSystems/samdenty-esp32-port) and [BlazeMCU](https://github.com/BlazingSystems/BlazeMCU) remain existing accessible repositories, distinct from [BlazeMCUstudio](https://github.com/BlazingSystems/BlazeMCUstudio). This migration does not rename, repurpose, archive or delete them.

## Phoenix safety gates

CORE ledger durability, signed payment validation, crash-atomic accounting, committed receipt replay and strict controller admission remain NO-GO pending independent proof. RENTAL authenticated-lease persistence, PISONET serial identity/reconnect and Authenticode signing, ESP firmware fail-closed relay/rollback behavior, cross-subsystem contracts and QA acceptance all require exact-head native or hardware evidence. **The Phoenix structure PR is not a source migration or a release.**

## CI strategy and preservation

- Exact-head source and status must be established before copying code and workflows.
- New destination CI must refer to new paths. Compare old/new required checks before retiring old triggers.
- Original Experiments signing, publishing, heavy test and hardware-related workflows are untouched.
- ThreadHarbor (27 files), BlazeFM (109 files), and BlazeNetMonitor (40 files) have exact-blob source migrations and successful native CI runs on their verified migration heads. Blaze MCU Studio (72 files) has source integrity verified and new full-fidelity CI pending. Hardware, GUI/device and release-signing acceptance remain outstanding.
- No user secrets, signing keys, historical customer data or production artifacts are part of these migration PRs.

## Minimum acceptance before marking VERIFIED

Source commit and dependency stack documented; 100% file integrity checked; necessary build/test paths work; required native and integration checks pass at the destination head; CI artifacts proven tied to the same SHA; independent QA and product-specific release controls satisfied. Any missing evidence remains **SOURCE_STAGED**, **STRUCTURE_CREATED**, **NOT_STARTED** or **BLOCKED**.

**This file is an allocation snapshot, not a new global project authority or replacement for existing historical handovers.**
