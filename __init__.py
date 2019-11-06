import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5 import uic as render
import request as req
import database as db

server, database = None, None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        render.loadUi("./UI/Login.ui", self)
        self.pushEnter.clicked.connect(self.enter)
        self.run_home()

    def enter(self):
        """ Вход и авторизация в системе """
        global server, database
        login = self.Login.text()
        password = self.Password.text()
        rem = self.checkBox.isChecked()
        if login and password:
            try:
                server = req.Request(login, password)
                database = db.Login()
                database.add_user(login, password)
                if rem:
                    database.add_auto_enter()
                else:
                    database.remove_auto_enter()
                self.run_home()
                print('Entered')
            except EnvironmentError:
                render.loadUi("./UI/LoginError.ui", self)
                self.pushEnter.clicked.connect(self.enter)

    def run_home(self):
        """ Главное окно написания письма """
        render.loadUi("./Ui/Home.ui", self)
        self.setWindowTitle('Написание письма - Home')

    def run_history(self):
        """ Окно просмотра истории сообщений """
        render.loadUi("./Ui/History.ui", self)
        self.setWindowTitle('История писем - History')


if __name__ == '__main__':
    App = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(App.exec_())
