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
