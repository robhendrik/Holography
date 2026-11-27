"""Animated morph from ordinary Minkowski coordinates to a Penrose diagram (Figure 4 GIF).

Interpolates the same scene -- Alice, Bob, and a light signal -- continuously
from ordinary (x, t) coordinates to the exact Penrose compactification.  Both
null directions are compactified simultaneously using the same strictly
increasing function, so null rays always travel at 45 degrees.

Dependencies: numpy, matplotlib, pillow.

Author: Rob Hendriks
"""
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

OUT = Path(__file__).resolve().parent

# Colour constants.
INK    = '#263441'  # dark slate for axes, text, borders
ALICE  = '#245778'  # blue for Alice's worldline
BOB    = '#a34f32'  # rust for Bob's worldline
SIGNAL = '#ba8b20'  # gold for the light signal

# Observer parameters.
BETA    = .28                    # Bob's velocity relative to Alice, in units of c
receive = 1 / (1 - BETA)        # time at which Bob receives Alice's light signal

plt.rcParams.update({
    'font.family':      'DejaVu Sans',
    'font.size':        12,
    'figure.facecolor': 'white',
})


def transform(x, t, a):
    """Interpolate between ordinary coordinates and the Penrose compactification.

    Both null coordinates use the same strictly increasing function so that
    null rays retain slopes +/-1 at every stage of the morph.

    Parameters
    ----------
    x, t : array-like
        Spatial position and time in units where c = 1.
    a : float
        Morph parameter: 0 gives scaled ordinary coordinates; 1 gives the
        exact Penrose compactification.

    Returns
    -------
    X, T : ndarray
        Interpolated display coordinates.
    """
    scale = (1 - a) / 4 + a * 2 / np.pi

    def f(q):
        return scale * q if a == 0 else scale * np.arctan(a * q) / a

    u = f(np.asarray(t) - np.asarray(x))
    v = f(np.asarray(t) + np.asarray(x))
    return (v - u) / 2, (v + u) / 2


# Pre-compute arrays used by every frame.
s  = np.sinh(np.linspace(-14, 14, 3501))   # sparse range for coordinate grid curves
ts = np.linspace(1, receive, 200)           # light signal time samples

# Create figure and axes (global so draw() can reference them directly).
fig, ax = plt.subplots(figsize=(6.3, 6.5), dpi=130)
fig.subplots_adjust(left=.105, right=.945, bottom=.12, top=.86)


def draw(a):
    """Render one animation frame at morph parameter a and return a PIL Image."""
    ax.clear()
    ax.set(xlim=(-1.12, 1.12), ylim=(-1.12, 1.12), aspect='equal')
    ax.axis('off')

    # At a > 0 the diamond boundary is visible; draw it once it fits in the viewport.
    if a > 0:
        d = ((1 - a) / 4 + a * 2 / np.pi) * np.pi / (2 * a)
        if d < 1.2:
            ax.fill([0, d, 0, -d], [d, 0, -d, 0], color='#e9edf0', zorder=0)
            ax.plot([0, d, 0, -d, 0], [d, 0, -d, 0, d], color=INK, lw=1.4, zorder=5)

    # Coordinate grid lines.
    for k in [-10, -4, -3, -2, -1, 0, 1, 2, 3, 4, 10]:
        ax.plot(*transform(np.full_like(s, k), s, a), color=INK, alpha=.19, lw=.8)
        ax.plot(*transform(s, np.full_like(s, k), a), color=INK, alpha=.19, lw=.8)

    # Worldlines.
    ax.plot(*transform(np.zeros_like(s), s,       a), color=ALICE, lw=2.7, zorder=6)
    ax.plot(*transform(BETA * s,         s,       a), color=BOB,   lw=2.7, ls=(0, (5, 2)), zorder=6)

    # Light signal with direction arrow.
    x_sig, y_sig = transform(ts - 1, ts, a)
    ax.plot(x_sig, y_sig, color=SIGNAL, lw=3, zorder=8)
    ax.annotate('', xy=(x_sig[155], y_sig[155]), xytext=(x_sig[45], y_sig[45]),
                arrowprops=dict(arrowstyle='->', color=SIGNAL, lw=2), zorder=9)

    # Event markers.
    for xx, tt, col in [(0, 1, ALICE), (BETA * receive, receive, BOB)]:
        ax.scatter(*transform(xx, tt, a), s=35, color=col,
                   edgecolor='white', linewidth=.7, zorder=10)

    # Observer labels with leader lines.
    label_data = [
        (0,           -1.5, 'Alice', ALICE, (38,   0), 'left'),
        (-1.5 * BETA, -1.5, 'Bob',   BOB,   (-38,  0), 'right'),
    ]
    for xx, tt, name, col, offset, ha in label_data:
        ax.annotate(
            name, xy=transform(xx, tt, a), xytext=offset,
            textcoords='offset points', ha=ha, va='center',
            color=col, weight='bold',
            arrowprops=dict(arrowstyle='-', color=col, lw=1), zorder=11,
        )

    ax.annotate(
        'Light signal',
        xy=transform(BETA * receive, receive, a), xytext=(34, 18),
        textcoords='offset points', ha='left', color=INK, fontsize=10,
        arrowprops=dict(arrowstyle='-', color=SIGNAL, lw=1), zorder=11,
    )

    # Axis labels at the initial frame; boundary labels at the final frame.
    if a == 0:
        ax.text(0,     -1.09, 'Position, x', ha='center', color=INK)
        ax.text(-1.09,  0,    'Time, ct',    ha='center', rotation=90, color=INK)
    if a == 1:
        ax.text(0,  1.035, 'Infinite future', ha='center', va='bottom', fontsize=10, color=INK)
        ax.text(0, -1.035, 'Infinite past',   ha='center', va='top',    fontsize=10, color=INK)

    if a == 0:
        title = 'Ordinary coordinates'
    elif a == 1:
        title = 'Penrose diagram'
    else:
        title = 'Changing the coordinates'
    ax.set_title(title, fontsize=14, pad=13, color=INK)

    fig.canvas.draw()
    return Image.fromarray(np.asarray(fig.canvas.buffer_rgba())[:, :, :3].copy())


if __name__ == '__main__':
    fig.suptitle('The same Minkowski spacetime',
                 fontsize=19, y=.965, color=INK, weight='bold')
    fig.text(.5, .055, 'Same observers. Same light signal.',
             ha='center', fontsize=13, color=INK)
    fig.text(.5, .025, 'Light always travels at 45 degrees.',
             ha='center', fontsize=11, color=INK)

    # Validate every interpolation step: null directions, monotonicity, endpoints.
    q = np.linspace(-20, 20, 401)
    for a in np.linspace(0, 1, 101):
        X, T = transform(q,  q + 1, a);  assert np.allclose(T - X, (T - X)[0])
        X, T = transform(-q, q + 1, a);  assert np.allclose(T + X, (T + X)[0])
        X, T = transform(0,  q,     a);  assert np.all(np.diff(T) > 0)
        X, T = transform(ts - 1, ts, a); assert np.allclose(T - X, (T - X)[0])
    assert np.isclose(receive - 1, BETA * receive)
    X, T = transform(q, q / 2, 1)
    assert np.allclose(X, (np.arctan(q * 1.5) - np.arctan(-q * .5)) / np.pi)

    # Build frames with ease-in and ease-out.
    steps  = (1 - np.cos(np.linspace(0, np.pi, 65))) / 2
    frames = [draw(float(a)) for a in steps]

    # Save representative stills.
    frames[0].save(OUT / 'ordinary.png')
    frames[-1].save(OUT / 'penrose.png')
    frames[len(frames) // 2].save(OUT / 'intermediate.png')

    # Build a looping sequence: forward then backward, with longer holds at each end.
    sequence  = frames + frames[-2:0:-1]
    durations = [65] * len(sequence)
    durations[0]            = 1800   # hold at ordinary-coordinates frame
    durations[len(frames) - 1] = 2200   # hold at Penrose-diagram frame

    sequence[0].save(
        OUT / 'figure_04_penrose_morph.gif',
        save_all=True, append_images=sequence[1:],
        duration=durations, loop=0, disposal=2, optimize=True,
    )
    print('Validated 101 interpolation steps; GIF saved.', len(sequence), 'frames')
