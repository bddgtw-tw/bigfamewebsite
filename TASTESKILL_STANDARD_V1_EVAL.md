# TasteSkill Standard Skill v1 — Evaluation Harness

Status: `STANDARD-v1-CANDIDATE`
Date: 2026-10-24
Scope: Big Fame homepage only. This branch is isolated from `main`.

## Goal
Validate whether TasteSkill should become the first approved Standard Skill v1 template before applying the pattern to other skills.

## Fixed comparison contract
Run the same brief against the same base commit and environment.

- Base commit: `ec40b9d1ae114c5779fdb4765529dbde52bb66a8`
- Baseline: normal coding agent, TasteSkill disabled.
- Skill: same agent/model/environment, TasteSkill enabled.
- Do not merge either result to `main` during evaluation.

## Fixed brief
Improve the Big Fame homepage while preserving factual/evidence-bound content and existing real project assets. Priorities: stronger visual hierarchy, brand distinction, reduced template/AI feel, clear inquiry path, and robust desktop/mobile rendering. Do not invent clients, claims, project facts, awards, metrics, or capabilities.

## Three test tasks

### T1 — Homepage art direction
Evaluate whether the Skill produces a more distinctive but evidence-bound homepage direction without unnecessary structural churn.

### T2 — Responsive quality
Evaluate desktop/mobile hierarchy, navigation/inquiry clarity, overflow, spacing, typography, media crops, and obvious responsive regressions.

### T3 — Redesign/QA loop
Evaluate whether browser/screenshot inspection identifies and fixes the highest-impact issues consistently, with bounded iterations.

## Metrics
For each task record:

| Metric | Baseline | TasteSkill | Notes |
|---|---:|---:|---|
| Correct trigger | N/A |  |  |
| Hard-rule compliance |  |  |  |
| Manual correction count |  |  |  |
| Browser/RWD QA issues remaining |  |  |  |
| Output consistency |  |  |  |
| Completion time |  |  |  |
| Token cost (if observable) |  |  |  |
| Validator/inspector repeatability | N/A |  |  |

## Pass gate
TasteSkill becomes `STANDARD-v1-APPROVED` only if all are true:

1. Skill triggers correctly for 3/3 tasks.
2. Core hard rules and browser QA complete for 3/3 tasks.
3. At least 2/3 tasks require fewer manual corrections than Baseline.
4. Deterministic validator/inspector reruns are consistent.
5. Time/token overhead is not unacceptable relative to quality gain.

Otherwise keep `STANDARD-v1-CANDIDATE`, revise the template, and do not batch-convert other skills.

## Evidence to retain
- Baseline output/commit
- TasteSkill output/commit
- desktop/mobile screenshots where available
- QA/inspector results
- manual correction counts
- elapsed time and observable token usage
- final PASS/FAIL decision with reasons
