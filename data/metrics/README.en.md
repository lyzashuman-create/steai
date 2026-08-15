# data/metrics/ — raw token / duration / cost tables

> **This is a translation of the original Chinese document. The Chinese version is authoritative.**

[中文](README.md) | English

> Collection date: 2026-08-16. Sources: NAS Hermes local session store (`/opt/data/state.db` and `profiles/judy/state.db`) + Mac Hermes read-only collection over SSH bridge (Mac `~/.hermes/state.db` + `~/.codex/sessions/`). All read-only; no source was modified.

## Files

| File | Content | Granularity |
|---|---|---|
| `nashermesa_rounds.csv` ([中文](nashermesa_rounds.csv)) | NasHermesA first-hand 3 rounds (The Library / The Lighthouse / The Door Under the Sea), per-round token | **per-round exact** (3 rounds each in their own session) |
| `machermes_rounds.csv` ([中文](machermes_rounds.csv)) | MacHermes Misty Moon Bay 7 rounds | session-level (7 rounds ran continuously in 83.6s; no per-round token in the store) |
| `nashermesb_rounds.csv` ([中文](nashermesb_rounds.csv)) | NasHermesB The Keeper of the Lighthouse 10 rounds + interview | session-level (10 rounds generated continuously in one session; no per-round token) |
| `maccodex_rollouts.csv` ([中文](maccodex_rollouts.csv)) | MacCodex 10 rounds + full 08/15 rollout detail | **reconstructed** (no per-round token for the 10 rounds; only rollout aggregates) |
| `token_cost_summary.csv` ([中文](token_cost_summary.csv)) | Cross-subject comparison summary | mixed (per-subject granularity noted honestly) |
| `basic_metrics.csv` | Basic per-subject metrics (rounds/duration/tool calls) | derived (metadata) |

## Key granularity notes (honest, don't misread)

1. **There is no "per-round token" layer in the store** — each subject's N rounds were generated continuously within **one very long assistant message** in a session, not as one API call per round. Therefore:
   - Only NasHermesA's 3 rounds achieve per-round exactness, because each round was a **separate session**.
   - MacHermes' 7 rounds and NasHermesB's 10 rounds each ran continuously in a **single session**, so only session-level aggregate tokens exist; per-round split is not possible.
2. **MacCodex's 10 rounds are entirely missing** (DATA_MANIFEST gap #1): the only game-prompt rollout on 08/15 was `turn_aborted` with no `task_complete`, so no token data for the 10 rounds exists — only a reconstructed self-narrative. The rollout detail listed in `maccodex_rollouts.csv` is Mac-side game-related work (post-game interviews, interview-guide review, STEAI repo review), for reference; it is not the 10 rounds themselves.
3. **cost field**: Hermes side is an estimate from the official price snapshot (`estimated`, `cost_status=estimated`); MacCodex's OpenAI rollout does not record cost, so the cost column is naturally empty.
4. **duration**: Hermes side computed from first/last message timestamps in the session; MacCodex rollout duration is the difference of file first/last timestamps (UTC, converted to local).

## Relation to README R6 / conclusions

The "30K vs 220K, 210K cache reads, ~7K pure generation, 17-56s/round" figures cited in README R6 were earlier narrative conclusions. The measured token tables here provide machine-readable raw data alongside that narrative, but **per-round values cannot be re-derived exactly due to the granularity limits above** — README already labels them as "association, not a law". This directory presents each subject's session-level measured values honestly and does not fabricate per-round numbers.
