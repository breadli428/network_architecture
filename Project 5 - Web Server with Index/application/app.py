import re
from application import utils
HTML_ROOT_DIR = './html'


def parse_request(request_data):
    request_data = str(request_data, 'utf-8')
    print("request data:", request_data)

    request_method = re.search(r'(\w+) ', request_data).group(1)
    print("request method is", request_method)

    if request_method == 'POST':
        frame = re.search(r'(\n\d.+)+', request_data).group()
        print("frame is:", frame)
        file = open('./html/saveddata/saveddata.txt', 'a')
        file.write(frame)
        file.close()

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
        response_body = "Error! %s\n" % error
        response_body = bytes(response_body, 'utf-8')
        response = utils.create_http_response('404 Not Found', response_body)

    else:
        file_data = file.read()
        file.close()
        response_body = file_data
        response = utils.create_http_response('200 OK', response_body)

    return response
