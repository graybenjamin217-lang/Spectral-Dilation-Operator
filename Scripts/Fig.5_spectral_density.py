import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# Build Stage k=3 Spectrum
primes = [2, 3, 5]
Nk = int(np.prod(primes))
Lk = np.log(Nk)

A_idx, B_idx = np.meshgrid(np.arange(1, Nk + 1), np.arange(1, Nk + 1))
T = np.zeros((Nk, Nk), dtype=np.float64)
for p in primes:
    T += (1.0 / np.sqrt(p)) * np.cos((2.0 * np.pi * A_idx * B_idx * p) / Nk)
mu_a = np.linalg.eigvalsh(T / np.sqrt(Nk))

m_max = 100
m_vals = np.arange(-m_max, m_max + 1)
epsilon0 = 0.35

lambda_ma = (2.0 * np.pi * m_vals[:, None] / Lk) + epsilon0 * mu_a[None, :]
spectrum = np.sort(lambda_ma.flatten())

# Compute Integrated Density Residual vs Ideal Lebesgue Limit (1 / 2\pi)
energy_bounds = np.linspace(5.0, 50.0, 100)
density_errors = []

for Lambda in energy_bounds:
    # Count modes inside window I = [-Lambda, Lambda]
    modes_in_window = np.sum((spectrum >= -Lambda) & (spectrum <= Lambda))
    empirical_density = modes_in_window / (Nk * Lk * (2.0 * Lambda))
    
    # Ideal uniform measure limit = 1 / (2 * pi)
    ideal_density = 1.0 / (2.0 * np.pi)
    density_errors.append(np.abs(empirical_density - ideal_density))

plt.figure(figsize=(8.5, 5.5))
plt.semilogy(energy_bounds, density_errors, 'b-o', markersize=4, label=r'Density Error $\left|\rho_k(I) - \frac{1}{2\pi}\right|$')

plt.title("Figure 5: Spectral Density Weak Convergence Residual", fontsize=12, fontweight='bold')
plt.xlabel("Energy Window Radius ($\Lambda$)", fontsize=11)
plt.ylabel("Absolute Density Error (Log Scale)", fontsize=11)
plt.grid(True, which="both", linestyle=':', alpha=0.6)
plt.legend(fontsize=10, loc='upper right')
plt.tight_layout()

plt.savefig("figures/fig5_convergence_error.png", dpi=300)
plt.show()

print("Status: Figure 5 saved to 'figures/fig5_convergence_error.png'")
