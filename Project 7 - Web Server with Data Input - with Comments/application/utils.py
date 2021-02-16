def create_http_response(status, response_body):
    """生成完整HTTP响应报文"""
    response_start_line = "HTTP/1.1 %s\r\n" % status
    # 生成HTTP响应报文起始行
    response_headers = "Server: My Server\r\n"
    # 生成HTTP响应报文响应头
    response = bytes(response_start_line + response_headers + '\r\n', 'utf-8') + response_body
    # 组合HTTP响应报文起始行、响应头及响应体并生成完整HTTP响应报文
    return response
    # 返回HTTP响应体
