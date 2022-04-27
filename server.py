import socket
import threading

port=8000
host=socket.gethostname()
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print('[SEARCHING]........')

while True:
    conn,addr=server.accept()
    print(f'[CONNECTION ESTABLISHED].....{addr}')
    data=conn.recv(1028)
    print(data.decode())
    while data:

        msg=input('msg>').encode()
        conn.send(msg)
        data=conn.recv(1028).decode()
        print(data)
            
        
        
    conn.close()
