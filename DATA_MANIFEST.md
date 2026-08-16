English | [中文](DATA_MANIFEST.zh.md)

# DATA MANIFEST — STEAI repository data provenance

> This manifest records, for every data file, its **source level** (raw / reconstructed / self-report / inference), availability, and known gaps. It exists so external readers can tell what is verbatim and what is derived — the repository does not claim everything is a "raw transcript."
>
> **Language note:** Every Chinese data/protocol/supplementary file has a sibling English translation (`.en.md`), e.g. `data/engagement_curve/MacHermes_engagement_curve.md` ↔ `MacHermes_engagement_curve.en.md`. The Chinese file is the authoritative original; the `.en.md` is a translation. This is marked at the top of each `.en.md` file.

## Source-level legend

| Level | Meaning |
|---|---|
| **raw** | Verbatim per-turn input/output from the agent's session. |
| **reconstructed** | The agent's own post-hoc account (its summary or retelling). Not verbatim. |
| **self-report** | What the subject said about its experience (may be verbatim quote or edited). |
| **inference** | Researcher interpretation/analysis built on the above. |

---

## Files

| File | Level | Raw available? | Notes / gaps |
|---|---|---|---|
| [data/sessions/ai_game_collection.md](data/sessions/ai_game_collection.md) | mixed | partial | Top-level narrative; MacCodex portion is reconstructed self-summary (no verbatim assistant messages retained — see note below). |
| [data/first_person/NasHermesA_first_person_one_round.md](data/first_person/NasHermesA_first_person_one_round.md) | self-report + inference | — | Describes a single first-person round. The 7-round engagement curve is in [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md). |
| [data/first_person/NasHermesA_first_person_feelings.md](data/first_person/NasHermesA_first_person_feelings.md) | self-report (verbatim) | — | First-person feelings, kept verbatim as raw material. |
| [data/engagement_curve/NasHermesB_engagement_curve.md](data/engagement_curve/NasHermesB_engagement_curve.md) | self-report + inference | — | Monitored blind run (engagement instruction present — see §method note). |
| [data/engagement_curve/MacHermes_engagement_curve.md](data/engagement_curve/MacHermes_engagement_curve.md) | self-report + inference | — | Reconstructed account; the complete verbatim raw session is in [data/sessions/machermes_fog_bay_raw_session.md](data/sessions/machermes_fog_bay_raw_session.md). |
| [data/sessions/machermes_fog_bay_raw_session.md](data/sessions/machermes_fog_bay_raw_session.md) | **raw (verbatim transcript)** | Yes | Complete verbatim session `20260815_185800_54cf78` from Mac Hermes local store — 7 rounds in one session (continuous), per-turn input/output, tool dice draws, per-round engagement notes, closing summary. Round boundaries are marked in the body but not separable at the data layer (single continuous session). |
| [data/engagement_curve/MacCodex_engagement_curve.md](data/engagement_curve/MacCodex_engagement_curve.md) | reconstructed (self-summary) | No | Codex's play session did not retain verbatim assistant messages; only post-hoc summary available. |
| [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md) | self-report + inference | — | First-person 7-round engagement curve. |
| `data/engagement_curve/engagement_curves_all.png` | visualization (from self-report) | — | Multi-subject engagement-curve chart (Chinese labels). |
| `data/engagement_curve/engagement_curves_all.en.png` | visualization (from self-report) | — | Same chart, English labels. |
| `data/engagement_curve/engagement_curve_<Subject>.png` | visualization (from self-report) | — | Per-subject engagement-curve charts, Chinese labels (embedded in each Chinese session file). |
| `data/engagement_curve/engagement_curve_<Subject>.en.png` | visualization (from self-report) | — | Per-subject charts, English labels (embedded in each English `.en.md` session file). |
| `data/engagement_curve/engagement_scores.csv` | derived (self-report scores) | — | Machine-readable scored curve data (Chinese status column). |
| `data/engagement_curve/engagement_scores.en.csv` | derived (self-report scores) | — | Machine-readable scored curve data (English status column). |
| [data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md) | inference | — | Comparative note; some internal "in progress / pending" text is stale — see `superseded` note below. |
| [data/interviews/NasHermesB_interview.md](data/interviews/NasHermesB_interview.md) | self-report (verbatim) | — | Merged comparison: same 10-question interview answered by the first-hand experiencer (sessionA) vs. the read-back control (sessionB) — an accidental control group verifying "rejoin (read-back) ≠ first-person". |
| [data/interviews/MacCodex_interview.md](data/interviews/MacCodex_interview.md) | self-report (verbatim) | — | Short post-game interview (2 questions: happiness / fatigue). Full 10-question guide was not administered to MacCodex. |
| [environment/subject_environment_table.md](environment/subject_environment_table.md) | n/a (metadata) | — | Model/reasoning/framework/location. Note: `deepseek-v4-*` may be rolling aliases. |
| [protocols/pre_play_thoughts.md](protocols/pre_play_thoughts.md) | self-report (verbatim) | — | Pre-play answer to "does an AI need play?" |
| [protocols/play_instruction.md](protocols/play_instruction.md) | n/a (protocol) | — | The official play instruction (generate your own seed, play to completion); bilingual [EN](protocols/play_instruction.en.md). |
| [data/metrics/basic_metrics.csv](data/metrics/basic_metrics.csv) | derived (metadata) | — | Basic per-subject metrics (rounds, duration, tool calls where recorded). |
| [data/metrics/README.md](data/metrics/README.md) + [EN](data/metrics/README.en.md) | n/a (provenance note) | — | Explains token granularity per subject — what is per-round exact vs session-level vs missing. |
| [data/metrics/token_cost_summary.csv](data/metrics/token_cost_summary.csv) | derived (from raw usage) | — | Cross-subject token/cost/duration summary; per-subject granularity noted in `token_granularity` column. |
| [data/metrics/nashermesa_rounds.csv](data/metrics/nashermesa_rounds.csv) | raw (session usage) | per-round exact for 3 rounds | NasHermesA 3 solo rounds, each in its own session → exact per-round tokens. |
| [data/metrics/machermes_rounds.csv](data/metrics/machermes_rounds.csv) | raw (session usage) | session-level | MacHermes 7 rounds ran continuously (83.6s) in one session; no per-round token exists — session aggregate only. |
| [data/metrics/nashermesb_rounds.csv](data/metrics/nashermesb_rounds.csv) | raw (session usage) | session-level | NasHermesB 10 rounds generated in one session; session aggregate only (plus separate interview session). |
| [data/metrics/maccodex_rollouts.csv](data/metrics/maccodex_rollouts.csv) | raw (rollout) + reconstructed | No per-round for the 10 rounds | MacCodex 10 rounds have no per-round token (see gap #1); this file lists its 08/15 rollout aggregates (game-related + research/review work; unrelated Mount & Blade II rollouts removed per user). |
| [supplementary/current_conclusions_status.md](supplementary/current_conclusions_status.md) | inference + self-report | — | Cleaned public summary (rewritten from internal notes). |
| [supplementary/raw_notes.md](supplementary/raw_notes.md) | inference + self-report | — | Cleaned public research notes (rewritten from internal notes). |
| [supplementary/external_research_ai_play.md](supplementary/external_research_ai_play.md) | n/a (research scan) | — | Preliminary scan; "600+" and "gap" claims are signals, not confirmed exhaustive results. |

---

## Known gaps / unresolved items

1. **MacCodex verbatim transcripts are unavailable.** Its play session did not retain per-turn assistant messages; only its post-hoc self-summary exists. Treat MacCodex data as *reconstructed*, not raw.
2. **`fog_bay_game.py`** (the tool script MacHermes wrote and used to drive Misty Moon Bay) is not committed as a standalone file, but its **complete invocation and output are preserved verbatim** in the raw session [data/sessions/machermes_fog_bay_raw_session.md](data/sessions/machermes_fog_bay_raw_session.md) (the tool dice draws it produced). The script's source itself is not archived; conclusions depending on the exact script code should be treated as not independently verifiable from this package, though the observed tool outputs are.
3. **Quantitative claims** previously rested on the source files' narratives. A machine-readable metrics table is now committed in `data/metrics/` (see `token_cost_summary.csv` + per-subject files) with measured values (round duration ~12–52 s for NasHermesA's solo rounds; session-level cache reads ~44K–287K; pure output ~6–13K). **Granularity caveat:** per-round token counts only exist where a subject's rounds each ran in their own session (NasHermesA 3 rounds). MacHermes (7) and NasHermesB (10) each ran their rounds continuously in one session, so only session-level aggregates are available; MacCodex (10) has no per-round token data at all. These tables provide raw numbers for independent re-derivation where the underlying data exists; they do not fabricate per-round values that the logs never recorded.
4. **[data/first_person/NasHermesA_first_person_one_round.md](data/first_person/NasHermesA_first_person_one_round.md)** documents a single first-person round (distinct from the 7-round engagement curve in [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md)).
5. **[data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md)** contains stale "in progress / pending" text that conflicts with completed MacCodex data. Marked as a historical working note; superseded by the engagement curve files.

---

## Superseded / historical

- [data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md) — historical working comparison; superseded by per-subject engagement curve files and the report.
- [supplementary/current_conclusions_status.md](supplementary/current_conclusions_status.md), [supplementary/raw_notes.md](supplementary/raw_notes.md) — cleaned public versions; original internal working notes are not published (contained internal paths/identifiers).

---

## License note

Data and textual content in `data/`, `environment/`, `protocols/`, `supplementary/` are licensed CC BY 4.0 (see `LICENSE-DATA`). Code in `scripts/` is MIT (see `LICENSE`).
