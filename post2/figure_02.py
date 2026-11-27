"""Coordinate compactification diagrams (Figure 2).

Panel (a) illustrates how arctan maps an infinite axis to a finite interval.
Panel (b) shows the resulting Penrose diamond when both null coordinates
are compactified.

Author: Rob Hendriks
"""
from spacetime import *

# Output directory is the same folder as this script.
OUT = Path(__file__).parent


def main():
    """Draw and save Figure 2: compactification overview."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.8), layout='constrained')

    # Panel (a): one-dimensional arctan compression of a single infinite axis.
    s = np.linspace(-12, 12, 1000)
    a.plot(s, 2 * np.arctan(s) / np.pi, color=PAST, lw=2.5)
    for y in [-1, 1]:
        a.axhline(y, color=INK, ls='--', lw=1)   # asymptotic boundaries at +/-1
    a.set(
        xlabel='Original coordinate, s',
        ylabel=r'Compressed coordinate, $(2/\pi)\arctan(s)$',
        ylim=(-1.13, 1.13),
        title='(a) Compress an infinite axis',
    )
    a.set_yticks([-1, 0, 1])
    a.grid(alpha=.15)

    # Panel (b): two-dimensional Penrose diagram formed by compactifying both
    # null coordinates simultaneously.
    diamond(b)
    grid(b)
    b.set_title('(b) Compress both light coordinates')

    # Label the four boundary points (corners) of the diamond.
    corners = [
        (( 0,  1.04), 'Infinite future'),
        (( 0, -1.08), 'Infinite past'),
        (( 1.02,  0), 'Spatial\ninfinity\n$x\\to+\\infty$'),
        ((-1.02,  0), 'Spatial\ninfinity\n$x\\to-\\infty$'),
    ]
    for (cx, cy), label in corners:
        if cx == 0:
            ha = 'center'
        elif cx > 0:
            ha = 'left'
        else:
            ha = 'right'
        b.text(cx, cy, label, ha=ha, va='center', fontsize=10)

    fig.savefig(OUT / 'figure_02.png', dpi=220, bbox_inches='tight', pad_inches=.18)


if __name__ == '__main__':
    main()
