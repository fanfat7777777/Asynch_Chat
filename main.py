#   1 задание
#   Непонял что тут требуется сделать по итогу


#   2 задание
print("2 Задание")
items = [ "class", "function", "method"]
for item in items:
    item = bytes(item, "utf-8")
    print(f"Тип: {type(item)}, Длина:  {len(item)}")
print()


#   3 задание
print("3 Задание")
print("attribute", bytes("attribute", "utf-8"))
print("класс", bytes("класс", "utf-8"))
print("функция", bytes("функция", "utf-8"))
print("type", bytes("type", "utf-8"))
print()


#   4 задание
print("4 Задание")
items = [ "разработка", "администрирование", "protocol", "standard"]
for item in items:
    item = item.encode("UTF-8")
    print(f"Кодируем: {item}, Декодируем: {item.decode('UTF-8')}")
print()


#   5 задание
print("5 Задание")
import subprocess
args = ["ping", "yandex.ru"]

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode("UTF-8"))
    break

args = ["ping", "youtube.com"]

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode("UTF-8"))
    break


#   6 задание
print("6 Задание")
with open("test_file.txt", "r") as f:
    for line in f:
        print(line)

print("Открываем в юникоде")
with open("test_file.txt", "rb") as f:
    for line in f:
        print(line.decode("unicode_escape"))

