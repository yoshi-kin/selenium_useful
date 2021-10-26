@echo off
setlocal
cd %~dp0

@REM chromeバージョンフォルダ名をテキストファイルに出力
dir /B /O-N "%LocalAppData%\Google\Chrome\Application" | findstr "^[0-9]." > "chrome_version.txt"
@REM chromeバージョンのhead部分をテキストファイルに出力
for /f "tokens=1 delims=:." %%a in (chrome_version.txt) do echo %%a> chrome_version_h.txt
@REM テキストファイルからchromeバージョンのheadを変数に入れる
set /p version_head= 0<"chrome_version_h.txt"
del chrome_version.txt
del chrome_version_h.txt
pip install chromedriver-binary=="%version_head%.*"

