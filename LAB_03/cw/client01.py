import socket

bufferSize=16
PORT=50000
SERVER=socket.gethostbyname(socket.gethostname())


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
    
send(f"Client's IP Address is {SERVER} and Client's Device name is {socket.gethostname()}")
send(DISCONNET_MSG)
