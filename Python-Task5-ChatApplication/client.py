
import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((HOST, PORT))

username = input("Enter your username: ").strip()

# Send username to server
client.recv(1024)
client.send(username.encode("utf-8"))


# Receive messages from server
def receive_messages():
    while True:
        try:
            message = client.recv(1024)

            if not message:
                print("Disconnected from server.")
                break

            print("\n" + message.decode("utf-8"))

        except:
            print("Connection closed.")
            break

    client.close()


# Send messages to server
def send_messages():
    while True:
        try:
            message = input()

            if message.lower() == "exit":
                print("Leaving chat...")
                client.close()
                break

            if message.strip():
                client.send(message.encode("utf-8"))

        except:
            print("Unable to send message.")
            break


# Start receiving messages in a separate thread
receive_thread = threading.Thread(
    target=receive_messages,
    daemon=True
)
receive_thread.start()

print(f"Welcome {username}! Start chatting.")
print("Type 'exit' to leave the chat.")

send_messages()
