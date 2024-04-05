from socket import *

def main():
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print("Connected to the server at", serverName, serverPort)

    clientSocket.settimeout(10)  # 10-second timeout

    try:
        while True:
            message = input('Input lowercase sentence (quit to exit): ')
            if message == "quit":
                break
            clientSocket.send(message.encode())
            modifiedMessage = clientSocket.recv(2048)
            print("From server:", modifiedMessage.decode())
    except timeout:
        print("Server timeout")
    except KeyboardInterrupt:
        print("Interrupted by the user")

    print("Closing connection")
    clientSocket.close()

if __name__ == "__main__":
    main()
