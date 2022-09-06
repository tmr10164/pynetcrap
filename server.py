import socket
import socketserver
import datetime


def servcess():
    serv = socket.create_server((socket.gethostbyname(socket.gethostname()), 10164))
    print(socket.gethostbyname(socket.gethostname()))
    serv.listen(99)
    conn, addr = serv.accept()
    print(addr[0], "connected")
    inc = conn.recv(4096).decode('utf-8')
    print('its', inc)
    while True:
        inc = "noshit"
        inc = conn.recv(4096).decode('utf-8')
        if inc != "noshit":
            print(inc)
    return()


servcess()
