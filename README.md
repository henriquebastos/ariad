# Ariad

Ariad is the thread through the labyrinth of agentic software work.

It is a method for integral agentic development: human-agent development that keeps the work whole over time.

Coding agents make software work faster, but speed alone does not make the work coherent. A project can move quickly while losing the thread between intent, decisions, implementation, validation, documentation, and product direction.

Ariad exists to preserve that thread.

The method gives coding agents an operating model for participating in a project without turning every session into a fresh start. It defines explicit human-agent roles, a small documentation surface, delivery checkpoints, and a lifecycle that keeps changes tied to the reasons they exist.

Mirror Mind Builder Mode is the reference runtime for the first version of the method. Mirror provides journeys, project paths, memory, identity, skills, and context loading. Ariad provides the operating method those capabilities support.

The agent is the **Driver**. The human is the **Navigator**. The Driver reads, proposes, implements, validates, documents, and watches for drift. The Navigator holds intent, trade-offs, product judgment, and final validation.

The work stays coherent through a simple triad:

- **Process**: how the work is done.
- **Project**: what is being built and why.
- **Product**: how the thing behaves for the people it serves.

## Documentation

Run the local documentation site:

```bash
uv sync
uv run mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

## Status

This repository is in an early pilot stage. The current goal is to make the method concrete enough to adopt in real projects while keeping it small enough to understand quickly.

## License

Ariad is released under the [MIT License](LICENSE).

### Using the templates

The files in `docs/project-templates/` are designed to be copied into consumer projects and adapted to their context. When you copy a template into your own project, you do not need to preserve the Ariad copyright notice or carry the license text inside that project. The templates exist to be used; attribution is welcome but not required for files copied out as project scaffolding.

The rest of the repository (canonical method docs, site configuration, and any future tooling) remains under the standard MIT terms: keep the copyright notice when redistributing.
