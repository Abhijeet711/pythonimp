import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database = 'pydb',user='root',password='')
    mysql_create_table_query = """CREATE TABLE Laptop(
    Id int(11) NOT NULL,
    Name varchar(250) NOT NULL,
    Price float NOT NULL,
    Purchase_date Date NOT NULL,
    primary key(Id))"""
    cursor = connection.cursor()
    result = cursor.execute(mysql_create_table_query)
    print("laptop table created successfully")
except mysql.connector.Error as error:
	print("failed to create table in mysql:{}",format(error))
finally:
    if connection.is_connected():
    	cursor.close()
    	connection.close()
