# Delete all the files "Thumbs.db" recursively in the Parasitized directory
del /s /q Parasitized\Thumbs.db

# Delete all the files "Thumbs.db" recursively in the Uninfected directory
del /s /q Uninfected\Thumbs.db

# Rename directories
ren Parasitized Parasitized_all
ren Uninfected Uninfected_all

# Create the new directories
mkdir Parasitized_train
mkdir Parasitized_test
mkdir Parasitized_validation

mkdir Uninfected_train
mkdir Uninfected_test
mkdir Uninfected_validation

# Transfer data into the specific directory
echo "---Parasitized---"
cd Parasitized_all
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| sort /r') do (
  move "%%a" ..\Parasitized_train
  set /a count+=1
  if !count! equ 5000 (
    goto ParasitizedValidation
  )
)
:ParasitizedValidation
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| sort /r') do (
  move "%%a" ..\Parasitized_validation
  set /a count+=1
  if !count! equ 10000 (
    goto ParasitizedTest
  )
)
:ParasitizedTest
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| sort /r') do (
  move "%%a" ..\Parasitized_test
)
cd ..

echo "---Uninfected---"
cd Uninfected_all
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| sort /r') do (
  move "%%a" ..\Uninfected_train
  set /a count+=1
  if !count! equ 5000 (
    goto UninfectedValidation
  )
)
:UninfectedValidation
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| sort /r') do (
  move "%%a" ..\Uninfected_validation
  set /a count+=1
  if !count! equ 10000 (
    goto UninfectedTest
  )
)
:UninfectedTest
for /f "tokens=1* delims= " %%a in ('dir /b /a-d-h ^| sort /r') do (
  move "%%a" ..\Uninfected_test
)
cd ..
