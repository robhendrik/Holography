"""Animated morph from a radius-time diagram to a Penrose diagram (Figure 8 GIF).

Morphs the matched dust-collapse chart from figure_07.py by continuously
interpolating between Painleve-Gullstrand (PG) coordinates and the Penrose
compactification.  Finite events use a common interpolation; infinity is shown
only at the final frame.

Dependencies: numpy, scipy, matplotlib, pillow.

Author: Rob Hendriks
"""
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from scipy.optimize import brentq

# Import coordinate functions and colour constants from the companion script.
from figure_07 import (R, ts, F, G, LV, LU, P, Q, xy, H,
                       INK, STAR, RUST, GOLD, BLUE)

OUT = Path(__file__).resolve().parent


# ------------------------------------------------------------------
# Coordinate mapping helpers
# ------------------------------------------------------------------

def p_label(t, r):
    """Outgoing null label p for the event (t, r).

    Follows the null ray continuously through the dust interior, using the
    same coordinate matching as figure_07.py.
    """
    if t < 0 and r <= R(t) + 1e-10:
        e = -2 * np.sqrt(R(t))
        return e - r / R(t)
    if abs(r - 1) < 1e-13:
        return -3.
    y = np.sqrt(r)
    z = np.log(abs(1 - y)) + (r + 2 * y - t) / 2
    if r < 1:
        if z >= -1e-13:
            return -1.
        if z < -30:
            return -3.
        return brentq(lambda e: LU(e) - z, -2 + 1e-14, 0) - 1
    lo = -4.
    while LU(lo) < z:
        lo *= 2
    return brentq(lambda e: LU(e) - z, lo, -2 - 1e-14) - 1


def paired(t, r, p, q):
    """Bundle PG coordinates (t, r) and Penrose coordinates (x, y) into one array.

    Returns an (N, 4) array with columns [r, t, x, y] where (x, y) = xy(p, q).
    """
    t, r, p, q = np.broadcast_arrays(t, r, p, q)
    x, y = xy(p, q)
    return np.column_stack((r, t, x, y))


# ------------------------------------------------------------------
# Parametric curves (stellar surface, centre, singularity, horizon, rays)
# ------------------------------------------------------------------

def surface(e):
    """Stellar surface as a function of dust label e."""
    return paired(ts(e), e ** 2 / 4, e - 1, P(e + 1))


def center(e):
    """Centre worldline (r = 0) as a function of dust label e."""
    return paired(ts(e), 0, e, P(e))


def dust_sing(chi):
    """Dust singularity at t = 0 parametrised by chi in [0, 1]."""
    return paired(0, 0, -chi, P(chi))


def vacuum_sing(e):
    """Vacuum singularity as a function of null label e."""
    return paired(-2 * LU(e), 0, e - 1, -P(e - 1))


def horizon_inside(e):
    """Event horizon inside the dust, parametrised by dust label e."""
    return paired(ts(e), e ** 2 / 4 * (e + 3), -3, P(2 * e + 3))


def horizon_out(t):
    """Event horizon in the exterior vacuum as a function of PG time t."""
    return paired(t, 1, -3, Q((t + G(1)) / 2))


def outgoing(re, tmax, rmax):
    """Compute an outgoing null ray emitted from radius re.

    Clips the ray at the PG-time and radius limits of the current viewport.
    Returns an (N, 4) paired array; asserts that the Penrose null slope is 1.
    """
    te = -2 / 3 * re ** 1.5
    p  = -2 * np.sqrt(re) - 1
    if re == 1:
        t = np.linspace(te, tmax, 450)
        r = np.ones_like(t)
    elif re > 1:
        end = rmax
        if te + F(end) - F(re) > tmax:
            end = brentq(lambda r: te + F(r) - F(re) - tmax, re, rmax)
        r = np.linspace(re, end, 450)
        t = te + F(r) - F(re)
    else:
        r = np.linspace(re, 0, 450)
        t = te + F(r) - F(re)
    q    = Q((t + G(r)) / 2)
    data = paired(t, r, p, q)
    assert np.max(abs(np.diff(data[:, 3]) - np.diff(data[:, 2]))) < 1e-12
    return data


# ------------------------------------------------------------------
# Pre-compute animation stages
# ------------------------------------------------------------------

# Total number of animation frames from first to last keyframe.
N = 35

stages = []
for s in np.linspace(0, 1, N):
    # The visible finite region grows only near the end, avoiding a false
    # identification of a finite viewport edge with infinity.
    grow  = 1 + 5 * s ** 10
    tmax  = 5 * grow
    rmax  = 4.6 * grow
    emin  = -np.cbrt(60 * grow)
    es    = np.linspace(emin, 0, 550)
    surf  = surface(es)
    ctr   = center(es)
    chi   = np.linspace(0, 1, 150)
    sing1 = dust_sing(chi)

    # Sanity checks on the dust singularity curve.
    assert np.all(sing1[:, :2] == 0)
    assert np.allclose(sing1[:, 3], 0)
    assert np.allclose(sing1[0],  ctr[-1])
    assert np.allclose(sing1[-1], surf[-1])

    # Vacuum singularity, ending at the same time limit as the PG view.
    eend  = brentq(lambda e: -2 * LU(e) - tmax, -2 + 1e-14, 0) if tmax < 55 else -2 + 1e-13
    sing2 = vacuum_sing(np.linspace(0, eend, 350))
    hi    = horizon_inside(np.linspace(-3, -2, 250))
    ho    = horizon_out(np.linspace(-2 / 3, tmax, 450))
    rays  = [outgoing(re, tmax, rmax) for re in (1.6, 1., .72)]

    # Dust fill uses the actual matched centre, surface, and singular boundary.
    dust  = np.vstack((ctr, sing1, surf[::-1]))
    stages.append((surf, ctr, sing1, sing2, hi, ho, rays, dust, grow))

# Set up figure and axes (global so that the draw() callback can access them).
fig, ax = plt.subplots(figsize=(7.0, 7.0), dpi=85)
fig.subplots_adjust(left=.13, right=.94, bottom=.15, top=.88)


def display(data, s, grow):
    """Interpolate between PG display coordinates and Penrose coordinates.

    At s = 0 the PG (r, t) columns are scaled isotropically; at s = 1 the
    exact Penrose (x, y) columns are used.  The PG scale shrinks smoothly as
    the visible domain expands (grow > 1) so the viewport stays fixed.
    """
    scale = .095 / (1 + .7 * (grow - 1))
    a = np.column_stack((data[:, 0] * scale, data[:, 1] * scale - .48))
    return (1 - s) * a + s * data[:, 2:]


# Verify that the dust singularity morphs correctly at every stage.
for i, stage in enumerate(stages):
    sg = stage[2]
    f  = i / (N - 1)
    z  = display(sg, f, stage[-1])
    assert np.isclose(np.ptp(z[:, 0]), f * P(1))
    assert np.ptp(z[:, 1]) < 1e-12


def draw(index):
    """Render one animation frame at the given stage index."""
    ax.clear()
    ax.set(xlim=(-.16, 1.04), ylim=(-1.08, .19), aspect='equal')
    ax.axis('off')

    s = index / (N - 1)
    surf, ctr, sg1, sg2, hi, ho, rays, dust, grow = stages[index]
    final = (index == N - 1)

    if final:
        # Show exact Penrose boundary at the final frame.
        ax.add_patch(Polygon(
            [(0, -1), ((H + 1) / 2, (H - 1) / 2), (H, 0), (0, 0)],
            facecolor=BLUE, edgecolor='none',
        ))
        ax.plot([0, (H + 1) / 2, H], [-1, (H - 1) / 2, 0], color=INK, lw=1.4)
        # Recompute surface and centre curves at full resolution for the final frame.
        es   = -np.geomspace(1e5, 1e-9, 1800)
        surf = surface(es)
        ctr  = center(es)
        dust = np.vstack(([[0, 0, 0, -1]], ctr, sg1, surf[::-1], [[0, 0, 0, -1]]))

    def d(a):
        """Apply display interpolation to a paired data array."""
        return display(a, s, grow)

    def line(a, **kw):
        """Plot a paired data curve with the current interpolation."""
        z = d(a)
        ax.plot(z[:, 0], z[:, 1], **kw)

    ax.add_patch(Polygon(d(dust), facecolor=STAR, edgecolor='none', alpha=.85))
    line(ctr,  color=INK,  lw=1.5)
    line(surf, color=RUST, lw=2,  ls='--')
    line(hi,   color=INK,  lw=2)
    line(ho,   color=INK,  lw=2)
    line(sg1,  color=INK,  lw=2,  ls=':')
    line(sg2,  color=INK,  lw=2,  ls=':')

    if final:
        ax.plot([0, H], [-H, 0], color=INK, lw=2)
        xx = np.linspace(0, H, 700)
        ax.plot(xx, .006 * np.sin(2 * np.pi * xx / H * 23), color=INK, lw=1.5)

    for j, (re, ray_data) in enumerate(zip((1.6, 1., .72), rays)):
        z = d(ray_data)
        if final and re >= 1:
            # Extend escaping and horizon rays to null infinity in the final frame.
            p  = -2 * np.sqrt(re) - 1
            xf, yf = xy(p, H)
            z = np.vstack((z, [xf, yf]))
        ax.plot(*z.T, color=GOLD, lw=2, ls=['-', '--', '-.'][j], zorder=5)
        ax.scatter(*z[0], s=23, color=GOLD, zorder=6)
        ax.annotate(
            str(j + 1), z[0],
            xytext=[(9, -12), (9, -3), (-15, 7)][j],
            textcoords='offset points', weight='bold', color=INK,
        )
        k = len(z) * 2 // 3
        ax.annotate('', xy=z[k], xytext=z[k - 25],
                    arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.2))

    # Labels follow real reference points rather than independently drawn geometry.
    e_star   = -4.0 + 2.4 * min(1., s * 3)
    chi_star = .42
    z_star   = d(paired(
        ts(e_star), chi_star * e_star ** 2 / 4,
        e_star - chi_star, P(e_star + chi_star),
    ))[0]
    ax.text(*z_star, 'Star', ha='center', va='center', color=INK, fontsize=10)

    z_hor = d(horizon_out(np.array([2.5])))[0]
    ax.annotate('Horizon', z_hor, xytext=(10, 8), textcoords='offset points', color=INK)

    if final:
        ax.text(H / 2, .035, 'Singularity', ha='center', color=INK)
    else:
        z_sing = d(vacuum_sing(np.array([-1.6])))[0]
        ax.annotate('Singularity', z_sing, xytext=(-10, 8),
                    textcoords='offset points', ha='right', color=INK)

    # Title changes with the morph progress.
    if index == 0:
        title = 'Radius and time'
    elif final:
        title = 'Penrose diagram'
    else:
        title = 'Changing coordinates'
    ax.set_title(title, fontsize=17, pad=10, color=INK)

    if index == 0:
        ax.annotate('Areal radius, r',  xy=(.45, -1.02), ha='center', color=INK)
        ax.annotate('PG time, ct',      xy=(-.13, -.45), rotation=90, ha='center', color=INK)

    ax.text(.5, -.045,
            '1  Escapes     •     2  Horizon     •     3  Trapped',
            transform=ax.transAxes, ha='center', fontsize=11, color=INK)
    ax.text(.5, -.085,
            'Same collapse — different representation',
            transform=ax.transAxes, ha='center', fontsize=10, color=INK)


if __name__ == '__main__':
    # Frame sequence: hold on first frame, morph through, hold on last, reverse.
    order = [0] * 12 + list(range(N)) + [N - 1] * 22 + list(range(N - 2, 0, -1))
    ani   = FuncAnimation(fig, draw, frames=order, interval=90, blit=False)
    ani.save(OUT / 'figure_08_morph.gif', writer=PillowWriter(fps=12))

    # Save representative still frames at start, middle, and end.
    for k in (0, N // 2, N - 1):
        draw(k)
        fig.savefig(OUT / f'frame_{k:02d}.png', dpi=110)
    draw(N - 1)
    fig.savefig(OUT / 'figure_08_morph_final.png', dpi=150)

    print('Saved GIF and final frame; sampled outgoing null slopes checked.')
