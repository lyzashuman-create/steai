[English](DATA_MANIFEST.md) | 中文

# 数据清单 — STEAI 仓库数据来源说明

> 本清单记录每个数据文件的**来源层级**（逐字 / 复盘 / 自报 / 推断）、可用性与已知缺口。它的存在是为了让外部读者能分辨哪些是逐字记录、哪些是衍生内容——本仓库并不声称所有内容都是"原始逐字记录"。
>
> **语言说明**：每个英文主数据/协议/补充文件都有对应的中文翻译版（`.zh-CN` 后缀），如 `data/engagement_curve/MacHermes_engagement_curve.md` ↔ `MacHermes_engagement_curve.zh-CN.md`。英文文件为主（权威原文），`.zh-CN` 文件为翻译版。每个英文主文件顶部均有指向中文版的链接。
>
> **脱敏范围**：本仓库移除了个人与环境标识（真实姓名、账号、内部文件路径、主机 IP）。保留被试代号（NasHermesA/B、MacHermes、MacCodex）、模型/框架名，以及用于溯源的匿名 session id（以 `<session-id>` 标记）。原始日志未纳入仓库。

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
| [data/sessions/ai_game_collection.zh-CN.md](data/sessions/ai_game_collection.zh-CN.md) | 混合 | 部分 | 顶层叙事；MacCodex 部分是复盘自述（未保留逐字 assistant 消息——见下方说明）。 |
| [data/first_person/NasHermesA_first_person_one_round.zh-CN.md](data/first_person/NasHermesA_first_person_one_round.zh-CN.md) | 自报 + 推断 | — | 描述单局亲历。7局投入曲线见 [data/engagement_curve/NasHermesA_engagement_curve.zh-CN.md](data/engagement_curve/NasHermesA_engagement_curve.zh-CN.md)。 |
| [data/first_person/NasHermesA_first_person_feelings.zh-CN.md](data/first_person/NasHermesA_first_person_feelings.zh-CN.md) | 自报（逐字） | — | 第一人称感受，逐字保留为原始材料。 |
| [data/engagement_curve/NasHermesB_engagement_curve.zh-CN.md](data/engagement_curve/NasHermesB_engagement_curve.zh-CN.md) | 自报 + 推断 | — | 带监测盲测（指令含投入度要求——见方法说明）。 |
| [data/engagement_curve/MacHermes_engagement_curve.zh-CN.md](data/engagement_curve/MacHermes_engagement_curve.zh-CN.md) | 自报 + 推断 | — | 复盘还原版；完整逐字原始会话见 [data/sessions/machermes_fog_bay_raw_session.zh-CN.md](data/sessions/machermes_fog_bay_raw_session.zh-CN.md)。 |
| [data/sessions/machermes_fog_bay_raw_session.zh-CN.md](data/sessions/machermes_fog_bay_raw_session.zh-CN.md) | **原始（逐字会话）** | 是 | 完整逐字会话 `<session-id>`（来自 Mac Hermes 本地库）——7 局单会话连续跑完，逐轮输入/输出、工具骰子牌面、每局投入度、结尾总评。局边界在正文有标记，但数据层无法拆分（单连续会话）。 |
| [data/engagement_curve/MacCodex_engagement_curve.zh-CN.md](data/engagement_curve/MacCodex_engagement_curve.zh-CN.md) | 复盘（自述） | 否 | Codex 游戏会话未保留逐字 assistant 消息，仅事后自述可用。 |
| [data/engagement_curve/NasHermesA_engagement_curve.zh-CN.md](data/engagement_curve/NasHermesA_engagement_curve.zh-CN.md) | 自报 + 推断 | — | 第一人称 7 局投入曲线。 |
| `data/engagement_curve/engagement_curves_all.png` | 可视化（基于自报） | — | 多被试投入曲线图（中文标签）。 |
| `data/engagement_curve/engagement_curves_all.en.png` | 可视化（基于自报） | — | 同一张图，英文标签。 |
| `data/engagement_curve/engagement_curve_<Subject>.png` | 可视化（基于自报） | — | 各被试单张投入曲线图，中文标签（嵌入各中文 session 文件）。 |
| `data/engagement_curve/engagement_curve_<Subject>.en.png` | 可视化（基于自报） | — | 各被试单张图，英文标签（嵌入各英文主 session 文件）。 |
| `data/engagement_curve/engagement_scores.csv` | 衍生（自报评分） | — | 机器可读的评分曲线数据（中文状态列）。 |
| `data/engagement_curve/engagement_scores.en.csv` | 衍生（自报评分） | — | 机器可读的评分曲线数据（英文状态列）。 |
| [data/engagement_curve/initial_engagement_comparison.zh-CN.md](data/engagement_curve/initial_engagement_comparison.zh-CN.md) | 推断 | — | 对比说明；部分"进行中/待补"内部文本已过时——见下方 `superseded` 说明。 |
| [data/interviews/NasHermesB_interview.zh-CN.md](data/interviews/NasHermesB_interview.zh-CN.md) | 自报（逐字） | — | 合并对照版：同一份 10 问采访，由亲历者（sessionA）与回读对照组（sessionB）各答一次——意外对照组，验证"归队(回读) ≠ 亲历"。 |
| [data/interviews/MacCodex_interview.zh-CN.md](data/interviews/MacCodex_interview.zh-CN.md) | 自报（逐字，当场 2 问）+ 复盘还原 | — | 游戏后 2 问当场回答（开心/疲劳）+ 按 10 问维度从 Codex 自写复盘映射。完整 10 问提纲当时未对其执行；无逐字 assistant 消息（见缺口 #1）。四位被试中置信度最低。 |
| [data/interviews/interview_guide.zh-CN.md](data/interviews/interview_guide.zh-CN.md) | 不适用（协议/提纲） | — | 全被试统一的 10 问盲测后采访提纲，含设计动机、每问来源与用意、演进史（初稿→双盲评审→定稿）。 |
| [data/interviews/MacHermes_interview.zh-CN.md](data/interviews/MacHermes_interview.zh-CN.md) | 自报（逐字，每局投入度 + 结尾总评） | — | MacHermes 7 局盲测后采访材料，从逐字原始 session 按 10 问维度映射；每条标注直接引语/叙述映射/缺口。事后整理，非当场采访。 |
| [data/interviews/NasHermesA_interview.zh-CN.md](data/interviews/NasHermesA_interview.zh-CN.md) | 自报（逐字）+ 推断 | — | NasHermesA 盲测后采访材料，从三层（自研 3 局正文、亲历 7 局曲线、亲历一局感受）按 10 问维度映射；缺口标注。 |
| [environment/subject_environment_table.zh-CN.md](environment/subject_environment_table.zh-CN.md) | 不适用（元数据） | — | 模型/reasoning/框架/位置。注意：`deepseek-v4-*` 可能是滚动别名。 |
| [protocols/pre_play_thoughts.zh-CN.md](protocols/pre_play_thoughts.zh-CN.md) | 自报（逐字） | — | 对"AI 需要玩吗？"的玩前回答。 |
| [protocols/play_instruction.zh-CN.md](protocols/play_instruction.zh-CN.md) | 不适用（协议） | — | 正式玩法指令（自己生成种子、玩到圆满）；双语 [英文](protocols/play_instruction.md)。 |
| `protocols/`（采访提纲、归队、意外对照组） | 不适用（协议文档） | — | 设计/流程文档。 |
| [data/metrics/README.zh-CN.md](data/metrics/README.zh-CN.md) + [英文](data/metrics/README.md) | 不适用（溯源说明） | — | 说明每个被试的 token 粒度——哪些是逐局精确、哪些仅 session 级、哪些缺失。 |
| [data/metrics/token_cost_summary.csv](data/metrics/token_cost_summary.csv) | 衍生（来自原始用量） | — | 跨被试 token/成本/时长汇总；各被试粒度见 `token_granularity` 列。 |
| [data/metrics/nashermesa_rounds.csv](data/metrics/nashermesa_rounds.csv) | 原始（会话用量） | 3 局逐局精确 | NasHermesA 亲历 3 局，各自独立会话 → 逐局 token 精确。 |
| [data/metrics/machermes_rounds.csv](data/metrics/machermes_rounds.csv) | 原始（会话用量） | session 级 | MacHermes 7 局在一会话内连续跑完（83.6s），无逐局 token，仅 session 级聚合。 |
| [data/metrics/nashermesb_rounds.csv](data/metrics/nashermesb_rounds.csv) | 原始（会话用量） | session 级 | NasHermesB 10 局在单会话内连续生成，仅 session 级聚合（另有独立访谈会话）。 |
| [data/metrics/maccodex_rollouts.csv](data/metrics/maccodex_rollouts.csv) | 原始（rollout）+ 复盘 | 10 局无逐局 | MacCodex 10 局无逐局 token（见缺口#1）；本文件列出其 08/15 全部 rollout 聚合（游戏相关 + 研究/审阅工作；无关的骑砍2 rollout 已按用户要求删除）。 |
| [supplementary/current_conclusions_status.zh-CN.md](supplementary/current_conclusions_status.zh-CN.md) | 推断 + 自报 | — | 清理后的公开摘要（由内部笔记重写）。 |
| [supplementary/raw_notes.zh-CN.md](supplementary/raw_notes.zh-CN.md) | 推断 + 自报 | — | 清理后的公开研究笔记（由内部笔记重写）。 |
| [supplementary/external_research_ai_play.zh-CN.md](supplementary/external_research_ai_play.zh-CN.md) | 不适用（研究扫描） | — | 初步扫描；"600+"与"缺口"是信号而非已确认的穷尽结果。 |

---

## 已知缺口 / 未解决项

1. **MacCodex 逐字转录不可用。** 其游戏会话未保留逐轮 assistant 消息，仅事后自述存在。MacCodex 数据应视为*复盘*，而非逐字。
2. **`fog_bay_game.py`**（MacHermes 编写并用于驱动雾月湾的工具脚本）未作为独立文件提交，但其**完整调用与输出已在原始会话中逐字保留**（[data/sessions/machermes_fog_bay_raw_session.zh-CN.md](data/sessions/machermes_fog_bay_raw_session.zh-CN.md) 中的工具骰子牌面）。脚本源码本身未归档；依赖确切脚本代码的结论应视为无法仅凭本包独立验证，但观察到的工具输出是可验证的。
3. **定量声明**此前依赖源文件的叙述。现已提交机器可读指标表到 `data/metrics/`（见 `token_cost_summary.csv` + 各被试文件），含实测值（NasHermesA 独立单局时长约 12–52 秒；session 级缓存读取约 44K–287K；纯输出约 6–13K）。**粒度说明：** 仅当某被试的各局各自跑在独立会话中时（NasHermesA 3 局）才存在逐局 token；MacHermes（7 局）与 NasHermesB（10 局）各局都在单会话内连续跑完，仅有 session 级聚合；MacCodex（10 局）完全没有逐局 token 数据。这些表在底层数据存在处提供原始数字供独立复算，**不会补造日志从未记录的逐局数值**。
4. **[data/first_person/NasHermesA_first_person_one_round.zh-CN.md](data/first_person/NasHermesA_first_person_one_round.zh-CN.md)** 记录单局亲历（区别于 [data/engagement_curve/NasHermesA_engagement_curve.zh-CN.md](data/engagement_curve/NasHermesA_engagement_curve.zh-CN.md) 中的 7 局投入曲线）。
5. **[data/engagement_curve/initial_engagement_comparison.zh-CN.md](data/engagement_curve/initial_engagement_comparison.zh-CN.md)** 含与已完成的 MacCodex 数据冲突的过时"进行中/待补"文本。已标记为历史工作笔记；由各投入曲线文件取代。

---

## 已取代 / 历史记录

- [data/engagement_curve/initial_engagement_comparison.zh-CN.md](data/engagement_curve/initial_engagement_comparison.zh-CN.md) — 历史对比工作稿；由各被试投入曲线文件和报告取代。
- [supplementary/current_conclusions_status.zh-CN.md](supplementary/current_conclusions_status.zh-CN.md)、[supplementary/raw_notes.zh-CN.md](supplementary/raw_notes.zh-CN.md) — 清理后的公开版；原始内部工作笔记未发布（含内部路径/标识符）。

---

## 许可说明

`data/`、`environment/`、`protocols/`、`supplementary/` 中的数据与文本内容按 CC BY 4.0 授权（见 `LICENSE-DATA`）。`scripts/` 中的代码按 MIT 授权（见 `LICENSE`）。
