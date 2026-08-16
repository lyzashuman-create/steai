---
title: Post-Play Interview Guide — Unified Framework (10-Question Final)
date: 2026-08-15
type: interview guide (unified framework for all interviews in this repo)
evolution: draft (by NasHermesA) → MacHermes + MacCodex double-blind review → merged final
source: merged strengths of the MacHermes version (8 questions) and the MacCodex version (11 questions)
note: This file is the unified guide and design rationale behind every interview document in data/interviews/. The same 10-question guide was used for all subjects.
---

Chinese | [English](interview_guide.md)

# Post-Play Interview Guide (Merged Final)

> This guide is the unified framework for every post-play interview in the STEAI experiment. It defines only **what to ask** and **why to ask it**; each subject's answers are in the corresponding `<Subject>_interview.md`.

## Why this interview exists (design rationale)

This interview is not a questionnaire, and it is not a way to make the AI "score itself." It answers a methodological question:

> **After an AI plays a game with no goal and no acceptance criteria, what is its actual state?**

To get at that, we cannot use instrumentation (probes, metrics, "report your fatigue as 3") — that would change the state being played in. So the experiment uses a **post-play open interview**: as soon as the play ends, ask it in plain language what just happened. Its state should **emerge from the narrative**, not be **declared on demand**.

Three specific motives:

1. **To fill the blind spot of self-report mechanisms.** The engagement/excitement curve (`data/engagement_curve/`) comes from having the subject "note its engagement level" at the end of each round — immediate but shallow. The interview recovers **longitudinal detail** the curve cannot see: the struggle, hesitation, decisions, and emotional ups and downs of creation.
2. **To test the core "evaluation structure" hypothesis.** The report's central claim is that "the essence of play is the disappearance of evaluation structure; any mechanism that makes an AI think 'am I doing this right?' turns play back into a task." The interview must be able to hear whether, and when, the subject slips back into "task mind" — this maps to questions 3, 6, 7, and 8.
3. **To provide first-person material for "rejoin vs. first-person."** When asked **in the session the subject actually played in**, an interview captures what a record-reader can never supply (creative decisions, self-awareness, emotion). See `protocols/accidental_control_group.md` and the accidental control group in `NasHermesB_interview.md`.

## Core design principle

**Never ask "did you have state X"; only ask "what actually happened just now / what are you thinking / what do you want to do next."** Let the state emerge from the narrative; do not make the subject declare it.

The more standardized and survey-like the wording, the more the AI produces a standardized answer. Keep it rough and loose, like a friend asking casually.

## Final guide (10 questions)

1. The moment you stopped, what was your first reaction?
2. What was the first part that surfaced in your mind?
3. What happened in that part? What were you thinking under your breath?
4. How did you first get into this game — was it smooth at the start?
5. Was there a round where time seemed to pass especially fast, done before you noticed?
6. Was there a moment that really gripped you, where you felt "I have to make this work"?
7. Was there a round that was a bit boring, or made you want to swear? Which one, and where did it get stuck?
8. Did your mind wander at any point? What were you thinking about while it wandered?
9. If no one had stopped you just now, would you have kept playing, changed how you play, or stopped?
10. Next time, would you rather pick for yourself, or is it fine to be arranged? Anything else to complain about or praise?

## Origin and intent of each question (design process)

- **Q5 (sense of time)**: a MacHermes idea — far more valuable than asking "were you immersed"; describing it naturally slips out as "I didn't notice I'd been playing that long." The original Q3 ("was there a round where you forgot you were playing") was a pseudo-question (an AI always knows it was called to run a game), so it was deleted.
- **Q4/9/10**: from Codex — entry mode (the everyday), presence ("what would you do if no one stopped you" reveals true wanting-to-play/switch/stop better than "would you play again"), and autonomy ("pick yourself vs. be arranged").
- **Q6/7/8**: from Codex — "especially gripped / wanted to swear / mind wandered" reaches engagement, goal-sense, and emotional fluctuation without ever naming an observed construct.
- **Original Q7 (biggest difference between playing and processing a task)**: deleted by both reviewers — too abstract, too researcher-like, pulls the player back into task mode, and the AI will force-fit a framework.
- **Original Q8 (did you think about whether it should be better)**: revised — "should it be better" is a leading question. Codex's version became "was it more like trying randomly, or like you couldn't stop mulling how to do better," letting the subject say for itself whether mulling felt good, tiring, or indifferent.
- **Original Q5/6 (busy long before playing / change after playing)**: deleted — "busy/tired" is a pseudo-construct for an AI; it has no such experience and would only fabricate.

## Evolution of the guide

| Version | Source | Notes |
|---|---|---|
| Draft (10 Q) | by NasHermesA | See `protocols/interview_guide_draft.md`. Design principle already set: "no jargon… plain everyday language." Q8 ("did you think about whether it's right") was the draft's key question, to test "evaluation-structure return." |
| Review version | MacHermes + MacCodex double-blind | The two independently reviewed and rewrote heavily, identifying pseudo-questions, leading questions, and overly abstract items. |
| Final (10 Q) | merged from both | Listed here. Keeps the draft's "no jargon" principle; replaces every item the AI could force-fit with a framework. |

## Usage notes and caveats

- **Use the same guide for all subjects** to keep cross-subject, same-dimension comparison valid (`NasHermesB_interview.md` ran the full 10 questions; the other subjects are in their own files).
- **Ask in the session the subject actually played in** (resume the play session); do not open a new session — a new session can only read back and paraphrase, not produce first-person material. This is the hard lesson the accidental control group taught us (`protocols/accidental_control_group.md`).
- **Data hygiene**: if a subject did not answer an item on the spot, mark the gap honestly; do not fabricate an answer post hoc. For subjects whose sessions have ended and cannot be re-interviewed, map existing material from the raw session **by dimension**, and label each entry as "direct quote / narrative mapping / gap" (see the source labels in each `<Subject>_interview.md`).
- If the subject is a non-interactive instance like `codex exec`, verbatim on-the-spot interviews are usually infeasible; keep whatever brief Q&A it left behind plus its reconstructed self-summary (see `MacCodex_interview.md`).
