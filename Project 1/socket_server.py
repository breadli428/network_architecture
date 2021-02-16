import socket
import binascii

HOST = ''
PORT = 5001
reply = 'test received'
reply = str.encode(reply)

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind((HOST, PORT))

so.listen(128)

# persistent connection
# conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)

while True:
    conn, addr = so.accept()
    print('connected by: ', addr)
    request_data = conn.recv(1024)
    try:
        request_data_bin = str(request_data, 'utf-8')

    except UnicodeDecodeError as error:
        conn_long = conn
        request_data_long = request_data
        request_data_hex = str(binascii.hexlify(request_data_long), 'utf-8')
        print('request_data_hex is: ', request_data_hex)
        conn_long.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        while True:
            request_data_long = conn_long.recv(1024)
            request_data_hex = str(binascii.hexlify(request_data_long), 'utf-8')
            print('request_data_hex is: ', request_data_hex)

        print('main_test')
    else:
        print('request_data_bin is: ', request_data_bin)
        print('rest')
        conn.sendall(reply)
        conn.close()

    # if request_data_bin[0:3] == 'GET':
    #     print('rest')
    #     conn.sendall(reply)
    #     conn.close()
    # else:
    #     conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
    #     print('main_test')
