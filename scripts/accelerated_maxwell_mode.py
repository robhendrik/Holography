r"""Full-vector Maxwell eigenmode in Born-rigid accelerated rectangular cavity.

Implements the first polarization class, Friis, Lee & Louko (2013) Sec. V B,
with transverse (m,n)=(1,0) and longitudinal p=1.  Natural units c=1,
epsilon_0=mu_0=1, vertical cavity height H=1.  The physical mode is
A_y(x,z,t)=sin(pi*x/Lx)*g(z)*cos(omega*t), A_x=A_z=0.

Rindler metric: ds^2 = -(1+eps*z)^2 dt^2 + dx^2+dy^2+dz^2.
The top clock at z=1 has lapse (1+eps), whereas the reference clock is at z=0.

The Maxwell eigenproblem is (N*g')' + (omega**2/N - N*kx**2)*g=0,
with g(0)=g(1)=0.  It is a stationary Rindler eigenmode, NOT a simulation
of switching on acceleration at t=0.  Stresses calculated directly from
E and B (physical local orthonormal components) on perfect-conductor walls.
"""
import argparse
import numpy as np
from scipy.integrate import solve_ivp, simpson
from scipy.optimize import brentq
import matplotlib.pyplot as plt
from pathlib import Path

out_prefix = str(Path(__file__).resolve().parent)

def compute(eps=0.06, lx=1.0, ly=1.0, nz=1601):
    k=np.pi/lx
    z=np.linspace(0,1,nz)
    N=1+eps*z
    def integrate(omega, dense=False):
        def rhs(s,y):
            ns=1+eps*s
            return [y[1],-eps/ns*y[1] - ((omega/ns)**2-k*k)*y[0]]
        sol=solve_ivp(rhs,(0,1),[0.,1.],rtol=2e-11,atol=2e-12, dense_output=dense,
                      t_eval=None if dense else [1.])
        return sol
    wflat=np.hypot(k,np.pi)
    guesses=np.linspace(wflat*.6,wflat*1.5,75)
    samples=np.array([integrate(w).y[0,-1] for w in guesses])
    br=np.flatnonzero(samples[1:]*samples[:-1]<0)
    if len(br)==0: raise RuntimeError('Eigenvalue bracket not found')
    lo,hi=guesses[br[0]],guesses[br[0]+1]
    omega=brentq(lambda w: integrate(w).y[0,-1],lo,hi,xtol=1e-12)
    sol=integrate(omega,dense=True)
    g,gp=sol.sol(z)
    # x-y integrated quantities (time-averaged E/B fields)
    C=lx*ly/8.0
    u_xintegrated=C*((omega/N)**2*g*g+gp*gp+k*k*g*g)
    q_xintegrated=C*((omega/N)**2*g*g+gp*gp-k*k*g*g)
    energy=simpson(u_xintegrated,x=z)
    qzz=simpson(q_xintegrated,x=z)
    Fb=-C*gp[0]**2
    Ft=+C*gp[-1]**2
    Fcommon=Fb+(1+eps)*Ft
    Flocal=Fb+Ft
    kappa=qzz/energy
    # The exact local pressure identity is F_local=-eps*int((u+Qzz)/N)dz.
    Flocal_from_integral=-eps*simpson((u_xintegrated+q_xintegrated)/N,x=z)
    # normalize all by eps*E. In units H=c=1, acceleration a=eps.
    d={"epsilon":eps,"Lx":lx,"Ly":ly,"omega":omega,"omega_flat":wflat,
       "E":energy,"Qzz":qzz,"kappa":kappa,"F_bottom":Fb,"F_top":Ft,
       "F_common":Fcommon,"F_local":Flocal,"r_common":Fcommon/(eps*energy),
       "r_local":Flocal/(eps*energy),"r_local_pred_1st":-(1+kappa),
       "r_local_exact":Flocal_from_integral/(eps*energy),"r_balance_error":(Fcommon+eps*energy)/(eps*energy),
       "z":z,"g":g,"gp":gp,"N":N,"k":k,"uz_integrated":u_xintegrated,"qz_integrated":q_xintegrated}
    return d


def figures(d,path):
    z=d['z']; g=d['g']; gp=d['gp']; N=d['N']; k=d['k']; w=d['omega']; lx=d['Lx']
    x=np.linspace(0,lx,151)
    xx,zz=np.meshgrid(x,z,indexing='xy')
    sx=np.sin(k*x)[None,:]; cx=np.cos(k*x)[None,:]
    # Time-averaged local EM energy density; all physical components.
    u=.25*((w/N[:,None])**2*(sx*g[:,None])**2+(sx*gp[:,None])**2 + (k*cx*g[:,None])**2)
    qzz=.25*((w/N[:,None])**2*(sx*g[:,None])**2+(sx*gp[:,None])**2 - (k*cx*g[:,None])**2)
    relative_u=u/u.mean()
    # x average of the energy density
    zprofile=np.mean(u,axis=1)
    zprofile/=np.mean(zprofile)
    fig=plt.figure(figsize=(12,8))
    gs=fig.add_gridspec(2,2,height_ratios=[1.05,1.0])
    ax=fig.add_subplot(gs[0,0]); im=ax.imshow(relative_u,origin='lower',aspect='auto',
       extent=[0,lx,0,1],cmap='viridis')
    ax.set(title='Time-averaged Maxwell-mode energy density',xlabel='Horizontal x / H',ylabel='Vertical z / H')
    fig.colorbar(im,ax=ax,shrink=.85,label='u(x,z) / volume mean')
    ax=fig.add_subplot(gs[0,1]); ax.plot(z,zprofile,label='Accelerated Maxwell mode',lw=2)
    flat=compute(0.000001,lx,d['Ly'],nz=801)
    # zero acceleration mode profile, interpolated
    uf=flat['uz_integrated']; uf=np.interp(z,flat['z'],uf);uf/=uf.mean()
    ax.plot(z,uf,'--',label='Unaccelerated mode',lw=1.5)
    ax.set(title='Energy density averaged over x and y',xlabel='z / H',ylabel='Relative u(z)')
    ax.legend(fontsize=9)
    ax=fig.add_subplot(gs[1,0]);ax.plot(z, d['uz_integrated']/d['E'],label='u(z) integrated over x,y')
    ax.plot(z,d['qz_integrated']/d['E'],label='Tzz(z) integrated over x,y')
    ax.set(title='Stress-energy integrals',xlabel='z / H',ylabel='Density / total E')
    ax.legend(fontsize=9)
    ax=fig.add_subplot(gs[1,1]);ax.axis('off')
    t=(f"Friis et al. first EM polarization: (m,n,p)=(1,0,1)\n"
       f"epsilon = aH/c² = {d['epsilon']:.4f}; Lx/H = {d['Lx']:.2f}; Ly/H = {d['Ly']:.2f}\n"
       f"omega = {d['omega']:.7f}; omega(a=0) = {d['omega_flat']:.7f}\n\n"
       f"1) F_support / (aE/c²)       = {d['r_common']:.7f}\n"
       f"2) F_local_sum / (aE/c²)     = {d['r_local']:.7f}\n"
       f"3) kappa = integral Tzz / E  = {d['kappa']:.7f}\n"
       f"   predicted 1st-order sum  = {d['r_local_pred_1st']:.7f}\n"
       f"   exact local-force sum    = {d['r_local_exact']:.7f}\n\n"
       f"Conservation check: {d['r_balance_error']:+.2e}\n"
       f"Side-wall vertical traction: 0 (perfect conductor)\n"
       f"Note: individual coherent mode; not isotropic photon gas")
    ax.text(0.01,.98,t,va='top',family='monospace',fontsize=10)
    fig.tight_layout();fig.savefig(path,dpi=160);plt.close(fig)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--eps',type=float,default=.06)
    ap.add_argument('--lx',type=float,default=1);ap.add_argument('--ly',type=float,default=1)
    ap.add_argument('--out',default=f'{out_prefix}/accelerated_maxwell_mode.png')
    a=ap.parse_args(); d=compute(a.eps,a.lx,a.ly)
    figures(d,a.out)
    for key in ['epsilon','omega','omega_flat','kappa','r_common','r_local','r_local_pred_1st','r_local_exact','r_balance_error']:
        print(key,d[key])
    print('Figure',a.out)
