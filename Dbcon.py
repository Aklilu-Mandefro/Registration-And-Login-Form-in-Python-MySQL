import pymysql

dbConfig = {
     'user': 'root',  # use your admin name
     'password': "",  # use your admin password
     'host': '127.0.0.1',  # IP address of localhost
     'database': 'adlogin', # your databse
}

conn = pymysql.connect(**dbConfig)
print(conn)