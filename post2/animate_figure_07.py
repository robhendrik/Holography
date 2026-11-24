"""Morph the matched dust-collapse chart in figure_07.py.
Finite events use a common interpolation; infinity is shown only at the endpoint.
Run with figure_07.py in the same directory. Requires numpy scipy matplotlib pillow.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Polygon
from scipy.optimize import brentq
from figure_07 import R, ts, F, G, LV, LU, P, Q, xy, H, INK, STAR, RUST, GOLD, BLUE
OUT=Path(__file__).resolve().parent

# All curves are paired at the same physical events. The finite PG window
# expands as the morph proceeds; the exact limiting boundary appears last.
def p_label(t,r):
    if t<0 and r<=R(t)+1e-10:
        e=-2*np.sqrt(R(t)); return e-r/R(t)
    if abs(r-1)<1e-13: return -3.
    y=np.sqrt(r); z=np.log(abs(1-y))+(r+2*y-t)/2
    if r<1:
        if z>=-1e-13: return -1.
        if z< -30: return -3.
        return brentq(lambda e: LU(e)-z,-2+1e-14,0)-1
    lo=-4.
    while LU(lo)<z: lo*=2
    return brentq(lambda e: LU(e)-z,lo,-2-1e-14)-1

def paired(t,r,p,q):
    t,r,p,q=np.broadcast_arrays(t,r,p,q)
    x,y=xy(p,q)
    return np.column_stack((r,t,x,y))

def surface(e): return paired(ts(e),e**2/4,e-1,P(e+1))
def center(e): return paired(ts(e),0,e,P(e))
def dust_sing(chi): return paired(0,0,-chi,P(chi))
def vacuum_sing(e): return paired(-2*LU(e),0,e-1,-P(e-1))
def horizon_inside(e): return paired(ts(e),e**2/4*(e+3),-3,P(2*e+3))
def horizon_out(t): return paired(t,1,-3,Q((t+G(1))/2))

def outgoing(re,tmax,rmax):
    te=-2/3*re**1.5; p=-2*np.sqrt(re)-1
    if re==1: t=np.linspace(te,tmax,450); r=np.ones_like(t)
    elif re>1:
        end=rmax
        if te+F(end)-F(re)>tmax: end=brentq(lambda r:te+F(r)-F(re)-tmax,re,rmax)
        r=np.linspace(re,end,450); t=te+F(r)-F(re)
    else:
        r=np.linspace(re,0,450); t=te+F(r)-F(re)
    q=Q((t+G(r))/2)
    data=paired(t,r,p,q)
    assert np.max(abs(np.diff(data[:,3])-np.diff(data[:,2])))<1e-12
    return data

# Cache stages; common isotropic scale for the PG panel preserves its angles.
N=35
stages=[]
for s in np.linspace(0,1,N):
    # The visible finite region grows only near the end, avoiding a false
    # identification of a finite viewport edge with infinity.
    grow=1+5*s**10
    tmax=5*grow; rmax=4.6*grow; emin=-np.cbrt(60*grow)
    es=np.linspace(emin,0,550)
    surf=surface(es); ctr=center(es)
    chi=np.linspace(0,1,150)
    sing1=dust_sing(chi)
    # singularity in vacuum, ending at the same time limit as the PG view
    eend=brentq(lambda e: -2*LU(e)-tmax,-2+1e-14,0) if tmax<55 else -2+1e-13
    sing2=vacuum_sing(np.linspace(0,eend,350))
    hi=horizon_inside(np.linspace(-3,-2,250)); ho=horizon_out(np.linspace(-2/3,tmax,450))
    rays=[outgoing(re,tmax,rmax) for re in (1.6,1.,.72)]
    # Dust fill uses actual matched center, surface, and singular boundary.
    dust=np.vstack((ctr,sing1,surf[::-1]))
    stages.append((surf,ctr,sing1,sing2,hi,ho,rays,dust,grow))

fig,ax=plt.subplots(figsize=(7.0,7.0),dpi=85)
fig.subplots_adjust(left=.13,right=.94,bottom=.15,top=.88)

def display(data,s,grow):
    # isotropic PG display, smoothly zooming out as the visible domain expands
    scale=.095/(1+.7*(grow-1))
    a=np.column_stack((data[:,0]*scale,data[:,1]*scale-.48))
    return (1-s)*a+s*data[:,2:]

def draw(index):
    ax.clear(); ax.set(xlim=(-.16,1.04),ylim=(-1.08,.19),aspect='equal'); ax.axis('off')
    s=index/(N-1); surf,ctr,sg1,sg2,hi,ho,rays,dust,grow=stages[index]
    final=index==N-1
    if final:
        ax.add_patch(Polygon([(0,-1),((H+1)/2,(H-1)/2),(H,0),(0,0)],facecolor=BLUE,edgecolor='none'))
        # exact compact boundary; the finite-window boundary never morphs into it
        ax.plot([0,(H+1)/2,H],[-1,(H-1)/2,0],color=INK,lw=1.4)
        es=-np.geomspace(1e5,1e-9,1800); surf=surface(es); ctr=center(es)
        dust=np.vstack(([[0,0,0,-1]],ctr,sg1,surf[::-1],[[0,0,0,-1]]))
    def d(a): return display(a,s,grow)
    def line(a,**kw):
        z=d(a); ax.plot(z[:,0],z[:,1],**kw)
    ax.add_patch(Polygon(d(dust),facecolor=STAR,edgecolor='none',alpha=.85))
    line(ctr,color=INK,lw=1.5); line(surf,color=RUST,lw=2,ls='--')
    line(hi,color=INK,lw=2); line(ho,color=INK,lw=2)
    line(sg1,color=INK,lw=2,ls=':'); line(sg2,color=INK,lw=2,ls=':')
    if final:
        ax.plot([0,H],[-H,0],color=INK,lw=2)
        xx=np.linspace(0,H,700); ax.plot(xx,.006*np.sin(2*np.pi*xx/H*23),color=INK,lw=1.5)
    for j,(re,a) in enumerate(zip((1.6,1.,.72),rays)):
        z=d(a)
        if final and re>=1:
            p=-2*np.sqrt(re)-1; x,y=xy(p,H); z=np.vstack((z,[x,y]))
        ax.plot(*z.T,color=GOLD,lw=2,ls=['-','--','-.'][j],zorder=5)
        ax.scatter(*z[0],s=23,color=GOLD,zorder=6)
        ax.annotate(str(j+1),z[0],xytext=[(9,-12),(9,-3),(-15,7)][j],textcoords='offset points',weight='bold',color=INK)
        k=len(z)*2//3; ax.annotate('',xy=z[k],xytext=z[k-25],arrowprops=dict(arrowstyle='-|>',color=GOLD,lw=1.2))
    # Labels follow real reference points rather than independently drawn geometry.
    z=d(surface(np.array([-3.7])))[0]; ax.annotate('Star',z,xytext=(-25,0),textcoords='offset points',ha='right',color=INK)
    z=d(horizon_out(np.array([2.5])))[0]; ax.annotate('Horizon',z,xytext=(10,8),textcoords='offset points',color=INK)
    if final: ax.text(H/2,.035,'Singularity',ha='center',color=INK)
    else:
        z=d(vacuum_sing(np.array([-1.6])))[0]; ax.annotate('Singularity',z,xytext=(-10,8),textcoords='offset points',ha='right',color=INK)
    ax.set_title('Radius and time' if index==0 else 'Penrose diagram' if final else 'Changing coordinates',fontsize=17,pad=10,color=INK)
    if index==0:
        ax.annotate('Radius, r',xy=(.45,-1.02),ha='center',color=INK)
        ax.annotate('Time, ct',xy=(-.13,-.45),rotation=90,ha='center',color=INK)
    ax.text(.5,-.045,'1  Escapes     •     2  Horizon     •     3  Trapped',transform=ax.transAxes,ha='center',fontsize=11,color=INK)
    ax.text(.5,-.085,'Same collapse — different representation',transform=ax.transAxes,ha='center',fontsize=10,color=INK)

if __name__=='__main__':
    order=[0]*12+list(range(N))+[N-1]*22+list(range(N-2,0,-1))
    ani=FuncAnimation(fig,draw,frames=order,interval=90,blit=False)
    ani.save(OUT/'figure_07_morph.gif',writer=PillowWriter(fps=12))
    draw(N-1); fig.savefig(OUT/'figure_07_morph_final.png',dpi=150)
    print('Saved GIF and final frame; sampled outgoing null slopes checked.')
