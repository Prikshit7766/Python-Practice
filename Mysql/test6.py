import mysql.connector as conn

mydb =conn.connect(host="localhost",user="root",passwd="Prikshit@12")

cursor= mydb.cursor()

cursor.execute("select * from prikshit.bank_details where age=41 ")
for i in cursor.fetchall():
    print(i)

cursor.execute("select * from prikshit.bank_details ")
for i in cursor.fetchall():
    print(i)

cursor.execute("select age,`default` from prikshit.bank_details ")
for i in cursor.fetchall():
    print(i)


