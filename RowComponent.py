# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Row.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Row(object):
    def __init__(self):
        super().__init__()
        self.Text = QtWidgets.QTextEdit(self.MyRow)
        self.listMails = QtWidgets.QListView(self.MyRow)
        self.MyRow = QtWidgets.QWidget(Row)
        self.DeleteBtn = QtWidgets.QPushButton(self.MyRow)
        self.Topic = QtWidgets.QLineEdit(self.MyRow)

    def setupUi(self, Row):
        Row.setObjectName("Row")
        Row.resize(799, 174)
        self.MyRow.setGeometry(QtCore.QRect(0, 20, 791, 141))
        self.MyRow.setObjectName("MyRow")
        self.DeleteBtn.setGeometry(QtCore.QRect(700, 110, 88, 27))
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.Text.setGeometry(QtCore.QRect(0, 30, 501, 111))
        self.Text.setObjectName("Text")
        self.Topic.setGeometry(QtCore.QRect(0, 0, 501, 27))
        self.Topic.setReadOnly(True)
        self.Topic.setObjectName("Topic")
        self.listMails.setGeometry(QtCore.QRect(510, 0, 181, 141))
        self.listMails.setObjectName("listMails")
        self.RepeteBtn = QtWidgets.QPushButton(self.MyRow)
        self.RepeteBtn.setGeometry(QtCore.QRect(700, 30, 88, 27))
        self.RepeteBtn.setObjectName("RepeteBtn")
        self.EditBtn = QtWidgets.QPushButton(self.MyRow)
        self.EditBtn.setGeometry(QtCore.QRect(700, 0, 88, 27))
        self.EditBtn.setObjectName("EditBtn")

        self.retranslateUi(Row)
        QtCore.QMetaObject.connectSlotsByName(Row)

    def retranslateUi(self, Row):
        _translate = QtCore.QCoreApplication.translate
        Row.setWindowTitle(_translate("Row", "Form"))
        self.DeleteBtn.setText(_translate("Row", "Удалить"))
        self.RepeteBtn.setText(_translate("Row", "Повтор"))
        self.EditBtn.setText(_translate("Row", "Изменить"))

    def row_data(self, idn, topic, text, listMails):
        self.Text.insertPlainText(text)
        self.Topic.setText(topic)
        self.listMails.setText(self.reconstruation_mails(listMails))
        self.DeleteBtn.clicked.connect(lambda: self.deleteRow(idn))
        return self.MyRow

    def deleteRow(self, ide):
        data = sqlite3.connect('Mail.db')
        cur = data.cursor()
        cur.execute("""
                        DELETE from Mail
                        WHERE id = ?
                    """, (ide, ))
        data.commit()
        data.close()


    @staticmethod
    def reconstruation_mails(string):
        print(string.split())
        some = '\r\n'.join(string.split())
        return some
