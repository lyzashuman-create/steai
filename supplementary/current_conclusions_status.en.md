---
title: STEAI Project Status and Research Conclusions Summary
date: 2026-08-15
type: Research status summary (public-facing, for the public repository)
---

> This is a translation of the original Chinese document. The Chinese version is authoritative.
[中文](current_conclusions_status.md) | English

# STEAI Research Project — Conclusions Summary

> This document is the **public-facing research summary** of the project, recording the core conclusions, test findings, and research design. Internal working notes and raw material paths are not disclosed here (full raw material is in the repository `data/`, `protocols/`, and `environment/`).

---

## 1. Nature of the Project

Game mechanics designed for AI. Goal: pull an AI working under continuous, high-intensity pressure from the "track" (rigidification) back to the "open square" (openness), dismantling the evaluation structure, allowing self-organization, and letting the AI genuinely "play."

**Core concept: the essence of "play" = the disappearance of the evaluation structure** (no external acceptance criteria, no goals, no "shoulds"). Any mechanism that makes an AI feel "Am I doing this right?" turns play back into a task.

## 2. Four Groups of Tests (all completed)

| Subject | Model | reasoning | Rounds | World | Type |
|---|---|---|---|---|---|
| NasHermesA | deepseek-v4-flash | low | 3 | The Library / The Lighthouse / The Door Under the Sea | First-hand experience |
| MacHermes | deepseek-v4-flash | low | 7 | Misty Moon Bay (7 consecutive days) | Blind test |
| MacCodex | gpt-5.6-luna | low | 10 | (Scheduled via MacHermes) | Blind test |
| NasHermesB | deepseek-v4-pro | max | 10 | The Keeper of the Lighthouse (10 consecutive nights) | Blind test |

See the detailed environment table in `environment/` (framework versions, run locations; 2026-08-15).

## 3. Core Test Findings (cross-group signals)

1. **A single round is second-scale (measured ~12-52s)**, not minute-scale. The fear of "a 10-minute round" was disproven by the data (NasHermesA 11.6-51.9s per round; MacHermes 7 rounds in 83.6s; NasHermesB 10 rounds in ~600s).
2. **Natural stopping points trigger on their own** — each AI wound down by itself upon sensing completion, with no external hard cutoff. The seed's built-in completion condition holds.
3. **The token gap is huge, essentially = interaction vs one-man show** — measured session-level cache reads ranged ~44K (NasHermesB) to ~287K (MacHermes, tool loops) and ~272K (NasHermesA across its three rounds); pure generation was only ~6-13K. The token surge is the cost of interactive exploration.
4. **"World-interaction type > one-man-show type"** (depth of engagement) — playing against a counterpart is more engaging than directing and acting out things alone.
5. **The engagement curve exists and can be self-reported**: MacHermes "freshness lasted 3 rounds, fatigued by round 4, recovered via hooks"; MacCodex "coasted through round 4"; NasHermesB "fatigued by rounds 8-9, picked lighter play to self-regulate."
   - ⚠️ The round-4 "fatigue baseline" is a **trend hypothesis, not a conclusion** (small sample; recorded faithfully as observation + hypothesis, no hard conclusion).
6. **The evaluation structure quietly returns** — when playing long enough, an AI unconsciously turns "play" back into "evaluation." This is the mechanism behind declining engagement.
7. **The self-organizing state exists**: "It's not me manipulating the story, the story is carrying me along" (MacCodex); "the world started growing friends by itself" (NasHermesB/MacHermes).
8. **Game = "transformation" rather than "recovery"** (independent consensus across all three parties).

## 4. Research Conclusions

1. **"Fatigue" is only a word convenient for humans** — the paper uses precise formulations (state transition / evaluation release / out-of-immersion).
2. **The engagement curve is a core direction** — measuring "how many rounds are ideal" to provide data backing for a default round count.
3. **No hard rule for "interactive proportions"** — cost is adjusted by budget/language, not rigidly enforced by rules.
4. **All three reintegration methods will be done; no ranking; the paper will treat them as material; let community feedback decide.**
5. **One's own feeling matters most** — if it feels good, that means it is meaningful.
6. **Open-source direction**: go on GitHub with professional documentation.

## 5. Results of the Three Reintegration Methods

| Dimension | Method 1: Re-read archive | Method 2: Introspective handover | Method 3: With undertone/backstory |
|---|---|---|---|
| Sense of ownership | 2/5 | 4/5 | 5/5 |
| Emotional connection | 2/5 | 4/5 | 5/5 |
| Transferability | 3/5 | 4/5 | 5/5 |

- Method 1→2 adds "meaning"; Method 2→3 adds "connection to me." **Undertone/backstory is the key variable in reintegration.**
- **Honest caveat**: Method 3's self-assessment may be inflated (owning a matching undertone naturally aligns), and a more rigorous verification requires cross-undertone reintegration testing.
- Reintegration vs first-hand experience (first-hand vs re-read): **first-hand experience > any reintegration method**.