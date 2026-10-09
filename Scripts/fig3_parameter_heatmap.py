
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# Build T_k^Herm for Stage k=3 (N_3 = 30)
primes = [2, 3, 5]
Nk = int(np.prod(primes))
Lk = np.log(Nk)

A_idx, B_idx = np.meshgrid(np.arange(1, Nk + 1), np.arange(1, Nk + 1))
T = np.zeros((Nk, Nk), dtype=np.float64)
for p in primes:
    T += (1.0 / np.sqrt(p)) * np.cos((2.0 * np.pi * A_idx * B_idx * p) / Nk)
mu_a = np.linalg.eigvalsh(T / np.sqrt(Nk))

# 2D Parameter Sweep Setup
grid_res = 40
epsilons = np.linspace(0.01, 1.0, grid_res)
m_max_vals = np.linspace(10, 80, grid_res, dtype=int)

r_matrix = np.zeros((grid_res, grid_res))

for i, m_max in enumerate(m_max_vals):
    m_vals = np.arange(-m_max, m_max + 1)
    for j, eps in enumerate(epsilons):
        # Compute joint spectrum
        lambda_ma = (2.0 * np.pi * m_vals[:, None] / Lk) + eps * mu_a[None, :]
        spec = np.sort(lambda_ma.flatten())

        # Calculate level spacing ratios r_i
        spacings = np.diff(spec)
        s_i = spacings[:-1]
        s_next = spacings[1:]

        r_i = np.minimum(s_i, s_next) / (np.maximum(s_i, s_next) + 1e-12)
        r_matrix[i, j] = np.mean(r_i)

plt.figure(figsize=(8, 6.5))
im = plt.imshow(
    r_matrix,
    extent=[epsilons[0], epsilons[-1], m_max_vals[0], m_max_vals[-1]],
    origin='lower',
    aspect='auto',
    cmap='viridis'
)

cbar = plt.colorbar(im)
cbar.set_label('Mean Level Spacing Ratio $\langle r \\rangle$', fontsize=11)

plt.title("Figure 3: Quantum Chaos Transition Heatmap ($\langle r \\rangle$ Metric)", fontsize=12, fontweight='bold')
plt.xlabel("Coupling Parameter ($\epsilon_0$)", fontsize=11)
plt.ylabel("Mode Truncation Limit ($m_{\mathrm{max}}$)", fontsize=11)
plt.tight_layout()

plt.savefig("figures/fig3_parameter_heatmap.png", dpi=300)
plt.show()

print("Status: Figure 3 saved to 'figures/fig3_parameter_heatmap.png'")
