
import mysql.connector as conn

mydb =conn.connect(host="localhost",user="root",passwd="Prikshit@12")

cursor= mydb.cursor()
s="insert into Prikshit.ineuron1 values(101,'prikshit','prikshit@gmail.com',100,30)"
cursor.execute(s)
mydb.commit() # assure it ... is required
cursor.execute("select * from Prikshit.ineuron1")
for i in cursor.fetchall():
    print(i)


