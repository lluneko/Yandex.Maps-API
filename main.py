import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        print('Введите координаты')
        coord_x, coord_y = float(input()), float(input())
        while coord_x > 100 or coord_y > 100:
            print("неверные данные")
            coord_x, coord_y = float(input()), float(input())
        print('Введите масштаб')
        z = int(input())
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

        m = f"http://static-maps.yandex.ru/1.x/?ll={coord_x},{coord_y}&z={z}&l=map"
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
