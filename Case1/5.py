import requests
import json
import numpy as np
import time
import datetime;

today = datetime.date.today()
date_begintime_stamp=int(time.mktime(today.timetuple())) - 86400
date_begintime_stamp=date_begintime_stamp*1000
date_endtime_stamp=(date_begintime_stamp+86399*1000+999)
print(date_begintime_stamp)#1668960000000
print(date_endtime_stamp)#1669046399999

url = 'http://8.219.83.66:8088/admin/v2/login'
headers = {"Content-Type": "application/json"}
#data = '{"username":"admin","password":"1234"}'
data = {'username':'admin','password':'1234'}
data=json.dumps(data)
r = requests.post(url, headers=headers, data=data)
#print(r.text) #成功登入
t = json.loads(r.text)#抓取token
token = t["token"] #抓取token
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
    print(response)
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

def newRegCount():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/newRegCount/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime':date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime':date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    print(_data)
    print(r)
    response = r.json()  # 轉json
    print(response)
    if response["data"]["activeOnline"] == 0:
        print("activeOnline_Error")
    if response["data"]["dailyAvgAct"] == 0:
        print("dailyAvgAct_Error")
    if response["data"]["dailyAvgOnline"] == 0:
        print("dailyAvgOnline_Error")
    if response["data"]["newRegCount"] == 0:
        print("newRegCount_Error")
    if response["data"]["onlinePodcast"] == 0:
        print("onlinePodcast_Error")
    if response["data"]["onlineUser"] == 0:
        print("onlineUser_Error")
    if response["data"]["totalBindCount"] == 0:
        print("totalBindCount_Error")
    if response["data"]["totalRegCount"] == 0:
        print("totalRegCount_Error")

def firstDayPayRate():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/firstDayPayRate/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime':date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime':date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    print(_data)
    print(r)
    response = r.json()  # 轉json
    print(response)
    if response["data"]["firstDayPayRate"] == 0:
        print("firstDayPayRate_Error")
    if response["data"]["firstRecharge"] == 0:
        print("firstRecharge_Error")
    if response["data"]["firstRechargeMoney"] == 0:
        print("firstRechargeMoney_Error")
    if response["data"]["firstRechargeRate"] == 0:
        print("firstRechargeRate_Error")
    # if response["data"]["secondRecharge"] == 0:
    #     print("secondRecharge_Error")
    # if response["data"]["secondRechargeMoney"] == 0:
    #     print("secondRechargeMoney_Error")
    if response["data"]["secondRechargeRate"] == 0:
        print("secondRechargeRate_Error")

def agentData():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/agentData/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime': date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime': date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    print(_data)
    print(r)
    response = r.json()
    print(response)
    if response["data"]["agentAvailableBetNum"] == 0:
        print("agentAvailableBetNum_Error")
    if response["data"]["agentGameBonus"] == 0:
        print("agentGameBonus_Error")
    if response["data"]["agentLiveBonus"] == 0:
        print("agentLiveBonus_Error")
    if response["data"]["agentSubChannelCount"] == 0:
        print("agentSubChannelCount_Error")
    if response["data"]["agentTotalBonus"] == 0:
        print("agentTotalBonus_Error")
    if response["data"]["agentUserCount"] == 0:
        print("agentUserCount_Error")

def gameData():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/gameData/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime':date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime':date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    print(_data)
    print(r)
    response = r.json()
    print(response)
    if response["data"]["boinLotteryAvailableBetSum"] == 0:
        print("boinLotteryAvailableBetSum_Error")
    if response["data"]["boinLotteryCount"] == 0:
        print("boinLotteryCount_Error")
    if response["data"]["boinLotteryIncome"] == 0:
        print("boinLotteryIncome_Error")
    if response["data"]["boinLotteryTotalBet"] == 0:
        print("boinLotteryTotalBet_Error")
    if response["data"]["boinLotteryUserCount"] == 0:
        print("boinLotteryUserCount_Error")
    if response["data"]["cardsChessAvailableBetSum"] == 0:
        print("cardsChessAvailableBetSum_Error")
    if response["data"]["cardsChessCount"] == 0:
        print("cardsChessCount_Error")
    if response["data"]["cardsChessIncome"] == 0:
        print("cardsChessIncome_Error")
    if response["data"]["cardsChessKillRate"] == 0:
        print("cardsChessKillRate_Error")
    if response["data"]["cardsChessTotalBet"] == 0:
        print("cardsChessTotalBet_Error")
    if response["data"]["cardsChessUserCount"] == 0:
        print("cardsChessUserCount_Error")
    # if response["data"]["djAvailableBetSum"] == 0:
    #     print("djAvailableBetSum_Error")
    # if response["data"]["djCount"] == 0:
    #     print("djCount_Error")
    # if response["data"]["djIncome"] == 0:
    #     print("djIncome_Error")
    # if response["data"]["djKillRate"] == 0:
    #     print("djKillRate_Error")
    # if response["data"]["djTotalBet"] == 0:
    #     print("djTotalBet_Error")
    # if response["data"]["djUserCount"] == 0:
    #     print("djUserCount_Error")
    if response["data"]["egameAvailableBetSum"] == 0:
        print("egameAvailableBetSum_Error")
    if response["data"]["egameCount"] == 0:
        print("egameCount_Error")
    if response["data"]["egameIncome"] == 0:
        print("egameIncome_Error")
    if response["data"]["egameKillRate"] == 0:
        print("egameKillRate_Error")
    if response["data"]["egameTotalBet"] == 0:
        print("egameTotalBet_Error")
    if response["data"]["egameUserCount"] == 0:
        print("egameUserCount_Error")
    if response["data"]["fishingAvailableBetSum"] == 0:
        print("fishingAvailableBetSum_Error")
    if response["data"]["egameCount"] == 0:
        print("egameCount_Error")
    if response["data"]["egameIncome"] == 0:
        print("egameIncome_Error")
    if response["data"]["egameKillRate"] == 0:
        print("egameKillRate_Error")
    if response["data"]["egameTotalBet"] == 0:
        print("egameTotalBet_Error")
    if response["data"]["egameUserCount"] == 0:
        print("egameUserCount_Error")
    if response["data"]["fishingAvailableBetSum"] == 0:
        print("fishingAvailableBetSum_Error")
    if response["data"]["fishingCount"] == 0:
        print("fishingCount_Error")
    if response["data"]["fishingIncome"] == 0:
        print("fishingIncome_Error")
    if response["data"]["fishingKillRate"] == 0:
        print("fishingKillRate_Error")
    if response["data"]["fishingTotalBet"] == 0:
        print("fishingTotalBet_Error")
    if response["data"]["fishingUserCount"] == 0:
        print("fishingUserCount_Error")
    if response["data"]["lotteryAvailableBetSum"] == 0:
        print("lotteryAvailableBetSum_Error")
    if response["data"]["lotteryCount"] == 0:
        print("lotteryCount_Error")
    if response["data"]["lotteryIncome"] == 0:
        print("lotteryIncome_Error")
    if response["data"]["lotteryKillRate"] == 0:
        print("lotteryKillRate_Error")
    if response["data"]["lotteryTotalBet"] == 0:
        print("lotteryTotalBet_Error")
    if response["data"]["lotteryUserCount"] == 0:
        print("lotteryUserCount_Error")
    if response["data"]["realAvailableBetSum"] == 0:
        print("realAvailableBetSum_Error")
    if response["data"]["realCount"] == 0:
        print("realCount_Error")
    if response["data"]["realIncome"] == 0:
        print("realIncome_Error")
    if response["data"]["realKillRate"] == 0:
        print("realKillRate_Error")
    if response["data"]["realTotalBet"] == 0:
        print("realTotalBet_Error")
    if response["data"]["realUserCount"] == 0:
        print("realUserCount_Error")
    if response["data"]["sportAvailableBetSum"] == 0:
        print("sportAvailableBetSum_Error")
    if response["data"]["sportCount"] == 0:
        print("sportCount_Error")
    if response["data"]["sportIncome"] == 0:
        print("sportIncome_Error")
    if response["data"]["sportKillRate"] == 0:
        print("sportKillRate_Error")
    if response["data"]["sportTotalBet"] == 0:
        print("sportTotalBet_Error")
    if response["data"]["sportUserCount"] == 0:
        print("sportUserCount_Error")
    if response["data"]["totalAvailableBetSum"] == 0:
        print("totalAvailableBetSum_Error")
    if response["data"]["totalBet"] == 0:
        print("totalBet_Error")
    if response["data"]["totalBetUserCount"] == 0:
        print("totalBetUserCount_Error")
    if response["data"]["totalIncome"] == 0:
        print("totalIncome_Error")
    if response["data"]["unknownAvailableBetSum"] == 0:
        print("unknownAvailableBetSum_Error")
    if response["data"]["unknownCount"] == 0:
        print("unknownCount_Error")
    if response["data"]["unknownIncome"] == 0:
        print("unknownIncome_Error")
    if response["data"]["unknownKillRate"] == 0:
        print("unknownKillRate_Error")
    if response["data"]["unknownTotalBet"] == 0:
        print("unknownTotalBet_Error")
    if response["data"]["unknownUserCount"] == 0:
        print("unknownUserCount_Error")

def podcastDiamond():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/podcastDiamond/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime':date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime':date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    print(_data)
    print(r.text)
    response = r.json()
    print(response)
    if response["data"]["compareRechargeDiamond"] == 0:
        print("compareRechargeDiamond_Error")
    if response["data"]["firstRechargeCount"] == 0:
        print("firstRechargeCount_Error")
    if response["data"]["firstRechargeDiamond"] == 0:
        print("firstRechargeDiamond_Error")
    if response["data"]["firstRechargeValue"] == 0:
        print("firstRechargeValue_Error")
    if response["data"]["podcastTotalBet"] == 0:
        print("podcastTotalBet_Error")
    if response["data"]["rechargeDiamond"] == 0:
        print("rechargeDiamond_Error")
    if response["data"]["rechargeUserCount"] == 0:
        print("rechargeUserCount_Error")
    if response["data"]["rechargeValue"] == 0:
        print("rechargeValue_Error")
    if response["data"]["ticketForPodcast"] == 0:
        print("tticketForPodcast_Error")
    if response["data"]["useDiamond"] == 0:
        print("useDiamond_Error")

def diamondConsumption():
    url = ' http://8.219.83.66:8088/admin/dataCenter/dataSummary/diamondConsumption/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {'beginTime':date_begintime_stamp,
            'channelId':'',
            'currency':'',
            'device':'',
            'endTime':date_endtime_stamp,
            'openChannelId':''}
    _data = json.dumps(data)
    r = requests.post(url, headers=headers, data=_data)
    print(_data)
    print(r.text)
    response = r.json()
    print(response)
    if response["data"]["totalDiamond"] == 0:
        print("totalDiamond_Error")
    if response["data"]["totalUserCount"] == 0:
        print("totalUserCount_Error")

if __name__== '__main__':
    channels()
    #rechargeCashoutDiff()
    #newRegCount()
    #firstDayPayRate()
    #agentData()
    #gameData()
    #podcastDiamond()
    #diamondConsumption()
