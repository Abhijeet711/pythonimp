import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database = 'pydb',user='root',password='')
    cursor = connection.cursor()
    mysql_query = "DELETE from laptop where Id=%s"
    tuple1 = (1,)
    cursor.execute(mysql_query, tuple1)
    connection.commit()
    print(cursor.rowcount, "record deleted.")
    cursor.execute("SELECT * FROM Laptop")
    myresult = cursor.fetchall()
    for x in myresult:
    		print(x)

except mysql.connector.Error as error:
    print("failed to delete record in mysql:{}",format(error))
finally:
    if connection.is_connected():
   	 cursor.close()
   	 connection.close()
   	 print("mysql connection closed")
