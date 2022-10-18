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

    t = json.loads(r.text)#定義token取用

    token = t["token"]

    print(token)

    url = ' http://8.219.83.66:8088/admin/v2/system/dict/data/channels'

    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }

    data = '{"pageNum":"1","pagesize":"10000"}'

    r = requests.post(url, headers=headers, data=data)

    print(r.text)


if __name__== '__main__':
    test_logging()

