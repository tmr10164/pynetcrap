import socket
import socketserver
device = socket.gethostname()
print(device)
ip = input("ip")


def clientcess():
    out = 0
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
    return()


clientcess()
