# Upgrading Ariad

The separate `upgrading-ariad` Agent Skill is a report-first operational specialization, not another method. Select and obtain the exact Ariad checkout/ref you intend to use; the checkout containing the skill is the candidate version. It never looks up “latest” or requires a network.

Run its read-only inventory before planning:

```console
python /path/to/candidate/skills/upgrading-ariad/scripts/audit.py /path/to/project --candidate /path/to/candidate --skill-destination .agents/skills/using-ariad
```

Add repeatable `--installed-package TARGET_RELATIVE_PATH` for runtime-native installations outside conventional probes, and select another safe target-relative `--skill-destination` when needed. Without an explicit destination, installation remains a manual choice and is not classified safe-additive. Add `--json` for stable machine-readable output. The audit inventories Git state, instruction scopes and harness support, the exact entrypoint contract, closed and digest-verified package manifests, candidate provenance and compatibility components, legacy/modular docs, repository-wide text references, semantic Ariad evidence, project-memory status vocabulary, possible intentional absences, and adjacent project documentation. Manifest paths and repository scans do not follow symlinks. Exhaustive path inventories stay in JSON while the human report summarizes large memory collections. It writes no report or cache and changes no target files.

Review its safe-additive, manual-integration, destructive/ambiguous-denied, and retain-unchanged classes at a Navigator checkpoint. This first slice intentionally has no apply, install, migration, fetch, or background-update command. Semantic migration remains Driver/Navigator work.
