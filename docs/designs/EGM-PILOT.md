# EGM Pilot — Big Fame Website

Status: TEST ONLY
Scope: isolated design/review gate; no production behavior changes.

## Problem
AI-assisted changes can inherit assumptions from the same long-running context. For medium or cross-file changes, we want a reviewer that can judge the implementation specification without inheriting the drafting conversation.

## Goal
Before implementation, produce a self-contained specification that a fresh reviewer can understand, challenge, and mark implementation-ready.

## Non-goals
- Do not replace tests, runtime verification, human acceptance, or Git review.
- Do not require EGM for copy-only, CSS-only, or obvious one-file fixes.
- Do not modify production code during this pilot.

## Pilot workflow
1. Elephant/drafting context writes a design under `docs/designs/`.
2. Goldfish/fresh context receives only the design plus repository source needed to validate concrete claims.
3. Review gates:
   - Comprehension: explain intended behavior and boundaries from the spec alone.
   - Critic: identify missing edge cases, dependencies, rollback concerns, and contradictions.
   - Readiness: verify concrete files, data/contracts, interfaces, acceptance criteria, validation, and rollback are specified.
4. Findings are resolved in the design before coding.
5. Existing implementation, tests, diff review, runtime verification, and read-back remain mandatory.

## When to trigger
Use this gate when any condition is true:
- change spans 3 or more implementation files;
- behavior crosses UI/data/API/routing boundaries;
- a requirement has meaningful ambiguity or hidden dependency risk;
- rollback would be non-trivial.

Skip it for low-risk point fixes where the overhead exceeds the likely benefit.

## Pilot acceptance metrics
For the next suitable feature compare against the normal workflow:
- requirement misunderstandings found before coding;
- implementation rework rounds;
- regressions/failures after first implementation;
- elapsed time;
- approximate agent/token overhead.

Adopt into the normal workflow only if the pilot reduces meaningful rework or catches a material pre-code defect without disproportionate overhead.

## Completion gate for a design
A design is implementation-ready only when a fresh reviewer can answer all of these without relying on prior chat:
- What user-visible outcome changes?
- What explicitly does not change?
- Which files/components are affected and why?
- What contracts/data/interfaces are involved?
- What edge cases and failure paths matter?
- How will the implementation be tested and read back?
- How can the change be rolled back safely?

## Rollback
Delete this pilot document/branch. No production code or main branch behavior depends on it.
