# -*- coding:utf-8 -*-
# tcp服务器搭建
import socket
from application import app, uploaded_data_operation
from multiprocessing import Process
import binascii


class WebServer(object):
    """定义Web服务器类"""

    def __init__(self):
        """初始化函数"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 创建套接字
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 设置套接字地址复用开启，避免端口占用
        HOST = ''
        # 设置服务器端IP地址为本地IP地址
        PORT = 5001
        # 设置服务器端端口
        server_socket.bind((HOST, PORT))
        # 绑定套接字到本地IP与端口
        server_socket.listen(128)
        # 开启监听
        self.server_socket = server_socket
        # 实例化对象，对象实例化后，类下的所有方法，都可以调用实例对象

    def start(self):
        """启动服务器"""
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s] connected" % client_address)
            # 接收客户端套接字和地址信息并打印
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            # 创建子进程，执行该类下handle_client()函数，传递参数
            handle_client_process.start()
            # 开启子进程
            client_socket.close()
            # 关闭客户端套接字

    def handle_client(self, client_socket):
        """客户端套接字处理"""
        request_data = client_socket.recv(1024)
        # 请求数据接收
        try:
            request_data_bin = str(request_data, 'utf-8')
            # 尝试将请求数据以'utf-8'编码解析为字符串
            # 解析成功说明请求来自客户端移动设备浏览器的HTTP请求，为短连接
            # 解析失败说明请求来自DTU的上传数据的TCP请求，为长连接

        except UnicodeDecodeError:
            # 解析失败说明请求来自DTU的上传数据的TCP请求
            client_socket_persistent = client_socket
            # 拷贝客户端套接字
            request_data_persistent = request_data
            # 拷贝客户端请求数据
            request_data_hex = str(binascii.hexlify(request_data_persistent), 'utf-8')
            print('request_data_hex is: ', request_data_hex)
            # 将客户端请求数据进行16进制转码后以'utf-8'编码解析为字符串并打印
            if len(request_data_hex) == 20 or len(request_data_hex) == 24:
                # 判断接收报文长度是否为20位（标准帧）或24位（扩展帧）
                uploaded_data_operation.data_operation(request_data_hex)
                # 将解析后的字符串送入data_operation()分离帧ID与数据信息并进行解析
            client_socket_persistent.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
            # 保持长连接
            while True:
                request_data_persistent = client_socket_persistent.recv(1024)
                # 长连接，为同一客户端套接字接收请求数据
                request_data_hex = str(binascii.hexlify(request_data_persistent), 'utf-8')
                print('request_data_hex is: ', request_data_hex)
                # 将客户端请求数据进行16进制转码后以'utf-8'编码解析为字符串并打印
                if len(request_data_hex) % 20 == 0:
                    # 判断客户端请求数据是否符合规则
                    for i in range(0, len(request_data_hex), 20):
                        print(request_data_hex[i:i + 20])
                        # 将符合规则的客户端请求数据拆分为多个CAN报文字符串并打印
                        uploaded_data_operation.data_operation(request_data_hex[i:i + 20])
                        # 将拆分后的CAN报文字符串送入data_operation()分离帧ID与数据信息并进行解析

        else:
            # 解析成功说明请求来自客户端移动设备浏览器的HTTP请求，为短连接
            print('request_data_bin is: ', request_data_bin)
            # 打印接收数据
            response = app.application(request_data)
            print("response data: ", response)
            # 将接收数据送入application()进行方法与地址解析，生成HTTP响应报文并打印
            client_socket.send(response)
            # 将HTTP响应报文发送给客户端
            client_socket.close()
            # 关闭客户端连接


def main():
    ws = WebServer()
    # 创建服务器类变量
    ws.start()
    # 开启服务器


if __name__ == '__main__':
    main()
    # 执行主函数
