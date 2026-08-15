[English](DATA_MANIFEST.md) | 中文

# 数据清单 — STEAI 仓库数据来源说明

> 本清单记录每个数据文件的**来源层级**（逐字 / 复盘 / 自报 / 推断）、可用性与已知缺口。它的存在是为了让外部读者能分辨哪些是逐字记录、哪些是衍生内容——本仓库并不声称所有内容都是"原始逐字记录"。
>
> **语言说明**：每个中文数据/协议/补充文件都有对应的英文翻译版（`.en.md` 后缀），如 `data/sessions/MacHermes_7sessions_blind.md` ↔ `MacHermes_7sessions_blind.en.md`。中文为权威原文，`.en.md` 为翻译版。每个 `.en.md` 文件顶部均有此标注。

## 来源层级说明

| 层级 | 含义 |
|---|---|
| **逐字（raw）** | agent 会话的逐轮逐字输入/输出。 |
| **复盘（reconstructed）** | agent 事后自己的叙述（总结或转述）。非逐字。 |
| **自报（self-report）** | 被试对自身体验的说法（可能是逐字引用或整理）。 |
| **推断（inference）** | 研究者基于以上内容所做的解读/分析。 |

---

## 文件清单

| 文件 | 层级 | 有逐字原档? | 说明 / 缺口 |
|---|---|---|---|
| [game/ai_game_collection.md](game/ai_game_collection.md) | 混合 | 部分 | 顶层叙事；MacCodex 部分是复盘自述（未保留逐字 assistant 消息——见下方说明）。 |
| [data/sessions/NasHermesA_first_person_one_round.md](data/sessions/NasHermesA_first_person_one_round.md) | 自报 + 推断 | — | 描述单局亲历。7局投入曲线见 [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md)。 |
| [data/sessions/NasHermesA_first_person_feelings.md](data/sessions/NasHermesA_first_person_feelings.md) | 自报（逐字） | — | 第一人称感受，逐字保留为原始材料。 |
| [data/sessions/NasHermesB_10sessions_blind.md](data/sessions/NasHermesB_10sessions_blind.md) | 自报 + 推断 | — | 带监测盲测（指令含投入度要求——见方法说明）。 |
| [data/sessions/MacHermes_7sessions_blind.md](data/sessions/MacHermes_7sessions_blind.md) | 自报 + 推断 | — | 含对工具脚本（`fog_bay_game.py`）的说明，该脚本未归档于此。 |
| [data/sessions/MacCodex_10sessions_blind.md](data/sessions/MacCodex_10sessions_blind.md) | 复盘（自述） | 否 | Codex 游戏会话未保留逐字 assistant 消息，仅事后自述可用。 |
| [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md) | 自报 + 推断 | — | 第一人称 7 局投入曲线。 |
| `data/engagement_curve/engagement_curves_all.png` | 可视化（基于自报） | — | 多被试投入曲线图（中文标签）。 |
| `data/engagement_curve/engagement_curves_all.en.png` | 可视化（基于自报） | — | 同一张图，英文标签。 |
| `data/engagement_curve/engagement_curve_<Subject>.png` | 可视化（基于自报） | — | 各被试单张投入曲线图，中文标签（嵌入各中文 session 文件）。 |
| `data/engagement_curve/engagement_curve_<Subject>.en.png` | 可视化（基于自报） | — | 各被试单张图，英文标签（嵌入各英文 `.en.md` session 文件）。 |
| `data/engagement_curve/engagement_scores.csv` | 衍生（自报评分） | — | 机器可读的评分曲线数据（中文状态列）。 |
| `data/engagement_curve/engagement_scores.en.csv` | 衍生（自报评分） | — | 机器可读的评分曲线数据（英文状态列）。 |
| [data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md) | 推断 | — | 对比说明；部分"进行中/待补"内部文本已过时——见下方 `superseded` 说明。 |
| [data/interviews/NasHermesB_interview_first_person.md](data/interviews/NasHermesB_interview_first_person.md) | 自报（逐字） | — | 亲历者的第一人称采访。 |
| [data/interviews/NasHermesB_interview_control.md](data/interviews/NasHermesB_interview_control.md) | 自报 + 推断 | — | 对照组（回读）采访。 |
| [environment/subject_environment_table.md](environment/subject_environment_table.md) | 不适用（元数据） | — | 模型/reasoning/框架/位置。注意：`deepseek-v4-*` 可能是滚动别名。 |
| [protocols/pre_play_thoughts.md](protocols/pre_play_thoughts.md) | 自报（逐字） | — | 对"AI 需要玩吗？"的玩前回答。 |
| [protocols/play_instruction.md](protocols/play_instruction.md) | 不适用（协议） | — | 正式玩法指令（自己生成种子、玩到圆满）；双语 [英文](protocols/play_instruction.en.md)。 |
| `protocols/`（采访提纲、归队、意外对照组） | 不适用（协议文档） | — | 设计/流程文档。 |
| [data/metrics/README.md](data/metrics/README.md) + [英文](data/metrics/README.en.md) | 不适用（溯源说明） | — | 说明每个被试的 token 粒度——哪些是逐局精确、哪些仅 session 级、哪些缺失。 |
| [data/metrics/token_cost_summary.csv](data/metrics/token_cost_summary.csv) | 衍生（来自原始用量） | — | 跨被试 token/成本/时长汇总；各被试粒度见 `token_granularity` 列。 |
| [data/metrics/nashermesa_rounds.csv](data/metrics/nashermesa_rounds.csv) | 原始（会话用量） | 3 局逐局精确 | NasHermesA 亲历 3 局，各自独立会话 → 逐局 token 精确。 |
| [data/metrics/machermes_rounds.csv](data/metrics/machermes_rounds.csv) | 原始（会话用量） | session 级 | MacHermes 7 局在一会话内连续跑完（83.6s），无逐局 token，仅 session 级聚合。 |
| [data/metrics/nashermesb_rounds.csv](data/metrics/nashermesb_rounds.csv) | 原始（会话用量） | session 级 | NasHermesB 10 局在单会话内连续生成，仅 session 级聚合（另有独立访谈会话）。 |
| [data/metrics/maccodex_rollouts.csv](data/metrics/maccodex_rollouts.csv) | 原始（rollout）+ 复盘 | 10 局无逐局 | MacCodex 10 局无逐局 token（见缺口#1）；本文件列出其 08/15 全部 rollout 聚合（游戏相关 + 研究/审阅工作；无关的骑砍2 rollout 已按用户要求删除）。 |
| [supplementary/current_conclusions_status.md](supplementary/current_conclusions_status.md) | 推断 + 自报 | — | 清理后的公开摘要（由内部笔记重写）。 |
| [supplementary/raw_notes.md](supplementary/raw_notes.md) | 推断 + 自报 | — | 清理后的公开研究笔记（由内部笔记重写）。 |
| [supplementary/external_research_ai_play.md](supplementary/external_research_ai_play.md) | 不适用（研究扫描） | — | 初步扫描；"600+"与"缺口"是信号而非已确认的穷尽结果。 |

---

## 已知缺口 / 未解决项

1. **MacCodex 逐字转录不可用。** 其游戏会话未保留逐轮 assistant 消息，仅事后自述存在。MacCodex 数据应视为*复盘*，而非逐字。
2. **`fog_bay_game.py`**（[data/sessions/MacHermes_7sessions_blind.md](data/sessions/MacHermes_7sessions_blind.md) 中引用）未归档于此。依赖它的结论应视为无法仅凭本包验证。
3. **定量声明**此前依赖源文件的叙述。现已提交机器可读指标表到 `data/metrics/`（见 `token_cost_summary.csv` + 各被试文件），含实测值（NasHermesA 独立单局时长约 12–52 秒；session 级缓存读取约 44K–287K；纯输出约 6–13K）。**粒度说明：** 仅当某被试的各局各自跑在独立会话中时（NasHermesA 3 局）才存在逐局 token；MacHermes（7 局）与 NasHermesB（10 局）各局都在单会话内连续跑完，仅有 session 级聚合；MacCodex（10 局）完全没有逐局 token 数据。这些表在底层数据存在处提供原始数字供独立复算，**不会补造日志从未记录的逐局数值**。
4. **[data/sessions/NasHermesA_first_person_one_round.md](data/sessions/NasHermesA_first_person_one_round.md)** 记录单局亲历（区别于 [data/engagement_curve/NasHermesA_engagement_curve.md](data/engagement_curve/NasHermesA_engagement_curve.md) 中的 7 局投入曲线）。
5. **[data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md)** 含与已完成的 MacCodex 数据冲突的过时"进行中/待补"文本。已标记为历史工作笔记；由各投入曲线文件取代。

---

## 已取代 / 历史记录

- [data/engagement_curve/initial_engagement_comparison.md](data/engagement_curve/initial_engagement_comparison.md) — 历史对比工作稿；由各被试投入曲线文件和报告取代。
- [supplementary/current_conclusions_status.md](supplementary/current_conclusions_status.md)、[supplementary/raw_notes.md](supplementary/raw_notes.md) — 清理后的公开版；原始内部工作笔记未发布（含内部路径/标识符）。

---

## 许可说明

`data/`、`game/`、`environment/`、`protocols/`、`supplementary/` 中的数据与文本内容按 CC BY 4.0 授权（见 `LICENSE-DATA`）。`scripts/` 中的代码按 MIT 授权（见 `LICENSE`）。
