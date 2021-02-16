import socket


HOST = '127.0.0.1'
PORT = 8000
request = 'Can you hear me?'
request = str.encode(request)

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.connect((HOST, PORT))


so.sendall(request)
reply = so.recv(1024)

print('reply is: ', reply)

so.close()
