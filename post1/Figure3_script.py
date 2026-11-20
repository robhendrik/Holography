"""Figure 3 — A standing-wave potential is skewed in physical distance.

Run with: python Figure3_script.py
Output is saved alongside this script: post1_figure3.png
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
BLUE='#2779ae'; ORANGE='#d8802a'; GREY='#596778'


def optical_coordinate(x,epsilon):
    if epsilon == 0:
        return np.asarray(x)
    return -np.log1p(-epsilon*np.asarray(x))/epsilon


def make_figure(output_path=None,epsilon=.55, mode=4):
    if not 0 <= epsilon < 1:
        raise ValueError('epsilon must satisfy 0 <= epsilon < 1')
    if output_path is None:
        output_path = OUT / 'post1_figure3.png'
    x=np.linspace(0,1,1601)
    fig,axs=plt.subplots(1,2,figsize=(11.6,5.3),sharex=True,sharey=True,dpi=180)
    fig.patch.set_facecolor('white')
    for ax,eps,col,heading in zip(
        axs,[0,epsilon],[BLUE,ORANGE],
        ['At rest: equally spaced nodes','Accelerating: nodes crowd below']
    ):
        Xi=optical_coordinate(x,eps)
        L=float(optical_coordinate(1.,eps))
        phase=mode*np.pi*Xi/L
        ax.plot(x,np.sin(phase),color=col,lw=2.8)
        nodes=np.linspace(0,1,mode+1) if eps == 0 else \
            -np.expm1(-eps*L*np.arange(mode+1)/mode)/eps
        # Analytical nodes (inverse optical map)
        assert np.all(np.diff(nodes)>0)
        for xp in nodes:
            ax.axvline(xp,ls=':',lw=.95,color=col,alpha=.55)
            ax.plot(xp,0,'o',ms=4,color=col)
        ax.axhline(0,lw=.9,color=GREY)
        ax.set_xlim(0,1)
        ax.set_ylim(-1.32,1.32)
        ax.set_xticks([0,.25,.50,.75,1])
        ax.set_xlabel(r'physical position down cavity,  $x/h$',fontsize=11.5)
        ax.set_title(heading,fontsize=12.5,color=col,pad=12)
        ax.text(.005,-1.23,'TOP',ha='left',fontsize=9.5,color=GREY)
        ax.text(.995,-1.23,'BOTTOM',ha='right',fontsize=9.5,color=GREY)
        ax.grid(axis='x',alpha=.10)
        ax.spines[['top','right']].set_visible(False)
        if eps:
            ax.annotate('',xy=(nodes[0],1.12),xytext=(nodes[1],1.12),
                        arrowprops={'arrowstyle':'<->','color':GREY,'lw':1.1})
            ax.text((nodes[0]+nodes[1])/2,1.16,'wide',ha='center',fontsize=10,color=GREY)
            ax.annotate('',xy=(nodes[-2],1.12),xytext=(nodes[-1],1.12),
                        arrowprops={'arrowstyle':'<->','color':GREY,'lw':1.1})
            ax.text((nodes[-2]+nodes[-1])/2,1.16,'narrow',ha='center',fontsize=10,color=GREY)
    axs[0].set_ylabel(r'vector potential  $A_y/A_0$',fontsize=11.5)
    fig.subplots_adjust(left=.09,right=.98,top=.89,bottom=.18,wspace=.09)
    fig.text(.50,.055,rf'4th standing mode  ·  accelerated case:  $ah/c^2={epsilon:.2f}$ (exaggerated)',
             ha='center',fontsize=10.5,color=GREY)
    fig.savefig(output_path,dpi=220,bbox_inches='tight',facecolor='white')
    plt.close(fig)
    return Path(output_path)


if __name__ == '__main__':
    make_figure()
