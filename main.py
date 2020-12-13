import os
import sys
import platform
import os.path
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sympy as sp
from scipy import integrate
from scipy.optimize import fsolve
import math
from math import sin, cos, tan, exp, log, log10
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(900, 760)
                MainWindow.setMaximumSize(QtCore.QSize(900, 760))
                self.Main = QtWidgets.QWidget(MainWindow)
                self.Main.setMinimumSize(QtCore.QSize(900, 760))
                font = QtGui.QFont()
                font.setFamily("Microsoft JhengHei")
                self.Main.setFont(font)
                self.Main.setObjectName("Main")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.Main)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.Top_bar = QtWidgets.QFrame(self.Main)
                self.Top_bar.setMaximumSize(QtCore.QSize(16777215, 64))
                self.Top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Top_bar.setObjectName("Top_bar")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_bar)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.Top_Left_menu = QtWidgets.QFrame(self.Top_bar)
                self.Top_Left_menu.setMinimumSize(QtCore.QSize(0, 0))
                self.Top_Left_menu.setMaximumSize(QtCore.QSize(128, 16777215))
                self.Top_Left_menu.setStyleSheet("background-color: rgb(40,40,40);\n"
        "border:0px solid;")
                self.Top_Left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Top_Left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Top_Left_menu.setObjectName("Top_Left_menu")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Top_Left_menu)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.Menu_button = QtWidgets.QPushButton(self.Top_Left_menu)
                self.Menu_button.setMinimumSize(QtCore.QSize(128, 64))
                self.Menu_button.setStyleSheet("\n"
        "\n"
        "QPushButton {\n"
        "    border-style: outset;\n"
        "border: 0px solid; \n"
        "color:white;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "}\n"
        "")
                self.Menu_button.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/list-white-g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Menu_button.setIcon(icon)
                self.Menu_button.setIconSize(QtCore.QSize(26, 26))
                self.Menu_button.setObjectName("Menu_button")
                self.horizontalLayout_2.addWidget(self.Menu_button)
                self.horizontalLayout.addWidget(self.Top_Left_menu)
                self.Top_Right_menu = QtWidgets.QFrame(self.Top_bar)
                font.setFamily("Microsoft JhengHei")
                self.Top_Right_menu.setFont(font)
                self.Top_Right_menu.setStyleSheet("background-color: rgb(40,40,40);")
                self.Top_Right_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Top_Right_menu.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Top_Right_menu.setObjectName("Top_Right_menu")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Top_Right_menu)
                self.verticalLayout_2.setContentsMargins(32, 12, 32, 12)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.Top_right_title = QtWidgets.QFrame(self.Top_Right_menu)
                self.Top_right_title.setMaximumSize(QtCore.QSize(700, 16777215))
                self.Top_right_title.setStyleSheet("")
                self.Top_right_title.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Top_right_title.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Top_right_title.setObjectName("Top_right_title")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Top_right_title)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setSpacing(0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.stackedWidget_2 = QtWidgets.QStackedWidget(self.Top_right_title)
                self.stackedWidget_2.setObjectName("stackedWidget_2")
                self.Home_title = QtWidgets.QWidget()
                self.Home_title.setObjectName("Home_title")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Home_title)
                self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_7.setSpacing(0)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.Home_title_label = QtWidgets.QLabel(self.Home_title)
                self.Home_title_label.setFont(font)
                self.Home_title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;")
                self.Home_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Home_title_label.setObjectName("Home_title_label")
                self.verticalLayout_7.addWidget(self.Home_title_label)
                self.stackedWidget_2.addWidget(self.Home_title)
                self.Derivative_title = QtWidgets.QWidget()
                self.Derivative_title.setObjectName("Derivative_title")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Derivative_title)
                self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_8.setSpacing(0)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.Derivative_label = QtWidgets.QLabel(self.Derivative_title)
                self.Derivative_label.setFont(font)
                self.Derivative_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;")
                self.Derivative_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Derivative_label.setObjectName("Derivative_label")
                self.verticalLayout_8.addWidget(self.Derivative_label)
                self.stackedWidget_2.addWidget(self.Derivative_title)
                self.Integral = QtWidgets.QWidget()
                self.Integral.setObjectName("Integral")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Integral)
                self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_10.setSpacing(0)
                self.verticalLayout_10.setObjectName("verticalLayout_10")
                self.Integral_label = QtWidgets.QLabel(self.Integral)
                self.Integral_label.setFont(font)
                self.Integral_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;")
                self.Integral_label.setMidLineWidth(0)
                self.Integral_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Integral_label.setObjectName("Integral_label")
                self.verticalLayout_10.addWidget(self.Integral_label)
                self.stackedWidget_2.addWidget(self.Integral)
                self.d_Integral_title = QtWidgets.QWidget()
                self.d_Integral_title.setObjectName("d_Integral_title")
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.d_Integral_title)
                self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_11.setSpacing(0)
                self.verticalLayout_11.setObjectName("verticalLayout_11")
                self.d_integral_title_label = QtWidgets.QLabel(self.d_Integral_title)
                self.d_integral_title_label.setFont(font)
                self.d_integral_title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;")
                self.d_integral_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.d_integral_title_label.setObjectName("d_integral_title_label")
                self.verticalLayout_11.addWidget(self.d_integral_title_label)
                self.stackedWidget_2.addWidget(self.d_Integral_title)
                self.c_Integral_title = QtWidgets.QWidget()
                self.c_Integral_title.setObjectName("c_Integral_title")
                self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.c_Integral_title)
                self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_12.setSpacing(0)
                self.verticalLayout_12.setObjectName("verticalLayout_12")
                self.c_integral_title_label = QtWidgets.QLabel(self.c_Integral_title)
                self.c_integral_title_label.setFont(font)
                self.c_integral_title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;")
                self.c_integral_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.c_integral_title_label.setObjectName("c_integral_title_label")
                self.verticalLayout_12.addWidget(self.c_integral_title_label)
                self.stackedWidget_2.addWidget(self.c_Integral_title)
                self.Plot_title = QtWidgets.QWidget()
                self.Plot_title.setObjectName("Plot_title")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Plot_title)
                self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_9.setSpacing(0)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.Plot_title_label = QtWidgets.QLabel(self.Plot_title)
                self.Plot_title_label.setFont(font)
                self.Plot_title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;")
                self.Plot_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.Plot_title_label.setObjectName("Plot_title_label")
                self.verticalLayout_9.addWidget(self.Plot_title_label)
                self.stackedWidget_2.addWidget(self.Plot_title)
                self.delta_title = QtWidgets.QWidget()
                self.delta_title.setObjectName("delta_title")
                self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.delta_title)
                self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_13.setSpacing(0)
                self.verticalLayout_13.setObjectName("verticalLayout_13")
                self.delta_title_label = QtWidgets.QLabel(self.delta_title)
                self.delta_title_label.setFont(font)
                self.delta_title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;")
                self.delta_title_label.setAlignment(QtCore.Qt.AlignCenter)
                self.delta_title_label.setObjectName("delta_title_label")
                self.verticalLayout_13.addWidget(self.delta_title_label)
                self.stackedWidget_2.addWidget(self.delta_title)
                self.horizontalLayout_3.addWidget(self.stackedWidget_2)
                self.verticalLayout_2.addWidget(self.Top_right_title)
                self.horizontalLayout.addWidget(self.Top_Right_menu)
                self.verticalLayout.addWidget(self.Top_bar)
                self.Bottom_bar = QtWidgets.QFrame(self.Main)
                self.Bottom_bar.setStyleSheet("border:0px solid;")
                self.Bottom_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Bottom_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Bottom_bar.setObjectName("Bottom_bar")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Bottom_bar)
                self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_4.setSpacing(0)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.Bottom_left_icons_out = QtWidgets.QFrame(self.Bottom_bar)
                self.Bottom_left_icons_out.setMinimumSize(QtCore.QSize(128, 0))
                self.Bottom_left_icons_out.setMaximumSize(QtCore.QSize(128, 16777215))
                self.Bottom_left_icons_out.setStyleSheet("background-color: rgb(60,60,60);")
                self.Bottom_left_icons_out.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Bottom_left_icons_out.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Bottom_left_icons_out.setObjectName("Bottom_left_icons_out")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Bottom_left_icons_out)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.Bottom_left_icons_in = QtWidgets.QFrame(self.Bottom_left_icons_out)
                self.Bottom_left_icons_in.setMinimumSize(QtCore.QSize(72, 0))
                self.Bottom_left_icons_in.setMaximumSize(QtCore.QSize(72, 16777215))
                self.Bottom_left_icons_in.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Bottom_left_icons_in.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Bottom_left_icons_in.setObjectName("Bottom_left_icons_in")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Bottom_left_icons_in)
                self.verticalLayout_4.setContentsMargins(0, 24, 0, 24)
                self.verticalLayout_4.setSpacing(24)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.Home_icon = QtWidgets.QFrame(self.Bottom_left_icons_in)
                self.Home_icon.setMinimumSize(QtCore.QSize(72, 72))
                self.Home_icon.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Home_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Home_icon.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_icon.setObjectName("Home_icon")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Home_icon)
                self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_5.setSpacing(0)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.Home_btn = QtWidgets.QPushButton(self.Home_icon)
                self.Home_btn.setMinimumSize(QtCore.QSize(72, 72))
                self.Home_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Home_btn.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("icons/Home-white-g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Home_btn.setIcon(icon1)
                self.Home_btn.setIconSize(QtCore.QSize(64, 64))
                self.Home_btn.setObjectName("Home_btn")
                self.verticalLayout_5.addWidget(self.Home_btn)
                self.verticalLayout_4.addWidget(self.Home_icon)
                self.Plot_icon = QtWidgets.QFrame(self.Bottom_left_icons_in)
                self.Plot_icon.setMinimumSize(QtCore.QSize(72, 72))
                self.Plot_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Plot_icon.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_icon.setObjectName("Plot_icon")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Plot_icon)
                self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_5.setSpacing(0)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.Plot_btn = QtWidgets.QPushButton(self.Plot_icon)
                self.Plot_btn.setMinimumSize(QtCore.QSize(72, 72))
                self.Plot_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Plot_btn.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("icons/plot-white-g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Plot_btn.setIcon(icon2)
                self.Plot_btn.setIconSize(QtCore.QSize(64, 64))
                self.Plot_btn.setObjectName("Plot_btn")
                self.horizontalLayout_5.addWidget(self.Plot_btn)
                self.verticalLayout_4.addWidget(self.Plot_icon)
                self.Derviate_icon = QtWidgets.QFrame(self.Bottom_left_icons_in)
                self.Derviate_icon.setMinimumSize(QtCore.QSize(72, 72))
                self.Derviate_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Derviate_icon.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Derviate_icon.setObjectName("Derviate_icon")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Derviate_icon)
                self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_6.setSpacing(0)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.Derviate_btn = QtWidgets.QPushButton(self.Derviate_icon)
                self.Derviate_btn.setMinimumSize(QtCore.QSize(72, 72))
                self.Derviate_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Derviate_btn.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("icons/poch-white-g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Derviate_btn.setIcon(icon3)
                self.Derviate_btn.setIconSize(QtCore.QSize(64, 64))
                self.Derviate_btn.setObjectName("Derviate_btn")
                self.horizontalLayout_6.addWidget(self.Derviate_btn)
                self.verticalLayout_4.addWidget(self.Derviate_icon)
                self.Integral_1st_icon = QtWidgets.QFrame(self.Bottom_left_icons_in)
                self.Integral_1st_icon.setMinimumSize(QtCore.QSize(72, 72))
                self.Integral_1st_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Integral_1st_icon.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Integral_1st_icon.setObjectName("Integral_1st_icon")
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Integral_1st_icon)
                self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_7.setSpacing(0)
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.Integral_1st_btn = QtWidgets.QPushButton(self.Integral_1st_icon)
                self.Integral_1st_btn.setMinimumSize(QtCore.QSize(72, 72))
                self.Integral_1st_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Integral_1st_btn.setText("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("icons/Calka1-white-g.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Integral_1st_btn.setIcon(icon4)
                self.Integral_1st_btn.setIconSize(QtCore.QSize(64, 64))
                self.Integral_1st_btn.setObjectName("Integral_1st_btn")
                self.horizontalLayout_7.addWidget(self.Integral_1st_btn)
                self.verticalLayout_4.addWidget(self.Integral_1st_icon)
                self.Integral_2x_icon = QtWidgets.QFrame(self.Bottom_left_icons_in)
                self.Integral_2x_icon.setMinimumSize(QtCore.QSize(70, 70))
                self.Integral_2x_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Integral_2x_icon.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Integral_2x_icon.setObjectName("Integral_2x_icon")
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Integral_2x_icon)
                self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_8.setSpacing(0)
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                self.Integral_2x_btn = QtWidgets.QPushButton(self.Integral_2x_icon)
                self.Integral_2x_btn.setMinimumSize(QtCore.QSize(72, 72))
                self.Integral_2x_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Integral_2x_btn.setText("")
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("icons/Calka2x-white-g.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Integral_2x_btn.setIcon(icon5)
                self.Integral_2x_btn.setIconSize(QtCore.QSize(64, 64))
                self.Integral_2x_btn.setObjectName("Integral_2x_btn")
                self.horizontalLayout_8.addWidget(self.Integral_2x_btn)
                self.verticalLayout_4.addWidget(self.Integral_2x_icon)
                self.Integral_curved_plot = QtWidgets.QFrame(self.Bottom_left_icons_in)
                self.Integral_curved_plot.setMinimumSize(QtCore.QSize(72, 72))
                self.Integral_curved_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Integral_curved_plot.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Integral_curved_plot.setObjectName("Integral_curved_plot")
                self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Integral_curved_plot)
                self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_9.setSpacing(0)
                self.horizontalLayout_9.setObjectName("horizontalLayout_9")
                self.Integral_curved_btn = QtWidgets.QPushButton(self.Integral_curved_plot)
                self.Integral_curved_btn.setMinimumSize(QtCore.QSize(72, 72))
                self.Integral_curved_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Integral_curved_btn.setText("")
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("icons/Calka3x-white-g.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Integral_curved_btn.setIcon(icon6)
                self.Integral_curved_btn.setIconSize(QtCore.QSize(64, 64))
                self.Integral_curved_btn.setShortcut("")
                self.Integral_curved_btn.setObjectName("Integral_curved_btn")
                self.horizontalLayout_9.addWidget(self.Integral_curved_btn)
                self.verticalLayout_4.addWidget(self.Integral_curved_plot)
                self.Delta_plot = QtWidgets.QFrame(self.Bottom_left_icons_in)
                self.Delta_plot.setMinimumSize(QtCore.QSize(72, 72))
                self.Delta_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Delta_plot.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Delta_plot.setObjectName("Delta_plot")
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Delta_plot)
                self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_10.setSpacing(0)
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                self.Delta_plot_btn = QtWidgets.QPushButton(self.Delta_plot)
                self.Delta_plot_btn.setMinimumSize(QtCore.QSize(72, 72))
                self.Delta_plot_btn.setStyleSheet("QPushButton {\n"
        "    border-radius: 32px;\n"
        "    border-style: outset;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }\n"
        "")
                self.Delta_plot_btn.setText("")
                icon7 = QtGui.QIcon()
                icon7.addPixmap(QtGui.QPixmap("icons/delta-white-g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.Delta_plot_btn.setIcon(icon7)
                self.Delta_plot_btn.setIconSize(QtCore.QSize(64, 64))
                self.Delta_plot_btn.setObjectName("Delta_plot_btn")
                self.horizontalLayout_10.addWidget(self.Delta_plot_btn)
                self.verticalLayout_4.addWidget(self.Delta_plot)
                self.verticalLayout_3.addWidget(self.Bottom_left_icons_in, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                self.horizontalLayout_4.addWidget(self.Bottom_left_icons_out)
                self.Bottom_right_content_out = QtWidgets.QFrame(self.Bottom_bar)
                self.Bottom_right_content_out.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.Bottom_right_content_out.setStyleSheet("background-color: rgb(60,60,60);\n"
        "border-left: 2px solid;\n"
        "border-left-color: rgb(60,60,60);")
                self.Bottom_right_content_out.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Bottom_right_content_out.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Bottom_right_content_out.setObjectName("Bottom_right_content_out")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Bottom_right_content_out)
                self.verticalLayout_6.setContentsMargins(30, 30, 30, 5)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.Bottom_right_content_in = QtWidgets.QFrame(self.Bottom_right_content_out)
                self.Bottom_right_content_in.setStyleSheet("border:0px solid;")
                self.Bottom_right_content_in.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.Bottom_right_content_in.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Bottom_right_content_in.setObjectName("Bottom_right_content_in")
                self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.Bottom_right_content_in)
                self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_11.setSpacing(0)
                self.horizontalLayout_11.setObjectName("horizontalLayout_11")
                self.stackedWidget = QtWidgets.QStackedWidget(self.Bottom_right_content_in)
                self.stackedWidget.setEnabled(True)
                self.stackedWidget.setMaximumSize(QtCore.QSize(800, 16777215))
                self.stackedWidget.setFont(font)
                self.stackedWidget.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
                self.stackedWidget.setObjectName("stackedWidget")
                self.Home_content = QtWidgets.QWidget()
                self.Home_content.setFont(font)
                self.Home_content.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size:22px;")
                self.Home_content.setObjectName("Home_content")
                self.Home_label_2 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_2.setGeometry(QtCore.QRect(0, 40, 800, 121))
                self.Home_label_2.setMaximumSize(QtCore.QSize(700, 200))
                self.Home_label_2.setFont(font)
                self.Home_label_2.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_2.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_2.setScaledContents(False)
                self.Home_label_2.setWordWrap(True)
                self.Home_label_2.setObjectName("Home_label_2")
                self.Home_label_1 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_1.setGeometry(QtCore.QRect(0, 0, 321, 33))
                self.Home_label_1.setMaximumSize(QtCore.QSize(16777215, 50))
                self.Home_label_1.setFont(font)
                self.Home_label_1.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;\n"
        "")
                self.Home_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Home_label_1.setObjectName("Home_label_1")
                self.Home_label_3 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_3.setGeometry(QtCore.QRect(0, 200, 621, 33))
                self.Home_label_3.setMaximumSize(QtCore.QSize(16777215, 50))
                self.Home_label_3.setFont(font)
                self.Home_label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;\n"
        "")
                self.Home_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Home_label_3.setObjectName("Home_label_3")
                self.Home_label_4 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_4.setGeometry(QtCore.QRect(0, 240, 700, 30))
                self.Home_label_4.setMaximumSize(QtCore.QSize(700, 100))
                self.Home_label_4.setFont(font)
                self.Home_label_4.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_4.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_4.setScaledContents(False)
                self.Home_label_4.setWordWrap(True)
                self.Home_label_4.setObjectName("Home_label_4")
                self.Home_label_5 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_5.setGeometry(QtCore.QRect(0, 270, 700, 30))
                self.Home_label_5.setMaximumSize(QtCore.QSize(700, 100))
                self.Home_label_5.setFont(font)
                self.Home_label_5.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_5.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_5.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_5.setScaledContents(False)
                self.Home_label_5.setWordWrap(True)
                self.Home_label_5.setObjectName("Home_label_5")
                self.Home_label_6 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_6.setGeometry(QtCore.QRect(0, 300, 700, 30))
                self.Home_label_6.setMaximumSize(QtCore.QSize(700, 100))
                self.Home_label_6.setFont(font)
                self.Home_label_6.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_6.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_6.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_6.setScaledContents(False)
                self.Home_label_6.setWordWrap(True)
                self.Home_label_6.setObjectName("Home_label_6")
                self.Home_label_7 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_7.setGeometry(QtCore.QRect(0, 330, 700, 30))
                self.Home_label_7.setMaximumSize(QtCore.QSize(700, 100))
                self.Home_label_7.setFont(font)
                self.Home_label_7.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_7.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_7.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_7.setScaledContents(False)
                self.Home_label_7.setWordWrap(True)
                self.Home_label_7.setObjectName("Home_label_7")
                self.Home_label_8 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_8.setGeometry(QtCore.QRect(0, 360, 700, 30))
                self.Home_label_8.setMaximumSize(QtCore.QSize(700, 100))
                self.Home_label_8.setFont(font)
                self.Home_label_8.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_8.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_8.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_8.setScaledContents(False)
                self.Home_label_8.setWordWrap(True)
                self.Home_label_8.setObjectName("Home_label_8")
                self.Home_label_9 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_9.setGeometry(QtCore.QRect(0, 390, 700, 30))
                self.Home_label_9.setMaximumSize(QtCore.QSize(700, 100))
                self.Home_label_9.setFont(font)
                self.Home_label_9.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_9.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_9.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_9.setScaledContents(False)
                self.Home_label_9.setWordWrap(True)
                self.Home_label_9.setObjectName("Home_label_9")
                self.Home_label_10 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_10.setGeometry(QtCore.QRect(0, 450, 321, 33))
                self.Home_label_10.setMaximumSize(QtCore.QSize(16777215, 50))
                self.Home_label_10.setFont(font)
                self.Home_label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 26px;\n"
        "")
                self.Home_label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Home_label_10.setObjectName("Home_label_10")
                self.Home_label_11 = QtWidgets.QLabel(self.Home_content)
                self.Home_label_11.setGeometry(QtCore.QRect(0, 490, 700, 51))
                self.Home_label_11.setMaximumSize(QtCore.QSize(700, 100))
                self.Home_label_11.setFont(font)
                self.Home_label_11.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Home_label_11.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Home_label_11.setTextFormat(QtCore.Qt.AutoText)
                self.Home_label_11.setScaledContents(False)
                self.Home_label_11.setWordWrap(True)
                self.Home_label_11.setObjectName("Home_label_11")
                self.stackedWidget.addWidget(self.Home_content)
                self.Integral_content = QtWidgets.QWidget()
                self.Integral_content.setObjectName("Integral_content")
                self.Integral_content.setStyleSheet('font-size:18px')
                self.Integral_main_label = QtWidgets.QLabel(self.Integral_content)
                self.Integral_main_label.setGeometry(QtCore.QRect(0, 0, 701, 191))
                self.Integral_main_label.setFont(font)
                self.Integral_main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Integral_main_label.setWordWrap(True)
                self.Integral_main_label.setObjectName("Integral_main_label")
                self.Integral_sign = QtWidgets.QPushButton(self.Integral_content)
                self.Integral_sign.setGeometry(QtCore.QRect(6, 315, 31, 71))
                self.Integral_sign.setText("")
                self.Integral_sign.setIcon(icon4)
                self.Integral_sign.setIconSize(QtCore.QSize(58, 58))
                self.Integral_sign.setObjectName("Integral_sign")
                self.Integral_label_fx = QtWidgets.QLabel(self.Integral_content)
                self.Integral_label_fx.setGeometry(QtCore.QRect(50, 200, 71, 31))
                self.Integral_label_fx.setFont(font)
                self.Integral_label_fx.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Integral_label_fx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Integral_label_fx.setObjectName("Integral_label_fx")
                self.Integral_input_value = QtWidgets.QLineEdit(self.Integral_content)
                self.Integral_input_value.setGeometry(QtCore.QRect(130, 200, 181, 31))
                self.Integral_input_value.setFont(font)
                self.Integral_input_value.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "outline: none;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Integral_input_value.setObjectName("Integral_input_value")
                self.Integral_label_fx_2 = QtWidgets.QLabel(self.Integral_content)
                self.Integral_label_fx_2.setGeometry(QtCore.QRect(48, 330, 81, 31))
                self.Integral_label_fx_2.setFont(font)
                self.Integral_label_fx_2.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Integral_label_fx_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.Integral_label_fx_2.setObjectName("Integral_label_fx_2")
                self.Integral_label_fxpr_res = QtWidgets.QLabel(self.Integral_content)
                self.Integral_label_fxpr_res.setGeometry(QtCore.QRect(130, 330, 181, 31))
                self.Integral_label_fxpr_res.setFont(font)
                self.Integral_label_fxpr_res.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Integral_label_fxpr_res.setText("")
                self.Integral_label_fxpr_res.setObjectName("Integral_label_fxpr_res")

                self.Integral_image_label_preview = QtWidgets.QLabel(self.Integral_content)
                self.Integral_image_label_preview.setGeometry(QtCore.QRect(410, 500, 271, 31))
                self.Integral_image_label_preview.setText('Preview calculated figure')
                self.Integral_image_label_preview.setFont(font)
                self.Integral_image_label_preview.setStyleSheet("font-size: 18px")
                self.Integral_image_label_preview.setObjectName('Integral_image_label_preview')
                

                self.Integral_image_frame_preview = QtWidgets.QFrame(self.Integral_content)
                self.Integral_image_frame_preview.setGeometry(QtCore.QRect(330, 160, 340, 340))
                self.Integral_image_frame_preview.setStyleSheet("border: 1px solid;\n"
        "border-color: rgb(90, 90, 90);")
                self.Integral_image_frame_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Integral_image_frame_preview.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Integral_image_frame_preview.setObjectName("Integral_image_frame_preview")

                self.Integral_image_label_preview_fig = QtWidgets.QLabel(self.Integral_image_frame_preview)
                self.Integral_image_label_preview_fig.setGeometry(QtCore.QRect(0,0,340,340))
                self.Integral_image_label_preview_fig.setText("")
                self.Integral_image_label_preview_fig.setScaledContents(True)
                self.Integral_image_label_preview_fig.setObjectName("Integral_image_label_preview_fig ")  

                self.Integral_BTN_compute = QtWidgets.QPushButton(self.Integral_content)
                self.Integral_BTN_compute.setGeometry(QtCore.QRect(100, 460, 131, 41))
                self.Integral_BTN_compute.setFont(font)
                self.Integral_BTN_compute.setStyleSheet("QPushButton {\n"
        "    border-radius: 16px;\n"
        "    border-style: outset;\n"
        "    color: white;\n"
        "    font-size: 22px;\n"
        "    border: 1px solid;\n"
        "    border-color: rgb(232, 232, 232);\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    color: black;\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }")
                self.Integral_BTN_compute.setObjectName("Integral_BTN_compute")

                ###

                self.Integral_plot_range = QtWidgets.QLabel(self.Integral_content)
                self.Integral_plot_range.setGeometry(QtCore.QRect(0, 245, 121, 61))
                self.Integral_plot_range.setFont(font)
                self.Integral_plot_range.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Integral_plot_range.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Integral_plot_range.setTextFormat(QtCore.Qt.AutoText)
                self.Integral_plot_range.setScaledContents(False)
                self.Integral_plot_range.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Integral_plot_range.setWordWrap(True)
                self.Integral_plot_range.setObjectName("Integral_plot_range")
                self.Integral_plot_range.setText('Integration area:')

                
                self.Integral_range_x1 = QtWidgets.QLineEdit(self.Integral_content)
                self.Integral_range_x1.setGeometry(QtCore.QRect(130, 260, 86, 36))
                self.Integral_range_x1.setFont(font)
                self.Integral_range_x1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Integral_range_x1.setObjectName("Integral_range_x1")
                
                self.Integral_range_x2 = QtWidgets.QLineEdit(self.Integral_content)
                self.Integral_range_x2.setGeometry(QtCore.QRect(220, 260, 86, 36))
                self.Integral_range_x2.setFont(font)
                self.Integral_range_x2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Integral_range_x2.setObjectName("Integral_range_x2")

                self.Integral_label_P = QtWidgets.QLabel(self.Integral_content)
                self.Integral_label_P.setGeometry(QtCore.QRect(50, 390, 71, 31))
                self.Integral_label_P.setFont(font)
                self.Integral_label_P.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Integral_label_P.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Integral_label_P.setObjectName("Integral_label_P")

                self.Integral_label_P_res = QtWidgets.QLabel(self.Integral_content)
                self.Integral_label_P_res.setGeometry(QtCore.QRect(130, 390, 181, 31))
                self.Integral_label_P_res.setFont(font)
                self.Integral_label_P_res.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Integral_label_P_res.setText("")
                self.Integral_label_P_res.setObjectName("Integral_label_P_res")

                ###
                self.stackedWidget_4 = QtWidgets.QStackedWidget(self.Integral_content)
                self.stackedWidget_4.setGeometry(QtCore.QRect(0, 510, 321, 61))
                self.stackedWidget_4.setFont(font)
                self.stackedWidget_4.setStyleSheet("color: rgb(253, 41, 41);\n"
        "font-size: 16px;")
                self.stackedWidget_4.setObjectName("stackedWidget_4")
                self.error_widget_6 = QtWidgets.QWidget()
                self.error_widget_6.setFont(font)
                self.error_widget_6.setObjectName("error_widget_6")
                self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.error_widget_6)
                self.horizontalLayout_18.setObjectName("horizontalLayout_18")
                self.error_label_6 = QtWidgets.QLabel(self.error_widget_6)
                self.error_label_6.setFont(font)
                self.error_label_6.setWordWrap(True)
                self.error_label_6.setObjectName("error_label_6")
                self.horizontalLayout_18.addWidget(self.error_label_6)
                self.stackedWidget_4.addWidget(self.error_widget_6)
                self.error_widget_7 = QtWidgets.QWidget()
                self.error_widget_7.setFont(font)
                self.error_widget_7.setObjectName("error_widget_7")
                self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.error_widget_7)
                self.horizontalLayout_19.setObjectName("horizontalLayout_19")
                self.error_label_7 = QtWidgets.QLabel(self.error_widget_7)
                self.error_label_7.setFont(font)
                self.error_label_7.setWordWrap(True)
                self.error_label_7.setObjectName("error_label_7")
                self.horizontalLayout_19.addWidget(self.error_label_7)
                self.stackedWidget_4.addWidget(self.error_widget_7)
                self.correct_widget_7 = QtWidgets.QWidget()
                self.correct_widget_7.setFont(font)
                self.correct_widget_7.setObjectName("correct_widget_7")
                self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.correct_widget_7)
                self.horizontalLayout_19.setObjectName("horizontalLayout_19")
                self.correct_label_7 = QtWidgets.QLabel(self.correct_widget_7)
                self.correct_label_7.setFont(font)
                self.correct_label_7.setWordWrap(True)
                self.correct_label_7.setStyleSheet('color:blue;')
                self.correct_label_7.setObjectName("correct_label_7")
                self.horizontalLayout_19.addWidget(self.correct_label_7)
                self.stackedWidget_4.addWidget(self.correct_widget_7)
                self.stackedWidget.addWidget(self.Integral_content)
                self.Plot_content = QtWidgets.QWidget()
                self.Plot_content.setEnabled(True)
                self.Plot_content.setFont(font)
                self.Plot_content.setObjectName("Plot_content")
                self.Plot_label_1 = QtWidgets.QLabel(self.Plot_content)
                self.Plot_label_1.setGeometry(QtCore.QRect(0, 20, 341, 91))
                self.Plot_label_1.setMaximumSize(QtCore.QSize(700, 200))
                self.Plot_label_1.setFont(font)
                self.Plot_label_1.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Plot_label_1.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_label_1.setTextFormat(QtCore.Qt.AutoText)
                self.Plot_label_1.setScaledContents(False)
                self.Plot_label_1.setWordWrap(True)
                self.Plot_label_1.setObjectName("Plot_label_1")
                self.Plot_frame = QtWidgets.QFrame(self.Plot_content)
                self.Plot_frame.setGeometry(QtCore.QRect(350, 0, 350, 350))
                self.Plot_frame.setStyleSheet("border: 1px solid;\n"
        "border-color: rgb(90, 90, 90);")
                self.Plot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Plot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_frame.setObjectName("Plot_frame")
                self.Plot_fn_edit = QtWidgets.QLineEdit(self.Plot_content)
                self.Plot_fn_edit.setGeometry(QtCore.QRect(130, 140, 141, 31))
                self.Plot_fn_edit.setFont(font)
                self.Plot_fn_edit.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Plot_fn_edit.setObjectName("Plot_fn_edit")
                self.Plot_fn_sign_label = QtWidgets.QLabel(self.Plot_content)
                self.Plot_fn_sign_label.setGeometry(QtCore.QRect(50, 135, 71, 41))
                self.Plot_fn_sign_label.setMaximumSize(QtCore.QSize(700, 200))
                self.Plot_fn_sign_label.setFont(font)
                self.Plot_fn_sign_label.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Plot_fn_sign_label.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_fn_sign_label.setTextFormat(QtCore.Qt.AutoText)
                self.Plot_fn_sign_label.setScaledContents(False)
                self.Plot_fn_sign_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Plot_fn_sign_label.setWordWrap(True)
                self.Plot_fn_sign_label.setObjectName("Plot_fn_sign_label")
                self.Plot_range_sign = QtWidgets.QLabel(self.Plot_content)
                self.Plot_range_sign.setGeometry(QtCore.QRect(35, 185, 81, 41))
                self.Plot_range_sign.setMaximumSize(QtCore.QSize(700, 200))
                self.Plot_range_sign.setFont(font)
                self.Plot_range_sign.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Plot_range_sign.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_range_sign.setTextFormat(QtCore.Qt.AutoText)
                self.Plot_range_sign.setScaledContents(False)
                self.Plot_range_sign.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Plot_range_sign.setWordWrap(True)
                self.Plot_range_sign.setObjectName("Plot_range_sign")
                self.Plot_range_x1 = QtWidgets.QLineEdit(self.Plot_content)
                self.Plot_range_x1.setGeometry(QtCore.QRect(130, 190, 61, 31))
                self.Plot_range_x1.setFont(font)
                self.Plot_range_x1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Plot_range_x1.setObjectName("Plot_range_x1")
                self.Plot_color_sign = QtWidgets.QLabel(self.Plot_content)
                self.Plot_color_sign.setGeometry(QtCore.QRect(25, 235, 91, 41))
                self.Plot_color_sign.setMaximumSize(QtCore.QSize(700, 200))
                self.Plot_color_sign.setFont(font)
                self.Plot_color_sign.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Plot_color_sign.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_color_sign.setTextFormat(QtCore.Qt.AutoText)
                self.Plot_color_sign.setScaledContents(False)
                self.Plot_color_sign.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Plot_color_sign.setWordWrap(True)
                self.Plot_color_sign.setObjectName("Plot_color_sign")
                self.Plot_range_x2 = QtWidgets.QLineEdit(self.Plot_content)
                self.Plot_range_x2.setGeometry(QtCore.QRect(210, 190, 61, 31))
                self.Plot_range_x2.setFont(font)
                self.Plot_range_x2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Plot_range_x2.setObjectName("Plot_range_x2")
                self.Plot_combo_color = QtWidgets.QComboBox(self.Plot_content)
                self.Plot_combo_color.setGeometry(QtCore.QRect(130, 240, 141, 31))
                self.Plot_combo_color.setFont(font)
                self.Plot_combo_color.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "border: 1px solid;\n"
        "border-color: rgb(200, 200, 200);\n"
        "border-radius: 15px;")
                self.Plot_combo_color.setObjectName("Plot_combo_color")
                self.Plot_combo_color.addItem("")
                self.Plot_combo_color.addItem("")
                self.Plot_combo_color.addItem("")
                self.Plot_combo_color.addItem("")
                self.Plot_combo_color.addItem("")
                self.Plot_combo_color.addItem("")
                self.Plot_BTN_generate = QtWidgets.QPushButton(self.Plot_content)
                self.Plot_BTN_generate.setGeometry(QtCore.QRect(110, 300, 131, 41))
                self.Plot_BTN_generate.setFont(font)
                self.Plot_BTN_generate.setStyleSheet("QPushButton {\n"
        "    border-radius: 16px;\n"
        "    border-style: outset;\n"
        "    color: white;\n"
        "    font-size: 22px;\n"
        "    \n"
        "    border: 1px solid;\n"
        "    border-color: rgb(232, 232, 232);\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    color: black;\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }")
                self.Plot_BTN_generate.setObjectName("Plot_BTN_generate")

                self.Plot_label_2 = QtWidgets.QLabel(self.Plot_content)
                self.Plot_label_2.setGeometry(QtCore.QRect(350, 350, 351, 21))
                self.Plot_label_2.setMaximumSize(QtCore.QSize(700, 200))
                self.Plot_label_2.setFont(font)
                self.Plot_label_2.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Plot_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_label_2.setTextFormat(QtCore.Qt.AutoText)
                self.Plot_label_2.setScaledContents(False)
                self.Plot_label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.Plot_label_2.setWordWrap(True)
                self.Plot_label_2.setObjectName("Plot_label_2")
                self.Plot_error_info = QtWidgets.QStackedWidget(self.Plot_content)
                self.Plot_error_info.setGeometry(QtCore.QRect(20, 370, 311, 51))
                self.Plot_error_info.setObjectName("Plot_error_info")
                self.error_widget_1 = QtWidgets.QWidget()
                self.error_widget_1.setObjectName("error_widget_1")
                self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.error_widget_1)
                self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_13.setSpacing(0)
                self.horizontalLayout_13.setObjectName("horizontalLayout_13")
                self.error_label_1 = QtWidgets.QLabel(self.error_widget_1)
                self.error_label_1.setFont(font)
                self.error_label_1.setStyleSheet("color: rgb(253, 41, 41);\n"
        "font-size: 16px;")
                self.error_label_1.setWordWrap(True)
                self.error_label_1.setObjectName("error_label_1")
                self.horizontalLayout_13.addWidget(self.error_label_1)
                self.Plot_error_info.addWidget(self.error_widget_1)
                self.error_widget_2 = QtWidgets.QWidget()
                self.error_widget_2.setObjectName("error_widget_2")
                self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.error_widget_2)
                self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_14.setSpacing(0)
                self.horizontalLayout_14.setObjectName("horizontalLayout_14")
                self.error_label_2 = QtWidgets.QLabel(self.error_widget_2)
                self.error_label_2.setFont(font)
                self.error_label_2.setStyleSheet("color: rgb(253, 41, 41);\n"
        "font-size: 16px;")
                self.error_label_2.setWordWrap(True)
                self.error_label_2.setObjectName("error_label_2")
                self.horizontalLayout_14.addWidget(self.error_label_2)
                self.Plot_error_info.addWidget(self.error_widget_2)
                self.Plot_figure_saved_widget = QtWidgets.QWidget()
                self.Plot_figure_saved_widget.setObjectName("Plot_figure_saved_widget")
                self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.Plot_figure_saved_widget)
                self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_15.setSpacing(0)
                self.horizontalLayout_15.setObjectName("horizontalLayout_15")
                self.Plot_figure_saved_label = QtWidgets.QLabel(self.Plot_figure_saved_widget)
                self.Plot_figure_saved_label.setFont(font)
                self.Plot_figure_saved_label.setStyleSheet("color: rgb(12, 158, 255);\n"
        "font-size: 16px;")
                self.Plot_figure_saved_label.setObjectName("Plot_figure_saved_label")
                self.horizontalLayout_15.addWidget(self.Plot_figure_saved_label)
                self.Plot_error_info.addWidget(self.Plot_figure_saved_widget)
                self.stackedWidget.addWidget(self.Plot_content)
                self.Derivative_centent = QtWidgets.QWidget()
                self.Derivative_centent.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Derivative_centent.setObjectName("Derivative_centent")
                self.Derivative_main_label = QtWidgets.QLabel(self.Derivative_centent)
                self.Derivative_main_label.setGeometry(QtCore.QRect(0, 0, 701, 141))
                self.Derivative_main_label.setFont(font)
                self.Derivative_main_label.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Derivative_main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Derivative_main_label.setWordWrap(True)
                self.Derivative_main_label.setObjectName("Derivative_main_label")
                self.Derivative_label_fx = QtWidgets.QLabel(self.Derivative_centent)
                self.Derivative_label_fx.setGeometry(QtCore.QRect(60, 160, 71, 31))
                self.Derivative_label_fx.setFont(font)
                self.Derivative_label_fx.setStyleSheet('font-size:18px;')
                self.Derivative_label_fx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Derivative_label_fx.setObjectName("Derivative_label_fx")
                self.Derivative_input_value = QtWidgets.QLineEdit(self.Derivative_centent)
                self.Derivative_input_value.setGeometry(QtCore.QRect(140, 160, 111, 31))
                self.Derivative_input_value.setFont(font)
                self.Derivative_input_value.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Derivative_input_value.setObjectName("Derivative_input_value")
                self.Derivative_label_fxpr = QtWidgets.QLabel(self.Derivative_centent)
                self.Derivative_label_fxpr.setGeometry(QtCore.QRect(60, 220, 71, 31))
                self.Derivative_label_fxpr.setStyleSheet('font-size:18px;')
                self.Derivative_label_fxpr.setFont(font)
                self.Derivative_label_fxpr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Derivative_label_fxpr.setObjectName("Derivative_label_fxpr")
                self.Derivative_label_fxpr_res = QtWidgets.QLabel(self.Derivative_centent)
                self.Derivative_label_fxpr_res.setGeometry(QtCore.QRect(140, 220, 111, 31))
                self.Derivative_label_fxpr_res.setFont(font)
                self.Derivative_label_fxpr_res.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Derivative_label_fxpr_res.setText("")
                self.Derivative_label_fxpr_res.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Derivative_label_fxpr_res.setObjectName("Derivative_label_fxpr_res")
                self.Derivative_sign = QtWidgets.QPushButton(self.Derivative_centent)
                self.Derivative_sign.setGeometry(QtCore.QRect(65, 205, 50, 58))
                self.Derivative_sign.setText('')
                self.Derivative_sign.setIcon(icon3)
                self.Derivative_sign.setIconSize(QtCore.QSize(48, 48))
                self.Derivative_sign.setObjectName('Derivative_dxdy_operator')


                self.Derivative_BTN_compute = QtWidgets.QPushButton(self.Derivative_centent)
                self.Derivative_BTN_compute.setGeometry(QtCore.QRect(100, 350, 141, 41))
                self.Derivative_BTN_compute.setFont(font)
                self.Derivative_BTN_compute.setStyleSheet("QPushButton {\n"
        "    border-radius: 16px;\n"
        "    border-style: outset;\n"
        "    color: white;\n"
        "    font-size: 22px;\n"
        "    border: 1px solid;\n"
        "    border-color: rgb(232, 232, 232);\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    color: black;\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }")
                self.Derivative_BTN_compute.setObjectName("Derivative_BTN_compute")


                self.Derivative_image_preview_dxdy = QtWidgets.QLabel(self.Derivative_centent)
                self.Derivative_image_preview_dxdy.setGeometry(QtCore.QRect(410, 460, 271, 31))
                self.Derivative_image_preview_dxdy.setText('Preview calculated figure')
                self.Derivative_image_preview_dxdy.setFont(font)
                self.Derivative_image_preview_dxdy.setStyleSheet("font-size: 18px")
                self.Derivative_image_preview_dxdy.setObjectName('Derivative_image_preview_dxdy')
                

                self.Derivative_frame_dxdy = QtWidgets.QFrame(self.Derivative_centent)
                self.Derivative_frame_dxdy.setGeometry(QtCore.QRect(330, 120, 340, 340))
                self.Derivative_frame_dxdy.setStyleSheet("border: 1px solid;\n"
        "border-color: rgb(90, 90, 90);")
                self.Derivative_frame_dxdy.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Derivative_frame_dxdy.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Derivative_frame_dxdy.setObjectName("Derivative_frame_dxdy")
                
                self.Derivative_plot_range = QtWidgets.QLabel(self.Derivative_centent)
                self.Derivative_plot_range.setGeometry(QtCore.QRect(50, 275, 81, 41))
                self.Derivative_plot_range.setFont(font)
                self.Derivative_plot_range.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Derivative_plot_range.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Derivative_plot_range.setTextFormat(QtCore.Qt.AutoText)
                self.Derivative_plot_range.setScaledContents(False)
                self.Derivative_plot_range.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Derivative_plot_range.setWordWrap(True)
                self.Derivative_plot_range.setObjectName("Derivative_plot_range")
                self.Derivative_plot_range.setText('Range:')

                
                self.Derivative_range_x1 = QtWidgets.QLineEdit(self.Derivative_centent)
                self.Derivative_range_x1.setGeometry(QtCore.QRect(140, 282, 61, 31))
                self.Derivative_range_x1.setFont(font)
                self.Derivative_range_x1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Derivative_range_x1.setObjectName("Derivative_range_x1")
                
                self.Derivative_range_x2 = QtWidgets.QLineEdit(self.Derivative_centent)
                self.Derivative_range_x2.setGeometry(QtCore.QRect(210, 282, 61, 31))
                self.Derivative_range_x2.setFont(font)
                self.Derivative_range_x2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Derivative_range_x2.setObjectName("Derivative_range_x2")





                self.stackedWidget_3 = QtWidgets.QStackedWidget(self.Derivative_centent)
                self.stackedWidget_3.setGeometry(QtCore.QRect(0, 400, 321, 81))
                self.stackedWidget_3.setStyleSheet("color: rgb(253, 41, 41);\n"
        "font-size: 16px;")
                self.stackedWidget_3.setObjectName("stackedWidget_3")


                self.error_widget_4 = QtWidgets.QWidget()
                self.error_widget_4.setObjectName("error_widget_4")
                self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.error_widget_4)
                self.horizontalLayout_16.setObjectName("horizontalLayout_16")
                self.error_label_4 = QtWidgets.QLabel(self.error_widget_4)
                self.error_label_4.setMaximumSize(QtCore.QSize(500, 16777215))
                self.error_label_4.setFont(font)
                self.error_label_4.setWordWrap(True)
                self.error_label_4.setObjectName("error_label_4")
                self.horizontalLayout_16.addWidget(self.error_label_4)
                self.stackedWidget_3.addWidget(self.error_widget_4)

                self.correct_widget_4 = QtWidgets.QWidget()
                self.correct_widget_4.setObjectName("correct_widget_4")
                self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.correct_widget_4)
                self.horizontalLayout_16.setObjectName("horizontalLayout_16")
                self.correct_label_4 = QtWidgets.QLabel(self.correct_widget_4)
                self.correct_label_4.setMaximumSize(QtCore.QSize(500, 16777215))
                self.correct_label_4.setStyleSheet('color: Blue;')
                self.correct_label_4.setFont(font)
                self.correct_label_4.setWordWrap(True)
                self.correct_label_4.setObjectName("correct_label_4")
                self.horizontalLayout_16.addWidget(self.correct_label_4)
                self.stackedWidget_3.addWidget(self.correct_widget_4)


                self.error_widget_5 = QtWidgets.QWidget()
                self.error_widget_5.setObjectName("error_widget_5")
                self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.error_widget_5)
                self.horizontalLayout_17.setObjectName("horizontalLayout_17")
                self.error_label_5 = QtWidgets.QLabel(self.error_widget_5)
                self.error_label_5.setFont(font)
                self.error_label_5.setWordWrap(True)
                self.error_label_5.setObjectName("error_label_5")
                self.horizontalLayout_17.addWidget(self.error_label_5)
                self.stackedWidget_3.addWidget(self.error_widget_5)
                self.stackedWidget.addWidget(self.Derivative_centent)
                self.d_Integral_content = QtWidgets.QWidget()
                self.d_Integral_content.setObjectName("d_Integral_content")
                self.d_Integral_main_label = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_main_label.setGeometry(QtCore.QRect(0, 0, 701, 91))
                self.d_Integral_main_label.setFont(font)
                self.d_Integral_main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.d_Integral_main_label.setWordWrap(True)
                self.d_Integral_main_label.setObjectName("d_Integral_main_label")
                self.d_Integral_label_fx = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_label_fx.setGeometry(QtCore.QRect(50, 280, 141, 31))
                self.d_Integral_label_fx.setFont(font)
                self.d_Integral_label_fx.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.d_Integral_label_fx.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.d_Integral_label_fx.setObjectName("d_Integral_label_fx")
                self.d_Integral_label_fxpr_res = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_label_fxpr_res.setGeometry(QtCore.QRect(160, 280, 151, 31))
                self.d_Integral_label_fxpr_res.setFont(font)
                self.d_Integral_label_fxpr_res.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.d_Integral_label_fxpr_res.setText("")
                self.d_Integral_label_fxpr_res.setObjectName("d_Integral_label_fxpr_res")
                self.d_Integral_sign = QtWidgets.QPushButton(self.d_Integral_content)
                self.d_Integral_sign.setGeometry(QtCore.QRect(0, 260, 41, 71))
                self.d_Integral_sign.setText("")
                self.d_Integral_sign.setIcon(icon5)
                self.d_Integral_sign.setIconSize(QtCore.QSize(64, 64))
                self.d_Integral_sign.setObjectName("d_Integral_sign")
                self.d_Integral_label_fx_2 = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_label_fx_2.setGeometry(QtCore.QRect(30, 130, 91, 31))
                self.d_Integral_label_fx_2.setFont(font)
                self.d_Integral_label_fx_2.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.d_Integral_label_fx_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.d_Integral_label_fx_2.setObjectName("d_Integral_label_fx_2")
                self.d_Integral_input_value = QtWidgets.QLineEdit(self.d_Integral_content)
                self.d_Integral_input_value.setGeometry(QtCore.QRect(130, 130, 181, 31))
                self.d_Integral_input_value.setFont(font)
                self.d_Integral_input_value.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.d_Integral_input_value.setObjectName("d_Integral_input_value")
                self.d_Integral_BTN_compute = QtWidgets.QPushButton(self.d_Integral_content)
                self.d_Integral_BTN_compute.setGeometry(QtCore.QRect(100, 410, 131, 41))
                self.d_Integral_BTN_compute.setFont(font)
                self.d_Integral_BTN_compute.setStyleSheet("QPushButton {\n"
        "    border-radius: 16px;\n"
        "    border-style: outset;\n"
        "    color: white;\n"
        "    font-size: 22px;\n"
        "    border: 1px solid;\n"
        "    border-color: rgb(232, 232, 232);\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    color: black;\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }")
                self.d_Integral_BTN_compute.setObjectName("d_Integral_BTN_compute")

                self.d_Integral_plot_range = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_plot_range.setGeometry(QtCore.QRect(0, 185, 121, 61))
                self.d_Integral_plot_range.setFont(font)
                self.d_Integral_plot_range.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.d_Integral_plot_range.setFrameShadow(QtWidgets.QFrame.Raised)
                self.d_Integral_plot_range.setTextFormat(QtCore.Qt.AutoText)
                self.d_Integral_plot_range.setScaledContents(False)
                self.d_Integral_plot_range.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.d_Integral_plot_range.setWordWrap(True)
                self.d_Integral_plot_range.setObjectName("d_Integral_plot_range")
                self.d_Integral_plot_range.setText('Integration area:')

                
                self.d_Integral_range_x1 = QtWidgets.QLineEdit(self.d_Integral_content)
                self.d_Integral_range_x1.setGeometry(QtCore.QRect(130, 180, 91, 31))
                self.d_Integral_range_x1.setFont(font)
                self.d_Integral_range_x1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.d_Integral_range_x1.setObjectName("d_Integral_range_x1")
                
                self.d_Integral_range_x2 = QtWidgets.QLineEdit(self.d_Integral_content)
                self.d_Integral_range_x2.setGeometry(QtCore.QRect(230, 180, 91, 31))
                self.d_Integral_range_x2.setFont(font)
                self.d_Integral_range_x2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.d_Integral_range_x2.setObjectName("d_Integral_range_x2")

                self.d_Integral_range_y1 = QtWidgets.QLineEdit(self.d_Integral_content)
                self.d_Integral_range_y1.setGeometry(QtCore.QRect(130, 220, 91, 31))
                self.d_Integral_range_y1.setFont(font)
                self.d_Integral_range_y1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.d_Integral_range_y1.setObjectName("d_Integral_range_y1")
                
                self.d_Integral_range_y2 = QtWidgets.QLineEdit(self.d_Integral_content)
                self.d_Integral_range_y2.setGeometry(QtCore.QRect(230, 220, 91, 31))
                self.d_Integral_range_y2.setFont(font)
                self.d_Integral_range_y2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.d_Integral_range_y2.setObjectName("d_Integral_range_y2")

                self.d_Integral_label_P = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_label_P.setGeometry(QtCore.QRect(40, 340, 81, 31))
                self.d_Integral_label_P.setFont(font)
                self.d_Integral_label_P.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.d_Integral_label_P.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.d_Integral_label_P.setObjectName("d_Integral_label_P")

                self.d_Integral_label_P_res = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_label_P_res.setGeometry(QtCore.QRect(130, 340, 181, 31))
                self.d_Integral_label_P_res.setFont(font)
                self.d_Integral_label_P_res.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.d_Integral_label_P_res.setText("")
                self.d_Integral_label_P_res.setObjectName("d_Integral_label_P_res")

                self.d_Integral_image_frame_preview = QtWidgets.QFrame(self.d_Integral_content)
                self.d_Integral_image_frame_preview.setGeometry(QtCore.QRect(330, 110, 340, 340))
                self.d_Integral_image_frame_preview.setStyleSheet("border: 1px solid;\n"
        "border-color: rgb(90, 90, 90);")
                self.d_Integral_image_frame_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.d_Integral_image_frame_preview.setFrameShadow(QtWidgets.QFrame.Raised)
                self.d_Integral_image_frame_preview.setObjectName("d_Integral_image_frame_preview")

                self.d_Integral_image_label_preview_fig = QtWidgets.QLabel(self.d_Integral_image_frame_preview)
                self.d_Integral_image_label_preview_fig.setGeometry(QtCore.QRect(0,0,340,340))
                self.d_Integral_image_label_preview_fig.setText("")
                self.d_Integral_image_label_preview_fig.setScaledContents(True)
                self.d_Integral_image_label_preview_fig.setObjectName("d_Integral_image_label_preview_fig ")  

                self.d_Integral_image_label_preview = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_image_label_preview.setGeometry(QtCore.QRect(410, 450, 271, 31))
                self.d_Integral_image_label_preview.setText('Preview calculated figure')
                self.d_Integral_image_label_preview.setFont(font)
                self.d_Integral_image_label_preview.setStyleSheet("font-size: 18px")
                self.d_Integral_image_label_preview.setObjectName('d_Integral_image_label_preview')

                
                self.stackedWidget_5 = QtWidgets.QStackedWidget(self.d_Integral_content)
                self.stackedWidget_5.setGeometry(QtCore.QRect(20, 470, 341, 61))
                self.stackedWidget_5.setStyleSheet("color: rgb(253, 41, 41);\n"
        "font-size: 16px;")
                self.stackedWidget_5.setObjectName("stackedWidget_5")
                self.error_widget_8 = QtWidgets.QWidget()
                self.error_widget_8.setObjectName("error_widget_8")
                self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.error_widget_8)
                self.horizontalLayout_20.setObjectName("horizontalLayout_20")
                self.error_label_8 = QtWidgets.QLabel(self.error_widget_8)
                self.error_label_8.setMaximumSize(QtCore.QSize(500, 16777215))
                self.error_label_8.setFont(font)
                self.error_label_8.setWordWrap(True)
                self.error_label_8.setObjectName("error_label_8")
                self.horizontalLayout_20.addWidget(self.error_label_8)
                self.stackedWidget_5.addWidget(self.error_widget_8)
                self.error_widget_9 = QtWidgets.QWidget()
                self.error_widget_9.setObjectName("error_widget_9")
                self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.error_widget_9)
                self.horizontalLayout_21.setObjectName("horizontalLayout_21")
                self.error_label_9 = QtWidgets.QLabel(self.error_widget_9)
                self.error_label_9.setFont(font)
                self.error_label_9.setWordWrap(True)
                self.error_label_9.setObjectName("error_label_9")
                self.horizontalLayout_21.addWidget(self.error_label_9)
                self.stackedWidget_5.addWidget(self.error_widget_9)

                self.correct_widget_9 = QtWidgets.QWidget()
                self.correct_widget_9.setObjectName("correct_widget_9")
                self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.correct_widget_9)
                self.horizontalLayout_21.setObjectName("horizontalLayout_21")
                self.correct_label_9 = QtWidgets.QLabel(self.correct_widget_9)
                self.correct_label_9.setStyleSheet('color:blue;')
                self.correct_label_9.setFont(font)
                self.correct_label_9.setWordWrap(True)
                self.correct_label_9.setObjectName("correct_label_9")
                self.horizontalLayout_21.addWidget(self.correct_label_9)
                self.stackedWidget_5.addWidget(self.correct_widget_9)
                self.stackedWidget.addWidget(self.d_Integral_content)

                self.c_Integral_content = QtWidgets.QWidget()
                self.c_Integral_content.setObjectName("c_Integral_content")
                self.c_Integral_input_value_fx = QtWidgets.QLineEdit(self.c_Integral_content)
                self.c_Integral_input_value_fx.setGeometry(QtCore.QRect(100, 111, 221, 31))
                self.c_Integral_input_value_fx.setFont(font)
                self.c_Integral_input_value_fx.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_input_value_fx.setObjectName("c_Integral_input_value_fx")
                self.c_Integral_BTN_compute = QtWidgets.QPushButton(self.c_Integral_content)
                self.c_Integral_BTN_compute.setGeometry(QtCore.QRect(80, 410, 141, 41))
                self.c_Integral_BTN_compute.setFont(font)
                self.c_Integral_BTN_compute.setStyleSheet("QPushButton {\n"
        "    border-radius: 16px;\n"
        "    border-style: outset;\n"
        "    color: white;\n"
        "    font-size: 22px;\n"
        "    border: 1px solid;\n"
        "    border-color: rgb(232, 232, 232);\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    color: black;\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }")
                self.c_Integral_BTN_compute.setObjectName("c_Integral_BTN_compute")
                self.c_Integral_main_label = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_main_label.setGeometry(QtCore.QRect(0, 0, 701, 91))
                self.c_Integral_main_label.setFont(font)
                self.c_Integral_main_label.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.c_Integral_main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.c_Integral_main_label.setWordWrap(True)
                self.c_Integral_main_label.setObjectName("c_Integral_main_label")
                self.c_Integral_label_fx = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_label_fx.setGeometry(QtCore.QRect(0, 110, 91, 31))
                self.c_Integral_label_fx.setFont(font)
                self.c_Integral_label_fx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.c_Integral_label_fx.setObjectName("c_Integral_label_fx")
                self.c_Integral_label_EP = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_label_EP.setGeometry(QtCore.QRect(0, 150, 101, 81))
                self.c_Integral_label_EP.setFont(font)
                self.c_Integral_label_EP.setWordWrap(True)
                self.c_Integral_label_EP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.c_Integral_label_EP.setObjectName("c_Integral_label_EP")
                self.c_Integral_input_value_x1 = QtWidgets.QLineEdit(self.c_Integral_content)
                self.c_Integral_input_value_x1.setGeometry(QtCore.QRect(110, 160, 101, 31))
                self.c_Integral_input_value_x1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_input_value_x1.setObjectName("c_Integral_input_value_x1")
                self.c_Integral_input_value_x2 = QtWidgets.QLineEdit(self.c_Integral_content)
                self.c_Integral_input_value_x2.setGeometry(QtCore.QRect(220, 160, 101, 31))
                self.c_Integral_input_value_x2.setFont(font)
                self.c_Integral_input_value_x2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_input_value_x2.setObjectName("c_Integral_input_value_x2")

                self.c_Integral_input_value_y1 = QtWidgets.QLineEdit(self.c_Integral_content)
                self.c_Integral_input_value_y1.setGeometry(QtCore.QRect(110, 200, 101, 31))
                self.c_Integral_input_value_y1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_input_value_y1.setObjectName("c_Integral_input_value_y1")
                self.c_Integral_input_value_y2 = QtWidgets.QLineEdit(self.c_Integral_content)
                self.c_Integral_input_value_y2.setGeometry(QtCore.QRect(220, 200, 101, 31))
                self.c_Integral_input_value_y2.setFont(font)
                self.c_Integral_input_value_y2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_input_value_y2.setObjectName("c_Integral_input_value_y2")

                self.c_Integral_input_value_z1 = QtWidgets.QLineEdit(self.c_Integral_content)
                self.c_Integral_input_value_z1.setGeometry(QtCore.QRect(110, 240, 101, 31))
                self.c_Integral_input_value_z1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_input_value_z1.setObjectName("c_Integral_input_value_z1")
                self.c_Integral_input_value_z2 = QtWidgets.QLineEdit(self.c_Integral_content)
                self.c_Integral_input_value_z2.setGeometry(QtCore.QRect(220, 240, 101, 31))
                self.c_Integral_input_value_z2.setFont(font)
                self.c_Integral_input_value_z2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_input_value_z2.setObjectName("c_Integral_input_value_z2")

                
                self.c_integral_sign = QtWidgets.QPushButton(self.c_Integral_content)
                self.c_integral_sign.setGeometry(QtCore.QRect(0, 280, 41, 71))
                self.c_integral_sign.setText("")
                self.c_integral_sign.setIcon(icon6)
                self.c_integral_sign.setIconSize(QtCore.QSize(56, 56))
                self.c_integral_sign.setObjectName("c_integral_sign")

                self.c_Integral_label_func = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_label_func.setGeometry(QtCore.QRect(40, 295, 131, 31))
                self.c_Integral_label_func.setFont(font)
                self.c_Integral_label_func.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.c_Integral_label_func.setObjectName("c_Integral_label_func")
                self.c_Integral_label_volume = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_label_volume.setGeometry(QtCore.QRect(70, 350, 101, 31))
                self.c_Integral_label_volume.setFont(font)
                self.c_Integral_label_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.c_Integral_label_volume.setObjectName("c_Integral_label_volume")

                self.c_Integral_label_symbolic_res = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_label_symbolic_res.setGeometry(QtCore.QRect(180, 296, 141, 31))
                self.c_Integral_label_symbolic_res.setFont(font)
                self.c_Integral_label_symbolic_res.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_label_symbolic_res.setText("")
                self.c_Integral_label_symbolic_res.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.c_Integral_label_symbolic_res.setObjectName("c_Integral_label_symbolic_res")
                

                self.c_Integral_label_volume_res = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_label_volume_res.setGeometry(QtCore.QRect(180, 351, 141, 31))
                self.c_Integral_label_volume_res.setFont(font)
                self.c_Integral_label_volume_res.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 16px;\n"
        "padding-left:10px;\n"
        "")
                self.c_Integral_label_volume_res.setText("")
                self.c_Integral_label_volume_res.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.c_Integral_label_volume_res.setObjectName("c_Integral_label_volume_res")

                #
                self.c_Integral_image_frame_preview = QtWidgets.QFrame(self.c_Integral_content)
                self.c_Integral_image_frame_preview.setGeometry(QtCore.QRect(330, 110, 340, 340))
                self.c_Integral_image_frame_preview.setStyleSheet("border: 1px solid;\n"
        "border-color: rgb(90, 90, 90);")
                self.c_Integral_image_frame_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.c_Integral_image_frame_preview.setFrameShadow(QtWidgets.QFrame.Raised)
                self.c_Integral_image_frame_preview.setObjectName("c_Integral_image_frame_preview")

                self.c_Integral_image_label_preview_fig = QtWidgets.QLabel(self.c_Integral_image_frame_preview)
                self.c_Integral_image_label_preview_fig.setGeometry(QtCore.QRect(0,0,340,340))
                self.c_Integral_image_label_preview_fig.setText("")
                self.c_Integral_image_label_preview_fig.setScaledContents(True)
                self.c_Integral_image_label_preview_fig.setObjectName("c_Integral_image_label_preview_fig ")  

                self.c_Integral_image_label_preview = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_image_label_preview.setGeometry(QtCore.QRect(410, 450, 271, 31))
                self.c_Integral_image_label_preview.setText('Preview calculated figure')
                self.c_Integral_image_label_preview.setFont(font)
                self.c_Integral_image_label_preview.setStyleSheet("font-size: 18px")
                self.c_Integral_image_label_preview.setObjectName('c_Integral_image_label_preview')
                #
                self.stackedWidget_6 = QtWidgets.QStackedWidget(self.c_Integral_content)
                self.stackedWidget_6.setGeometry(QtCore.QRect(20, 470, 341, 61))
                self.stackedWidget_6.setStyleSheet("color: rgb(253, 41, 41);\n"
        "font-size: 16px;")
                self.stackedWidget_6.setObjectName("stackedWidget_6")
                self.error_widget_10 = QtWidgets.QWidget()
                self.error_widget_10.setObjectName("error_widget_10")
                self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.error_widget_10)
                self.horizontalLayout_22.setObjectName("horizontalLayout_22")
                self.error_label_10 = QtWidgets.QLabel(self.error_widget_10)
                self.error_label_10.setMaximumSize(QtCore.QSize(500, 16777215))
                self.error_label_10.setFont(font)
                self.error_label_10.setWordWrap(True)
                self.error_label_10.setObjectName("error_label_10")
                self.horizontalLayout_22.addWidget(self.error_label_10)
                self.stackedWidget_6.addWidget(self.error_widget_10)
                self.error_widget_11 = QtWidgets.QWidget()
                self.error_widget_11.setObjectName("error_widget_11")
                self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.error_widget_11)
                self.horizontalLayout_23.setObjectName("horizontalLayout_23")
                self.error_label_11 = QtWidgets.QLabel(self.error_widget_11)
                self.error_label_11.setFont(font)
                self.error_label_11.setWordWrap(True)
                self.error_label_11.setObjectName("error_label_11")
                self.horizontalLayout_23.addWidget(self.error_label_11)
                self.stackedWidget_6.addWidget(self.error_widget_11)
                self.stackedWidget.addWidget(self.c_Integral_content)
                self.delta_content = QtWidgets.QWidget()
                self.delta_content.setObjectName("delta_content")
                self.Delta_input_value_A = QtWidgets.QLineEdit(self.delta_content)
                self.Delta_input_value_A.setGeometry(QtCore.QRect(90, 260, 51, 31))
                self.Delta_input_value_A.setFont(font)
                self.Delta_input_value_A.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Delta_input_value_A.setObjectName("Delta_input_value_A")
                self.Delta_input_value_B = QtWidgets.QLineEdit(self.delta_content)
                self.Delta_input_value_B.setGeometry(QtCore.QRect(150, 260, 51, 31))
                self.Delta_input_value_B.setFont(font)
                self.Delta_input_value_B.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Delta_input_value_B.setObjectName("Delta_input_value_B")

                self.Delta_input_value_C = QtWidgets.QLineEdit(self.delta_content)
                self.Delta_input_value_C.setGeometry(QtCore.QRect(210, 260, 51, 31))
                self.Delta_input_value_C.setFont(font)
                self.Delta_input_value_C.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Delta_input_value_C.setObjectName("Delta_input_value_B")

                self.Delta_BTN_compute_2 = QtWidgets.QPushButton(self.delta_content)
                self.Delta_BTN_compute_2.setGeometry(QtCore.QRect(80, 360, 141, 41))
                self.Delta_BTN_compute_2.setFont(font)
                self.Delta_BTN_compute_2.setStyleSheet("QPushButton {\n"
        "    border-radius: 16px;\n"
        "    border-style: outset;\n"
        "    color: white;\n"
        "    font-size: 22px;\n"
        "    border: 1px solid;\n"
        "    border-color: rgb(232, 232, 232);\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    color: black;\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
        "    }")
                self.Delta_BTN_compute_2.setObjectName("Delta_BTN_compute_2")
                self.Delta_main_label_2 = QtWidgets.QLabel(self.delta_content)
                self.Delta_main_label_2.setGeometry(QtCore.QRect(0, 0, 701, 71))
                self.Delta_main_label_2.setFont(font)
                self.Delta_main_label_2.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Delta_main_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Delta_main_label_2.setWordWrap(True)
                self.Delta_main_label_2.setObjectName("Delta_main_label_2")
                self.Delta_label_fx_2 = QtWidgets.QLabel(self.delta_content)
                self.Delta_label_fx_2.setGeometry(QtCore.QRect(70, 215, 141, 31))
                self.Delta_label_fx_2.setFont(font)
                self.Delta_label_fx_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Delta_label_fx_2.setObjectName("Delta_label_fx_2")

                self.Delta_label_range = QtWidgets.QLabel(self.delta_content)
                self.Delta_label_range.setGeometry(QtCore.QRect(0, 260, 81, 31))
                self.Delta_label_range.setFont(font)
                self.Delta_label_range.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Delta_label_range.setObjectName("Delta_label_range")

                self.Delta_label_result_x2 = QtWidgets.QLabel(self.delta_content)
                self.Delta_label_result_x2.setGeometry(QtCore.QRect(40, 310, 81, 31))
                self.Delta_label_result_x2.setFont(font)
                self.Delta_label_result_x2.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Delta_label_result_x2.setText("")
                self.Delta_label_result_x2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Delta_label_result_x2.setObjectName("Delta_label_result_x2")
                self.Delta_result_x1 = QtWidgets.QLabel(self.delta_content)
                self.Delta_result_x1.setGeometry(QtCore.QRect(0, 310, 31, 31))
                self.Delta_result_x1.setFont(font)
                self.Delta_result_x1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Delta_result_x1.setObjectName("Delta_result_x1")
                self.Delta_main_label_3 = QtWidgets.QLabel(self.delta_content)
                self.Delta_main_label_3.setGeometry(QtCore.QRect(0, 80, 701, 91))
                self.Delta_main_label_3.setFont(font)
                self.Delta_main_label_3.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Delta_main_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Delta_main_label_3.setWordWrap(True)
                self.Delta_main_label_3.setObjectName("Delta_main_label_3")
                self.Delta_label_result_x1 = QtWidgets.QLabel(self.delta_content)
                self.Delta_label_result_x1.setGeometry(QtCore.QRect(170, 310, 81, 31))
                self.Delta_label_result_x1.setFont(font)
                self.Delta_label_result_x1.setStyleSheet("border: 1px solid;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "\n"
        "color: rgb(235, 235, 235);\n"
        "font-size: 18px;\n"
        "padding-left:10px;\n"
        "")
                self.Delta_label_result_x1.setText("")
                self.Delta_label_result_x1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Delta_label_result_x1.setObjectName("Delta_label_result_x1")
                self.Delta_result_x1_2 = QtWidgets.QLabel(self.delta_content)
                self.Delta_result_x1_2.setGeometry(QtCore.QRect(130, 310, 31, 31))
                self.Delta_result_x1_2.setFont(font)
                self.Delta_result_x1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.Delta_result_x1_2.setObjectName("Delta_result_x1_2")

                self.Delta_image_frame_preview = QtWidgets.QFrame(self.delta_content)
                self.Delta_image_frame_preview.setGeometry(QtCore.QRect(330, 170, 340, 340))
                self.Delta_image_frame_preview.setStyleSheet("border: 1px solid;\n"
        "border-color: rgb(90, 90, 90);")
                self.Delta_image_frame_preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Delta_image_frame_preview.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Delta_image_frame_preview.setObjectName("Delta_image_frame_preview")

                self.Delta_image_label_preview_fig = QtWidgets.QLabel(self.Delta_image_frame_preview)
                self.Delta_image_label_preview_fig.setGeometry(QtCore.QRect(0,0,340,340))
                self.Delta_image_label_preview_fig.setText("")
                self.Delta_image_label_preview_fig.setScaledContents(True)
                self.Delta_image_label_preview_fig.setObjectName("Delta_image_label_preview_fig ")  

                self.Delta_image_label_preview = QtWidgets.QLabel(self.delta_content)
                self.Delta_image_label_preview.setGeometry(QtCore.QRect(410, 510, 271, 31))
                self.Delta_image_label_preview.setText('Preview calculated figure')
                self.Delta_image_label_preview.setFont(font)
                self.Delta_image_label_preview.setStyleSheet("font-size: 18px")
                self.Delta_image_label_preview.setObjectName('c_Integral_image_label_preview')
                
                self.stackedWidget_7 = QtWidgets.QStackedWidget(self.delta_content)
                self.stackedWidget_7.setGeometry(QtCore.QRect(0, 410, 291, 81))
                self.stackedWidget_7.setStyleSheet("color: rgb(253, 41, 41);\n"
        "font-size: 16px;")
                self.stackedWidget_7.setObjectName("stackedWidget_7")
                self.error_widget_12 = QtWidgets.QWidget()
                self.error_widget_12.setObjectName("error_widget_12")
                self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.error_widget_12)
                self.horizontalLayout_24.setObjectName("horizontalLayout_24")
                self.error_label_12 = QtWidgets.QLabel(self.error_widget_12)
                self.error_label_12.setMaximumSize(QtCore.QSize(500, 16777215))
                self.error_label_12.setFont(font)
                self.error_label_12.setWordWrap(True)
                self.error_label_12.setObjectName("error_label_12")
                self.horizontalLayout_24.addWidget(self.error_label_12)
                self.stackedWidget_7.addWidget(self.error_widget_12)
                self.error_widget_13 = QtWidgets.QWidget()
                self.error_widget_13.setObjectName("error_widget_13")
                self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.error_widget_13)
                self.horizontalLayout_25.setObjectName("horizontalLayout_25")
                self.error_label_13 = QtWidgets.QLabel(self.error_widget_13)
                self.error_label_13.setFont(font)
                self.error_label_13.setWordWrap(True)
                self.error_label_13.setObjectName("error_label_13")
                self.horizontalLayout_25.addWidget(self.error_label_13)
                self.stackedWidget_7.addWidget(self.error_widget_13)

                self.correct_widget_14 = QtWidgets.QWidget()
                self.correct_widget_14.setObjectName("correct_widget_14")
                self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.correct_widget_14)
                self.horizontalLayout_25.setObjectName("horizontalLayout_25")
                self.correct_label_14 = QtWidgets.QLabel(self.correct_widget_14)
                self.correct_label_14.setFont(font)
                self.correct_label_14.setWordWrap(True)
                self.correct_label_14.setObjectName("correct_label_14")
                self.correct_label_14.setStyleSheet('color:blue;')
                self.horizontalLayout_25.addWidget(self.correct_label_14)
                self.stackedWidget_7.addWidget(self.correct_widget_14)

                self.stackedWidget.addWidget(self.delta_content)
                self.horizontalLayout_11.addWidget(self.stackedWidget)
                self.verticalLayout_6.addWidget(self.Bottom_right_content_in)
                self.Bottom_right_copyright = QtWidgets.QFrame(self.Bottom_right_content_out)
                self.Bottom_right_copyright.setMaximumSize(QtCore.QSize(16777215, 30))
                self.Bottom_right_copyright.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Bottom_right_copyright.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Bottom_right_copyright.setObjectName("Bottom_right_copyright")
                self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.Bottom_right_copyright)
                self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_12.setSpacing(0)
                self.horizontalLayout_12.setObjectName("horizontalLayout_12")
                self.Copyright_label = QtWidgets.QLabel(self.Bottom_right_copyright)
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.Copyright_label.setFont(font)
                self.Copyright_label.setStyleSheet("color: rgb(235, 235, 235)")
                self.Copyright_label.setObjectName("Copyright_label")
                self.horizontalLayout_12.addWidget(self.Copyright_label)
                self.verticalLayout_6.addWidget(self.Bottom_right_copyright, 0, QtCore.Qt.AlignRight)
                self.horizontalLayout_4.addWidget(self.Bottom_right_content_out)
                self.verticalLayout.addWidget(self.Bottom_bar)
                self.Plot_preview_label = QtWidgets.QLabel(self.Plot_frame)
                self.Plot_preview_label.setGeometry(QtCore.QRect(0,0,350,350))
                self.Plot_preview_label.setText("")
                self.Plot_preview_label.setScaledContents(True)
                self.Plot_preview_label.setObjectName("Plot_preview_label")
                self.Derivative_preview_label_dxdy = QtWidgets.QLabel(self.Derivative_frame_dxdy)
                self.Derivative_preview_label_dxdy.setGeometry(QtCore.QRect(0,0,340,340))
                self.Derivative_preview_label_dxdy.setText("")
                self.Derivative_preview_label_dxdy.setScaledContents(True)
                self.Derivative_preview_label_dxdy.setObjectName("Derivative_preview_label_dxdy") 

                self.Plot_warrning_note = QtWidgets.QLabel(self.Plot_content)
                self.Plot_warrning_note.setGeometry(QtCore.QRect(0, 570, 701, 61))
                self.Plot_warrning_note.setText('Note: Error may occour if you type uncountable function like: x/0 or log(x=0) etc.')
                self.Plot_warrning_note.setFont(font)
                self.Plot_warrning_note.setStyleSheet("font-size: 18px")
                self.Plot_warrning_note.setObjectName('Plot_warrning_note')
                self.Plot_warrning_note.setFont(font)
                self.Plot_warrning_note.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Plot_warrning_note.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Plot_warrning_note.setTextFormat(QtCore.Qt.AutoText)
                self.Plot_warrning_note.setScaledContents(False)
                self.Plot_warrning_note.setWordWrap(True)

                self.Derivative_warrning_note = QtWidgets.QLabel(self.Derivative_centent)
                self.Derivative_warrning_note.setGeometry(QtCore.QRect(0, 570, 701, 61))
                self.Derivative_warrning_note.setText('Note: Error may occour if you type uncountable function like: x/0 or log(x=0) etc.')
                self.Derivative_warrning_note.setFont(font)
                self.Derivative_warrning_note.setStyleSheet("font-size: 18px")
                self.Derivative_warrning_note.setObjectName('Derivative_warrning_note')
                self.Derivative_warrning_note.setFont(font)
                self.Derivative_warrning_note.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Derivative_warrning_note.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Derivative_warrning_note.setTextFormat(QtCore.Qt.AutoText)
                self.Derivative_warrning_note.setScaledContents(False)
                self.Derivative_warrning_note.setWordWrap(True)

                self.Integral_warrning_note = QtWidgets.QLabel(self.Integral_content)
                self.Integral_warrning_note.setGeometry(QtCore.QRect(0, 570, 701, 61))
                self.Integral_warrning_note.setText('Note: Error may occour if you type uncountable function like: x/0 or log(x=0) etc.')
                self.Integral_warrning_note.setFont(font)
                self.Integral_warrning_note.setStyleSheet("font-size: 18px")
                self.Integral_warrning_note.setObjectName('Integral_warrning_note')
                self.Integral_warrning_note.setFont(font)
                self.Integral_warrning_note.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.Integral_warrning_note.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Integral_warrning_note.setTextFormat(QtCore.Qt.AutoText)
                self.Integral_warrning_note.setScaledContents(False)
                self.Integral_warrning_note.setWordWrap(True)

                self.d_Integral_warrning_note = QtWidgets.QLabel(self.d_Integral_content)
                self.d_Integral_warrning_note.setGeometry(QtCore.QRect(0, 570, 701, 61))
                self.d_Integral_warrning_note.setText('Note: Error may occour if you type uncountable function like: x/0 or log(x=0) etc.')
                self.d_Integral_warrning_note.setFont(font)
                self.d_Integral_warrning_note.setStyleSheet("font-size: 18px")
                self.d_Integral_warrning_note.setObjectName('d_Integral_warrning_note')
                self.d_Integral_warrning_note.setFont(font)
                self.d_Integral_warrning_note.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.d_Integral_warrning_note.setFrameShadow(QtWidgets.QFrame.Raised)
                self.d_Integral_warrning_note.setTextFormat(QtCore.Qt.AutoText)
                self.d_Integral_warrning_note.setScaledContents(False)
                self.d_Integral_warrning_note.setWordWrap(True)

                self.c_Integral_warrning_note = QtWidgets.QLabel(self.c_Integral_content)
                self.c_Integral_warrning_note.setGeometry(QtCore.QRect(0, 570, 701, 61))
                self.c_Integral_warrning_note.setText('Note: Error may occour if you type uncountable function like: x/0 or log(x=0) etc.')
                self.c_Integral_warrning_note.setFont(font)
                self.c_Integral_warrning_note.setStyleSheet("font-size: 18px")
                self.c_Integral_warrning_note.setObjectName('c_Integral_warrning_note')
                self.c_Integral_warrning_note.setFont(font)
                self.c_Integral_warrning_note.setStyleSheet("color: rgb(235, 235, 235);\n"
        "font-size: 18px;")
                self.c_Integral_warrning_note.setFrameShadow(QtWidgets.QFrame.Raised)
                self.c_Integral_warrning_note.setTextFormat(QtCore.Qt.AutoText)
                self.c_Integral_warrning_note.setScaledContents(False)
                self.c_Integral_warrning_note.setWordWrap(True)

                MainWindow.setCentralWidget(self.Main)
                self.retranslateUi(MainWindow)
                self.stackedWidget_2.setCurrentIndex(0)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)


                self.retranslateUi(MainWindow)
                self.set_page(MainWindow)
                self.set_toggle_flag()
                self.set_figure_flags()

                self.plot_expressions()


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.Home_title_label.setText(_translate("MainWindow", "Home"))
                self.Derivative_label.setText(_translate("MainWindow", "Derivative"))
                self.Integral_label.setText(_translate("MainWindow", "Integral"))
                self.d_integral_title_label.setText(_translate("MainWindow", "Double Integral"))
                self.c_integral_title_label.setText(_translate("MainWindow", "Triple Integral"))
                self.Plot_title_label.setText(_translate("MainWindow", "Plots"))
                self.delta_title_label.setText(_translate("MainWindow", "Quadratic Equation"))
                self.Home_label_2.setText(_translate("MainWindow", "This is demonstrational version of program. Software is created with persons in mind who study mathematics in high school and people who work on scientific stuff. The basic function of software is calculating advanced mathematic functions like integrals, derivatives etc., also software contains basic mathematic features like creating plots established by functions."))
                self.Home_label_1.setText(_translate("MainWindow", "About Scientific Calculator"))
                self.Home_label_3.setText(_translate("MainWindow", "Scientific Calculator\'s features:"))
                self.Home_label_4.setText(_translate("MainWindow", "- Creating plots"))
                self.Home_label_5.setText(_translate("MainWindow", "- Calculating derivative"))
                self.Home_label_6.setText(_translate("MainWindow", "- Calculating integrals"))
                self.Home_label_7.setText(_translate("MainWindow", "- Calculating double integrals"))
                self.Home_label_8.setText(_translate("MainWindow", "- Calculating triple integrals"))
                self.Home_label_9.setText(_translate("MainWindow", "- Calculating square equation"))
                self.Home_label_10.setText(_translate("MainWindow", "About Author"))
                self.Home_label_11.setText(_translate("MainWindow", "The author of this software is Grzegorz Jakmiuk. Program has been created only just for portfolio needs."))
                self.Integral_main_label.setText(_translate("MainWindow", "In mathematics, an integral assigns numbers to functions in a way that can describe displacement, area, volume, and other concepts that arise by combining infinitesimal data. Integration is one of the two main operations of calculus; its inverse operation, differentiation, is the other. Given a function f of a real variable x and an interval [a, b] of the real line, the definite integral of f from a to b can be interpreted informally as the signed area of the region in the xy-plane that is bounded by the graph of f, the x-axis and the vertical lines x = a and x = b. Source: Wikipedia"))
                self.Integral_label_fx.setText(_translate("MainWindow", "f(x) ="))
                self.Integral_input_value.setPlaceholderText(_translate("MainWindow", "x**2"))
                self.Integral_label_fx_2.setText(_translate("MainWindow", "f(x) dx ="))
                self.Integral_label_P.setText(_translate("MainWindow", "P(x) ="))
                self.d_Integral_label_P.setText(_translate("MainWindow", "P(x,y) ="))
                self.Integral_BTN_compute.setText(_translate("MainWindow", "Compute"))
                self.error_label_6.setText(_translate("MainWindow", "Error: you left blank bracket somewhere, make sure that you enter correct values"))
                self.error_label_7.setText(_translate("MainWindow", "Error: wrong data type in bracket, make sure that you enter correct values"))
                self.correct_label_7.setText(_translate("MainWindow", "The function has been calculated"))
                self.Plot_label_1.setText(_translate("MainWindow", "Insert input values to brackets and click generate to get plot with your datas. Only you can use integer or float type of data "))
                self.Plot_fn_edit.setPlaceholderText(_translate("MainWindow", "ax+b"))
                self.Plot_fn_sign_label.setText(_translate("MainWindow", "f(x) = "))
                self.Plot_range_sign.setText(_translate("MainWindow", "Range:"))
                self.Plot_range_x1.setPlaceholderText(_translate("MainWindow", "x1"))
                self.Plot_color_sign.setText(_translate("MainWindow", "Color:"))
                self.Plot_range_x2.setPlaceholderText(_translate("MainWindow", "x2"))
                self.Plot_combo_color.setItemText(0, _translate("MainWindow", "Red"))
                self.Plot_combo_color.setItemText(1, _translate("MainWindow", "Blue"))
                self.Plot_combo_color.setItemText(2, _translate("MainWindow", "Purple"))
                self.Plot_combo_color.setItemText(3, _translate("MainWindow", "Yellow"))
                self.Plot_combo_color.setItemText(4, _translate("MainWindow", "Teal"))
                self.Plot_combo_color.setItemText(5, _translate("MainWindow", "Green"))
                self.Plot_BTN_generate.setText(_translate("MainWindow", "Compute"))
                
                self.Plot_label_2.setText(_translate("MainWindow", "Preview calculated figure"))
                self.error_label_1.setText(_translate("MainWindow", "Error: you left blank bracket somewhere, make sure that you enter correct values"))
                self.error_label_2.setText(_translate("MainWindow", "Error: wrong data type in bracket, make sure that you enter correct values"))
                self.Plot_figure_saved_label.setText(_translate("MainWindow", "The figure has been saved"))
                self.Derivative_main_label.setText(_translate("MainWindow", "The derivative of a function of a real variable measures the sensitivity to change of the function value (output value) with respect to a change in its argument (input value). Derivatives are a fundamental tool of calculus. For example, the derivative of the position of a moving object with respect to time is the object\'s velocity: this measures how quickly the position of the object changes when time advances. Source: wikipedia"))
                self.Derivative_label_fx.setText(_translate("MainWindow", "y ="))
                self.Derivative_input_value.setPlaceholderText(_translate("MainWindow", "x**2-3*x"))
                self.Derivative_label_fxpr.setText(_translate("MainWindow", "="))
                self.Derivative_BTN_compute.setText(_translate("MainWindow", "Compute"))
                self.Derivative_range_x1.setPlaceholderText(_translate("MainWindow", "x1"))
                self.Derivative_range_x2.setPlaceholderText(_translate("MainWindow", "x2"))
                self.Integral_range_x1.setPlaceholderText(_translate("MainWindow", "x1"))
                self.Integral_range_x2.setPlaceholderText(_translate("MainWindow", "x2"))
                self.d_Integral_range_x1.setPlaceholderText(_translate("MainWindow", "x1"))
                self.d_Integral_range_x2.setPlaceholderText(_translate("MainWindow", "x2"))
                self.d_Integral_range_y1.setPlaceholderText(_translate("MainWindow", "y1"))
                self.d_Integral_range_y2.setPlaceholderText(_translate("MainWindow", "y2"))
                self.correct_label_4.setText(_translate("MainWindow", "The function has been calculated"))
                self.error_label_4.setText(_translate("MainWindow", "Error: you left blank bracket somewhere, make sure that you enter correct values"))
                self.error_label_5.setText(_translate("MainWindow", "Error: wrong data type in bracket, make sure that you enter correct values"))
                self.d_Integral_main_label.setText(_translate("MainWindow", "The multiple integral is a definite integral of a function of more than one real variable, for instance, f or f. Integrals of a function of two variables over a region in R² are called double integrals, and integrals of a function of three variables over a region of R³ are called triple integrals. Source: Wikipedia"))
                self.d_Integral_label_fx.setText(_translate("MainWindow", "f(x,y)dxdy ="))
                self.d_Integral_label_fx_2.setText(_translate("MainWindow", "f(x,y) ="))
                self.d_Integral_input_value.setPlaceholderText(_translate("MainWindow", "x*y"))
                self.d_Integral_BTN_compute.setText(_translate("MainWindow", "Compute"))
                self.error_label_8.setText(_translate("MainWindow", "Error: you left blank bracket somewhere, make sure that you enter correct values"))
                self.error_label_9.setText(_translate("MainWindow", "Error: wrong data type in bracket, make sure that you enter correct values"))
                self.correct_label_9.setText(_translate("MainWindow", "The function has been calculated"))
                self.c_Integral_input_value_fx.setPlaceholderText(_translate("MainWindow", "x**2*y*z"))
                self.c_Integral_BTN_compute.setText(_translate("MainWindow", "Compute"))
                self.c_Integral_main_label.setText(_translate("MainWindow", "In mathematics, a multiple integral is a definite integral of a function of several real variables, for instance, f or f. Integrals of a function of two variables over a region in are called double integrals, and integrals of a function of three variables over a region in are called triple integrals. Source: Wikipedia"))
                self.c_Integral_label_fx.setText(_translate("MainWindow", "f(x,y,z) ="))
                self.c_Integral_label_EP.setText(_translate("MainWindow", "Integration area:"))
                self.c_Integral_input_value_x1.setPlaceholderText(_translate("MainWindow", "x1"))
                self.c_Integral_input_value_x2.setPlaceholderText(_translate("MainWindow", "x2"))
                self.c_Integral_input_value_y1.setPlaceholderText(_translate("MainWindow", "y1"))
                self.c_Integral_input_value_y2.setPlaceholderText(_translate("MainWindow", "y2"))
                self.c_Integral_input_value_z1.setPlaceholderText(_translate("MainWindow", "z1"))
                self.c_Integral_input_value_z2.setPlaceholderText(_translate("MainWindow", "z2"))

                

                self.c_Integral_label_func.setText(_translate("MainWindow", "f(x,y,x)dxdydz ="))
                self.c_Integral_label_volume.setText(_translate("MainWindow", "V(x,y,z) ="))
                self.error_label_10.setText(_translate("MainWindow", "Error: you left blank bracket somewhere, make sure that you enter correct values"))
                self.error_label_11.setText(_translate("MainWindow", "Error: wrong data type in bracket, make sure that you enter correct values"))
                
                self.Delta_input_value_A.setPlaceholderText(_translate("MainWindow", "A"))
                self.Delta_input_value_B.setPlaceholderText(_translate("MainWindow", "B"))
                self.Delta_input_value_C.setPlaceholderText(_translate("MainWindow", "C"))
                self.Delta_BTN_compute_2.setText(_translate("MainWindow", "Compute"))
                self.Delta_main_label_2.setText(_translate("MainWindow", "The quadratic equation only contains powers of x that are non-negative integers, and therefore it is a polynomial equation. In particular, it is a second-degree polynomial equation, since the greatest power is two."))
                self.Delta_label_fx_2.setText(_translate("MainWindow", "f(x) = Ax²+Bx+C"))
                self.Delta_label_range.setText(_translate("MainWindow", "Variables:"))
                self.Delta_result_x1.setText(_translate("MainWindow", "x1"))
                self.Delta_main_label_3.setText(_translate("MainWindow", "In algebra, a quadratic equation is any equation that can be rearranged in standard form as where x represents an unknown, and a, b, and c represent known numbers, where a ≠ 0. If a = 0, then the equation is linear, not quadratic, as there is no term. Source: Wikipedia"))
                self.Delta_result_x1_2.setText(_translate("MainWindow", "x2"))
                self.error_label_12.setText(_translate("MainWindow", "Error: you left blank bracket somewhere, make sure that you enter correct values"))
                self.error_label_13.setText(_translate("MainWindow", "Error: wrong data type in bracket, make sure that you enter correct values"))
                self.correct_label_14.setText(_translate("MainWindow", "The function has been calculated"))
                self.Copyright_label.setText(_translate("MainWindow", "© 2020 Grzegorz Jakimiuk. All Rights Reserved. version 1.0"))

        def set_page(self, MainWindow):
                
                #Pages
                self.Home_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Home_content))
                self.Home_btn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.Home_title))
                self.Plot_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Plot_content))
                self.Plot_btn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.Plot_title))
                self.Derviate_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Derivative_centent))
                self.Derviate_btn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.Derivative_title))
                self.Integral_1st_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Integral_content))
                self.Integral_1st_btn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.Integral))
                self.Integral_2x_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.d_Integral_content))
                self.Integral_2x_btn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.d_Integral_title))
                self.Integral_curved_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.c_Integral_content))
                self.Integral_curved_btn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.c_Integral_title))
                self.Delta_plot_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.delta_content))
                self.Delta_plot_btn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.delta_title))
                
                #Toggle Menu
                self.Menu_button.clicked.connect(lambda: self.toggle_menu(0))

                #Errors dispaly
                self.Plot_error_info.setVisible(False)
                self.stackedWidget_4.setVisible(False)
                self.stackedWidget_3.setVisible(False)
                self.stackedWidget_6.setVisible(False)
                self.stackedWidget_7.setVisible(False)
                self.stackedWidget_5.setVisible(False)
        
        def set_figure_flags(self):
                global delta_close_figure_flag 
                delta_close_figure_flag = True

        def set_toggle_flag(self):
                global flagIt
                flagIt = True
        
        
        def toggle_menu(self, Value):
                global flagIt
                if flagIt:
                        #HIDDEN
                        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 0))
                        self.stackedWidget.setMaximumSize(QtCore.QSize(800, 16777215))

                        self.Bottom_left_icons_out.setMinimumSize(QtCore.QSize(Value, 0))
                        self.Bottom_left_icons_out.setMaximumSize(QtCore.QSize(Value, 16777215))

                        #Home section
                        self.Home_label_2.setMaximumWidth(1200)
                        self.Home_label_2.setGeometry(QtCore.QRect(0,40,800,121))
                        self.Home_label_11.setMaximumWidth(1200)
                        self.Home_label_11.setGeometry(QtCore.QRect(0, 490, 800, 51))
                        #Plot Section
                        self.Plot_frame.setGeometry(QtCore.QRect(450, 0, 350, 350))
                        self.Plot_label_2.setGeometry(QtCore.QRect(450, 350, 351, 21))
                        self.Plot_label_1.setGeometry(QtCore.QRect(0, 20, 441, 91))
                        #Derivative Section
                        self.Derivative_main_label.setGeometry(QtCore.QRect(0, 0, 801, 141))
                        self.Derivative_frame_dxdy.setGeometry(QtCore.QRect(430, 120, 340, 340))
                        self.Derivative_image_preview_dxdy.setGeometry(QtCore.QRect(510, 460, 271, 31))
                        #Integral Section
                        self.Integral_main_label.setGeometry(QtCore.QRect(0, 0, 801, 191))
                        self.Integral_image_label_preview.setGeometry(QtCore.QRect(510, 500, 271, 31))
                        self.Integral_image_frame_preview.setGeometry(QtCore.QRect(430, 160, 340, 340))
                        self.Integral_input_value.setGeometry(QtCore.QRect(130, 200, 281, 31))
                        self.Integral_label_fxpr_res.setGeometry(QtCore.QRect(130, 330, 281, 31))
                        self.Integral_label_P_res.setGeometry(QtCore.QRect(130, 390, 281, 31))
                        self.Integral_BTN_compute.setGeometry(QtCore.QRect(150, 460, 131, 41))
                        self.stackedWidget_4.setGeometry(QtCore.QRect(50, 510, 321, 61))
                        #Double Integral Section
                        self.d_Integral_main_label.setGeometry(QtCore.QRect(0, 0, 801, 91))    
                        self.d_Integral_image_frame_preview.setGeometry(QtCore.QRect(430, 110, 340, 340)) 
                        self.d_Integral_image_label_preview.setGeometry(QtCore.QRect(510, 450, 271, 31))
                        self.d_Integral_label_fxpr_res.setGeometry(QtCore.QRect(160, 280, 251, 31))
                        self.d_Integral_input_value.setGeometry(QtCore.QRect(130, 130, 281, 31))
                        self.d_Integral_label_P_res.setGeometry(QtCore.QRect(130, 340, 281, 31))
                        self.d_Integral_BTN_compute.setGeometry(QtCore.QRect(150, 410, 131, 41))
                        self.stackedWidget_5.setGeometry(QtCore.QRect(70, 470, 341, 61))
                        #Triple Integral Section
                        self.c_Integral_main_label.setGeometry(QtCore.QRect(0, 0, 801, 91))
                        self.c_Integral_input_value_fx.setGeometry(QtCore.QRect(100, 111, 321, 31))
                        self.c_Integral_image_frame_preview.setGeometry(QtCore.QRect(430, 110, 340, 340))
                        self.c_Integral_image_label_preview.setGeometry(QtCore.QRect(510, 450, 271, 31))
                        self.c_Integral_label_symbolic_res.setGeometry(QtCore.QRect(180, 296, 241, 31))
                        self.c_Integral_label_volume_res.setGeometry(QtCore.QRect(180, 351, 241, 31))
                        self.c_Integral_BTN_compute.setGeometry(QtCore.QRect(130, 410, 141, 41))
                        self.stackedWidget_6.setGeometry(QtCore.QRect(70, 470, 341, 61))
                        #Delta Section
                        self.Delta_main_label_2.setGeometry(QtCore.QRect(0, 0, 801, 71))
                        self.Delta_main_label_3.setGeometry(QtCore.QRect(0, 80, 801, 91))
                        self.Delta_image_frame_preview.setGeometry(QtCore.QRect(430, 170, 340, 340))
                        self.Delta_image_label_preview.setGeometry(QtCore.QRect(510, 510, 271, 31))
                        flagIt = False
                        return 0
                else:
                        #NOT HIDDEN
                        self.stackedWidget.setMinimumSize(QtCore.QSize(800+128, 0))
                        self.stackedWidget.setMaximumSize(QtCore.QSize(800+128, 16777215))
                        self.Bottom_left_icons_out.setMinimumSize(QtCore.QSize(128, 0))
                        self.Bottom_left_icons_out.setMaximumSize(QtCore.QSize(128, 16777215))
                        #Home section
                        self.Home_label_2.setGeometry(QtCore.QRect(0,40,700,121))
                        self.Home_label_11.setGeometry(QtCore.QRect(0, 490, 700, 51))
                        #Plot Section
                        self.Plot_frame.setGeometry(QtCore.QRect(350, 0, 350, 350))
                        self.Plot_label_2.setGeometry(QtCore.QRect(350, 350, 351, 21))
                        self.Plot_label_1.setGeometry(QtCore.QRect(0, 20, 341, 91))
                        #Derivative Section
                        self.Derivative_main_label.setGeometry(QtCore.QRect(0, 0, 701, 141))
                        self.Derivative_frame_dxdy.setGeometry(QtCore.QRect(330, 120, 340, 340))
                        self.Derivative_image_preview_dxdy.setGeometry(QtCore.QRect(410, 460, 271, 31))
                        #Integral Section
                        self.Integral_main_label.setGeometry(QtCore.QRect(0, 0, 801, 191))
                        self.Integral_image_label_preview.setGeometry(QtCore.QRect(410, 500, 271, 31))
                        self.Integral_image_frame_preview.setGeometry(QtCore.QRect(330, 160, 340, 340))
                        self.Integral_input_value.setGeometry(QtCore.QRect(130, 200, 181, 31))
                        self.Integral_label_fxpr_res.setGeometry(QtCore.QRect(130, 330, 181, 31))
                        self.Integral_label_P_res.setGeometry(QtCore.QRect(130, 390, 181, 31))
                        self.Integral_BTN_compute.setGeometry(QtCore.QRect(100, 460, 131, 41))
                        self.stackedWidget_4.setGeometry(QtCore.QRect(0, 510, 321, 61))
                        #Double Integral Section
                        self.d_Integral_main_label.setGeometry(QtCore.QRect(0, 0, 701, 91))
                        self.d_Integral_image_frame_preview.setGeometry(QtCore.QRect(330, 110, 340, 340))
                        self.d_Integral_image_label_preview.setGeometry(QtCore.QRect(410, 450, 271, 31))
                        self.d_Integral_label_fxpr_res.setGeometry(QtCore.QRect(160, 280, 151, 31))
                        self.d_Integral_input_value.setGeometry(QtCore.QRect(130, 130, 181, 31))
                        self.d_Integral_label_P_res.setGeometry(QtCore.QRect(130, 340, 181, 31))
                        self.d_Integral_BTN_compute.setGeometry(QtCore.QRect(100, 410, 131, 41))
                        self.stackedWidget_5.setGeometry(QtCore.QRect(20, 470, 341, 61))
                        #Triple Integral Section
                        self.c_Integral_main_label.setGeometry(QtCore.QRect(0, 0, 701, 91))
                        self.c_Integral_input_value_fx.setGeometry(QtCore.QRect(100, 111, 221, 31))
                        self.c_Integral_image_frame_preview.setGeometry(QtCore.QRect(330, 110, 340, 340))
                        self.c_Integral_image_label_preview.setGeometry(QtCore.QRect(410, 450, 271, 31))
                        self.c_Integral_label_symbolic_res.setGeometry(QtCore.QRect(180, 296, 141, 31))
                        self.c_Integral_label_volume_res.setGeometry(QtCore.QRect(180, 351, 141, 31))
                        self.c_Integral_BTN_compute.setGeometry(QtCore.QRect(80, 410, 141, 41))
                        self.stackedWidget_6.setGeometry(QtCore.QRect(20, 470, 341, 61))
                        #Delta Section
                        self.Delta_main_label_2.setGeometry(QtCore.QRect(0, 0, 701, 71))
                        self.Delta_main_label_3.setGeometry(QtCore.QRect(0, 80, 701, 91))
                        self.Delta_image_frame_preview.setGeometry(QtCore.QRect(330, 170, 340, 340))
                        self.Delta_image_label_preview.setGeometry(QtCore.QRect(410, 510, 271, 31))
                        flagIt = True
                        return 0

        def plot_expressions(self):
                self.Plot_BTN_generate.clicked.connect(lambda: self.plot_generate_btn_function())
                self.Derivative_BTN_compute.clicked.connect(lambda: self.derivative_compute_btn_function())
                self.Integral_BTN_compute.clicked.connect(lambda: self.integral_compute_btn_function())
                self.d_Integral_BTN_compute.clicked.connect(lambda: self.d_integral_compute_btn_function())
                self.c_Integral_BTN_compute.clicked.connect(lambda: self.c_integral_compute_btn_function())
                self.Delta_BTN_compute_2.clicked.connect(lambda: self.delta_compute_btn_function())

                

        def plot_generate_btn_function(self):     
                try:
                        def Plot_checking_blank_brackets(x, a, b):
                                if x == '' or a == '' or b == '':
                                        self.Plot_error_info.setVisible(True)
                                        self.Plot_error_info.setCurrentWidget(self.error_widget_1)
                                        return False
                                else:
                                        return True
                        def Plot_checking_correct_datatypes(Enable):
                                if Enable:
                                        if 'x' in self.Plot_fn_edit.text():
                                                self.x1 = float(self.Plot_range_x1.text())
                                                self.x2 = float(self.Plot_range_x2.text())
                                                if self.x2 > self.x1:
                                                        self.Plot_range_values = [self.x1, self.x2]
                                                        return True
                                                self.Plot_error_info.setCurrentWidget(self.error_widget_2)
                                                return False
                                        else:
                                                self.Plot_error_info.setCurrentWidget(self.error_widget_2)
                                                return False
                                else: 
                                        return False
                        def Plot_counting_erase_data(RG, Enable):
                                if Enable:
                                        self.Data_x_axis = []
                                        self.Data_y_axis = []
                                        self.x1 = RG[0]
                                        self.x2 = RG[1]
                                        self.Dens = 200
                                        self.Step = (self.x2-self.x1)/self.Dens
                                        for i in range(1, self.Dens+2):
                                                self.Data_x_axis.append(float("{:.2f}".format(self.x1+(i-1)*self.Step)))
                                        for x in self.Data_x_axis:
                                                x = float(x)
                                                self.y_res = eval(self.Plot_fn_edit.text())
                                                self.Data_y_axis.append(self.y_res)
                                        self.Plot_error_info.setVisible(False)
                                        return (self.Data_x_axis, self.Data_y_axis)                                              
                        def Plot_range_plot_value_function(Data):
                                self.x1 = np.max(Data[0]) 
                                self.x2 = np.max(Data[1])
                                if self.x1 >= self.x2:
                                        return self.x1
                                else:
                                        return self.x2
                        def Plot_figure_positioning(Data):
                                self.x1 = np.min(Data[0])
                                self.x2 = np.max(Data[0])
                                self.y1 = np.min(Data[1])
                                self.y2 = np.max(Data[1])
                                return (self.x1-1, self.x2+1), (self.y1-1, self.y2+1)
                        def Plot_figure_lim(Data):
                                plt.xlim(Data[0])
                                plt.ylim(Data[1])
                                return True
                        def Plot_figure_draw(Enable, Data, Range):
                                if Enable:
                                        plt.close('all')
                                        plt.grid(True, color='black', linewidth=0.5)
                                        plt.axhline(color = 'k')
                                        plt.axvline(color = 'k')
                                        plt.plot(Data[0], Data[1], color=self.Plot_combo_color.currentText(),label='Figure',linewidth=2)
                                        plt.savefig(path+'/figure-preview-img.png')
                                        self.Plot_preview_label.setPixmap(QtGui.QPixmap(path+"/figure-preview-img.png"))
                                        plt.show()
                                        return True
                                        
                        self.Plot_range_values = []
                        self.Flag_Plot_checking_blank_brackets = Plot_checking_blank_brackets(self.Plot_fn_edit.text(), self.Plot_range_x1.text(), self.Plot_range_x2.text())
                        self.Flag_Plot_checking_correct_datatypes = Plot_checking_correct_datatypes(self.Flag_Plot_checking_blank_brackets)
                        self.Plot_figure_data = Plot_counting_erase_data(self.Plot_range_values, self.Flag_Plot_checking_correct_datatypes)
                        self.Plot_range_plot_value = Plot_range_plot_value_function(self.Plot_figure_data)
                        self.Plot_figure_positioning_value = Plot_figure_positioning(self.Plot_figure_data)
                        self.Plot_figure_lim_flag = Plot_figure_lim(self.Plot_figure_positioning_value)
                        self.Plot_figure_draw_flag = Plot_figure_draw(self.Plot_figure_lim_flag, self.Plot_figure_data ,self.Plot_figure_positioning_value)
                  
                except:
                        self.Plot_error_info.setVisible(True)
                        self.Plot_error_info.setCurrentWidget(self.error_widget_2)

        def plot_save_btn_function(self):
                self.Plot_error_info.setVisible(True)
                self.Plot_error_info.setCurrentWidget(self.Plot_figure_saved_widget)

        def derivative_compute_btn_function(self):  
                try:
                        def Derivative_checking_blank_brackets(x, R1, R2):
                                if x == '' or R1 == '' or R2 == '':
                                        self.stackedWidget_3.setVisible(True)
                                        self.stackedWidget_3.setCurrentWidget(self.error_widget_4)
                                        return False
                                else:
                                        return True
                        
                        def Derivative_checking_correct_datatypes(Enable, Data):
                                if Enable:
                                        return True
                                else:
                                        return False

                        def Derivative_compute(Enable, Data):
                                global Derivative_final_result
                                if Enable:
                                        self.x = sp.Symbol('x')
                                        Derivative_final_result = sp.diff(Data, self.x)
                                        return True
                                else:
                                        return False

                        def Derivative_show_result(Enable):
                                if Enable:
                                        self.stackedWidget_3.setVisible(False)
                                        self.Derivative_label_fxpr_res.setText(str(Derivative_final_result))
                                        return True
                                else:
                                        return False

                        def Derivative_draw_figures(Enable, Data_Input, Data_Output, R1, R2):
                                if Enable:
                                        self.Data_x_axis = []
                                        self.Data_y_axis = []
                                        self.Data_dydx_axis = []
                                        self.Dens = 20
                                        self.x1 = float(R1)
                                        self.x2 = float(R2)
                                        self.Step = (self.x2-self.x1)/self.Dens
                                        for i in range(1, self.Dens+2):
                                                self.Data_x_axis.append(float("{:.2f}".format(self.x1+(i-1)*self.Step)))
                                        for x in self.Data_x_axis:
                                                x = float(x)
                                                self.res_y = eval(Data_Input)
                                                self.res_dydx = eval(str(Data_Output))
                                                self.Data_y_axis.append(self.res_y)
                                                self.Data_dydx_axis.append(self.res_dydx)
                                        
                                        plt.grid(True, color='black', linewidth=0.5)
                                        plt.plot(self.Data_x_axis,self.Data_y_axis, color='Blue',label=Data_Input,linewidth=2)
                                        plt.plot(self.Data_x_axis,self.Data_dydx_axis, color='Red',label=Data_Output,linewidth=2)
                                        plt.axhline(color = 'k')
                                        plt.axvline(color = 'k')
                                        plt.legend()
                                        plt.savefig(path+'/figure-dydx-img.png')
                                        self.Derivative_preview_label_dxdy.setPixmap(QtGui.QPixmap(path+'/figure-dydx-img.png'))
                                        self.stackedWidget_3.setVisible(True)
                                        self.stackedWidget_3.setCurrentWidget(self.correct_widget_4)
                                        plt.show()            
                                        return True
                                else:
                                        return False

                        self.Derivative_checking_blank_brackets_Flag = Derivative_checking_blank_brackets(self.Derivative_input_value.text(),self.Derivative_range_x1.text(),self.Derivative_range_x2.text())
                        self.Derivative_checking_correct_datatypes_Flag = Derivative_checking_correct_datatypes(self.Derivative_checking_blank_brackets_Flag, self.Derivative_input_value.text())
                        self.Derivative_compute_flag = Derivative_compute(self.Derivative_checking_correct_datatypes_Flag, self.Derivative_input_value.text())
                        self.Derivative_show_result_flag = Derivative_show_result(self.Derivative_compute_flag)
                        self.Derivative_draw_figures_flag = Derivative_draw_figures(
                                self.Derivative_show_result_flag,
                                self.Derivative_input_value.text(),
                                Derivative_final_result, 
                                self.Derivative_range_x1.text(), 
                                self.Derivative_range_x2.text())
     
                except:
                        self.stackedWidget_3.setVisible(True)
                        self.stackedWidget_3.setCurrentWidget(self.error_widget_5)
        
        def integral_compute_btn_function(self):
                try:
                        def Integral_checking_blank_brackets(x, R1, R2):
                                if x == '' or R1 == '' or R2 == '':
                                        self.stackedWidget_4.setVisible(True)
                                        self.stackedWidget_4.setCurrentWidget(self.error_widget_6)
                                        return False
                                else:
                                        return True
                        def Integral_checking_correct_datatypes(Enable, Data, R1, R2):
                                if Enable:
                                        if float(R2) > float(R1):
                                                return True
                                        else:
                                                return False
                                else:
                                        return False

                        def Integral_compute(Enable, Data):
                                global Integral_final_result
                                if Enable:
                                        self.x = sp.Symbol('x')
                                        Integral_final_result = sp.integrate(Data, self.x)
                                        return True
                                else:
                                        return False
                        
                        def Integral_show_result(Enable):
                                if Enable:
                                        self.Integral_label_fxpr_res.setText(str(Integral_final_result)+'+C')
                                        return True
                                else:
                                        return False

                        def Intgeral_draw_figures(Enable, Data_Input, Data_Output, R1, R2):
                                if Enable:
                                        plt.close('all')
                                        self.Data_x_axis = []
                                        self.Data_y_axis = []
                                        self.Data_inte_axis = []
                                        self.Dens = 500
                                        self.x1 = float(R1)
                                        self.x2 = float(R2)
                                        self.R = [self.x1, self.x2]

                                        self.dx_plt = self.x2 - self.x1
                                        self.dx_plt = self.dx_plt * 0.25
                                        
                                        self.dx1_plt = self.x1 - self.dx_plt
                                        self.dx2_plt = self.x2 + self.dx_plt

                                        self.Step = (self.dx2_plt-self.dx1_plt)/self.Dens
                                        for i in range(1, self.Dens+2):
                                                self.Data_x_axis.append(float("{:.2f}".format(self.dx1_plt+(i-1)*self.Step)))
                                        for x in self.Data_x_axis:
                                                x = float(x)
                                                self.res_y = eval(Data_Input)
                                                self.res_inte = eval(str(Data_Output))
                                                self.Data_y_axis.append(self.res_y)
                                                self.Data_inte_axis.append(self.res_inte)

                                        self.Data_x_axis = np.array(self.Data_x_axis)
                                        self.Data_y_axis = np.array(self.Data_y_axis)
                                        self.Data_inte_axis = np.array(self.Data_inte_axis)

                                        self.P_arr = []
                                        for x in self.R[::-1]:
                                                self.Pd = eval(str(Integral_final_result))
                                                self.P_arr.append(self.Pd)
                                        self.P = self.P_arr[0] - self.P_arr[1]
                                        self.P = "{:.3f}".format(self.P)
                                        self.Integral_label_P_res.setText(str(self.P))

                                        plt.grid(True, color='black', linewidth=0.5)
                                        plt.plot(self.Data_x_axis,self.Data_y_axis, color='Red',label=Data_Input,linewidth=1)
                                        plt.plot(self.Data_x_axis,self.Data_inte_axis, color='Blue',label=Data_Output,linewidth=1)
                                        plt.fill_between(self.Data_x_axis,self.Data_y_axis, 0, where=(self.Data_x_axis >= self.x1) & (self.Data_x_axis <= self.x2), color='Red', alpha=0.5)
                                        plt.axhline(color = 'k')
                                        plt.axvline(color = 'k')
                                        plt.legend()
                                        plt.savefig(path+'/figure-inte-img.png')
                                        self.Integral_image_label_preview_fig.setPixmap(QtGui.QPixmap(path+"/figure-inte-img.png"))
                                        self.stackedWidget_4.setVisible(True)
                                        self.stackedWidget_4.setCurrentWidget(self.correct_widget_7)
                                        plt.show()
                                else:
                                        self.stackedWidget_4.setVisible(True)
                                        self.stackedWidget_4.setCurrentWidget(self.error_widget_7)
                                        
   
                        self.Integral_checking_blank_brackets_flag = Integral_checking_blank_brackets(self.Integral_input_value.text(), self.Integral_range_x1.text(), self.Integral_range_x2.text())
                        self.Integral_checking_correct_datatypes_flag = Integral_checking_correct_datatypes(self.Integral_checking_blank_brackets_flag, self.Integral_input_value.text(), self.Integral_range_x1.text(), self.Integral_range_x2.text())
                        self.Integral_compute_flag = Integral_compute(self.Integral_checking_correct_datatypes_flag, self.Integral_input_value.text())
                        self.Integral_show_result_flag = Integral_show_result(self.Integral_compute_flag)
                        Intgeral_draw_figures(
                                self.Integral_show_result_flag,
                                self.Integral_input_value.text(),
                                Integral_final_result,
                                self.Integral_range_x1.text(),
                                self.Integral_range_x2.text()
                        )

                except:
                        self.stackedWidget_4.setVisible(True)
                        self.stackedWidget_4.setCurrentWidget(self.error_widget_7)

        def d_integral_compute_btn_function(self):
                try:
                        def d_Integral_checking_blank_brackets(x, RX1, RX2, RY1, RY2):
                                if x == '' or RX1 == '' or RX2 == '' or RY1 == '' or RY2 == '':
                                        self.stackedWidget_5.setVisible(True)
                                        self.stackedWidget_5.setCurrentWidget(self.error_widget_8)
                                        return False
                                else:
                                        return True
                        def d_Integral_checking_correct_datatypes(Enable, Data, RX1, RX2, RY1, RY2):
                                if Enable:
                                        if float(RX2) > float(RX1) and float(RY2) > float(RY1):
                                                return True
                                        else:
                                                return False
                                else:
                                        return False

                        def d_Integral_compute(Enable, Data, RX1, RX2, RY1, RY2):
                                global d_Integral_final_result_symbolic, d_Integral_final_result_area
                               
                                if Enable:
                                        self.x = sp.Symbol('x')
                                        self.y = sp.Symbol('y')
                                        self.d_Integral_final_result_x = sp.integrate(Data, self.x)
                                        self.d_Integral_final_result_y = sp.integrate(self.d_Integral_final_result_x, self.y)
                                        d_Integral_final_result_symbolic = self.d_Integral_final_result_y
                                        
                                        self.f = lambda y, x: eval(Data)
                                        d_Integral_final_result_area = integrate.dblquad(self.f, float(RX1), float(RX2), lambda x: float(RY1), lambda x: float(RY2))
                                        return True
                                else:
                                        return False
                        
                        def d_Integral_show_result(Enable):
                                if Enable:
                                        self.stackedWidget_5.setVisible(False) 
                                        self.d_Integral_label_fxpr_res.setText(str(d_Integral_final_result_symbolic)+'+C')
                                        self.d_Integral_label_P_res.setText(str("{:.3f}".format(d_Integral_final_result_area[0])))
                                        return True
                                else:
                                        return False

                        def d_Integral_draw_figures(Enable, Data_Input, Data_Output, RX1, RX2, RY1, RY2):
                                if Enable:
                                        plt.close('all')
                                        self.Data_a = np.array([float(RX1), float(RX2)])
                                        self.Data_b1 = np.array([float(RY1), float(RY1)])
                                        self.Data_b2 = np.array([float(RY2), float(RY2)])
                                        plt.fill_between(self.Data_a, self.Data_b1, self.Data_b2, color='red', alpha=0.75)
                                        plt.grid(True, color='black', linewidth=0.5)
                                        self.Data_fn = np.array([float(RX1), float(RX2), float(RY1), float(RY2)])
                                        for i in range(len(self.Data_fn)):
                                                if 0 > self.Data_fn[i]:
                                                        self.Data_fn[i] = self.Data_fn[i]*(-1)
                                        self.range = max(self.Data_fn)
                                        plt.axhline(color = 'k')
                                        plt.axvline(color = 'k')
                                        plt.xlim(self.range*(-1)*1.2,self.range*1.2)
                                        plt.ylim(self.range*(-1)*1.2,self.range*1.2)
                                        plt.savefig(path+'/figure-dinte-img.png')
                                        self.d_Integral_image_label_preview_fig.setPixmap(QtGui.QPixmap(path+"/figure-dinte-img.png"))
                                        self.stackedWidget_5.setVisible(True)
                                        self.stackedWidget_5.setCurrentWidget(self.correct_widget_9) 
                                        plt.show()

                        self.d_Integral_checking_blank_brackets_flag = d_Integral_checking_blank_brackets(
                                self.d_Integral_input_value.text(),
                                self.d_Integral_range_x1.text(),
                                self.d_Integral_range_x2.text(),
                                self.d_Integral_range_y1.text(),
                                self.d_Integral_range_y2.text()
                                )

                        self.d_Integral_checking_correct_datatypes_flag = d_Integral_checking_correct_datatypes(
                                self.d_Integral_checking_blank_brackets_flag, 
                                self.d_Integral_input_value.text(),
                                self.d_Integral_range_x1.text(),
                                self.d_Integral_range_x2.text(),
                                self.d_Integral_range_y1.text(),
                                self.d_Integral_range_y2.text()                        
                                )

                        self.d_Integral_compute_flag = d_Integral_compute(
                                self.d_Integral_checking_correct_datatypes_flag, 
                                self.d_Integral_input_value.text(),
                                self.d_Integral_range_x1.text(),
                                self.d_Integral_range_x2.text(),
                                self.d_Integral_range_y1.text(),
                                self.d_Integral_range_y2.text()  
                                )

                        self.d_Integral_show_result_flag = d_Integral_show_result(self.d_Integral_compute_flag)
                        d_Integral_draw_figures(
                                self.d_Integral_show_result_flag,
                                self.d_Integral_input_value.text(),
                                d_Integral_final_result_symbolic,
                                self.d_Integral_range_x1.text(),
                                self.d_Integral_range_x2.text(),
                                self.d_Integral_range_y1.text(),
                                self.d_Integral_range_y2.text()  
                        )

                except:
                        self.stackedWidget_5.setVisible(True)
                        self.stackedWidget_5.setCurrentWidget(self.error_widget_9) 

        def c_integral_compute_btn_function(self):
                try:
                        def c_Integral_checking_blank_brackets(x, RX1, RX2, RY1, RY2, RZ1, RZ2):
                                if x == '' or RX1 == '' or RX2 == '' or RY1 == '' or RY2 == '' or RZ1 == '' or RZ2 == '':
                                        self.stackedWidget_6.setVisible(True)
                                        self.stackedWidget_6.setCurrentWidget(self.error_widget_10)
                                        return False
                                else:
                                        return True
                        def c_Integral_checking_correct_datatypes(Enable, Data, RX1, RX2, RY1, RY2, RZ1, RZ2):
                                if Enable:
                                        if float(RX2) > float(RX1) and float(RY2) > float(RY1) and float(RZ2) > float(RZ1):
                                                return True
                                        else:
                                                return False
                                else:
                                        return False
                        def c_Integral_compute(Enable, Data, RX1, RX2, RY1, RY2, RZ1, RZ2):
                                global c_Integral_final_result_symbolic, c_Integral_final_result_volume
                               
                                if Enable:
                                        self.x = sp.Symbol('x')
                                        self.y = sp.Symbol('y')
                                        self.z = sp.Symbol('z')
                                        self.c_Integral_symbolic_result_x = sp.integrate(Data, self.x)
                                        self.c_Integral_symbolic_result_y = sp.integrate(self.c_Integral_symbolic_result_x, self.y)
                                        self.c_Integral_symbolic_result_z = sp.integrate(self.c_Integral_symbolic_result_y, self.z)
                                        c_Integral_final_result_symbolic = self.c_Integral_symbolic_result_z
                                        self.f = lambda z, y, x: eval(Data)
                                        c_Integral_final_result_volume = integrate.tplquad(self.f, float(RX1), float(RX2), 
                                        lambda x: float(RY1), lambda x: float(RY2),
                                        lambda x, y: float(RZ1), lambda x, y: float(RZ2)
                                        )
                                        return True
                                else:
                                        return False
                        
                        def c_Integral_show_result(Enable):
                                if Enable:
                                        self.stackedWidget_5.setVisible(False) 
                                        self.c_Integral_label_symbolic_res.setText(str(c_Integral_final_result_symbolic)+'+C')
                                        self.c_Integral_label_volume_res.setText(str("{:.3f}".format(c_Integral_final_result_volume[0])))
                                        return True
                                else:
                                        return False

                        def c_Integral_draw_figures(Enable, Data_Input, Data_Output, RX1, RX2, RY1, RY2, RZ1, RZ2):
                                if Enable:
                                        rx1, rx2, ry1, ry2, rz1, rz2 = float(RX1), float(RX2), float(RY1), float(RY2), float(RZ1), float(RZ2)
                                        nx = (rx2 + rx1)/2
                                        ny = (ry2 + ry1)/2
                                        nz = (rz2 + rz1)/2
                                        
                                        dx = rx2 - rx1
                                        dy = ry2 - ry1
                                        dz = rz2 - rz1

                                        def Xaxisrange(x1, x2, dx, nx):
                                                if x1 <= 0 and x2 >= 0:
                                                        Tx = 1.2*dx
                                                elif x1 > 0:
                                                        Tx = 1.5*nx
                                                elif x2 < 0:
                                                        Tx = -1.5*nx
                                                return Tx

                                        def Yaxisrange(y1, y2, dy, ny):
                                                if y1 <= 0 and y2 >= 0:
                                                        Ty = 1.2*dy
                                                elif y1 > 0:
                                                        Ty = 1.5*ny
                                                elif y2 < 0:
                                                        Ty = -1.5*ny
                                                return Ty

                                        def Zaxisrange(z1, z2, dz, nz):
                                                if z1 <= 0 and z2 >= 0:
                                                        Tz = 1.2*dz
                                                elif z1 > 0:
                                                        Tz = 1.5*nz
                                                elif z2 < 0:
                                                        Tz = -1.5*nz
                                                return Tz

                                        plt.close('all')
                                        Range_X = Xaxisrange(rx1, rx2, dx, nx)
                                        Range_Y = Yaxisrange(ry1, ry2, dy, ny)
                                        Range_Z = Zaxisrange(rz1, rz2, dz, nz)

                                        fig = plt.figure()
                                        ax = fig.add_subplot(111, projection='3d')
                                        ax1 = fig.gca(projection='3d')

                                        ax.set_xlim(-Range_X,Range_X)
                                        ax.set_ylim(-Range_Y,Range_Y)
                                        ax.set_zlim(-Range_Z,Range_Z)

                                        self.x1 = np.array([[nx,rx1,rx1,nx],[nx,rx1,rx1,nx],[nx,rx2,rx2,nx],[nx,rx2,rx2,nx],[nx,rx1,rx1,nx]])
                                        self.y1 = np.array([[ny,ry1,ry1,ny],[ny,ry2,ry2,ny],[ny,ry2,ry2,ny],[ny,ry1,ry1,ny],[ny,ry1,ry1,ny]])
                                        self.z1 = np.array([[rz1,rz1,rz2,rz2],[rz1,rz1,rz2,rz2],[rz1,rz1,rz2,rz2],[rz1,rz1,rz2,rz2],[rz1,rz1,rz2,rz2]])

                                        self.XaxisDrawX = [-Range_X, Range_X]
                                        self.YaxisDrawX = self.ZaxisDrawX = [0, 0] 

                                        self.YaxisDrawY = [-Range_Y, Range_Y]
                                        self.XaxisDrawY = self.ZaxisDrawY = [0, 0]

                                        self.ZaxisDrawZ = [-Range_Z, Range_Z]
                                        self.YaxisDrawZ = self.XaxisDrawZ = [0, 0] 

                                        ax.set_xlabel('X axis')
                                        ax.set_ylabel('Y axis')
                                        ax.set_zlabel('Z axis')

                                        ax.plot_surface(self.x1, self.y1, self.z1, color='r')
                                        ax1.plot(self.XaxisDrawX, self.YaxisDrawX, self.ZaxisDrawX, color='black', linewidth=1)
                                        ax1.plot(self.XaxisDrawY, self.YaxisDrawY, self.ZaxisDrawY, color='black', linewidth=1)
                                        ax1.plot(self.XaxisDrawZ, self.YaxisDrawZ, self.ZaxisDrawZ, color='black', linewidth=1)

                                        plt.savefig(path+'/figure-cinte-img.png')
                                        self.c_Integral_image_label_preview_fig.setPixmap(QtGui.QPixmap(path+"/figure-cinte-img.png"))
                                        self.stackedWidget_5.setVisible(True)
                                        self.stackedWidget_5.setCurrentWidget(self.correct_widget_9) 
                                        plt.show()

                        self.c_Integral_checking_blank_brackets_flag = c_Integral_checking_blank_brackets(
                                        self.c_Integral_input_value_fx.text(),
                                        self.c_Integral_input_value_x1.text(),
                                        self.c_Integral_input_value_x2.text(),
                                        self.c_Integral_input_value_y1.text(),
                                        self.c_Integral_input_value_y2.text(),
                                        self.c_Integral_input_value_z1.text(),
                                        self.c_Integral_input_value_z2.text()
                        )

                        self.c_Integral_checking_correct_datatypes_flag = c_Integral_checking_correct_datatypes(
                                        self.c_Integral_checking_blank_brackets_flag,
                                        self.c_Integral_input_value_fx.text(),
                                        self.c_Integral_input_value_x1.text(),
                                        self.c_Integral_input_value_x2.text(),
                                        self.c_Integral_input_value_y1.text(),
                                        self.c_Integral_input_value_y2.text(),
                                        self.c_Integral_input_value_z1.text(),
                                        self.c_Integral_input_value_z2.text()
                        )

                        self.c_Integral_compute_flag = c_Integral_compute(
                                        self.c_Integral_checking_correct_datatypes_flag,
                                        self.c_Integral_input_value_fx.text(),
                                        self.c_Integral_input_value_x1.text(),
                                        self.c_Integral_input_value_x2.text(),
                                        self.c_Integral_input_value_y1.text(),
                                        self.c_Integral_input_value_y2.text(),
                                        self.c_Integral_input_value_z1.text(),
                                        self.c_Integral_input_value_z2.text()
                        )

                        self.c_Integral_show_result_flag = c_Integral_show_result(self.c_Integral_compute_flag)

                        c_Integral_draw_figures(
                                        self.c_Integral_show_result_flag,
                                        self.c_Integral_input_value_fx.text(),
                                        c_Integral_final_result_symbolic,
                                        self.c_Integral_input_value_x1.text(),
                                        self.c_Integral_input_value_x2.text(),
                                        self.c_Integral_input_value_y1.text(),
                                        self.c_Integral_input_value_y2.text(),
                                        self.c_Integral_input_value_z1.text(),
                                        self.c_Integral_input_value_z2.text()
                        )


                except:
                        self.stackedWidget_6.setVisible(True)
                        self.stackedWidget_6.setCurrentWidget(self.error_widget_11) 

        def delta_compute_btn_function(self):
                try:
                        def Delta_checking_blank_brackets(A):
                                if A == '':
                                        self.stackedWidget_7.setVisible(True)
                                        self.stackedWidget_7.setCurrentWidget(self.error_widget_12) 
                                        return False
                                else: 
                                        return True
                                        
                        def Delta_checking_correct_datatypes(Enable, A, B, C):
                                global A_value, B_value, C_value
                                if Enable:
                                        if float(A) == 0:
                                                return False
                                        else:
                                                A_value = float(A)
                                        if B == '':
                                                B_value = 0
                                        else:
                                                B_value = float(B)
                                        if C == '':
                                                C_value = 0
                                        else:
                                                C_value = float(C)
                                        return True
                                else: 
                                        return False

                        def Delta_computing_values(Enable, A, B, C):
                                global Delta_final_results
                                if Enable:
                                        delta = B**2-4*A*C
                                        if delta > 0:
                                                x1 = float("{:.2f}".format(((-B-math.sqrt(delta)))/(2*A)))
                                                x2 = float("{:.2f}".format(((-B+math.sqrt(delta)))/(2*A)))
                                                Delta_final_results = [x1, x2]
                                        elif delta == 0:
                                                x0 = float("{:.2f}".format(-B/2*A))
                                                Delta_final_results = [x0]
                                        else:
                                                Delta_final_results = []
                                        return True
                                else:
                                        return False

                        def Delta_draw_plot(Enable, DATA, A, B, C):
                                if Enable:
                                        def Delta_checking_soultion_ammount(data, A, B, C):                              
                                                if len(data) == 2:
                                                        x1 = data[0]
                                                        x2 = data[1]
                                                        dx = x2- x1
                                                        x_data = np.linspace(x1-dx,x2+dx,100)
                                                        self.Delta_label_result_x1.setText(str(data[1]))
                                                        self.Delta_label_result_x2.setText(str(data[0]))
                                                        return x_data
                                                elif len(data) == 1:
                                                        x0 = data[0]
                                                        x_data = np.linspace(x0-3,x0+3,100)
                                                        self.Delta_label_result_x1.setText(str(x0))
                                                        self.Delta_label_result_x2.setText('-')
                                                        return x_data
                                                elif len(data) == 0:
                                                        p = -B/(2*A)
                                                        x_data = np.linspace(p-3,p+3,100)
                                                        self.Delta_label_result_x1.setText('-')
                                                        self.Delta_label_result_x2.setText('-')
                                                        return x_data
                                        def Delta_y_get_data(x,A,B,C):
                                                return A*x**2+B*x+C

                                        def delta_figure_close_event(event):
                                                global delta_close_figure_flag
                                                delta_close_figure_flag = True

                                        plt.close('all')
                                        data_x_axis = Delta_checking_soultion_ammount(DATA,A,B,C)
                                        data_y_axis = Delta_y_get_data(data_x_axis,A,B,C)
                                        self.stackedWidget_7.setVisible(True)
                                        self.stackedWidget_7.setCurrentWidget(self.correct_widget_14)
                                        fig = plt.figure()
                                        fig.canvas.mpl_connect('close_event', delta_figure_close_event)
                                        plt.plot(data_x_axis, data_y_axis, color='Blue')
                                        plt.plot(DATA, np.full_like(DATA, 0), 'ro', color='Red')
                                        plt.grid()
                                        plt.axhline(color = 'k')
                                        plt.axvline(color = 'k')
                                        plt.savefig(path+'/figure-quadeq-img.png')
                                        self.Delta_image_label_preview_fig.setPixmap(QtGui.QPixmap(path+"/figure-quadeq-img.png"))
                                        delta_close_figure_flag = False
                                        plt.show()

                        Delta_checking_blank_brackets_flag = Delta_checking_blank_brackets(
                                self.Delta_input_value_A.text(), 
                        )

                        Delta_checking_correct_datatypes_flag = Delta_checking_correct_datatypes(
                                Delta_checking_blank_brackets_flag,
                                self.Delta_input_value_A.text(),
                                self.Delta_input_value_B.text(), 
                                self.Delta_input_value_C.text(),  
                        )

                        Delta_computing_values_flag = Delta_computing_values(
                                Delta_checking_correct_datatypes_flag,
                                A_value,
                                B_value, 
                                C_value,  
                        )
                        Delta_draw_plot(
                                Delta_computing_values_flag,
                                Delta_final_results,
                                A_value,
                                B_value, 
                                C_value,                           
                        )
                except:
                        self.stackedWidget_7.setVisible(True)
                        self.stackedWidget_7.setCurrentWidget(self.error_widget_13) 

if __name__ == "__main__":
    global path
    userprofile = os.environ['USERPROFILE']
    path = os.path.join(userprofile, 'Pictures')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle('Scientific Calculator')
    sys.exit(app.exec_())
