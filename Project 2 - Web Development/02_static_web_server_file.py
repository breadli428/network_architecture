# -*- coding:utf-8 -*-
# tcp socket server
import socket
import re

from multiprocessing import Process

HTML_ROOT_DIR = './html'


def handle_client(client_socket):
    request_data = client_socket.recv(1024)
    request_data = str(request_data, 'utf-8')
    print("request data:", request_data)

    request_method = re.search(r'(\w+) ', request_data).group(1)
    print("request method is", request_method)

    request_path = re.search(r'(/.*) ', request_data).group(1)
    if request_path == '/':
        request_path = '/index.html'

    print("request path is", request_path)
    file_path = HTML_ROOT_DIR + request_path
    try:
        file = open(file_path, 'rb')
    except IOError as error:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: My Server\r\n"
        response_body = "Error! %s\n" % error
        response_body = bytes(response_body, 'utf-8')
    else:
        file_data = file.read()
        file.close()

        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My Server\r\n"
        response_body = file_data

    response = bytes(response_start_line + response_headers + '\r\n', 'utf-8') + response_body
    print("response data: ", response)

    client_socket.send(response)

    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
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
