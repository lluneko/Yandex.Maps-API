import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        print('Введите координаты')
        self.coord_x, self.coord_y = float(input()), float(input())
        while (self.coord_x > 100 or self.coord_y > 100) or (self.coord_x < 0 or self.coord_y < 0):
            print("неверные данные")
            self.coord_x, self.coord_y = float(input()), float(input())
        print('Введите масштаб')
        self.z = int(input())
        while self.z > 17 or self.z < 0:
            print("неверные данные")
            self.z = int(input())
        self.setObjectName("MainWindow")
        self.resize(550, 500)
        self.setStyleSheet("background-color: rgb(186, 248, 105);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 480, 490))
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.label.setText("TextLabel")

        m = f"http://static-maps.yandex.ru/1.x/?ll={self.coord_x},{self.coord_y}&z={self.z}&l=map"
        response = requests.get(m)
        if not response:
            print("Ошибка выполнения запроса:")
            print(m)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        im = "m.png"
        with open(im, "wb") as file:
            file.write(response.content)

        img = QtGui.QPixmap(im)
        self.label.setPixmap(img)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.z -= 1
            m = f"http://static-maps.yandex.ru/1.x/?ll={self.coord_x},{self.coord_y}&z={self.z}&l=map"
            response = requests.get(m)
            if not response:
                print("Ошибка выполнения запроса:")
                print(m)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            im = "m.png"
            with open(im, "wb") as file:
                file.write(response.content)

            img = QtGui.QPixmap(im)
            self.label.setPixmap(img)
        if event.key() == Qt.Key_PageDown:
            self.z += 1
            m = f"http://static-maps.yandex.ru/1.x/?ll={self.coord_x},{self.coord_y}&z={self.z}&l=map"
            response = requests.get(m)
            if not response:
                print("Ошибка выполнения запроса:")
                print(m)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            im = "m.png"
            os.remove(im)
            with open(im, "wb") as file:
                file.write(response.content)

            img = QtGui.QPixmap(im)
            self.label.setPixmap(img)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
