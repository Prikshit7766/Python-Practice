import mysql.connector as conn
# cnn is alias
# now we have to establish the communication between mypython and mysql

mydb =conn.connect(host="localhost",user="root",passwd="Prikshit@12") # to establish a communication
#print(mydb)

#connection is estalish
cursor= mydb.cursor()
# cursor is just like a pointer which goes to tables one by one and perform read and write operation
#cursor.execute("create database Prikshit")
#cursor.execute("show databases")
s=cursor.execute("create table Prikshit.ineuron1(emp_id int(10),emp_name varchar(40),emp_mailid varchar(30), emp_salary int(6), emp_attendence int(3))")
q1=cursor.execute(s)

q2= cursor.execute("select * from Prikshit.ineuron1")
print(q2)

#returning the list of databases







