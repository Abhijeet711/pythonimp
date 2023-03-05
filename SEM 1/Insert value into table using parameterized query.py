import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database = 'pydb',user='root',password='')

    cursor = connection.cursor()
    mysql_query = "INSERT INTO Laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)"
    val = (1, 'Dell', 21000, '21-JAN-2022')
    cursor.execute(mysql_query, val)    

    print(cursor.rowcount, "record inserted.")

    cursor.execute("SELECT * FROM Laptop")
    myresult = cursor.fetchall()

    for x in myresult:
    	print(x)
    
except mysql.connector.Error as error:
    print("failed to insert record in mysql:{}",format(error))
finally:
    if connection.is_connected():
   	 cursor.close()
   	 connection.close()
