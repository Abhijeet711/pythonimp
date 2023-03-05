import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database = 'pydb',user='root',password='')

    cursor = connection.cursor()
    mysql_query = "INSERT INTO laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)"
    tuple1 = (1, 'Dell', 21000, '21-JAN-2022')
    tuple2 = (2, 'hp', 26000, '9-JAN-2023')
    cursor.execute(mysql_query, tuple1)
    cursor.execute(mysql_query, tuple2)
    connection.commit()

    print(cursor.rowcount, "record inserted.")

    cursor.execute("SELECT * FROM laptop")
    myresult = cursor.fetchall()

    for x in myresult:
    	print(x)
    
except mysql.connector.Error as error:
    print("failed to insert record in mysql:{}",format(error))
finally:
    if connection.is_connected():
   	 cursor.close()
   	 connection.close()
