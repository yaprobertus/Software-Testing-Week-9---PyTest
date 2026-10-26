"""Perhitungan ongkos kirim."""
import math

BERAT_MAKS_KG = 30
ZONA_VALID = ("lokal", "nasional")


def hitung_ongkir(berat_kg, zona):
    """Hitung ongkir berdasarkan berat (kg) dan zona.

    - lokal    : Rp10.000 untuk 1 kg pertama, +Rp3.000 tiap kg berikutnya
    - nasional : Rp20.000 untuk 1 kg pertama, +Rp8.000 tiap kg berikutnya
    Berat dibulatkan ke atas. Berat <= 0 atau > 30 kg dan zona tak dikenal -> ValueError.
    """
    if berat_kg <= 0:
        raise ValueError("Berat harus lebih dari 0")
    if berat_kg > BERAT_MAKS_KG:
        raise ValueError("Berat melebihi batas 30 kg")
    if zona not in ZONA_VALID:
        raise ValueError("Zona tidak dikenal")

    kg = math.ceil(berat_kg)
    if zona == "lokal":
        return 10_000 + (kg - 1) * 3_000
    return 20_000 + (kg - 1) * 8_000
