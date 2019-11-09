import sqlite3


class Login:
    def __init__(self):
        self.open()

    def add_user(self, login, password):
        self.cur.execute("""
                            INSERT INTO Login(login, password) VALUES(?, ?)
                        """, (login, password))
        self.currentUser = login

    def delete_last(self):
        self.cur.execute("""
                                    DELETE from Login
                                    WHERE login = ?
                                """, (self.currentUser, ))

    def check_auto_enter(self):
        result = self.cur.execute("""
                                                SELECT login, password FROM Login
                                                    WHERE Auto IS TRUE
                                            """).fetchone()
        if result:
            login, password = result
            self.currentUser = login

    def add_auto_enter(self):
        self.cur.execute("""
                            UPDATE Login
                            SET Auto = TRUE
                            WHERE login = ?
                        """, (self.currentUser,))

    def remove_auto_enter(self):
        self.cur.execute("""
                                    UPDATE Login
                                    SET Auto = FALSE
                                    WHERE login = ?
                                """, (self.currentUser,))

    def open(self):
        self.data = sqlite3.connect("Mail.db")
        self.cur = self.data.cursor()
        self.currentUser = ''

    def close(self):
        self.data.close()


class Mail:
    def __init__(self):
        self.open()

    def open(self):
        self.data = sqlite3.connect("Mail.db")
        self.cur = self.data.cursor()

    def close(self):
        self.data.close()

    def add_mail(self, desk_mails, topic, message):
        self.cur.execute("""
                            INSERT INTO History(
                                title, text, mailto
                                )
                             VALUES(
                                    ?, ?, ?
                                )
                        """, (topic, message, desk_mails))

    def loof_for_message(self):
        return self.cur.execute("""
                            SELECT id, title, text, mailto FROM History
                        """).fetchall()

    def delete_message(self, id):
        self.cur.execute("""
                            DELETE from History
                            WHERE id = ?
                        """, (id, ))


mail = Mail().add_mail("a", 'a', 'mima')
