# 2a_Stop_and_Wait_Protocol
## AIM 
To write a python program to perform stop and wait protocol
## ALGORITHM
1. Start the program.
2. Get the frame size from the user
3. To create the frame based on the user request.
4. To send frames to server from the client side.
5. If your frames reach the server it will send ACK signal to client
6. Stop the Program
## PROGRAM
```
server.py 

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

client.py 

import socket
import time

s = socket.socket()
s.connect(('localhost', 12345))

n = int(input("Enter number of frames: "))

for i in range(1, n + 1):
    while True:
        print("\nSending Frame:", i)
        s.send(str(i).encode())

        # wait for ACK
        s.settimeout(2)

        try:
            ack = s.recv(1024).decode()
            print("Received:", ack)
            break
        except:
            print("No ACK received... Resending Frame")

        time.sleep(1)

print("\nAll frames sent successfully!")
s.close()
```
## OUTPUT
![alt text](<Screenshot 2026-05-02 140215.png>)

![alt text](<Screenshot 2026-05-02 140158.png>)
## RESULT
Thus, python program to perform stop and wait protocol was successfully executed.
