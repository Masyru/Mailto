import sqlite3


class Login:
    def __init__(self):
        self.data = sqlite3.connect("Mail.db")
        self.cur = self.data.cursor()
        self.currentUser = ''

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

