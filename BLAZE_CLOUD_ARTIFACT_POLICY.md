# BLAZE SYSTEMS CLOUD ARTIFACT POLICY

**Owner:** Blaze Systems · **Effective:** 2026-10-26 · **Policy ID:** BLAZE-CLOUD-ARTIFACT/1

GitHub is the **source-code authority**. A designated private Google Drive project mirror stores large build artifacts, recovery snapshots, previews, firmware images, testing evidence, and release backups. Keep source code, branches, issues, PRs, small tests and documentation in GitHub; do not upload unnecessary large binaries to source repositories.

## Mandatory artifact rules
1. Before creating a new project mirror, consult the canonical registry and sync ledger in the owner's restricted Drive mirror. Reuse existing project identities.
2. Store builds with source repository, exact commit SHA/ref, version, platform, architecture, release channel, original filename, byte size, SHA-256, build verification, and access classification. Preserve the original artifact bytes.
3. Transfer only approved, security-reviewed and licensable artifacts. Never include secrets, private signing keys, real client/customer datasets, proprietary records or unreviewed upstream materials.
4. A transfer is **VERIFIED** only after destination identity, size and SHA-256 are independently confirmed by a remote readback. Request acceptance alone is **PARTIAL**.
5. Preserve previous versions. Never overwrite a verified release with a different build. Keep failed/incomplete transfers in the ledger as **FAILED**, **BLOCKED**, or **NOT_ACCESSIBLE**.
6. A source ZIP is not a complete Git-history backup; preserve full refs/history through a verified Git bundle when an authorized capable runner is available.
7. Drive links are restricted backup locations, **not public download promises**. Existing public release distribution may remain on GitHub.
8. Archive/mirror work does not authorize a merge, deployment, production release or hardware flash. **Phoenix Light / BlazePwifi financial admission remains NO-GO** pending its independent controller/durability, QA and physical-hardware acceptance gates. CI-only passing results do not waive these gates.
9. Never make a folder/file public, modify sharing, delete records, rewrite history, bypass quota/security controls, or register insecure unattended credentials to simplify mirroring.
10. Use a manifest-based, append-only sync ledger and exact source commit guards for incremental/idempotent snapshots. Every run records successes AND blockers.

## Official recovery control
The canonical internal files are `BLAZE_PROJECT_REGISTRY`, `BLAZE_GITHUB_INVENTORY`, `BLAZE_DRIVE_STORAGE_INDEX`, `BLAZE_ARTIFACT_MANIFEST`, `BLAZE_SYNC_LEDGER`, `BLAZE_RECOVERY_REPORT`, `BLAZE_STORAGE_POLICY`, and `BLAZE_DEVELOPMENT_HANDOVER`. These belong under the owner's approved private Drive folder `Experimental Projects/Blaze-Systems-Project-Mirror/00-MASTER-CONTROL/`. This public policy intentionally omits private Drive artifact and folder IDs.

## Reusable development-worker directive
> BLAZE SYSTEMS CLOUD ARTIFACT POLICY: GitHub is the source-code authority. The designated private Google Drive project mirror holds large builds, recovery snapshots, previews, firmware images, tests, and release backups. Every stored artifact must identify its exact source commit, version, checksum, and verification state. Never present Drive as a public mirror, overwrite verified recovery files, or waive safety NO-GO gates. Read the canonical private registry and synchronization ledger before creating new project directories. If the Drive connector is unavailable, report BLOCKED instead of pretending to upload.

**Scope:** All Blaze Systems projects. Worker acknowledgments require real observable action; a public policy file does not imply that isolated ChatGPT conversations have been notified.
