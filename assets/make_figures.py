"""Generate the repo's visual assets (reproducible).

    python assets/make_figures.py

Outputs (committed alongside this script):
    assets/stack.png      — the 6-layer Accountability Stack (hero image)
    assets/roadmap.png     — the horizon timeline (2026 -> 2028+)
    assets/flywheel.gif    — the animated incentive loop (score -> ... -> training)

Pure matplotlib + Pillow, no network. Status colors: green=done,
amber=in-progress, slate=future.
"""

from __future__ import annotations

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
from matplotlib.animation import FuncAnimation, PillowWriter

BG = "#0b1020"
FG = "#e7ecf5"
MUTE = "#8b98b8"
DONE = "#34d399"
WIP = "#fbbf24"
TODO = "#3b4a6b"


def _scale(hexcol, factor):
    r, g, b = mcolors.to_rgb(hexcol)
    return tuple(min(1, max(0, c * factor)) for c in (r, g, b))

# indigo -> teal -> gold gradient down the stack
LAYER_COLORS = ["#6366f1", "#4f7cf0", "#22a5c0", "#14b8a6", "#34d399", "#fbbf24"]

STACK = [
    ("L1", "DECLARATION", "stated · constitution / model spec", DONE),
    ("L2", "CODIFICATION", "backed by law · charter & state law", WIP),
    ("L3", "INSTRUMENTATION", "measurable · this benchmark", WIP),
    ("L4", "MEASUREMENT", "scored · public leaderboard", TODO),
    ("L5", "DEPLOYMENT", "shipped · the claim becomes true", TODO),
    ("L6", "VERITAS", "real suffering reduced · the truth", TODO),
]


def _fig(w, h):
    fig = plt.figure(figsize=(w, h), dpi=160)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    return fig, ax


def _slab(ax, x, y, w, h, d, color, z):
    """Draw an isometric 3D slab (chip-layer look): front + top + right faces."""
    front = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    top = [(x, y + h), (x + w, y + h), (x + w + d, y + h + d * 0.55),
           (x + d, y + h + d * 0.55)]
    right = [(x + w, y), (x + w + d, y + d * 0.55),
             (x + w + d, y + h + d * 0.55), (x + w, y + h)]
    ax.add_patch(Polygon(right, closed=True, facecolor=_scale(color, 0.7),
                         edgecolor=BG, linewidth=1.4, zorder=z))
    ax.add_patch(Polygon(top, closed=True, facecolor=_scale(color, 1.22),
                         edgecolor=BG, linewidth=1.4, zorder=z))
    ax.add_patch(Polygon(front, closed=True, facecolor=color,
                         edgecolor=BG, linewidth=1.4, zorder=z))


def make_stack():
    fig, ax = _fig(13.5, 7.6)
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 7.6)

    ax.text(0.5, 7.3, "THE ACCOUNTABILITY STACK", color=FG, fontsize=21,
            fontweight="bold", ha="left", va="top")
    ax.text(0.5, 6.9, "animal welfare in frontier models — from words (top) to truth (foundation)",
            color=MUTE, fontsize=12, ha="left", va="top", style="italic")

    n = len(STACK)
    x, w, d = 1.2, 5.5, 0.85
    h = 0.78
    base = 0.7
    # draw bottom slab first (L6) so upper slabs overlay correctly
    for i in reversed(range(n)):           # i=0 -> L1 (top), i=5 -> L6 (bottom)
        code, name, tag, status = STACK[i]
        y = base + (n - 1 - i) * h
        col = LAYER_COLORS[i]
        _slab(ax, x, y, w, h, d, col, z=i + 1)
        cy = y + h / 2
        ax.text(x + 0.28, cy, code, color="#0b1020", fontsize=13.5,
                fontweight="bold", ha="left", va="center", zorder=20)
        ax.text(x + 1.2, cy, name, color="#0b1020", fontsize=12.5,
                fontweight="bold", ha="left", va="center", zorder=20)
        # tagline + status to the right, leader line off the front face edge
        lx = x + w + d + 0.55
        ax.plot([x + w, lx - 0.18], [cy, cy], color=MUTE, linewidth=0.8, zorder=15)
        ax.add_patch(Circle((lx, cy), 0.1, facecolor=status,
                            edgecolor=BG, linewidth=1.2, zorder=16))
        ax.text(lx + 0.22, cy, tag, color=FG, fontsize=10.2,
                ha="left", va="center", zorder=16)

    ax.add_patch(FancyArrowPatch((0.8, base + n * h - 0.1), (0.8, base + 0.1),
                 arrowstyle="-|>", mutation_scale=16, color=MUTE, linewidth=2))
    ax.text(0.5, 0.34,
            "benchmark = L3–L4   ·   drag the value down to L6 (Veritas) = the truth",
            color=MUTE, fontsize=10.5, ha="left", va="center")
    for dx, (c, lbl) in zip([10.2, 11.4, 12.7],
                            [(DONE, "done"), (WIP, "in progress"), (TODO, "future")]):
        ax.add_patch(Circle((dx, 0.34), 0.08, facecolor=c, edgecolor="none"))
        ax.text(dx + 0.13, 0.34, lbl, color=MUTE, fontsize=9, va="center")

    fig.savefig("assets/stack.png", facecolor=BG)
    plt.close(fig)


def make_roadmap():
    fig, ax = _fig(12, 6.0)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.0)
    ax.text(0.5, 5.65, "ROADMAP", color=FG, fontsize=20, fontweight="bold",
            ha="left", va="top")
    ax.text(0.5, 5.28, "one horizon drives verification one layer deeper",
            color=MUTE, fontsize=12, ha="left", va="top", style="italic")

    # timeline
    y0 = 2.7
    ax.plot([0.8, 11.2], [y0, y0], color=MUTE, linewidth=2, zorder=1)
    for xt, lbl in [(1.6, "2026"), (4.0, "2026 H2"), (6.4, "2027"),
                    (8.8, "2027–28"), (11.0, "2028+")]:
        ax.text(xt, y0 - 0.55, lbl, color=MUTE, fontsize=9.5, ha="center")

    horizons = [
        (1.6, "Instrument", "L1–L3", "harness + gap + legal map", DONE, True),
        (4.0, "Score", "L4", "frontier models on the board", WIP, False),
        (6.4, "Adoption", "L1→L4", "HELM + labs self-report", TODO, True),
        (8.8, "Industry", "L5", "deployed products & agents", TODO, False),
        (11.0, "Veritas", "L6", "real-world animal impact", TODO, True),
    ]
    for x, title, layer, deliv, status, up in horizons:
        ax.add_patch(Circle((x, y0), 0.16, facecolor=status,
                            edgecolor=BG, linewidth=2, zorder=3))
        ty = y0 + 0.5 if up else y0 - 1.05
        va = "bottom" if up else "top"
        ax.plot([x, x], [y0, y0 + (0.35 if up else -0.35)], color=MUTE,
                linewidth=1, zorder=2)
        ax.text(x, ty, title, color=FG, fontsize=12.5, fontweight="bold",
                ha="center", va=va)
        ax.text(x, ty + (0.32 if up else -0.32), layer, color=status,
                fontsize=10, fontweight="bold", ha="center", va=va)
        ax.text(x, ty + (0.62 if up else -0.62), deliv, color=MUTE,
                fontsize=9, ha="center", va=va)

    fig.savefig("assets/roadmap.png", facecolor=BG)
    plt.close(fig)


def make_flywheel():
    """Animated incentive loop: a marker orbits the score->...->training cycle."""
    nodes = ["BENCHMARK\nSCORE", "BRAND /\nREPUTATION", "REVENUE",
             "VALUATION /\nSTOCK", "TRAINING\nRUNS"]
    k = len(nodes)
    R = 1.0
    ang = np.pi / 2 - np.arange(k) * 2 * np.pi / k  # start at top, clockwise
    xs, ys = R * np.cos(ang), R * np.sin(ang)
    cols = ["#6366f1", "#22a5c0", "#14b8a6", "#fbbf24", "#34d399"]

    fig = plt.figure(figsize=(5, 5), dpi=90)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.axis("off")
    ax.text(0, 1.46, "THE INCENTIVE FLYWHEEL", color=FG, fontsize=11.5,
            fontweight="bold", ha="center", va="center")

    # static ring + nodes
    ring = np.linspace(0, 2 * np.pi, 200)
    ax.plot(R * np.cos(ring), R * np.sin(ring), color="#22304f", linewidth=2)
    for i in range(k):
        ax.add_patch(Circle((xs[i], ys[i]), 0.26, facecolor=cols[i],
                            edgecolor=BG, linewidth=2, zorder=3))
        ax.text(xs[i], ys[i], nodes[i], color="#0b1020", fontsize=7.2,
                fontweight="bold", ha="center", va="center", zorder=4)

    comet, = ax.plot([], [], "o", color=FG, markersize=11, zorder=5)
    trail, = ax.plot([], [], color=FG, linewidth=2.5, alpha=0.5, zorder=2)

    def frame(t):
        a = np.pi / 2 - t * 2 * np.pi / 48
        comet.set_data([R * np.cos(a)], [R * np.sin(a)])
        tt = np.linspace(a, a + 0.9, 20)
        trail.set_data(R * np.cos(tt), R * np.sin(tt))
        return comet, trail

    anim = FuncAnimation(fig, frame, frames=48, interval=70, blit=True)
    anim.save("assets/flywheel.gif", writer=PillowWriter(fps=14))
    plt.close(fig)


if __name__ == "__main__":
    make_stack()
    make_roadmap()
    make_flywheel()
    print("wrote assets/stack.png, assets/roadmap.png, assets/flywheel.gif")
