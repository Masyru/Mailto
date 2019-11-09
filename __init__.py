import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic as render
import request as req
import database as db
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mail = db.Mail()
        render.loadUi("./UI/Login.ui", self)
        self.pushEnter.clicked.connect(self.enter)

    def enter(self):
        """ Вход и авторизация в системе """
        login = self.Login.text()
        password = self.Password.text()
        rem = self.checkBox.isChecked()
        if login and password:
            try:
                self.server = req.Request(login, password)
                self.server.server.ehlo()
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
        render.loadUi("./UI/Home.ui", self)
        self.setWindowTitle('Написание письма - Home')
        self.HistoryBtn.clicked.connect(self.run_history)
        self.Submit.clicked.connect(self.submit)

    def run_history(self):
        """ Окно просмотра истории сообщений """
        render.loadUi("./UI/History.ui", self)
        self.setWindowTitle('История писем - History')
        self.WriteBtn.clicked.connect(self.run_home)

    def module_success(self):
        render.loadUi("./UI.SuccessSent.ui", self)
        time.sleep(1.5)
        self.run_home()

    def submit(self):
        topic = self.Topic.text().strip()
        mails = list(map(str.strip, self.To.text().split()))
        text = self.Text.toPlainText().strip()
        print(topic, mails, text)
        try:
            self.server.send_email(topic, mails, text)
            self.mail.add_mail(mails, topic, text)
        finally:
            render.loadUi('./UI/HomeError.ui', self)
            self.setWindowTitle('Ошибка отправки - Home')
            self.HistoryBtn.clicked.connect(self.run_history)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(App.exec_())
