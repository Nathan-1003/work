import pymysql  #pip3 install PyMySQL ,pip install mysql-connector-python
import flask

db = pymysql.connect(host='34.142.180.39',
                     port=13306,
                     user='root',
                     passwd='oh_my_ody!',
                     db = 'data_center',
                     charset='utf8')

#def test_select_channel():

sql_cmd = 'SELECT * FROM channel WHERE uuid="1_default" '

cur=db.cursor()

cur.execute(sql_cmd)

result = cur.fetchall()

print(result)

#print(type(result)) 確認type

str_result = ''.join(str(result).strip()) #轉換字串 將result tuple轉為str


app = flask.Flask(__name__)
@app.route("/")

def hello():
    return(str_result)

if __name__ == '__main__':
    app.run()


