import socket
import threading

bufferSize = 16
PORT = 50000
SERVER=socket.gethostbyname(socket.gethostname())

ADDR=(SERVER, PORT)
FORMAT="utf8"
DISCONNET_MSG="End"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()

def handle_clients(conn,addr):
    connected = True
    
    while connected:
        msg_length = conn.recv(bufferSize).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNET_MSG:
                connected=False
                conn.send("Goodbye".encode(FORMAT))
            else:
                vowels = "aeiouAEIOU"
                count = 0
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

def main():
    server.listen()
    print("Server is listening")
    while True:
        conn, addr= server.accept()
        thread=threading.Thread(target=handle_clients,args=(conn,addr))
        thread.start()
        print(f"total Clients connected: {threading.active_count()-1} ")
main()
