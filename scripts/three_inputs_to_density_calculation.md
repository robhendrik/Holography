
# The Stationary Isotropic Photon Gas in an Accelerating Cavity

## 1. Physical Setup

Consider a perfectly rigid rectangular cavity accelerating upward through flat spacetime.

The cavity has height $h$, with its suspension point at the top. We use the downward vertical coordinate $x$:

- $x=0$: top mirror and suspension point.
- $x=h$: bottom mirror (the back wall).
- $a$: proper acceleration of the top mirror, directed upward.
- $\tau$: proper time of the top observer.

The Rindler metric is

$$
ds^2=-N(x)^2c^2d\tau^2+dx^2+dy^2+dz^2,
$$

where

$$
N(x)=1-\frac{ax}{c^2}.
$$

We require

$$
\epsilon=\frac{ah}{c^2}<1.
$$

The proper acceleration of a stationary observer at height $x$ is

$$
a_{\mathrm{loc}}(x)=\frac{a}{N(x)}.
$$

Our objective is to determine the spatial distribution of photon number and energy in a stationary, locally isotropic radiation field.

In particular, we want to understand whether photons become more concentrated toward the back wall.

## 2. Describing the Radiation With a Phase-Space Distribution

Instead of following a single photon, we introduce the phase-space distribution

$$
f(\tau,\mathbf r,\mathbf p).
$$

It is defined such that

$$
d\mathcal N=f(\tau,\mathbf r,\mathbf p)\,d^3r\,d^3p
$$

is the expected number of photons in a small spatial volume $d^3r$ and momentum-space volume $d^3p$ on a surface of constant Rindler time $\tau$.

The momentum $\mathbf p$ is measured in the instantaneous local rest frame of an observer attached to the cavity.

The local photon number density is

$$
n(\tau,\mathbf r)=\int f(\tau,\mathbf r,\mathbf p)\,d^3p.
$$

The local radiation energy density is

$$
u_{\mathrm{loc}}(\tau,\mathbf r)
=\int c|\mathbf p|\,f(\tau,\mathbf r,\mathbf p)\,d^3p.
$$

We assume the distribution is spatially uniform in the two horizontal directions, so that any position dependence is through $x$.

We now introduce three assumptions.

## 3. Assumption 1: Collisionless Propagation and Elastic Reflection

Between wall reflections, photons propagate freely along null trajectories.

The Hamiltonian governing their motion in Rindler time is

$$
H(x,\mathbf p)=N(x)c|\mathbf p|.
$$

Because the cavity geometry is independent of $\tau$, this Hamiltonian is conserved:

$$
\boxed{
K=N(x)c|\mathbf p|=\text{constant}.
}
$$

Here $K$ is the Killing energy of an individual photon, referred to the suspension-point clock.

Consequently, the local photon energy is

$$
E_{\mathrm{loc}}(x)=c|\mathbf p|
=\frac{K}{N(x)}.
$$

A photon travelling toward the back wall is locally blueshifted.

At a perfectly elastic wall reflection, the photon energy measured in the wall's instantaneous rest frame is unchanged. Since the wall is stationary in Rindler coordinates, $K$ is also conserved at reflection.

The collisionless phase-space distribution obeys Liouville's equation:

$$
\boxed{
\frac{\partial f}{\partial\tau}
+\frac{\partial H}{\partial\mathbf p}\cdot\nabla_{\mathbf r}f
-\nabla_{\mathbf r}H\cdot\nabla_{\mathbf p}f
=0.
}
$$

This expresses conservation of phase-space density along freely propagating photon trajectories.

It does not prescribe the distribution $f$ or require it to be isotropic.

**Physical meaning:** photons are neither created nor destroyed, and their individual Killing energies are conserved.

## 4. Assumption 2: Stationarity

We assume that the radiation has reached a stationary state relative to the accelerating cavity.

Mathematically,

$$
\boxed{
\frac{\partial f}{\partial\tau}=0.
}
$$

This is stronger than requiring only the local photon number density to be time independent:

$$
\frac{\partial n}{\partial\tau}=0.
$$

Stationarity of $f$ requires the complete local momentum distribution to remain unchanged with time.

Photons continue to move and reflect, but the statistical distribution at each position remains constant.

Using the Hamiltonian

$$
H=N(x)cp,
\qquad p=|\mathbf p|,
$$

the stationary transport equation becomes

$$
cN\frac{\mathbf p}{p}\cdot\nabla_{\mathbf r}f
-cpN'(x)\frac{\partial f}{\partial p_x}=0,
$$

where $p_x$ is the downward momentum component and

$$
N'(x)=\frac{dN}{dx}=-\frac{a}{c^2}.
$$

Because the distribution depends on position only through $x$,

$$
\boxed{
N\frac{p_x}{p}\frac{\partial f}{\partial x}
-pN'(x)\frac{\partial f}{\partial p_x}=0.
}
$$

This equation constrains how the momentum distribution may vary with height while remaining stationary.

However, stationarity alone does not determine the spatial photon density.

Different stationary distributions can retain information about photon trajectories and conserved transverse momentum components.

## 5. Assumption 3: Local Isotropy

We now assume that an observer attached to the cavity sees the same photon distribution in every momentum direction.

At fixed position $x$ and fixed momentum magnitude $p$, the phase-space distribution is independent of direction.

Mathematically,

$$
\boxed{
f(x,\mathbf p)=f(x,p),
\qquad p=|\mathbf p|.
}
$$

This does not mean that the photon number density is the same at every height.

It also does not mean that the photon energy spectrum is identical at every height.

Local isotropy concerns only the angular dependence of the momentum distribution.

For an isotropic distribution,

$$
\frac{\partial f}{\partial p_x}
=\frac{p_x}{p}\frac{\partial f}{\partial p}.
$$

Substituting into the stationary transport equation gives

$$
\frac{p_x}{p}
\left[
N\frac{\partial f}{\partial x}
-pN'(x)\frac{\partial f}{\partial p}
\right]=0.
$$

Because this must hold for arbitrary photon directions, we obtain

$$
\boxed{
N\frac{\partial f}{\partial x}
-pN'(x)\frac{\partial f}{\partial p}=0.
}
$$

We can now solve for the allowed distribution.

## 6. Deriving the Stationary Phase-Space Distribution

The characteristic curves of the preceding equation satisfy

$$
\frac{dp}{dx}=-\frac{N'(x)}{N(x)}p.
$$

Equivalently,

$$
\frac{dp}{p}=-\frac{dN}{N}.
$$

Integrating,

$$
\ln p+\ln N=\text{constant},
$$

so

$$
Np=\text{constant}.
$$

Since $cNp=K$, the general solution is

$$
\boxed{
f(x,\mathbf p)=F(N(x)c|\mathbf p|)=F(K).
}
$$

Here $F$ is an arbitrary nonnegative function representing the distribution over conserved Killing energies.

We have not assumed a thermal spectrum.

For example, $F$ could describe a narrow energy band, a monoenergetic ensemble, or a thermal radiation field.

The essential result is that the dependence on position and momentum magnitude occurs through the combination $N(x)cp$.

This result follows from:

1. Collisionless photon propagation.
2. Stationarity of the phase-space distribution.
3. Local isotropy of the momentum distribution.

The spatial photon-density profile has not been imposed independently.

## 7. Deriving the Local Photon Number Density

The photon number density is

$$
n(x)=\int f(x,\mathbf p)\,d^3p.
$$

Using the derived distribution,

$$
n(x)=\int F(N(x)c|\mathbf p|)\,d^3p.
$$

Introduce the new momentum variable

$$
\mathbf q=N(x)\mathbf p.
$$

At fixed $x$, the lapse factor $N(x)$ is constant in the momentum integration.

Because momentum space is three-dimensional,

$$
d^3p=N(x)^{-3}d^3q.
$$

Therefore,

$$
n(x)=N(x)^{-3}
\int F(c|\mathbf q|)\,d^3q.
$$

The remaining integral is independent of position.

At the top, $N(0)=1$, so

$$
n(0)=\int F(c|\mathbf q|)\,d^3q.
$$

Hence,

$$
\boxed{
n(x)=n(0)N(x)^{-3}.
}
$$

The photon number density increases toward the back wall because $N(x)$ decreases downward.

The exponent $-3$ follows from the three-dimensional momentum-space measure.

## 8. Deriving the Local Radiation Energy Density

The local energy density is

$$
u_{\mathrm{loc}}(x)
=\int cp\,f(x,\mathbf p)\,d^3p.
$$

Substituting the stationary distribution,

$$
u_{\mathrm{loc}}(x)
=\int cp\,F(Ncp)\,d^3p.
$$

Again define $\mathbf q=N\mathbf p$.

Then

$$
p=\frac{q}{N},
\qquad
d^3p=N^{-3}d^3q.
$$

Therefore,

$$
u_{\mathrm{loc}}(x)
=N(x)^{-4}
\int cq\,F(cq)\,d^3q.
$$

The integral equals the energy density at the top.

Thus,

$$
\boxed{
u_{\mathrm{loc}}(x)
=u_{\mathrm{loc}}(0)N(x)^{-4}.
}
$$

The fourth power consists of:

$$
\underbrace{N^{-3}}_{\text{photon number density}}
\times
\underbrace{N^{-1}}_{\text{mean local photon energy}}
=
\boxed{N^{-4}}.
$$

Notice that the density gradient is not an independently prescribed property of the system. It follows from the stationary isotropic phase-space distribution.

## 9. Total Energy Referred to the Suspension Point

The local energy density is measured by observers at different positions, each using their own proper time.

The conserved energy associated with the suspension-point clock is

$$
\boxed{
E_T=\int_V N(x)u_{\mathrm{loc}}(x)\,dV.
}
$$

Define the energy density referred to the top observer as

$$
u_T(x)=N(x)u_{\mathrm{loc}}(x).
$$

Using the derived local energy density,

$$
\boxed{
u_T(x)=u_{\mathrm{loc}}(0)N(x)^{-3}.
}
$$

For a cavity with constant horizontal cross-sectional area $A$,

$$
E_T=A u_{\mathrm{loc}}(0)\int_0^h N(x)^{-3}\,dx.
$$

Define

$$
I_3=\int_0^h N(x)^{-3}\,dx.
$$

Then

$$
u_{\mathrm{loc}}(0)=\frac{E_T}{AI_3}.
$$

Consequently, the normalized density profiles are

$$
\boxed{
u_{\mathrm{loc}}(x)
=\frac{E_T}{AI_3}N(x)^{-4},
}
$$

and

$$
\boxed{
u_T(x)
=\frac{E_T}{AI_3}N(x)^{-3}.
}
$$

The conserved total energy is exactly

$$
\boxed{
\int_V N(x)u_{\mathrm{loc}}(x)\,dV=E_T.
}
$$

## 10. What Have We Assumed, and What Have We Derived?

| Property | Assumed or derived? |
| :--- | :--- |
| Photons propagate freely between reflections | Assumed |
| Reflections conserve local photon energy | Assumed |
| Individual Killing energy $K=Ncp$ is conserved | Derived from stationary geometry and elastic reflection |
| Phase-space distribution is stationary, $\partial f/\partial\tau=0$ | Assumed |
| Momentum distribution is locally isotropic | Assumed |
| Phase-space distribution has form $f=F(K)$ | Derived |
| Photon number density obeys $n(x)\propto N^{-3}$ | Derived |
| Local energy density obeys $u_{\mathrm{loc}}(x)\propto N^{-4}$ | Derived |
| Top-referred energy density obeys $u_T(x)\propto N^{-3}$ | Derived |
| The system evolves toward this distribution | **Not established** |

## 11. The Role of the Walls

The derivation determines a stationary, locally isotropic solution of the photon transport equation.

It does not establish whether this state will develop from arbitrary initial conditions.

The wall-reflection mechanism becomes important here.

### Perfectly Specular Walls

Specular reflection reverses the normal momentum component and preserves the tangential components in the local wall frame.

The stationary distribution $F(K)$ is compatible with specular reflection.

However, specular reflection does not generally erase information about the photon's initial trajectory.

Other stationary, anisotropic distributions may therefore exist.

### Diffusely Reflecting Walls

Diffuse reflection randomizes the outgoing momentum direction while preserving its locally measured magnitude.

Such reflections can mix photon trajectories and may drive the radiation toward a locally isotropic stationary state.

For isotropic radiation in the interior, the outgoing flux distribution at a wall follows Lambert's cosine law,

$$
\frac{dP}{d\Omega}\propto\cos\theta,
$$

where $\theta$ is measured from the inward wall normal.

Thus, Lambertian diffuse reflection is compatible with the stationary isotropic distribution.

Whether the stochastic wall dynamics actually converge to this distribution, and under which conditions, is a separate dynamical question.

## 12. Research Question

We have derived a possible stationary radiation state in a uniformly accelerating cavity:

$$
\boxed{
f(x,\mathbf p)=F(N(x)c|\mathbf p|).
}
$$

This predicts

$$
\boxed{
n(x)\propto N(x)^{-3},
\qquad
u_{\mathrm{loc}}(x)\propto N(x)^{-4}.
}
$$

Our central research question is:

**Does radiation confined in a uniformly accelerating cavity evolve toward a stationary, locally isotropic phase-space distribution, and how does the reflection mechanism of the walls affect that evolution?**

The theoretical calculation identifies the stationary isotropic solution.

The dynamics of the cavity determine whether that solution is actually reached.

This distinction is essential when comparing single-photon trajectories, ray-tracing simulations, and full electromagnetic cavity modes.
