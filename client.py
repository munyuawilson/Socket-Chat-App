import socket

port=8000

host=socket.gethostname()

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect((host,port))

print('[CONNECTED]')



msg=input('send>>>')

server.send(msg.encode())
data=server.recv(1028).decode()
print(data)

while data:
    
        msg=input('send>>>').encode()
        server.send(msg)
        data=server.recv(1028).decode()
        print(data)
        
    
