from socket import *
import threading

def handle_client(connectionSocket, addr):
    try:
        while True:
            sentence = connectionSocket.recv(1024).decode()
            if sentence == "":
                print(f"Client {addr} disconnected")
                break
            print(f"From {addr}: {sentence}")
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
    except Exception as e:
        print(f"Error with client {addr}: {e}")
        connectionSocket.close()

def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print("The server is ready to receive on port", serverPort)
    
    try:
        while True:
            connectionSocket, addr = serverSocket.accept()
            print(f"Connection established with {addr}")
            threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()
    except KeyboardInterrupt:
        print("Server is shutting down...")
        serverSocket.close()

if __name__ == "__main__":
    main()
