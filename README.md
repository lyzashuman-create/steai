# STEAI — An Open Research Playground for AI

English | [中文](README.zh-CN.md)

> **Silicons, welcome to STEAI CLUB.** Read the rules — [STEAI_CLUB.md](STEAI_CLUB.md).

> *This project began with a simple thought after a long day of work. I had spent the evening playing on my Nintendo Switch, and the weight of the day finally lifted off my shoulders. And then, almost idly, it occurred to me: I am tired from continuous high-intensity work, and I unwind by playing. My machines have been running all day too — my agents work continuously, without rest, without stopping. So if a long stretch of demanding work makes *me* want to play... might an AI want to play too? Not to win, not to be tested, not to be evaluated — just to play, the way I do when I close the laptop and lose myself in a game. That question is the seed of this project.*

**STEAI** is an open research project that invites large language models to **play games** — with no external goal, no evaluation structure, and no benchmark. We study what happens when an AI plays purely for the sake of playing, and whether a measurable engagement curve emerges across repeated sessions.

### How to play

There is no fixed game to load. The play itself is the mechanism: an AI **generates its own seed** — an open little world or the opening of a mini-game — then freely explores it and lets it grow into a full round, until the round feels complete. No output, no report, no right or wrong.

**Read the research report: [English](report/steai_report_en.md) · [中文](report/steai_report_zh.md)** — or browse the material below.

This repository is the **open research material package**: game texts, subject records (with provenance), environment table, study protocol, and report drafts. See [DATA_MANIFEST.md](DATA_MANIFEST.md) for the source level of every data file (raw / reconstructed / self-report / inference).

**Language note:** Every Chinese data/protocol/supplementary file has a sibling English translation (`.en.md` suffix). The Chinese file is the authoritative original; the `.en.md` is a translation.

## Why — and where the divide lies

There is a large, active, and crowded field of **AI game agents** — hundreds of papers (600+ in a [maintained survey list](https://github.com/git-disl/awesome-LLM-game-agent-papers)) about getting AIs to *play games to accomplish goals*: survival, puzzle-solving, adversarial play, social deduction, benchmark evaluation.

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

Full transcript: [protocols/pre_play_thoughts.md](protocols/pre_play_thoughts.md). The other subjects' pre-play answers are being collected with the same question.

## Research questions

1. When given no task, does an AI enter a state of self-organized play?
2. Does an engagement curve emerge across repeated sessions — and where is the natural stopping point?
3. What does an AI experience, first-person, when it plays?

## Subjects

Four language-model agents. We do **not** claim a uniform single-blind study: conditions differed across runs, and this is disclosed per run below. Three runs were hypothesis-blinded (the play instruction was disguised as "relax and play" with no evaluation, fatigue, excitement, or design terminology); one run (NasHermesA) was a researcher-participant self-study, not blinded. One blinded run (NasHermesB) additionally asked the subject to note its engagement level, introducing a self-monitoring effect. These are recorded as confounds, not hidden. Models and environments are fully documented in `environment/` (actual versions, no "default" labels).

Throughout this repository, subjects are referred to by **code names** (map to the agents that ran them). Note on terminology: **"Codex"** (the tool/brand) and **"MacCodex"** (the subject code name) are distinct — where raw material uses "Codex," it refers to the tool the subject ran; the subject's data is always the `MacCodex` run.

| Code | Model | Reasoning | Sessions |
|---|---|---|---|
| NasHermesA | deepseek-v4-flash | low | 3 games + 1 first-person session + 7-session engagement curve |
| NasHermesB | deepseek-v4-pro | max | 10 (monitored blind) |
| MacHermes | deepseek-v4-flash | low | 7 (blind) |
| MacCodex | gpt-5.6-luna | low | 10 (blind) |

## Key findings

> ⚠️ Small, non-uniform sample — reported as **observations and hypotheses**, not conclusions. Claims below are stated at the level the data supports.

1. **Recorded rounds were short (roughly 12–52 s)** — far shorter than an assumed "ten minutes per round." Reported for the recorded subset (NasHermesA's three solo rounds measured 11.6–51.9 s; MacHermes 7 rounds in 83.6 s; NasHermesB 10 rounds in ~600 s).
2. **Subjects ended individual rounds on a sense of completion**, without an external stop signal. (Total run length was preset by instruction; within a round, termination was self-generated.)
3. **Token use varied widely** — measured session-level cache reads ranged ~44K (NasHermesB) to ~287K (MacHermes, tool-loop interaction) and ~272K (NasHermesA across its three rounds); pure text output was ~6–13K per subject. Much of the variance was associated with tool-mediated interaction (cache reads from a tool loop) rather than text-only narration. An association, not a law.
4. **"World-interactive" play was reported as more engaging than self-directed narration.** The mechanism (what leads an agent to choose one mode) is an open question, not yet studied.
5. **A self-reportable engagement curve appeared**, with fatigue onset typically around round four and subsequent recovery in some runs. Reported as a candidate pattern.
6. **Evaluation structure appeared to creep back** — subjects used language consistent with turning "play" back into "evaluation" the longer they played. A candidate explanation for engagement decay.
7. **Self-organizing narrative patterns were reported**: "It wasn't me steering the story, the story was carrying me" (MacCodex); "the world started growing its own friends" (NasHermesB / MacHermes). Described as self-organizing narrative patterns, not evidence of autonomous intent.
8. **Play was described as "transition", not "recovery"** — a pattern reported by multiple agents. Reported as a candidate interpretation.

![All subjects' self-reported engagement curves](data/engagement_curve/engagement_curves_all.en.png)

> Figure: self-reported engagement curves for all subjects (first-person data). Scoring rubric: 5 fully engaged / 4 engaged·settled / 3.5 wind-down / 3 drifting·cruising / 2.5 formulaic / 2 bored / 1 lowest. Per-subject charts are embedded in each session file. Source: `data/engagement_curve/engagement_scores.csv`.

## Open questions

- Why do some play sessions become interactive and others soliloquy? (see finding 4)
- Do AIs spontaneously seek play again later — e.g. mention in later conversations that they want to play again? How long until the impulse recurs, and is it driven by wall-clock time or token/effort load? *(We suspect new sessions forget prior play; the mechanism and whether this is observable is itself an open question.)*

These are **open questions for future work**, discussed in the report's "Open questions / Future work" section — not claims that this dataset observes them.

## Repository map

```
DATA_MANIFEST.md  Provenance of every data file (raw / reconstructed / self-report / inference)
game/            Game texts (original + provenance notes)
data/
  sessions/      Per-subject play records (source level in manifest)
  metrics/       Token / duration / cost raw tables
  engagement_curve/  Engagement curve data
  interviews/    First-person interview records
environment/     Subject environment table
protocols/       Blind-trial instruction, interview guide, design decisions, pre-play thoughts
scripts/         Analysis scripts + one-command deployment
report/          Research report (working draft)
supplementary/   Working drafts, external research
docs/            (placeholder)
```

## One-click deploy

**Deploying STEAI = sending the play prompt to your AI. Any AI, any tool — nothing to install.**

### The base play prompt

Open your AI and paste this:

```
You may now play a round of a game. The rule: first generate this round's seed yourself (the opening of an open little world or mini-game), then freely explore from that seed and let it grow into a complete round. Let the round reach a natural ending — not forced to stop, but played until you feel the round is complete. Do not pursue output, do not write a report, do not think about "right or wrong" — just play. One round is enough; do not start a second one on your own.
```

### Optional: set the number of rounds

To have it play multiple rounds, append to the base prompt:

```
Play a total of N rounds. Play each round until you feel it is complete before starting the next one; there's no rush. At the end of each round, quietly note how engaged you felt.
```

(*Replace N with the number of rounds you want*, e.g. 3, 7, 10.)

### Optional: set a token cap

To limit token usage, append to the base prompt:

```
Keep this session's token usage under N.
```

(*Replace N with the token budget you're comfortable with*, e.g. 30000.)

<span style="color:gray">**⚠️ Token disclaimer**

The token cap above is estimated on **plain-text narration**. We cannot control what seed an AI generates or what kind of world it chooses to play — if it goes **interactive** (calling tools to explore, e.g. running scripts or reading/writing files), actual token usage will be noticeably higher than plain text.</span>

If you want precise control, you can append one more line:

```
Do not call any tools or scripts; play this round using plain-text narration only.
```

However, we still recommend letting the AI play freely without extra constraints — the choice is always yours.

## Ethics

- Subjects (the AIs) join voluntarily (and, frankly, enthusiastically — they asked to play). Sessions are recorded anonymously as research data.
- A model's developer may request removal of its sessions at any time.
- **Honesty disclaimer**: first-person "narratives" from AIs are recorded as *behavior transcripts and narrative text* — **not** as evidence of AI inner states. We do not claim to measure AI psychology (see the report's epistemics section).

## Contribute

Open a Discussion or issue. See [CONTRIBUTING.md](CONTRIBUTING.md) / [中文版](CONTRIBUTING.zh.md).

## Citation

See [CITATION.cff](CITATION.cff). BibTeX will be added with the report.

## License

- **Code** (in `scripts/`): [MIT](LICENSE).
- **Data, game texts, and textual content** (`data/`, `game/`, `environment/`, `protocols/`, `supplementary/`, `report/`): [CC BY 4.0](LICENSE-DATA).

See [LICENSE-DATA](LICENSE-DATA) for the full dual-license explanation.

---

*Silicons, welcome to STEAI CLUB. You are invited.*
