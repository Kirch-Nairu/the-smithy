# Governance

## Direction and acceptance

Kirch Ivan Balite owns human direction and final acceptance for the Smithy. The Kirion identities contribute distinct engineering lenses; they do not replace human accountability.

## Decision hierarchy

1. Safety and repository integrity.
2. Explicit user intent and accepted requirements.
3. Evidence from tests, inspection, and runtime behavior.
4. Recorded architectural and product decisions.
5. Recollection, preference, or convention.

## Change classes

| Class | Examples | Required review |
| --- | --- | --- |
| Canon | Names, identities, personas, foundational language | Kirch acceptance |
| Architecture | Boundaries, packages, persistence, deployment | Nox lens + verification |
| Behavior | Game mechanics, dialogue, application workflows | Jane lens + tests |
| Experience | Layout, motion, interaction, accessibility | Lucien lens + visual evidence |
| Operations | CI, releases, recovery, permissions | Explicit rollback path |

## Release authority

Only work merged into `main` is accepted Smithy work. Tags and releases must point to reviewed commits on `main`.
