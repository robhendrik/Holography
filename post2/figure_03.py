"""Same inertial observers and light signal in ordinary and compactified spacetime."""
from spacetime import *

BETA = 0.28  # Bob's velocity in units of c
BOB = '#a34f32'
ALICE = '#245778'
SIGNAL = '#ba8b20'
# Alice emits at t=1; Bob receives when t-1 = beta*t.
t_receive = 1/(1-BETA)
x_receive = BETA*t_receive
OUT=Path(__file__).parent

def render():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), layout='constrained')
    for ax, transformed in zip(axes, [False, True]):
        project = compact if transformed else lambda x,t: (x,t)
        if transformed:
            diamond(ax); grid(ax)
            ax.text(0,1.035,'Infinite future',ha='center',va='bottom',fontsize=10)
            ax.text(0,-1.035,'Infinite past',ha='center',va='top',fontsize=10)
            s = np.sinh(np.linspace(-14,14,4001))
        else:
            ordinary(ax,4)
            ax.set_xticks(np.arange(-4,5,1)); ax.set_yticks(np.arange(-4,5,1))
            ax.tick_params(length=0,labelbottom=False,labelleft=False)
            ax.grid(color=INK,alpha=.13,lw=.8)
            s=np.linspace(-4,4,1001)
        ax.plot(*project(np.zeros_like(s),s),color=ALICE,lw=2.7,zorder=6)
        ax.plot(*project(BETA*s,s),color=BOB,lw=2.7,ls=(0,(5,2)),zorder=6)
        # One physical light signal, identical endpoints in both coordinate systems.
        ts=np.linspace(1,t_receive,200)
        xx,yy=project(ts-1,ts)
        ax.plot(xx,yy,color=SIGNAL,lw=3,zorder=8)
        ax.annotate('',xy=(xx[150],yy[150]),xytext=(xx[50],yy[50]),arrowprops=dict(arrowstyle='->',color=SIGNAL,lw=2),zorder=9)
        for x,t,col in [(0,1,ALICE),(x_receive,t_receive,BOB)]:
            ax.scatter(*project(x,t),s=32,color=col,edgecolor='white',linewidth=.7,zorder=10)
        # Labels below the crossing, with leader lines to the same physical events.
        for x,t,label,col,loc in [(0,-1.5,'Alice',ALICE,(.29,-.53) if transformed else (1.7,-1.5)),(-1.5*BETA,-1.5,'Bob',BOB,(-.32,-.53) if transformed else (-2.0,-1.5))]:
            ax.annotate(label,xy=project(x,t),xytext=loc,color=col,weight='bold',ha='center',arrowprops=dict(arrowstyle='-',color=col,lw=1),zorder=11)
        ax.annotate('Light signal',xy=project(x_receive,t_receive),xytext=(.40,.36) if transformed else (2.5,2.6),ha='center',color=INK,fontsize=10,arrowprops=dict(arrowstyle='-',color=SIGNAL,lw=1),zorder=11)
        ax.set_title('(b) Minkowski spacetime\nPenrose diagram' if transformed else '(a) Minkowski spacetime\nOrdinary coordinates',pad=18)
    # Explicit validation: both light-signal endpoints and null slope.
    X,T=compact(ts-1,ts)
    assert np.allclose(T-X,(T-X)[0])
    assert np.isclose(x_receive,BETA*t_receive)
    assert np.isclose(t_receive-1,x_receive)
    fig.savefig(OUT/f'figure_03.png',dpi=220,bbox_inches='tight',pad_inches=.18)

if __name__=='__main__':
    render()
