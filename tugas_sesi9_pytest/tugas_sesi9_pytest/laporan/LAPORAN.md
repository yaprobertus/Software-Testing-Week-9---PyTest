# Laporan Tugas Sesi 9 - Unit Test PyTest
Nama / NIM : ........................
Mata Kuliah: Software Testing

## 1. Ringkasan
Modul yang diuji ada di folder `src/`. Seluruh test ada di `tests/`.
Hasil: **48 test, semua PASSED**. Coverage total **99%** (statement dan branch).

## 2. Pemetaan terhadap syarat tugas
| No | Syarat | Pemenuhan | Lokasi |
|----|--------|-----------|--------|
| 1 | Modul Python minimal 3 fungsi berlogika bersyarat | `apply_discount`, `grade`, `hitung_ongkir` (+ `Keranjang.tambah`, `proses_pesanan`) | `src/` |
| 2 | Minimal 8 test | 48 test case (22 fungsi test, sebagian diparametrize) | `tests/` |
| 3 | Minimal 1 parametrize berdasar BVA | `test_hitung_diskon_bva` (0, 1, 499.999, 500.000, 500.001, 1.000.000), `test_grade_bva` (0, 39, 40, 54, 55, 69, 70, 84, 85, 100), `test_ongkir_valid` | `tests/test_discount.py`, `test_grade.py`, `test_shipping.py` |
| 4 | Minimal 2 test `pytest.raises` | `test_total_negatif_ditolak`, `test_grade_di_luar_rentang_ditolak` (-1, 101), `test_berat_*_ditolak`, `test_zona_tidak_dikenal_ditolak`, `test_input_tidak_valid_ditolak`, `test_id_tidak_valid_tidak_mengirim_email` | semua file test |
| 5 | Minimal 1 fixture dengan cleanup `yield` | fixture `keranjang` (cleanup `k.kosongkan()` setelah yield) | `tests/conftest.py` |
| 6 | Minimal 1 penggunaan mock | `patch("src.app.kirim_email", ...)` dengan return_value, side_effect, `assert_called_once_with`, `assert_not_called`; plus `monkeypatch` | `tests/test_app.py` |
| 7 | Laporan `pytest --cov --cov-branch` + analisis cabang belum tercakup | bagian 3 dan 4 di bawah | `laporan/`, `htmlcov/` |

## 3. Hasil coverage
Perintah: `pytest --cov=src --cov-branch --cov-report=term-missing --cov-report=html`

```
Name                   Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------
src/app.py                 6      0      2      0   100%
src/discount.py            6      0      4      0   100%
src/email_service.py       2      1      0      0    50%   6
src/grade.py              12      0     10      0   100%
src/keranjang.py          18      0      6      0   100%
src/shipping.py           14      0      8      0   100%
------------------------------------------------------------------
TOTAL                     58      1     30      0    99%
```

## 4. Analisis cabang / baris yang belum tercakup
- **Cabang (branch)**: kolom `BrPart` bernilai 0 di semua modul, artinya semua cabang `if` (True dan False) sudah teruji, termasuk cabang False pada kondisi tanpa `else` seperti `if nama in self._item` di `Keranjang.tambah` (diuji lewat item baru dan item yang sama).
- **Baris 6 `src/email_service.py` (belum tercakup)**: isi fungsi `kirim_email`, yaitu layanan email eksternal. Ini disengaja: pada unit test fungsi ini selalu di-mock agar tidak mengirim email sungguhan (isolasi, cepat, repeatable). Perilaku aslinya sebaiknya diverifikasi lewat integration test / contract test, bukan unit test.
- **Keterbatasan**: coverage 99% tidak berarti bebas bug. Coverage hanya mengukur kode yang dijalankan, sehingga kualitas assertion tetap kunci. Karena itu setiap test memeriksa hasil (assert) atau exception, bukan sekadar memanggil fungsi.
- Target wajar 70-85% dengan branch coverage pada logika bisnis penting; angka di atas melampaui target tersebut.

## 5. Screenshot
(Tempel screenshot di sini: lihat daftar pada README / penjelasan dosen.)
