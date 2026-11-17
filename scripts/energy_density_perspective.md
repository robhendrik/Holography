
# Energy of a Single Photon in an Accelerating Cavity

## 1. Setup and Reference Observer

Consider a photon bouncing vertically between two perfectly reflecting mirrors, separated by a fixed proper distance $h$.

The cavity undergoes Born-rigid acceleration upward. The top mirror is the suspension point and serves as our reference observer.

We define:

- $x=0$: top mirror.
- $x=h$: bottom mirror.
- $a$: proper acceleration of the top mirror, directed upward.
- $\tau$: proper time of the top observer.
- $A$: constant transverse cross-sectional area.
- $E_T=\hbar\omega_T$: photon energy measured locally at the top.

The Rindler metric is

$$
ds^2=-N(x)^2c^2d\tau^2+dx^2,
$$

with

$$
N(x)=1-\frac{ax}{c^2}.
$$

Introducing

$$
\epsilon=\frac{ah}{c^2}<1,
$$

we have $N(0)=1$ and $N(h)=1-\epsilon$.

The proper acceleration and clock rate of an observer fixed at position $x$ are

$$
a_{\mathrm{loc}}(x)=\frac{a}{N(x)},
$$

$$
d\tau_x=N(x)\,d\tau.
$$

Thus, observers lower in the cavity experience greater proper acceleration and have slower clocks relative to the top observer.

## 2. Conserved Photon Energy and Local Redshift

Because the Rindler metric is stationary, the photon has a conserved Killing energy $K$, associated with translations in the top observer's time $\tau$.

For a photon measured locally at position $x$,

$$
K=N(x)E_{\mathrm{loc}}(x).
$$

At the top, $N(0)=1$, so

$$
\boxed{K=E_T=\hbar\omega_T.}
$$

Consequently,

$$
\boxed{
E_{\mathrm{loc}}(x)
=\frac{E_T}{N(x)}
=\frac{\hbar\omega_T}{1-ax/c^2}.
}
$$

The bottom observer measures

$$
E_B=\frac{E_T}{1-\epsilon}.
$$

The photon's local energy increases toward the bottom, but its Killing energy $K$ remains constant throughout the motion, including at perfectly elastic reflections.

## 3. Photon Travel Time

For a vertically moving photon, $ds^2=0$ gives

$$
d\tau=\frac{|dx|}{cN(x)}.
$$

Therefore, the one-way travel time measured by the top observer is

$$
T_{\mathrm{one}}
=\int_0^h\frac{dx}{cN(x)}
=\frac{c}{a}\ln\left(\frac{1}{1-\epsilon}\right).
$$

The round-trip time is

$$
\boxed{
T_{\mathrm{round}}
=\frac{2c}{a}\ln\left(\frac{1}{1-\epsilon}\right).
}
$$

At any fixed position $x$, the corresponding proper-time interval is multiplied by $N(x)$.

## 4. Time-Averaged Position Distribution

The photon travels repeatedly between the mirrors.

We define $P(x)\,dx$ as the probability of finding it between $x$ and $x+dx$, when sampling uniformly in the top observer's time over many round trips.

The photon traverses each position twice per round trip.

The time spent in an interval $dx$ during one round trip is

$$
dt_x=\frac{2\,dx}{cN(x)}.
$$

Dividing by the complete round-trip time,

$$
P(x)\,dx
=\frac{dt_x}{T_{\mathrm{round}}}.
$$

Hence

$$
\boxed{
P(x)=\frac{1}{cT_{\mathrm{one}}N(x)}.
}
$$

This is normalized:

$$
\int_0^h P(x)\,dx
=\frac{1}{cT_{\mathrm{one}}}
\int_0^h\frac{dx}{N(x)}
=1.
$$

Thus,

$$
\boxed{P(x)\propto N(x)^{-1}.}
$$

The photon spends a greater fraction of the top observer's time near the bottom of the accelerating cavity.

This distribution is a time average of one periodic trajectory, not a thermal equilibrium distribution.

## 5. Time-Averaged Number Density

To express the result as a volume density, imagine that the photon's transverse position is uniformly distributed over a constant area $A$.

Equivalently, calculate the energy per unit vertical length and divide by $A$.

The time-averaged photon number density is

$$
n(x)=\frac{P(x)}{A}.
$$

Therefore,

$$
\boxed{
n(x)=\frac{1}{AcT_{\mathrm{one}}N(x)}.
}
$$

Its normalization is

$$
A\int_0^h n(x)\,dx=1.
$$

For a strictly one-dimensional trajectory, the physically primary quantity is the probability per unit length $P(x)$; the transverse area $A$ is an averaging convention.

## 6. Locally Measured Energy Density

The local energy density is the photon number density multiplied by the photon energy measured by the local co-accelerating observer:

$$
u_{\mathrm{loc}}(x)
=n(x)E_{\mathrm{loc}}(x).
$$

Using the previous results,

$$
u_{\mathrm{loc}}(x)
=\frac{1}{AcT_{\mathrm{one}}N(x)}
\frac{E_T}{N(x)}.
$$

Thus,

$$
\boxed{
u_{\mathrm{loc}}(x)
=\frac{E_T}{AcT_{\mathrm{one}}}
\frac{1}{N(x)^2}.
}
$$

There are two factors:

$$
\underbrace{N^{-1}}_{\text{residence-time weighting}}
\times
\underbrace{N^{-1}}_{\text{local photon energy}}
=
\boxed{N^{-2}}.
$$

Hence

$$
\boxed{u_{\mathrm{loc}}(x)\propto N(x)^{-2}.}
$$

This is the time-averaged energy density measured by a collection of observers attached to the accelerating cavity, each using their own local energy measurements.

## 7. Energy Density Referred to the Suspension Point

We now define an energy density whose spatial integral gives the conserved energy associated with the top observer's time.

A locally measured energy contribution at position $x$ is multiplied by the lapse factor $N(x)$ when referred to the top.

Define

$$
u_T(x)=N(x)u_{\mathrm{loc}}(x).
$$

Therefore,

$$
\boxed{
u_T(x)
=\frac{E_T}{AcT_{\mathrm{one}}}
\frac{1}{N(x)}.
}
$$

The two distributions have different position dependence:

$$
u_{\mathrm{loc}}(x)\propto N(x)^{-2},
$$

$$
u_T(x)\propto N(x)^{-1}.
$$

The first is the local energy density; the second is the contribution per unit proper volume to the conserved energy referred to the suspension point.

## 8. Total Conserved Energy

The total photon energy referred to the suspension point is defined as

$$
E_{\mathrm{total},T}
=\int_V N(x)u_{\mathrm{loc}}(x)\,dV.
$$

For a constant cross-sectional area,

$$
E_{\mathrm{total},T}
=A\int_0^h u_T(x)\,dx.
$$

Substituting,

$$
E_{\mathrm{total},T}
=\frac{E_T}{cT_{\mathrm{one}}}
\int_0^h\frac{dx}{N(x)}.
$$

Since

$$
\int_0^h\frac{dx}{N(x)}
=cT_{\mathrm{one}},
$$

we find

$$
\boxed{
E_{\mathrm{total},T}=E_T=\hbar\omega_T.
}
$$

This identity is exact for every $\epsilon<1$.

The residence-time distribution, local blueshift, and lapse weighting are all accounted for.

## 9. Integrating Local Energies Without Redshift Weighting

We can also calculate the spatial integral of the local energy density without the lapse factor:

$$
E_{\mathrm{sum,loc}}
=A\int_0^h u_{\mathrm{loc}}(x)\,dx.
$$

Using

$$
\int_0^h\frac{dx}{N(x)^2}
=\frac{h}{1-\epsilon},
$$

we obtain

$$
E_{\mathrm{sum,loc}}
=\frac{E_Th}{cT_{\mathrm{one}}(1-\epsilon)}.
$$

Substituting the travel time,

$$
\boxed{
E_{\mathrm{sum,loc}}
=E_T
\frac{\epsilon}{
(1-\epsilon)\ln[1/(1-\epsilon)]
}.
}
$$

For small $\epsilon$,

$$
E_{\mathrm{sum,loc}}
=E_T\left(1+\frac{\epsilon}{2}
+O(\epsilon^2)\right).
$$

This is greater than $E_T$.

It represents an integral of local energy measurements made by observers at different heights, not the conserved Killing energy associated with the suspension point.

## 10. Connection to the Force on the Mirrors

The photon transfers momentum to the mirrors during reflection.

At the top, the local impulse magnitude is

$$
\Delta p_T=\frac{2E_T}{c}.
$$

At the bottom,

$$
\Delta p_B=\frac{2E_T}{c(1-\epsilon)}.
$$

The top mirror's average force magnitude is

$$
F_T=\frac{2E_T}{cT_{\mathrm{round}}}.
$$

The bottom mirror's proper time per round trip is

$$
T_B=(1-\epsilon)T_{\mathrm{round}}.
$$

Therefore, the bottom mirror's locally measured force magnitude is

$$
F_B^{\mathrm{loc}}
=\frac{2E_T}{c(1-\epsilon)^2T_{\mathrm{round}}}.
$$

To compare the forces using the suspension-point convention, the bottom force is lapse-weighted:

$$
F_{B\to T}=(1-\epsilon)F_B^{\mathrm{loc}}.
$$

Taking upward as positive, the net radiation force on the mirrors, referred to the top, is

$$
F_{\mathrm{rad},T}
=F_T-F_{B\to T}.
$$

Hence

$$
F_{\mathrm{rad},T}
=-\frac{2E_T}{cT_{\mathrm{round}}}
\frac{\epsilon}{1-\epsilon}.
$$

Using the exact round-trip time,

$$
\boxed{
F_{\mathrm{rad},T}
=-\frac{aE_T}{c^2}
\frac{\epsilon}{
(1-\epsilon)\ln[1/(1-\epsilon)]
}.
}
$$

Notice that

$$
\boxed{
F_{\mathrm{rad},T}
=-\frac{a}{c^2}E_{\mathrm{sum,loc}}.
}
$$

For $\epsilon\ll1$,

$$
\boxed{
F_{\mathrm{rad},T}
\longrightarrow-\frac{aE_T}{c^2}.
}
$$

Thus the light contributes an inertial mass $E_T/c^2$ in the small-cavity limit.

At finite $\epsilon$, the support-force coefficient contains a correction because the proper acceleration varies across the cavity. This does not change the conserved-energy definition.

The radiation calculation concerns forces on the mirrors. A complete suspension-force calculation must also include the cavity's material stresses.

## 11. Summary of the Exact One-Photon Results

With

$$
N(x)=1-\frac{ax}{c^2},
\qquad
\epsilon=\frac{ah}{c^2},
$$

we have:

| Quantity | Expression |
|---|---|
| Conserved Killing energy | $K=E_T=\hbar\omega_T$ |
| Local photon energy | $E_{\mathrm{loc}}(x)=E_T/N(x)$ |
| Position probability density | $P(x)=1/[cT_{\mathrm{one}}N(x)]$ |
| Number density | $n(x)=1/[AcT_{\mathrm{one}}N(x)]$ |
| Local energy density | $u_{\mathrm{loc}}(x)=E_T/[AcT_{\mathrm{one}}N(x)^2]$ |
| Top-referred energy density | $u_T(x)=E_T/[AcT_{\mathrm{one}}N(x)]$ |
| Conserved total energy | $\int_V Nu_{\mathrm{loc}}\,dV=E_T$ |
| Integral of local energies | $\int_Vu_{\mathrm{loc}}\,dV=E_T\epsilon/[(1-\epsilon)\ln(1/(1-\epsilon))]$ |

### Physical Interpretation

A single photon bouncing vertically in an accelerating cavity spends more coordinate time near the bottom, where it is also measured to have greater local energy.

Consequently, its time-averaged local energy density increases toward the back wall as $N^{-2}$.

However, the total conserved energy referred to the suspension point remains exactly $\hbar\omega_T$.

The distinction between local energy density and top-referred Killing-energy density is essential when comparing ray tracing, photon gases, Maxwell eigenmodes, and the inertia of confined light.

### Scope and Limitations

- One photon on a periodic vertical trajectory.
- Perfectly elastic reflections.
- Ideal Born-rigid cavity.
- Fixed acceleration, with $0<\epsilon<1$.
- No thermalization or redistribution among directions.
- The smooth density profile is a long-time average.
- The transverse area is introduced only as an averaging convention.
- Mirror recoil, material energy, and supporting stresses are not included in the photon-energy calculation.

The natural extension is an ensemble of photons whose individual conserved Killing energies are $K_i$.

For such an ensemble, the total conserved energy is

$$
\boxed{
E_{\mathrm{total},T}=\sum_i K_i
=\int_V N(x)u_{\mathrm{loc}}(\mathbf r)\,dV.
}
$$

This provides the energy-conservation reference for both ray-tracing and electromagnetic-mode calculations.


## Comparison: Single Vertical Photon and Isotropic 3D Photon Gas

We consider a Born-rigid cavity accelerating upward, with the suspension point at the top ($x=0$) and the back wall at $x=h$.

The Rindler lapse is

$$
N(x)=1-\frac{ax}{c^2},
\qquad
\epsilon=\frac{ah}{c^2}<1.
$$

To simplify the expressions, define

$$
I_m=\int_0^h N(x)^{-m}\,dx.
$$

Let $M$ denote the total number of photons, $E_T$ their total conserved Killing energy referred to the top observer, and $\bar K=E_T/M$ their mean conserved energy per photon.

For a single vertically bouncing photon, $M=1$ and $E_T=\hbar\omega_T$.

For the isotropic 3D photon gas, we assume a stationary phase-space distribution $f(K)$, where $K=N(x)E_{\mathrm{loc}}(x)$.

### Energy and Density Comparison

| Quantity | Single Vertical Photon (1D) | Isotropic Photon Gas (3D) |
| :--- | :--- | :--- |
| Conserved Killing energy | $K=E_T=\hbar\omega_T$ | $K_i=N(x)E_{\mathrm{loc},i}(x)$ |
| Local photon energy | $E_{\mathrm{loc}}(x)=E_T/N(x)$ | $\langle E_{\mathrm{loc}}(x)\rangle=\bar K/N(x)$ |
| Position probability density | $P(x)=N(x)^{-1}/I_1$ | $P(x)=N(x)^{-3}/I_3$ |
| Number density | $n(x)=N(x)^{-1}/(AI_1)$ | $n(x)=MN(x)^{-3}/(AI_3)$ |
| Local energy density | $u_{\mathrm{loc}}(x)=E_TN(x)^{-2}/(AI_1)$ | $u_{\mathrm{loc}}(x)=E_TN(x)^{-4}/(AI_3)$ |
| Top-referred energy density | $u_T(x)=E_TN(x)^{-1}/(AI_1)$ | $u_T(x)=E_TN(x)^{-3}/(AI_3)$ |
| Conserved total energy | $\int_V Nu_{\mathrm{loc}}\,dV=E_T$ | $\int_V Nu_{\mathrm{loc}}\,dV=E_T=\sum_i K_i$ |
| Integral of local energies | $E_T I_2/I_1$ | $E_T I_4/I_3$ |

Here $A$ is the cavity's horizontal cross-sectional area, and $I_1=cT_{\mathrm{one}}$ is the one-way photon travel time multiplied by $c$.

### Explicit Expressions for the Integrals

For $m=1$,

$$
I_1=\frac{h}{\epsilon}
\ln\left(\frac{1}{1-\epsilon}\right).
$$

For $m>1$,

$$
I_m=
\frac{h}{\epsilon(m-1)}
\left[(1-\epsilon)^{1-m}-1\right].
$$

In particular,

$$
I_2=\frac{h}{1-\epsilon},
$$

$$
I_3=\frac{h(2-\epsilon)}
{2(1-\epsilon)^2},
$$

and

$$
I_4=
\frac{h(3-3\epsilon+\epsilon^2)}
{3(1-\epsilon)^3}.
$$

### Main Scaling Laws

For the single vertically bouncing photon,

$$
n(x)\propto N(x)^{-1},
$$

$$
u_{\mathrm{loc}}(x)\propto N(x)^{-2},
$$

$$
u_T(x)\propto N(x)^{-1}.
$$

For the stationary isotropic 3D photon gas,

$$
n(x)\propto N(x)^{-3},
$$

$$
u_{\mathrm{loc}}(x)\propto N(x)^{-4},
$$

$$
u_T(x)\propto N(x)^{-3}.
$$

The additional powers in the 3D case arise from the three-dimensional momentum-space measure,

$$
d^3p=N(x)^{-3}d^3q,
\qquad
\mathbf q=N(x)\mathbf p.
$$

The local photon energy supplies an additional factor $N(x)^{-1}$.

### Total Energy

In both cases, the conserved energy referred to the suspension point is

$$
\boxed{
E_T=\int_V N(x)u_{\mathrm{loc}}(x)\,dV.
}
$$

This differs from the spatial integral of locally measured energies,

$$
E_{\mathrm{sum,loc}}
=\int_V u_{\mathrm{loc}}(x)\,dV.
$$

For the single vertical photon,

$$
E_{\mathrm{sum,loc}}
=E_T\frac{I_2}{I_1}
=E_T
\frac{\epsilon}
{(1-\epsilon)\ln[1/(1-\epsilon)]}.
$$

For the isotropic 3D gas,

$$
E_{\mathrm{sum,loc}}
=E_T\frac{I_4}{I_3}.
$$

In the limit $\epsilon\to0$, both approach $E_T$.

### Interpretation

The single vertically bouncing photon has a time-averaged position distribution proportional to $N^{-1}$ because it spends more coordinate time near the back wall. Its local energy increases toward the back wall as $N^{-1}$, giving a local energy density proportional to $N^{-2}$.

For a stationary isotropic 3D photon gas, the number density scales as $N^{-3}$ because the allowed local momentum-space volume associated with a fixed Killing-energy distribution scales as $N^{-3}$. Including the local energy blueshift gives $u_{\mathrm{loc}}\propto N^{-4}$.

The 1D result describes a periodic photon trajectory, whereas the 3D result assumes a stationary isotropic ensemble. Neither result requires treating the radiation as a material gas.

The common reference for both cases is the conserved Killing energy $E_T$, measured relative to the suspension-point clock.
