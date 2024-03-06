### Ignore this practice file

##########################################
import socket;

buffer_size = 50
port_address = 50000
device_name= socket.gethostname()
ip_address = socket.gethostbyname(device_name)

socket_address=(ip_address, port_address)

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM)

client_socket.connect(socket_address)

def send_handler(message):
    encoded_message = message.encode('utf-8')
    message_length = len(encoded_message)
    sending_length = str(message_length).encode('utf-8')
    sending_length += b' ' * (buffer_size - len(sending_length))
    client_socket.send(sending_length)
    client_socket.send(encoded_message)

send_handler('hello')
send_handler('End')
print("Client has started")
###########################################

###########################################


