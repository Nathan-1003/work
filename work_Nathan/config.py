DIALECT='mysql'
DRIVER='mysqldb'
USERNAME='root'
PASSWORD='oh_my_ody'
HOST='34.142.180.39'
PORT='13306'
DATABASE='data_center'

SQLALCHEMY_DATABASE_URI='{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
