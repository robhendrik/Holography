"""Thumbnail image based on the calculated Figure 7 Penrose diagram (feature image).

Renders the same dust-collapse Penrose chart as Figure 7b, but without title or
annotations, sized and cropped for use as a post feature image.

Author: Rob Hendriks
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

OUT = Path(__file__).resolve().parent

# Colour palette (matches figure_07.py).
INK  = '#263441'  # dark slate for axes, text, borders
STAR = '#cab8a8'  # dusty rose for the stellar interior
RUST = '#995b43'  # rust for the stellar surface
GOLD = '#a87526'  # gold for outgoing null rays
BLUE = '#e8eff3'  # pale blue for the exterior region

# Set to True to overlay star and singularity labels (useful for inspection).
SHOW_LABELS = False


def P(p):
    """Smooth compactification function: P(p) = (2/pi) * arctan(p / 1.5)."""
    return 2 / np.pi * np.arctan(np.asarray(p) / 1.5)


def xy(p, q):
    """Convert Penrose null coordinates (p, q) to Cartesian (x, y)."""
    return (q - P(p)) / 2, (q + P(p)) / 2


# Height of the future null-infinity boundary in the Penrose chart.
H = float(-P(-3))


def main():
    """Draw and save the feature image."""
    fig = plt.figure(figsize=(12, 6.75), facecolor='white')
    ax  = fig.add_axes([.04, .04, .92, .92])
    ax.set_aspect('equal')
    ax.axis('off')

    im = (0, -1)
    i0 = ((H + 1) / 2, (H - 1) / 2)
    ip = (H, 0)

    # Exterior (vacuum) region.
    ax.add_patch(Polygon([im, i0, ip, (0, 0)], facecolor=BLUE, edgecolor='none'))

    # Stellar interior region.
    e  = -np.geomspace(1e5, 1e-9, 2400)
    sx, sy = xy(e - 1, P(e + 1))
    sx = np.r_[0, sx, P(1)]
    sy = np.r_[-1, sy, 0]
    ax.add_patch(Polygon(
        np.vstack([np.column_stack([sx, sy]), [0, 0], im]),
        facecolor=STAR, edgecolor='none',
    ))

    # Boundaries: outer edge, centre line, stellar surface, singularity, horizon.
    ax.plot([0, i0[0], ip[0]], [-1, i0[1], 0], color=INK, lw=3)
    ax.plot([0, 0], [-1, 0], color=INK, lw=3)
    ax.plot(sx, sy, '--', color=RUST, lw=3)
    xx = np.linspace(0, H, 700)
    ax.plot(xx, .009 * np.sin(2 * np.pi * xx / H * 23), color=INK, lw=3)
    ax.plot([0, H], [-H, 0], color=INK, lw=3)

    # Three outgoing null rays (same null-coordinate map as figure_07.py;
    # emission radii are slightly more separated for thumbnail clarity).
    for re, style in [(2.5, '-'), (1., '--'), (.48, '-.')]:
        p  = -2 * np.sqrt(re) - 1
        q0 = P(p + 2)
        qe = H if re >= 1 else -P(p)
        x, y = xy(p, np.linspace(q0, qe, 500))

        # Validation: null slope, endpoint constraints.
        assert np.allclose(np.diff(x), np.diff(y), atol=1e-12)
        if re < 1:
            assert np.isclose(y[-1], 0)
        elif re > 1:
            assert np.isclose(x[-1] + y[-1], H)
        else:
            assert np.allclose([x[-1], y[-1]], ip)

        ax.plot(x, y, style, color=GOLD, lw=3.5, zorder=5)
        ax.scatter(x[0], y[0], s=65, color=GOLD, zorder=6)
        k = 300
        ax.annotate('', xy=(x[k], y[k]), xytext=(x[k - 40], y[k - 40]),
                    arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=2,
                                   mutation_scale=20), zorder=7)

    if SHOW_LABELS:
        ax.text(.12, -.30, 'Star',        ha='center', fontsize=19, color=INK)
        ax.text(H / 2, .045, 'Singularity', ha='center', fontsize=19, color=INK)

    ax.set(xlim=(-.12, i0[0] + .12), ylim=(-1.08, .10))
    fig.savefig(OUT / 'holography_post2_feature.png', dpi=160, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
