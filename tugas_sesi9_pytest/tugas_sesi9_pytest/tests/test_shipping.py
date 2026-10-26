import pytest

from src.shipping import hitung_ongkir


@pytest.mark.parametrize("berat, zona, diharapkan", [
    (0.5, "lokal", 10_000),        # dibulatkan jadi 1 kg
    (1, "lokal", 10_000),          # batas 1 kg
    (1.1, "lokal", 13_000),        # dibulatkan jadi 2 kg
    (30, "lokal", 97_000),         # batas atas berat
    (1, "nasional", 20_000),
    (2, "nasional", 28_000),
    (30, "nasional", 252_000),     # batas atas berat
])
def test_ongkir_valid(berat, zona, diharapkan):
    assert hitung_ongkir(berat, zona) == diharapkan


@pytest.mark.parametrize("berat", [0, -1])
def test_berat_nol_atau_negatif_ditolak(berat):
    with pytest.raises(ValueError, match="lebih dari 0"):
        hitung_ongkir(berat, "lokal")


def test_berat_melebihi_batas_ditolak():
    with pytest.raises(ValueError, match="30 kg"):
        hitung_ongkir(30.01, "lokal")


def test_zona_tidak_dikenal_ditolak():
    with pytest.raises(ValueError, match="Zona"):
        hitung_ongkir(1, "luar negeri")
