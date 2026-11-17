
# Light Is Heavy — A Photon in an Accelerating Box

## 1. A Photon Between Two Mirrors

Consider a photon bouncing vertically between two perfectly reflecting mirrors, separated by a distance $L$.

The photon satisfies the vacuum dispersion relation:

$$
k^2-\frac{\omega^2}{c^2}=0.
$$

Choose the reference frame of the top mirror. At the instant of reflection, the top mirror is at rest:

$$
k_T=\frac{\omega}{c}, \qquad v_T=0.
$$

The bottom mirror moves with velocity $v$ relative to this frame.

## 2. Lorentz Transformation at the Bottom Mirror

The photon wave vector and angular frequency transform according to

$$
k_b=\gamma\left(k_T-\frac{v\omega}{c^2}\right),
$$

$$
\omega_b=\gamma(\omega-vk_T),
$$

where

$$
\gamma=\frac{1}{\sqrt{1-v^2/c^2}}.
$$

For $v\ll c$, we take $\gamma\simeq1$.

## 3. Momentum Transfer at the Mirrors

At the top mirror, reflection reverses the photon's momentum:

$$
\Delta p_T=2\hbar k_T.
$$

At the bottom mirror, the corresponding momentum transfer is

$$
\Delta p_b=-2\hbar
\left(k_T-\frac{v\omega}{c^2}\right).
$$

Adding the two contributions gives

$$
\Delta p
=\Delta p_T+\Delta p_b
=\frac{2\hbar\omega v}{c^2}.
$$

Thus,

$$
\boxed{\Delta p=\frac{2\hbar\omega v}{c^2}}.
$$

## 4. From Momentum Transfer to Force

The time for one complete round trip is

$$
\Delta t=2\tau,
$$

where $\tau=L/c$ is the one-way light-travel time.

The average force is

$$
F=\frac{\Delta p}{\Delta t}
=\frac{2\hbar\omega}{c^2}\frac{v}{\Delta t}.
$$

For constant acceleration $g$, the relative velocity acquired during one light-travel time is

$$
v=g\tau.
$$

Since

$$
\Delta t=2\tau,
$$

we have

$$
\frac{v}{\Delta t}=\frac{g}{2}.
$$

Substituting,

$$
F=\frac{2\hbar\omega}{c^2}\frac{g}{2}.
$$

Therefore,

$$
\boxed{F=\frac{\hbar\omega}{c^2}g}.
$$

## 5. The Inertial Mass of Confined Light

Comparing with Newton's second law,

$$
F=mg,
$$

we identify

$$
\boxed{m=\frac{\hbar\omega}{c^2}}.
$$

Since the photon energy is

$$
E=\hbar\omega,
$$

the result is

$$
\boxed{m=\frac{E}{c^2}}.
$$

A photon has no invariant mass of its own, but the energy of light confined inside a box contributes to the inertia of the complete system.

## 6. Assumptions and Interpretation

This derivation assumes:

- Perfectly reflecting mirrors.
- A single photon propagating vertically.
- Small relative velocities, $v\ll c$.
- Constant acceleration over a light round trip.
- Negligible recoil and deformation of the mirrors.

The essential mechanism is the Doppler shift at the moving mirror. The photon transfers slightly different amounts of momentum at the two ends of the cavity.

Over one complete round trip, the imbalance produces a force proportional to the photon's energy and the acceleration:

$$
F=\frac{E}{c^2}g.
$$

### A Subtlety: Comparing Forces in Different Frames

The wave vector $k_b$ is expressed in the bottom mirror's instantaneous rest frame, whereas $k_T$ is expressed in the top mirror's frame.

Strictly, the corresponding momentum transfers cannot simply be added without specifying how forces are compared between frames.

This distinction is important when connecting the Doppler argument to the $4/3$ problem and to the stresses in the cavity walls.

The derivation above captures the first-order Doppler argument; a complete calculation must also account consistently for the frame in which momentum and force are defined.

# Light Is Heavy — Photon Propagation in an Accelerating Cavity

## 1. The Metric

Consider a cavity of height $h$ in an accelerating reference frame.

Using the Rindler metric,

$$
ds^2=-\left(1-\frac{ax}{c^2}\right)^2c^2d\tau^2+dx^2.
$$

Here:

- $x=0$ is the top mirror.
- $x=h$ is the bottom mirror.
- $a$ is the proper acceleration at the top mirror.
- $\tau$ is the proper time measured at the top.
- The photon travels vertically between the mirrors.

## 2. Photon Travel Time

For light, $ds^2=0$. Therefore,

$$
0=-\left(1-\frac{ax}{c^2}\right)^2c^2d\tau^2+dx^2.
$$

Solving for the time interval gives

$$
d\tau=\frac{|dx|}{c(1-ax/c^2)}.
$$

The one-way travel time is

$$
\tau_L=\int_0^h\frac{dx}{c(1-ax/c^2)}.
$$

Integrating,

$$
\boxed{
\tau_L=-\frac{c}{a}\ln\left(1-\frac{ah}{c^2}\right)
}
$$

Because the metric is static, the upward and downward travel times are equal:

$$
\tau_\uparrow=\tau_\downarrow=\tau_L.
$$

The round-trip time is

$$
\boxed{
\Delta\tau=-\frac{2c}{a}\ln\left(1-\frac{ah}{c^2}\right)
}
$$

## 3. Radiation Force at the Top Mirror

For a photon with energy $E=\hbar\omega$, the momentum transfer at a perfect reflection is

$$
\Delta p=2\hbar k=\frac{2E}{c}.
$$

The average force at the top mirror is

$$
F_{\mathrm{top}}=\frac{2\hbar k}{\Delta\tau}.
$$

Substituting the round-trip time,

$$
\boxed{
F_{\mathrm{top}}=
-\frac{\hbar k a}{c\ln(1-ah/c^2)}
}
$$

## 4. Redshift at the Bottom Mirror

Define

$$
\epsilon=\frac{ah}{c^2}.
$$

The photon wave number at the bottom is

$$
\boxed{
k_{\mathrm{bottom}}=\frac{k}{1-\epsilon}
}
$$

The proper time at the bottom and top mirrors is related by

$$
d\tau_{\mathrm{bottom}}
=(1-\epsilon)d\tau_{\mathrm{top}}.
$$

The local average force at the bottom is therefore

$$
F_{\mathrm{bottom}}
=\frac{2\hbar k_{\mathrm{bottom}}}
{(1-\epsilon)\Delta\tau}.
$$

Substituting,

$$
\boxed{
F_{\mathrm{bottom}}
=\frac{2\hbar k}
{(1-\epsilon)^2\Delta\tau}
}
$$

## 5. Net Force

To compare forces at the two mirrors, we must specify a common time coordinate.

The bottom force, referred to the top clock, is weighted by the lapse factor $1-\epsilon$.

Thus,

$$
F_{\mathrm{bottom\to top}}
=(1-\epsilon)F_{\mathrm{bottom}}.
$$

The net force balance is

$$
F_{\mathrm{net}}
=F_{\mathrm{top}}
-F_{\mathrm{bottom\to top}}.
$$

Substituting the expressions above,

$$
F_{\mathrm{net}}
=\frac{2\hbar k}{\Delta\tau}
-\frac{2\hbar k}{(1-\epsilon)\Delta\tau}.
$$

Hence,

$$
F_{\mathrm{net}}
=-\frac{2\hbar k}{\Delta\tau}
\frac{\epsilon}{1-\epsilon}.
$$

For $\epsilon\ll1$,

$$
\Delta\tau\simeq\frac{2h}{c}.
$$

Therefore,

$$
F_{\mathrm{net}}
\simeq-\frac{\hbar kc}{h}\epsilon.
$$

Using $\epsilon=ah/c^2$ and $E=\hbar kc$,

$$
\boxed{
F_{\mathrm{net}}\simeq-\frac{Ea}{c^2}
}
$$

The negative sign indicates the direction of the force relative to the chosen coordinate orientation.

## 6. Inertial Mass of the Photon

The magnitude of the force is

$$
F=\frac{Ea}{c^2}.
$$

Comparing with $F=ma$, we identify

$$
\boxed{
m=\frac{E}{c^2}
}
$$

For a single photon,

$$
\boxed{
m=\frac{\hbar\omega}{c^2}
}
$$

## 7. Interpretation

The top observer measures the acceleration $a$, the cavity height $h$, and the photon energy $E$.

The accelerating frame produces a position-dependent photon frequency. The bottom mirror measures a higher photon energy than the top mirror.

Two effects enter the calculation:

1. **Gravitational redshift:** The photon momentum at the bottom differs from that at the top.
2. **Time dilation:** The reflection rates measured using local clocks differ between the two mirrors.

By referring both forces to the top observer's clock, we obtain the inertial contribution of the confined photon:

$$
\boxed{E=mc^2}
$$

This calculation concerns the radiation contribution. A complete physical cavity also contains mirrors and mechanical stresses, whose contributions must be included when calculating the total energy and momentum of the system.

## 5. Net Force — Exact Expression

We retain the exact expressions for the forces on the top and bottom mirrors, postponing the small-cavity approximation.

Define

$$
\epsilon=\frac{ah}{c^2}.
$$

The round-trip travel time, measured by the top observer, is

$$
\Delta\tau=\frac{2c}{a}\ln\left(\frac{1}{1-\epsilon}\right).
$$

The average force at the top mirror is

$$
F_{\mathrm{top}}
=\frac{2\hbar k}{\Delta\tau}
=\frac{\hbar ka}{c}
\frac{1}{\ln\left(\frac{1}{1-\epsilon}\right)}.
$$

The local average force at the bottom mirror is

$$
F_{\mathrm{bottom}}
=\frac{2\hbar k}{(1-\epsilon)^2\Delta\tau}
=\frac{\hbar ka}{c}
\frac{1}{(1-\epsilon)^2\ln\left(\frac{1}{1-\epsilon}\right)}.
$$

### Referring Both Forces to the Top Observer

The forces act at different heights and are measured using different local clocks.

To refer the bottom force to the top observer, we multiply by the lapse factor $1-\epsilon$:

$$
F_{\mathrm{bottom\to top}}
=(1-\epsilon)F_{\mathrm{bottom}}.
$$

The net force, taking the upward direction as positive, is

$$
F_{\mathrm{net}}
=F_{\mathrm{top}}-(1-\epsilon)F_{\mathrm{bottom}}.
$$

Substituting the exact expressions,

$$
F_{\mathrm{net}}
=\frac{\hbar ka}{c}
\frac{1}{\ln\left(\frac{1}{1-\epsilon}\right)}
\left[
1-\frac{1}{1-\epsilon}
\right].
$$

Since

$$
1-\frac{1}{1-\epsilon}
=-\frac{\epsilon}{1-\epsilon},
$$

we obtain

$$
\boxed{
F_{\mathrm{net}}
=-\frac{\hbar ka}{c}
\frac{\epsilon}
{(1-\epsilon)\ln\left(\frac{1}{1-\epsilon}\right)}
}.
$$

## 6. Small-Cavity Limit

Only now do we consider the limit $\epsilon\to0$, corresponding to $ah/c^2\ll1$.

Using

$$
\ln\left(\frac{1}{1-\epsilon}\right)
=\epsilon+\frac{\epsilon^2}{2}
+\frac{\epsilon^3}{3}+\cdots,
$$

we find

$$
\lim_{\epsilon\to0}
\frac{\epsilon}
{(1-\epsilon)\ln\left(\frac{1}{1-\epsilon}\right)}
=1.
$$

Therefore,

$$
\boxed{
\lim_{\epsilon\to0}F_{\mathrm{net}}
=-\frac{\hbar ka}{c}
}.
$$

Since the photon energy measured at the top mirror is

$$
E=\hbar\omega=\hbar kc,
$$

the force becomes

$$
\boxed{
F_{\mathrm{net}}=-\frac{Ea}{c^2}
}.
$$

The negative sign indicates the downward force relative to the chosen coordinate orientation.

The magnitude of the force is

$$
F=\frac{Ea}{c^2}.
$$

Comparing with Newton's second law, $F=ma$, we identify

$$
\boxed{
m=\frac{E}{c^2}
}.
$$

## 7. Physical Interpretation

The top observer knows the cavity height $h$, the acceleration $a$, and the photon energy $E$.

The acceleration produces a frequency shift between the mirrors. Consequently, the photon transfers different amounts of momentum at the top and bottom.

Two effects enter the force calculation:

1. **Frequency shift:** The photon momentum at the bottom is larger by a factor $1/(1-\epsilon)$.
2. **Time dilation:** The bottom mirror's local reflection rate is larger by another factor $1/(1-\epsilon)$.

The local bottom force therefore contains the factor $1/(1-\epsilon)^2$.

When comparing the two forces using the top observer's clock, one factor is removed by the lapse correction $1-\epsilon$.

The resulting force is

$$
F_{\mathrm{net}}
=-\frac{Ea}{c^2}
\frac{\epsilon}
{(1-\epsilon)\ln\left(\frac{1}{1-\epsilon}\right)}.
$$

In the small-cavity limit, this reduces to

$$
\boxed{F_{\mathrm{net}}=-\frac{Ea}{c^2}}.
$$

This establishes the inertial contribution of the confined photon within the accelerating-cavity model.

**Qualification:** The calculation combines radiation-pressure forces using the top observer's time convention. A complete mechanical description of the cavity must also include the stresses that hold the mirrors apart.


## Three Effects in the Accelerating Cavity

There are three distinct effects that determine the difference between the forces measured at the top and bottom mirrors.

Define

$$
\epsilon=\frac{ah}{c^2},
\qquad N=1-\epsilon.
$$

### 1. Wavelength (Frequency Shift)

The bottom observer measures a shorter wavelength and therefore a larger photon momentum:

$$
\frac{p_{\mathrm{bottom}}}{p_{\mathrm{top}}}
=\frac{1}{1-\epsilon}.
$$

This increases the momentum transferred during each reflection at the bottom mirror.

### 2. Time Dilation (Reflection Rate)

The bottom observer's clock runs more slowly relative to the top observer's clock:

$$
\Delta\tau_{\mathrm{bottom}}
=(1-\epsilon)\Delta\tau_{\mathrm{top}}.
$$

Consequently, the bottom observer measures a higher reflection rate:

$$
\frac{\Delta\tau_{\mathrm{top}}}
{\Delta\tau_{\mathrm{bottom}}}
=\frac{1}{1-\epsilon}.
$$

Combining the first two effects gives the ratio of locally measured forces:

$$
\boxed{
\frac{F_{\mathrm{bottom}}}{F_{\mathrm{top}}}
=\frac{1}{(1-\epsilon)^2}
}.
$$

Thus, the wavelength shift and time dilation reinforce each other.

### 3. Referring the Bottom Force to the Top Observer

To compare forces acting at different heights, we must express them using a common reference convention.

The bottom force, referred to the top observer, is

$$
F_{\mathrm{bottom\to top}}
=(1-\epsilon)F_{\mathrm{bottom}}.
$$

This introduces a factor $1-\epsilon$, cancelling one of the two factors from the first two effects.

Therefore,

$$
\boxed{
\frac{F_{\mathrm{bottom\to top}}}
{F_{\mathrm{top}}}
=\frac{1}{1-\epsilon}
}.
$$

The three factors combine as

$$
\underbrace{\frac{1}{1-\epsilon}}_{\text{photon momentum}}
\times
\underbrace{\frac{1}{1-\epsilon}}_{\text{local reflection rate}}
\times
\underbrace{(1-\epsilon)}_{\text{force referred to top}}
=
\boxed{\frac{1}{1-\epsilon}}.
$$

### Physical Interpretation

The first two effects are differences in local measurements:

1. The photon transfers more momentum per reflection at the bottom.
2. The bottom observer measures more reflections per unit of local proper time.

The third effect is different. It is not an additional physical change to the photon, but the conversion needed to compare forces at different heights using the top observer's reference convention.

The resulting imbalance is

$$
F_{\mathrm{net}}
=F_{\mathrm{top}}-(1-\epsilon)F_{\mathrm{bottom}}.
$$

Therefore,

$$
F_{\mathrm{net}}
=F_{\mathrm{top}}
\left(1-\frac{1}{1-\epsilon}\right)
=-F_{\mathrm{top}}\frac{\epsilon}{1-\epsilon}.
$$

Using the exact expression

$$
F_{\mathrm{top}}
=\frac{\hbar ka}{c}
\frac{1}{\ln\left(\frac{1}{1-\epsilon}\right)},
$$

we obtain

$$
\boxed{
F_{\mathrm{net}}
=-\frac{\hbar ka}{c}
\frac{\epsilon}
{(1-\epsilon)\ln\left(\frac{1}{1-\epsilon}\right)}
}.
$$

Only now, taking $\epsilon\to0$,

$$
\boxed{
F_{\mathrm{net}}\longrightarrow
-\frac{\hbar ka}{c}
=-\frac{Ea}{c^2}
}.
$$

The magnitude of the force corresponds to an inertial mass

$$
\boxed{m=\frac{E}{c^2}}.
$$

**Note:** This is the radiation-force calculation in the idealized accelerating-cavity model. The force transmitted to an actual suspension sensor also requires accounting for mechanical stresses in the cavity.