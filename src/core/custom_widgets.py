#!/usr/bin/env python3
"""This module contains all modified/simplified widgets from PySide6
It is made to be easier to use and to be consistent in terms of colors and sizes.

If you want to modify the police and color of your application, try to change the following variables!

@author: Aurèle Boussard
"""
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QImage, QPixmap, QFont, QPainter
# from cv2 import cvtColor, COLOR_BGR2RGB, resize

night_mode = False
# colorblind-friendly : rgb(42, 251, 97) , rgb(126, 85, 197)
buttonfont = QFont("Segoe UI Semibold", 17, QFont.Bold)
# titlesize = 40

titlefont = f"Baskerville Old Face" #"40pt Baskerville Old Face"
textsize = 15
textfont = "Century Gothic"

backgroundcolor = "rgb(255,255,255)"
textColor = "rgb(0, 0, 0)"
bordercolor = "rgb(255,255,255)"
selectioncolor = "rgb(1, 122, 94)"
selectionbackgroundcolor = "rgb(240,240,240)"
selectionbordercolor = "rgb(255,0,0)"
buttoncolor = "rgb(255,255,255)"
buttonclickedcolor = "rgb(100,100,120)"
buttonborder = "2px solid rgb(0, 0, 0)"
buttonangles = "13px"
rollingborder = "1px solid rgb(127, 127, 127)"
rollingangles = "4px"

night_background_color = "rgb(50,50,65)"
night_text_Color = "rgb(255, 255, 255)"
night_border_color = "rgb(50,50,65)"
night_selection_color = "rgb(1, 152, 117)"
night_selection_background_color = "rgb(50,50,65)"
night_selection_border_color = "rgb(255,0,0)"
night_button_color = "rgb(50,50,65)"
night_button_clicked_color = "rgb(100,100,120)"
night_button_border = "2px solid rgb(255, 255, 255)"


class WindowType(QtWidgets.QWidget):
    resized = QtCore.Signal()
    def __init__(self, night_mode=False):
        super().__init__()
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.setFont(QFont(textfont, textsize, QFont.Medium))
        self.night_mode_switch(night_mode)
        self.horizontal_space = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.MinimumExpanding,
                                              QtWidgets.QSizePolicy.Maximum)
        self.vertical_space = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Maximum,
                                              QtWidgets.QSizePolicy.MinimumExpanding)
        self.resized.connect(self.center_window)

    def resizeEvent(self, event):
        '''
        # Use this signal to detect a resize event and call center window function
        :param event:
        :return:
        '''
        self.resized.emit()
        return super(WindowType, self).resizeEvent(event)

    def center_window(self):
        qr = self.frameGeometry()
        # cp = QtWidgets.QDesktopWidget().availableGeometry().center()  # PyQt 5
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()  # Pyside 6
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def night_mode_switch(self, night_mode):
        if night_mode:
            self.setStyleSheet(
                "background-color: %s; color: %s; font: %s; border-color: %s; selection-color: %s; selection-background-color: %s" % (
                night_background_color, night_text_Color, f"{textsize}pt {textfont};", night_border_color,
                night_selection_color, night_selection_background_color))
        else:
            self.setStyleSheet(
                "background-color: %s; color: %s; font: %s; border-color: %s; selection-color: %s; selection-background-color: %s" % (
                backgroundcolor, textColor, f"{textsize}pt {textfont};", bordercolor, selectioncolor,
                selectionbackgroundcolor))


class PButton(QtWidgets.QPushButton):
    def __init__(self, text, fade=True, night_mode=False):
        """

        self.setStyleSheet("background-color: rgb(107, 145, 202);\n"
                                "border-color: rgb(255, 255, 255);\n"
                                "color: rgb(0, 0, 0);\n"
                                "font: 17pt \"Britannic Bold\";")
        :param text:
        """
        super().__init__()
        self.setText(text)
        self.night_mode_switch(night_mode)
        self.setFont(buttonfont)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setFixedWidth(len(text)*15 + 25)

    def night_mode_switch(self, night_mode):
        if night_mode:
            self.style = {"buttoncolor": night_button_color, "buttontextColor": night_text_Color, "buttonborder": night_button_border,
                          "buttonangles": buttonangles}
        else:
            self.style = {"buttoncolor": buttoncolor, "buttontextColor": textColor, "buttonborder": buttonborder,
                          "buttonangles": buttonangles}
        self.update_style()

    def event_filter(self, event):
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
                self.fade()
            else:
                self.unfade()

    def update_style(self):
        self.setStyleSheet(
            "background-color: %s; color: %s; border: %s; border-radius: %s" % tuple(self.style.values()))

    def color(self, color):
        self.style["buttoncolor"] = color
        self.update_style()

    def textcolor(self, textcolor):
        self.style["buttontextColor"] = textcolor
        self.update_style()

    def border(self, border):
        self.style["buttonborder"] = border
        self.update_style()

    def angles(self, angles):
        self.style["buttonangles"] = angles
        self.update_style()

    def fade(self):
        self.setWindowOpacity(0.5)
        self.setStyleSheet("background-color: %s; color: %s; border: %s; border-radius: %s" % (buttonclickedcolor, textColor, buttonborder, buttonangles))
        QtCore.QTimer.singleShot(300, self.unfade)

    def unfade(self):
        self.setWindowOpacity(1)
        self.setStyleSheet("background-color: %s; color: %s; border: %s; border-radius: %s" % (buttoncolor, textColor, buttonborder, buttonangles))


class Spinbox(QtWidgets.QDoubleSpinBox):
    def __init__(self, min=0, max=100000, val=0, decimals=None, night_mode=False):
        super().__init__()
        self.setMinimum(min)
        self.setMaximum(max)
        self.setValue(val)
        self.decimals = decimals
        if decimals is not None:
            self.setDecimals(decimals)
            self.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        else:
            self.setDecimals(0)
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.setFont(QFont(textfont, textsize, QFont.Medium))
        self.night_mode_switch(night_mode)

    def night_mode_switch(self, night_mode):
        if night_mode:
            self.setStyleSheet(
                "background-color: %s; color: %s; border-color: %s; border: %s; border-radius: %s" % (
                    night_background_color, night_text_Color, night_border_color, rollingborder, rollingangles))
        else:
            self.setStyleSheet(
                "background-color: %s; color: %s; border-color: %s; border: %s; border-radius: %s" % (
                    backgroundcolor, textColor, bordercolor, rollingborder, rollingangles))


class Combobox(QtWidgets.QComboBox):
    def __init__(self, items_list, current_idx=None, night_mode=False):
        super().__init__()
        for item in items_list:
            self.addItem(item)
        if current_idx is not None:
            self.setCurrentIndex(current_idx)
        self.setFixedHeight(30)
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.night_mode_switch(night_mode)

    def night_mode_switch(self, night_mode):
        if night_mode:
            self.setStyleSheet("border-color: %s; border: %s; border-radius: %s" % (
                night_background_color, rollingborder, rollingangles))
        else:
            self.setStyleSheet("border-color: %s; border: %s; border-radius: %s" % (
                backgroundcolor, rollingborder, rollingangles))


class Checkbox(QtWidgets.QCheckBox):
    def __init__(self, set_checked, night_mode=None):
        super().__init__()
        self.setChecked(set_checked)
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.setMinimumWidth(75)
        # self.setStyleSheet("padding:5px")
        self.setStyleSheet("margin-left:50%; margin-right:50%;")


class EditText(QtWidgets.QLineEdit):
    def __init__(self, text, police=None, align='l', tip=None, night_mode=False):
        super().__init__()
        self.setMaximumHeight(36)
        self.setText(str(text))
        self.night_mode_switch(night_mode)

    def night_mode_switch(self, night_mode):
        if night_mode:
            self.setStyleSheet(
                "background-color: %s; color: %s; font: %s; border-bottom: %s; border-top: %s" % (
                    night_background_color, night_text_Color, f"{textsize}pt {textfont};", f"1px solid grey", f"1px solid grey"))
        else:
            self.setStyleSheet(
                "background-color: %s; color: %s; font: %s; border-bottom: %s; border-top: %s" % (
                    backgroundcolor, textColor, f"{textsize}pt {textfont};", f"1px solid grey", f"1px solid grey"))


class FixedText(QtWidgets.QLabel):
    def __init__(self, text, police=None, align='l', tip=None, night_mode=False):
        super().__init__()
        self.setText(text)
        if align == 'l':
            self.setAlignment(QtCore.Qt.AlignLeft)
        elif align == 'r':
            self.setAlignment(QtCore.Qt.AlignRight)
        else:
            self.setAlignment(QtCore.Qt.AlignCenter)
        if police is not None:
            if police > 23:
                self.night_mode_switch(night_mode, f"{police}pt {titlefont}")
                self.setMargin(2)

        else:
            self.setFont(QFont(textfont, textsize + 2, QFont.Medium))

        if tip is not None:
            self.setToolTip(tip)
            if night_mode:
                self.setStyleSheet("""QToolTip {background-color: rgb(70,70,85);color: rgb(1, 152, 117);
                                                            border: white solid 1px}""")
            else:
                self.setStyleSheet("""QToolTip {background-color: rgb(240,240,240);
                                                                                  color: rgb(1, 122, 94);
                                                                                  border: black solid 1px
                                                                                  }""")

    def night_mode_switch(self, night_mode, font):
        if night_mode:
            self.setStyleSheet("font: %s; color: %s; margin-bottom: %s" % (font, night_text_Color, "30%"))
        else:
            self.setStyleSheet("font: %s; color: %s; margin-bottom: %s" % (font, textColor, "30%"))


class LineWidget(QtWidgets.QWidget):
    def __init__(self, ori="h", size=None, night_mode=False):
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout()
        self.line = QtWidgets.QFrame()
        if ori == "h":
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            # self.setFrameShadow(QtWidgets.QFrame.Sunken)
        else:
            self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.night_mode_switch(night_mode)
        if size is None:
            size = [1, 4]
        self.line.setFixedHeight(size[0])
        self.line.setFixedWidth(size[1])
        horizontal_space = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.MinimumExpanding,
                                                      QtWidgets.QSizePolicy.Maximum)
        self.layout.addItem(horizontal_space)
        self.layout.addWidget(self.line)
        self.layout.addItem(horizontal_space)
        self.setLayout(self.layout)

    def night_mode_switch(self, night_mode):
        if night_mode:
            self.line.setStyleSheet("QFrame { background-color: rgb(255, 255, 255) }")
        else:
            self.line.setStyleSheet("QFrame { background-color: rgb(0, 0, 0) }")


""" If you want to add an image and modify it dynamically with the usage of your application, use and modify these: """


# class InsertImage(QtWidgets.QLabel):
#     def __init__(self, image, max_height, max_width):
#         super().__init__()
#         self.true_shape = image.shape
#         self.max_height = max_height
#         self.max_width = max_width
#         self.im_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
#                                                     QtWidgets.QSizePolicy.MinimumExpanding)
#         self.setSizePolicy(self.im_size_policy)
#
#         height_width_ratio = image.shape[0] / image.shape[1]
#         image = cvtColor(image, COLOR_BGR2RGB)
#         image = QImage(image.data, image.shape[1], image.shape[0], 3 * image.shape[1], QImage.Format_RGB888)
#         image = QPixmap(image)
#         self.setScaledContents(True)
#         if self.max_width * height_width_ratio < self.max_height:
#             self.scaled_shape = [round(self.max_width * height_width_ratio), self.max_width]
#         else:
#             self.scaled_shape = [self.max_height, round(self.max_height / height_width_ratio)]
#         self.setMaximumHeight(self.scaled_shape[0])
#         self.setMaximumWidth(self.scaled_shape[1])
#         self.setPixmap(QPixmap(image))
#         self.adjustSize()
#
#
#     def update_image(self, image, text=None, color=255):
#         self.true_shape = image.shape
#         height_width_ratio = image.shape[0] / image.shape[1]
#         image = cvtColor(image, COLOR_BGR2RGB)
#         image = QImage(image.data, image.shape[1], image.shape[0], 3 * image.shape[1], QImage.Format_RGB888)
#         image = QPixmap(image)
#         self.setScaledContents(True)
#         if self.max_width * height_width_ratio < self.max_height:
#             self.scaled_shape = [int(round(self.max_width * height_width_ratio)), self.max_width]
#         else:
#             self.scaled_shape = [self.max_height, int(round(self.max_height / height_width_ratio))]
#         self.setMaximumHeight(self.scaled_shape[0])
#         self.setMaximumWidth(self.scaled_shape[1])
#
#         if text is not None:
#             pass
#         self.setPixmap(QPixmap(image))
#
#     def update_image_scaling_factors(self):
#         self.scaling_factors = (self.true_shape[0] / self.scaled_shape[0]), (self.true_shape[1] / self.scaled_shape[1])


# class FullScreenImage(QtWidgets.QLabel):
#     def __init__(self, image, screen_height, screen_width):
#         super().__init__()
#         self.true_shape = image.shape
#         self.max_height = screen_height
#         self.max_width = screen_width
#         self.im_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
#                                                     QtWidgets.QSizePolicy.MinimumExpanding)
#         self.setSizePolicy(self.im_size_policy)
#
#         height_width_ratio = image.shape[0] / image.shape[1]
#         image = cvtColor(image, COLOR_BGR2RGB)
#         image = QImage(image.data, image.shape[1], image.shape[0], 3 * image.shape[1], QImage.Format_RGB888)
#         image = QPixmap(image)
#         self.setScaledContents(True)
#         if self.max_width * height_width_ratio < self.max_height:
#             self.scaled_shape = [round(self.max_width * height_width_ratio), self.max_width]
#         else:
#             self.scaled_shape = [self.max_height, round(self.max_height / height_width_ratio)]
#         self.setMinimumSize(self.scaled_shape[1], self.scaled_shape[0])
#         self.setPixmap(QPixmap(image))
#         self.adjustSize()
#
