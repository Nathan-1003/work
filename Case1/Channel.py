import requests
import json


def test_logging():
    url = 'http://8.219.83.66:8088/admin/v2/login'

    headers = {
        "Content-Type": "application/json"
    }
    data = '{"username":"admin","password":"1234"}'

    r = requests.post(url, headers=headers, data=data)

    #print(r.text) #成功登入


    url = ' http://8.219.83.66:8088/admin/v2/system/dict/data/channels'


    headers = {
        "Content-Type": "application/json",
        "Authorization":
        "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY3MTdhZjEwLTBkODEtNDJjZS1hODZjLTFhM2NmODY0MzM5MyJ9.6AOYAmk6B3bge3h0oeGppqz3r6P8y2Ql7aUv5QDE7F3NJvfB_4NYj3-Lr7DMaS0ic6ISpIBaN5nSAW-_GQpi8Q"
    }

    data = {"pageNum":"1","pagesize":"10000"}

    r = requests.post(url, headers=headers, data=data)

    print(r.json)


if __name__== '__main__':
    test_logging()