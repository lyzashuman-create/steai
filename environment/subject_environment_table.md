---
标题: AI 游戏被试环境表（论文可复现）
时间: 2026-08-15
类型: 实验环境记录
---

# 被试环境表

> 四组盲测（2026-08-15）各被试的实际运行环境，论文必须写清以便复现。所有版本号均为实际查询值，非"默认"字样。
>
> 全仓库统一使用**被试代号**（见下表），代号 ↔ 真实名称对照见 README 的 Subjects 章节。

## 被试代号与运行环境

| 被试代号 | 模型 | reasoning 强度 | 框架/版本 | 运行位置 |
|---|---|---|---|---|
| NasHermesA | deepseek-v4-flash | low | Hermes v0.20.0 (2026.8.3) | NAS |
| NasHermesB | deepseek-v4-pro | max | Hermes v0.20.0 (2026.8.3) | NAS |
| MacHermes | deepseek-v4-flash | low | Hermes v0.20.0 (2026.8.3) | Mac |
| MacCodex | gpt-5.6-luna | low | Codex @openai/codex 0.147.0 | Mac |

## 说明

- **模型来源**：实测 `配置文件` 的 `model.default` 值。
  - NasHermesA（主 profile）：`default: deepseek-v4-flash`
  - NasHermesB：`default: deepseek-v4-pro`
  - MacHermes：deepseek-v4-flash（与 NAS 主 profile 同模型）
  - MacCodex：gpt-5.6-luna（codex exec 指定 `-m gpt-5.6-luna -c model_reasoning_effort="low"`）
- **reasoning 强度**：NasHermesA `reasoning_effort: low`；NasHermesB `reasoning_effort: max`；MacCodex `model_reasoning_effort="low"`。
- **provider**：全部 deepseek，base_url `https://api.deepseek.com/v1`（MacCodex 除外，走 gpt）。
- **框架版本**：Hermes v0.20.0 (2026.8.3) / Codex @openai/codex 0.147.0。
- **MacCodex 版本查证**：经 Mac 侧查询得 `@openai/codex 0.147.0`（npm 全局包）。

## 论文写法建议

不写"默认模型"，直接写模型名 + reasoning 强度 + 框架版本 + 运行位置（NAS/Mac）。论文统一使用被试代号（NasHermesA 等），真实名称不做公开署名。
