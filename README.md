# Pi CLI

A small `uv` package that prints pi to a requested number of decimal digits.

## Usage

```powershell
uv run pi 25
uv run pi 250
```

The argument is the number of digits after the decimal point.

You can also run the module form directly:

```powershell
uv run python -m pi_cli 25
```

## Standalone page

There is also a single-file browser version in `pi.html`.
Open it directly in a browser to calculate pi with the same Machin-style approach used by the Python CLI.

## Algorithm options

Common ways to calculate or approximate pi include:

- `Leibniz series`: very easy to understand, very slow to converge.
- `Nilakantha series`: still simple, noticeably better than Leibniz.
- `Machin-like formulas`: compact and accurate for a small CLI.
- `Chudnovsky`: best choice when you want very large digit counts.
- `Monte Carlo`: fun for simulation demos, not for exact decimal output.

This script uses a Machin-like formula with fixed-point integer arithmetic:

```text
pi / 4 = 4 * arctan(1 / 5) - arctan(1 / 239)
```

That keeps the code short and easy to tweak while still producing accurate decimal output.

## Project layout

- `pyproject.toml`: package metadata and the `pi` console script entry point
- `src/pi_cli/cli.py`: the command-line interface and pi calculation logic
- `src/pi_cli/__main__.py`: supports `python -m pi_cli`
