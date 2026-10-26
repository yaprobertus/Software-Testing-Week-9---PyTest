import pytest

from src.grade import grade


# BVA pada setiap batas, termasuk 0, 100, -1, dan 101 (latihan kelas)
@pytest.mark.parametrize("nilai, huruf", [
    (0, "E"),      # batas bawah valid
    (39, "E"),     # tepat di bawah batas D
    (40, "D"),     # batas bawah D
    (54, "D"),     # batas atas D
    (55, "C"),     # batas bawah C
    (69, "C"),     # batas atas C
    (70, "B"),     # batas bawah B
    (84, "B"),     # batas atas B
    (85, "A"),     # batas bawah A
    (100, "A"),    # batas atas valid
])
def test_grade_bva(nilai, huruf):
    assert grade(nilai) == huruf


@pytest.mark.parametrize("nilai", [-1, 101])
def test_grade_di_luar_rentang_ditolak(nilai):
    with pytest.raises(ValueError, match="Nilai harus 0-100"):
        grade(nilai)
