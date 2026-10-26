"""Konversi nilai angka ke nilai huruf."""


def grade(nilai):
    """A (>=85), B (70-84), C (55-69), D (40-54), E (<40).

    Nilai di luar 0-100 melempar ValueError.
    """
    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus 0-100")
    if nilai >= 85:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 55:
        return "C"
    if nilai >= 40:
        return "D"
    return "E"
