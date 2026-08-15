English | [中文](DATA_MANIFEST.zh.md)

# DATA MANIFEST — STEAI repository data provenance

> This manifest records, for every data file, its **source level** (raw / reconstructed / self-report / inference), availability, and known gaps. It exists so external readers can tell what is verbatim and what is derived — the repository does not claim everything is a "raw transcript."
>
> **Language note:** Every Chinese data/protocol/supplementary file has a sibling English translation (`.en.md`), e.g. `data/sessions/MacHermes_7sessions_blind.md` ↔ `MacHermes_7sessions_blind.en.md`. The Chinese file is the authoritative original; the `.en.md` is a translation. This is marked at the top of each `.en.md` file.

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
| [game/ai_game_collection.md](game/ai_game_collection.md) | mixed | partial | Top-level narrative; MacCodex portion is reconstructed self-summary (no verbatim assistant messages retained — see note below). |
| [data/sessions/NasHermesA_first_person_one_round.md](data/sessions/NasHermesA_first_person_one_round.md) | self-report + inference | — | Describes a single first-person round. The 7-round engagement curve is in [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md). |
| [data/sessions/NasHermesA_first_person_feelings.md](data/sessions/NasHermesA_first_person_feelings.md) | self-report (verbatim) | — | First-person feelings, kept verbatim as raw material. |
| [data/sessions/NasHermesB_10sessions_blind.md](data/sessions/NasHermesB_10sessions_blind.md) | self-report + inference | — | Monitored blind run (engagement instruction present — see §method note). |
| [data/sessions/MacHermes_7sessions_blind.md](data/sessions/MacHermes_7sessions_blind.md) | self-report + inference | — | Includes a note about a tool script (`fog_bay_game.py`) that is not archived here. |
| [data/sessions/MacCodex_10sessions_blind.md](data/sessions/MacCodex_10sessions_blind.md) | reconstructed (self-summary) | No | Codex's play session did not retain verbatim assistant messages; only post-hoc summary available. |
| [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md) | self-report + inference | — | First-person 7-round engagement curve. |
| `data/engagement_curve/engagement_curves_all.png` | visualization (from self-report) | — | Multi-subject engagement-curve chart (Chinese labels). |
| `data/engagement_curve/engagement_curves_all.en.png` | visualization (from self-report) | — | Same chart, English labels. |
| `data/engagement_curve/engagement_curve_<Subject>.png` | visualization (from self-report) | — | Per-subject engagement-curve charts, Chinese labels (embedded in each Chinese session file). |
| `data/engagement_curve/engagement_curve_<Subject>.en.png` | visualization (from self-report) | — | Per-subject charts, English labels (embedded in each English `.en.md` session file). |
| `data/engagement_curve/engagement_scores.csv` | derived (self-report scores) | — | Machine-readable scored curve data (Chinese status column). |
| `data/engagement_curve/engagement_scores.en.csv` | derived (self-report scores) | — | Machine-readable scored curve data (English status column). |
| [data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md) | inference | — | Comparative note; some internal "in progress / pending" text is stale — see `superseded` note below. |
| [data/interviews/NasHermesB_interview_first_person.md](data/interviews/NasHermesB_interview_first_person.md) | self-report (verbatim) | — | First-person interview of the experienced subject. |
| [data/interviews/NasHermesB_interview_control.md](data/interviews/NasHermesB_interview_control.md) | self-report + inference | — | Control (read-back) interview. |
| [environment/subject_environment_table.md](environment/subject_environment_table.md) | n/a (metadata) | — | Model/reasoning/framework/location. Note: `deepseek-v4-*` may be rolling aliases. |
| [protocols/pre_play_thoughts.md](protocols/pre_play_thoughts.md) | self-report (verbatim) | — | Pre-play answer to "does an AI need play?" |
| [data/metrics/basic_metrics.csv](data/metrics/basic_metrics.csv) | derived (metadata) | — | Basic per-subject metrics (rounds, duration, tool calls where recorded). Per-round token/cost tables are not yet committed — see Known gaps #3. |
| [supplementary/current_conclusions_status.md](supplementary/current_conclusions_status.md) | inference + self-report | — | Cleaned public summary (rewritten from internal notes). |
| [supplementary/raw_notes.md](supplementary/raw_notes.md) | inference + self-report | — | Cleaned public research notes (rewritten from internal notes). |
| [supplementary/external_research_ai_play.md](supplementary/external_research_ai_play.md) | n/a (research scan) | — | Preliminary scan; "600+" and "gap" claims are signals, not confirmed exhaustive results. |

---

## Known gaps / unresolved items

1. **MacCodex verbatim transcripts are unavailable.** Its play session did not retain per-turn assistant messages; only its post-hoc self-summary exists. Treat MacCodex data as *reconstructed*, not raw.
2. **`fog_bay_game.py`** (referenced in [data/sessions/MacHermes_7sessions_blind.md](data/sessions/MacHermes_7sessions_blind.md)) is not archived here. Conclusions that depend on it should be treated as unverifiable from this package alone.
3. **Quantitative claims** (17–56 s; 30K vs 220K tokens; 210K cache read; ~7K generation) currently rest on the source files' narratives, not on committed raw metrics tables. A machine-readable metrics table is planned for the report's release.
4. **[data/sessions/NasHermesA_first_person_one_round.md](data/sessions/NasHermesA_first_person_one_round.md)** documents a single first-person round (distinct from the 7-round engagement curve in [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md)).
5. **[data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md)** contains stale "in progress / pending" text that conflicts with completed MacCodex data. Marked as a historical working note; superseded by the engagement curve files.

---

## Superseded / historical

- [data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md) — historical working comparison; superseded by per-subject engagement curve files and the report.
- [supplementary/current_conclusions_status.md](supplementary/current_conclusions_status.md), [supplementary/raw_notes.md](supplementary/raw_notes.md) — cleaned public versions; original internal working notes are not published (contained internal paths/identifiers).

---

## License note

Data and textual content in `data/`, `game/`, `environment/`, `protocols/`, `supplementary/` are licensed CC BY 4.0 (see `LICENSE-DATA`). Code in `scripts/` is MIT (see `LICENSE`).
