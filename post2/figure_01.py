"""Light-cone diagram in ordinary Minkowski coordinates (Figure 1).

Shows Alice's past and future light cones at the origin, illustrating
which spacetime regions can causally communicate with her present moment.

Author: Rob Hendriks
"""
from spacetime import *

# Output directory is the same folder as this script.
OUT = Path(__file__).parent


def main():
    """Draw and save Figure 1: Minkowski light-cone diagram."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ordinary(ax)

    # Shade causal regions: past cone (blue), future cone (gold), spacelike (grey).
    polygon(ax, [(-4, -4), ( 0,  0), ( 4, -4)], PAST,   .30)
    polygon(ax, [(-4,  4), ( 0,  0), ( 4,  4)], FUTURE, .32)
    polygon(ax, [(-4, -4), (-4,  4), ( 0,  0)], GRAY)
    polygon(ax, [( 4, -4), ( 4,  4), ( 0,  0)], GRAY)

    # Light-cone boundary lines (45 deg null rays) and Alice's dashed worldline.
    ax.plot([-4, 4], [-4,  4], color=INK, lw=1.4)
    ax.plot([-4, 4], [ 4, -4], color=INK, lw=1.4)
    ax.plot([ 0, 0], [-4,  4], color=INK, ls='--', lw=1)

    # Mark Alice's present event and label it.
    ax.scatter(0, 0, color=INK, s=36, zorder=5)
    ax.annotate('Alice now', (0, 0), xytext=(9, 7), textcoords='offset points')

    # Region labels.
    ax.text(0, -2.7, 'Can influence\nAlice',  ha='center', va='center', color=INK)
    ax.text(0,  2.7, 'Alice can\ninfluence',  ha='center', va='center', color=INK)
    for x in [-2.8, 2.8]:
        ax.text(x, 0, 'Neither', ha='center', va='center', color=INK)
    ax.text(2.6, 3.0, 'Light', rotation=45, ha='center', fontsize=11)

    fig.savefig(OUT / 'figure_01.png', dpi=220, bbox_inches='tight', pad_inches=.18)


if __name__ == '__main__':
    main()
