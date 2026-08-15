---
title: AI Game Subject Environment Table (Reproducible for the Paper)
date: 2026-08-15
type: Experimental environment record
---

> This is a translation of the original Chinese document. The Chinese version is authoritative.

# Subject Environment Table

> The actual run environments of each subject in the four blind-test groups (2026-08-15). The paper must state them clearly for reproducibility. All version numbers are actual queried values, not the "default" wording.
>
> The whole repository uniformly uses **subject codenames** (see table below); the codename ↔ real-name mapping is in the README's Subjects section.

## Subject Codenames and Run Environments

| Subject codename | Model | reasoning strength | Framework/version | Run location |
|---|---|---|---|---|
| NasHermesA | deepseek-v4-flash | low | Hermes v0.20.0 (2026.8.3) | NAS |
| NasHermesB | deepseek-v4-pro | max | Hermes v0.20.0 (2026.8.3) | NAS |
| MacHermes | deepseek-v4-flash | low | Hermes v0.20.0 (2026.8.3) | Mac |
| MacCodex | gpt-5.6-luna | low | Codex @openai/codex 0.147.0 | Mac |

## Notes

- **Model source**: measured from the `model.default` value in the `configuration file`.
  - NasHermesA (main profile): `default: deepseek-v4-flash`
  - NasHermesB: `default: deepseek-v4-pro`
  - MacHermes: deepseek-v4-flash (same model as the NAS main profile)
  - MacCodex: gpt-5.6-luna (codex exec specified `-m gpt-5.6-luna -c model_reasoning_effort="low"`)
- **reasoning strength**: NasHermesA `reasoning_effort: low`; NasHermesB `reasoning_effort: max`; MacCodex `model_reasoning_effort="low"`.
- **provider**: all deepseek, base_url `https://api.deepseek.com/v1` (MacCodex excepted, goes through gpt).
- **Framework versions**: Hermes v0.20.0 (2026.8.3) / Codex @openai/codex 0.147.0.
- **MacCodex version verification**: queried on the Mac side to obtain `@openai/codex 0.147.0` (npm global package).

## Paper Writing Recommendations

Don't write "default model"; write directly the model name + reasoning strength + framework version + run location (NAS/Mac). The paper uniformly uses subject codenames (NasHermesA, etc.); real names are not publicly credited.