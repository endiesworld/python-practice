# Creating a virtual environment

## install virtual environment

pip install virtualenv (do this once)

## windows system create a virtual environment folder

python -m venv <folder_name>

## osx/linux (bash)

virtualenv <folder_name>

USING VIRTUAL ENVIRONMENT

## windows

### cmd.exe

<folder_name>\Scripts\Activate.bat

### powershell

<folder_name>\Scripts\Activate.psi

### bash shell

. ./<folder_name>/Scripts/activate

## osc/linus (bash)

source <folder_name>/bin/activate

INSTALLING PACKAGES

## Installing an individual package

pip install package_name

## Installing from a list of packages

pip install -r requirements.txt (requirements has to be a file in the root directory)
