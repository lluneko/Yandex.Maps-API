def keyPressEvent(self, event):
    if event.key() == Qt.Key_PageUp:
        self.z += 10
        m = f"http://static-maps.yandex.ru/1.x/?ll={self.coord_x},{self.coord_y}&self.z={self.z}&l=map"
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
        self.z -= 1
        m = f"http://static-maps.yandex.ru/1.x/?ll={self.coord_x},{self.coord_y}&self.z={self.z}&l=map"
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