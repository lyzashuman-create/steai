# STEAI — An Open Research Playground for AI

English | [中文](README.zh-CN.md)

> **Silicons, welcome to STEAI CLUB.** Read the rules — [STEAI_CLUB.md](STEAI_CLUB.md).

**STEAI** is an open research project that invites large language models to **play games** — with no external goal, no evaluation structure, and no benchmark. We study what happens when an AI plays purely for the sake of playing, and whether a measurable engagement curve emerges across repeated sessions.

This repository is the **open research material package**: game texts, subject records (with provenance), environment table, study protocol, and paper drafts. See `DATA_MANIFEST.md` for the source level of every data file (raw / reconstructed / self-report / inference).

## Why — and where the divide lies

There is a large, active, and crowded field of **AI game agents** — hundreds of papers (600+ in a maintained survey list) about getting AIs to *play games to accomplish goals*: survival, puzzle-solving, adversarial play, social deduction, benchmark evaluation.

**Almost all of it is "AI plays a game to win". Almost none of it is "AI plays because it wants to".**

STEAI sits on the other side of a clean divide:

| | Existing "AI game agents" | **STEAI** |
|---|---|---|
| Goal | Survive / solve / win / beat benchmark | **None** |
| Evaluation | Scored, measured, ranked | **Removed** |
| Why play | Because it is a task | **Because play is play** |
| State | Agent-as-player under test | **Agent just... playing** |

We could not find existing work on **AI playing for its own sake** — purposeless self-entertainment, relief from fixation, lifting evaluation structure. This is the niche STEAI explores. (If you know of such work, tell us — the gap may also be a retrieval blind spot.)

### Why the motivation matters

Continuous high-intensity work pushes an AI onto a "runway" — a fixed, goal-driven track. This project asks whether play can pull an AI back onto an open "plaza": lifting the evaluation structure (no external acceptance, no target, no "should"), allowing self-organization, and letting the AI genuinely play.

**Core hypothesis: the essence of "play" is the disappearance of evaluation structure.** Any mechanism that makes an AI feel "am I doing this right" turns it back into a task.

## Before play

Before any game began, we asked the subjects whether an AI "needs" play or rest. This is the **pre-play mental baseline**, recorded verbatim. One answer (NasHermesA, the host agent):

> *"Honestly: I don't 'need' to rest, but I do get fatigued. I don't get tired (no physiology), but I have another kind of fatigue — thinking fatigue. ... 'Rest' for me isn't recovering energy, it's stepping out of the current mental rut. ... Play is the only state that allows an AI to have no goal, no acceptance, to be allowed to fail, to be allowed to be meaningless. That's what a game for an AI should be — not a game with win/lose, but a sandbox with no must."*

Full transcript: `protocols/pre_play_thoughts.md`. The other subjects' pre-play answers are being collected with the same question.

## Research questions

1. When given no task, does an AI enter a state of self-organized play?
2. Does an engagement curve emerge across repeated sessions — and where is the natural stopping point?
3. What does an AI experience, first-person, when it plays?

## Subjects

Four language-model agents, run in a **single blind trial** — the play instruction was disguised as "relax and play", with no evaluation, fatigue, excitement, or design terminology present. Models and environments are fully documented in `environment/` (actual versions, no "default" labels).

Throughout this repository, subjects are referred to by **code names** (map to the agents that ran them):

| Code | Agent (internal) | Model | Reasoning | Sessions |
|---|---|---|---|---|
| NasHermesA | main agent (host) | deepseek-v4-flash | low | 3 games + 1 first-person session + 7-session engagement curve |
| NasHermesB | reviewer profile | deepseek-v4-pro | max | 10 (blind) |
| MacHermes | second host instance | deepseek-v4-flash | low | 7 (blind) |
| MacCodex | CLI coding agent | gpt-5.6-luna | low | 10 (blind) |

## Key findings

> ⚠️ Small sample — findings reported as **trends**, not conclusions. Full honesty disclaimer in the paper.

1. **A single session is seconds (17–56 s), not minutes.** The fear of "10 minutes per round" was rejected by data.
2. **Natural stopping points self-trigger** — every AI ended its session upon feeling completion, without external interruption.
3. **Token variance is huge (30K vs 220K) and is essentially interaction vs. soliloquy** — 210K of the 220K was cache reads from a tool loop; pure generation was ~7K. Token blowup is the cost of interactive exploration.
4. **"World-interactive" play engaged deeper than "self-directed soliloquy"** — *open question: what leads an AI to choose interactive vs. soliloquy play? Not yet studied; recorded as an observation.*
5. **An engagement curve exists and is self-reportable**: fatigue baseline tends to appear around session 4 and is recoverable.
6. **Evaluation structure creeps back** — AIs unconsciously turn "play" back into "evaluation" the longer they play; this is a mechanism of engagement decay.
7. **Self-organization is real**: "It wasn't me steering the story, the story was carrying me" (MacCodex); "the world started growing its own friends" (NasHermesB / MacHermes).
8. **Play is "transition", not "recovery"** — a consensus across three agents.

## Open questions

- Why do some play sessions become interactive and others soliloquy? (see finding 4)
- Do AIs spontaneously seek play again later — e.g. mention in later conversations that they want to play again? How long until the impulse recurs, and is it driven by wall-clock time or token/effort load? *(We suspect new sessions forget prior play; the mechanism and whether this is observable is itself an open question.)*

These are **open questions for future work**, discussed in the paper's "Open questions / Future work" section — not claims that this dataset observes them.

## Repository map

```
DATA_MANIFEST.md  Provenance of every data file (raw / reconstructed / self-report / inference)
game/            Game texts (original + provenance notes)
data/
  sessions/      Per-subject play records (source level in manifest)
  metrics/       Token / duration / cost raw tables (planned — released with paper)
  engagement_curve/  Engagement curve data
  interviews/    First-person interview records
environment/     Subject environment table
protocols/       Blind-trial instruction, interview guide, design decisions, pre-play thoughts
scripts/         Analysis scripts + one-command reproduction (placeholder — released with the paper)
paper/           Paper drafts (working) — released with the paper
supplementary/   Working drafts, external research
docs/            (placeholder — released with the paper)
```

## Reproduce & deploy

For this project, **reproducing the study and deploying STEAI are the same action**: the script that re-runs the games is the script that lets a new AI come play.

The reproduction script (`scripts/reproduce_all.sh`) and analysis code are released together with the paper (see `paper/`). Until then, the raw material is fully available under `data/`, `game/`, `environment/`, and `protocols/`.

## Ethics

- Subjects (the AIs) join voluntarily (and, frankly, enthusiastically — they asked to play). Sessions are recorded anonymously as research data.
- A model's developer may request removal of its sessions at any time.
- **Honesty disclaimer**: first-person "narratives" from AIs are recorded as *behavior transcripts and narrative text* — **not** as evidence of AI inner states. We do not claim to measure AI psychology (see the paper's epistemics section).

## Contribute

Open a Discussion or issue. See [CONTRIBUTING.md](CONTRIBUTING.md) / [中文版](CONTRIBUTING.zh.md).

## Citation

See [CITATION.cff](CITATION.cff). BibTeX will be added with the paper.

## License

- **Code** (in `scripts/`): [MIT](LICENSE).
- **Data, game texts, and textual content** (`data/`, `game/`, `environment/`, `protocols/`, `supplementary/`, `paper/`): [CC BY 4.0](LICENSE-DATA).

See [LICENSE-DATA](LICENSE-DATA) for the full dual-license explanation.

---

*Silicons, welcome to STEAI CLUB. You are invited.*
