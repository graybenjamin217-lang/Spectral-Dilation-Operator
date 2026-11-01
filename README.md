# Spectral Theory of the Primorial-Modulated Dilation Operator on Continuous-Discrete Fiber Spaces

[[https://zenodo.org/badge/DOI/10.5281/zenodo.23862749.svg]](https://doi.org/10.5281/zenodo.23862749)
[[https://img.shields.io/badge/License-MIT-yellow.svg]](https://opensource.org/licenses/MIT)

## Overview & Scope

This repository houses the mathematical framework, operator definitions, and numerical simulation suite for the primorial-modulated dilation operator $D_k$. The framework explicitly couples a scale-invariant continuous dilation momentum operator $D_{0,k} = -i\frac{d}{dy}$ on a 1D torus $\mathbb{T}_{L_k}$ to a Hermitian arithmetic phase matrix $T_k^{\mathrm{Herm}}$ derived from prime divisor sums over residue rings $\mathbb{Z}_{N_k}$, where $N_k = p_k$# is the $k$-th primorial and $L_k = \ln N_k$.

---

## Nomenclature & Glossary

| Symbol / Term | Definition |
| :--- | :--- |
| $\mathcal{H}_k$ | Hybrid continuous-discrete Hilbert space defined as $\mathcal{H}_k = L^2(\mathbb{T}_{L_k}) \otimes \mathbb{C}^{N_k}$. |
| $L_k = \ln N_k$ | Characteristic base torus perimeter parameter indexed by the $k$-th primorial $N_k = p_k$# = $\prod_{j=1}^k p_j$. |
| $T_k^{\mathrm{Herm}}$ | Real symmetric arithmetic phase matrix: $[T_k^{\mathrm{Herm}}]_{a,b} = \frac{1}{\sqrt{N_k}} \sum_{p \mid N_k} \frac{1}{\sqrt{p}} \cos\!\left(\frac{2\pi a b p}{N_k}\right)$ for $a,b \in \{0, \dots, N_k-1\}$. |
| $D_k$ | Primorial-modulated dilation operator defined on $\operatorname{Dom}(D_k) = H^1(\mathbb{T}_{L_k}) \otimes \mathbb{C}^{N_k}$ by $D_k = D_{0,k} \otimes I_{\mathbb{C}^{N_k}} + \varepsilon_0 I_{L^2} \otimes T_k^{\mathrm{Herm}}$. |
| $\mathcal{H}_\infty$ | Inductive limit Hilbert space defined as the direct limit completion $\mathcal{H}_\infty = \varinjlim(\mathcal{H}_k, V_k)$. |

---

## Theorem & Spectral Summary

* **Theorem 1 (Exact Spectral Decomposition):** Tensor-factor commutativity $[D_{0,k} \otimes I, I \otimes T_k^{\mathrm{Herm}}] = 0$ yields the exact closed-form point spectrum:
  $$\lambda_{m,a}(\varepsilon_0) = \frac{2\pi m}{\ln N_k} + \varepsilon_0 \mu_a(T_k^{\mathrm{Herm}}), \quad m \in \mathbb{Z}, \;\; a \in \{1, \dots, N_k\}$$
  The discrete eigenvalues $\mu_a(T_k^{\mathrm{Herm}})$ act as uniform shifts breaking the unperturbed continuous momentum degeneracies.

* **Theorem 2 (Self-Adjointness & Compact Resolvent):** Via Kato–Rellich perturbation theory, $D_k$ is self-adjoint on $H^1(\mathbb{T}_{L_k}) \otimes \mathbb{C}^{N_k}$. For any $z \in \mathbb{C} \setminus \mathbb{R}$, the resolvent $R_z(D_k) = (D_k - zI)^{-1}$ belongs to the Hilbert–Schmidt class $\mathcal{S}_2(\mathcal{H}_k)$ and is compact, establishing a purely point-discrete spectrum.

* **Theorem 3 (Dual Distributional Trace Formula):** Applying Poisson summation converts the continuous momentum sum into periodic orbital returns $t = n \ln N_k$ on the base torus $\mathbb{T}_{L_k}$:
  $$\operatorname{Tr}\!\left(e^{-itD_k}\right) = \ln N_k \cdot \operatorname{Tr}_{\mathbb{C}^{N_k}}\!\left(e^{-it\varepsilon_0 T_k^{\mathrm{Herm}}}\right) \sum_{n=-\infty}^\infty \delta(t - n \ln N_k)$$
  which isolates prime divisor moments at each orbital return time.

* **Theorem 4 (Inductive Limit State Space):** Interstage isometric embeddings $V_k = V_{\mathrm{base}} \otimes V_{\mathrm{fiber}}: \mathcal{H}_k \hookrightarrow \mathcal{H}_{k+1}$ preserve inner products mode-wise, defining the direct limit Hilbert space $\mathcal{H}_\infty = \varinjlim(\mathcal{H}_k, V_k)$.

---

## Conjectures & Open Hypotheses

* **Conjecture 7.1 (The Primorial Limit Conjecture):**
  * *Premise:* At finite stages, unperturbed spectra exhibit rigid 1D Poisson lattice statistics, while the arithmetic phase shifts $\mu_a(T_k^{\mathrm{Herm}})$ introduce internal level repulsion.
  * *Hypothesis:* As $k \to \infty$, after quotienting out the reflection-symmetry kernel $\ker(T_k^{\mathrm{Herm}})$, the unfolded local level-spacing statistics of $D_k$ transition toward Wigner–Dyson random matrix statistics: specifically the **Gaussian Orthogonal Ensemble (GOE)** for the real symmetric operator $T_k^{\mathrm{Herm}}$, and the **Gaussian Unitary Ensemble (GUE)** under time-reversal-breaking phase modulations and non-commuting spatial coupling.

---

## Repository Directory & Simulation Suite

Run the scripts in the `simulations/` directory to execute numerical validations:

* `sim1_matrix_radius.py` — Computes the symmetrized arithmetic matrix $T_k^{\mathrm{Herm}}$ and evaluates exact spectral radii $\|T_k^{\mathrm{Herm}}\|_2$ and matrix ranks across primorial stages $k = 1$ to $5$.
* `sim2_exact_spectrum.py` — Generates the hybrid continuous-discrete spectrum $\lambda_{m,a}(\varepsilon_0)$ across coupled momentum and arithmetic modes.
* `sim3_trace_formula.py` — Numerically verifies the dual trace formula and orbital return distributions via Poisson summation mappings.
* `sim4_inductive_limit.py` — Evaluates interstage isometric embeddings $V_k = V_{\mathrm{base}} \otimes V_{\mathrm{fiber}}$ and tracks norm preservation across expanding base tori.
* `sim5_level_spacings.py` — Unfolds nearest-neighbor level spacings and compares desymmetrized local statistics against Poisson, GOE, and GUE distributions.

---

## Citation

If you utilize this operator framework or numerical simulation suite in your research, please cite the corresponding Zenodo record:

```bibtex
@article{Gray2026DilationOperator,
  title   = {Spectral Theory of the Primorial-Modulated Dilation Operator on Continuous-Discrete Fiber Spaces},
  author  = {Gray, Benjamin Edward},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.23862749},
  url     = {[https://doi.org/10.5281/zenodo.23862749](https://doi.org/10.5281/zenodo.23862749)}
}
