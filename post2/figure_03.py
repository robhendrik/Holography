"""Inertial observers and a light signal in Minkowski spacetime (Figure 3).

Shows the same physical scene -- Alice, Bob, and a light signal -- first in
ordinary Minkowski coordinates and then in the Penrose compactification.
The light signal travels at 45 degrees in both representations.

Author: Rob Hendriks
"""
from spacetime import *

# Output directory is the same folder as this script.
OUT = Path(__file__).parent

# Observer parameters.
BETA   = 0.28       # Bob's velocity relative to Alice, in units of c
BOB    = '#a34f32'  # colour for Bob's worldline and events
ALICE  = '#245778'  # colour for Alice's worldline and events
SIGNAL = '#ba8b20'  # colour for the light signal

# Derived event coordinates: Alice emits at t = 1; Bob receives when t - 1 = beta * t.
t_receive = 1 / (1 - BETA)
x_receive = BETA * t_receive


def main():
    """Draw and save Figure 3: Minkowski spacetime in two coordinate systems."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), layout='constrained')

    for ax, transformed in zip(axes, [False, True]):
        # Choose the identity map or the Penrose compactification.
        project = compact if transformed else lambda x, t: (x, t)

        if transformed:
            diamond(ax)
            grid(ax)
            ax.text(0,  1.035, 'Infinite future', ha='center', va='bottom', fontsize=10)
            ax.text(0, -1.035, 'Infinite past',   ha='center', va='top',    fontsize=10)
            # Sinh spacing gives a dense sample near the diamond boundary.
            s = np.sinh(np.linspace(-14, 14, 4001))
        else:
            ordinary(ax, 4)
            ax.set_xticks(np.arange(-4, 5, 1))
            ax.set_yticks(np.arange(-4, 5, 1))
            ax.tick_params(length=0, labelbottom=False, labelleft=False)
            ax.grid(color=INK, alpha=.13, lw=.8)
            s = np.linspace(-4, 4, 1001)

        # Worldlines: Alice at x = 0, Bob at x = beta * t.
        ax.plot(*project(np.zeros_like(s), s), color=ALICE, lw=2.7, zorder=6)
        ax.plot(*project(BETA * s, s),         color=BOB,   lw=2.7, ls=(0, (5, 2)), zorder=6)

        # One physical light signal -- identical endpoints in both coordinate systems.
        ts = np.linspace(1, t_receive, 200)
        xx, yy = project(ts - 1, ts)
        ax.plot(xx, yy, color=SIGNAL, lw=3, zorder=8)
        ax.annotate('', xy=(xx[150], yy[150]), xytext=(xx[50], yy[50]),
                    arrowprops=dict(arrowstyle='->', color=SIGNAL, lw=2), zorder=9)

        # Scatter the two key events: emission (Alice) and reception (Bob).
        for x, t, col in [(0, 1, ALICE), (x_receive, t_receive, BOB)]:
            ax.scatter(*project(x, t), s=32, color=col,
                       edgecolor='white', linewidth=.7, zorder=10)

        # Observer labels below the crossing, with leader lines to the events.
        label_data = [
            (0,           -1.5, 'Alice', ALICE, ( .29, -.53) if transformed else ( 1.7, -1.5)),
            (-1.5 * BETA, -1.5, 'Bob',   BOB,   (-.32, -.53) if transformed else (-2.0, -1.5)),
        ]
        for x, t, label, col, loc in label_data:
            ax.annotate(
                label, xy=project(x, t), xytext=loc,
                color=col, weight='bold', ha='center',
                arrowprops=dict(arrowstyle='-', color=col, lw=1), zorder=11,
            )

        signal_text_loc = (.40, .36) if transformed else (2.5, 2.6)
        ax.annotate(
            'Light signal',
            xy=project(x_receive, t_receive), xytext=signal_text_loc,
            ha='center', color=INK, fontsize=10,
            arrowprops=dict(arrowstyle='-', color=SIGNAL, lw=1), zorder=11,
        )
        ax.set_title(
            '(b) Minkowski spacetime\nPenrose diagram'
            if transformed else
            '(a) Minkowski spacetime\nOrdinary coordinates',
            pad=18,
        )

    # Validation: null slope and consistent event positions.
    # ts retains the value from the last loop iteration (transformed = True).
    X, T = compact(ts - 1, ts)
    assert np.allclose(T - X, (T - X)[0])
    assert np.isclose(x_receive, BETA * t_receive)
    assert np.isclose(t_receive - 1, x_receive)

    fig.savefig(OUT / 'figure_03.png', dpi=220, bbox_inches='tight', pad_inches=.18)


if __name__ == '__main__':
    main()
