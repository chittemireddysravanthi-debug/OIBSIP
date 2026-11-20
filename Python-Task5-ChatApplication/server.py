
import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

clients = []
usernames = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

print("Chat server is running...")
print("Waiting for users to connect...")


def broadcast(message, sender=None):
    for client in clients[:]:
        if client != sender:
            try:
                client.send(message)
            except:
                remove_client(client)


def remove_client(client):
    if client in clients:
        index = clients.index(client)
        username = usernames[index]

        clients.remove(client)
        usernames.pop(index)

        client.close()

        print(f"{username} disconnected.")

        broadcast(f"{username} left the chat.".encode("utf-8"))


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            timestamp = datetime.now().strftime("%H:%M:%S")
            formatted_message = (
                f"[{timestamp}] {message.decode('utf-8')}"
            )

            print(formatted_message)
            broadcast(formatted_message.encode("utf-8"), client)

        except:
            break

    remove_client(client)


def receive_connections():
    while True:
        try:
            client, address = server.accept()

            client.send("USERNAME".encode("utf-8"))
            username = client.recv(1024).decode("utf-8").strip()

            if not username:
                client.close()
                continue

            clients.append(client)
            usernames.append(username)

            print(f"{username} connected from {address}")

            broadcast(f"{username} joined the chat.".encode("utf-8"))

            thread = threading.Thread(
                target=handle_client,
                args=(client,),
                daemon=True
            )
            thread.start()

        except OSError:
            break


try:
    receive_connections()
except KeyboardInterrupt:
    print("\nServer shutting down...")
finally:
    for client in clients[:]:
        client.close()
    server.close()
