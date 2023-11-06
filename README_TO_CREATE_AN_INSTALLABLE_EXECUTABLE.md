How to create an executable for any python project and compress it into a setup file.
=================
The first part allows this on Windows, the second on Mac.

# 1. Create a windows executable and setup file
Always make sure that pythonxx (for python.exe) and pythonxx/Scripts (for pip) are in windows path
Always use the exact same folder architecture as in the RenameFiles project, i.e.:

-RenamesFiles/
--src/
--renamefiles/
---__main__.py
---__init__.py
---core/
----any_file.py
----any_other_file.py
---any_other_folder/
----any_file.py
----any_other_file.py

## 1.1 Go in the project directory (in terminal)
```
cd C:/Directory/Scripts/Python/RenameFiles
```
## 1.2. Install all packages (in terminal)
To run these lines, you need a pyproject.toml file in your project. Using it facilitate python package usages.  
If you don't have this file, see the README_TO_USE_AND_CREATE_PYTHON_PACKAGES_EASILY.md
```
python -m pip install --upgrade pip
python -m pip install poetry
```
Make sure that both the terminal and poetry use the same environment:
```
poetry env use C:/Directory/Scripts/Python/RenameFilesEnv/Scripts/python.exe
C:/Directory/Scripts/Python/RenameFilesEnv/Scripts/activate
```
Install all packages
```
poetry add pyinstaller
poetry install
```
## 1.3 Change directory (in terminal)
```
cd C:/Directory/Scripts/Python/RenameFiles/src/RenameFiles
```

## 1.4 If your project is complex and requires a python file containing paths to particular files
This file (e.g. paths.py) should contain: 
```
import os
from pathlib import Path
CURR_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
renamefiles_DIR = CURR_DIR.parent#.parent # Add the ".parent" when creating a windows executable
```
Contrary to all uses, creating an executable requires to add a .parent

## 1.5. Create the windows executable

### 1.5.1 If no __main__.spec file exists, use (in terminal):
```
pyinstaller __main__.py
```

### 1.5.2 There already is a __main__.spec file, use:
#### 1.5.2.1 Update the __main__.spec file:
In Analysis/pathex : after "RenameFiles_DIR, ", put the path toward the current virtual Env, e.g.:\

#### 1.5.2.2 Check path to the environment in the __main__.spec file 
It should be something like:

C:\Directory\Scripts\Python\RenameFilesEnv\Scripts\python.exe

#### 1.5.2.3. Create .exe (in terminal)
```
pyinstaller __main__.spec
```

## 1.6. Create an installer
### 1.6.1 Move and Rename the dist folder (within src\RenameFiles) into RenameFiles
### 1.6.2 Compress it into a .zip file.
### 1.6.3 Run the NSIS program (if not installed, download and install it)
### 1.6.4 Click on "Installer based on zip file "/open/RenameFiles.zip
Note: Economize installer size by checking the "Solid" option/
### 1.6.5 Click on Generate, wait and close. The installer is ready.



# 2. Create a Mac executable and an ISO image
This can also be done with poetry although I did not test it. The method below has been tested.
## 2.1. Install all packages in Terminal
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade coloredlogs exif ExifRead llvmlite numba numpy opencv-python-headless pandas plum-py psutil pyinstaller PySide2 python-dateutil pytz rawpy scipy screeninfo six
```

## 2.2. Create a python environment
python3 -m venv /path/to/new/virtual/environment

## 2.3. Activate the python environment
source /Users/UserName/Desktop/python/Venv/bin/activate

## 2.4. Install all packages in that env (May be only usefull for pycharm)
python -m pip install -U pip setuptools 
pip install --upgrade coloredlogs exif ExifRead llvmlite numba numpy opencv-python-headless pandas plum-py psutil pyinstaller PySide2 python-dateutil pytz rawpy scipy screeninfo six

## 2.5 Go to project location
cd /Users/Annuminas/Desktop/python/src/RenameFiles

## 2.5. Create the Mac executable
### 2.5.1 Easy way, use (in terminal):
```
pyinstaller __main__.py
```
### 2.5.2 There already is a __main__.spec file and you don't want to overwrite it:
#### 2.5.2.1 Update the __main__.spec file:
In Analysis/pathex : after "RenameFiles_DIR, ", put the path toward the current virtual Env, e.g.:\

#### 2.5.2.2 Check path to the environment in the __main__.spec file 
It should be something like:

/Users/UserName/Desktop/python/Venv

#### 2.5.2.3. Create .exe (in terminal)
```
pyinstaller __main__.spec
```
## 2.6. Create an ISO image
If Homebrew is not installed, put that link in the terminal (or get an updated link here:https://brew.sh)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
brew install create-dmg
```
IF already installed proceed:
Once brew and create-dmg are installed, save the shell script in the project root
and execute it to create the iso image:
```
chmod +x create_dmg.sh
./create_dmg.sh
```
