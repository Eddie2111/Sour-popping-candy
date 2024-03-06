import socket

bufferSize = 16
PORT = 50000
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
FORMAT = "utf8"
DISCONNET_MSG = "End"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("server is Listening")
conn, addr= server.accept()

connected = True

while connected: 
    msg_length=conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length= int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT)
        if msg==DISCONNET_MSG:
            connected=False
            conn.send("Goodbye".encode(FORMAT))
        else:
            print(msg)
            conn.send("Meesage Received".encode(FORMAT))
conn.close()
            
