import pytest

from src.discount import apply_discount


def test_diskon_di_batas_atas():
    assert apply_discount(500_000) == pytest.approx(450_000)


def test_tanpa_diskon_di_bawah_batas():
    assert apply_discount(499_999) == 499_999


def test_float_dengan_toleransi():
    assert apply_discount(500_001) == pytest.approx(450_000.9)


# Parametrize berdasar BVA (batas 500.000 dan batas 0)
@pytest.mark.parametrize("total, diharapkan", [
    (0, 0),                    # batas bawah valid
    (1, 1),                    # tepat di atas batas bawah
    (499_999, 499_999),        # tepat di bawah batas diskon
    (500_000, 450_000),        # tepat di batas diskon
    (500_001, 450_000.9),      # tepat di atas batas diskon
    (1_000_000, 900_000),      # nilai besar
])
def test_hitung_diskon_bva(total, diharapkan):
    assert apply_discount(total) == pytest.approx(diharapkan)


def test_total_negatif_ditolak():
    with pytest.raises(ValueError, match="Total negatif"):
        apply_discount(-1)
