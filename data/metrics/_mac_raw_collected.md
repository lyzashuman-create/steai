# Mac 侧原始采集（2026-08-16，Mac Hermes 只读采集，经 SSH 桥接）

> 来源：Mac Hermes（mac_hermes_bridge）对 ~/.hermes/state.db + ~/.codex/sessions 的只读采集。已脱敏，不含凭据。
> 采集指令见交接日志。全程只读，未修改 Mac 任何文件。

## 表1：MacHermes 雾月湾 7 局（session 级聚合）

subject,round,session_id,started_at,duration_seconds,api_call_count,input_tokens,output_tokens,cache_read_tokens,reasoning_tokens,estimated_cost_usd,notes
MacHermes,7,20260815_185800_54cf78,2026-08-15 18:58:21,83.6,9,8184,7260,287744,3013,0.0039842432,session级聚合无法逐局拆分(7局连续83.6s跑完库内无逐局token)；token=session_model_usage task为空行实际值(deepseek-v4-flash共9次API调用)；另有title_generation计费行1次(+468输入/+1025输出/+128缓存/+1018推理/+$0.0003528784)在7局窗口外未计入；cache_write=0

## 表2：MacCodex（游戏10局无逐局token原始记录）

subject,round,session_id,started_at,duration_seconds,api_call_count,input_tokens,output_tokens,cache_read_tokens,reasoning_tokens,estimated_cost_usd,notes
MacCodex,10,,2026-08-15 19:09:04,,,,,,,,重建自述无逐局token原始记录(对应DATA_MANIFEST缺口#1)：08/15 rollout内无游戏10局逐局token(仅19-09-04 game prompt起始且turn_aborted无task_complete)；codex为OpenAI gpt-5.6-sol，rollout未记录成本字段
MacCodex,,rollout-2026-08-15T19-09-04-01a0051c-6d72-7320-944e-8b8c640c91d9.jsonl,2026-08-15 19:09:39,,2,36305,3242,27136,422,,游戏10局prompt起始(aborted无task_complete)；input含cached=27136,uncached=9169,total=39547
MacCodex,,rollout-2026-08-15T19-21-52-01a00528-24aa-7a00-98a2-962567417976.jsonl,2026-08-15 19:22:00,,4,73794,591,62464,213,,游戏后访谈-开心；input含cached=62464,uncached=11330,total=74385
MacCodex,,rollout-2026-08-15T19-36-41-01a00535-b77c-7981-9448-01a55550a007.jsonl,2026-08-15 19:36:50,,4,74602,934,52480,288,,游戏后访谈-疲劳感；input含cached=52480,uncached=22122,total=75536
MacCodex,,rollout-2026-08-15T19-49-40-01a00541-9ac1-78f1-ad5e-ca2a4af78df0.jsonl,2026-08-15 19:50:20,,1,19298,1895,11008,19,,采访提纲审稿；input含cached=11008,uncached=8290,total=21193
MacCodex,,rollout-2026-08-15T23-24-47-01a00606-8b28-7063-ad6a-a8ed1b62b333.jsonl,2026-08-15 23:25:00,,28,2665645,24213,2493440,9682,,STEAI仓库审查；input含cached=2493440,uncached=172205,total=2689858
MacCodex,,rollout-2026-08-15T23-27-24-01a00608-f21b-7c42-8060-019a7e0ec4fd.jsonl,2026-08-15 23:27:39,,19,1151654,14517,1033472,11774,,STEAI仓库审查；input含cached=1033472,uncached=118182,total=1166171
MacCodex,SUM,(08/15全部rollout汇总),,,87,4556973,51115,4118528,25229,,15个rollout聚合：input=4556973(含cached=4118528,uncached=438445) output=51115 reasoning=25229 total=4608088 token_count事件=87

## 中文总结（Mac Hermes）

Mac 侧实际能采到：
- Hermes 侧 7 局有完整 session 级 token 聚合（session_model_usage 实际值，deepseek 计费含 cost），但只有 session 级、无法逐局拆分；

缺口：
- DATA_MANIFEST #1——Codex 游戏 10 局没有任何逐局 token 原始记录，连那唯一的 19-09-04 game prompt 起始 rollout 都是 turn_aborted、无 task_complete，等于这 10 局的本体 token 数据整块缺失，只能重建自述、token/成本字段留空。
- Codex rollout 不记成本，成本列 Codex 侧天然为空。
