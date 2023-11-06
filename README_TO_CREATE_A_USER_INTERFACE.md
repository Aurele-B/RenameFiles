How to use RenameFiles as a quickstart to create a user interface for your project
=================

# 1. Read README.md to learn how to install and use RenameFiles

# 2. Modify the rename_files.py file to transform it into what you want
If you want to modify it to create your own application, start by slightly modifying the python file named:
rename_files.py in the src/core folder.

For instance, you can start by modifying the title, then a push button, then the method linked to that push button...
To do so, follow the next steps

## 2.1. In rename_files.py, find the "RenameFilesWidget" class its method called "complete_widget".
## 2.2. Identify the 9 paragraphs (corresponding to something named "layout") corresponding to 9 rows in the interface.
When the application runs, you can see the title and 8 rows containing 2 to 3 elements (called widgets). 
In each row, these elements are encapsulated into a horizontal layout, and that layout is put inside a bigger widget. 
Hence, each row is also a widget that needs to be encapsulated in the vertical layout (forming a column) of the whole windows. 
Note: The ninth row is invisible and appears after a particular event. 

## 2.3. You can safely delete/modify these paragraphs to understand how they work and make your own application.
- Deleting most of them as soon as possible is good to simplify your code. 
Note: Keep another version of the code to later incorporate new widgets properly 

## 2.4. The widgets you can learn to use here are:
- Text: fixed text in the app
- Text to edit: modifiable text
- Push button: a button linked to an action coded in a particular method (function) in the "RenameFilesWidget" class.
- Combo box: select from a list of options
- Spin box: select a number
- Check box: check or uncheck a condition

## 2.5. Most widgets can be linked to a method so that the interface react to the actions of the user
To allow your app to react to the actions of the user, (for instance: to run some code when the user click on the Run Push button)
you need to connect the push button widget with a method of the "RenameFilesWidget" class.
Basically, you create the widget with:
```
        self.run = PButton('Run', night_mode)
```
And you connect it with:
```
        self.run.clicked.connect(self.run_is_clicked)
```
To a method (called run_is_clicked), defined after the end of the definition of the "def complete_widget(self):" method, with:
```
    def run_is_clicked(self):
        pass
```
This line is less indented than the lines it contains. 
Replace "pass" by anything you want to happen when the click button is clicked.
