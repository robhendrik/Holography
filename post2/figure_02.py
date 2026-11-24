from spacetime import *
OUT=Path(__file__).parent
fig,(a,b)=plt.subplots(1,2,figsize=(10,4.8),layout='constrained')
s=np.linspace(-12,12,1000); a.plot(s,2*np.arctan(s)/np.pi,color=PAST,lw=2.5)
for y in [-1,1]: a.axhline(y,color=INK,ls='--',lw=1)
a.set(xlabel='Original coordinate',ylabel='Compressed coordinate',ylim=(-1.13,1.13),title='(a) Compress an infinite axis'); a.set_yticks([-1,0,1]); a.grid(alpha=.15)
diamond(b); grid(b); b.set_title('(b) Compress both light coordinates')
for xy,label in [((0,1.04),'Infinite future'),((0,-1.08),'Infinite past'),((1.02,0),'∞'),((-1.02,0),'−∞')]: b.text(*xy,label,ha='center' if xy[0]==0 else ('left' if xy[0]>0 else 'right'),va='center',fontsize=10)
fig.savefig(OUT/f'figure_02.png',dpi=220,bbox_inches='tight',pad_inches=.18)
