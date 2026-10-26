"""Fungsi diskon belanja."""


def apply_discount(total):
    """Beri diskon 10% bila total >= 500.000. Total negatif ditolak."""
    if total < 0:
        raise ValueError("Total negatif")
    if total >= 500_000:
        return total * 0.90  # diskon 10%
    return total
