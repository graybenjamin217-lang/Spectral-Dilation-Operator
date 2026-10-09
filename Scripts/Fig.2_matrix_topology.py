import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# Build Symmetrized Arithmetic Matrix T_k^Herm (Stage k=3, N_3 = 30)
primes = [2, 3, 5]
Nk = int(np.prod(primes))

A_idx, B_idx = np.meshgrid(np.arange(1, Nk + 1), np.arange(1, Nk + 1))
T = np.zeros((Nk, Nk), dtype=np.float64)
for p in primes:
    T += (1.0 / np.sqrt(p)) * np.cos((2.0 * np.pi * A_idx * B_idx * p) / Nk)
T_herm = T / np.sqrt(Nk)

plt.figure(figsize=(7.5, 6.5))
im = plt.imshow(T_herm, cmap='magma', origin='lower', aspect='equal')

cbar = plt.colorbar(im)
cbar.set_label('Matrix Element $[T_k^{\mathrm{Herm}}]_{a,b}$', fontsize=11)

plt.title(f"Figure 2: Arithmetic Phase Matrix Topology ($T_3^{{\mathrm{{Herm}}}}$ on $\mathbb{{Z}}_{{30}}$)", fontsize=12, fontweight='bold')
plt.xlabel("Fiber Index $b \in \{1, \dots, N_k\}$", fontsize=11)
plt.ylabel("Fiber Index $a \in \{1, \dots, N_k\}$", fontsize=11)
plt.tight_layout()

plt.savefig("figures/fig2_matrix_topology.png", dpi=300)
plt.show()

print("Status: Figure 2 saved to 'figures/fig2_matrix_topology.png'")
