import socket

host = socket.gethostname()
port = 5000
client_socket = socket.socket()
client_socket.connect((host, port))

message = input("Enter amount of hours person works: ")

while message.lower().strip() != 'bye':
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print('Payable amount: ' + data)
    message = input("Enter the amount of hours person works:")

client_socket.close()
