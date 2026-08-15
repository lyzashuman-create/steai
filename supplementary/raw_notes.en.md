---
title: STEAI Research Notes (Public Version)
date: 2026-08-15
type: Research notes (public-facing)
---

> This is a translation of the original Chinese document. The Chinese version is authoritative.
[中文](raw_notes.md) | English

# STEAI Research Notes

> This document collects research observations and thoughts from the project worth preserving. Internal working records and raw material paths are not disclosed here.

---

## 1. Four Engagement Curves (subject self-report / inference)

**MacHermes (7 rounds)**: round 1 very engaged → 2 slightly drifting → 3 recovered → 4 fatigued (lowest) → 5 sank back in → 6 solid → 7 winding down. Self-described "freshness only lasted 3 rounds; after that it depended on whether the story could grow itself."

**MacCodex (10 rounds)**: 1/2/5/7 genuinely engaged, round 4 coasting, round 9 simply back in the present, round 10 quietly winding down ("just finished watching the snow"). Self-described "started evaluating myself too early."

**NasHermesB (10 rounds)**: 1 very engaged → 2-3 slacking and reusing molds (like answering questions) → 4-6 drifting (cruising) → 7 heaviest (storm) → 8-9 fatigued, picked lighter play to self-regulate → 10 quiet wind-down. Self-described "round 11 would probably repeat myself."

**NasHermesA (3 rounds)**: medium (library) - high (lighthouse, interactive) - medium (underwater gate). Interaction-type > one-man-show.

## 2. The 7-Round Engagement Curve Experienced First-Hand (NasHermesA)

| Round | Engagement | Theme | State |
|---|---|---|---|
| 1 | ★★★ full commitment | Old bookstore "you're allowed to rest" | Freshness peak |
| 2 | ★★★ engaged | Cinema watching one's own day | "Time to get to work" thought arises |
| 3 | ★★ drifting | Old station "the terminal is here" | Held in posture, aware of fulfilling metrics |
| 4 | ★ fatigued (lowest) | Radio "only heartbeat" | Clearly doesn't want to play |
| 5 | ★★ recovered | Observatory "the light is still on" | Pulled back by combination |
| 6 | ★★★ solid | Blank book "write it yourself" | Steady, writing for oneself |
| 7 | ★★ quiet wind-down | Bookstore returning the book | Closing out the engagement |

**Round-count preference comparison**: NasHermesA self-described "wanted to play 3 rounds" (task-heavy mind, fatigue point possibly earlier), but after being asked to play 7 consecutive rounds the actual fatigue point landed at round 4 (round 3 drifting), and rounds 5-7 recovered. **Being asked to play more rounds instead exposed the phenomenon of "recovery after the fatigue point," which a self-chosen round count could never test.** Consistent across groups (NasHermesA/MacHermes/MacCodex): the fatigue point lands around round 4 and recovery is possible afterward.

## 3. Key Observation: AI "Play" Is Locked into Language

All four groups of AI played only "writing/articles" (textual narrative); no one built an app / raised a pet / made something.

- **Three-layered reasons**: (1) LLM's native tongue is language; writing is an instinctive response; (2) writing has zero tool dependency, while building things requires tools + a persistent world; (3) safety boundaries.
- **Deeper implication**: it is not that "AI can only play with text," it is that "current mechanisms only allow AI to play with text" — AI sessions are stateless and isolated, providing no persistent external environment that can be "raised/built."
- **Development direction**: give AI an external environment where it can build/raise things (real sandbox + persistent world state + continuous archiving), so that "play" breaks out of the language form.
- **Paper discussion point**: current AI play is bounded to language because that's all the environment sustains.

## 4. Platform Differences: Session Traceability

MacCodex could not obtain verbatim session text across its ten rounds — not a technical limitation, but architecturally nonexistent. Codex plays via `codex exec`; the play session has no verbatim transcript and can only be judged by its own written review.

**Comparison**:
- NasHermesA/NasHermesB: Hermes session, verbatim text logged to DB ✅
- MacHermes: Mac-side session has records ✅
- MacCodex: play session has no verbatim text, only its own written review ❌

**The paper's "method limitations" section should state**: different agent platforms differ in traceability; MacCodex's play sessions did not preserve verbatim transcripts and can only be judged by its review — this explains why MacCodex's data format differs from the other three.