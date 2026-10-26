"""Fixture bersama: otomatis tersedia untuk semua file test di folder ini."""
import pytest

from src.keranjang import Keranjang


@pytest.fixture
def keranjang():
    k = Keranjang()              # Arrange
    k.tambah("Buku", 50_000)
    yield k                      # diberikan ke test
    k.kosongkan()                # cleanup setelah test selesai
