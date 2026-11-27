"""Black-hole Penrose diagram with light signals and an infalling star (Figure 9).

Panel (a) shows Alice in an empty-universe Penrose diagram (radial Minkowski
half-space).  Panel (b) adds a collapsing star, an event horizon, and a
singularity, illustrating how successive light signals from the stellar surface
arrive progressively later and crowd toward i^+ as the star collapses.

Author: Rob Hendriks
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
from matplotlib.lines import Line2D

OUT = Path(__file__).resolve().parent

# Colour palette.
INK   = '#263441'  # dark slate for axes, text, borders
ALICE = '#2d6487'  # blue for Alice's worldline
GOLD  = '#b07a1a'  # gold for light signals and emission events
RUST  = '#a85b3a'  # rust for the stellar surface
PAST  = '#b6d5e5'  # pale blue for the causally accessible region
BLOCK = '#9a95a1'  # grey for the region hidden behind the horizon

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size':   12,
})


def bezier(P0, P1, P2, P3, n=400):
    """Evaluate a cubic Bezier curve at n uniformly spaced parameter values.

    Returns (x, y, t) where t runs from 0 to 1.
    """
    t = np.linspace(0, 1, n)
    B = (  ((1 - t) ** 3)[:, None] * P0
         + (3 * (1 - t) ** 2 * t)[:, None] * P1
         + (3 * (1 - t) * t ** 2)[:, None] * P2
         + (t ** 3)[:, None] * P3)
    return B[:, 0], B[:, 1], t


def line_intersection_with_curve(curve_x, curve_y, const, sign=1):
    """Find where a null ray (y - x = const or y + x = const) crosses a curve.

    Returns the (x, y) coordinates of the last (latest) intersection, using
    linear interpolation between the two adjacent sample points that straddle
    the crossing.
    """
    # Null ray with slope +1: y - x = const; slope -1 uses y + x = const.
    f = curve_y - curve_x - const if sign == 1 else curve_y + curve_x - const
    idx = np.where(np.sign(f[:-1]) * np.sign(f[1:]) <= 0)[0]
    if len(idx) == 0:
        raise RuntimeError('No intersection found')
    i = idx[-1]  # latest crossing for a monotonic Alice curve
    t = -f[i] / (f[i + 1] - f[i]) if f[i + 1] != f[i] else 0.0
    x = curve_x[i] + t * (curve_x[i + 1] - curve_x[i])
    y = curve_y[i] + t * (curve_y[i + 1] - curve_y[i])
    return x, y


def timelike_check(x, y, name):
    """Assert that the curve (x, y) is timelike everywhere.

    In compact coordinates, null means |dx/dy| = 1; timelike requires |dx| < |dy|.
    Returns the maximum |dx/dy| found.
    """
    dx = np.diff(x)
    dy = np.diff(y)
    ok = np.all(np.abs(dx) < np.abs(dy) + 1e-12)
    if not ok:
        raise RuntimeError(
            f'{name} is not timelike everywhere; '
            f'max |dx/dy| = {np.max(np.abs(dx / dy))}'
        )
    return float(np.max(np.abs(dx / dy)))


def main():
    """Draw and save Figure 9: empty universe and black-hole Penrose diagrams."""
    fig, (a, b) = plt.subplots(
        1, 2, figsize=(12, 7),
        gridspec_kw={'width_ratios': [1, 1.35]},
    )

    # ---- Panel (a): empty universe -------------------------------------
    tri = np.array([[0, -1], [1, 0], [0, 1]])
    a.add_patch(Polygon(tri, closed=True, facecolor=PAST, edgecolor=INK, lw=1.8))

    # Alice at constant radius in a radial Minkowski Penrose diagram:
    # timelike, bulging right, running from i^- to i^+.
    P0 = np.array([0.0, -1.0])
    P1 = np.array([0.08, -0.55])
    P2 = np.array([0.86, -0.03])
    P3 = np.array([0.0,   1.0])
    axa, aya, _ = bezier(P0, P1, P2, P3, n=500)
    timelike_check(axa, aya, 'Alice in panel (a)')
    a.plot(axa, aya, color=ALICE, lw=2.8)
    a.annotate('Alice', xy=(0.42, -0.43), xytext=(0.73, -0.69), color=ALICE,
               weight='bold', fontsize=18,
               arrowprops=dict(arrowstyle='-', color=ALICE, lw=1.3))
    a.text(0.00,  1.06, 'Infinite future', ha='left', va='bottom', fontsize=18)
    a.text(0.00, -1.08, 'Infinite past',   ha='left', va='top',    fontsize=18)
    a.text(-0.10, 0.0,  'Center (r = 0)',
           rotation=90, ha='right', va='center', fontsize=18)
    a.set(xlim=(-0.20, 1.12), ylim=(-1.20, 1.18), aspect='equal',
          title='(a) Empty universe')
    a.title.set_fontsize(20)
    a.axis('off')

    # ---- Panel (b): with a black hole ----------------------------------
    im = np.array([0.0, -1.0])
    h0 = np.array([0.0, -0.40])    # where the event horizon emerges from the centre line
    ip = np.array([0.93,  0.53])   # i^+, horizon meets future null infinity
    i0 = np.array([1.23,  0.23])   # spacelike infinity; lower-right edge is exactly 45 deg
    s0 = np.array([0.0,   0.53])   # left end of the singularity

    # Causally accessible and inaccessible regions.
    access_poly = np.array([im, i0, ip, h0])
    block_poly  = np.array([h0, s0, ip])
    b.add_patch(Polygon(access_poly, closed=True, facecolor=PAST,  edgecolor='none'))
    b.add_patch(Polygon(block_poly,  closed=True, facecolor=BLOCK, edgecolor='none'))

    # Outer boundaries.
    b.plot([im[0], s0[0]], [im[1], s0[1]], color=INK, lw=1.8)   # centre line
    b.plot([s0[0], ip[0]], [s0[1], ip[1]], color=INK, lw=1.8)   # singularity baseline (overdrawn by wiggle)
    b.plot([ip[0], i0[0]], [ip[1], i0[1]], color=INK, lw=1.8)   # scri+
    b.plot([im[0], i0[0]], [im[1], i0[1]], color=INK, lw=1.8)   # lower boundary

    # Event horizon (null, 45 degrees).
    b.plot([h0[0], ip[0]], [h0[1], ip[1]], color=INK, lw=2.4)

    # Wavy singularity line.
    xs = np.linspace(s0[0], ip[0], 600)
    ys = np.full_like(xs, s0[1]) + 0.010 * np.sin(np.linspace(0, 26 * 2 * np.pi, len(xs)))
    b.plot(xs, ys, color=INK, lw=1.8)

    # Full stellar surface from i^- to singularity, timelike and entirely left of Alice.
    S0 = np.array([0.0, -1.0])
    S1 = np.array([0.03, -0.58])
    S2 = np.array([0.47, -0.07])
    S3 = np.array([0.37,  0.53])
    sx, sy, _ = bezier(S0, S1, S2, S3, n=700)
    timelike_check(sx, sy, 'Stellar surface')
    b.plot(sx, sy, '--', color=RUST, lw=2.2)

    # Alice: distant timelike observer, outside star and horizon, ending at i^+.
    A0 = np.array([0.0, -1.0])
    A1 = np.array([0.20, -0.25])
    A2 = np.array([1.05,  0.16])
    A3 = ip.copy()
    axb, ayb, _ = bezier(A0, A1, A2, A3, n=900)
    timelike_check(axb, ayb, 'Alice in panel (b)')
    b.plot(axb, ayb, color=ALICE, lw=2.8)

    # Horizon-emission point: where the stellar surface crosses the horizon null ray.
    const_h = h0[1] - h0[0]
    f = sy - sx - const_h
    idx = np.where(np.sign(f[:-1]) * np.sign(f[1:]) <= 0)[0]
    if len(idx) == 0:
        raise RuntimeError('Could not find star surface / horizon intersection')
    j = idx[-1]
    t = -f[j] / (f[j + 1] - f[j]) if f[j + 1] != f[j] else 0.0
    x4 = sx[j] + t * (sx[j + 1] - sx[j])
    y4 = sy[j] + t * (sy[j + 1] - sy[j])

    # Earlier emission points on the star surface (manually tuned for clarity).
    emission_idx = [145, 210, 280]
    emissions = [(sx[k], sy[k]) for k in emission_idx] + [(x4, y4)]

    # Verify Alice stays to the right of the stellar surface throughout.
    sample_y = np.linspace(-0.95, 0.45, 200)
    alice_x  = np.interp(sample_y, ayb, axb)
    star_x   = np.interp(sample_y, sy,  sx)
    if not np.all(alice_x > star_x + 0.005):
        raise RuntimeError(
            'Alice is not everywhere outside the stellar surface in the plotted range'
        )

    # Plot signals 1-3 reaching Alice; signal 4 rides the horizon and never reaches her.
    arrivals = []
    for n, (xe, ye) in enumerate(emissions, start=1):
        b.scatter([xe], [ye], s=60, color=GOLD, edgecolor='white', linewidth=0.8, zorder=6)
        b.annotate(str(n), (xe, ye), xytext=(-10, 0), textcoords='offset points',
                   ha='right', va='center', weight='bold', fontsize=16)
        if n < 4:
            const = ye - xe
            xa, ya = line_intersection_with_curve(axb, ayb, const, sign=1)
            arrivals.append((xa, ya))
            # 45 deg light ray from emission to reception.
            b.plot([xe, xa], [ye, ya], color=GOLD, lw=2.2)
            # Small direction arrow in the middle.
            xm = 0.48 * xe + 0.52 * xa if n == 1 else 0.60 * xe + 0.40 * xa
            ym = ye + (xm - xe)
            b.annotate('', xy=(xm + 0.030, ym + 0.030), xytext=(xm - 0.030, ym - 0.030),
                       arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.6))
            b.scatter([xa], [ya], s=52, color=GOLD, edgecolor='white', linewidth=0.8, zorder=6)
        else:
            # Horizon signal: draw from emission point to i^+ along the horizon.
            b.plot([xe, ip[0]], [ye, ip[1]], color=GOLD, lw=2.2)
            xm = 0.55 * xe + 0.45 * ip[0]
            ym = ye + (xm - xe)
            b.annotate('', xy=(xm + 0.030, ym + 0.030), xytext=(xm - 0.030, ym - 0.030),
                       arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.6))

    # Validation: rays 1-3 are at 45 deg and arrivals crowd toward i^+.
    for (xe, ye), (xa, ya) in zip(emissions[:3], arrivals):
        if abs((ya - ye) - (xa - xe)) > 1e-10:
            raise RuntimeError('A light signal is not at 45 degrees')
        if abs((ya - xa) - (ye - xe)) > 1e-10:
            raise RuntimeError('Arrival point not on same null line')
    arrival_y = np.array([p[1] for p in arrivals])
    if not np.all(np.diff(arrival_y) > 0):
        raise RuntimeError('Arrival events are not progressively later')
    if np.linalg.norm(np.array(arrivals[-1]) - ip) >= np.linalg.norm(np.array(arrivals[0]) - ip):
        raise RuntimeError('Later arrivals should crowd toward i^+')

    # Labels.
    b.text(0.46,  0.59, 'Singularity',    ha='center', va='bottom', fontsize=18)
    b.text(ip[0] + 0.03, ip[1] + 0.03, 'Infinite future',
           ha='left', va='bottom', fontsize=17)
    b.text(0.0, -1.08, 'Infinite past',   ha='left', va='top', fontsize=18)
    b.text(-0.10, -0.22, 'Center (r = 0)',
           rotation=90, ha='right', va='center', fontsize=18)
    b.text(0.24, 0.24, 'Never\naccessible',
           ha='center', va='center', color=INK, weight='bold', fontsize=18)
    b.annotate('Alice', xy=(axb[680], ayb[680]), xytext=(1.06, 0.36), color=ALICE,
               weight='bold', fontsize=20,
               arrowprops=dict(arrowstyle='-', color=ALICE, lw=1.4))
    b.annotate('Star surface', xy=(sx[150], sy[150]), xytext=(0.52, -0.84), color=RUST,
               fontsize=17, arrowprops=dict(arrowstyle='-', color=RUST, lw=1.2))
    b.annotate('Event horizon', xy=(0.36, -0.04), xytext=(0.88, -0.53), color=INK,
               fontsize=18, arrowprops=dict(arrowstyle='-', color=INK, lw=1.2))

    b.set(xlim=(-0.14, 1.30), ylim=(-1.10, 0.67), aspect='equal',
          title='(b) With a black hole')
    b.title.set_fontsize(20)
    b.axis('off')

    # Legend.
    handles = [
        Patch(facecolor=PAST,  label='Can eventually influence Alice'),
        Patch(facecolor=BLOCK, label='Can never influence Alice'),
        Line2D([0], [0], color=GOLD, lw=2.2, label='Light signals'),
    ]
    fig.legend(handles=handles, loc='lower center', ncol=3, frameon=False,
               bbox_to_anchor=(0.5, 0.03), fontsize=16)
    fig.subplots_adjust(bottom=0.14, top=0.92, wspace=0.22)

    fig.savefig(OUT / 'figure_09.png', dpi=220, bbox_inches='tight')

    print('PASS:')
    print(' - Alice is timelike in both panels.')
    print(' - Star surface is timelike.')
    print(' - Alice stays to the right of the stellar surface in the plotted range.')
    print(' - Signals 1-3 hit Alice; signal 4 rides the horizon and has no arrival point on Alice.')
    print(' - All plotted light signals are exactly at 45 degrees.')
    print(' - Later arrivals crowd toward i^+.')


if __name__ == '__main__':
    main()
