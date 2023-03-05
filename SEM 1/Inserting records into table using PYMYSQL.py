import pymysql as pm
db=pm.connect(host='localhost',database='pydb',user='root',password='')
cur=db.cursor()
try:
    cur.execute("select * from laptop")
    for row in cur.fetchone():
        print(row)
except:
    print("Error: unable to fetch data.")
finally:
    db.close()
