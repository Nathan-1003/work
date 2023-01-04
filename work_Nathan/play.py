import json
import requests



url = 'http://34.142.180.39:17001/qcie-admin-sit/login'

headers = {'Content-Type': 'application/json'}

data = '{"username":"admin","password":"1234","code":"666666"}'

r = requests.post(url, headers=headers, data=data,)

t = json.loads(r.text)

print(t)



# url = 'http://34.142.180.39:17001/qcie-admin-sit/paymentLayer/list'
#
# headers = {'Content-Type': 'application/json','Authorization':'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImZkMzE5N2IyLWIzMDYtNDcxNi05MGMxLTg4YmYxYTg1NTUxMyJ9.yY7gqL1zFxycis8pTgFjYEIVYVienY5KmB983KDYenMLtZmX4-xFm4Dlc8o1RWXP_0jVc9fpz1hJSjSaMBgAuA'}
#
# data = '{"channel_id":''}'
#
# r = requests.post(url, headers=headers, data=data,)
#
# t = json.loads(r.text)
#
# print(t)
