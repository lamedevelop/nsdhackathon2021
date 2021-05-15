import requests


f = open("../test.txt", 'rb')
files = {"file": (f.name, f, "multipart/form-data")}
requests.post(url="http://127.0.0.1:8000/api/send", files=files)
f.close()
