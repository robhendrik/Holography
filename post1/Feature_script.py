"""Feature artwork: compressed standing-wave lobes in an accelerated cavity.

Run: python feature_standing_wave_modepattern.py
Output is saved next to this script as post1_feature_modepattern.png.

Color represents the *electric standing-wave amplitude squared* (a mode-pattern
visualization), NOT the full time-averaged electromagnetic energy density.
The latter would vary smoothly as N(x)^(-2), without nodes.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyArrow, Rectangle

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT = SCRIPT_DIR / 'post1_feature_modepattern.png'
EPSILON = 0.55     # ah/c^2; exaggerated to reveal the optical compression
MODE = 8           # longitudinal mode / number of antinodes


def optical_coordinate(depth: np.ndarray, epsilon: float) -> np.ndarray:
    """Dimensionless optical coordinate for 0 <= depth <= 1, measured downward."""
    return depth if epsilon == 0 else -np.log1p(-epsilon * depth) / epsilon


def make_figure(output_path: Path = OUTPUT, epsilon: float = EPSILON,
                mode: int = MODE) -> Path:
    if not (0 <= epsilon < 1):
        raise ValueError('Require 0 <= epsilon < 1 for this Rindler cavity.')
    if mode < 1 or int(mode) != mode:
        raise ValueError('mode must be a positive integer')

    fig, ax = plt.subplots(figsize=(12.0, 6.75), dpi=200)
    fig.patch.set_facecolor('#060814')
    ax.set_facecolor('#060814')
    ax.set_xlim(0, 1)
    ax.set_ylim(1, 0)  # downward physical coordinate
    ax.axis('off')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # The entire field lives between these two mirrors, with no extension beyond.
    left, right = 0.0, 1.0
    top, bottom = 0.09, 0.91

    # Rectangular 2D field image: transverse Gaussian illumination multiplied by
    # the calculated standing-wave electric-field amplitude squared.
    ny, nx = 1600, 800
    depth = np.linspace(0, 1, ny)
    xs = np.linspace(left, right, nx)
    xi = optical_coordinate(depth, epsilon)
    phase = mode * np.pi * xi / xi[-1]
    N = 1 - epsilon * depth

    # Time-averaged electric-field contribution: <E_y^2> ∝ sin²(k xi) / N².
    # It has dark nodes. Magnetic energy is not included in this visualization.
    axial_intensity = np.sin(phase)**2 / N**2
    transverse = np.exp(-0.5 * ((xs - (left + right) / 2) / 0.075)**2)
    intensity = axial_intensity[:, None] * transverse[None, :]
    intensity /= intensity.max()

    palette = LinearSegmentedColormap.from_list('mode_lobes', [
        (0.00, '#070b20'),
        (0.10, '#17143b'),
        (0.25, '#42206b'),
        (0.45, '#8f2e88'),
        (0.62, '#cf4b62'),
        (0.78, '#f58b39'),
        (0.92, '#ffcb48'),
        (1.00, '#fff2a0'),
    ])
    # imshow is confined to the cavity extent by construction.
    ax.imshow(intensity, cmap=palette, vmin=0, vmax=1,
              extent=(left, right, bottom, top), interpolation='bilinear',
              aspect='auto', zorder=1)

    # Very subtle physical enclosure; no traced sine wave or outer lobe contours.
    #ax.plot([left, left], [top, bottom], color='#8190b3', alpha=0.27, lw=1.2, zorder=3)
    #ax.plot([right, right], [top, bottom], color='#8190b3', alpha=0.27, lw=1.2, zorder=3)

    mirror_width = (right - left) + 0.03
    mirror_x = (left + right) / 2 - mirror_width / 2
    # for y in (top - 0.017, bottom):
    #     ax.add_patch(Rectangle((mirror_x, y), mirror_width, 0.019,
    #                            facecolor='#c1c8d9', edgecolor='#8590ad',
    #                            lw=1.2, zorder=5))
    #     ax.plot([mirror_x + 0.004, mirror_x + mirror_width - 0.004],
    #             [y + 0.002, y + 0.002], color='white', alpha=0.7,
    #             lw=0.9, zorder=6)

    # # Upward acceleration indicator, without labels or equations.
    # ax.add_patch(FancyArrow(0.78, 0.72, 0, -0.36, width=0.009,
    #                         head_width=0.038, head_length=0.055,
    #                         length_includes_head=True, facecolor='#efaa3b',
    #                         edgecolor='none', zorder=5))

    output_path = Path(output_path)
    fig.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(),
                bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    return output_path


if __name__ == '__main__':
    print(f'Saved: {make_figure()}')