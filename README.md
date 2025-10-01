# FARSEC — Phone Number Geolocation Tool

🔍 FARSEC adalah tool Python untuk melacak lokasi nomor telepon, menampilkan operator, domisili, serta membuat map HTML otomatis.  
Terinspirasi dari Sherlock Holmes, dan menggunakan OpenCage Geocoder API.

---

## Fitur

- Mendapatkan informasi nomor telepon:
  - Nomor internasional terformat
  - Operator / provider
  - Domisili (kota + negara)
  - Latitude & Longitude
- Membuat **map HTML** interaktif dengan marker lokasi
- Banner pixel art keren di terminal
- API Key fleksibel:
  - Bisa langsung input saat run
  - Bisa juga pakai environment variable `OPENCAGE_API_KEY`
- Bisa jalan di **VS Code** maupun **terminal** (Linux / macOS / Windows)

---

## Cara Install

@echo off
REM FARSEC Runner for Windows

REM Cek Python
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ❌ Python tidak ditemukan. Install Python dulu.
    pause
    exit /b
)

REM Install dependencies
pip install -r requirements.txt

REM Jalankan FARSEC
python farsec.py
pause



