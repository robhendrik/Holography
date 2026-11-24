"""Shared plotting and exact null-coordinate compactification (c=1)."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
OUT = Path(__file__).resolve().parent / 'output'
PAST='#459bc9'; FUTURE='#e6ad51'; INK='#263441'; GRAY='#e9edf0'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.labelsize':13,'axes.titlesize':14,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white','figure.facecolor':'white'})

def compact(x,t):
    """Return X,T, in units of pi/2. Light rays retain slopes ±1."""
    U=np.arctan(t-x); V=np.arctan(t+x)
    return (V-U)/np.pi, (V+U)/np.pi

def polygon(ax, vertices, color, alpha=1, **kw):
    ax.add_patch(Polygon(vertices,closed=True,facecolor=color,alpha=alpha,edgecolor='none',**kw))

def diamond(ax):
    polygon(ax,[(0,-1),(1,0),(0,1),(-1,0)],GRAY,zorder=0)
    ax.plot([0,1,0,-1,0],[-1,0,1,0,-1],color=INK,lw=1.6,zorder=5)
    ax.set(xlim=(-1.13,1.13),ylim=(-1.13,1.13),aspect='equal'); ax.axis('off')

def grid(ax):
    s=np.sinh(np.linspace(-12,12,1601))
    for k in [-10,-3,-1,0,1,3,10]:
        ax.plot(*compact(np.full_like(s,k),s),color=INK,alpha=.19,lw=.8,zorder=2)
        ax.plot(*compact(s,np.full_like(s,k)),color=INK,alpha=.19,lw=.8,zorder=2)

def past_diamond(ax,T,color=PAST,alpha=.30):
    a=(1+T)/2
    polygon(ax,[(0,-1),(a,(T-1)/2),(0,T),(-a,(T-1)/2)],color,alpha,zorder=1)
    ax.plot([-a,0,a],[(T-1)/2,T,(T-1)/2],color=color,lw=1.7,zorder=3)

def worldline(ax):
    ax.plot([0,0],[-1,1],color=INK,lw=1.5,zorder=4)

def save(fig,name):
    OUT.mkdir(exist_ok=True)
    for ext in ['png','svg']:
        fig.savefig(OUT/f'{name}.{ext}',dpi=220,bbox_inches='tight',pad_inches=.15)
    plt.close(fig)

def ordinary(ax,lim=4):
    ax.set(xlim=(-lim,lim),ylim=(-lim,lim),aspect='equal',xlabel='Position, x',ylabel='Time, ct')
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines[['left','bottom']].set_color(INK)
