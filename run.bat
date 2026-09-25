@echo off
rem Launch the game. Set RENPY_SDK to your Ren'Py SDK path if different.
setlocal
if "%RENPY_SDK%"=="" set RENPY_SDK=F:\bian\renpy\renpy-8.5.3-sdk
"%RENPY_SDK%\lib\py3-windows-x86_64\renpy.exe" "%~dp0" %*
