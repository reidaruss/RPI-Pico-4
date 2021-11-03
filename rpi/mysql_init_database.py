import mysql.connector as mysqlConnector
conn = mysqlConnector.connect(host='localhost',user='root',passwd='root')
if conn:
    print("Connection Successful :)")
else:
    print("Connection Failed :(")
cur = conn.cursor()
try:
    cur.execute("create database pico")
    print("Query Executed Successfully !!!")
except Exception as e:
    print("Invalid Query")
    print(e)
conn.close()


# import mysql.connector as mysqlConnector
# conn = mysqlConnector.connect(host='localhost',user='root',passwd='root',database='pico')
# if conn:print("Connection Successful :)")
# else:print("Connection Failed :(")
# cur = conn.cursor()
# try:
#     cur.execute("create table measurements (temp double(3,1), humidity double(3,1),soil_moisture double(3,1), time datetime)")
#     print("Query Executed Successfully !!!")
# except Exception as e:
#     print("Invalid Query")
#     print(e)
# conn.close()