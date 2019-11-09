import sqlite3
import datetime


class Login:
    def __init__(self):
        self.open()

    def add_user(self, login, password):
        self.cur.execute("""
                            INSERT INTO Login(login, password) VALUES(?, ?)
                        """, (login, password))
        self.currentUser = login
        self.data.commit()

    def delete_last(self):
        self.cur.execute("""
                                    DELETE from Login
                                    WHERE login = ?
                                """, (self.currentUser, ))
        self.data.commit()

    def check_auto_enter(self):
        result = self.cur.execute("""
                                                SELECT login, password FROM Login
                                                    WHERE Auto IS TRUE
                                            """).fetchone()
        if result:
            login, password = result
            self.currentUser = login
            return login, password
        return ('', '')

    def add_auto_enter(self):
        self.cur.execute("""
                            UPDATE Login
                            SET Auto = TRUE
                            WHERE login = ?
                        """, (self.currentUser,))
        self.data.commit()

    def remove_auto_enter(self):
        self.cur.execute("""
                                    UPDATE Login
                                    SET Auto = FALSE
                                    WHERE login = ?
                                """, (self.currentUser,))
        self.data.commit()

    def open(self):
        self.data = sqlite3.connect("Mail.db")
        self.cur = self.data.cursor()
        self.currentUser = ''

    def close(self):
        self.data.close()


class Mail:
    def __init__(self):
        self.data = sqlite3.connect("Mail.db")
        self.cur = self.data.cursor()

    def close(self):
        self.data.close()

    def add_mail(self, desk_mails, topic, message):
        now = f'{datetime.datetime.today().strftime("%H:%M")} {datetime.date.today().day}.{datetime.date.today().month}'
        year = f'{datetime.date.today().year}'
        self.cur.execute("""
                            INSERT INTO History(
                                title, text, mailto, time, year, notes
                                )
                             VALUES(
                                    ?, ?, ?, ?, ?, ?
                                )
                        """, (topic, message, desk_mails, now, year, "Не указано"))
        self.data.commit()

    def look_for_message(self):
        return self.cur.execute("""
                            SELECT id, title, text, mailto FROM History
                        """).fetchall()

    def delete_message(self, id):
        self.cur.execute("""
                            DELETE from History
                            WHERE id = ?
                        """, (id, ))
        self.data.commit()
