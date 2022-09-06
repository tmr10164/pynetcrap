import socket
import socketserver


def servcess():
    lastprint = 0
    serv = socket.create_server((socket.gethostbyname(socket.gethostname()), 10164))
    serv.listen(1)
    conn, addr = serv.accept()
    print(addr[0], "connected")
    inc = conn.recv(4096).decode('utf-8')
    print('its', inc)
    while inc != "/diepotato":
        inc = conn.recv(4096).decode('utf-8')
        if lastprint != inc:
            print(inc)
            lastprint = inc
        out = input("enter message:")
        if out == '/disconnect':
            print("disconnecting")
            print("disconnected")
            break
        else:
            serv.send(bytes(out, encoding='UTF-8'))
    return()


def clientcess():
    lastprint = 0
    out = 0
    ip = input("ip")
    print("connecting")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 10164))
    client.send(bytes(str(device), encoding='UTF-8'))
    print("connected")
    while out != '/disconnect':
        out = input("enter message")
        if out == '/reconnect':
            clientcess()
        elif out == '/disconnect':
            print("disconnecting")
            print("disconnected")
            break
        else:
            client.send(bytes(out, encoding='UTF-8'))
        inc = client.recv(4096).decode('utf-8')
        if lastprint != inc:
            print(inc)
            lastprint = inc
    return()


device = socket.gethostname()
print(device)
print(socket.gethostbyname(socket.gethostname()))
mode = int(input('1 to connect, 2 to create')) - 1
while (mode > 1) or (mode < 0):
    mode = int(input('1 to connect, 2 to create')) - 1
if mode == 0:
    clientcess()
else:
    servcess()
