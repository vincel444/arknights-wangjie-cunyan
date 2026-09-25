@echo off
rem Run Ren'Py lint to validate scripts and assets.
setlocal
if "%RENPY_SDK%"=="" set RENPY_SDK=F:\bian\renpy\renpy-8.5.3-sdk
"%RENPY_SDK%\lib\py3-windows-x86_64\renpy.exe" "%~dp0" lint
type "%~dp0lint.txt"
pause
