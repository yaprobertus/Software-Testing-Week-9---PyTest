"""Layanan email EKSTERNAL (dependensi yang akan di-mock pada unit test)."""


def kirim_email(tujuan, pesan):
    """Di dunia nyata memanggil SMTP/API email. Tidak dijalankan saat unit test."""
    raise ConnectionError("Layanan email asli tidak boleh dipanggil saat unit test")
