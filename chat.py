import argparse
import socket
import json

ADDRESS = 'localhost'
PORT = 7777
CONNECTIONS = 10


def get_server_socket(addr, port):
    s = socket.socket()     # Создаём сокет
    s.bind((addr, port))    # Указываем хост и порт
    s.listen(CONNECTIONS)   # Запускаем режим прослушивания и указываем максимальное
                            #   количество подключений в очереди
    return s


def get_client_socket(addr, port):
    s = socket.socket()     # Создаём сокет
    s.connect((addr, port)) # Подключение клиента
    return s


# Отправляем сообщение
def send_data(recipient, data):
    recipient.send(json.dumps(data).encode('utf-8'))


# Получаем сообщение
def get_data(sender):
    return json.loads(sender.recv(1024).decode("utf-8"))

# Обработка коммандной строки
def create_parser():
    # Создаём объект с указанием описания
    parser = argparse.ArgumentParser(
        description='JSON instant messaging'
    )

    # Объединяем параметры командной строки в группу
    parser_group = parser.add_argument_group(title='Parameters')
    # Описываем параметры
    parser_group.add_argument('-a', '--addr', default=ADDRESS, help='IP address')
    parser_group.add_argument('-p', '--port', type=int, default=PORT, help='TCP port')

    return parser