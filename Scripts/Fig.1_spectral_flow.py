import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# 1. Primorial Matrix Construction (Stage k=3, N_3 = 30)
primes = [2, 3, 5]
Nk = int(np.prod(primes))
Lk = np.log(Nk)

A_idx, B_idx = np.meshgrid(np.arange(1, Nk + 1), np.arange(1, Nk + 1))
T = np.zeros((Nk, Nk), dtype=np.float64)
for p in primes:
    T += (1.0 / np.sqrt(p)) * np.cos((2.0 * np.pi * A_idx * B_idx * p) / Nk)
T_herm = T / np.sqrt(Nk)

# Compute real symmetric eigenvalues mu_a
mu_a = np.linalg.eigvalsh(T_herm)

# 2. Sweep Coupling Parameter epsilon_0
epsilon_vals = np.linspace(0.0, 1.0, 200)
m_modes = np.arange(-3, 4)  # Momentum modes m in [-3, 3]

plt.figure(figsize=(9, 5.5))

# Plot level flow for each (m, a) combination
for m in m_modes:
    unperturbed = (2.0 * np.pi * m) / Lk
    for a_idx in range(Nk):
        eigenvalues = unperturbed + epsilon_vals * mu_a[a_idx]
        plt.plot(epsilon_vals, eigenvalues, color='navy', alpha=0.15, linewidth=0.8)

plt.title(f"Figure 1: Spectral Level Flow vs Coupling ($\epsilon_0$) [Stage $k=3$, $N_3=30$]", fontsize=12, fontweight='bold')
plt.xlabel("Coupling Parameter ($\epsilon_0$)", fontsize=11)
plt.ylabel("Eigenvalue Spectrum ($\lambda_{m,a}$)", fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig("figures/fig1_spectral_flow.png", dpi=300)
plt.show()

print("Status: Figure 1 saved to 'figures/fig1_spectral_flow.png'")
