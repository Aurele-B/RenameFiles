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
  src="https://github.com/Aurele-B/RenameFiles/blob/main/How_to_download_from_github.jpg"
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

To do so, you will modify the "complete_widget" method of "RenameFilesWidget" class. 
This method has 9 paragraph, each corresponding to a row in the window when the application runs.
You can safely delete/modify these paragraph to understand how they work and make your own application.
Deleting them quickly is good to simplify your code, 
but keep their usage somewhere so that you can learn how to use the widget(s) they contain. These widgets are:
- Text: fixed text in the app
- Text to edit: modifiable text
- Push button: a button linked to an action coded in a particular method (function) in the "RenameFilesWidget" class.
- Combo box: select from a list of options
- Spin box: select a number
- Check box: check or uncheck a condition