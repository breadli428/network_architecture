import re
HTML_ROOT_DIR = './html'

def parse_request(request_data):
    request_data = str(request_data, 'utf-8')
    print("request data:", request_data)

    request_method = re.search(r'(\w+) ', request_data).group(1)
    print("request method is", request_method)

    request_path = re.search(r'(/.*) ', request_data).group(1)
    if request_path == '/':
        request_path = '/index.html'

    print("request path is", request_path)
    file_path = HTML_ROOT_DIR + request_path
    return file_path


def application(request_data):
    file_path = parse_request(request_data)
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
    return response
