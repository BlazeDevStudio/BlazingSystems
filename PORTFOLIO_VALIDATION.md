# Portfolio Validation Record

This document defines the validation boundary of the current public BlazingSystems portfolio. Status applies only to the sanitized public editions currently published.

## Validation Levels

| Level | Meaning |
|---|---|
| **Working build** | Runs in the stated demonstration environment |
| **Source-ready** | Coherent implementation exists; target hardware/platform validation remains |
| **Lab** | Active implementation with identified validation work |
| **Experimental** | Feasibility, compatibility, alpha or prototype work |
| **Archive** | Historical engineering record rather than a maintained release |

## Projects

| Project | Public status | Validation boundary |
|---|---|---|
| Marine Operations Logbook | Demonstration build | Browser-local workflow with synthetic data; not an operational survey system |
| Draft Reading Trainer | Working browser build | Standalone generic training exercise |
| Daily Operations Update | Demonstration build | Browser reporting demo using synthetic records |
| BlazeSystems Arcade | Demonstration build | Original public mini-game/launcher edition; commercial ROMs and third-party payloads excluded |
| Last Stand | Working browser build | Dependency-free HTML5 strategy game |
| ESP8266 Thermostat | Source-ready | Exact-board, sensor-disconnect, relay and endurance validation remain |
| Captive Portal UI Demo | Demonstration build | Standalone interface study with no production hotspot backend |

## Labs

| Project | Public status | Remaining validation |
|---|---|---|
| Blaze Pisonet Universal | Lab / source-ready | ESP8266 compile, GPIO behavior, persistence, recovery and multi-device hardware tests |
| Blaze Pisonet Timer | Lab / recovered derivative | Public edition uses generated first-boot setup values; exact-board compile, relay/coin/display behavior, persistence and endurance tests remain |
| BlazeFM | Lab / source-ready | Gradle build, Android storage-permission regressions, device validation and signed packaging |
| MachDownload | Lab / working alpha | Wider Windows, CDN, proxy, authentication and release-build testing |
| Local AI Studio | Lab / engine prototype | Model-dependent generation and performance testing with separately supplied model weights |
| OpenWrt VLAN Deployment Study | Lab / documentation | Target-router deployment and rollback validation with sanitized configuration |
| ESPHole | Lab / source-ready | Generated first-boot credentials are used in the public Lab edition; exact-board DNS/NAPT, recovery and multi-client testing remain |
| BlazeTube ESP8266 | Lab / source-ready | No bundled API key; compile, NAPT, service integration and multi-client validation remain |

## Experiments

| Project | Current public status | Validation boundary |
|---|---|---|
| BlazeAPK | Beta 0.6 experiment | Parser/runtime research; not Android Runtime/ART |
| BlazeJ2ME | v1.6 experiment | Java ME compatibility remains application-dependent |
| TokenLauncher | Android + ESP32 prototype | Security, kiosk/device-owner lifecycle and hardware testing remain |
| ESP8266 controller studies | Prototype | Exact-board and load validation remain |
| ESP8266 Arcade public shell | Experimental derivative | Captive/NAPT shell only; commercial ROM/emulator payloads excluded |
| ESPHole versioned branch | Experimental firmware history | Numbered releases preserve regression work; physical NodeMCU testing remains authoritative |
| BlazePwifi | 0.1.0-alpha.1 | Static/integration-oriented reconstruction; OpenWrt target, coin pulse timing and recovery require hardware validation |
| EasyMode for OpenWrt | 5.0.0-alpha.1 | Static tested; hardware verification required across supported device classes |

## Forked / Upstream Work

Forked or third-party projects are kept separate from original BlazingSystems work. Upstream attribution and licensing must remain intact, and fork status does not imply original authorship or production validation.

## Publication Boundary

Public editions use generic interfaces, fictional or placeholder data, and exclude production credentials, raw router backups, private keys, employer/client records, commercial ROM/APK payloads and proprietary operational datasets.

Validation is intentionally separated into source/static checks, controlled functional tests, target-platform testing, and real hardware/deployment testing. A project is not promoted merely because it compiles or opens successfully.
