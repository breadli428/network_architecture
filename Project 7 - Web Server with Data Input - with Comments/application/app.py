import re
from application import utils
HTML_ROOT_DIR = './html/webpage'
# 根目录


def parse_request(request_data):
    """获取请求数据目标路径"""
    request_data = str(request_data, 'utf-8')
    print("request data:", request_data)
    # 将请求数据以'utf-8'编码解析为字符串并打印

    request_method = re.search(r'(\w+) ', request_data).group(1)
    print("request method is", request_method)
    # 利用正则表达式提取其中方法文本并打印

    request_path = re.search(r'(/.*) ', request_data).group(1)
    # 利用正则表达式提取其中目标路径文本
    if request_path == '/':
        request_path = '/index.html'
        # 若请求目标路径为根目录则转至根目录下index.html

    print("request path is", request_path)
    # 打印目标路径
    file_path = HTML_ROOT_DIR + request_path
    # 在目标路径中补充根目录，生成完整目标路径
    return file_path
    # 返回完整目标路径


def application(request_data):
    """解析方法与访问地址并生成HTTP响应报文"""
    file_path = parse_request(request_data)
    # 将请求数据送入parse_request()获取完整目标路径
    try:
        file = open(file_path, 'rb')
        # 尝试在目标路径下打开对象文件
    except IOError as error:
        # 打开文件失败
        response_body = "Error! %s\n" % error
        # 生成HTTP响应体并包含错误代码
        response_body = bytes(response_body, 'utf-8')
        # 将HTTP响应体编码为bytes类型
        response = utils.create_http_response('404 Not Found', response_body)
        # 将HTTP响应体（错误响应）送入create_http_response()生成完整HTTP响应报文

    else:
        # 打开文件成功
        file_data = file.read()
        # 读取文件内容
        file.close()
        # 关闭文件
        response_body = file_data
        # 用读取的文件内容作为HTTP响应体
        response = utils.create_http_response('200 OK', response_body)
        # 将HTTP响应体（成功响应）送入create_http_response()生成完整HTTP响应报文

    return response
    # 返回HTTP响应体
