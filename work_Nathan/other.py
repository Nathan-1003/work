import requests
import json
import numpy as np
import time
import datetime;

today = datetime.date.today()
date_begintime_stamp=int(time.mktime(today.timetuple())) - 86400
date_begintime_stamp=date_begintime_stamp*1000
date_endtime_stamp=(date_begintime_stamp+86399*1000+999)
#print(date_begintime_stamp)#1668960000000
#print(date_endtime_stamp)#1669046399999

url = 'http://8.219.83.66:8088/admin/v2/login'
headers = {
    "Content-Type": "application/json"
}
data = '{"username":"admin","password":"1234"}'
r = requests.post(url, headers=headers, data=data)
#print(r.text) #成功登入
t = json.loads(r.text)#定義token取用
token = t["token"] #response提取的token使用
#print(token)

def channels():#總表
    url = ' http://8.219.83.66:8088/admin/v2/system/dict/data/channels'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"pageNum":"1","pagesize":"10000"}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)

def rechargeCashoutDiff():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/rechargeCashoutDiff/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    #data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    data = {'beginTime': date_begintime_stamp,#1668960000000
            'channelId': '',
            'currency': '',
            'device':'',
            'endTime': date_endtime_stamp,#1669046399999
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    #print(_data)
    print(r)
    response = r.json()  # 轉json
    #print(response)
    if response["data"]["rechargeCashoutDiff"] == 0:
        print("rechargeCashoutDiff_Error")
    if response["data"]["activityDetailCount"] == 0:
        print("activityDetailCount_Error")
    if response["data"]["activityMoney"] == 0:
        print("activityMoney_Error")
    if response["data"]["activityUserCount"] == 0:
        print("activityUserCount_Error")
    if response["data"]["cashout"] == 0:
        print("cashout_Error")
    if response["data"]["cashoutCount"] == 0:
        print("cashoutCount_Error")
    if response["data"]["cashoutUsers"] == 0:
        print("cashoutUsers_Error")
    if response["data"]["manualRechargeGift"] == 0:
        print("manualRechargeGift_Error")
    if response["data"]["manualRechargeGiftCount"] == 0:
        print("manualRechargeGiftCount_Error")
    if response["data"]["onlineRecharge"] == 0:
        print("onlineRecharge_Error")
    if response["data"]["onlineRechargeCount"] == 0:
        print("onlineRechargeCount_Error")
    if response["data"]["onlineRechargeUsers"] == 0:
        print("onlineRechargeUsers_Error")

if __name__== '__main__':
    rechargeCashoutDiff()

