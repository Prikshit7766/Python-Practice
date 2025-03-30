from flask import Flask,request, jsonify
import mysql.connector as conn

app = Flask(__name__)# it is just creating a constructor

mydb= conn.connect(host="localhost",user="root",passwd="1234")
cursor=mydb.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table if not exists tasksql.mytable(name varchar(30),number int)")

@app.route('/insert',methods=["GET", "POST"])
def insert_():
    if (request.method== "POST"):
        name= request.json["name"]
        number=request.json["number"]
        cursor.execute("insert into tasksql.mytable values (%s,%s)",(name,number))
        mydb.commit()
        return jsonify(str("done"))

@app.route('/update',methods=["GET", "POST"])
def upadte_():
    if (request.method== "POST"):
        get_name=request.json["get_name"]
        cursor.execute("update tasksql.mytable set number = number+500 where name = %s",(get_name,))
        mydb.commit()
        return jsonify(str("done"))

@app.route('/delete',methods=["GET", "POST"])
def delete_():
    if (request.method == "POST"):
        name_del =request.json["name_del"]
        cursor.execute("delete from tasksql.mytable where name =c",(name_del,))
        mydb.commit()
        return jsonify(str("done"))


@app.route('/fetch_all',methods=["GET", "POST"])
def fetch_all():
    if (request.method == "POST"):
        cursor.execute("select * from tasksql.mytable")
        l=[]
        for i in  cursor.fetchall():
            l.append(i)

        return  (l)




if __name__ =='__main__':
    app.run(port=8000)





