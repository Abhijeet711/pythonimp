import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host="localhost",database = 'pydb',user = 'root',password = '')
    if connection.is_connected():
    	db_info = connection.get_server_info()
    	print("connected to mysql server version",db_info)
    	cursor = connection.cursor()
    	cursor.execute("select database();")
    	record = cursor.fetchone()
    	print("You are connected to database: ",record)
except Error as e:
	print("Error While connecting to mysql",e)
finally:
    if connection.is_connected():
    	cursor.close()
    	connection.close()
    	print("Mysql connection is closed")
