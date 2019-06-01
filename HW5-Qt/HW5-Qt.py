from PyQt5 import QtWidgets, uic
import sqlite3
import requests
import json
import datetime
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_re(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_re, self).__init__()
        uic.loadUi('dialog1.ui', self)
        self.label.setVisible(False)
        self.pushButton_2.clicked.connect(self.registerbutton)
        self.show()

    def registerbutton(self):
        self.label.setVisible(True)
        conn = sqlite3.connect('mapdb.db')
        c = conn.cursor()
        name = str(self.nametext.displayText())
        phone = int(str(self.phonetext.displayText()))
        username = str(self.usertext.displayText())
        password = str(self.passtext.displayText())
        args = (name, phone, username, password)
        sql = '''INSERT INTO users(name, phone, username, password) values(?,?,?,?)'''
        c.execute(sql, args)
        conn.commit()


class Ui_lo(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_lo, self).__init__()
        uic.loadUi('dialog.ui', self)
        self.pushButton.clicked.connect(self.loginbutton)
        self.pushButton_2.clicked.connect(self.registerbutton)
        self.show()

    def registerbutton(self):
        registerwindow = Ui_re()
        registerwindow.exec_()

    def loginbutton(self):
        send_url = 'https://api.ipdata.co/es?api-key=c5806cd4281d6b151ca778f0a1d06c02c62642af9f01f6c815bcc7d9'
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        conn = sqlite3.connect('mapdb.db')
        c = conn.cursor()
        stmt = '''SELECT id, name FROM users WHERE username = (?)'''
        args = (str(self.usernametext.displayText()), )
        c.execute(stmt, args)
        rows = c.fetchall()
        conn.commit()
        userid = rows[0][0]
        currentDT = datetime.datetime.now()
        args = (userid, latitude, longitude, currentDT.strftime("%Y-%m-%d"))
        sql = '''INSERT INTO locations(user_id, lat, lon, time) values(?,?,?,?)'''
        c.execute(sql, args)
        url = 'https://map.ir/static?width=700&height=400&zoom_level=12&markers=color%3Aorigin%7Clabel%3A%D9%85%D9%BE%7C' + str(
            longitude) + '%2C' + str(latitude)
        r = requests.get(url, allow_redirects=True)
        open('sample.png', 'wb').write(r.content)
        conn.commit()
        mapwindow = Ui_map(rows)
        mapwindow.exec_()


class Ui_map(QtWidgets.QDialog):
    def __init__(self, detail):
        super(Ui_map, self).__init__()
        uic.loadUi('dialog2.ui', self)
        conn = sqlite3.connect('mapdb.db')
        c = conn.cursor()
        userid = detail[0][0]
        stmt = '''SELECT lat, lon, time FROM locations WHERE user_id = (?)'''
        args = (userid,)
        c.execute(stmt, args)
        coordinates = c.fetchall()
        conn.commit()
        img = Image.open('sample.png')
        img = img.resize((261, 281), Image.ANTIALIAS)
        img.save('sample.png')
        pixmap = QPixmap('sample.png')
        self.image.setPixmap(pixmap)
        for i in range(len(coordinates)-1):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(str(coordinates[i][0])))
            self.table.setItem(i, 1, QTableWidgetItem(str(coordinates[i][1])))
            self.table.setItem(i, 2, QTableWidgetItem(str(coordinates[i][2])))
        self.lat.setText(str(coordinates[len(coordinates)-1][0]))
        self.lon.setText(str(coordinates[len(coordinates)-1][1]))
        self.titlename.setText('Hello '+detail[0][1]+'!')
        self.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = Ui_lo()
    sys.exit(app.exec_())