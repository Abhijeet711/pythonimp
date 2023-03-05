import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database = 'pydb',user='root',password='')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Laptop")
    myresult = cursor.fetchall()
    for x in myresult:
    		print(x)
finally:
    if connection.is_connected():
   	 cursor.close()
   	 connection.close()
