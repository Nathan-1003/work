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

def get_charts():

    url = ' http://8.219.83.66:8088/admin/v2/system/dict/data/channels'

    #獲得token，將token定義為Authorization

    access_token = get_access_token()

    headers = {
        "Content-Type": "application/json",
        "Authorization": "access_token"
    }
    data = {"pageNum":"1","pagesize":"10000"}

    r = requests.post(url, headers=headers, data=data, Authorization=Authorization)

    print(r.text)


if __name__== '__main__':
    test_logging()