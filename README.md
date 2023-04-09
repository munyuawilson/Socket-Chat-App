# Socket-Chat-App
Documentation for Server.py

**Introduction:**
The server.py file is a Python script that creates a server which listens for incoming connections on a specific port number. It uses the socket library to handle network communication with clients.

**Functionality:**
The server.py script binds to a hostname and port number specified in the code, and listens for incoming connections. Once a client connects, it prints a message to the console and receives data from the client. It then enters into a loop where it sends messages to the client and receives responses until the client disconnects.

**Code breakdown:**

**import socket** : Imports the necessary socket module for network communication.

**import threading**: Imports the threading module for handling multiple clients.

**port=8000**: Sets the port number to listen on as 8000.

**host=socket.gethostname()**: Sets the hostname to the current machine's hostname.

**server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)**: Creates a socket object to establish the server connection.

**server.bind((host,port))**: Binds the server to the hostname and port specified in the code.

**server.listen(5)**: Starts listening for incoming connections with a maximum of 5 queued connections.

**print('[SEARCHING]........')**: Prints a message to the console indicating that the server is searching for incoming connections.

**while True:**: Starts an infinite loop to keep the server running continuously.

**conn,addr=server.accept()**: Accepts a client connection and assigns it to a variable 'conn' and 'addr'.

**print(f'[CONNECTION ESTABLISHED].....{addr}')**: Prints a message to the console indicating that a connection has been established with a client.

**Documentation for Client.py**

**Introduction:**
The client.py file is a Python script that establishes a connection to a server on a specific port number. It uses the socket library to handle network communication with the server.

**Functionality:**
The client.py script creates a socket object and connects it to a hostname and port number specified in the code. Once connected, it sends data to the server and receives responses. It then enters into a loop where it sends messages to the server and receives responses until the connection is closed.

**Code breakdown:**

**import socket:** Imports the necessary socket module for network communication.

**port=8000:** Sets the port number to connect to as 8000.

**host=socket.gethostname()**: Sets the hostname to the current machine's hostname.

**server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)**: Creates a socket object to establish the client connection.

**server.connect((host,port))**: Connects the client to the server using the hostname and port specified in the code.

**print('[CONNECTED]')**: Prints a message to the console indicating that the client has connected to the server.

**msg=input('send>>>')**: Prompts the user for a message to send to the server.

**server.send(msg.encode())**: Sends the encoded message to the server.

**data=server.recv(1028).decode()**: Receives a response from the server and decodes it.

**print(data)**: Prints the response received from the server.

**while data**:: Enters into a loop to send and receive messages until the connection is closed.

**msg=input('send>>>').encode()**: Prompts the user for a message to send to the server and encodes it for transmission.

**server.send(msg)**: Sends the encoded message to the server.

**data=server.recv(1028).decode()**: Receives a response from the server and decodes it.

**print(data)**: Prints the response received from the server.

**server.close()**: Closes the connection with the server.

**Conclusion:**
This client.py script demonstrates a basic client-side implementation for connecting to a server using the socket library in Python. It can be used as a starting point for building more complex client applications.

**data=conn.recv(1028)**: Receives data from the client with a buffer size of 1028 bytes.

**print(data.decode())**: Decodes and prints the data received from the client.

**while data:**: Enters into a loop to send and receive messages until the client disconnects.

**msg=input('msg>').encode(**): Prompts the user for a message to send to the client and encodes it for transmission.

**conn.send(msg)**: Sends the encoded message to the client.

**data=conn.recv(1028).decode()**: Receives a response from the client and decodes it.

**print(data)**: Prints the response received from the client.

**conn.close()**: Closes the connection with the client.

**Conclusion:**
This server.py script demonstrates a basic server-side implementation for handling client connections using the socket library in Python. It can be used as a starting point for building more complex server applications.
