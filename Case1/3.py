import re

import pymysql  #pip3 install PyMySQL ,pip install mysql-connector-python
import HTMLTable #pip install html-table
import flask
import pandas as pd


db = pymysql.connect(host='34.142.180.39',
                     port=13306,
                     user='root',
                     passwd='oh_my_ody!',
                     db = 'data_center',
                     charset='utf8')

#def test_select_channel():

#sql_cmd = 'SELECT  COUNT(DISTINCT channel_id) FROM data_center.channel'

my_sql = db.cursor()

sql_cmd = 'SELECT channel_id FROM data_center.channel GROUP BY channel_id'

my_sql.execute(sql_cmd)

result = my_sql.fetchall()

str_result = ''.join(str(result)) #轉換字串 將result tupl轉為str

str_result = re.sub("[(,)]","",str_result) #去除(,)

print(str_result)

table = HTMLTable(test='channel')
table.append_header_rows(())



#
# app = flask.Flask(__name__)
# @app.route("/")
#
# def hello():
#     return(str_result)
#
# if __name__ == '__main__':
#     app.run()