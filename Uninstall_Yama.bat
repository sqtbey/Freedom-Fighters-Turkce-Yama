@echo off
chcp 65001 >nul
title Freedom Fighters Türkçe Yama Kaldırıcı - sqtbey
echo ============================================================
echo   Freedom Fighters Türkçe Yama Kaldırıcı v1.0
echo   Geliştirici: sqtbey
echo ============================================================
echo.
echo Orijinal dosyalar geri yükleniyor...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [HATA] Sisteminizde Python bulunamadı!
    pause
    exit /b 1
)

python "%~dp0patch_game.py" --uninstall
echo.
pause
