import socket

bufferSize = 16
PORT = 50000
SERVER = socket.gethostbyname(socket.gethostname())

ADDR=(SERVER, PORT)
FORMAT="utf8"
DISCONNET_MSG="End"

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message) 
    send_length = str(msg_length).encode(FORMAT)
    send_length+=b' '*(bufferSize-len(send_length))
    
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    
connected = True
while connected:
    input_message = input("Please enter your message\n")
    if input_message == "Done":
        connected = False
        send(DISCONNET_MSG)
    else:
        send(input_message)
