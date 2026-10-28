# BlazingSystems — Repository Allocation and Migration Status

**Snapshot:** 2026-10-28. Account: [BlazingSystems](https://github.com/BlazingSystems).  
**Scope:** 17 repositories accessible to the connected GitHub installation; this is not an assertion that no other private/inaccessible repositories exist. All were visible as public and writable at discovery.  
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
| ThreadHarbor | [ThreadHarbor](https://github.com/BlazingSystems/ThreadHarbor) | [Experiments PR #209](https://github.com/BlazingSystems/BlazingSystems-Experiments/pull/209), `a5ef1e1c959da06674540ffcd88c89fe01ee4261` | SOURCE_STAGED | [Draft PR #1](https://github.com/BlazingSystems/ThreadHarbor/pull/1): 27/27 source Git blobs verified equal; CI and device acceptance pending |
| BlazeFM | [BlazeFM](https://github.com/BlazingSystems/BlazeFM) | `BlazingSystems-Labs/android/blazefm/` on Lab main | NOT_STARTED | Full Android source located, migration/integrity and CI pending |
| BlazeNetMonitor | [BlazeNetMonitor](https://github.com/BlazingSystems/BlazeNetMonitor) | [Experiments draft PR #206](https://github.com/BlazingSystems/BlazingSystems-Experiments/pull/206), `3f762cdf436f2c996eb39088a33468e85c23143a` | NOT_STARTED | Source is PR-head-specific; signed/installer checks pending |
| Blaze Ultimate Optimizer | [Blaze-Ultimate-Optimizer](https://github.com/BlazingSystems/Blaze-Ultimate-Optimizer) | `BlazingSystems-Labs/BlazeUltimateOptimizer/` | NOT_STARTED | Preview source and binary assets need provenance/license/security review |
| EasyMode for OpenWrt | [EasyMode](https://github.com/BlazingSystems/EasyMode) | `BlazingSystems-Experiments/experiment/openwrt/easymode-project/` | NOT_STARTED | Existing source and release variants need exact ref/installer reconciliation |
| Blaze MCU Studio | [BlazeMCU](https://github.com/BlazingSystems/BlazeMCU) **candidate only** | [Experiments draft PR #211](https://github.com/BlazingSystems/BlazingSystems-Experiments/pull/211), `581ff6f9f63e6120ebcb206540598cd4f898fec0` | BLOCKED — exact destination confirmation | Do not assume BlazeMCU naming signifies Studio source authority |

### Destinations not visible under their expected names

The connected repository list does not currently contain standalone repositories named `LAN-Messenger`, `ConnectIT`, `Blaze-Gen2-Portable-Studio`, or `BlazeDroid`. These are **access/naming unresolved**, not permission to create replacements or silently move them into `AndroidDevel`, `BlazeExeCute`, or `BlazeWeb`. Their ongoing source remains in Experiments draft branches until independently reconciled.

### Other existing repositories

[AndroidDevel](https://github.com/BlazingSystems/AndroidDevel), [BlazeExeCute](https://github.com/BlazingSystems/BlazeExeCute), [BlazeWeb](https://github.com/BlazingSystems/BlazeWeb), [samdenty-esp32-port](https://github.com/BlazingSystems/samdenty-esp32-port) and [BlazeMCU](https://github.com/BlazingSystems/BlazeMCU) remain existing accessible repositories. This migration does not rename, repurpose, archive or delete them.

## Phoenix safety gates

CORE ledger durability, signed payment validation, crash-atomic accounting, committed receipt replay and strict controller admission remain NO-GO pending independent proof. RENTAL authenticated-lease persistence, PISONET serial identity/reconnect and Authenticode signing, ESP firmware fail-closed relay/rollback behavior, cross-subsystem contracts and QA acceptance all require exact-head native or hardware evidence. **The Phoenix structure PR is not a source migration or a release.**

## CI strategy and preservation

- Exact-head source and status must be established before copying code and workflows.
- New destination CI must refer to new paths. Compare old/new required checks before retiring old triggers.
- Original Experiments signing, publishing, heavy test and hardware-related workflows are untouched.
- The ThreadHarbor preview source's 27 Git blob SHAs match exactly, with a new root-aware independent CI workflow pending real run validation.
- No user secrets, signing keys, historical customer data or production artifacts are part of these migration PRs.

## Minimum acceptance before marking VERIFIED

Source commit and dependency stack documented; 100% file integrity checked; necessary build/test paths work; required native and integration checks pass at the destination head; CI artifacts proven tied to the same SHA; independent QA and product-specific release controls satisfied. Any missing evidence remains **SOURCE_STAGED**, **STRUCTURE_CREATED**, **NOT_STARTED** or **BLOCKED**.

**This file is an allocation snapshot, not a new global project authority or replacement for existing historical handovers.**
