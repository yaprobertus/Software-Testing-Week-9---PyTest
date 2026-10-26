"""Mocking: layanan email eksternal diganti objek pengganti."""
from unittest.mock import patch

import pytest

from src.app import proses_pesanan


def test_pesanan_sukses_dan_email_terkirim():
    # patch ke tempat nama DIPAKAI ("src.app.kirim_email"), bukan tempat didefinisikan
    with patch("src.app.kirim_email", return_value=True) as palsu:   # stub + mock
        assert proses_pesanan(1, "a@b.id") == "selesai"
        palsu.assert_called_once_with("a@b.id", "Pesanan 1 diterima")


def test_email_gagal_ditangani():
    with patch("src.app.kirim_email", return_value=False):
        assert proses_pesanan(1, "a@b.id") == "email gagal"


def test_layanan_email_timeout():
    with patch("src.app.kirim_email", side_effect=TimeoutError):     # simulasi error
        with pytest.raises(TimeoutError):
            proses_pesanan(1, "a@b.id")


@pytest.mark.parametrize("id", [0, -5])
def test_id_tidak_valid_tidak_mengirim_email(id):
    with patch("src.app.kirim_email") as palsu:
        with pytest.raises(ValueError, match="ID tidak valid"):
            proses_pesanan(id, "a@b.id")
        palsu.assert_not_called()                                    # verifikasi interaksi


def test_dengan_monkeypatch(monkeypatch):
    monkeypatch.setattr("src.app.kirim_email", lambda to, msg: True)
    assert proses_pesanan(1, "a@b.id") == "selesai"
