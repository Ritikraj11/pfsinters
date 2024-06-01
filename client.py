import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
machine = socket.gethostbyname(socket.gethostname())
port = 9999

client.connect((machine, port))


def receiver():
    while True:
        print("Recieving the file from server")
        data = client .recv(1024)
        print("creating the file where to save")
        with open("file.txt", 'wb') as f:
            f.write(data)
            print("data has been recieved")
            break


receiver()
