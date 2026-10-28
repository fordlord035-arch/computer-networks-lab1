import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Подключено к серверу.")
print("Введите сообщение (или 'exit' для выхода).")

while True:
    message = input("> ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024)
    print("Ответ сервера:", response.decode())

    if message.lower() == "exit":
        break

client_socket.close()
print("Клиент завершил работу.")