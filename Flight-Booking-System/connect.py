import mysql.connector
conn=mysql.connector.connect(host='localhost',password='siddhant@3101',user='root')

if conn.is_connected():
    print("connection established")
