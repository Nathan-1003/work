import requests
import json

url = 'http://8.219.83.66:8088/admin/v2/login'
headers = {
    "Content-Type": "application/json"
}
data = '{"username":"admin","password":"1234"}'
r = requests.post(url, headers=headers, data=data)
#print(r.text) #成功登入
t = json.loads(r.text)#定義token取用
token = t["token"]
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
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    r = requests.post(url, headers=headers, data=data)
    #print(r.text)
    if r.json== 0:
        print("")

def newRegCount():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/newRegCount/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)

def firstDayPayRate():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/firstDayPayRate/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)

def agentData():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/agentData/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)

def gameData():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/gameData/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)

def podcastDiamond():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/podcastDiamond/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)

def diamondConsumption():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/diamondConsumption/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)

def businessReport():#經營報表
    url = ' http://8.219.83.66:8088/admin/dataCenter/businessReport/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","endTime":"1668700799999","isAsc":"ASC","openChannelId":"","orderByColumn":"channel_id","pageNum":" 1","pageSize":"20"}'

    r = requests.post(url, headers=headers, data=data)

    print(r.text)

def dailyReport():#日報表
    url = ' http://8.219.83.66:8088/admin/dataCenter/dailyReport/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"","currency":"","device":"","endTime":"1668700799999","openChannelId":""}'

    r = requests.post(url, headers=headers, data=data)

    print(r.text)

def gameBet():#遊戲注單列表
    url = ' http://8.219.83.66:8088/admin/dataCenter/gameBet/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"null","currency":"null","endTime":"1668700799999","gameType":"null","openChannelId":"","pageNum":"1","pageSize":"1000","pid":"null"}'

    r = requests.post(url, headers=headers, data=data)

    print(r.text)

def gameBetDetail():#遊戲數據列表
    url = 'http://8.219.83.66:8088/admin/dataCenter/gameBetDetail/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = '{"beginTime":"1668614400000","channelId":"null","country":"cn","currency":"null","endTime":"1668700799999","openChannelId":"null","pageNum":"1","pageSize":"20","param":"null","pid":"null"}'

    r = requests.post(url, headers=headers, data=data)

    print(r.text)



if __name__== '__main__':
    #channels()
    #businessReport()
    #dailyReport()
    rechargeCashoutDiff()
    # newRegCount()
    # firstDayPayRate()
    # agentData()
    # gameData()
    # podcastDiamond()
    # diamondConsumption()
