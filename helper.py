# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helper3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(2000, 1500))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(233, 233, 233)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 1431, 871))
        self.stackedWidget.setStyleSheet(" background-color: rgb(235, 235, 235)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_5_bdset = QtWidgets.QLabel(self.page_1)
        self.label_5_bdset.setGeometry(QtCore.QRect(425, 35, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(16)
        self.label_5_bdset.setFont(font)
        self.label_5_bdset.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_5_bdset.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5_bdset.setObjectName("label_5_bdset")
        self.label_14 = QtWidgets.QLabel(self.page_1)
        self.label_14.setGeometry(QtCore.QRect(450, 100, 141, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.page_1)
        self.label_17.setGeometry(QtCore.QRect(945, 40, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_7_letter = QtWidgets.QLabel(self.page_1)
        self.label_7_letter.setGeometry(QtCore.QRect(1000, 590, 161, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        self.label_7_letter.setFont(font)
        self.label_7_letter.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_7_letter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7_letter.setObjectName("label_7_letter")
        self.label_cross_2 = QtWidgets.QLabel(self.page_1)
        self.label_cross_2.setGeometry(QtCore.QRect(410, 140, 190, 190))
        self.label_cross_2.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_cross_2.setText("")
        self.label_cross_2.setPixmap(QtGui.QPixmap(":/logos/cross.png"))
        self.label_cross_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cross_2.setObjectName("label_cross_2")
        self.pushButton_send = QtWidgets.QPushButton(self.page_1)
        self.pushButton_send.setGeometry(QtCore.QRect(1000, 670, 161, 41))
        self.pushButton_send.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_new_bd = QtWidgets.QPushButton(self.page_1)
        self.pushButton_new_bd.setGeometry(QtCore.QRect(410, 140, 190, 190))
        self.pushButton_new_bd.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_new_bd.setText("")
        self.pushButton_new_bd.setObjectName("pushButton_new_bd")
        self.label_8 = QtWidgets.QLabel(self.page_1)
        self.label_8.setGeometry(QtCore.QRect(410, 140, 190, 190))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/logos/rectangle.png"))
        self.label_8.setObjectName("label_8")
        self.label_15_openhtml = QtWidgets.QLabel(self.page_1)
        self.label_15_openhtml.setGeometry(QtCore.QRect(850, 103, 131, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        self.label_15_openhtml.setFont(font)
        self.label_15_openhtml.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_15_openhtml.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15_openhtml.setObjectName("label_15_openhtml")
        self.label_18 = QtWidgets.QLabel(self.page_1)
        self.label_18.setGeometry(QtCore.QRect(410, 590, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.pushButton_main_2 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_main_2.setGeometry(QtCore.QRect(0, 222, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.pushButton_main_2.setFont(font)
        self.pushButton_main_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_main_2.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_main_2.setObjectName("pushButton_main_2")
        self.label_23 = QtWidgets.QLabel(self.page_1)
        self.label_23.setGeometry(QtCore.QRect(30, 310, 36, 36))
        self.label_23.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/logos/summarize.png"))
        self.label_23.setObjectName("label_23")
        self.label_24_home = QtWidgets.QLabel(self.page_1)
        self.label_24_home.setGeometry(QtCore.QRect(30, 228, 33, 36))
        self.label_24_home.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_24_home.setText("")
        self.label_24_home.setPixmap(QtGui.QPixmap(":/logos/home.png"))
        self.label_24_home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24_home.setObjectName("label_24_home")
        self.label_2 = QtWidgets.QLabel(self.page_1)
        self.label_2.setGeometry(QtCore.QRect(50, 8, 201, 131))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/logos/logo.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton_archive_2 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_archive_2.setGeometry(QtCore.QRect(0, 300, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.pushButton_archive_2.setFont(font)
        self.pushButton_archive_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_archive_2.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"QPushButton::clicked\n"
"{\n"
"background-color : red;\n"
"}")
        self.pushButton_archive_2.setObjectName("pushButton_archive_2")
        self.label_25 = QtWidgets.QLabel(self.page_1)
        self.label_25.setGeometry(QtCore.QRect(30, 400, 47, 21))
        self.label_25.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap(":/logos/link.png"))
        self.label_25.setObjectName("label_25")
        self.pushButton_linktotitle = QtWidgets.QPushButton(self.page_1)
        self.pushButton_linktotitle.setGeometry(QtCore.QRect(0, 384, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.pushButton_linktotitle.setFont(font)
        self.pushButton_linktotitle.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_linktotitle.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_linktotitle.setObjectName("pushButton_linktotitle")
        self.label_26 = QtWidgets.QLabel(self.page_1)
        self.label_26.setGeometry(QtCore.QRect(0, 188, 321, 91))
        self.label_26.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(":/logos/activeb.png"))
        self.label_26.setObjectName("label_26")
        self.label_28_back = QtWidgets.QLabel(self.page_1)
        self.label_28_back.setGeometry(QtCore.QRect(0, 2, 321, 881))
        self.label_28_back.setStyleSheet("background-color: rgb(46, 46, 46);\n"
"border: none\n"
"")
        self.label_28_back.setText("")
        self.label_28_back.setObjectName("label_28_back")
        self.plainTextEdit_pics = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_pics.setGeometry(QtCore.QRect(815, 145, 201, 31))
        self.plainTextEdit_pics.setObjectName("plainTextEdit_pics")
        self.plainTextEdit_button_link = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_button_link.setGeometry(QtCore.QRect(815, 265, 201, 31))
        self.plainTextEdit_button_link.setObjectName("plainTextEdit_button_link")
        self.plainTextEdit_logolink = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_logolink.setGeometry(QtCore.QRect(815, 425, 201, 31))
        self.plainTextEdit_logolink.setObjectName("plainTextEdit_logolink")
        self.plainTextEdit_textafter = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_textafter.setGeometry(QtCore.QRect(815, 385, 201, 31))
        self.plainTextEdit_textafter.setObjectName("plainTextEdit_textafter")
        self.pushButton_edithtml = QtWidgets.QPushButton(self.page_1)
        self.pushButton_edithtml.setGeometry(QtCore.QRect(990, 505, 91, 23))
        self.pushButton_edithtml.setObjectName("pushButton_edithtml")
        self.plainTextEdit_text = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_text.setGeometry(QtCore.QRect(1055, 185, 201, 31))
        self.plainTextEdit_text.setObjectName("plainTextEdit_text")
        self.plainTextEdit_theme = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_theme.setGeometry(QtCore.QRect(1055, 145, 201, 31))
        self.plainTextEdit_theme.setObjectName("plainTextEdit_theme")
        self.plainTextEdit_button_name = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_button_name.setGeometry(QtCore.QRect(815, 225, 201, 31))
        self.plainTextEdit_button_name.setObjectName("plainTextEdit_button_name")
        self.listWidget = QtWidgets.QListWidget(self.page_1)
        self.listWidget.setGeometry(QtCore.QRect(615, 670, 291, 171))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_add_to_mail = QtWidgets.QPushButton(self.page_1)
        self.pushButton_add_to_mail.setGeometry(QtCore.QRect(400, 660, 190, 190))
        self.pushButton_add_to_mail.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_add_to_mail.setText("")
        self.pushButton_add_to_mail.setObjectName("pushButton_add_to_mail")
        self.label_9 = QtWidgets.QLabel(self.page_1)
        self.label_9.setGeometry(QtCore.QRect(400, 660, 190, 190))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/logos/rectangle.png"))
        self.label_9.setObjectName("label_9")
        self.label_cross_3 = QtWidgets.QLabel(self.page_1)
        self.label_cross_3.setGeometry(QtCore.QRect(400, 660, 190, 190))
        self.label_cross_3.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_cross_3.setText("")
        self.label_cross_3.setPixmap(QtGui.QPixmap(":/logos/cross.png"))
        self.label_cross_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cross_3.setObjectName("label_cross_3")
        self.plainTextEdit_mail_name = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_mail_name.setGeometry(QtCore.QRect(815, 465, 201, 31))
        self.plainTextEdit_mail_name.setObjectName("plainTextEdit_mail_name")
        self.plainTextEdit_intext_link = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_intext_link.setGeometry(QtCore.QRect(1055, 265, 201, 31))
        self.plainTextEdit_intext_link.setObjectName("plainTextEdit_intext_link")
        self.plainTextEdit_intext_link_name = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_intext_link_name.setGeometry(QtCore.QRect(1055, 305, 201, 31))
        self.plainTextEdit_intext_link_name.setObjectName("plainTextEdit_intext_link_name")
        self.pushButton_send_test = QtWidgets.QPushButton(self.page_1)
        self.pushButton_send_test.setGeometry(QtCore.QRect(1000, 720, 161, 41))
        self.pushButton_send_test.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_send_test.setObjectName("pushButton_send_test")
        self.plainTextEdit_test_mail = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_test_mail.setGeometry(QtCore.QRect(1190, 725, 231, 31))
        self.plainTextEdit_test_mail.setObjectName("plainTextEdit_test_mail")
        self.plainTextEdit_pics_2 = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_pics_2.setGeometry(QtCore.QRect(815, 185, 201, 31))
        self.plainTextEdit_pics_2.setObjectName("plainTextEdit_pics_2")
        self.label_15_openhtml_3 = QtWidgets.QLabel(self.page_1)
        self.label_15_openhtml_3.setGeometry(QtCore.QRect(1085, 103, 141, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        self.label_15_openhtml_3.setFont(font)
        self.label_15_openhtml_3.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_15_openhtml_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15_openhtml_3.setObjectName("label_15_openhtml_3")
        self.plainTextEdit_intext_link_2 = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_intext_link_2.setGeometry(QtCore.QRect(1055, 345, 201, 31))
        self.plainTextEdit_intext_link_2.setObjectName("plainTextEdit_intext_link_2")
        self.plainTextEdit_intext_link_name_2 = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_intext_link_name_2.setGeometry(QtCore.QRect(1055, 385, 201, 31))
        self.plainTextEdit_intext_link_name_2.setObjectName("plainTextEdit_intext_link_name_2")
        self.plainTextEdit_list = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_list.setGeometry(QtCore.QRect(1055, 425, 201, 31))
        self.plainTextEdit_list.setObjectName("plainTextEdit_list")
        self.plainTextEdit_italic = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_italic.setGeometry(QtCore.QRect(1055, 465, 201, 31))
        self.plainTextEdit_italic.setObjectName("plainTextEdit_italic")
        self.plainTextEdit_button_link_2 = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_button_link_2.setGeometry(QtCore.QRect(815, 345, 201, 31))
        self.plainTextEdit_button_link_2.setObjectName("plainTextEdit_button_link_2")
        self.plainTextEdit_button_name_2 = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_button_name_2.setGeometry(QtCore.QRect(815, 305, 201, 31))
        self.plainTextEdit_button_name_2.setObjectName("plainTextEdit_button_name_2")
        self.plainTextEdit_text_2 = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_text_2.setGeometry(QtCore.QRect(1055, 225, 201, 31))
        self.plainTextEdit_text_2.setObjectName("plainTextEdit_text_2")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(30, 793, 41, 41))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logos/btc_push.png"))
        self.label.setObjectName("label")
        self.pushButton_BTC = QtWidgets.QPushButton(self.page_1)
        self.pushButton_BTC.setGeometry(QtCore.QRect(30, 793, 261, 41))
        self.pushButton_BTC.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.pushButton_BTC.setText("")
        self.pushButton_BTC.setObjectName("pushButton_BTC")
        self.plainTextEdit_BTC = QtWidgets.QPlainTextEdit(self.page_1)
        self.plainTextEdit_BTC.setGeometry(QtCore.QRect(100, 790, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.plainTextEdit_BTC.setFont(font)
        self.plainTextEdit_BTC.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:  rgb(233, 233, 233);\n"
"border: none;\n"
"margin-top: 5px")
        self.plainTextEdit_BTC.setObjectName("plainTextEdit_BTC")
        self.line = QtWidgets.QFrame(self.page_1)
        self.line.setGeometry(QtCore.QRect(810, 150, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.page_1)
        self.line_2.setGeometry(QtCore.QRect(1051, 150, 20, 341))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_2.raise_()
        self.line.raise_()
        self.label_9.raise_()
        self.label_15_openhtml.raise_()
        self.label_28_back.raise_()
        self.label_26.raise_()
        self.label_5_bdset.raise_()
        self.label_14.raise_()
        self.label_17.raise_()
        self.label_7_letter.raise_()
        self.pushButton_send.raise_()
        self.label_8.raise_()
        self.label_cross_2.raise_()
        self.label_18.raise_()
        self.pushButton_main_2.raise_()
        self.label_23.raise_()
        self.label_24_home.raise_()
        self.label_2.raise_()
        self.pushButton_archive_2.raise_()
        self.label_25.raise_()
        self.pushButton_linktotitle.raise_()
        self.pushButton_new_bd.raise_()
        self.plainTextEdit_pics.raise_()
        self.plainTextEdit_button_link.raise_()
        self.plainTextEdit_logolink.raise_()
        self.plainTextEdit_textafter.raise_()
        self.pushButton_edithtml.raise_()
        self.plainTextEdit_text.raise_()
        self.plainTextEdit_button_name.raise_()
        self.listWidget.raise_()
        self.label_cross_3.raise_()
        self.pushButton_add_to_mail.raise_()
        self.plainTextEdit_mail_name.raise_()
        self.plainTextEdit_intext_link_name.raise_()
        self.pushButton_send_test.raise_()
        self.plainTextEdit_test_mail.raise_()
        self.plainTextEdit_intext_link.raise_()
        self.plainTextEdit_pics_2.raise_()
        self.label_15_openhtml_3.raise_()
        self.plainTextEdit_theme.raise_()
        self.plainTextEdit_intext_link_2.raise_()
        self.plainTextEdit_intext_link_name_2.raise_()
        self.plainTextEdit_list.raise_()
        self.plainTextEdit_italic.raise_()
        self.plainTextEdit_button_link_2.raise_()
        self.plainTextEdit_button_name_2.raise_()
        self.plainTextEdit_text_2.raise_()
        self.label.raise_()
        self.plainTextEdit_BTC.raise_()
        self.pushButton_BTC.raise_()
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_2)
        self.textEdit_2.setGeometry(QtCore.QRect(310, 250, 104, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_19 = QtWidgets.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(410, 35, 681, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.plainTextEdit_in = QtWidgets.QPlainTextEdit(self.page_3)
        self.plainTextEdit_in.setGeometry(QtCore.QRect(410, 155, 531, 71))
        self.plainTextEdit_in.setObjectName("plainTextEdit_in")
        self.label_20 = QtWidgets.QLabel(self.page_3)
        self.label_20.setGeometry(QtCore.QRect(410, 115, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_3)
        self.label_21.setGeometry(QtCore.QRect(410, 255, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_3)
        self.label_22.setGeometry(QtCore.QRect(410, 395, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(46, 46, 46)")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.pushButton_copytitle = QtWidgets.QPushButton(self.page_3)
        self.pushButton_copytitle.setGeometry(QtCore.QRect(866, 375, 75, 23))
        self.pushButton_copytitle.setObjectName("pushButton_copytitle")
        self.pushButton_copylink = QtWidgets.QPushButton(self.page_3)
        self.pushButton_copylink.setGeometry(QtCore.QRect(866, 515, 75, 23))
        self.pushButton_copylink.setObjectName("pushButton_copylink")
        self.label_28_back_3 = QtWidgets.QLabel(self.page_3)
        self.label_28_back_3.setGeometry(QtCore.QRect(0, 2, 321, 881))
        self.label_28_back_3.setStyleSheet("background-color: rgb(46, 46, 46);\n"
"border: none\n"
"")
        self.label_28_back_3.setText("")
        self.label_28_back_3.setObjectName("label_28_back_3")
        self.label_24_home_3 = QtWidgets.QLabel(self.page_3)
        self.label_24_home_3.setGeometry(QtCore.QRect(30, 228, 33, 36))
        self.label_24_home_3.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_24_home_3.setText("")
        self.label_24_home_3.setPixmap(QtGui.QPixmap(":/logos/home.png"))
        self.label_24_home_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24_home_3.setObjectName("label_24_home_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(50, 8, 201, 131))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/logos/logo.png"))
        self.label_4.setObjectName("label_4")
        self.label_33 = QtWidgets.QLabel(self.page_3)
        self.label_33.setGeometry(QtCore.QRect(30, 400, 47, 21))
        self.label_33.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(":/logos/link.png"))
        self.label_33.setObjectName("label_33")
        self.label_32 = QtWidgets.QLabel(self.page_3)
        self.label_32.setGeometry(QtCore.QRect(0, 352, 321, 91))
        self.label_32.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap(":/logos/activeb.png"))
        self.label_32.setObjectName("label_32")
        self.label_31_archive_3 = QtWidgets.QLabel(self.page_3)
        self.label_31_archive_3.setGeometry(QtCore.QRect(30, 310, 36, 36))
        self.label_31_archive_3.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_31_archive_3.setText("")
        self.label_31_archive_3.setPixmap(QtGui.QPixmap(":/logos/summarize.png"))
        self.label_31_archive_3.setObjectName("label_31_archive_3")
        self.pushButton_home_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_home_3.setGeometry(QtCore.QRect(0, 222, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.pushButton_home_3.setFont(font)
        self.pushButton_home_3.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_home_3.setObjectName("pushButton_home_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 384, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 300, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(233, 233, 233);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_insterlink = QtWidgets.QPushButton(self.page_3)
        self.pushButton_insterlink.setGeometry(QtCore.QRect(866, 235, 75, 23))
        self.pushButton_insterlink.setObjectName("pushButton_insterlink")
        self.textBrowser_title = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_title.setGeometry(QtCore.QRect(410, 295, 531, 70))
        self.textBrowser_title.setObjectName("textBrowser_title")
        self.textBrowser_link = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_link.setGeometry(QtCore.QRect(410, 435, 531, 70))
        self.textBrowser_link.setObjectName("textBrowser_link")
        self.label_28_back_3.raise_()
        self.label_19.raise_()
        self.plainTextEdit_in.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.pushButton_copytitle.raise_()
        self.pushButton_copylink.raise_()
        self.label_4.raise_()
        self.label_32.raise_()
        self.label_31_archive_3.raise_()
        self.label_24_home_3.raise_()
        self.pushButton_home_3.raise_()
        self.pushButton_4.raise_()
        self.label_33.raise_()
        self.pushButton_5.raise_()
        self.pushButton_insterlink.raise_()
        self.textBrowser_title.raise_()
        self.textBrowser_link.raise_()
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "1xHelper"))
        self.setWindowIcon(QIcon('logo.png'))
        self.label_5_bdset.setText(_translate("MainWindow", "Настройка БД"))
        self.label_14.setText(_translate("MainWindow", "Выбрать файл"))
        self.label_17.setText(_translate("MainWindow", "Создание HTML"))
        self.label_7_letter.setText(_translate("MainWindow", "Письмо"))
        self.pushButton_send.setText(_translate("MainWindow", "отправить"))
        self.label_15_openhtml.setText(_translate("MainWindow", "Структура письма"))
        self.label_18.setText(_translate("MainWindow", "Файлы рассылки"))
        self.pushButton_main_2.setText(_translate("MainWindow", "Рассылка"))
        self.pushButton_archive_2.setText(_translate("MainWindow", "Архив"))
        self.pushButton_linktotitle.setText(_translate("MainWindow", "Link2title"))
        self.plainTextEdit_pics.setPlainText(_translate("MainWindow", "ссылка на картинку"))
        self.plainTextEdit_button_link.setPlainText(_translate("MainWindow", "ссылка под кнопку"))
        self.plainTextEdit_logolink.setPlainText(_translate("MainWindow", "ссылка под лого"))
        self.plainTextEdit_textafter.setPlainText(_translate("MainWindow", "текст после кнопок"))
        self.pushButton_edithtml.setText(_translate("MainWindow", "создать"))
        self.plainTextEdit_text.setPlainText(_translate("MainWindow", "текст после первой картинки"))
        self.plainTextEdit_theme.setPlainText(_translate("MainWindow", "тема письма"))
        self.plainTextEdit_button_name.setPlainText(_translate("MainWindow", "название кнопки"))
        self.plainTextEdit_mail_name.setPlainText(_translate("MainWindow", "имя рассылки"))
        self.plainTextEdit_intext_link.setPlainText(_translate("MainWindow", "ссылка в тексте"))
        self.plainTextEdit_intext_link_name.setPlainText(_translate("MainWindow", "якорь ссылки в тексте"))
        self.pushButton_send_test.setText(_translate("MainWindow", "отправить тест"))
        self.plainTextEdit_test_mail.setPlainText(_translate("MainWindow", "email"))
        self.plainTextEdit_pics_2.setPlainText(_translate("MainWindow", "ссылка на вторую картинку"))
        self.label_15_openhtml_3.setText(_translate("MainWindow", "Настройка текста"))
        self.plainTextEdit_intext_link_2.setPlainText(_translate("MainWindow", "вторая ссылка в тексте"))
        self.plainTextEdit_intext_link_name_2.setPlainText(_translate("MainWindow", "якорь второй ссылки в тексте"))
        self.plainTextEdit_list.setPlainText(_translate("MainWindow", "список"))
        self.plainTextEdit_italic.setPlainText(_translate("MainWindow", "курсивный текст"))
        self.plainTextEdit_button_link_2.setPlainText(_translate("MainWindow", "ссылка под вторую кнопку"))
        self.plainTextEdit_button_name_2.setPlainText(_translate("MainWindow", "название второй кнопки"))
        self.plainTextEdit_text_2.setPlainText(_translate("MainWindow", "текст после второй картинки"))
        self.plainTextEdit_BTC.setPlainText(_translate("MainWindow", "update"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">page 2</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "Конвертировать ссылку в заголовок + рефку"))
        self.label_20.setText(_translate("MainWindow", "Вставить ссылку"))
        self.label_21.setText(_translate("MainWindow", "Заголовок"))
        self.label_22.setText(_translate("MainWindow", "Рефка"))
        self.pushButton_copytitle.setText(_translate("MainWindow", "Копировать"))
        self.pushButton_copylink.setText(_translate("MainWindow", "Копировать"))
        self.pushButton_home_3.setText(_translate("MainWindow", "Рассылка"))
        self.pushButton_4.setText(_translate("MainWindow", "Link2title"))
        self.pushButton_5.setText(_translate("MainWindow", "Архив"))
        self.pushButton_insterlink.setText(_translate("MainWindow", "Ок"))
        self.textBrowser_title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_link.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
import mailer_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
