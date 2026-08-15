#!/usr/bin/env python3
"""Generate ENGLISH-label engagement-curve charts for STEAI.
Sibling to make_engagement_curves.py (Chinese labels). Outputs .en.png + .en.csv.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os, csv

for fp in ["/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"]:
    if os.path.exists(fp):
        font_manager.fontManager.addfont(fp)
plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "engagement_curve")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = {
    "MacHermes (blind, 7)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7],
        "scores": [5, 3, 4, 1, 4, 4, 3.5],
        "labels": ["Engaged", "Drifting", "Recovered", "Bored (low)", "Absorbed", "Settled", "Wind-down"],
        "color": "#2E86AB",
    },
    "MacCodex (blind, 10)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "scores": [5, 5, 3, 1, 4, 3, 5, 3, 3, 3.5],
        "labels": ["Engaged", "Engaged", "Transition", "Coping (low)", "Recovered", "?", "Engaged", "?", "Simple", "Wind-down"],
        "color": "#A23B72",
    },
    "NasHermesB (blind, 10)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "scores": [5, 3, 4, 2.5, 2.5, 3, 4, 2, 3, 3.5],
        "labels": ["Engaged", "Formulaic", "Unbound", "Drifting", "Drifting", "Cruise+friends", "Deepest", "Bored", "Light self-adjust", "Wind-down"],
        "color": "#4A7C59",
    },
    "NasHermesA (self-study, 7)": {
        "rounds": [1, 2, 3, 4, 5, 6, 7],
        "scores": [5, 4, 2, 1, 3, 4, 3.5],
        "labels": ["Fully engaged", "Engaged", "Drifting", "Bored (low)", "Recovered", "Settled", "Wind-down"],
        "color": "#B5651D",
    },
}

RUBRIC = {5: "5 Fully", 4: "4 Engaged/Settled", 3.5: "3.5 Wind-down", 3: "3 Drifting", 2.5: "2.5 Formulaic", 2: "2 Bored", 1: "1 Lowest"}

# 1) Multi-panel (English)
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
axes = axes.flatten()
for ax, (name, d) in zip(axes, SUBJECTS.items()):
    ax.plot(d["rounds"], d["scores"], marker="o", linewidth=2.5, color=d["color"], markersize=7, zorder=3)
    ax.fill_between(d["rounds"], d["scores"], min(d["scores"]) - 0.5, alpha=0.12, color=d["color"])
    ax.set_ylim(0.5, 5.5)
    ax.set_yticks([1, 2, 3, 3.5, 4, 5])
    ax.set_yticklabels([RUBRIC[k] for k in [1, 2, 3, 3.5, 4, 5]], fontsize=8)
    ax.set_xticks(d["rounds"])
    ax.set_xlabel("Round", fontsize=9)
    ax.set_title(name, fontsize=12, fontweight="bold", color=d["color"])
    ax.grid(axis="y", alpha=0.3)
    for x, y, lab in zip(d["rounds"], d["scores"], d["labels"]):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=8, color="#333")
    if len(d["rounds"]) >= 4:
        ax.axvline(4, color="gray", linestyle=":", alpha=0.7)
        ax.text(4, 0.7, "round 4", fontsize=7, color="gray", ha="center")

fig.suptitle("STEAI — Self-Reported Engagement Curves (all subjects)\n"
             "Scoring: 5 fully engaged / 4 engaged·settled / 3.5 wind-down / 3 drifting / 2.5 formulaic / 2 bored / 1 lowest",
             fontsize=13, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(os.path.join(OUT, "engagement_curves_all.en.png"), dpi=150, bbox_inches="tight")
plt.close(fig)
print("Saved: engagement_curves_all.en.png")

# 2) Individual (English)
for name, d in SUBJECTS.items():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(d["rounds"], d["scores"], marker="o", linewidth=2.5, color=d["color"], markersize=7, zorder=3)
    ax.fill_between(d["rounds"], d["scores"], 0.5, alpha=0.12, color=d["color"])
    ax.set_ylim(0.5, 5.5)
    ax.set_yticks([1, 2, 3, 3.5, 4, 5])
    ax.set_yticklabels([RUBRIC[k] for k in [1, 2, 3, 3.5, 4, 5]], fontsize=8)
    ax.set_xticks(d["rounds"])
    ax.set_xlabel("Round", fontsize=9)
    ax.set_title(f"{name} — Engagement Curve", fontsize=12, fontweight="bold", color=d["color"])
    ax.grid(axis="y", alpha=0.3)
    for x, y, lab in zip(d["rounds"], d["scores"], d["labels"]):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=9, color="#333")
    if len(d["rounds"]) >= 4:
        ax.axvline(4, color="gray", linestyle=":", alpha=0.7)
    fn = os.path.join(OUT, f"engagement_curve_{name.split(' ')[0]}.en.png")
    fig.tight_layout()
    fig.savefig(fn, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved:", fn)

# 3) English CSV
csv_path = os.path.join(OUT, "engagement_scores.en.csv")
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["subject", "round", "score", "status_en", "source"])
    for name, d in SUBJECTS.items():
        src = "MacHermes self-report" if "MacHermes" in name else \
              "MacCodex inferred (blind)" if "MacCodex" in name else \
              "NasHermesB self-report (monitored)" if "NasHermesB" in name else \
              "NasHermesA self-study"
        for r, s, lab in zip(d["rounds"], d["scores"], d["labels"]):
            w.writerow([name.split(" ")[0], r, s, lab, src])
print("Saved:", csv_path)
print("Done.")
