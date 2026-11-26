<!--
HOLOGRAPHY — POST 2 — MEDIUM PUBLISHING METADATA (not article prose)
Status: GATE B — complete prose draft, internally reviewed / awaiting author approval / not approved for publication
Revision: 2026-11-25 — full prose draft, scientific and author-voice review

Medium title: A Black Hole Has Formed. Why Can’t We See It Happen?
Medium subtitle: Which parts of the universe can influence us, which parts can we influence, and how does a black hole change that?
Medium topics (choose up to five):
  - Black Holes
  - General Relativity
  - Physics
  - Spacetime
  - Astronomy
SEO title: Why Can’t We See a Black Hole Form? Penrose Diagrams Explained
SEO description: Follow light signals through spacetime and discover why some events remain invisible to a distant observer, however long they wait.
Suggested preview title: A Black Hole Has Formed. Why Can’t We See It Happen?
Suggested preview subtitle: How a black hole changes what we can ever observe
Publication: Science Spectrum (select at publishing time, if approved)
Canonical URL: [leave blank unless an earlier original is the canonical source]
Featured image: holography_post2_feature.png
Featured-image caption: A collapsing star, seen through a Penrose diagram. Image by author.
Featured-image alt text: Penrose diagram of a collapsing star, showing the event horizon, singularity, and three gold light rays with different destinations.
Suggested excerpt: Some events in the universe can influence us, while others are still beyond our reach. Penrose diagrams reveal how these regions change as we wait, and why a black hole places a permanent limit on what we can observe.

Asset notes:
- Final numbering: Figures 1–9, including separately numbered animations 4 and 8. Do not renumber.
- Figure 4: figure_04_penrose_morph.gif. The latest uploaded copy has one frame; the recovered original has 128 frames and is included in the asset package.
- Figure 5: figure_05.png (three growing past regions).
- Figure 6: figure_06.png (three panels). Before publication, correct the left-hand arrow in panel (a) so both arrows indicate the same direction through the center; panels (b,c) already illustrate the incoming and outgoing radial segments.
- Figure 7: figure_07.png (latest supplied areal-radius/PG-time version); use the calculated marginally bound homogeneous dust model. Distinguish the coordinate radius from a measured distance.
- Figure 8: figure_08_morph.gif (recovered 68-frame animation); figure_08_morph_final.png is the still supplied for review and may serve as a fallback, not a separately numbered figure. Intermediate frames are illustrative interpolations, not certified conformal charts.
- Figure 9: figure_09.png (latest supplied causal schematic). Do not describe its curves as calculated constant-radius trajectories or as the identical coordinate map of Figure 7. Signals 1–3 end on Alice; signal 4 follows the horizon without a reception marker. Final polish: move Never accessible label clear of the stellar surface and verify leader lines. Check consistency of null boundaries and worldlines before publication.
- Featured image completed: use the text-free calculated Penrose diagram. Confirm image credits and animated GIF handling in the importer before publication.
- Use Unicode for inline mathematical notation; no inline LaTeX. Use display equations only where they materially help.

Editorial handoff:
- Classical general relativity; idealized spherical, nonrotating, non-evaporating collapse. Figure 7 uses the calculated dust model; Figure 9 is schematic. No claim of a quantitative constant-radius trajectory in Figure 9.
- Tong §4.4.2 and Witten arXiv:2412.16795v5 §3 checked against their online text. Reference [3] added for the collapse coordinates (standard PG metric, Eq. 12 in the preprint arXiv:1008.0470). No new figures were generated in this prose revision.
- Gate B: author review required. Resolve Figure 6 arrow, Figure 9 visual polish, animation review and importer tests before publication.
-->

# A Black Hole Has Formed. Why Can’t We See It Happen?
## Which parts of the universe can influence us, which parts can we influence, and how does a black hole change that?

![Feature image](holography_post2_feature.png)
> Caption: A collapsing star, seen through a Penrose diagram. Image by author.
> Alt text: Penrose diagram of a collapsing star, showing the event horizon, singularity, and three gold light rays with different destinations.
> Source: Image by author.

## What Can Influence Us?

Suppose Alice is observing a star one light-year away. If the star emitted a flash of light six months ago, she would not see it yet. Even if she knew exactly where to look, she would have to wait another six months. For now we assume that spacetime is flat and that the star and Alice are at rest relative to each other.

At any given moment, some events in the universe can influence Alice and others cannot. Information cannot travel faster than light.

We can draw these regions in a spacetime diagram. We consider one spatial dimension, with position *x* on the horizontal axis. On the vertical axis we plot time *t* multiplied by the speed of light *c*. Both axes now have units of length, and with equal scales on the two axes, light follows lines at 45°.

The point in the middle of Figure 1 represents Alice at one particular moment. Such a point is called an event: it specifies both a position and a time. The dashed vertical line is Alice’s worldline, the succession of events that describes her life at a fixed position.

The two diagonal lines divide spacetime into four regions. An event in the blue region can send a signal that reaches Alice by the marked moment. The yellow region contains events that she can influence from that moment onwards. Exchanging a signal between Alice now and an event in either gray region would require faster-than-light communication. The blue and yellow regions are the interiors of her past and future light cones.

![Figure 1](figure_01.png)
> Caption: **Figure 1.** Alice at a particular moment in spacetime. Events in the blue region can influence Alice, while Alice can influence events in the yellow region. Events in the gray regions cannot exchange a signal with Alice at the marked moment. The diagonal lines represent the paths of light.
> Alt text: Square position–time diagram with Alice at the center, a blue triangle below, a pale yellow triangle above, and gray triangles on either side. Diagonal light paths separate the four regions.
> Source: Image by author.

The emission of the flash belongs to a gray region in Figure 1. Six months from now, it will lie on the boundary of Alice’s blue region.

## How Do We Draw Infinity?

As Alice moves up her worldline, the blue region grows. Events that could not influence her yesterday may be able to do so today. Can she eventually receive a signal from every event if she waits long enough?

Our diagram covers only a finite range of positions and times. We need a way to draw all of spacetime on a finite piece of paper while preserving the distinction between the blue, yellow and gray regions.

A function that maps the entire real line onto a finite interval is the arctangent. For a dimensionless variable *s*, we use the normalized form

$$
f(s)=\frac{2}{\pi}\arctan(s).
$$

As *s* increases, *f(s)* approaches +1; for increasingly negative values of *s*, it approaches −1 (Figure 2a). Neither limit is reached for any finite *s*.

Applying this function separately to position and time would compress the diagram, but light paths would no longer be straight lines at 45°. Instead, we use two coordinates that are directly related to the paths of light. We define

$$
u=\frac{ct-x}{L},\qquad v=\frac{ct+x}{L},
$$

where *L* is an arbitrary reference length that makes *u* and *v* dimensionless. For light travelling to the right, *x* increases at the same rate as *ct*, so *u* remains constant. For light travelling to the left, *v* remains constant.

We compress *u* and *v* into new light coordinates *U* and *V*. Their sum and difference give us the new vertical coordinate *T* and horizontal coordinate *X*:

$$
\begin{aligned}
U&=f(u),\qquad V=f(v),\\[4pt]
T&=\frac{V+U}{2},\qquad X=\frac{V-U}{2}.
\end{aligned}
$$

For light travelling to the right, *T* − *X* is constant; for light travelling to the left, *T* + *X* is constant. Both directions are still at 45°. Along any future-directed physical path, neither light coordinate can decrease. Compressing them with a strictly increasing function preserves this condition. The result is the diamond in Figure 2b, a **Penrose diagram** of flat spacetime [1].

![Figure 2](figure_02.png)
> Caption: **Figure 2.** The normalized arctangent compresses the real line into the open interval from −1 to +1. Applying this compression separately to the two light coordinates produces a diamond while preserving the 45° direction of light rays. The left and right corners represent spatial infinity, not infinite time. Based on [1].
> Alt text: Left, a normalized arctangent curve approaching −1 and +1. Right, a diamond-shaped spacetime diagram with curved coordinate lines, infinite past and future at the bottom and top, and spatial infinity at the left and right corners.
> Source: Image by author.

The four corners have different meanings. At the top and bottom, time goes to plus or minus infinity at fixed position. The left and right corners represent spatial infinity, for example when we let *x* tend to −∞ or +∞ at a fixed time. A light ray travelling forever reaches one of the diagonal edges instead. These edges represent limits, not places where the light encounters a wall.

## The Same Spacetime, Drawn Differently

Suppose Bob moves to the right at a constant velocity relative to Alice. Alice sends him a light signal. Figure 3 shows its emission and reception in the ordinary coordinates of special relativity (Minkowski spacetime) and in the Penrose diagram of the same spacetime.

![Figure 3](figure_03.png)
> Caption: **Figure 3.** Alice remains at a fixed position while Bob moves to the right at constant velocity. Their paths look different in ordinary Minkowski coordinates and in the Penrose diagram, but the light signal connects exactly the same two events.
> Alt text: Two panels show Alice as a solid blue vertical line, Bob as a dashed rust-colored line, and a short gold light signal between them. Bob's straight path becomes curved in the diamond-shaped diagram on the right.
> Source: Image by author.

Bob’s worldline has become curved in the Penrose diagram, but he is still moving at the same constant velocity relative to Alice. Neither physical distances nor time intervals can be read directly from the new diagram.

The light signal, however, still connects the same two events at 45°. We can see this throughout the transformation in Figure 4.

![Figure 4](figure_04_penrose_morph.gif)
> Caption: **Figure 4.** Ordinary Minkowski coordinates gradually transform into a Penrose diagram. The grid and the observers’ paths change shape, but the light signal continues to connect the same events and retains its 45° direction.
> Alt text: Looping animation in which a rectangular spacetime grid compresses into a diamond, carrying Alice's and Bob's paths and their connecting light signal along with it.
> Source: Image by author.

A physical signal can only travel upwards, at no more than 45° from the vertical. The worldline of a massive observer must lie strictly within these two directions.

## Can We Eventually See Everything?

Alice waits at a fixed position in Minkowski spacetime. At three successive moments we draw her past light cone (Figure 5).

![Figure 5](figure_05.png)
> Caption: **Figure 5.** The blue region is Alice’s accessible past at three successive times. For an observer at a fixed position in Minkowski spacetime, every finite event is eventually included. Based on [1].
> Alt text: Three Penrose diamonds marked Earlier, Later and Much later. A point moves upwards along Alice's vertical path, and the blue region below it expands until it nearly fills the diamond.
> Source: Image by author.

The blue region covers more and more of the diamond. For any event at a finite position and time, a light signal can reach Alice in a finite time. She does not need to reach the point labelled Infinite future to receive it.

There is no region of this universe that is permanently inaccessible to Alice. The events she cannot yet observe simply require more time. Does this result still hold if our spacetime contains a black hole?

## From a Line to a Universe

A collapsing star occupies three spatial dimensions. If the star remains spherical throughout the collapse, we can still use a diagram with only two axes.

Instead of distinguishing directions in space, we retain only the radius *r*. A point at nonzero radius in our spacetime diagram now represents an entire spherical surface at a particular time.

Figure 6a shows three such spherical surfaces. If they remain at fixed radii, they become the three vertical lines in Figure 6b. Applying the same transformation as before, with *r* in place of *x*, gives us the three curved lines in Figure 6c.

![Figure 6](figure_06.png)
> Caption: **Figure 6.** Three spherical shells are represented by their radii in ordinary spacetime and by corresponding curves in the Penrose diagram. A light ray passes through the center and continues outwards on the other side. Its change of direction in the radial diagrams reflects the use of the nonnegative radius *r*, not a physical reflection. Based on [1].
> Alt text: Three panels show numbered concentric spherical shells, three matching vertical lines in radial spacetime, and three matching curved lines inside a triangular Penrose diagram. A gold light path passes through the center.
> Source: Image by author.

The diamond has become a triangle because *r* cannot be negative. The vertical line on the left is the center, not an edge of the physical universe. A light ray travelling straight through the center first moves to smaller radii and then to larger radii. Its path in the radial diagrams changes from an upward-left to an upward-right diagonal, although the light itself has not reflected.

## A Star Collapses

Suppose we put a star in this universe and let it collapse under its own gravity. Our model is a nonrotating, homogeneous sphere of pressureless matter, collapsing from rest at infinity [3]. We use classical general relativity and neglect evaporation.

Figure 7a shows the radius of the stellar surface (the dashed brown line) decreasing with time. Here the radial coordinate *r* is defined so that the sphere has area *A* = 4π*r²*. This is called the areal radius. It does not in general equal the distance measured along a radial path from the center.

The unit of radius in the figure is the Schwarzschild radius *rₛ*, which depends on the mass *M* of the star and Newton’s gravitational constant *G*:

$$
r_s=\frac{2GM}{c^2}.
$$

Here *t* denotes Painlevé–Gullstrand time, a time coordinate based on freely falling observers [3]. Unlike the usual Schwarzschild time, it allows us to follow the collapsing surface through *r* = *rₛ*. We can therefore draw light signals emitted before, at and after the surface passes this radius.

In the vacuum outside the stellar material, the radial coordinate velocity of outward-directed light in these coordinates is

$$
\frac{dr}{dt}=c\left(1-\sqrt{\frac{r_s}{r}}\right).
$$

Consider the three signals in Figure 7a. The first leaves the star while its radius is still larger than *rₛ*. The radial velocity is positive, and the light travels to larger radii. For the second signal, emitted at *r* = *rₛ*, the radial coordinate velocity is zero. The third signal is also directed outwards, but because the radius of the star is now smaller than *rₛ*, its radial coordinate velocity is negative. It travels towards smaller radii until it encounters the singularity.

![Figure 7](figure_07.png)
> Caption: **Figure 7.** Three outward-directed light signals leave the surface of an idealized collapsing star. Signal 1 escapes, signal 2 follows the event horizon, and signal 3 reaches the singularity. Panel (a) uses areal radius *r* and Painlevé–Gullstrand (PG) time, which remains regular at the horizon. Panel (b) shows the same collapse in Penrose coordinates, where all three signals follow parallel 45° lines. Calculated for a homogeneous pressureless collapse model [3], with the diagram guided by [2].
> Alt text: Left, the radius of a collapsing star decreases with time. Three numbered light paths bend outwards, remain vertical at the horizon, or turn towards zero radius. Right, the corresponding Penrose diagram shows three diagonal gold paths, a dashed stellar surface, and a horizontal wavy singularity.
> Source: Image by author.

All three signals are emitted radially outwards in the local frame of the collapsing surface, and all travel locally at the speed of light. The sign of the coordinate velocity tells us whether the areal radius increases or decreases, not how fast light passes a local observer.

In Figure 7b the star occupies the brown region. The triangular diagram of Figure 6 has acquired a new upper boundary, drawn as a wavy line. This represents the singularity, where the classical spacetime ends. Light cannot pass through it as it could through the regular center in Figure 6.

The three light paths become parallel lines at 45°. Signal 1 reaches the upper-right boundary, which represents light escaping to infinity. Signal 2 follows the diagonal line that separates light paths that can escape from those that cannot. Signal 3 ends at the wavy line.

The separating line is the **event horizon**. Trace it backwards and you find that it starts at the center of the star, before it reaches the stellar surface. Part of the star is already inside the horizon before the surface crosses it. The horizon is not a material barrier that stops light. Its location is determined by where light can eventually go in the entire spacetime [2].

Figure 8 shows how the vertical part of the horizon becomes diagonal and the singularity at zero radius becomes a horizontal future boundary.

![Figure 8](figure_08_morph.gif)
> Caption: **Figure 8.** A visual transition between the areal-radius and PG-time representation of Figure 7 and its Penrose diagram. The constant-radius part of the horizon becomes diagonal, and the singularity becomes a horizontal future boundary. The intermediate frames are an illustrative interpolation, not necessarily conformal coordinate systems.
> Alt text: Animation transforming the collapsing star, its horizon, singularity and three light paths from a radius–time diagram into a compact Penrose diagram and back again.
> Source: Image by author.

Signal 3 moves to the right in the Penrose diagram while approaching zero areal radius. Moving to the right no longer necessarily means moving to a larger radius.

## Infinity Is No Longer Enough

Let Alice observe the collapsing star from a great distance, remaining outside the horizon and eventually settling at a fixed radius. We give her as much time as she needs and ask which events can ever send a signal that reaches her.

Figure 9 compares the answer with the one we found for flat spacetime. The left panel is the limit of the process shown in Figure 5, now drawn using radial coordinates. In the right panel, Alice remains outside the black hole and her worldline approaches the upper end of the horizon in the infinite future. There is a whole region of spacetime from which she can never receive a signal.

We can see why by picking an event in the gray region and drawing a light ray towards the right. The ray ends at the singularity, without crossing the horizon. Any slower signal travelling towards the future is confined to directions between the two possible radial light paths, so it cannot escape either. The horizon is the limiting outward-directed light path between those that escape and those that reach the singularity.

![Figure 9](figure_09.png)
> Caption: **Figure 9.** Blue marks events that can eventually influence Alice. In empty Minkowski spacetime, an observer remaining at a fixed position can eventually receive a signal from any finite event. With a black hole, the gray region remains inaccessible to Alice, however long she waits outside the horizon. Signals 1–3 reach Alice at successively later moments; signal 4 is emitted at horizon crossing and follows the horizon without ever reaching her. Schematic causal diagrams guided by [1,2].
> Alt text: Two radial Penrose diagrams compare an entirely blue empty universe with a black-hole spacetime divided into blue and gray regions by a diagonal event horizon. Alice follows a blue curve in each panel. In the right panel, the dashed stellar surface extends to the singularity. Three gold signals end on Alice’s path; a fourth follows the horizon without an arrival dot.
> Source: Image by author.

We have also drawn four light signals emitted from the stellar surface. The first three reach Alice. The fourth is emitted precisely when the stellar surface crosses the horizon, and there is no reception event on Alice’s worldline.

For a distant observer held at a fixed radius, the closer the emission is to horizon crossing, the longer the signal takes to arrive. Near the horizon, the outgoing radial velocity in Figure 7a is proportional to the difference *r* − *rₛ*. Integrating the inverse of that velocity gives a travel time that grows without bound as the emission radius approaches *rₛ*. If the collapsing surface emits light at a fixed frequency in its own frame, the light received from progressively closer to the crossing is also increasingly redshifted [2]. The surface fades from view; Alice does not see a bright image of it frozen at the horizon forever.

The gaps between the reception events in Figure 9 are illustrative, not measurements of elapsed time. But the absence of a fourth reception event is a physical result, independent of how we choose the coordinates.

## A New Perspective on Horizons

There is a difference between knowing that a black hole has formed and receiving light from the event at which the stellar surface crossed the horizon. Alice can infer the former from observations outside the horizon and a model of the collapse. The latter is impossible, even with a perfect telescope.

We can wait longer. We can look closer. But from the outside, we will never see the star cross its horizon.

**Infinity is no longer enough.**

Suppose Alice waits another second. How much closer to the horizon was the light she now receives emitted? In the next post we will use this relation between reception time and emission near the horizon to make the connection with the quantum physics of black holes [2].

## References

1. David Tong, *General Relativity* (2019), lecture notes, University of Cambridge. Section 4.4.2 (Penrose diagrams) and Section 6.1 (Schwarzschild solution). https://www.damtp.cam.ac.uk/user/tong/gr.html

2. Edward Witten, *Introduction to Black Hole Thermodynamics*, arXiv:2412.16795v5 (first posted 2024), Section 3, Figures 1–2 and Eqs. (7)–(8). https://arxiv.org/html/2412.16795v5

3. Y. Kanai, M. Siino and A. Hosoya, *Gravitational Collapse in Painlevé–Gullstrand Coordinates*, Progress of Theoretical Physics **125**, 1053–1065 (2011). https://doi.org/10.1143/PTP.125.1053
