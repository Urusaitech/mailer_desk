# if logo disappears in helper.py: retranslateui-> self.setWindowIcon(QIcon('logo.png'))
# self.plainTextEdit_in = QTextEdit()
# self.radioButton_unicode.setChecked(True)
# auto-py-to-exe to compile
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QMessageBox, QFileDialog
import os
import pyperclip

import helper
import bd_converter
import html_edit
import update_rate


class HelperApp(QtWidgets.QMainWindow, helper.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.scrollable_text_area = None
        self.title = None
        self.file_path = None
        listWidget = QListWidget()
        self.setupUi(self)
        # self.pushButton_new_folder.clicked.connect(self.browse_folder)
        self.pushButton_new_bd.clicked.connect(self.sort_bd)
        self.pushButton_linktotitle.clicked.connect(self.third_page)
        listWidget.itemClicked.connect(self.clicked)
        self.pushButton_home_3.clicked.connect(self.first_page)
        self.pushButton_insterlink.clicked.connect(self.check_in)
        self.pushButton_copytitle.clicked.connect(self.copy_title)
        self.pushButton_copylink.clicked.connect(self.copy_link)
        self.pushButton_edithtml.clicked.connect(self.edit_html)
        self.pushButton_BTC.clicked.connect(self.update_btc)
        
    # TODO: comments
    path = None

    char = "UTF-8"

    # def set_code(self):
    #    code = char
    #    print(code)
    #    if code == "UTF-8":
    #        pass
    # TODO: refactor funcs to methods
    def browse_folder(self) -> None:
        # TODO: comments
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose folder")
        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

    def clicked(self, item) -> None:
        # TODO: comments
        print(self, "Info", item.text())

    def dialog(self) -> str:
        # TODO: comments
        file, check = QFileDialog.getOpenFileNames(None, "QFileDialog.getOpenFileNames()",
                                                   "", "All Files (*);;OpenDataSheets (*.ods);;Text Files (*.txt)")
        if check:
            return file

    def sort_bd(self) -> None:
        # TODO: comments

        try:
            bd_converter.convert_bd(self.dialog())
            msg = QMessageBox()
            msg.setWindowTitle("DB")
            msg.setText("Success!")

            msg.exec_()

        except:
            alert = QMessageBox()
            alert.setWindowTitle("DB Set up")
            alert.setText("An error occurred")
            alert.setIcon(QMessageBox.Warning)

            alert.exec_()
            pass

    def open_new_file(self) -> None:
        # TODO: comments
        self.file_path, filter_type = QFileDialog.getOpenFileName(self, "Open new file",
                                                                  "", "All files (*)")
        if self.file_path:
            with open(self.file_path, "r") as f:
                file_contents = f.read()
                self.title.setText(self.file_path)
                self.scrollable_text_area.setText(file_contents)
        else:
            self.invalid_path_alert_message()

    def invalid_path_alert_message(self) -> None:
        print("Error!")

    def first_page(self) -> None:
        # TODO: comments
        self.stackedWidget.setCurrentIndex(0)

    def second_page(self) -> None:
        # TODO: comments
        self.stackedWidget.setCurrentIndex(1)

    def third_page(self) -> None:
        # TODO: comments
        self.stackedWidget.setCurrentIndex(2)

    def check_in(self) -> None:
        # TODO: comments
        check = self.plainTextEdit_in.toPlainText()
        if 'com' in check:
            self.insert_link()
        else:
            self.textBrowser_title.setText('Error! Your link should look like example.com/***')

    def insert_link(self) -> None:
        # TODO: comments
        # XXX: do not use globals
        global insert, link, text, text_to_copy
        insert = self.plainTextEdit_in.toPlainText()

        link = ''
        try:
            text = insert.rpartition('.com')[2]  # clean the string
        except:
            pass

        link += text
        try:
            link = link.replace('/ru', '')
        except:
            pass

        txt_index = text.rindex('/')
        names = text[txt_index::]
        names = names.split('-')
        del names[0]
        flag_names = 0
        club1 = []
        club2 = []
        for word in names:
            if flag_names < len(names) / 2:
                club1.append(word)
                flag_names += 1
            else:
                club2.append(word)
        # XXX: not very pytonic
        club1 = ' '.join(club1)
        club1 = club1.title()
        club2 = ' '.join(club2)
        club2 = club2.title()
        clubs = club1 + ' - ' + club2
        league = text[:txt_index:]
        league = league.split('-')
        del league[0]
        league = ' '.join(league)
        league = league.upper()

        text_to_copy = league + ': ' + clubs
        self.textBrowser_title.setText(text_to_copy)
        self.textBrowser_link.setText(link)

    def copy_title(self) -> None:
        # TODO: comments
        pyperclip.copy(text_to_copy)

    def copy_link(self) -> None:
        # TODO: comments
        pyperclip.copy(link)

    def open_html(self) -> None:
        # TODO: comments
        try:
            html_edit.convert_html(self.dialog())
        except:
            pass

    def edit_html(self) -> None:
        # TODO: comments
        try:
            # each variable stores entered value and passes it to the html_edit.py
            pic_link = self.plainTextEdit_pics.toPlainText()
            sec_pic_link = self.plainTextEdit_pics_2.toPlainText()
            but_title = self.plainTextEdit_button_name.toPlainText()
            but_link = self.plainTextEdit_button_link.toPlainText()
            sec_but_title = self.plainTextEdit_button_name_2.toPlainText()
            sec_but_link = self.plainTextEdit_button_link_2.toPlainText()
            aftertext = self.plainTextEdit_textafter.toPlainText()
            logolink = self.plainTextEdit_logolink.toPlainText()
            mail_name = self.plainTextEdit_mail_name.toPlainText()

            theme = self.plainTextEdit_theme.toPlainText()
            message = self.plainTextEdit_text.toPlainText()
            message_2 = self.plainTextEdit_text_2.toPlainText()
            intext_link = self.plainTextEdit_intext_link.toPlainText()
            intext_link_title = self.plainTextEdit_intext_link_name.toPlainText()
            sec_intext_link = self.plainTextEdit_intext_link_2.toPlainText()
            sec_intext_link_title = self.plainTextEdit_intext_link_name_2.toPlainText()
            listing = self.plainTextEdit_list.toPlainText()
            italic = self.plainTextEdit_italic.toPlainText()

            path = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose a folder to save in")
            # XXX: split in smaller funcs
            if sec_pic_link == "ссылка на вторую картинку":
                html_edit.create_html_1(pic_link, but_title, but_link, sec_but_title, sec_but_link,
                                        aftertext, logolink, mail_name, theme, message, intext_link, intext_link_title,
                                        sec_intext_link, sec_intext_link_title, listing, italic, path)
            else:
                html_edit.create_html_2(pic_link, sec_pic_link, but_title, but_link, sec_but_title, sec_but_link,
                                        aftertext, logolink, mail_name, theme, message, intext_link, intext_link_title,
                                        sec_intext_link, sec_intext_link_title, listing, italic, path, message_2)

            html_alert = QMessageBox()
            html_alert.setWindowTitle("HTML")
            html_alert.setText("HTML файл создан")

            html_alert.exec_()
        except:
            # XXX: catch specific exceptions
            print("error in edit_html()")
            pass

    def update_btc(self) -> None:
        # TODO: comments
        try:
            # self.plainTextEdit_BTC.setPlainText(update_rate.call_kraken_free())
            self.plainTextEdit_BTC.setPlainText(update_rate.call_cmc())

        # update_rate.call_cmc()
        # sample2.call_kraken_paid()
        except:
            # XXX: catch specific exceptions
            pass


def main() -> None:
    # TODO: comments
    app = QtWidgets.QApplication(sys.argv)
    window = HelperApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
