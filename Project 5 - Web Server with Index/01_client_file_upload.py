import requests

url = 'http://127.0.0.1:8000'
files = {'file': open('./html/uploadtest/testfile.txt', 'rb')}
r = requests.post(url, files=files)
print(r.text)
