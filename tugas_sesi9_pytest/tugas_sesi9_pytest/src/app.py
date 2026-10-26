"""Proses pesanan yang memakai layanan email eksternal."""
from src.email_service import kirim_email  # dependensi eksternal


def proses_pesanan(id, email):
    if id <= 0:
        raise ValueError("ID tidak valid")
    ok = kirim_email(email, f"Pesanan {id} diterima")
    return "selesai" if ok else "email gagal"
