import socket

host = socket.gethostname()
port = 5000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)

print("Server is Listening")
conn, address = server_socket.accept()
print("User Joined: " + str(address))


while True:
    data = conn.recv(1024).decode()
    if not data: # if no data
        break
    print("hours received: " + str(data) + " Hrs")
    data = int(data)
    pay = 0
    if (data <= 40): pay = data * 200
    elif (data > 40): pay = ((data - 40) * 300) + 8000

    data = str(float(pay)) + " TK"

    conn.send(data.encode())

print("Server closed")
conn.close()
