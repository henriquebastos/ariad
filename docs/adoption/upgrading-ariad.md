# Upgrading Ariad

An Ariad upgrade is performed by an agent against an exact candidate checkout or immutable release selected by the Navigator. The candidate's `skills/upgrading-ariad/SKILL.md` is the operating contract.

The Driver first runs a read-only audit. It inventories target and candidate repository state, candidate identity, the installed `using-ariad` snapshot and provenance, project-owned Ariad documents, local adaptations, legacy paths, instruction scopes, and collisions. It compares the complete installed and candidate skill snapshots separately from semantic changes to project-owned documents.

Every proposed operation is classified as safe additive, manual integration, whole-snapshot replacement blocked pending explicit Navigator approval, destructive or ambiguous and therefore denied, or retain unchanged. The Driver presents evidence and stops for Navigator approval before writing.

An approved package update re-verifies candidate identity, replaces the complete installed skill snapshot from that selected source, and records the resulting provenance. It never merges package files in place. Project-owned documents are migrated separately and semantically: local truth, decisions, policy, and history are preserved rather than overwritten by newer templates.

There is intentionally no automatic fetch, “latest” lookup, background update, generic merge, or unattended migration. Agent judgment and Navigator review are the upgrade mechanism.
