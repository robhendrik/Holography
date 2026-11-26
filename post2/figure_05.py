from spacetime import *
OUT=Path(__file__).parent
fig,axs=plt.subplots(1,3,figsize=(10,4),layout='constrained')
for ax,T,title in zip(axs,[-.4,.35,.88],['Earlier','Later','Much later']):
    diamond(ax); past_diamond(ax,T); worldline(ax); ax.scatter(0,T,color=INK,s=28,zorder=6); ax.set_title(title)
    ax.text(0,-1.07,'Infinite past',ha='center',fontsize=9); ax.text(0,1.07,'Infinite future',ha='center',fontsize=9)
fig.text(.5,.015,'Blue: events that can influence Alice by the marked moment',ha='center',fontsize=12,color=INK)
fig.savefig(OUT/f'figure_05.png',dpi=220,bbox_inches='tight',pad_inches=.18)
