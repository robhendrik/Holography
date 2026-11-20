"""Figure 4 — Instantaneous total and time-averaged EM energy density.

Run with: python Figure4_script.py
Output is saved alongside this script: post1_figure4.png
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
ORANGE='#d8802a'; GREY='#596778'


def optical_coordinate(x,epsilon):
    if epsilon == 0:
        return np.asarray(x)
    return -np.log1p(-epsilon*np.asarray(x))/epsilon


def make_figure(output_path=None,epsilon=.45,mode=3):
    if not 0 <= epsilon < 1:
        raise ValueError('epsilon must satisfy 0 <= epsilon < 1')
    if output_path is None:
        output_path = OUT / 'post1_figure4.png'
    depth=np.linspace(0,1,680)
    theta=np.linspace(0,2*np.pi,621,endpoint=False)
    N=1-epsilon*depth
    Xi=optical_coordinate(depth,epsilon)
    phase=mode*np.pi*Xi/Xi[-1]
    # Instantaneous total electromagnetic energy, electric + magnetic.
    # Normalize by time-averaged energy density at the top mirror.
    U=2/N[:,None]**2 * (
        np.sin(phase[:,None])**2 * np.sin(theta[None,:])**2
        + np.cos(phase[:,None])**2 * np.cos(theta[None,:])**2
    )
    exact=1/N**2
    mean=np.mean(U,axis=1)
    assert np.max(np.abs(mean-exact)) < 1.e-12, 'Cycle average inconsistent'

    fig=plt.figure(figsize=(11.0,6.0),facecolor='white',dpi=170)
    gs=fig.add_gridspec(1,2,width_ratios=[2.2,1],left=.09,right=.95,
                        top=.88,bottom=.17,wspace=.22)
    left=fig.add_subplot(gs[0,0])
    right=fig.add_subplot(gs[0,1],sharey=left)
    left.imshow(U,extent=(0,1,1,0),aspect='auto',cmap='inferno',
                vmin=0,vmax=7,interpolation='nearest')
    left.set_xlabel(r'one oscillation,  $\omega\tau/(2\pi)$',fontsize=11.5)
    left.set_ylabel(r'depth down cavity,  $x/h$',fontsize=11.5)
    left.set_title('Instantaneous total EM energy density',fontsize=12.5,pad=12)
    left.set_xticks([0,.25,.5,.75,1])
    left.set_yticks([0,.25,.5,.75,1])
    right.fill_betweenx(depth,1,exact,color=ORANGE,alpha=.21)
    right.plot(exact,depth,color=ORANGE,lw=2.8)
    right.axvline(1,color=GREY,lw=1.1,ls='--')
    right.set_xlabel('average energy / top value',fontsize=11.5)
    right.set_title('Average EM energy density',fontsize=12.5,pad=12)
    right.set_xlim(.7,3.75)
    right.set_xticks([1,2,3])
    right.tick_params(axis='y',labelleft=False,left=False)
    right.spines[['top','right']].set_visible(False)
    for ax in (left,right):
        ax.text(.02,.985,'TOP',transform=ax.transAxes,ha='left',va='top',
                fontsize=10.5,color='white' if ax is left else GREY,
                bbox={'fc':'#3d3440' if ax is left else 'white','ec':'none','alpha':.80})
        ax.text(.02,.015,'BOTTOM',transform=ax.transAxes,ha='left',va='bottom',
                fontsize=10.5,color='white' if ax is left else GREY,
                bbox={'fc':'#3d3440' if ax is left else 'white','ec':'none','alpha':.80})
    fig.text(.5,.06,rf'Stationary 3rd standing mode  ·  $\overline{{u}}(x)/\overline{{u}}(0)=N(x)^{{-2}}$  ·  $ah/c^2={epsilon:.2f}$ (exaggerated)',
             ha='center',fontsize=10.5,color=GREY)
    fig.savefig(output_path,dpi=220,bbox_inches='tight',facecolor='white')
    plt.close(fig)
    return Path(output_path)


if __name__ == '__main__':
    make_figure()
