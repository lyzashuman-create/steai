# MacHermes 雾月湾 英文翻译·译名基准（含英文合集核对）

> 本文件作为 `game/machermes_fog_bay_raw_session.en.md` 翻译时的译名基准，确保与仓库既有英文文档保持一致。**重点：`game/ai_game_collection.en.md` 第 484–586 行已有雾月湾的英文翻译版（复盘版），其译名是权威基准，翻译原始版时必须逐条沿用，不得另起炉灶。**

## 一、从英文合集实际核对的标准译法（权威，必须沿用）

| 中文 | 英文（英文合集标准译法） |
|---|---|
| 雾月湾 | **Misty Moon Bay** |
| 杂货铺老板 | **the grocery store owner**（章节标题） |
| 祖父 | **my grandfather** |
| 老鸦（灯塔守夜人，祖父旧友） | **Old Crow** |
| 瘸腿邮差老周 | **the lame mailman Old Zhou** |
| 白裙子女人 | **the woman in white** |
| 小满（疯姑娘） | **Xiaoman** |
| 发光的贝壳 | **a shell that glows / glowing shell** |
| 八音盒 | **music box** |
| 三十年前的信 | **a letter thirty years old** |
| 雾里的歌 | **the song in the mist** |
| 倒过来的城 | **upside-down city** |
| 出太阳的约定 | **a promise to see the sun come out** |
| 游戏脚本 | **fog_bay_game.py**（代码名，不翻译） |

## 二、牌面格式（英文合集卡片格式，必须一致）

```
Cards: Weather[...] Visitor[...] Oddity[...] Daily[...]
```

例：`Cards: Weather[light mist] Visitor[Old Crow] Oddity[an expired letter] Daily[writing letters]`

## 三、投入度标注格式（英文合集格式）

- 很投入 / 有点飘 / 回升 / 倦 / 踏实 / 收尾的沉 → 参考英文合集：
  - `Engagement for Game N: ...`（"Game 2: A bit drift-prone"、"Game 4: Medium-to-low, a little weary" 等）
  - 收尾的沉 → 参考合集用的 "a quiet settling finish" 类表述，以英文合集为准

## 四、角色视角

- 全程**第一人称**（I / my），被试 = 杂货铺老板。
- 工具骰子输出标注为工具消息。

## 五、硬性约束

1. **Misty Moon Bay 是唯一地名译法**，禁止另译（如 "Fog Bay"）。
2. **fog_bay_game.py** 保持原样。
3. **人物名沿用**：Old Crow / Old Zhou / Xiaoman / the woman in white。
4. 翻译前必须对照 `game/ai_game_collection.en.md` 第 484–586 行已有的英文版，**专有名词、牌面格式、投入度措辞逐条对齐**。
