# Contributing to the Smithy

The Smithy accepts work that is bounded, reviewable, and supported by evidence.

## Working agreement

1. Start from an issue, decision record, or clearly stated problem.
2. Keep each pull request focused on one capability or concern.
3. Separate implementation from verification when practical.
4. Document assumptions, failure modes, and deferred work.
5. Never describe unverified behavior as complete.

## Commit convention

Use Conventional Commit prefixes:

- `feat` — user-visible capability
- `fix` — defect correction
- `docs` — documentation or canon
- `test` — automated or manual verification
- `refactor` — behavior-preserving restructuring
- `chore` — tooling, maintenance, or repository operations
- `art` — original visual or audio assets

## Pull request evidence

Every pull request must state:

- what changed;
- why the change is needed;
- how it was verified;
- known limitations or follow-up work;
- whether canon, interface, data, or deployment behavior changed.

## Review lenses

- **Kirch:** intent, sequencing, and final acceptance.
- **Jane:** application behavior, integration, and useful implementation.
- **Lucien:** interaction, hierarchy, accessibility, and visible state.
- **Nox:** boundaries, data integrity, failure behavior, and recovery.
