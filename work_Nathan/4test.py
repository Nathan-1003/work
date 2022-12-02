import json
import re
import pymysql  #pip3 install PyMySQL ,pip install mysql-connector-python
import flask
import datetime

db = pymysql.connect(host='34.142.180.39',
                     port=13306,
                     user='root',
                     passwd='oh_my_ody!',
                     db = 'data_center',
                     charset='utf8')
#def test_select_channel():

#sql_cmd = 'SELECT channel_id FROM data_center.channel GROUP BY channel_id ORDER BY channel_id'
sql_cmd = 'SELECT * FROM data_center.channel LIMIT 5 '
cur=db.cursor()
cur.execute(sql_cmd)
result = cur.fetchall()
print(result)
print(cur.description)
print()
for row in cur:
    print(row)

cur.close()



# for row in result:
#     uuid = row[0]
#     channel_id = row[1]
#     channel_name = row[2]
#     open_channel_id = row[3]
#     hosting_channel = row[4]
#     creat_at = row[5]
#     update_at = row[6]
#     date_time = row[7]
db.close()



#print(type(result))
#str_result = ''.join(str(result)) #轉換字串 將result tupl轉為str
#print(str_result)

# app = flask.Flask(__name__)
# @app.route("/")
#
# def hello():
#     return(str_result)
#
# if __name__ == '__main__':
#     app.run()








