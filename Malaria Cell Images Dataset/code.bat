@echo off
rem Rename directories
ren Parasitized Parasitized_all
ren Uninfected Uninfected_all

rem Create the new directories
mkdir Parasitized_train
mkdir Parasitized_test
mkdir Parasitized_validation
mkdir Uninfected_train
mkdir Uninfected_test
mkdir Uninfected_validation

rem Transfer data into the specific directories
echo ---Parasitized---
cd Parasitized_all
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| more +5001 ^| more /n') do (
  if %%a LEQ 5000 (
    copy "%%b" "..\Parasitized_train"
  ) else if %%a LEQ 10000 (
    copy "%%b" "..\Parasitized_validation"
  ) else (
    copy "%%b" "..\Parasitized_test"
  )
)

cd ..

echo ---Uninfected---
cd Uninfected_all
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| more +5001 ^| more /n') do (
  if %%a LEQ 5000 (
    copy "%%b" "..\Uninfected_train"
  ) else if %%a LEQ 10000 (
    copy "%%b" "..\Uninfected_validation"
  ) else (
    copy "%%b" "..\Uninfected_test"
  )
)

cd ..
