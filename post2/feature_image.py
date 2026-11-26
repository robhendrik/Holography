"""Thumbnail based on the calculated Figure 7b. No title or annotations by default."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
OUT=Path(__file__).resolve().parent
SHOW_LABELS=False
INK='#263441'; STAR='#cab8a8'; RUST='#995b43'; GOLD='#a87526'; BLUE='#e8eff3'
def P(p): return 2/np.pi*np.arctan(np.asarray(p)/1.5)
def xy(p,q): return (q-P(p))/2,(q+P(p))/2
H=float(-P(-3))
fig=plt.figure(figsize=(12,6.75),facecolor='white')
ax=fig.add_axes([.04,.04,.92,.92]); ax.set_aspect('equal'); ax.axis('off')
im=(0,-1); i0=((H+1)/2,(H-1)/2); ip=(H,0)
ax.add_patch(Polygon([im,i0,ip,(0,0)],facecolor=BLUE,edgecolor='none'))
e=-np.geomspace(1e5,1e-9,2400); sx,sy=xy(e-1,P(e+1)); sx=np.r_[0,sx,P(1)]; sy=np.r_[-1,sy,0]
ax.add_patch(Polygon(np.vstack([np.column_stack([sx,sy]),[0,0],im]),facecolor=STAR,edgecolor='none'))
ax.plot([0,i0[0],ip[0]],[-1,i0[1],0],color=INK,lw=3)
ax.plot([0,0],[-1,0],color=INK,lw=3)
ax.plot(sx,sy,'--',color=RUST,lw=3)
xx=np.linspace(0,H,700); ax.plot(xx,.009*np.sin(2*np.pi*xx/H*23),color=INK,lw=3)
ax.plot([0,H],[-H,0],color=INK,lw=3)
# Same null-coordinate map as Figure 7; slightly more separated emission radii for thumbnail clarity.
for re,style in [(2.5,'-'),(1.,'--'),(.48,'-.')]:
    p=-2*np.sqrt(re)-1; q0=P(p+2); qe=H if re>=1 else -P(p)
    x,y=xy(p,np.linspace(q0,qe,500))
    assert np.allclose(np.diff(x),np.diff(y),atol=1e-12)
    if re<1: assert np.isclose(y[-1],0)
    elif re>1: assert np.isclose(x[-1]+y[-1],H)
    else: assert np.allclose([x[-1],y[-1]],ip)
    ax.plot(x,y,style,color=GOLD,lw=3.5,zorder=5)
    ax.scatter(x[0],y[0],s=65,color=GOLD,zorder=6)
    k=300; ax.annotate('',xy=(x[k],y[k]),xytext=(x[k-40],y[k-40]),arrowprops=dict(arrowstyle='-|>',color=GOLD,lw=2,mutation_scale=20),zorder=7)
if SHOW_LABELS:
    ax.text(.12,-.30,'Star',ha='center',fontsize=19,color=INK)
    ax.text(H/2,.045,'Singularity',ha='center',fontsize=19,color=INK)
ax.set(xlim=(-.12,i0[0]+.12),ylim=(-1.08,.10))
fig.savefig(OUT/f'holography_post2_feature.png',dpi=160,facecolor='white')
plt.close(fig)
