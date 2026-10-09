
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# Build T_k^Herm for Stage k=4 (N_4 = 210)
primes = [2, 3, 5, 7]
Nk = int(np.prod(primes))
Lk = np.log(Nk)

A_idx, B_idx = np.meshgrid(np.arange(1, Nk + 1), np.arange(1, Nk + 1))
T = np.zeros((Nk, Nk), dtype=np.float64)
for p in primes:
    T += (1.0 / np.sqrt(p)) * np.cos((2.0 * np.pi * A_idx * B_idx * p) / Nk)
mu_a = np.linalg.eigvalsh(T / np.sqrt(Nk))

# Compute Spectrum at epsilon_0 = 0.35
m_max = 50
m_vals = np.arange(-m_max, m_max + 1)
epsilon0 = 0.35

lambda_ma = (2.0 * np.pi * m_vals[:, None] / Lk) + epsilon0 * mu_a[None, :]
spectrum = np.sort(lambda_ma.flatten())

# Unfolded Spacings
spacings = np.diff(spectrum)
s = spacings / np.mean(spacings)

# Render Plot
plt.figure(figsize=(8.5, 5.5))
plt.hist(s, bins=50, density=True, alpha=0.55, color='skyblue', label=f'$D_k$ Spectrum ($k=4, N_4=210$)')

s_grid = np.linspace(0, 3.5, 200)
plt.plot(s_grid, np.exp(-s_grid), 'r--', linewidth=2.0, label='Poisson Uncoupled Baseline ($e^{-s}$)')
plt.plot(s_grid, (32.0 / (np.pi**2)) * (s_grid**2) * np.exp(-(4.0 / np.pi) * (s_grid**2)), 'g-', linewidth=2.0, label='GUE Wigner Surmise')

plt.title("Figure 4: Benchmark Level-Spacing Distribution $P(s)$", fontsize=12, fontweight='bold')
plt.xlabel("Normalized Spacing ($s = \Delta \lambda / \langle \Delta \lambda \\rangle$)", fontsize=11)
plt.ylabel("Probability Density $P(s)$", fontsize=11)
plt.legend(fontsize=10, loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig("figures/fig4_benchmark_comparison.png", dpi=300)
plt.show()

print("Status: Figure 4 saved to 'figures/fig4_benchmark_comparison.png'")
