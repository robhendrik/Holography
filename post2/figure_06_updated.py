from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

OUT = Path(__file__).parent
INK = '#263441'
GOLD = '#a87520'
BLUE = '#456c83'
GRID = '#a8b0b6'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 12,
    'figure.facecolor': 'white'
})


def compact(r, t):
    u = np.arctan(t - r)
    v = np.arctan(t + r)
    return (v - u) / np.pi, (v + u) / np.pi


def ray(ax, x, y):
    ax.plot(x, y, color=GOLD, lw=2.5, zorder=6)
    for i, j in [(0, 1), (1, 2)]:
        a = np.array([x[i], y[i]])
        b = np.array([x[j], y[j]])
        p = a + 0.62 * (b - a)
        q = a + 0.84 * (b - a)
        ax.annotate('', q, p,
                    arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=2.2),
                    zorder=7)


def badge(ax, x, y, k):
    ax.text(
        x, y, str(k),
        ha='center', va='center', fontsize=10, color=INK, weight='bold',
        bbox=dict(boxstyle='circle,pad=.18', fc='white', ec=BLUE, lw=.8),
        zorder=10
    )


fig, axs = plt.subplots(
    1, 3, figsize=(12, 5.2),
    gridspec_kw={'width_ratios': [1.05, 1, 1]}
)
fig.subplots_adjust(left=.035, right=.97, bottom=.17, top=.86, wspace=.36)
a, b, c = axs

radii = [.5, 1.0, 1.5]
extent = 1.85
# Choose the center-crossing event at t = 0 for a cleaner, symmetric mapping.
tc = 0.0

# ------------------------------------------------------------------
# (a) Spherical space
# ------------------------------------------------------------------
for k, r in enumerate(radii, 1):
    a.add_patch(Circle((0, 0), r, facecolor=BLUE, edgecolor='none', alpha=.055))
    a.add_patch(Circle((0, 0), r, fill=False, edgecolor=BLUE, lw=1.15))
    q = np.linspace(0, 2 * np.pi, 500)
    a.plot(r * np.cos(q), .28 * r * np.sin(q), color=BLUE, lw=.8, alpha=.6)
    badge(a, r * .64, r * .768, k)

# In ordinary space the radial light ray is a straight line through the center.
a.plot([-extent, extent], [0, 0], color=GOLD, lw=2.5, zorder=6)
# Both arrows point right: the ray travels through, not away from, the center.
spatial_arrows = []
for x in (-1.15, 1.15):
    start, end = (x - .17, 0), (x + .17, 0)
    spatial_arrows.append(a.annotate('', xy=end, xytext=start,
        arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=2.2), zorder=7))
assert all(arrow.xy[0] > arrow.get_position()[0] for arrow in spatial_arrows)
a.scatter(0, 0, color=INK, s=22, zorder=9)
a.text(0, -.17, 'Center', ha='center', va='top', fontsize=11)
a.set(xlim=(-2.02, 2.02), ylim=(-1.9, 1.9), aspect='equal')
a.axis('off')
a.set_title('(a) Spherical space', pad=13)
a.text(.5, -.07, 'Three spherical shells', transform=a.transAxes, ha='center', fontsize=11)

# ------------------------------------------------------------------
# (b) Radial spacetime
# ------------------------------------------------------------------
b.set(
    xlim=(-.13, 2.15), ylim=(-2.55, 2.55), aspect='equal',
    xlabel='Radius, r', ylabel='Time, ct'
)
b.set_xticks([])
b.set_yticks([])
b.spines[['top', 'right', 'left']].set_visible(False)
b.spines['bottom'].set_color(GRID)
for t in [-2, -1, 0, 1, 2]:
    b.hlines(t, 0, 2.15, color=GRID, lw=.65, alpha=.45)
for k, r in enumerate(radii, 1):
    b.vlines(r, -2.55, 2.55, color=BLUE, lw=1.25)
    badge(b, r, 1.92, k)
b.axvline(0, color=INK, lw=1.7)
center_label = b.text(.08, -1.65, 'Center', rotation=90, ha='left', va='center', fontsize=10)

# In radial coordinates r >= 0, the same light ray becomes two null segments
# meeting at r = 0. For clarity we place the turning point at t = 0.
rr = np.array([extent, 0, extent])
tt = np.array([tc - extent, tc, tc + extent])
ray(b, rr, tt)
b.scatter(0, tc, color=INK, s=22, zorder=9)

b.set_title('(b) Radial spacetime', pad=13)
b.text(.5, -.15, 'Each line follows one shell', transform=b.transAxes, ha='center', fontsize=11)

# ------------------------------------------------------------------
# (c) Penrose diagram
# ------------------------------------------------------------------
c.add_patch(Polygon([(0, -1), (1, 0), (0, 1)], facecolor='#f0f3f5', edgecolor=INK, lw=1.5))
s = np.sinh(np.linspace(-12, 12, 2400))
rs = np.sinh(np.linspace(0, 12, 1400))
for t in [-2, -1, 0, 1, 2]:
    c.plot(*compact(rs, np.full_like(rs, t)), color=GRID, lw=.65, alpha=.55)
for k, r in enumerate(radii, 1):
    c.plot(*compact(np.full_like(s, r), s), color=BLUE, lw=1.25)
    x_badge, y_badge = compact(r, 0)
    badge(c, x_badge, y_badge, k)

# The compactified image of the same symmetric radial null ray.
X, T = compact(rr, tt)
ray(c, X, T)
c.scatter(X[1], T[1], color=INK, s=22, zorder=9)
c.text(-.045, -.15, 'Center', rotation=90, ha='right', va='center', fontsize=10)
c.set(xlim=(-.16, 1.12), ylim=(-1.08, 1.08), aspect='equal')
c.axis('off')
c.set_title('(c) Penrose diagram', pad=13)
c.text(.5, -.07, 'The same three shells', transform=c.transAxes, ha='center', fontsize=11)

# ------------------------------------------------------------------
# Validation
# ------------------------------------------------------------------
# In panel (b), each segment is null: |Δr| = |Δt|.
assert np.allclose(np.abs(np.diff(rr)), np.diff(tt))
# In panel (c), the compactified null ray still sits at 45 degrees.
assert np.allclose(np.abs(np.diff(X)), np.diff(T))
# The turning point is centered for pedagogical clarity.
assert np.isclose(tt[1], 0.0)
assert np.isclose(T[1], 0.0)

fig.canvas.draw()
renderer = fig.canvas.get_renderer()
assert not center_label.get_window_extent(renderer).overlaps(b.yaxis.label.get_window_extent(renderer))

for ext in ['png', 'svg']:
    fig.savefig(OUT / f'figure_06.{ext}', dpi=220, bbox_inches='tight', pad_inches=.18)

print('PASS: symmetric null ray, both spatial arrows point right, and center/time labels do not overlap.')
