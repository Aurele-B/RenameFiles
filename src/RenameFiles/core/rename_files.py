#!/usr/bin/env python3
"""This module contains the RenameFilesWidget, main widget of the RenameFiles application
Transform this script, and only this script (at first), to create your own app.

@author: Aurèle Boussard
"""

import os
from glob import glob
import shutil
from pathlib import Path
from src.RenameFiles.core.custom_widgets import *


class RenameFilesWidget(WindowType):
    """ This is the main widget of the RenameFiles application: the one that you will transform to create your own app.

     This widget is the big window containing all text, buttons, checkboxes... of the application
     Each of these (sub)widget are simplified in the custom_widgets.py file. Use them as they are used here.

     The RenameFilesWidget is a class inherited from the widget WindowType,
                               itself inherited from Pyside6.QtWidgets.QWidget
     --> Class inheritance allows to modify and add features to a parent class without modifying that parent.

    """

    def __init__(self):
        """ This method automatically runs as soon as an instance of RenameFilesWidget is created through, e.g.:
        session = RenameFilesWidget()

        Here, it directly runs the lines allowing to complete the widget, in the complete_widget method.
        """
        super().__init__()
        self.complete_widget()

    def complete_widget(self):
        """Initialization of all sub-widgets in the RenameFilesWidget

        This method:
        1. Initialize default parameters to help the user to know what to do in each fields
        2. Organize the RenameFilesWidget as vertical boxes (named QVBoxLayout)
        containing many horizontal boxes (named QHBoxLayout)
        3. Connect widgets (e.g. Push buttons) to other methods of RenameFilesWidget, like the run_is_clicked method
        (allowing to run the software)

        """
        """1. Initialize default parameters"""
        self.default_file_name = "IMG_"
        self.default_file_extension = ".jpg"
        self.default_src_dir = "C:/"
        self.default_dest_dir = "C:/"
        self.default_action_on_constant_chars = "Keep"
        self.default_remove_from_src = False
        self.existing_files = []


        self.setWindowTitle('Rename files')

        """2. Organize the RenameFilesWidget as vertical boxes
        (named self.Vlayout) containing horizontal boxes (named, for instance, self.file_name_layout"""
        self.Vlayout = QtWidgets.QVBoxLayout()

        """Use FixedText() to insert text in your main widget"""
        self.title_label = FixedText('Rename files', police=40, night_mode=night_mode)
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)

        """Use the addWidget() method of a layout to add a widget to one layout (here, organized as vertical boxes)"""
        self.Vlayout.addWidget(self.title_label)
        """Use addItem(self.vertical_space) create an epty space between two boxes of a vertical layout"""
        self.Vlayout.addItem(self.vertical_space)

        """To add a horizontal boxes in one box of a vertical layout:
        a. Create an empty widget
        b. Create a QHBoxLayout
        c. Create one or several widgets that you want to add to that layout
        d. Add these widgets to the layout, with any required horizontal spaces
        e. Set the layout inside the empty widget
        f. Add this widget (contaning the horizontal layout) to the (larger) vertical layout
        
        --> the following is only a repetition of each of these steps. 
        You can delete any of the nine following paragraphs. 
        Do not forget to also delete the methods (small function definitions below) their widgets are connected to.
        """

        # First horizontal layout:
        # a. Create an empty widget
        self.src_widget = QtWidgets.QWidget()
        # b. Create a QHBoxLayout
        self.src_layout = QtWidgets.QHBoxLayout()
        # c. Create one or several widgets that you want to add to that layout
        self.src_path_label = FixedText('Source folder:', police=20, night_mode=night_mode)
        self.src_path = EditText(self.default_src_dir, night_mode)
        self.browse_src = PButton('Browse', night_mode)
        self.browse_src.clicked.connect(self.browse_src_is_clicked)  # Clicking the button triggers the function
        # d. Add these widgets to the layout, with any required horizontal spaces
        self.src_layout.addWidget(self.src_path_label)
        self.src_layout.addWidget(self.src_path)
        self.src_layout.addWidget(self.browse_src)
        self.src_layout.addItem(self.horizontal_space)
        # e. Set the layout inside the empty widget
        self.src_widget.setLayout(self.src_layout)
        # f. Add this widget (contaning the horizontal layout) to the (larger) vertical layout
        self.Vlayout.addWidget(self.src_widget)

        # Second horizontal layout:
        self.dest_widget = QtWidgets.QWidget()
        self.dest_layout = QtWidgets.QHBoxLayout()
        self.dest_path_label = FixedText('Target folder:', police=20, night_mode=night_mode)
        self.dest_path = EditText(self.default_dest_dir, night_mode)
        self.browse_dest = PButton('Browse', night_mode)
        self.browse_dest.clicked.connect(self.browse_dest_is_clicked)
        self.dest_layout.addWidget(self.dest_path_label)
        self.dest_layout.addWidget(self.dest_path)
        self.dest_layout.addWidget(self.browse_dest)
        self.dest_layout.addItem(self.horizontal_space)
        self.dest_widget.setLayout(self.dest_layout)
        self.Vlayout.addWidget(self.dest_widget)

        # Third horizontal layout:
        self.file_name_widget = QtWidgets.QWidget()
        self.file_name_layout = QtWidgets.QHBoxLayout()
        self.file_name_label = FixedText('Constant characters:', police=20, night_mode=night_mode)
        self.file_name = EditText(self.default_file_name, night_mode)
        self.file_name_layout.addWidget(self.file_name_label)
        self.file_name_layout.addWidget(self.file_name)
        self.file_name_layout.addItem(self.horizontal_space)
        self.file_name_widget.setLayout(self.file_name_layout)
        self.Vlayout.addWidget(self.file_name_widget)

        # Fourth horizontal layout:
        self.action_on_constant_chars_widget = QtWidgets.QWidget()
        self.action_on_constant_chars_layout = QtWidgets.QHBoxLayout()
        self.action_on_constant_chars_label = FixedText('Action on const chars:', police=20, night_mode=night_mode)
        self.action_on_constant_chars = Combobox(["Keep", "Change", "Remove"], night_mode)
        self.action_on_constant_chars.setCurrentText('Keep')
        self.action_on_constant_chars.currentTextChanged.connect(self.action_on_constant_chars_changed)
        self.action_on_constant_chars_layout.addWidget(self.action_on_constant_chars_label)
        self.action_on_constant_chars_layout.addWidget(self.action_on_constant_chars)
        self.action_on_constant_chars_layout.addItem(self.horizontal_space)
        self.action_on_constant_chars_widget.setLayout(self.action_on_constant_chars_layout)
        self.Vlayout.addWidget(self.action_on_constant_chars_widget)

        # Fifth horizontal layout:
        # As this layout is only useful when self.default_action_on_constant_chars == "Change",
        # the last row of this paragraph set it invisible. It can become visible when
        # the combobox: self.action_on_constant_chars changes to "Change"
        self.new_file_name_widget = QtWidgets.QWidget()
        self.new_file_name_layout = QtWidgets.QHBoxLayout()
        self.new_file_name_label = FixedText('New constant characters:', police=20, night_mode=night_mode)
        self.new_file_name = EditText("", night_mode)
        self.new_file_name_layout.addWidget(self.new_file_name_label)
        self.new_file_name_layout.addWidget(self.new_file_name)
        self.new_file_name_layout.addItem(self.horizontal_space)
        self.new_file_name_widget.setLayout(self.new_file_name_layout)
        self.Vlayout.addWidget(self.new_file_name_widget)
        self.new_file_name_widget.setVisible(False)

        # Sixth horizontal layout:
        self.file_extension_widget = QtWidgets.QWidget()
        self.file_extension_layout = QtWidgets.QHBoxLayout()
        self.file_extension_label = FixedText('File extension:', police=20, night_mode=night_mode)
        self.file_extension = EditText(self.default_file_extension, night_mode)
        self.file_extension_layout.addWidget(self.file_extension_label)
        self.file_extension_layout.addWidget(self.file_extension)
        self.file_extension_layout.addItem(self.horizontal_space)
        self.file_extension_widget.setLayout(self.file_extension_layout)
        self.Vlayout.addWidget(self.file_extension_widget)

        # Seventh horizontal layout:
        self.start_nb_widget = QtWidgets.QWidget()
        self.start_nb_layout = QtWidgets.QHBoxLayout()
        # If you want a tip to appear when the mouse stays 1 second on a text, use the tip parameter.
        self.start_nb_label = FixedText('Starting number:', police=20, night_mode=night_mode, tip="When renaming files, the number to give to the first file.")
        self.start_nb = Spinbox(0, 1000000000, val=1)
        self.start_nb_layout.addWidget(self.start_nb_label)
        self.start_nb_layout.addWidget(self.start_nb)
        self.start_nb_layout.addItem(self.horizontal_space)
        self.start_nb_widget.setLayout(self.start_nb_layout)
        self.Vlayout.addWidget(self.start_nb_widget)

        # Eighth horizontal layout:
        self.remove_from_src_widget = QtWidgets.QWidget()
        self.remove_from_src_layout = QtWidgets.QHBoxLayout()
        self.remove_from_src = Checkbox(self.default_remove_from_src)
        self.remove_from_src.stateChanged.connect(self.default_remove_from_src_check)
        self.remove_from_src_label = FixedText('Remove files from source', police=20, night_mode=night_mode)
        self.remove_from_src_layout.addWidget(self.remove_from_src)
        self.remove_from_src_layout.addWidget(self.remove_from_src_label)
        self.remove_from_src_layout.addItem(self.horizontal_space)
        self.remove_from_src_widget.setLayout(self.remove_from_src_layout)
        self.Vlayout.addWidget(self.remove_from_src_widget)

        # Ninth horizontal layout:
        self.run_widget = QtWidgets.QWidget()
        self.run_layout = QtWidgets.QHBoxLayout()
        self.check_run = PButton('Check', night_mode)
        self.check_run.clicked.connect(self.check_run_is_clicked)
        self.message = FixedText('', police=20, night_mode=night_mode)
        self.message.setStyleSheet("color: rgb(230, 145, 18)")
        self.run = PButton('Run', night_mode)
        self.run.clicked.connect(self.run_is_clicked)
        self.run_layout.addWidget(self.check_run)
        self.run_layout.addItem(self.horizontal_space)
        self.run_layout.addWidget(self.message)
        self.run_layout.addItem(self.horizontal_space)
        self.run_layout.addWidget(self.run)
        self.run_widget.setLayout(self.run_layout)
        self.Vlayout.addWidget(self.run_widget)


        self.Vlayout.addItem(self.vertical_space)
        """NEVER DELETE THIS LINE
         As for horizontal layouts, never forget to set the vertical layout in the current widget, i.e. self"""
        self.setLayout(self.Vlayout)

    def browse_src_is_clicked(self):
        """This method is connected to the browse_src push button
        Each time this button is clicked, this method open a file dialog window allowing to chose a directory"""
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory(self.default_src_dir)
        self.default_src_dir = dialog.getExistingDirectory(self, 'Select the folder where the files are')
        self.src_path.setText(self.default_src_dir)

    def browse_dest_is_clicked(self):
        """This method is connected to the browse_dest push button
        Each time this button is clicked, this method open a file dialog window allowing to chose a directory"""
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory(self.default_dest_dir)
        self.default_dest_dir = dialog.getExistingDirectory(self, 'Select where to put file')
        self.dest_path.setText(self.default_dest_dir)

    def action_on_constant_chars_changed(self):
        """This method is connected to the action_on_constant_chars combobox
        Each time the status of this combobox change, these lines are run"""
        self.default_action_on_constant_chars = self.action_on_constant_chars.currentText()
        # Set visible, only when action_on_constant_chars is "Change"
        self.new_file_name_widget.setVisible(self.default_action_on_constant_chars == "Change")

    def default_remove_from_src_check(self):
        """This method is connected to the default_remove_from_src checkbox
        Each time the status of this checkbox change, these lines are run"""
        self.default_remove_from_src = self.remove_from_src.isChecked()

    def check_run_is_clicked(self):
        """This method is connected to the check_run push button
        Each time this button is clicked, this method check whether user-set informations are correct"""
        src = self.src_path.text()
        dest = self.dest_path.text()
        name = self.file_name.text()
        extension = self.file_extension.text()

        os.chdir(Path(src))
        self.existing_files = glob(name + '*' + extension)

        if len(self.existing_files) > 0:
            if os.path.isdir(dest):
                self.message.setText("Files found, ready to run")
                return True
            else:
                self.message.setText("Incorrect destination file")
                return False
        else:
            if os.path.isdir(dest):
                self.message.setText("No corresponding files")
            else:
                self.message.setText("No files and wrong destination")
            return False

    def run_is_clicked(self):
        """This method is connected to the run push button
        Each time this button is clicked, this method runs the application to rename and move files"""
        run_is_possible = self.check_run_is_clicked()
        if run_is_possible:
            self.message.setText("Renaming files, please wait...")
            name_length = max((len(self.existing_files[0]), len(self.existing_files[-1])))
            digit_number = name_length - len(self.file_name.text()) - len(self.file_extension.text())
            radical_length = name_length - digit_number - len(self.file_extension.text())
            if self.action_on_constant_chars.currentText() == "Keep":
                radical = self.existing_files[0][:radical_length]
            elif self.action_on_constant_chars.currentText() == "Change":
                radical = self.new_file_name.text()
            elif self.action_on_constant_chars.currentText() == "Remove":
                radical = ""

            for file_i in range(len(self.existing_files)):
                new_name = radical + str(file_i + int(self.start_nb.value())).rjust(digit_number, "0") + self.file_extension.text()
                dest_name = Path(self.dest_path.text()) / new_name
                if self.remove_from_src.isChecked():
                    os.rename(self.existing_files[file_i], dest_name)
                else:
                    shutil.copy(self.existing_files[file_i], dest_name)
            self.message.setText("All files are renamed.")

