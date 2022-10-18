import pymysql  #pip3 install PyMySQL ,pip install mysql-connector-python
import json

db = pymysql.connect(host='34.142.180.39',
                     port=13306,
                     user='root',
                     passwd='oh_my_ody!',
                     db = 'data_center',
                     charset='utf8')

def select_version():

    cursor = db.cursor()

    sql = 'SELECT VERSION()' #下SQL

    cursor.execute("SELECT VERSION()") #確認版本

    data = cursor.fetchone()

    print (data)


def select_channel():

    cursor = db.cursor()

    sql_cmd = 'SELECT uuid FROM data_center.channel'

    cursor.execute("SELECT uuid FROM data_center.channel")

    channel = cursor.fetchone()

    print(channel)

if __name__== '__main__':
    #select_version()
    select_channel()