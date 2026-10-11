@echo off
setlocal EnableExtensions
rem Lab6 / PYNQ-Z2 - pornește automat simularea C a IP-ului Resize.
rem Se ruleaza NUMAI pe Windows, pe calculatorul cu Vitis HLS 2022.2.
cd /d "%~dp0"
set "LAB6_HLS_STAGE=csim"
set "LOG_FILE=%~dp0resize_csim.log"

echo [1/4] Verific Vitis HLS 2022.2...
where vitis_hls >nul 2>nul
if errorlevel 1 (
  if exist "C:\Xilinx\Vitis_HLS\2022.2\settings64.bat" (
    call "C:\Xilinx\Vitis_HLS\2022.2\settings64.bat"
  ) else if exist "C:\Xilinx\Vitis\2022.2\settings64.bat" (
    call "C:\Xilinx\Vitis\2022.2\settings64.bat"
  )
)
where vitis_hls >nul 2>nul
if errorlevel 1 (
  echo EROARE: vitis_hls nu este in PATH si nu am gasit instalarea standard.
  echo Deschideti un "Vitis HLS 2022.2 Command Prompt" si rulati din nou acest fisier.
  goto fail
)

echo [2/4] Verific biblioteca Vitis Vision din ramura 2022.2...
if not defined VITIS_VISION_INCLUDE (
  set "VITIS_VISION_INCLUDE=%~dp0..\..\..\..\Vitis_Libraries_2022_2\vision\L1\include"
)
if exist "%VITIS_VISION_INCLUDE%\imgproc\xf_resize.hpp" goto vision_ok

where git >nul 2>nul
if errorlevel 1 (
  echo EROARE: biblioteca Vitis Vision lipseste, iar git nu este in PATH.
  echo Instalati Git for Windows sau definiti VITIS_VISION_INCLUDE.
  goto fail
)
echo Descarc automat numai directoarele necesare din biblioteca oficiala AMD/Xilinx...
set "VISION_REPO=%~dp0..\..\..\..\Vitis_Libraries_2022_2"
if not exist "%VISION_REPO%\.git" (
  git clone --depth 1 --single-branch --filter=blob:none --sparse --branch 2022.2 "https://github.com/Xilinx/Vitis_Libraries.git" "%VISION_REPO%"
  if errorlevel 1 goto fail
)
git -C "%VISION_REPO%" sparse-checkout set vision/L1/include
if errorlevel 1 goto fail
:vision_ok
if not exist "%VITIS_VISION_INCLUDE%\imgproc\xf_resize.hpp" (
  echo EROARE: nu gasesc xf_resize.hpp in %VITIS_VISION_INCLUDE%
  goto fail
)

echo [3/4] Rulez C Simulation pentru Resize...
echo Log: "%LOG_FILE%"
vitis_hls -f build_resize.tcl >"%LOG_FILE%" 2>&1
if errorlevel 1 (
  echo.
  echo EROARE la C Simulation. Ultimele mesaje relevante:
  findstr /i /c:"ERROR:" /c:"error:" /c:"failed" "%LOG_FILE%"
  goto fail
)
echo [4/4] C Simulation s-a incheiat cu cod 0.
findstr /c:"SIMULARE C REUSITA" /c:"OK:" "%LOG_FILE%"
echo.
echo Verificati mesajele OK din jurnal. Daca nu apar, trimiteti resize_csim.log.
echo Nu pornesc automat sinteza pana nu confirmam simularea.
goto end

:fail
echo.
echo Procedura nu a fost finalizata. Trimiteti continutul relevant din:
echo "%LOG_FILE%"
:end
echo.
pause
endlocal
