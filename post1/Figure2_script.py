"""Figure 2 — Three force factors for a photon in a Rindler-rigid cavity.

Run with: python Figure2_script.py
Output is saved alongside this script: post1_figure2.png
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
BLUE='#317fb2'; ORANGE='#e6964a'; GREEN='#258f81'; GREY='#606b76'


def make_figure(output_path=None, epsilon=.18):
    if not 0 < epsilon < 1:
        raise ValueError('epsilon must satisfy 0 < epsilon < 1')
    if output_path is None:
        output_path = OUT / 'post1_figure2.png'
    n = 1-epsilon
    factors = [1/n, 1/n, n]
    titles = ['1. Momentum per bounce', '2. Bounces per local second',
              '3. Referred to top support']
    notation = [r'$p_b/p_t$', r'$r_b/r_t$', r'$F_{b\to t}/F_b$']
    colors = [ORANGE, BLUE, GREEN]
    fig, axs = plt.subplots(1,3,figsize=(12.3,4.0), dpi=170)
    fig.patch.set_facecolor('white')
    fig.subplots_adjust(left=.045, right=.98, bottom=.25, top=.84, wspace=.11)
    for ax, val, heading, tag, col in zip(axs, factors, titles, notation, colors):
        ax.bar([0,1], [1,val], width=.53, color=[GREY,col])
        ax.set_xticks([0,1], ['reference','factor'])
        ax.set_ylim(0,1.56)
        ax.axhline(1,color='#d5d9dc',lw=.9)
        ax.text(.50, 1.47, tag, ha='center', va='center', fontsize=16, color=col)
        ax.text(1, val+.045, f'{val:.3f}×', ha='center', va='bottom', fontsize=11.5)
        ax.set_title(heading, pad=12, fontsize=12.5)
        ax.spines[['top','right','left']].set_visible(False)
        ax.tick_params(axis='y',left=False,labelleft=False)
        ax.tick_params(axis='x',labelsize=10.5)
    # Keep only the net result as a light annotation. Example ε is in caption.
    fig.text(.5, .09,
             rf'Net bottom/top factor at one support: $1/(1-\varepsilon)={1/n:.3f}\times$',
             ha='center', fontsize=12, color=GREY)
    fig.savefig(output_path, dpi=220, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return Path(output_path)


if __name__ == '__main__':
    make_figure()
