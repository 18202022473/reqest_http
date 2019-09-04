import pymysql

from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(

    ssh_address_or_host=('175.126.163.12', 22),  # 指定ssh登录的跳转机的address(ssh通道)

    ssh_username='root',  # 跳转机的用户

    ssh_password='GversJIG178@,./1',  # 跳转机的密码

    remote_bind_address=('175.126.163.12', 3306)

)

server.start()

db = pymysql.connect(

    host='127.0.0.1',

    port=server.local_bind_port,

    user='root',

    passwd='.j6xMag2,;BX',

    db='db_exchange_etex'

)

cur = db.cursor()

cur.execute('select * from t_user limit 1')

data = cur.fetchall()

print(data)

db.close()

server.close()
