import requests, sys
m = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format()
response = requests.get(m)
if not response:
    print("Ошибка выполнения запроса:")
    print(m)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
im = "m.png"
with open(im, "wb") as file:
    file.write(response.content)
