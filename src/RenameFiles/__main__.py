#!/usr/bin/env python3
"""This script contains the entry point of the module
The run_rename_files function allows to start the application

@author: Aurèle Boussard
"""

import os
import sys
from pathlib import Path
from PySide6 import QtWidgets

def run_rename_files():
    """Entry point of rename files software.
    It uses the RenameFilesWidget, i.e. the main widget of the application.

    To create your own app:
    1. Check that this one works on your computer
    2. Modify the RenameFilesWidget in rename_files.py
    3. Test if it works as you wanted it to work

    Redo 2. and 3. as many times as necessary
    """
    from RenameFiles.core.rename_files import RenameFilesWidget
    app = QtWidgets.QApplication([])
    session = RenameFilesWidget()
    session.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_rename_files()

