# Pi calculator

A single-file browser app that calculates pi to a requested number of decimal digits.

## Live version

Hosted on GitHub Pages. Open the URL in any browser — no install needed.

## Algorithms

Five algorithms are available, selectable in the UI:

| Algorithm | Max digits | Notes |
|---|---|---|
| **Machin** | 100,000 | Fast-converging identity using two arctangent terms |
| **Chudnovsky** | 100,000 | ~14.18 correct digits per term via binary splitting; the standard choice for large counts |
| **Nilakantha** | 20 | Simple alternating series; O(1/N³) convergence |
| **Leibniz** | 10 | Demo only — O(1/N) convergence, extremely slow |
| **Monte Carlo** | 5 | Probabilistic estimate; result varies each run |

Machin and Chudnovsky use fixed-point arithmetic with `BigInt`. The calculation runs in a Web Worker so the UI stays responsive for large digit counts.
