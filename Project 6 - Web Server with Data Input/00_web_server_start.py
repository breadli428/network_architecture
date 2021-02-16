# -*- coding:utf-8 -*-
# tcp socket server
import socket
from application import app, uploaded_data_operation
from multiprocessing import Process
import binascii


class WebServer(object):

    def __init__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        HOST = ''
        PORT = 5001
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
        try:
            request_data_bin = str(request_data, 'utf-8')

        except UnicodeDecodeError:
            client_socket_persistent = client_socket
            request_data_persistent = request_data
            request_data_hex = str(binascii.hexlify(request_data_persistent), 'utf-8')
            print('request_data_hex is: ', request_data_hex)
            if len(request_data_hex) == 20 or len(request_data_hex) == 24:
                uploaded_data_operation.data_operation(request_data_hex)
            client_socket_persistent.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
            while True:
                request_data_persistent = client_socket_persistent.recv(1024)
                request_data_hex = str(binascii.hexlify(request_data_persistent), 'utf-8')
                print('request_data_hex is: ', request_data_hex)
                if len(request_data_hex) == 20 or len(request_data_hex) == 24:
                    uploaded_data_operation.data_operation(request_data_hex)
            print('main_test')

        else:
            print('request_data_bin is: ', request_data_bin)
            response = app.application(request_data)
            print("response data: ", response)
            client_socket.send(response)
            client_socket.close()


def main():
    ws = WebServer()
    ws.start()


if __name__ == '__main__':
    main()
