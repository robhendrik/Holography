import argparse
import numpy as np
import matplotlib.pyplot as plt

r"""Monte Carlo photons in a Born-rigid uniformly accelerated rectangular cavity.

Coordinates are dimensionless with z in [0,1] spanning the vertical cavity size H,
while x in [0, ax_ratio], y in [0, ay_ratio] span the horizontal sizes.
The Rindler lapse is N(z)=1+eps*z where eps=aH/c^2.  (This matches the earlier
script's convention; changing the reference wall only affects higher-order details.)

Reflection model:
- specularity = 1.0  -> perfectly specular reflection.
- specularity = 0.0  -> fully diffuse reflection with p(mu)  mu**power over the inward hemisphere.
- intermediate values  -> Bernoulli mixture: specular with probability specularity, diffuse otherwise.

Outputs:
1) common-clock/support force ratio:      F_support c^2 /(a <E>)
2) simple sum of local wall-force ratios: F_local   c^2 /(a <E>)
3) kappa = (\int T^{zz} dV)/E, estimated directly from ray samples,
   so the local-force prediction is -(1+kappa).
"""
from pathlib import Path

out_prefix = str(Path(__file__).resolve()/"accelerated_cavity_mc_extended")

def sample_diffuse_inward(rng, normals, power):
    """Sample diffuse outgoing directions on the hemisphere about inward unit normals.
    normals: (m,3) array of unit normals pointing into the cavity.
    returns (m,3) local directions.
    """
    m = len(normals)
    mu = rng.random(m) ** (1.0 / (power + 1.0))
    phi = rng.uniform(0.0, 2*np.pi, m)
    rr = np.sqrt(np.maximum(1.0 - mu*mu, 0.0))

    # build orthonormal tangential basis per normal
    a = np.tile(np.array([1.0, 0.0, 0.0]), (m, 1))
    close = np.abs((normals * a).sum(axis=1)) > 0.9
    a[close] = np.array([0.0, 1.0, 0.0])
    t1 = np.cross(normals, a)
    t1 /= np.linalg.norm(t1, axis=1)[:, None]
    t2 = np.cross(normals, t1)
    out = mu[:, None] * normals + (rr*np.cos(phi))[:, None] * t1 + (rr*np.sin(phi))[:, None] * t2
    out /= np.linalg.norm(out, axis=1)[:, None]
    return out


def reflect_specular(d_in, normals):
    dot = (d_in * normals).sum(axis=1)
    out = d_in - 2.0 * dot[:, None] * normals
    out /= np.linalg.norm(out, axis=1)[:, None]
    return out


def run(
    n=12000,
    rounds=600,
    burn=150,
    eps=0.02,
    ax_ratio=1.0,
    ay_ratio=1.0,
    power=1,
    specularity=0.0,
    bins_z=28,
    bins_x=28,
    seed=7,
    out_prefix='/mnt/data/accelerated_cavity'
):
    rng = np.random.default_rng(seed)

    # initial positions uniformly throughout cavity
    xyz = np.column_stack([
        rng.random(n) * ax_ratio,
        rng.random(n) * ay_ratio,
        rng.random(n)
    ])
    # initial directions isotropic in local frame
    u = rng.uniform(-1, 1, n)
    phi = rng.uniform(0, 2*np.pi, n)
    dirs = np.stack([np.sqrt(1-u*u)*np.cos(phi), np.sqrt(1-u*u)*np.sin(phi), u], axis=1)

    N0 = 1.0 + eps * xyz[:, 2]
    K = N0.copy()      # conserved Killing energy; initial local photon energy set to 1

    impulse_common = np.zeros(6)   # [xL,xR,yL,yR,bottom,top]
    impulse_local = np.zeros(6)
    time_integral = 0.0
    time_integral_energy = 0.0
    time_integral_energy_nz2 = 0.0
    dwell_energy_z = np.zeros(bins_z)
    dwell_time_z = np.zeros(bins_z)
    dwell_energy_xz = np.zeros((bins_z, bins_x))
    dwell_time_xz = np.zeros((bins_z, bins_x))
    checkpoints = []

    for step in range(rounds):
        nx, ny, nz = dirs.T
        z0 = xyz[:, 2]

        # Time-like parameter q = c * Delta t / H in the flat embedding.
        candidates = []
        wall_ids = []
        # x walls
        q = np.divide(0.0 - xyz[:, 0], nx, out=np.full(n, np.inf), where=nx < -1e-14)
        candidates.append(q); wall_ids.append(0)
        q = np.divide(ax_ratio - xyz[:, 0], nx, out=np.full(n, np.inf), where=nx > 1e-14)
        candidates.append(q); wall_ids.append(1)
        # y walls
        q = np.divide(0.0 - xyz[:, 1], ny, out=np.full(n, np.inf), where=ny < -1e-14)
        candidates.append(q); wall_ids.append(2)
        q = np.divide(ay_ratio - xyz[:, 1], ny, out=np.full(n, np.inf), where=ny > 1e-14)
        candidates.append(q); wall_ids.append(3)

        # z walls: exact intersection with Rindler hyperbola, same algebra as the earlier script.
        A = -eps * (nx*nx + ny*ny)
        B = 2.0 * N0 * nz
        for zw, wid in [(0.0, 4), (1.0, 5)]:
            C = (z0 - zw) * (2.0 + eps * (z0 + zw))
            disc = B*B - 4.0*A*C
            sq = np.sqrt(np.maximum(disc, 0.0))
            with np.errstate(divide='ignore', invalid='ignore'):
                root1 = (-B + sq) / (2.0*A)
                root2 = (-B - sq) / (2.0*A)
                linear = -C / B
            q1 = np.where((root1 > 1e-12) & np.isfinite(root1), root1, np.inf)
            q2 = np.where((root2 > 1e-12) & np.isfinite(root2), root2, np.inf)
            q = np.minimum(q1, q2)
            q = np.where((np.abs(A) < 1e-12) & (linear > 1e-12), linear, q)
            q = np.where(disc >= 0.0, q, np.inf)
            candidates.append(q); wall_ids.append(wid)

        qs = np.stack(candidates, axis=0)
        pick = qs.argmin(axis=0)
        q = qs[pick, np.arange(n)]
        which = np.array(wall_ids, dtype=int)[pick]
        if not np.isfinite(q).all():
            raise RuntimeError('Ray lost; candidate intersections failed numerically.')

        # Update endpoint positions
        x1 = xyz[:, 0] + nx * q
        y1 = xyz[:, 1] + ny * q
        newN = np.sqrt(np.maximum(N0*N0 + 2*eps*N0*nz*q - eps**2*(nx*nx + ny*ny)*q*q, 0.0))
        z1 = (newN - 1.0) / eps
        z1 = np.where(which == 4, 0.0, np.where(which == 5, 1.0, z1))
        newN = 1.0 + eps * z1

        # Rindler time increment of the chosen reference clock used by the original script.
        rapidity = np.arctanh(np.clip(eps*q / (N0 + eps*nz*q), -1+1e-14, 1-1e-14))
        dt = rapidity / eps
        beta = np.tanh(rapidity)

        # Incoming direction in local rest frame of struck wall/static observer at the event.
        fac = 1.0 / (np.cosh(rapidity) * (1.0 - nz*beta))
        d_in = np.column_stack((nx*fac, ny*fac, (nz - beta) / (1.0 - nz*beta)))
        d_in /= np.linalg.norm(d_in, axis=1)[:, None]

        # Inward normals
        normals = np.zeros_like(d_in)
        normals[which == 0, 0] = 1.0
        normals[which == 1, 0] = -1.0
        normals[which == 2, 1] = 1.0
        normals[which == 3, 1] = -1.0
        normals[which == 4, 2] = 1.0
        normals[which == 5, 2] = -1.0

        d_spec = reflect_specular(d_in, normals)
        d_diff = sample_diffuse_inward(rng, normals, power=power)
        use_spec = rng.random(n) < specularity
        d_out = np.where(use_spec[:, None], d_spec, d_diff)
        d_out /= np.linalg.norm(d_out, axis=1)[:, None]

        E = K / newN   # local photon energy at the collision
        impulse_z = E * (d_in[:, 2] - d_out[:, 2])  # vertical wall impulse in local frame

        if step >= burn:
            f = rng.random(n)
            alpha = f * rapidity
            betas = np.tanh(alpha)
            Ns = N0 / (np.cosh(alpha) - nz*np.sinh(alpha))
            zs = np.clip((Ns - 1.0) / eps, 0.0, 1.0 - 1e-12)
            xs = np.clip(xyz[:, 0] + nx * (f*q), 0.0, ax_ratio - 1e-12)
            Es = K / Ns
            nzs = (nz - betas) / (1.0 - nz*betas)

            bz = np.minimum((bins_z * zs).astype(int), bins_z - 1)
            bx = np.minimum((bins_x * (xs / ax_ratio)).astype(int), bins_x - 1)
            np.add.at(dwell_time_z, bz, dt)
            np.add.at(dwell_energy_z, bz, dt * Es)
            np.add.at(dwell_time_xz, (bz, bx), dt)
            np.add.at(dwell_energy_xz, (bz, bx), dt * Es)

            time_integral += dt.sum()
            time_integral_energy += (dt * Es).sum()
            time_integral_energy_nz2 += (dt * Es * nzs*nzs).sum()
            np.add.at(impulse_common, which, impulse_z)
            np.add.at(impulse_local, which, impulse_z / newN)

            if (step + 1) % 50 == 0:
                common_ratio = impulse_common.sum() / (eps * time_integral_energy)
                local_ratio = impulse_local.sum() / (eps * time_integral_energy)
                kappa = time_integral_energy_nz2 / time_integral_energy
                checkpoints.append((step + 1, common_ratio, local_ratio, kappa))

        xyz = np.column_stack((np.clip(x1, 0.0, ax_ratio), np.clip(y1, 0.0, ay_ratio), np.clip(z1, 0.0, 1.0)))
        dirs = d_out
        N0 = newN

    # Outputs 1, 2, 3.
    common_ratio = impulse_common.sum() / (eps * time_integral_energy)
    local_ratio = impulse_local.sum() / (eps * time_integral_energy)
    kappa = time_integral_energy_nz2 / time_integral_energy
    predicted_local = -(1.0 + kappa)

    wall_names = ['x-left', 'x-right', 'y-left', 'y-right', 'bottom', 'top']
    per_wall_common = impulse_common / (eps * time_integral_energy)
    per_wall_local = impulse_local / (eps * time_integral_energy)

    print('=== accelerated cavity MC (extended) ===')
    print(f'N={n}, rounds={rounds}, burn={burn}, eps={eps}, ax_ratio={ax_ratio}, ay_ratio={ay_ratio}')
    print(f'specularity={specularity} (1=perfect specular, 0=fully diffuse), diffuse power={power}, seed={seed}')
    print('1) common-clock/support force ratio      =', common_ratio)
    print('2) simple sum of local wall-force ratios =', local_ratio)
    print('3) kappa = int(Tzz dV)/E                 =', kappa)
    print('   predicted local-force ratio -(1+kappa)=', predicted_local)
    print('Per-wall common-clock ratios:')
    for nme, val in zip(wall_names, per_wall_common):
        print(f'  {nme:>8s}: {val: .6f}')
    print('Per-wall local-force ratios:')
    for nme, val in zip(wall_names, per_wall_local):
        print(f'  {nme:>8s}: {val: .6f}')
    if checkpoints:
        print('Final checkpoint:', checkpoints[-1])

    # Visuals
    z_centres = (np.arange(bins_z) + 0.5) / bins_z
    x_centres = ax_ratio * (np.arange(bins_x) + 0.5) / bins_x

    energy_density_z = np.divide(dwell_energy_z, dwell_time_z, out=np.zeros_like(dwell_energy_z), where=dwell_time_z > 0)
    energy_density_xz = np.divide(dwell_energy_xz, dwell_time_xz, out=np.zeros_like(dwell_energy_xz), where=dwell_time_xz > 0)

    rel_z = energy_density_z / np.nanmean(energy_density_z)
    rel_xz = energy_density_xz / np.nanmean(energy_density_xz)
    pred = (1.0 + eps * z_centres) ** -4
    pred /= pred.mean()

    fig = plt.figure(figsize=(12, 8))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1.0])

    ax0 = fig.add_subplot(gs[0, 0])
    im = ax0.imshow(rel_xz, origin='lower', aspect='auto',
                    extent=[0, ax_ratio, 0, 1], interpolation='nearest')
    ax0.set_xlabel('x / H')
    ax0.set_ylabel('z / H')
    ax0.set_title('Relative steady-state energy density\n(x-z marginal, averaged over y)')
    plt.colorbar(im, ax=ax0, fraction=0.046, pad=0.04)

    ax1 = fig.add_subplot(gs[0, 1])
    ax1.plot(z_centres, rel_z, 'o-', label='MC energy density')
    ax1.plot(z_centres, pred, '--', label='N(z)^-4 reference')
    ax1.set_xlabel('z / H')
    ax1.set_ylabel('Relative energy density')
    ax1.set_title('Vertical energy-density profile')
    ax1.legend(fontsize=8)

    ax2 = fig.add_subplot(gs[1, 0])
    if checkpoints:
        arr = np.asarray(checkpoints)
        ax2.plot(arr[:, 0], arr[:, 1], label='1) support/common-clock')
        ax2.plot(arr[:, 0], arr[:, 2], label='2) simple local-force sum')
        ax2.plot(arr[:, 0], -(1.0 + arr[:, 3]), label='-(1 + kappa) from 3)')
    ax2.axhline(-1.0, ls='--', lw=1, color='gray')
    ax2.set_xlabel('Collision rounds')
    ax2.set_ylabel('Force ratio')
    ax2.set_title('Convergence of outputs 1, 2, 3')
    ax2.legend(fontsize=8)

    ax3 = fig.add_subplot(gs[1, 1])
    ax3.axis('off')
    text = (
        f"Model:\n"
        f"  eps = {eps:.4f} = aH/c^2\n"
        f"  Lx/H = {ax_ratio:.3f}, Ly/H = {ay_ratio:.3f}\n"
        f"  specularity = {specularity:.2f}\n"
        f"  diffuse power = {power}\n\n"
        f"Outputs:\n"
        f"  1) support/common-clock = {common_ratio:.5f}\n"
        f"  2) simple local-force sum = {local_ratio:.5f}\n"
        f"  3) kappa = {kappa:.5f}\n"
        f"     -(1+kappa) = {predicted_local:.5f}\n\n"
        f"Expected:\n"
        f"  support/common-clock -> -1\n"
        f"  local sum -> -(1+kappa)\n"
    )
    ax3.text(0.02, 0.98, text, va='top', family='monospace')

    fig.tight_layout()
    plot_path = f'{out_prefix}.png'
    fig.savefig(plot_path, dpi=170)
    plt.close(fig)

    return {
        'common_ratio': common_ratio,
        'local_ratio': local_ratio,
        'kappa': kappa,
        'predicted_local': predicted_local,
        'plot_path': plot_path,
        'checkpoints': checkpoints,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=12000)
    ap.add_argument('--rounds', type=int, default=700)
    ap.add_argument('--burn', type=int, default=200)
    ap.add_argument('--eps', type=float, default=0.02)
    ap.add_argument('--ax_ratio', type=float, default=1.0)
    ap.add_argument('--ay_ratio', type=float, default=1.0)
    ap.add_argument('--power', type=int, default=1, choices=[0, 1, 2, 3, 4])
    ap.add_argument('--specularity', type=float, default=0.0)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--out_prefix', type=str,
                default='accelerated_cavity')
    args = ap.parse_args()
    run(**vars(args))
