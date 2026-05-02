import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)

print("Server waiting for connection...")
conn, addr = s.accept()
print("Connected to client:", addr)

while True:
    frame = conn.recv(1024).decode()

    if not frame:
        break

    print("Received Frame:", frame)

    # Send ACK
    ack = "ACK " + frame
    conn.send(ack.encode())
    print("ACK sent for Frame", frame)

conn.close()
