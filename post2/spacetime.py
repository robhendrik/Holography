"""Shared plotting utilities and exact null-coordinate compactification (c = 1).

Imported with ``from spacetime import *`` by the individual figure scripts.
Provides the Penrose compactification map, common colour constants, matplotlib
defaults, and helper functions for drawing diamonds, grids, light cones, and
ordinary Minkowski axes.

Author: Rob Hendriks
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Output directory used by the save() helper (not called by individual figure scripts).
OUT = Path(__file__).resolve().parent / 'output'

# Colour palette shared across all figures.
PAST   = '#459bc9'  # blue tint for past light-cone regions
FUTURE = '#e6ad51'  # gold tint for future light-cone regions
INK    = '#263441'  # dark slate for axes, text, and borders
GRAY   = '#e9edf0'  # light grey background inside the Penrose diamond

plt.rcParams.update({
    'font.family':          'DejaVu Sans',
    'font.size':            12,
    'axes.labelsize':       13,
    'axes.titlesize':       14,
    'axes.spines.top':      False,
    'axes.spines.right':    False,
    'savefig.facecolor':    'white',
    'figure.facecolor':     'white',
})


def compact(x, t):
    """Apply the Penrose compactification to Minkowski coordinates (x, t).

    Maps the entire plane onto the open diamond by passing through null
    coordinates U = arctan(t - x) and V = arctan(t + x).  Outgoing and
    incoming null rays retain slopes +/-1 in the compactified picture.

    Parameters
    ----------
    x, t : array-like
        Spatial position and time in units where c = 1.

    Returns
    -------
    X, T : ndarray
        Compactified coordinates scaled so that the boundary of the diamond
        lies at |X| + |T| = 1.
    """
    U = np.arctan(t - x)
    V = np.arctan(t + x)
    return (V - U) / np.pi, (V + U) / np.pi


def polygon(ax, vertices, color, alpha=1, **kw):
    """Fill a closed polygon on *ax* with no edge colour."""
    ax.add_patch(
        Polygon(vertices, closed=True, facecolor=color,
                alpha=alpha, edgecolor='none', **kw)
    )


def diamond(ax):
    """Draw the Penrose diamond boundary and grey background on *ax*."""
    polygon(ax, [(0, -1), (1, 0), (0, 1), (-1, 0)], GRAY, zorder=0)
    ax.plot([0, 1, 0, -1, 0], [-1, 0, 1, 0, -1], color=INK, lw=1.6, zorder=5)
    ax.set(xlim=(-1.13, 1.13), ylim=(-1.13, 1.13), aspect='equal')
    ax.axis('off')


def grid(ax):
    """Overlay compactified coordinate lines on the Penrose diamond."""
    # Dense sinh-spaced sample to cover the diamond smoothly near the boundary.
    s = np.sinh(np.linspace(-12, 12, 1601))
    for k in [-10, -3, -1, 0, 1, 3, 10]:
        ax.plot(*compact(np.full_like(s, k), s), color=INK, alpha=.19, lw=.8, zorder=2)
        ax.plot(*compact(s, np.full_like(s, k)), color=INK, alpha=.19, lw=.8, zorder=2)


def past_diamond(ax, T, color=PAST, alpha=0.30):
    """Shade the causal past of the event (0, T) inside the Penrose diamond.

    Fills the region that can causally influence the event at Penrose
    time T on Alice's worldline, and draws the light-cone boundary.
    """
    a = (1 + T) / 2
    polygon(
        ax,
        [(0, -1), (a, (T - 1) / 2), (0, T), (-a, (T - 1) / 2)],
        color, alpha, zorder=1,
    )
    # Light-cone boundary at the top of the shaded region.
    ax.plot([-a, 0, a], [(T - 1) / 2, T, (T - 1) / 2],
            color=color, lw=1.7, zorder=3)


def worldline(ax):
    """Draw Alice's worldline at x = 0 from infinite past to infinite future."""
    ax.plot([0, 0], [-1, 1], color=INK, lw=1.5, zorder=4)


def save(fig, name):
    """Save *fig* as a PNG file in the output subdirectory, then close it."""
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / f'{name}.png', dpi=220, bbox_inches='tight', pad_inches=.15)
    plt.close(fig)


def ordinary(ax, lim=4):
    """Configure *ax* as an ordinary Minkowski spacetime diagram.

    Sets equal-aspect Cartesian axes with labelled position and time axes
    and no tick marks, leaving room for the caller to add content.
    """
    ax.set(
        xlim=(-lim, lim), ylim=(-lim, lim),
        aspect='equal',
        xlabel='Position, x',
        ylabel='Time, ct',
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines[['left', 'bottom']].set_color(INK)
