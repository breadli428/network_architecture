# -*- coding:utf-8 -*-
# tcp socket server
import socket
from application import app
from multiprocessing import Process


class WebServer(object):

    def __init__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        HOST = ''
        PORT = 8000
        server_socket.bind((HOST, PORT))
        server_socket.listen(128)
        self.server_socket = server_socket

    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s] connected" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024)
        response = app.application(request_data)
        print("response data: ", response)
        client_socket.send(response)
        client_socket.close()


def main():
    ws = WebServer()
    ws.start()


if __name__ == '__main__':
    main()
