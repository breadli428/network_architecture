# -*- coding:utf-8 -*-
# tcp socket server
import socket
import re

from multiprocessing import Process


def handle_client(client_socket):
    request_data = client_socket.recv(1024)
    request_data = str(request_data, 'utf-8')
    request_method = re.search(r'(\w+) ', request_data).group(1)
    request_path = re.search(r'(/.*) ', request_data).group(1)
    print("request method is", request_method)
    print("request path is", request_path)
    print("request data:", request_data)
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My Server\r\n"
    response_body = "hello world!"
    response = response_start_line + response_headers + '\r\n' + response_body
    print("response data: ", response)

    client_socket.send(bytes(response, 'utf-8'))

    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = ''
    PORT = 8000
    server_socket.bind((HOST, PORT))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s] connected" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()


if __name__ == '__main__':
    main()
