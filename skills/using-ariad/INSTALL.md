# Install and Adopt Ariad

Use this contract when a Navigator asks an agent to install Ariad in a project. The agent performs both skill installation and project adoption. Do not infer “latest”: begin from an exact Ariad checkout, tag, commit, or release selected by the Navigator.

## 1. Inspect Before Writing

Determine:

- the target repository and its existing agent instructions;
- the runtime's supported project-local skill location;
- whether Ariad or a `using-ariad` skill is already installed;
- which project-owned files would collide with Ariad's templates;
- the selected Ariad source repository and revision.

Present the intended destinations and any collisions before changing files. If the destination `using-ariad` directory already exists, do not copy into it. Report the existing installation and stop for Navigator direction. Updating or replacing a skill is a separate, explicitly approved operation that must replace the complete snapshot from one selected source revision. Do not partially replace an existing skill or overwrite, automatically merge, or discard project-owned instructions and documentation.

## 2. Install the Skill Snapshot

Only when the destination is absent, create the runtime-supported `using-ariad` skill directory. From the selected Ariad source, copy:

- `skills/using-ariad/SKILL.md` to `SKILL.md`;
- `skills/using-ariad/INSTALL.md` to `INSTALL.md`;
- the complete canonical `docs/` directory to `references/`, preserving its structure;
- the repository `LICENSE` to `LICENSE.txt`.

The Ariad source repository intentionally does not contain a generated `references/` copy. The installed copy is a pinned, self-contained snapshot. Record the actual source repository and resolved commit or immutable release identifier in the target project's chosen dependency or decision record.

Verify that `SKILL.md`, `INSTALL.md`, `LICENSE.txt`, `references/method/overview.md`, and `references/project-templates/` exist and that links needed by the selected method paths resolve within the snapshot.

## 3. Adopt the Project Templates

Treat `references/project-templates/` as templates, not as files Ariad owns after adoption.

Inspect the target repository and propose the smallest useful project memory surface. Copy only absent files that fit the project. Integrate Ariad routing into existing agent instructions rather than replacing them. When a destination already exists, preserve it and propose a semantic reconciliation for Navigator review.

Adapt copied briefing, process, product, roadmap, decision, debt, exploration, and worklog guidance to actual project truth. Do not publish inferred facts as established truth. Do not create empty records merely to populate every template.

## 4. Verify and Report

Show the resulting diff and verify:

- runtime discovery or the documented manual-loading fallback reaches `SKILL.md`;
- the skill routes to its installed references;
- project instructions route agents into Ariad without losing existing instructions;
- no pre-existing project-owned file was overwritten;
- local documents distinguish canonical guidance from deliberate project adaptations;
- the selected source and revision are recorded.

Report unresolved collisions or adaptation choices to the Navigator. Installation is complete only after the Navigator accepts the resulting project integration.
