import pytest


def test_total_keranjang(keranjang):
    assert keranjang.total() == 50_000


def test_tambah_item_baru(keranjang):
    keranjang.tambah("Pena", 5_000, 2)
    assert keranjang.total() == 60_000
    assert keranjang.jumlah_item() == 2


def test_tambah_item_yang_sama_menambah_jumlah(keranjang):
    keranjang.tambah("Buku", 50_000, 2)
    assert keranjang.jumlah_item() == 1
    assert keranjang.total() == 150_000


def test_kosongkan(keranjang):
    keranjang.kosongkan()
    assert keranjang.total() == 0
    assert keranjang.jumlah_item() == 0


@pytest.mark.parametrize("harga, jumlah, pesan", [
    (0, 1, "Harga"),
    (-10, 1, "Harga"),
    (1_000, 0, "Jumlah"),
    (1_000, -1, "Jumlah"),
])
def test_input_tidak_valid_ditolak(keranjang, harga, jumlah, pesan):
    with pytest.raises(ValueError, match=pesan):
        keranjang.tambah("X", harga, jumlah)


@pytest.mark.slow
def test_keranjang_banyak_item(keranjang):
    for i in range(1000):
        keranjang.tambah(f"item{i}", 100)
    assert keranjang.jumlah_item() == 1001
