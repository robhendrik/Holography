"""Figure 1 — Rindler-rigid accelerating cavity and inertial spacetime diagram.

Run with: python Figure1_script.py
Output is saved alongside this script: post1_figure1.png
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parent
BLUE = '#317fb2'
ORANGE = '#e6964a'
DARK = '#2d435d'
GREY = '#626e7b'


def make_figure(output_path=None, epsilon=0.27):
    if not 0 < epsilon < 1:
        raise ValueError('epsilon must satisfy 0 < epsilon < 1')
    if output_path is None:
        output_path = OUT / 'post1_figure1.png'

    fig, (ax0, ax1) = plt.subplots(
        1, 2, figsize=(13.4, 6.0), dpi=160,
        gridspec_kw={'width_ratios': [1.02, 1.35]}
    )
    fig.patch.set_facecolor('white')
    fig.subplots_adjust(left=.055, right=.985, bottom=.13, top=.82, wspace=.20)

    # Physical cavity schematic, not spacetime plot.
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, 1)
    ax0.axis('off')
    x0, y0, w, h = .42, .14, .38, .70
    ax0.add_patch(Rectangle((x0, y0), w, h,
                            facecolor='#e4edf4', edgecolor=BLUE, linewidth=1.5))
    for yy in (y0, y0 + h):
        ax0.add_patch(Rectangle((x0, yy-.011), w, .022,
                                facecolor=DARK, edgecolor=DARK))
    ax0.text(.03, .77, 'TOP', fontsize=13, va='bottom')
    ax0.text(.03, .70, r'$N_t=1,\quad a_t=a$', fontsize=12.5, va='bottom')
    ax0.text(.03, .49, r'$\varepsilon=ah/c^2$', fontsize=14.5, va='center')
    ax0.text(.03, .23, 'BOTTOM', fontsize=13, va='bottom')
    ax0.text(.03, .16, r'$N_b=1-\varepsilon$', fontsize=12.5, va='bottom')
    ax0.text(.03, .09, r'$a_b=a/(1-\varepsilon)$', fontsize=12.5, va='bottom')
    ax0.text(x0-.045, y0+h, r'$x=0$', ha='right', va='center', fontsize=12.5)
    ax0.text(x0-.045, y0, r'$x=h$', ha='right', va='center', fontsize=12.5)

    # Two directions of light propagation.
    for ya, yb in ((.24,.34), (.44,.54), (.64,.74)):
        ax0.annotate('', xy=(x0+w*.48, yb), xytext=(x0+w*.48, ya),
                     arrowprops={'arrowstyle':'-|>', 'color':ORANGE, 'lw':2.0,
                                 'mutation_scale':14})
    for ya, yb in ((.74,.64), (.54,.44), (.34,.24)):
        ax0.annotate('', xy=(x0+w*.61, yb), xytext=(x0+w*.61, ya),
                     arrowprops={'arrowstyle':'-|>', 'color':ORANGE, 'lw':2.0,
                                 'mutation_scale':14})
    ax0.annotate('', xy=(.96,.88), xytext=(.96,.62),
                 arrowprops={'arrowstyle':'-|>', 'color':BLUE, 'lw':2.5,
                             'mutation_scale':18})
    ax0.text(.80, .94, 'upward acceleration', color=BLUE, fontsize=12.5,
             ha='center', va='bottom')

    # Inertial (X,ct) coordinates, scaled by c^2/a.  The two worldlines are
    # X = rho cosh(eta), ct = rho sinh(eta), rho_top=1, rho_bottom=1-epsilon.
    eta = np.linspace(-1.15, 1.15, 600)
    rho_t, rho_b = 1.0, 1.0-epsilon
    Xt, Tt = rho_t*np.cosh(eta), rho_t*np.sinh(eta)
    Xb, Tb = rho_b*np.cosh(eta), rho_b*np.sinh(eta)
    ax1.plot(Xt, Tt, color=BLUE, lw=2.8, label='top mirror', zorder=3)
    ax1.plot(Xb, Tb, color=ORANGE, lw=2.8, label='bottom mirror', zorder=3)
    xh = np.linspace(0.48, 1.83, 350)
    ax1.plot(xh, +xh, ls=':', color=GREY, lw=1.6, label='Rindler horizons')
    ax1.plot(xh, -xh, ls=':', color=GREY, lw=1.6)
    ax1.set_xlim(.48, 1.82)
    ax1.set_ylim(-1.6, 1.6)
    ax1.set_xlabel(r'$X/(c^2/a)$ — inertial position', fontsize=12.5)
    ax1.set_ylabel(r'$ct/(c^2/a)$', fontsize=12.5)
    for name in ('top', 'right'):
        ax1.spines[name].set_visible(False)
    ax1.tick_params(labelsize=10.5)
    ax1.text(.01, 1.10, 'Spacetime diagram', transform=ax1.transAxes,
             fontsize=12.5, ha='left', va='bottom')
    # Legend is outside the plotting rectangle, so no curve or horizon
    # passes behind its text.
    ax1.legend(loc='lower left', bbox_to_anchor=(.01, 1.01), ncol=3,
               fontsize=10.5, frameon=False, handlelength=2.0,
               columnspacing=1.3, borderaxespad=0.)

    fig.savefig(output_path, dpi=220, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return Path(output_path)


if __name__ == '__main__':
    make_figure()
