# Spectral Theory of the Primorial-Modulated Dilation Operator on Continuous-Discrete Fiber Spaces

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22899831.svg)](https://doi.org/10.5281/zenodo.22899831)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview & Scope
This repository houses the mathematical framework, operator definitions, and numerical simulation suite for the primorial-modulated dilation operator $D_k$. The framework explicitly couples a scale-invariant continuous dilation momentum operator to a Hermitian arithmetic phase matrix $T_k^(Herm)$ derived from divisor sums over prime factors of the primorial $N_k$ = p_k#.

---

## Nomenclature & Glossary

| Symbol / Term | Definition |
| :--- | :--- |
| **$H_k$** | Hybrid continuous-discrete Hilbert space defined as $H_k = L^2(T_{L_k})$ tensor $C^{N_k}$. |
| **$L_k = ln N_k$** | Characteristic base torus perimeter parameter indexed by the $k-th$ primorial $N_k$ = p_k#. |
| **$T_k^(Herm)$** | Real-symmetric symmetrized arithmetic phase matrix constructed via $T_k^(Herm) = 1/2(T_k + T_k^*)$. |
| **$D_k$** | Primorial-modulated dilation operator defined by $D_k = D_{0,k}$ tensor $I + epsilon_0$ I tensor $T_k^(Herm)$. |
| **$H_infinity$** | Inductive limit Hilbert space defined as the direct limit completion $H_infinity = colim (H_k, V_k)$. |

---

## Theorem & Spectral Summary

* **Theorem 1 (Exact Spectral Decomposition):** Tensor-factor commutativity $[D_{0,k} tensor I, I tensor T_k^(Herm)] = 0$ yields the exact closed-form spectrum $lambda_{m,a}(epsilon_0) = (2 pi m / ln N_k) + epsilon_0 mu_a(T_k^(Herm))$.
* **Theorem 2 (Self-Adjointness & Compact Resolvent):** Via Kato-Rellich perturbation theory, $D_k$ is densely defined and self-adjoint, possessing a point-discrete spectrum with a Hilbert-Schmidt class resolvent $R_z(D_k)$ in $S_2(H_k)$ for all $z$ not in $R$.
* **Theorem 3 (Dual Trace Formula):** Poisson summation converts the distribution trace into a sum over periodic orbits on the base torus $T_{L_k}$ weighted by prime divisor matrix traces.
* **Theorem 4 (Inductive Limit Convergence):** Interstage isometric embeddings $V_k = V_base$ tensor $V_fiber$ construct the direct limit space $H_infinity$, ensuring strong convergence of $D_k$ on dense domains.

---

## Conjectures & Open Hypotheses

* **Conjecture 8.1 (The Primorial Limit Conjecture):** 
  * *Premise:* Unperturbed spectra exhibit rigid Poisson lattice statistics, whereas finite-stage arithmetic phase sums break degeneracy.
  * *Hypothesis:* As #k -> infinity and $epsilon_0 -> epsilon_c$, the local level-spacing correlation functions of $D_k$ exhibit Gaussian Unitary Ensemble (GUE) statistics, characterizing arithmetic quantum chaos.

---

## Repository Directory & Simulation Suite

Run the provided Python script to execute numerical diagonalizations and generate level-spacing statistics:

* `sim_dilation_spectrum.py` — Builds the symmetrized arithmetic matrix $T_k^(Herm)$, computes exact eigenvalues across momentum modes, unfolds level spacings, and compares results against Poisson and GUE Wigner distributions.

---

## Citation

If you utilize this operator framework or numerical simulation suite in your research, please cite the corresponding Zenodo record:

```bibtex
@article{Gray2026DilationOperator,
  title={Spectral Theory of the Primorial-Modulated Dilation Operator on Continuous-Discrete Fiber Spaces},
  author={Gray, Benjamin Edward},
  journal={Zenodo},
  year={2026},
  doi={10.5281/zenodo.22899831}
}
