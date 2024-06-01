import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
machine = socket.gethostbyname(socket.gethostname())
port = 9999
print("Socket Created")

server.bind((machine, port))

server.listen( )


def sender():
    print(f"[{machine}]waiting for a connection")
    while True:
        client, address = server.accept()
        file = open("file.txt", 'rb')
        data = file.read(1024)
        while True:
            if data:
                print("sending data")
                client.send(data)
                data = file.read(1024)
                print("data sent")
                break
            else:
                print("failed to send data")
                break


sender()
