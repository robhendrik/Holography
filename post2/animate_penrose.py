"""Exact null-coordinate morph; c=1, coordinates displayed on a common scale.
Run: python animate_penrose.py  (numpy, matplotlib, pillow)
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

OUT=Path(__file__).resolve().parent
INK='#263441'; ALICE='#245778'; BOB='#a34f32'; SIGNAL='#ba8b20'
BETA=.28; receive=1/(1-BETA)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'figure.facecolor':'white'})

def transform(x,t,a):
    # Both null coordinates use the same strictly increasing function.
    # a=0: ordinary coordinates /4; a=1: exact normalized Penrose coordinates.
    scale=(1-a)/4+a*2/np.pi
    def f(q):
        return scale*q if a==0 else scale*np.arctan(a*q)/a
    u,v=f(np.asarray(t)-np.asarray(x)),f(np.asarray(t)+np.asarray(x))
    return (v-u)/2,(v+u)/2

s=np.sinh(np.linspace(-14,14,3501))
ts=np.linspace(1,receive,200)
fig,ax=plt.subplots(figsize=(6.3,6.5),dpi=130)
fig.subplots_adjust(left=.105,right=.945,bottom=.12,top=.86)

def draw(a):
    ax.clear(); ax.set(xlim=(-1.12,1.12),ylim=(-1.12,1.12),aspect='equal')
    ax.axis('off')
    if a>0:
        d=((1-a)/4+a*2/np.pi)*np.pi/(2*a)
        if d<1.2:
            ax.fill([0,d,0,-d],[d,0,-d,0],color='#e9edf0',zorder=0)
            ax.plot([0,d,0,-d,0],[d,0,-d,0,d],color=INK,lw=1.4,zorder=5)
    for k in [-10,-4,-3,-2,-1,0,1,2,3,4,10]:
        ax.plot(*transform(np.full_like(s,k),s,a),color=INK,alpha=.19,lw=.8)
        ax.plot(*transform(s,np.full_like(s,k),a),color=INK,alpha=.19,lw=.8)
    ax.plot(*transform(np.zeros_like(s),s,a),color=ALICE,lw=2.7,zorder=6)
    ax.plot(*transform(BETA*s,s,a),color=BOB,lw=2.7,ls=(0,(5,2)),zorder=6)
    x,y=transform(ts-1,ts,a)
    ax.plot(x,y,color=SIGNAL,lw=3,zorder=8)
    ax.annotate('',xy=(x[155],y[155]),xytext=(x[45],y[45]),arrowprops=dict(arrowstyle='->',color=SIGNAL,lw=2),zorder=9)
    for xx,tt,col in [(0,1,ALICE),(BETA*receive,receive,BOB)]:
        ax.scatter(*transform(xx,tt,a),s=35,color=col,edgecolor='white',linewidth=.7,zorder=10)
    for xx,tt,name,col,offset,ha in [(0,-1.5,'Alice',ALICE,(38,0),'left'),(-1.5*BETA,-1.5,'Bob',BOB,(-38,0),'right')]:
        ax.annotate(name,xy=transform(xx,tt,a),xytext=offset,textcoords='offset points',ha=ha,va='center',color=col,weight='bold',arrowprops=dict(arrowstyle='-',color=col,lw=1),zorder=11)
    ax.annotate('Light signal',xy=transform(BETA*receive,receive,a),xytext=(34,18),textcoords='offset points',ha='left',color=INK,fontsize=10,arrowprops=dict(arrowstyle='-',color=SIGNAL,lw=1),zorder=11)
    if a==0:
        ax.text(0,-1.09,'Position, x',ha='center',color=INK)
        ax.text(-1.09,0,'Time, ct',ha='center',rotation=90,color=INK)
    if a==1:
        ax.text(0,1.035,'Infinite future',ha='center',va='bottom',fontsize=10,color=INK)
        ax.text(0,-1.035,'Infinite past',ha='center',va='top',fontsize=10,color=INK)
    ax.set_title('Ordinary coordinates' if a==0 else 'Penrose diagram' if a==1 else 'Changing the coordinates',fontsize=14,pad=13,color=INK)
    fig.canvas.draw()
    return Image.fromarray(np.asarray(fig.canvas.buffer_rgba())[:,:,:3].copy())

fig.suptitle('The same Minkowski spacetime',fontsize=19,y=.965,color=INK,weight='bold')
fig.text(.5,.055,'Same observers. Same light signal.',ha='center',fontsize=13,color=INK)
fig.text(.5,.025,'Light always travels at 45°.',ha='center',fontsize=11,color=INK)
# Test every interpolation step: both null directions, monotonicity, endpoints.
q=np.linspace(-20,20,401)
for a in np.linspace(0,1,101):
    X,T=transform(q,q+1,a); assert np.allclose(T-X,(T-X)[0])
    X,T=transform(-q,q+1,a); assert np.allclose(T+X,(T+X)[0])
    X,T=transform(0,q,a); assert np.all(np.diff(T)>0)
    X,T=transform(ts-1,ts,a); assert np.allclose(T-X,(T-X)[0])
assert np.isclose(receive-1,BETA*receive)
X,T=transform(q,q/2,1); assert np.allclose(X,(np.arctan(q*1.5)-np.arctan(-q*.5))/np.pi)
# Ease in and out; return slowly to start for a seamless loop.
steps=(1-np.cos(np.linspace(0,np.pi,65)))/2
frames=[draw(float(a)) for a in steps]
frames[0].save(OUT/'ordinary.png'); frames[-1].save(OUT/'penrose.png')
frames[len(frames)//2].save(OUT/'intermediate.png')
sequence=frames+frames[-2:0:-1]
durations=[65]*len(sequence); durations[0]=1800; durations[len(frames)-1]=2200
sequence[0].save(OUT/'penrose_morph.gif',save_all=True,append_images=sequence[1:],duration=durations,loop=0,disposal=2,optimize=True)
print('Validated 101 interpolation steps; GIF saved.',len(sequence),'frames')
