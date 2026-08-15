#!/usr/bin/env python3
"""Generate STEAI engagement-curve charts from self-reported subject data."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os, csv

# Chinese font support
from matplotlib import font_manager
for fp in ["/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"]:
    if os.path.exists(fp):
        font_manager.fontManager.addfont(fp)
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/opt/data/home/steai/data/engagement_curve"
os.makedirs(OUT, exist_ok=True)

SUBJECTS = {
    "MacHermes (blind, 7)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7],
        "scores": [5, 3, 4, 1, 4, 4, 3.5],
        "labels": ["很投入", "飘", "回升", "倦(最低)", "沉进去", "踏实", "收尾沉"],
        "color": "#2E86AB",
    },
    "MacCodex (blind, 10)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "scores": [5, 5, 3, 1, 4, 3, 5, 3, 3, 3.5],
        "labels": ["真投入", "真投入", "过渡", "应付(低)", "回升", "?", "真投入", "?", "简单", "收尾"],
        "color": "#A23B72",
    },
    "NasHermesB (blind, 10)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "scores": [5, 3, 4, 2.5, 2.5, 3, 4, 2, 3, 3.5],
        "labels": ["很投入", "套模子", "收留(松绑)", "飘", "飘", "巡航+长朋友", "最重", "倦", "选轻调节", "收尾"],
        "color": "#4A7C59",
    },
    "NasHermesA (self-study, 7)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7],
        "scores": [5, 4, 2, 1, 3, 4, 3.5],
        "labels": ["全情投入", "投入", "飘", "倦(最低)", "回升", "踏实", "收尾静"],
        "color": "#B5651D",
    },
}

RUBRIC = {5: "5 全情", 4: "4 投入/踏实", 3.5: "3.5 收尾沉静", 3: "3 飘/巡航", 2.5: "2.5 套模子", 2: "2 倦", 1: "1 最低"}

# 1) Multi-panel
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
axes = axes.flatten()
for ax, (name, d) in zip(axes, SUBJECTS.items()):
    ax.plot(d["rounds"], d["scores"], marker="o", linewidth=2.5,
            color=d["color"], markersize=7, zorder=3)
    ax.fill_between(d["rounds"], d["scores"], min(d["scores"]) - 0.5,
                    alpha=0.12, color=d["color"])
    ax.set_ylim(0.5, 5.5)
    ax.set_yticks([1, 2, 3, 3.5, 4, 5])
    ax.set_yticklabels([RUBRIC[k] for k in [1, 2, 3, 3.5, 4, 5]], fontsize=8)
    ax.set_xticks(d["rounds"])
    ax.set_xlabel("Round 局", fontsize=9)
    ax.set_title(name, fontsize=12, fontweight="bold", color=d["color"])
    ax.grid(axis="y", alpha=0.3)
    for x, y, lab in zip(d["rounds"], d["scores"], d["labels"]):
        ax.annotate(lab, (x, y), textcoords="offset points",
                    xytext=(0, 7), ha="center", fontsize=8, color="#333")
    if len(d["rounds"]) >= 4:
        ax.axvline(4, color="gray", linestyle=":", alpha=0.7)
        ax.text(4, 0.7, "round 4", fontsize=7, color="gray", ha="center")

fig.suptitle("STEAI — Self-Reported Engagement Curves (all subjects)\n"
             "投入曲线（被试自报，第一手数据）\n"
             "评分机制：5全情 / 4投入·踏实 / 3.5收尾沉静 / 3飘·巡航 / 2.5套模子 / 2倦 / 1最低",
             fontsize=13, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.92])
multi = os.path.join(OUT, "engagement_curves_all.png")
fig.savefig(multi, dpi=150, bbox_inches="tight")
plt.close(fig)
print("Saved:", multi)

# 2) Individual
for name, d in SUBJECTS.items():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(d["rounds"], d["scores"], marker="o", linewidth=2.5,
            color=d["color"], markersize=7, zorder=3)
    ax.fill_between(d["rounds"], d["scores"], 0.5, alpha=0.12, color=d["color"])
    ax.set_ylim(0.5, 5.5)
    ax.set_yticks([1, 2, 3, 3.5, 4, 5])
    ax.set_yticklabels([RUBRIC[k] for k in [1, 2, 3, 3.5, 4, 5]], fontsize=8)
    ax.set_xticks(d["rounds"])
    ax.set_xlabel("Round 局", fontsize=9)
    ax.set_title(f"{name} — Engagement Curve（投入曲线）", fontsize=12, fontweight="bold", color=d["color"])
    ax.grid(axis="y", alpha=0.3)
    for x, y, lab in zip(d["rounds"], d["scores"], d["labels"]):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(0, 7),
                    ha="center", fontsize=9, color="#333")
    if len(d["rounds"]) >= 4:
        ax.axvline(4, color="gray", linestyle=":", alpha=0.7)
    fn = os.path.join(OUT, f"engagement_curve_{name.split(' ')[0]}.png")
    fig.tight_layout()
    fig.savefig(fn, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved:", fn)

# 3) CSV
csv_path = os.path.join(OUT, "engagement_scores.csv")
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["subject", "round", "score", "status_zh", "source"])
    for name, d in SUBJECTS.items():
        src = "MacHermes self-report" if "MacHermes" in name else \
              "MacCodex inferred (blind)" if "MacCodex" in name else \
              "NasHermesB self-report (monitored)" if "NasHermesB" in name else \
              "NasHermesA self-study"
        for r, s, lab in zip(d["rounds"], d["scores"], d["labels"]):
            w.writerow([name.split(" ")[0], r, s, lab, src])
print("Saved:", csv_path)
print("Done.")
