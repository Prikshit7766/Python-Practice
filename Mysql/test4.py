
import mysql.connector as conn

mydb =conn.connect(host="localhost",user="root",passwd="1234")

cursor= mydb.cursor()
pikshit=1
s="insert into Prikshit.bank_details values(prikshit,'management','married','tertiary','no',2143,'yes','no','unknown',5,'may',261,1,-1,0,'unknown','no')"
cursor.execute(s)
mydb.commit()