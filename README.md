# Readme of RenameFiles application

## Purposes
This simple application has one simple usage and is a learning support for 3 python skills.

1. Usage: A simple tool to move files (having similar names) from one place to another while changing their naming.

3. Learning support:
- How to create a user interface
- How to use python packages and environments easily. And how to create packages.
- How to create executable and installer on Windows and Mac.
Note: each of these skills have a corresponding README file allowing you to learn them with the RenameFiles project.

## Content
The src folder contains 3 .py files:
1. _ _ main _ _.py
2. core/custom_widgets.py
3. core/rename_files.py

## Installation
1. Install [Python](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe), an IDE (like [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows) or Spyder) and git[git](https://git-scm.com/downloads)

3. Create a new project using "Get from Version Control..." or "Get from VCS"
<img
  src="https://github.com/Aurele-B/RenameFiles/blob/main/Get_from_VCS.jpg"
  alt="Alt text"
  title="Create project from VCS (github)"
  style="display: inline-block; margin: 0 auto; max-width: 300px"> 
<img
  src="https://github.com/Aurele-B/RenameFiles/blob/main/Clone_directly.jpg"
  alt="Alt text"
  title="Clone github repository)"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

3. Paste this URL: https://github.com/Aurele-B/RenameFiles.git to clone the repository
   (At this point, setting up a poetry environment is facultative)

4. Create an environment in another folder (i.e. "Configure a python interpreter")

Note: you also can clone "manually" this repository by downloading its zip file:
- Click: "Code" and "Download ZIP"
<img
  src="https://github.com/Aurele-B/RenameFiles/blob/main/How_to_download_from_github.jpg"
  alt="Alt text"
  title="Watch were to click"
  style="display: inline-block; margin: 0 auto; max-width: 300px"> 

- Extract this zip file and put the content of the sub-folder "RenameFiles-main/RenameFiles-main" in the newly created python project.

### Package requirements
To install the tool to create user interfaces, write in terminal:
```
pip install Pyside6
```

### Usage
To run the python application, open src/RenameFiles/__main__.py (in an IDE) and run the function:
```
run_rename_files()
```
Use one of the README files to learn what you need for your own project.
