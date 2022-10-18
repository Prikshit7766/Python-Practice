from flask import Flask,request, jsonify
import mysql.connector as conn

app = Flask(__name__)

@app.route("/testsql")
def test_sql():
    database_name=request.args.get("database")
    table_name=request.args.get("table")
    try:
        mydb = conn.connect(host="localhost", user="root", passwd="1234", database=database_name)
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(f"select * from {table_name}")
        l=[]
        data= cursor.fetchall()
        mydb.commit()
        mydb.close()
    except Exception as e:
        return  jsonify(str(e))


    return  (data)


if __name__ =='__main__':
    app.run(port=8000)


# not secure
# http://127.0.0.1:8000/testsql?database=tasksql&table=mytable