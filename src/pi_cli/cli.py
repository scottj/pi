from __future__ import annotations

import argparse
import sys
from time import perf_counter

MAX_DECIMAL_DIGITS = 100_000
GUARD_DIGITS = 25


def calculate_pi(decimal_digits: int) -> str:
    if decimal_digits < 0:
        raise ValueError("decimal_digits must be non-negative")

    working_digits = decimal_digits + GUARD_DIGITS
    scale = 10**working_digits

    # Machin-like formula:
    # pi / 4 = 4 * arctan(1 / 5) - arctan(1 / 239)
    pi_scaled = 4 * ((4 * arctan_inverse(5, scale)) - arctan_inverse(239, scale))

    divisor = 10**GUARD_DIGITS
    rounded = (pi_scaled + (divisor // 2)) // divisor
    return format_decimal(rounded, decimal_digits)


def arctan_inverse(inverse_x: int, scale: int) -> int:
    inverse_squared = inverse_x * inverse_x
    term = scale // inverse_x
    total = term
    denominator = 3
    subtract = True

    while term:
        term //= inverse_squared
        if not term:
            break

        current = term // denominator
        if not current:
            break

        total = total - current if subtract else total + current
        denominator += 2
        subtract = not subtract

    return total


def format_decimal(value: int, decimal_digits: int) -> str:
    digits = str(value)

    if decimal_digits == 0:
        return digits

    if len(digits) <= decimal_digits:
        digits = digits.rjust(decimal_digits + 1, "0")

    split_at = len(digits) - decimal_digits
    return f"{digits[:split_at]}.{digits[split_at:]}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Print pi to a requested number of decimal digits."
    )
    parser.add_argument(
        "decimal_digits",
        type=int,
        help="number of digits to print after the decimal point",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if not 0 <= args.decimal_digits <= MAX_DECIMAL_DIGITS:
        print(
            f"Please choose a value between 0 and {MAX_DECIMAL_DIGITS:,}.",
            file=sys.stderr,
        )
        return 1

    started = perf_counter()
    pi_value = calculate_pi(args.decimal_digits)
    elapsed_ms = (perf_counter() - started) * 1000

    print(pi_value)
    print(
        f"Computed {args.decimal_digits:,} decimal digits in {elapsed_ms:,.0f} ms.",
        file=sys.stderr,
    )
    return 0
