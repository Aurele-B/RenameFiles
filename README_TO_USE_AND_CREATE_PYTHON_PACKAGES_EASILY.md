# How to ease dependency management and packaging with poetry

# 1. Avoid most package and virtual environment issues
Python is an amazing tool, but must users lose a lot of time because of package incompatibilities 
and other problems related to virtual environments. Although using virtual environments is great for replicability.
## 1.2. Use a programme to manage these problems for you
Use the terminal to install the python package and dependency management tool: poetry
```
pip install poetry
```
Stil in the terminal, use poetry to create the pyproject.toml and poetry.lock files:
```
poetry init
```
And follow instructions to add the necessary packages (called "main dependencies") to an environment automatically handled by poetry.
Then, and at any moment, you can add any package (dependency) to it with:
```
poetry add Pyside6
```
Note: if you want to create your own package, I recommand to define the following development dependencies: h5py, typing-extensions, wheel, setuptools

# 2. Create your own package
## 2.1. Create your own python package with poetry
You now just need to run:
```
poetry build
```
This will create a .whl file in a folder named dist than contain all your project.

## 2.2. Run your program with the command "RenameFiles" from the terminal
If you want your program to run with the command "RenameFiles" in the terminal, add these lines :
```
[tool.poetry.scripts]
RenameFiles = "renamefiles.__main__:run_rename_files"
```

## 2.3. Install a python package from a .whl file
### 2.3.1. Put the .whl file in a particular folder (here C:\Directory)
### 2.3.2. If already installed, use the terminal to uninstall it with:
- On windows
```
pip uninstall RenameFiles-1.0.0-py3-none-any.whl
```
- On Mac:
```
python3 -m pip uninstall RenameFiles-1.0.0-py3-none-any.whl
```
### 2.3.3. Install the package, using the terminal with:
- On windows:
```
cd C:\Directory
pip install h5py
pip install typing-extensions
pip install wheel
pip install RenameFiles-1.0.0-py3-none-any.whl
```
- On Mac:
```
cd \Directory
python3 -m pip install h5py
python3 -m pip install typing-extensions
python3 -m pip install wheel
python3 -m pip install RenameFiles-1.0.0-py3-none-any.whl
```
