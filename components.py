import sqlite3
import RowComponent


class Component(RowComponent.Ui_Row):
    def __init__(self):
        super(Component, self).__init__()

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
