
# Can an Empty Box Fill With Light Just by Accelerating?
## From classical standing waves to quantum vacuum and the Unruh effect

**Status:** Exploratory research outline  
**Prerequisite:** Light Is Heavy. And It Sinks.  
**Scope:** Quantum field theory in an accelerating cavity

---

# Central Question

We have solved Maxwell's equations inside an accelerating cavity.

But what happens when we quantize those electromagnetic modes?

If the cavity is initially empty, can acceleration produce photons?

And do different observers agree on what "empty" means?

---

# Proposed Story Arc

## 1. Once Upon a Time — An Empty Box

Take the same perfectly reflecting cavity.

Remove all classical electromagnetic radiation.

The box is now empty.

Or is it?

In quantum field theory, the electromagnetic field still exists, even in its vacuum state.

Each cavity mode becomes a quantum harmonic oscillator.

Its energy spectrum is:

\[
E_n=\hbar\omega_n(N_n+1/2).
\]

The vacuum is the state with no excitations relative to a chosen mode basis.

## 2. Every Day — The Vacuum Seems Unremarkable

For a stationary inertial cavity, we know how to define the electromagnetic modes and their annihilation operators.

The vacuum satisfies:

\[
a_n|0\rangle=0.
\]

A detector at rest in this cavity, initially in its ground state, does not undergo steady excitation in the ideal stationary vacuum.

## 3. Until One Day — We Accelerate the Box

Now accelerate the cavity.

For the coaccelerating observer, the cavity has stationary Rindler modes.

For an inertial observer, the mirrors move and the classical field configuration is time-dependent.

This raises the first question:

**Are the two observers describing the same vacuum?**

---

# Part I — The Classical Bridge

## 4. One Field, Two Coordinate Systems

Start with our existing Rindler Maxwell solution:

\[
A_y(x,\tau)=A_0\sin(k\xi(x))\cos(\omega\tau).
\]

Transform it into inertial Minkowski coordinates.

The Rindler transformation, with an appropriate choice of origin, is:

\[
cT=(x+c^2/a)\sinh(a\tau/c)
\]

\[
X=(x+c^2/a)\cosh(a\tau/c)-c^2/a.
\]

Here x is measured upward from the reference mirror; the sign convention must be adjusted consistently when reusing the top-to-bottom coordinate of Post 1.

The inertial observer sees:

- Accelerating mirrors
- Different proper accelerations at different heights
- A time-dependent electromagnetic field
- Doppler-shifted reflections
- Changing field energy and momentum

**Figure 1:** Same cavity viewed in Rindler and Minkowski coordinates.

**Figure 2:** Animation of one classical standing wave as seen by the inertial observer.

Important:

A coordinate-dependent frequency spectrum is not, by itself, evidence of photon creation.

---

# Part II — Quantizing the Modes

## 5. From Classical Modes to Quantum Oscillators

Expand the field in a complete set of cavity modes:

\[
\hat A=\sum_n
\left(
a_n u_n+a_n^\dagger u_n^*
\right).
\]

Each mode becomes a harmonic oscillator.

Define the vacuum using the annihilation operators associated with that basis.

For the accelerating cavity, natural modes are positive-frequency solutions with respect to Rindler time.

This defines a Rindler-cavity vacuum.

For a stationary inertial cavity, positive frequency is instead defined with respect to Minkowski time.

These are different physical boundary-value problems unless the motion and comparison procedure are specified.

---

## 6. Bogoliubov Coefficients

Two complete mode bases can be related by:

\[
u_n^{\mathrm{out}}
=
\sum_m
\left(
\alpha_{nm}u_m^{\mathrm{in}}
+
\beta_{nm}u_m^{\mathrm{in}*}
\right).
\]

The alpha coefficients describe positive-frequency mixing.

The beta coefficients describe mixing with complex-conjugate modes.

If the initial state is the in-vacuum, the expected number of out-quanta is:

\[
\langle N_n^{\mathrm{out}}\rangle
=
\sum_m|\beta_{nm}|^2.
\]

But we must specify what "in" and "out" mean.

A useful concrete setup is:

1. Cavity initially inertial
2. Field prepared in its inertial cavity vacuum
3. Cavity accelerates according to a prescribed trajectory
4. Cavity eventually returns to inertial motion
5. Count excitations in the final inertial cavity modes

This avoids ambiguities about comparing an eternally accelerated cavity with a free-space Minkowski vacuum.

**Figure 3:** Mode mixing under a finite acceleration protocol.

---

# Part III — Can Acceleration Create Photons?

## 7. Stationary Acceleration Versus Changing Acceleration

Distinguish two situations.

### A. Eternally stationary Rindler cavity

The geometry and boundaries are stationary in Rindler time.

The Rindler-cavity vacuum remains stationary under its own Hamiltonian.

There is no automatic continuous photon production merely because the cavity accelerates.

### B. Acceleration begins or ends

The cavity motion changes.

The mode basis can undergo nontrivial Bogoliubov mixing.

The final state may contain excitations relative to the final inertial cavity vacuum.

This is related to dynamical Casimir physics.

**Research question:**

For a finite acceleration interval, what is the resulting photon spectrum?

Does photon production depend primarily on the acceleration, its duration, or the switching profile?

---

# Part IV — What Does a Detector Actually See?

## 8. The Unruh Effect

An accelerated detector moving through the Minkowski vacuum can respond thermally.

The characteristic Unruh temperature is:

\[
T_U=\frac{\hbar a}{2\pi c k_B}.
\]

But a detector response is not identical to the presence of a pre-existing gas of real photons.

The detector interacts locally with the quantum field.

Its excitation probability depends on the field's two-point correlation function along its worldline.

---

## 9. Two Detectors Inside the Same Cavity

Place identical detectors at different heights.

The local proper acceleration differs between them.

For a Born-rigid accelerating cavity:

\[
a_{\mathrm{local}}(x)=a/N(x)
\]

with the appropriate Rindler lapse convention.

Consequently, the corresponding local Unruh temperature scale also varies with height.

But this does not automatically imply that one detector sees photons while the other does not.

We must specify:

- The quantum state of the field
- The detector energy gaps
- The detector trajectories
- The coupling and switching functions
- The cavity boundary conditions

**Research question:**

In the Rindler-cavity vacuum, do two stationary ground-state detectors at different heights remain unexcited in the long-time ideal limit?

What changes if the field is prepared in a state inherited from an initially inertial cavity?

**Figure 4:** Two detectors at different heights in the accelerating cavity.

---

# Part V — The Vacuum Depends on the Question

## 10. Three Notions That Must Stay Separate

### Coordinate-dependent mode decomposition

The same classical field can have different frequency decompositions.

### Quantum particle definition

Different positive-frequency mode bases can define different annihilation operators and vacua.

### Detector response

A detector measures local field correlations, not an abstract particle number directly.

These three ideas are connected, but not interchangeable.

This distinction is central to explaining the Unruh effect correctly.

---

# Proposed Computational Program

## Experiment 1 — Classical Field Transformation

Use our exact Rindler Maxwell modes.

Transform them to Minkowski coordinates.

Animate the moving mirrors and field evolution.

No quantization required.

## Experiment 2 — Quantized 1D Cavity

Start with a massless scalar field or one transverse electromagnetic polarization.

Construct normalized stationary cavity modes.

Calculate Bogoliubov coefficients for a finite acceleration protocol.

Verify the canonical normalization identities.

## Experiment 3 — Photon Production

Prepare the inertial cavity vacuum.

Apply acceleration for a finite time.

Return to inertial motion.

Compute:

\[
N_n=\sum_m|\beta_{nm}|^2.
\]

Explore dependence on:

- Acceleration strength
- Cavity length
- Acceleration duration
- Smooth versus abrupt switching

## Experiment 4 — Detector Response

Model two Unruh–DeWitt-type detectors at different heights.

Compute their excitation probabilities using the field correlation function.

Compare:

- Rindler-cavity vacuum
- Initially inertial vacuum evolved through acceleration
- Excited cavity states

Note: A scalar detector is a useful toy model; an electromagnetic detector requires a suitable physical coupling.

---

# Important Literature

## Closest to Our Cavity Setup

Friis, Lee & Louko (2013)

*Scalar, Spinor, and Photon Fields Under Relativistic Cavity Motion*

https://arxiv.org/abs/1307.1631

## Relativistic Cavity Motion and Quantum Mode Mixing

Bruschi, Dragan, Lee, Fuentes & Louko (2013)

*Relativistic Motion Generates Quantum Gates and Entanglement Resonances*

https://arxiv.org/abs/1201.0663

## Background Topics

- Unruh effect
- Rindler quantization
- Bogoliubov transformations
- Dynamical Casimir effect
- Quantum detectors in cavities

---

# Open Physics Questions

1. Can the Bogoliubov coefficients for our simplest 1D model be obtained analytically?

2. How does the electromagnetic case differ from the massless scalar toy model?

3. Does a smoothly accelerated cavity produce fewer photons than one with abrupt switching?

4. Can a stationary accelerating cavity exhibit detector excitations without ongoing photon production?

5. How do detector responses vary with height?

6. Which effects arise from the cavity boundaries, and which survive in unbounded Minkowski space?

7. Can we make the difference between particle number and detector response visually intuitive?

---

# Possible Ending

We began with a box full of light and discovered that light has inertia.

Then we emptied the box.

But in quantum field theory, empty is not quite as simple as it sounds.

The field remains.

And whether it contains particles may depend on how we move, how we define our modes, and what we actually measure.

**The question is no longer just whether light has weight.**

It is whether two observers can agree that the box is empty.
