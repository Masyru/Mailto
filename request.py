import smtplib


class Request:
    def __init__(self, email, password):
        self.server = smtplib.SMTP('smtp.yandex.ru', 587)
        self.login, self.password = email, password
        self.server.ehlo()
        self.server.starttls()
        self.response = self.server.login(self.login, self.password)

    def send_message(self, dest_emails, subject, email_text):
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.login, self.password)
        message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % \
                  (self.login, dest_emails, subject, email_text)
        self.server.set_debuglevel(1)  # Необязательно; так будут отображаться данные с сервера в консоли
        self.server.sendmail(self.login, dest_emails, message)


