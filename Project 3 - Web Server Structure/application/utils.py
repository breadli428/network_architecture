def create_http_response(status, response_body):
    response_start_line = "HTTP/1.1 %s\r\n" % status
    response_headers = "Server: My Server\r\n"
    response = bytes(response_start_line + response_headers + '\r\n', 'utf-8') + response_body
    return response
