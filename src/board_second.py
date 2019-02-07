# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'board.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import socket
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from src.network import *
from src.util import *
from src.deta_def import *
from random import *
import time
from src.processing import *
from src.minimax import *
from datetime import datetime


class Ui_MainWindow(object):
    def __init__(self, ip):
        self.ip = ip
        self.my_stone_color = None  # 1: black, 2: white
        self.opponent_stone_color = None
        self.val = None
        self.point = None
        self.available_position_num = None
        self.changed_points = None
        self.client_msg = None
        self.pushButton = [[0 for _ in range(8)] for _ in range(8)]

        self.board = np.zeros((8, 8), dtype=int)
        self.board[3][3] = STONE_COLOR.WHITE.value
        self.board[3][4] = STONE_COLOR.BLACK.value
        self.board[4][3] = STONE_COLOR.BLACK.value
        self.board[4][4] = STONE_COLOR.WHITE.value

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2_1 = QPushButton(self.centralwidget)
        self.pushButton_2_1.setMinimumSize(QSize(70, 70))
        self.pushButton_2_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_1.setText("")
        self.pushButton_2_1.setObjectName("pushButton_2_1")
        self.gridLayout.addWidget(self.pushButton_2_1, 2, 1, 1, 1)
        self.pushButton_1_7 = QPushButton(self.centralwidget)
        self.pushButton_1_7.setMinimumSize(QSize(70, 70))
        self.pushButton_1_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_7.setText("")
        self.pushButton_1_7.setObjectName("pushButton_1_7")
        self.gridLayout.addWidget(self.pushButton_1_7, 1, 7, 1, 1)
        self.pushButton_2_0 = QPushButton(self.centralwidget)
        self.pushButton_2_0.setMinimumSize(QSize(70, 70))
        self.pushButton_2_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_0.setText("")
        self.pushButton_2_0.setObjectName("pushButton_2_0")
        self.gridLayout.addWidget(self.pushButton_2_0, 2, 0, 1, 1)
        self.pushButton_3_2 = QPushButton(self.centralwidget)
        self.pushButton_3_2.setMinimumSize(QSize(70, 70))
        self.pushButton_3_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_2.setText("")
        self.pushButton_3_2.setObjectName("pushButton_3_2")
        self.gridLayout.addWidget(self.pushButton_3_2, 3, 2, 1, 1)
        self.pushButton_3_3 = QPushButton(self.centralwidget)
        self.pushButton_3_3.setMinimumSize(QSize(70, 70))
        self.pushButton_3_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_3.setText("")
        self.pushButton_3_3.setObjectName("pushButton_3_3")
        self.gridLayout.addWidget(self.pushButton_3_3, 3, 3, 1, 1)
        self.pushButton_2_7 = QPushButton(self.centralwidget)
        self.pushButton_2_7.setMinimumSize(QSize(70, 70))
        self.pushButton_2_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_7.setText("")
        self.pushButton_2_7.setObjectName("pushButton_2_7")
        self.gridLayout.addWidget(self.pushButton_2_7, 2, 7, 1, 1)
        self.pushButton_3_0 = QPushButton(self.centralwidget)
        self.pushButton_3_0.setMinimumSize(QSize(70, 70))
        self.pushButton_3_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_0.setText("")
        self.pushButton_3_0.setObjectName("pushButton_3_0")
        self.gridLayout.addWidget(self.pushButton_3_0, 3, 0, 1, 1)
        self.pushButton_0_5 = QPushButton(self.centralwidget)
        self.pushButton_0_5.setMinimumSize(QSize(70, 70))
        self.pushButton_0_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_5.setText("")
        self.pushButton_0_5.setObjectName("pushButton_0_5")
        self.gridLayout.addWidget(self.pushButton_0_5, 0, 5, 1, 1)
        self.pushButton_0_1 = QPushButton(self.centralwidget)
        self.pushButton_0_1.setMinimumSize(QSize(70, 70))
        self.pushButton_0_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_1.setText("")
        self.pushButton_0_1.setObjectName("pushButton_0_1")
        self.gridLayout.addWidget(self.pushButton_0_1, 0, 1, 1, 1)
        self.pushButton_0_3 = QPushButton(self.centralwidget)
        self.pushButton_0_3.setMinimumSize(QSize(70, 70))
        self.pushButton_0_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_3.setText("")
        self.pushButton_0_3.setObjectName("pushButton_0_3")
        self.gridLayout.addWidget(self.pushButton_0_3, 0, 3, 1, 1)
        self.pushButton_2_6 = QPushButton(self.centralwidget)
        self.pushButton_2_6.setMinimumSize(QSize(70, 70))
        self.pushButton_2_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_6.setText("")
        self.pushButton_2_6.setObjectName("pushButton_2_6")
        self.gridLayout.addWidget(self.pushButton_2_6, 2, 6, 1, 1)
        self.pushButton_3_1 = QPushButton(self.centralwidget)
        self.pushButton_3_1.setMinimumSize(QSize(70, 70))
        self.pushButton_3_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_1.setText("")
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.gridLayout.addWidget(self.pushButton_3_1, 3, 1, 1, 1)
        self.pushButton_2_4 = QPushButton(self.centralwidget)
        self.pushButton_2_4.setMinimumSize(QSize(70, 70))
        self.pushButton_2_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_4.setText("")
        self.pushButton_2_4.setObjectName("pushButton_2_4")
        self.gridLayout.addWidget(self.pushButton_2_4, 2, 4, 1, 1)
        self.pushButton_2_3 = QPushButton(self.centralwidget)
        self.pushButton_2_3.setMinimumSize(QSize(70, 70))
        self.pushButton_2_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_3.setText("")
        self.pushButton_2_3.setObjectName("pushButton_2_3")
        self.gridLayout.addWidget(self.pushButton_2_3, 2, 3, 1, 1)
        self.pushButton_2_5 = QPushButton(self.centralwidget)
        self.pushButton_2_5.setMinimumSize(QSize(70, 70))
        self.pushButton_2_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_5.setText("")
        self.pushButton_2_5.setObjectName("pushButton_2_5")
        self.gridLayout.addWidget(self.pushButton_2_5, 2, 5, 1, 1)
        self.pushButton_5_2 = QPushButton(self.centralwidget)
        self.pushButton_5_2.setMinimumSize(QSize(70, 70))
        self.pushButton_5_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_2.setText("")
        self.pushButton_5_2.setObjectName("pushButton_5_2")
        self.gridLayout.addWidget(self.pushButton_5_2, 5, 2, 1, 1)
        self.pushButton_3_6 = QPushButton(self.centralwidget)
        self.pushButton_3_6.setMinimumSize(QSize(70, 70))
        self.pushButton_3_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_6.setText("")
        self.pushButton_3_6.setObjectName("pushButton_3_6")
        self.gridLayout.addWidget(self.pushButton_3_6, 3, 6, 1, 1)
        self.pushButton_5_7 = QPushButton(self.centralwidget)
        self.pushButton_5_7.setMinimumSize(QSize(70, 70))
        self.pushButton_5_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_7.setText("")
        self.pushButton_5_7.setObjectName("pushButton_5_7")
        self.gridLayout.addWidget(self.pushButton_5_7, 5, 7, 1, 1)
        self.pushButton_6_0 = QPushButton(self.centralwidget)
        self.pushButton_6_0.setMinimumSize(QSize(70, 70))
        self.pushButton_6_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_0.setText("")
        self.pushButton_6_0.setObjectName("pushButton_6_0")
        self.gridLayout.addWidget(self.pushButton_6_0, 6, 0, 1, 1)
        self.pushButton_3_7 = QPushButton(self.centralwidget)
        self.pushButton_3_7.setMinimumSize(QSize(70, 70))
        self.pushButton_3_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_7.setText("")
        self.pushButton_3_7.setObjectName("pushButton_3_7")
        self.gridLayout.addWidget(self.pushButton_3_7, 3, 7, 1, 1)
        self.pushButton_6_1 = QPushButton(self.centralwidget)
        self.pushButton_6_1.setMinimumSize(QSize(70, 70))
        self.pushButton_6_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_1.setText("")
        self.pushButton_6_1.setObjectName("pushButton_6_1")
        self.gridLayout.addWidget(self.pushButton_6_1, 6, 1, 1, 1)
        self.pushButton_6_2 = QPushButton(self.centralwidget)
        self.pushButton_6_2.setMinimumSize(QSize(70, 70))
        self.pushButton_6_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_2.setText("")
        self.pushButton_6_2.setObjectName("pushButton_6_2")
        self.gridLayout.addWidget(self.pushButton_6_2, 6, 2, 1, 1)
        self.pushButton_4_5 = QPushButton(self.centralwidget)
        self.pushButton_4_5.setMinimumSize(QSize(70, 70))
        self.pushButton_4_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_5.setText("")
        self.pushButton_4_5.setObjectName("pushButton_4_5")
        self.gridLayout.addWidget(self.pushButton_4_5, 4, 5, 1, 1)
        self.pushButton_5_5 = QPushButton(self.centralwidget)
        self.pushButton_5_5.setMinimumSize(QSize(70, 70))
        self.pushButton_5_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_5.setText("")
        self.pushButton_5_5.setObjectName("pushButton_5_5")
        self.gridLayout.addWidget(self.pushButton_5_5, 5, 5, 1, 1)
        self.pushButton_6_3 = QPushButton(self.centralwidget)
        self.pushButton_6_3.setMinimumSize(QSize(70, 70))
        self.pushButton_6_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_3.setText("")
        self.pushButton_6_3.setObjectName("pushButton_6_3")
        self.gridLayout.addWidget(self.pushButton_6_3, 6, 3, 1, 1)
        self.pushButton_5_0 = QPushButton(self.centralwidget)
        self.pushButton_5_0.setMinimumSize(QSize(70, 70))
        self.pushButton_5_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_0.setText("")
        self.pushButton_5_0.setObjectName("pushButton_5_0")
        self.gridLayout.addWidget(self.pushButton_5_0, 5, 0, 1, 1)
        self.pushButton_4_2 = QPushButton(self.centralwidget)
        self.pushButton_4_2.setMinimumSize(QSize(70, 70))
        self.pushButton_4_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_2.setText("")
        self.pushButton_4_2.setObjectName("pushButton_4_2")
        self.gridLayout.addWidget(self.pushButton_4_2, 4, 2, 1, 1)
        self.pushButton_3_4 = QPushButton(self.centralwidget)
        self.pushButton_3_4.setMinimumSize(QSize(70, 70))
        self.pushButton_3_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_4.setText("")
        self.pushButton_3_4.setObjectName("pushButton_3_4")
        self.gridLayout.addWidget(self.pushButton_3_4, 3, 4, 1, 1)
        self.pushButton_4_0 = QPushButton(self.centralwidget)
        self.pushButton_4_0.setMinimumSize(QSize(70, 70))
        self.pushButton_4_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_0.setText("")
        self.pushButton_4_0.setObjectName("pushButton_4_0")
        self.gridLayout.addWidget(self.pushButton_4_0, 4, 0, 1, 1)
        self.pushButton_3_5 = QPushButton(self.centralwidget)
        self.pushButton_3_5.setMinimumSize(QSize(70, 70))
        self.pushButton_3_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_3_5.setText("")
        self.pushButton_3_5.setObjectName("pushButton_3_5")
        self.gridLayout.addWidget(self.pushButton_3_5, 3, 5, 1, 1)
        self.pushButton_5_3 = QPushButton(self.centralwidget)
        self.pushButton_5_3.setMinimumSize(QSize(70, 70))
        self.pushButton_5_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_3.setText("")
        self.pushButton_5_3.setObjectName("pushButton_5_3")
        self.gridLayout.addWidget(self.pushButton_5_3, 5, 3, 1, 1)
        self.pushButton_4_1 = QPushButton(self.centralwidget)
        self.pushButton_4_1.setMinimumSize(QSize(70, 70))
        self.pushButton_4_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_1.setText("")
        self.pushButton_4_1.setObjectName("pushButton_4_1")
        self.gridLayout.addWidget(self.pushButton_4_1, 4, 1, 1, 1)
        self.pushButton_4_4 = QPushButton(self.centralwidget)
        self.pushButton_4_4.setMinimumSize(QSize(70, 70))
        self.pushButton_4_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_4.setText("")
        self.pushButton_4_4.setObjectName("pushButton_4_4")
        self.gridLayout.addWidget(self.pushButton_4_4, 4, 4, 1, 1)
        self.pushButton_4_7 = QPushButton(self.centralwidget)
        self.pushButton_4_7.setMinimumSize(QSize(70, 70))
        self.pushButton_4_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_7.setText("")
        self.pushButton_4_7.setObjectName("pushButton_4_7")
        self.gridLayout.addWidget(self.pushButton_4_7, 4, 7, 1, 1)
        self.pushButton_4_6 = QPushButton(self.centralwidget)
        self.pushButton_4_6.setMinimumSize(QSize(70, 70))
        self.pushButton_4_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_6.setText("")
        self.pushButton_4_6.setObjectName("pushButton_4_6")
        self.gridLayout.addWidget(self.pushButton_4_6, 4, 6, 1, 1)
        self.pushButton_5_1 = QPushButton(self.centralwidget)
        self.pushButton_5_1.setMinimumSize(QSize(70, 70))
        self.pushButton_5_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_1.setText("")
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        self.gridLayout.addWidget(self.pushButton_5_1, 5, 1, 1, 1)
        self.pushButton_4_3 = QPushButton(self.centralwidget)
        self.pushButton_4_3.setMinimumSize(QSize(70, 70))
        self.pushButton_4_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_4_3.setText("")
        self.pushButton_4_3.setObjectName("pushButton_4_3")
        self.gridLayout.addWidget(self.pushButton_4_3, 4, 3, 1, 1)
        self.pushButton_5_4 = QPushButton(self.centralwidget)
        self.pushButton_5_4.setMinimumSize(QSize(70, 70))
        self.pushButton_5_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_4.setText("")
        self.pushButton_5_4.setObjectName("pushButton_5_4")
        self.gridLayout.addWidget(self.pushButton_5_4, 5, 4, 1, 1)
        self.pushButton_5_6 = QPushButton(self.centralwidget)
        self.pushButton_5_6.setMinimumSize(QSize(70, 70))
        self.pushButton_5_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_5_6.setText("")
        self.pushButton_5_6.setObjectName("pushButton_5_6")
        self.gridLayout.addWidget(self.pushButton_5_6, 5, 6, 1, 1)
        self.pushButton_7_1 = QPushButton(self.centralwidget)
        self.pushButton_7_1.setMinimumSize(QSize(70, 70))
        self.pushButton_7_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_1.setText("")
        self.pushButton_7_1.setObjectName("pushButton_7_1")
        self.gridLayout.addWidget(self.pushButton_7_1, 7, 1, 1, 1)
        self.pushButton_6_6 = QPushButton(self.centralwidget)
        self.pushButton_6_6.setMinimumSize(QSize(70, 70))
        self.pushButton_6_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_6.setText("")
        self.pushButton_6_6.setObjectName("pushButton_6_6")
        self.gridLayout.addWidget(self.pushButton_6_6, 6, 6, 1, 1)
        self.pushButton_7_3 = QPushButton(self.centralwidget)
        self.pushButton_7_3.setMinimumSize(QSize(70, 70))
        self.pushButton_7_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_3.setText("")
        self.pushButton_7_3.setObjectName("pushButton_7_3")
        self.gridLayout.addWidget(self.pushButton_7_3, 7, 3, 1, 1)
        self.pushButton_7_7 = QPushButton(self.centralwidget)
        self.pushButton_7_7.setMinimumSize(QSize(70, 70))
        self.pushButton_7_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_7.setText("")
        self.pushButton_7_7.setObjectName("pushButton_7_7")
        self.gridLayout.addWidget(self.pushButton_7_7, 7, 7, 1, 1)
        self.pushButton_7_2 = QPushButton(self.centralwidget)
        self.pushButton_7_2.setMinimumSize(QSize(70, 70))
        self.pushButton_7_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_2.setText("")
        self.pushButton_7_2.setObjectName("pushButton_7_2")
        self.gridLayout.addWidget(self.pushButton_7_2, 7, 2, 1, 1)
        self.pushButton_7_4 = QPushButton(self.centralwidget)
        self.pushButton_7_4.setMinimumSize(QSize(70, 70))
        self.pushButton_7_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_4.setText("")
        self.pushButton_7_4.setObjectName("pushButton_7_4")
        self.gridLayout.addWidget(self.pushButton_7_4, 7, 4, 1, 1)
        self.pushButton_7_5 = QPushButton(self.centralwidget)
        self.pushButton_7_5.setMinimumSize(QSize(70, 70))
        self.pushButton_7_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_5.setText("")
        self.pushButton_7_5.setObjectName("pushButton_7_5")
        self.gridLayout.addWidget(self.pushButton_7_5, 7, 5, 1, 1)
        self.pushButton_6_5 = QPushButton(self.centralwidget)
        self.pushButton_6_5.setMinimumSize(QSize(70, 70))
        self.pushButton_6_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_5.setText("")
        self.pushButton_6_5.setObjectName("pushButton_6_5")
        self.gridLayout.addWidget(self.pushButton_6_5, 6, 5, 1, 1)
        self.pushButton_6_7 = QPushButton(self.centralwidget)
        self.pushButton_6_7.setMinimumSize(QSize(70, 70))
        self.pushButton_6_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_7.setText("")
        self.pushButton_6_7.setObjectName("pushButton_6_7")
        self.gridLayout.addWidget(self.pushButton_6_7, 6, 7, 1, 1)
        self.pushButton_6_4 = QPushButton(self.centralwidget)
        self.pushButton_6_4.setMinimumSize(QSize(70, 70))
        self.pushButton_6_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_6_4.setText("")
        self.pushButton_6_4.setObjectName("pushButton_6_4")
        self.gridLayout.addWidget(self.pushButton_6_4, 6, 4, 1, 1)
        self.pushButton_7_0 = QPushButton(self.centralwidget)
        self.pushButton_7_0.setMinimumSize(QSize(70, 70))
        self.pushButton_7_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_0.setText("")
        self.pushButton_7_0.setObjectName("pushButton_7_0")
        self.gridLayout.addWidget(self.pushButton_7_0, 7, 0, 1, 1)
        self.pushButton_0_7 = QPushButton(self.centralwidget)
        self.pushButton_0_7.setMinimumSize(QSize(70, 70))
        self.pushButton_0_7.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_7.setText("")
        self.pushButton_0_7.setObjectName("pushButton_0_7")
        self.gridLayout.addWidget(self.pushButton_0_7, 0, 7, 1, 1)
        self.pushButton_1_0 = QPushButton(self.centralwidget)
        self.pushButton_1_0.setMinimumSize(QSize(70, 70))
        self.pushButton_1_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_0.setText("")
        self.pushButton_1_0.setObjectName("pushButton_1_0")
        self.gridLayout.addWidget(self.pushButton_1_0, 1, 0, 1, 1)
        self.pushButton_0_0 = QPushButton(self.centralwidget)
        self.pushButton_0_0.setMinimumSize(QSize(70, 70))
        self.pushButton_0_0.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_0.setText("")
        self.pushButton_0_0.setObjectName("pushButton_0_0")
        self.gridLayout.addWidget(self.pushButton_0_0, 0, 0, 1, 1)
        self.pushButton_0_4 = QPushButton(self.centralwidget)
        self.pushButton_0_4.setMinimumSize(QSize(70, 70))
        self.pushButton_0_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_4.setText("")
        self.pushButton_0_4.setObjectName("pushButton_0_4")
        self.gridLayout.addWidget(self.pushButton_0_4, 0, 4, 1, 1)
        self.pushButton_0_6 = QPushButton(self.centralwidget)
        self.pushButton_0_6.setMinimumSize(QSize(70, 70))
        self.pushButton_0_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_6.setText("")
        self.pushButton_0_6.setObjectName("pushButton_0_6")
        self.gridLayout.addWidget(self.pushButton_0_6, 0, 6, 1, 1)
        self.pushButton_0_2 = QPushButton(self.centralwidget)
        self.pushButton_0_2.setMinimumSize(QSize(70, 70))
        self.pushButton_0_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_0_2.setText("")
        self.pushButton_0_2.setObjectName("pushButton_0_2")
        self.gridLayout.addWidget(self.pushButton_0_2, 0, 2, 1, 1)
        self.pushButton_1_5 = QPushButton(self.centralwidget)
        self.pushButton_1_5.setMinimumSize(QSize(70, 70))
        self.pushButton_1_5.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_5.setText("")
        self.pushButton_1_5.setObjectName("pushButton_1_5")
        self.gridLayout.addWidget(self.pushButton_1_5, 1, 5, 1, 1)
        self.pushButton_1_3 = QPushButton(self.centralwidget)
        self.pushButton_1_3.setMinimumSize(QSize(70, 70))
        self.pushButton_1_3.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_3.setText("")
        self.pushButton_1_3.setObjectName("pushButton_1_3")
        self.gridLayout.addWidget(self.pushButton_1_3, 1, 3, 1, 1)
        self.pushButton_1_4 = QPushButton(self.centralwidget)
        self.pushButton_1_4.setMinimumSize(QSize(70, 70))
        self.pushButton_1_4.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_4.setText("")
        self.pushButton_1_4.setObjectName("pushButton_1_4")
        self.gridLayout.addWidget(self.pushButton_1_4, 1, 4, 1, 1)
        self.pushButton_1_1 = QPushButton(self.centralwidget)
        self.pushButton_1_1.setMinimumSize(QSize(70, 70))
        self.pushButton_1_1.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_1.setText("")
        self.pushButton_1_1.setObjectName("pushButton_1_1")
        self.gridLayout.addWidget(self.pushButton_1_1, 1, 1, 1, 1)
        self.pushButton_1_6 = QPushButton(self.centralwidget)
        self.pushButton_1_6.setMinimumSize(QSize(70, 70))
        self.pushButton_1_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_6.setText("")
        self.pushButton_1_6.setObjectName("pushButton_1_6")
        self.gridLayout.addWidget(self.pushButton_1_6, 1, 6, 1, 1)
        self.pushButton_1_2 = QPushButton(self.centralwidget)
        self.pushButton_1_2.setMinimumSize(QSize(70, 70))
        self.pushButton_1_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_1_2.setText("")
        self.pushButton_1_2.setObjectName("pushButton_1_2")
        self.gridLayout.addWidget(self.pushButton_1_2, 1, 2, 1, 1)
        self.pushButton_2_2 = QPushButton(self.centralwidget)
        self.pushButton_2_2.setMinimumSize(QSize(70, 70))
        self.pushButton_2_2.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_2_2.setText("")
        self.pushButton_2_2.setObjectName("pushButton_2_2")
        self.gridLayout.addWidget(self.pushButton_2_2, 2, 2, 1, 1)
        self.pushButton_7_6 = QPushButton(self.centralwidget)
        self.pushButton_7_6.setMinimumSize(QSize(70, 70))
        self.pushButton_7_6.setStyleSheet("background-color: rgb(54, 115, 74);")
        self.pushButton_7_6.setText("")
        self.pushButton_7_6.setObjectName("pushButton_7_6")
        self.gridLayout.addWidget(self.pushButton_7_6, 7, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setMinimumSize(QSize(100, 200))
        self.label.setFrameShape(QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QSize(100, 200))
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setLineWidth(2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QSize(200, 100))
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setLineWidth(2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QSize(100, 200))
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setLineWidth(2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QSize(100, 200))
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setLineWidth(2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # board init
        self.pushButton_3_3.setIcon(QIcon('../images/white_stone.png'))
        self.pushButton_3_3.setIconSize(QSize(55, 55))

        self.pushButton_3_4.setIcon(QIcon('../images/black_stone.png'))
        self.pushButton_3_4.setIconSize(QSize(55, 55))

        self.pushButton_4_3.setIcon(QIcon('../images/black_stone.png'))
        self.pushButton_4_3.setIconSize(QSize(55, 55))

        self.pushButton_4_4.setIcon(QIcon('../images/white_stone.png'))
        self.pushButton_4_4.setIconSize(QSize(55, 55))

        self.pushButton = [[self.pushButton_0_0, self.pushButton_0_1, self.pushButton_0_2, self.pushButton_0_3,
                            self.pushButton_0_4, self.pushButton_0_5, self.pushButton_0_6, self.pushButton_0_7],
                           [self.pushButton_1_0, self.pushButton_1_1, self.pushButton_1_2, self.pushButton_1_3,
                            self.pushButton_1_4, self.pushButton_1_5, self.pushButton_1_6, self.pushButton_1_7],
                           [self.pushButton_2_0, self.pushButton_2_1, self.pushButton_2_2, self.pushButton_2_3,
                            self.pushButton_2_4, self.pushButton_2_5, self.pushButton_2_6, self.pushButton_2_7],
                           [self.pushButton_3_0, self.pushButton_3_1, self.pushButton_3_2, self.pushButton_3_3,
                            self.pushButton_3_4, self.pushButton_3_5, self.pushButton_3_6, self.pushButton_3_7],
                           [self.pushButton_4_0, self.pushButton_4_1, self.pushButton_4_2, self.pushButton_4_3,
                            self.pushButton_4_4, self.pushButton_4_5, self.pushButton_4_6, self.pushButton_4_7],
                           [self.pushButton_5_0, self.pushButton_5_1, self.pushButton_5_2, self.pushButton_5_3,
                            self.pushButton_5_4, self.pushButton_5_5, self.pushButton_5_6, self.pushButton_5_7],
                           [self.pushButton_6_0, self.pushButton_6_1, self.pushButton_6_2, self.pushButton_6_3,
                            self.pushButton_6_4, self.pushButton_6_5, self.pushButton_6_6, self.pushButton_6_7],
                           [self.pushButton_7_0, self.pushButton_7_1, self.pushButton_7_2, self.pushButton_7_3,
                            self.pushButton_7_4, self.pushButton_7_5, self.pushButton_7_6, self.pushButton_7_7]]
        """
        for i in range(8):
            for j in range(8):
                self.pushButton[i][j].clicked.connect(lambda state, i=i, j=j: self.put_stone(state, i, j))
        """

        # network connect
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, 8472))

        self.network = Network(self.sock)
        self.network.server_msg.connect(self.msg_from_server_to_client)
        self.network.start()

    def msg_from_server_to_client(self, msg):
        time.sleep(0.3)
        # print(msg)
        if msg["type"] == 0:  # READY
            self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">READY</span></p>")

        elif msg["type"] == 1:  # START
            self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">START</span></p>")

            if msg["color"] == 1:  # BLACK
                self.my_stone_color = STONE_COLOR.BLACK.value
                self.opponent_stone_color = STONE_COLOR.WHITE.value

                pixmap = QPixmap('../images/black_stone2.png')
                pixmap = pixmap.scaled(90, 90)
                self.label_4.setAlignment(Qt.AlignCenter)
                self.label_4.setPixmap(pixmap)

                pixmap = QPixmap('../images/white_stone2.png')
                pixmap = pixmap.scaled(90, 90)
                self.label_5.setAlignment(Qt.AlignCenter)
                self.label_5.setPixmap(pixmap)

            else:  # WHITE
                self.my_stone_color = STONE_COLOR.WHITE.value
                self.opponent_stone_color = STONE_COLOR.BLACK.value

                pixmap = QPixmap('../images/white_stone2.png')
                pixmap = pixmap.scaled(90, 90)
                self.label_4.setAlignment(Qt.AlignCenter)
                self.label_4.setPixmap(pixmap)

                pixmap = QPixmap('../images/black_stone2.png')
                pixmap = pixmap.scaled(90, 90)
                self.label_5.setAlignment(Qt.AlignCenter)
                self.label_5.setPixmap(pixmap)

        elif msg["type"] == 2:  # TURN
            self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">MY<br>TURN</span></p>")

            if msg["opponent_put"] is not None:
                self.board[msg["opponent_put"][0]][msg["opponent_put"][1]] = self.opponent_stone_color
                self.rendering(self.opponent_stone_color, msg["opponent_put"][0], msg["opponent_put"][1])

                for i, j in msg["changed_points"]:
                    self.board[i, j] = self.opponent_stone_color
                    self.rendering(self.opponent_stone_color, i, j)

            self.point = ai()

            self.client_msg = serialize({'type': 0, 'point': self.point})
            self.sock.send(self.client_msg)

        elif msg["type"] == 3:  # ACCEPT
            self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">OPPONENT<br>TURN</span></p>")

            self.changed_points = getReversedPosition(self.board, self.my_stone_color, self.point[0], self.point[1])

            for i, j in self.changed_points:
                self.board[i, j] = self.my_stone_color
                self.rendering(self.my_stone_color, i, j)

            self.board[self.point[0], self.point[1]] = self.my_stone_color
            self.rendering(self.my_stone_color, self.point[0], self.point[1])

        elif msg["type"] == 5:  # NOPOINT
            self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">PASS</span></p>")

            self.board[msg["opponent_put"][0]][msg["opponent_put"][1]] = self.opponent_stone_color
            self.rendering(self.opponent_stone_color, msg["opponent_put"][0], msg["opponent_put"][1])

            for i, j in msg["changed_points"]:
                self.board[i, j] = self.opponent_stone_color
                self.rendering(self.opponent_stone_color, i, j)

        elif msg["type"] == 6:  # GAMEOVER
            try:
                self.board[msg["opponent_put"][0]][msg["opponent_put"][1]] = self.opponent_stone_color
                self.rendering(self.opponent_stone_color, msg["opponent_put"][0], msg["opponent_put"][1])

                for i, j in msg["changed_points"]:
                    self.board[i, j] = self.opponent_stone_color
                    self.rendering(self.opponent_stone_color, i, j)

            except KeyError:
                pass

            if msg["result"] == 1:
                self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">YOU WIN</span></p>")
            elif msg["result"] == 0:
                self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">YOU LOSE</span></p>")

        elif msg["type"] == 7:  # ERROR
            self.label_3.setText("<p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">ERROR</span></p>")

        # print(self.board)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">상</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">대</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">나</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))

    def rendering(self, stone_color, x, y):
        if stone_color == STONE_COLOR.BLACK.value:
            self.pushButton[x][y].setIcon(QIcon('../images/black_stone.png'))
        elif stone_color == STONE_COLOR.WHITE.value:
            self.pushButton[x][y].setIcon(QIcon('../images/white_stone.png'))

        self.pushButton[x][y].setIconSize(QSize(55, 55))
