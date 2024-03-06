### Ignore this practice file

###################################################
###################################################
import socket;

buffer_size = 50
port_address = 50000
device_name= socket.gethostname()
ip_address = socket.gethostbyname(device_name)

socket_address=(ip_address, port_address)

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)
server_socket.bind(socket_address)

server_socket.listen() 

print("Server has started")

client_socket, client_address = server_socket.accept()

while True:
    message_length = client_socket.recv(buffer_size)
    if message_length != None:
        message_length = int(message_length)
        message = client_socket.recv(message_length).decode('utf-8')
        print(f'Server: received message:{message}')
        print(f'Server: received message length:{message_length}')
        if message == 'End':
            client_socket.close()
            break
        else:
            print(message)

#####################################################
