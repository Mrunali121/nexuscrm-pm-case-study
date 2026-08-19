"""
Generates the roadmap Gantt chart and sprint velocity chart for the
NexusCRM case study.

Included in the repo so both charts' underlying data (phase dates, sprint
commitments, the Sprint 3 dependency issue) are transparent and
reproducible, not just static images.

Usage:
    pip install matplotlib
    python generate_charts.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Phase: (label, start_week, end_week, color)
PHASES = [
    ("Initiation",             0, 0.5,  "#5B6472"),
    ("Planning",               0.5, 2,  "#5B6472"),
    ("Design",                 2, 3,    "#5B6472"),
    ("R1: Sprint 1",           3, 5,    "#0E8F7E"),
    ("R1: Sprint 2",           5, 7,    "#0E8F7E"),
    ("R1: Sprint 3",           6, 8,    "#0E8F7E"),
    ("R1: Sprint 4",           7, 8.5,  "#0E8F7E"),
    ("R1 Launch",              8, 8.5,  "#0B7A6C"),
    ("R2: Sprint 5",           9, 11,   "#E2963A"),
    ("R2: Sprint 6",           11, 13,  "#E2963A"),
    ("R2: Sprint 7",           13, 15,  "#E2963A"),
    ("R2: Sprint 8",           15, 16.5, "#E2963A"),
    ("Security/GDPR Audit",    15, 16,  "#14213D"),
    ("R2 Launch",              16, 16.5, "#B5711F"),
    ("Parallel-Run & Closure", 16.5, 18, "#5B6472"),
]

# Sprint velocity: committed vs. completed story points per sprint.
# Sprint 3 completed short because of the WebSocket dependency issue
# (I-01, see 11-risk-issue-register.md) — absorbed by Sprint 4's slack.
SPRINTS = [f"S{i}" for i in range(1, 9)]
COMMITTED = [11, 23, 21, 16, 8, 10, 18, 24]
COMPLETED = [11, 23, 13, 24, 8, 10, 18, 24]


def build_roadmap_chart(output_path: str = "roadmap-chart.png") -> None:
    fig, ax = plt.subplots(figsize=(11, 5.3))

    for i, (label, start, end, color) in enumerate(PHASES):
        y = len(PHASES) - i
        ax.barh(y, end - start, left=start, height=0.6, color=color, edgecolor="white")
        ax.text(start - 0.15, y, label, ha="right", va="center",
                 fontsize=9, family="monospace", color="#14213D")

    ax.set_xlim(0, 19)
    ax.set_ylim(-2.2, len(PHASES) + 1)
    ax.set_xlabel("Project Week", fontsize=10)
    ax.set_yticks([])
    ax.set_title("NexusCRM Roadmap — 18-Week Timeline", fontsize=14,
                  fontweight="bold", loc="left")
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.grid(axis="x", linestyle=":", alpha=0.4)

    legend_patches = [
        mpatches.Patch(color="#5B6472", label="Governance / Closure"),
        mpatches.Patch(color="#0E8F7E", label="Release 1"),
        mpatches.Patch(color="#E2963A", label="Release 2"),
    ]
    ax.legend(handles=legend_patches, loc="lower left", bbox_to_anchor=(0, -0.02),
              fontsize=9, frameon=False, ncol=3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"Saved {output_path}")
    plt.close(fig)


def build_velocity_chart(output_path: str = "release-velocity-chart.png") -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    x = range(len(SPRINTS))

    ax.bar([i - 0.18 for i in x], COMMITTED, width=0.36, color="#D4D9D6", label="Committed")
    ax.bar([i + 0.18 for i in x], COMPLETED, width=0.36, color="#0E8F7E", label="Completed")
    ax.set_xticks(list(x))
    ax.set_xticklabels(SPRINTS, family="monospace")
    ax.set_ylabel("Story Points")
    ax.set_title("Sprint Velocity — Committed vs. Completed", fontsize=14,
                  fontweight="bold", loc="left")

    ax.annotate(
        "Sprint 3 dependency\nissue (I-01) absorbed\nby Sprint 4 slack",
        xy=(2.18, 13), xytext=(2.6, 4),
        arrowprops=dict(arrowstyle="->", color="#B5711F"),
        fontsize=8.5, color="#8A5217",
        bbox=dict(boxstyle="round,pad=0.35", fc="#FCEFDD", ec="#E2963A"),
    )

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    ax.legend(frameon=False, fontsize=9)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    print(f"Saved {output_path}")
    plt.close(fig)


if __name__ == "__main__":
    build_roadmap_chart()
    build_velocity_chart()
