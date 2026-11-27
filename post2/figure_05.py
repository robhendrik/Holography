"""Growing causal past on a Penrose diagram at three moments (Figure 5).

Shows how the region that can causally influence Alice (at x = 0) expands
as her proper time advances.  The three panels correspond to progressively
later moments on her worldline.

Author: Rob Hendriks
"""
from spacetime import *

# Output directory is the same folder as this script.
OUT = Path(__file__).parent


def main():
    """Draw and save Figure 5: expanding causal past at three times."""
    fig, axs = plt.subplots(1, 3, figsize=(10, 4), layout='constrained')

    # Three representative moments along Alice's worldline (Penrose time coordinate T).
    moments = [
        (-.4,  'Earlier'),
        ( .35, 'Later'),
        ( .88, 'Much later'),
    ]

    for ax, (T, title) in zip(axs, moments):
        diamond(ax)                                        # draw the Penrose diamond
        past_diamond(ax, T)                                # shade causal past up to time T
        worldline(ax)                                      # Alice's worldline at x = 0
        ax.scatter(0, T, color=INK, s=28, zorder=6)       # mark Alice's current event
        ax.set_title(title)
        ax.text(0, -1.07, 'Infinite past',   ha='center', fontsize=9)
        ax.text(0,  1.07, 'Infinite future', ha='center', fontsize=9)

    fig.text(
        .5, .015,
        'Blue: events that can influence Alice by the marked moment',
        ha='center', fontsize=12, color=INK,
    )

    fig.savefig(OUT / 'figure_05.png', dpi=220, bbox_inches='tight', pad_inches=.18)


if __name__ == '__main__':
    main()
