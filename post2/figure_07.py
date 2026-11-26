"""Marginally bound homogeneous dust collapse, rs=c=1.
Original calculated illustration guided by Witten arXiv:2412.16795v5, Fig. 1.
Run: python figure_07.py. Dependencies: numpy scipy matplotlib.
"""
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
OUT=Path(__file__).resolve().parent
INK='#263441'; STAR='#cab8a8'; RUST='#995b43'; GOLD='#a87526'; BLUE='#e8eff3'
def R(t): return np.maximum(-1.5*np.asarray(t),0)**(2/3)
def ts(e): return np.asarray(e)**3/12
def F(r):
    y=np.sqrt(r); return r+2*y+2*np.log(np.abs(y-1))
def G(r):
    y=np.sqrt(r); return r-2*y+2*np.log1p(y)
def LV(e):
    y=-np.asarray(e)/2; return np.log1p(y)-y+y*y/2-y**3/3
def LU(e):
    y=-np.asarray(e)/2; return np.log(np.abs(1-y))+y+y*y/2+y**3/3
def P(p): return 2/np.pi*np.arctan(np.asarray(p)/1.5)
H=float(-P(-3))
def Q_scalar(L):
    # Incoming ray label, globally increasing. For L<=0 continue through dust.
    if L==0: return float(P(1))
    if L<0:
        lo=-4.
        while LV(lo)>L: lo*=2
        e=brentq(lambda e: LV(e)-L,lo,0,xtol=1e-13)
        return float(P(e+1))
    # At exterior singularity r=0, LU(e)=-L. Enforce Q=-P(e-1).
    if L>30: return H # below machine-level resolution of the chosen chart
    e=brentq(lambda e: LU(e)+L,-2+1e-15,0,xtol=1e-14)
    return float(-P(e-1))
def Q(L): return np.array([Q_scalar(float(v)) for v in np.atleast_1d(L)])
def xy(p,q):
    pp=P(p); return (q-pp)/2,(q+pp)/2
# interior null labels p=eta-chi, q_in=eta+chi; exterior L=(t+G(r))/2
# at star eta=e, chi=1, hence p=e-1, L=LV(e).
def ray(re):
    te=-2/3*re**1.5
    if re==1: return np.linspace(te,5,500),np.ones(500)
    if re>1: r=np.linspace(re,4.6,700)
    else: r=np.linspace(re,0,700)
    return te+F(r)-F(re),r

def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,(a,b)=plt.subplots(1,2,figsize=(11,6.8),gridspec_kw={'width_ratios':[1,1.35]})
    t=np.linspace(-5,0,800); a.fill_betweenx(t,0,R(t),color=STAR,alpha=.85); a.plot(R(t),t,'--',color=RUST,lw=2)
    a.plot([0,0],[-5,0],color=INK,lw=1.5); a.plot([0,0],[0,5],color=INK,lw=2.4,ls=':')
    e=np.linspace(-3,-2,500); hr=e**2/4*(e+3); ht=ts(e)
    a.plot(hr,ht,color=INK,lw=2); a.plot([1,1],[-2/3,5],color=INK,lw=2)
    a.text(.14,3.1,'Singularity',rotation=90,color=INK,va='center'); a.text(1.14,2.8,'Event horizon',color=INK,rotation=90,va='center')
    a.text(.35,-3.7,'Star',color=INK); a.set(xlim=(-.12,4.6),ylim=(-5,5),xlabel=r'Areal radius, $r/r_s$',ylabel=r'Infall time (PG), $ct/r_s$',title='(a) Radius and time'); a.set_aspect('equal')
    im=(0,-1); i0=((H+1)/2,(H-1)/2); ip=(H,0)
    b.add_patch(Polygon([im,i0,ip,(0,0)],facecolor=BLUE,edgecolor='none'))
    es=-np.geomspace(1e5,1e-9,2400)
    # Surface: q_in=e+1 <=1, so Q=P(e+1) exactly.
    sx,sy=xy(es-1,P(es+1))
    sx=np.r_[0,sx,float(P(1))]; sy=np.r_[-1,sy,0]
    b.add_patch(Polygon(np.vstack([np.column_stack([sx,sy]),[0,0],im]),facecolor=STAR,alpha=.95,edgecolor='none'))
    b.plot([0,i0[0],ip[0]],[-1,i0[1],ip[1]],color=INK,lw=1.5)
    b.plot([0,0],[-1,0],color=INK,lw=1.5); b.plot(sx,sy,'--',color=RUST,lw=2.1)
    # Wiggle is a conventional graphical symbol, not a change in coordinates.
    xx=np.linspace(0,H,700); b.plot(xx,.009*np.sin(2*np.pi*xx/H*23),color=INK,lw=1.6)
    b.plot([0,H],[-H,0],color=INK,lw=2)
    b.text(-.035,-.49,'Center (r = 0)',rotation=90,ha='right',va='center'); b.text(.10,-.37,'Star',ha='center')
    b.text(H/2,.045,'Singularity',ha='center'); b.text(.40,-H+.40-.047,'Event horizon',rotation=45,ha='center',va='top',color=INK)
    escape_edge = ((i0[0]+ip[0])/2, (i0[1]+ip[1])/2)
    b.annotate('Light escapes\nto infinity', xy=escape_edge, xytext=(i0[0]+.045, i0[1]+.13), ha='left', va='center', fontsize=10, arrowprops=dict(arrowstyle='-', color=INK, lw=1.0))
    assert np.isclose(sum(escape_edge), H)
    assert ip[0] < escape_edge[0] < i0[0]
    b.text(H+.025,.035,'Infinite future',ha='left',fontsize=10)
    styles=['-','--','-.']
    for j,re in enumerate([1.6,1.,.72]):
        tt,rr=ray(re); mask=(tt<=5)&(rr<=4.6); a.plot(rr[mask],tt[mask],color=GOLD,lw=2,ls=styles[j],zorder=5)
        a.scatter(rr[0],tt[0],s=25,color=GOLD,zorder=6); a.annotate(str(j+1),(rr[0],tt[0]),xytext=[(9,-12),(9,-13),(-15,6)][j],textcoords='offset points',weight='bold')
        p=-2*np.sqrt(re)-1; q0=float(P(p+2)); qend=H if re>=1 else float(-P(p)); qs=np.linspace(q0,qend,500); x,y=xy(p,qs)
        b.plot(x,y,color=GOLD,lw=2,ls=styles[j],zorder=5); b.scatter(x[0],y[0],s=25,color=GOLD,zorder=6); b.annotate(str(j+1),(x[0],y[0]),xytext=[(8,-13),(9,-4),(-15,7)][j],textcoords='offset points',weight='bold')
        k=300; b.annotate('',xy=(x[k],y[k]),xytext=(x[k-25],y[k-25]),arrowprops={'arrowstyle':'-|>','color':GOLD,'lw':1.4})
        ids=np.flatnonzero(mask); k=ids[len(ids)//2]; k0=ids[max(0,len(ids)//2-35)]; a.annotate('',xy=(rr[k],tt[k]),xytext=(rr[k0],tt[k0]),arrowprops={'arrowstyle':'-|>','color':GOLD,'lw':1.4})
        assert np.max(abs(np.diff(y)-np.diff(x)))<1e-12
        if re!=1: assert np.max(abs(tt-F(rr)-(tt[0]-F(rr[0]))))<1e-10
        else: assert np.all(rr==1)
        if re<1: assert abs(y[-1])<1e-12 and rr[-1]==0
        if re>1: assert abs(x[-1]+y[-1]-H)<1e-12
        # Independently verify the surface match and exterior incoming mapping.
        assert abs(Q([(tt[0]+G(re))/2])[0]-q0)<1e-10
        if re<1: assert abs(Q([tt[-1]/2])[0]-qend)<1e-10
    # Independent samples of singular boundary in vacuum and dust.
    ee=np.linspace(-1.99,-.03,200); assert np.max(abs(P(ee-1)+Q(-LU(ee))))<1e-9
    chi=np.linspace(0,1,200); assert np.max(abs(P(-chi)+P(chi)))<1e-14
    assert np.all(np.diff(Q(np.linspace(-20,15,500)))>0)
    b.set(xlim=(-.14,1.16),ylim=(-1.06,.13),aspect='equal',title='(b) Penrose diagram'); b.axis('off')
    fig.text(.5,.045,'1  Escapes     •     2  Follows the horizon     •     3  Reaches the singularity',ha='center',color=INK,fontsize=12)
    fig.subplots_adjust(bottom=.14,top=.91,wspace=.20)
    for ext in ['png']: fig.savefig(OUT/f'figure_07.{ext}',dpi=220,bbox_inches='tight')
    print('PASS: null slopes, matching, ray endpoints, horizontal singularity, monotone incoming coordinate')
if __name__=='__main__': main()
