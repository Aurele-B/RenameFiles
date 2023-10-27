# Readme of RenameFiles application

## Purposes
This application has two purposes:
1. To move files (having similar names) from one place to another while changing their naming.
2. To be a quickstart for anyone who want to do a graphical user interface (GUI) in python.

## Content
The src folder contains 3 .py files:
1. __main.py
2. core/custom_widgets.py
3. core/rename_files.py

To download this content, use Code and Download ZIP:
<img
  src="https://github.com/Aurele-B/RenameFiles/How_to_download_from_github.jpg"
  alt="Alt text"
  title="Watch were to click"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

To create your first GUI, put these in a new python project and install the required package (next section).

## Package requirements
This application requires to install the Pyside6 package in the environment of your python project:
```
pip install Pyside6
```

## Usage
To run the python application, open the __main.py (in an IDE) and run the function:
```
run_rename_files()
```
If you want to modify it to create your own application, start by slightly modifying the third python file:
3. core/rename_files.py

For instance, you can start by modifying the title, then a push button, then the method linked to that push button...
Enjoy!