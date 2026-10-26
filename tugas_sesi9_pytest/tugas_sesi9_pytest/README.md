# Tugas Sesi 9 - Unit Test PyTest dengan Fixture dan Parametrize
Mata Kuliah Software Testing

## Struktur
```
src/                  kode yang diuji (6 modul: discount, grade, shipping, keranjang, app, email_service)
tests/                kode test PyTest (conftest.py berisi fixture bersama)
laporan/              output pytest -v dan coverage + LAPORAN.md
htmlcov/              laporan coverage HTML (buka htmlcov/index.html)
pytest.ini, .coveragerc
```

## Cara menjalankan
```bash
python -m venv venv
# Windows: venv\Scripts\activate    |  Mac/Linux: source venv/bin/activate
pip install -r requirements.txt

pytest -v                                   # jalankan semua test
pytest -m "not slow"                        # lewati test bermarker slow
pytest --cov=src --cov-branch --cov-report=term-missing --cov-report=html
```
