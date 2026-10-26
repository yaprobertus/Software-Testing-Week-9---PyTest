"""Keranjang belanja sederhana (dipakai untuk demo fixture)."""


class Keranjang:
    def __init__(self):
        self._item = {}

    def tambah(self, nama, harga, jumlah=1):
        if harga <= 0:
            raise ValueError("Harga harus positif")
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif")
        if nama in self._item:
            harga_lama, jumlah_lama = self._item[nama]
            self._item[nama] = (harga_lama, jumlah_lama + jumlah)
        else:
            self._item[nama] = (harga, jumlah)

    def total(self):
        return sum(h * j for h, j in self._item.values())

    def jumlah_item(self):
        return len(self._item)

    def kosongkan(self):
        self._item.clear()
