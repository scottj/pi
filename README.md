# Pi calculator

A single-file browser app that calculates pi to a requested number of decimal digits.

## Live version

Hosted on GitHub Pages. Open the URL in any browser — no install needed.

## Algorithm

Uses a Machin-like formula with fixed-point integer arithmetic and `BigInt`:

```text
pi / 4 = 4 * arctan(1 / 5) - arctan(1 / 239)
```

The calculation runs in a Web Worker so the UI stays responsive for large digit counts.

## Other approaches

- **Leibniz series**: easy to understand, very slow to converge.
- **Nilakantha series**: still simple, noticeably better than Leibniz.
- **Chudnovsky**: best choice for very large digit counts.
- **Monte Carlo**: useful for simulation demos, not exact decimal output.
