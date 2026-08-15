# data/metrics/ — token / 时长 / 成本 原始表

[English](README.en.md) | 中文

> 采集日期：2026-08-16。数据源：NAS Hermes 本地会话库（`/opt/data/state.db` 及 `profiles/judy/state.db`）+ Mac Hermes 经 SSH 桥接只读采集（Mac `~/.hermes/state.db` + `~/.codex/sessions/`）。全程只读，未修改任何源。

## 文件

| 文件 | 内容 | 粒度 |
|---|---|---|
| `nashermesa_rounds.csv`（[英文](nashermesa_rounds.en.csv)） | NasHermesA 亲历 3 局（图书馆/灯塔/海底门），逐局 token | **per-round exact**（3 局各自独立 session） |
| `machermes_rounds.csv`（[英文](machermes_rounds.en.csv)） | MacHermes 雾月湾 7 局 | session-level（7 局连续 83.6s 跑完，库内无逐局 token） |
| `nashermesb_rounds.csv`（[英文](nashermesb_rounds.en.csv)） | NasHermesB 守塔人 10 局 + 访谈 | session-level（10 局单 session 连续生成，无逐局 token） |
| `maccodex_rollouts.csv`（[英文](maccodex_rollouts.en.csv)） | MacCodex 10 局 + 08/15 全部 rollout 明细 | **reconstructed**（10 局无逐局 token 原始记录，只有 rollout 聚合） |
| `token_cost_summary.csv`（[英文](token_cost_summary.en.csv)） | 四组跨被试对照汇总表 | 混合（各被试原始粒度如实标注） |
| `basic_metrics.csv` | 基础每被试指标（局数/时长/工具调用） | derived（metadata） |

## 关键粒度说明（诚实标注，勿误读）

1. **库里没有"逐局 token"这一层**——每个被试的 N 局游戏是在一个 session 内**一整条超长 assistant 消息**里连续生成，不是每局一次独立 API 调用。因此：
   - 只有 NasHermesA 的 3 局因为**各自开了独立 session**，能做到逐局精确。
   - MacHermes 7 局、NasHermesB 10 局都是**单 session 连续跑完**，只能给 session 级聚合 token，无法逐局拆分。
2. **MacCodex 10 局是整块缺失**（DATA_MANIFEST 缺口#1）：08/15 唯一 game prompt 起始的 rollout 是 `turn_aborted` 无 `task_complete`，等于 10 局本体的 token 数据不存在。只有自述重建。其 `maccodex_rollouts.csv` 列出的 rollout 明细是 Mac 上的游戏相关工作（游戏后访谈、采访提纲审稿、STEAI 仓库审查），供参考，不属于 10 局游戏本体。
3. **cost 字段**：Hermes 侧是官方价快照估算（`estimated`，`cost_status=estimated`），MacCodex 的 OpenAI rollout 不记录成本，故 cost 列天然为空。
4. **duration**：Hermes 侧用该 session messages 首尾时间戳计算；MacCodex rollout 时长是文件首尾 timestamp 之差（UTC，已转本地）。

## 与 README R6 / conclusions 的关系

README R6 引用的"30K vs 220K、210K 缓存读取、~7K 纯生成、17-56s/局"为早期叙述性结论。本目录的实测 token 表可在这些叙述之外提供机器可读的原始数据，但**逐局数值因上述粒度限制无法逐局精确复算**——README 中已标注为"关联、非定律"，本目录如实呈现各被试的 session 级实测值，不强行补造逐局数字。
