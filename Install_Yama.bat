@echo off
chcp 65001 >nul
title Freedom Fighters Türkçe Yama Yükleyici - sqtbey
echo ============================================================
echo   Freedom Fighters Türkçe Yama v1.0
echo   Geliştirici: sqtbey
echo ============================================================
echo.
echo Yama dosyaları kontrol ediliyor...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [HATA] Sisteminizde Python bulunamadı!
    echo Lütfen https://www.python.org adresinden Python'ı kurun ve tekrar deneyin.
    echo Kurulum sırasında 'Add Python to PATH' kutucuğunu işaretlemeyi unutmayın.
    pause
    exit /b 1
)

python "%~dp0patch_game.py"
echo.
pause
