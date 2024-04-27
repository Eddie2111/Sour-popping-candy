import socket
from typing import Tuple

PORT: int = 50000
SERVER: str = socket.gethostbyname(socket.gethostname())

ADDR: Tuple[str, int] = (SERVER, PORT)
FORMAT: str = "utf-8"
DISCONNECT_MSG: str = "End"

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("Server is listening")

def get_client_info(conn: socket.socket, addr: Tuple[str, int]) -> None:
    client_ip: str = addr[0]
    client_hostname: str = socket.gethostbyaddr(client_ip)[0]
    client_info: str = f"Client IP: {client_ip}, Hostname: {client_hostname}"
    conn.send(client_info.encode(FORMAT))

while True:
    conn: socket.socket
    addr: Tuple[str, int]
    conn, addr = server.accept()
    print(f"Connected to {addr}")

    get_client_info(conn, addr)

    connected: bool = True
    while connected:
        msg: str = conn.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            conn.send("Goodbye".encode(FORMAT))
        else:
            print(msg)
            conn.send("Message Received".encode(FORMAT))
    conn.close()
