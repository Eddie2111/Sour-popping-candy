import socket

bufferSize: int = 16
PORT: int = 50000
SERVER: str = socket.gethostbyname(socket.gethostname())

ADDR: tuple = (SERVER, PORT)
FORMAT: str = "utf8"
DISCONNECT_MSG: str = "End"

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("Server is Listening")
conn: socket.socket;
addr: tuple;
conn, addr = server.accept()

connected: bool = True

while connected:
    msg_length: bytes = conn.recv(bufferSize)
    if msg_length:
        msg_length = int(msg_length.decode(FORMAT))
        msg: str = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            conn.send("Quitting".encode(FORMAT))
        else:
            vowels: str = "aeiouAEIOU"
            count: int = 0
            for i in msg:
                if i in vowels:
                    count += 1
            if count == 0:
                conn.send("Not enough vowels".encode(FORMAT))
            elif count <= 2:
                conn.send("Enough vowels".encode(FORMAT))
            else:
                conn.send("Too many vowels".encode(FORMAT))
conn.close()
