import mysql.connector as conn

mydb =conn.connect(host="localhost",user="root",passwd="Prikshit@12")

cursor= mydb.cursor()

cursor.execute("select emp_id,emp_mailid from   Prikshit.ineuron1")
l=[]
for i in cursor.fetchall():

    l.append(i)

print(l)
print(type(l[0]))

