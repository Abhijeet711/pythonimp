import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and successfully connected to Sqlite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("Sqlite Database Version is: ",record)
    cursor.close()

except sqlite3.Error as error:
	print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
    	sqliteConnection.close()
    	print("The Sqlite connection is closed")
