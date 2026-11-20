# Real-Time Chat Application using Python

## Project Description
A real-time chat application developed using Python socket programming and multithreading. It allows multiple users to connect to a central server and exchange messages.

## Features
- Multiple users can connect to the server.
- Real-time message sending and receiving.
- Username identification.
- Message timestamps.
- Broadcast messages to connected users.
- Graceful client disconnection.

## Technologies Used
- Python
- Socket Programming
- Threading
- DateTime

## Project Structure

```text
Python-Task5-ChatApplication/
├── server.py
├── client.py
└── README.md
```

## How to Run

### 1. Start the server

```bash
py server.py
```

### 2. Start the first client in another terminal

```bash
py client.py
```

Enter a username when prompted.

### 3. Start another client

Open a third terminal and run:

```bash
py client.py
```

Enter another username to join the conversation.

### 4. Leave the chat

Type `exit` to disconnect.

## Developer
Sravanthi Chittemreddy

## Internship
Oasis Infobyte – Python Programming Internship
